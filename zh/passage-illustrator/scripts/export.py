"""Export reviewed source images, caption layers and a portable review package."""

import argparse
import hashlib
import html
import io
import json
import os
import re
import sys
import tempfile
import zipfile
from pathlib import Path
from typing import Any

from PIL import Image, ImageCms, ImageColor, ImageDraw, ImageFilter, ImageFont, ImageOps

PROFILE = ImageCms.ImageCmsProfile(ImageCms.createProfile("sRGB"))


def digest(data: bytes) -> str:
    """Hash the exact bytes used or delivered."""
    return hashlib.sha256(data).hexdigest()


def asset(root: Path, name: str) -> Path:
    """Resolve a relative file in the work directory."""
    path = (root / name).resolve()
    if Path(name).is_absolute() or not path.is_relative_to(root) or not path.is_file():
        raise ValueError(f"Missing or external project file: {name!r}")
    return path


def integer_pair(values: list, field: str, minimum: int) -> tuple[int, int]:
    """Read two whole numbers with a common lower bound."""
    if len(values) != 2 or any(type(n) is not int or n < minimum for n in values):
        raise ValueError(f"{field} needs two integers >= {minimum}")
    return values[0], values[1]


def load_base(raw: bytes, canvas: tuple[int, int], centering: list) -> Image.Image:
    """Orient, color-convert and fit a base in one pass."""
    if len(centering) != 2 or not all(0 <= n <= 1 for n in centering):
        raise ValueError("centering needs two fractions in [0, 1]")
    with Image.open(io.BytesIO(raw)) as original:
        image = ImageOps.exif_transpose(original)
        has_alpha = image.mode in ("RGBA", "LA", "PA") or "transparency" in image.info
        if has_alpha and image.convert("RGBA").getchannel("A").getextrema()[0] < 255:
            raise ValueError(
                "Flatten transparent artwork onto the intended background first"
            )
        embedded = image.info.get("icc_profile")
        if embedded:
            source = ImageCms.ImageCmsProfile(io.BytesIO(embedded))
            # LittleCMS needs RGB pixels for RGB profiles, including palette inputs.
            if source.profile.xcolor_space.strip() == "RGB":
                image = image.convert("RGB")
            image = ImageCms.profileToProfile(image, source, PROFILE, outputMode="RGB")
        elif image.mode == "CMYK":
            raise ValueError("CMYK artwork requires an embedded color profile")
        return ImageOps.fit(
            image.convert("RGB"),
            canvas,
            Image.Resampling.LANCZOS,
            centering=tuple(centering),
        )


def label_text(label: dict, paragraphs: dict, sources: list) -> str:
    """Resolve an editorial title or verify every fragment of a source quotation."""
    if ("text" in label) == ("quote" in label):
        raise ValueError("A label needs exactly one of text or quote")
    if "text" in label:
        value = label["text"]
    else:
        fragments = []
        cursor = (-1, 0)
        for part in label["quote"]:
            key, fragment = part["source"], part["text"]
            if key not in sources or not isinstance(fragment, str) or not fragment:
                raise ValueError(f"Invalid quotation fragment for {key!r}")
            index = sources.index(key)
            start = paragraphs[key].find(
                fragment, cursor[1] if index == cursor[0] else 0
            )
            if index < cursor[0] or start < 0:
                raise ValueError(
                    f"Quotation not found in reading order in {key}: {fragment!r}"
                )
            cursor = (index, start + len(fragment))
            fragments.append(fragment)
        value = "…".join(fragments)
    if not isinstance(value, str) or not value.strip():
        raise ValueError("Empty label")
    return value


def draw_label(
    layer: Image.Image, text: str, label: dict, font: ImageFont.FreeTypeFont
) -> None:
    """Lay out one block and reject clipped or overlapping label rectangles."""
    x, y = integer_pair(label["xy"], "xy", 0)
    direction = label.get("direction", "horizontal")
    draw = ImageDraw.Draw(layer)
    if direction == "vertical":
        step = label.get("step", font.size + 2)
        if "\n" in text or type(step) is not int or step <= 0:
            raise ValueError("Use a positive step and one column per vertical label")
        parts = [((x, y + i * step), char) for i, char in enumerate(text)]
    elif direction == "horizontal":
        parts = [((x, y), text)]
    else:
        raise ValueError(f"Unknown label direction: {direction}")
    # Horizontal multiline layout uses Pillow's own baseline and spacing.
    bounds = [draw.multiline_textbbox(pos, part, font=font) for pos, part in parts]
    box = (
        min(b[0] for b in bounds),
        min(b[1] for b in bounds),
        max(b[2] for b in bounds),
        max(b[3] for b in bounds),
    )
    if box[0] < 0 or box[1] < 0 or box[2] > layer.width or box[3] > layer.height:
        raise ValueError(f"Label outside canvas at {box}: {text!r}")
    backing = label.get("paper")
    patch = Image.new("RGBA", layer.size)
    if backing:
        padding = backing.get("padding", 4)
        blur = backing.get("blur", 0)
        opacity = backing.get("opacity", 160)
        if (
            not all(type(n) is int and n >= 0 for n in (padding, blur, opacity))
            or opacity > 255
        ):
            raise ValueError(
                "paper needs nonnegative integer padding/blur and opacity in [0, 255]"
            )
        rect = (box[0] - padding, box[1] - padding, box[2] + padding, box[3] + padding)
        mask = Image.new("L", layer.size)
        if (
            min(rect[0], rect[1]) < 0
            or rect[2] >= layer.width
            or rect[3] >= layer.height
        ):
            raise ValueError(f"Label backing extends beyond canvas: {text!r}")
        ImageDraw.Draw(mask).rectangle(rect, fill=opacity)
        if blur:
            mask = mask.filter(ImageFilter.GaussianBlur(blur))
        patch.paste(
            ImageColor.getrgb(backing.get("color", "#ffffff")), (0, 0, *layer.size)
        )
        patch.putalpha(mask)
    if layer.getchannel("A").crop(patch.getbbox() or box).getbbox():
        raise ValueError(f"Label overlaps earlier type at {box}: {text!r}")
    color = ImageColor.getrgb(label.get("color", "#292723"))
    draw = ImageDraw.Draw(patch)
    for pos, part in parts:
        draw.multiline_text(pos, part, font=font, fill=color)
    layer.alpha_composite(patch)


def render(root: Path, stage: Path, config: dict, spec: dict, stem: str) -> dict:
    """Render a single item and verify its output pixels and source identity."""
    base = asset(root, spec["base"])
    raw = base.read_bytes()
    if digest(raw) != spec["sha256"]:
        raise ValueError(f"{stem}: base hash changed; review {spec['base']} again")
    sources = spec.get("sources", [])
    if not isinstance(sources, list) or (not sources and stem != "cover"):
        raise ValueError(f"{stem}: provide source paragraph IDs in reading order")
    paragraphs = config["paragraphs"]
    if any(s not in paragraphs for s in sources) or len(set(sources)) != len(sources):
        raise ValueError(f"{stem}: unknown or repeated paragraph IDs")
    order = {key: i for i, key in enumerate(paragraphs)}
    if sources != sorted(sources, key=order.__getitem__):
        raise ValueError(f"{stem}: paragraph IDs out of source order")
    canvas = integer_pair(spec.get("canvas", config["canvas"]), "canvas", 1)
    image = load_base(raw, canvas, spec.get("centering", [0.5, 0.5]))
    layer = Image.new("RGBA", canvas)
    captions = []
    for label in spec.get("labels", []):
        text = label_text(label, paragraphs, sources)
        size = label["size"]
        if type(size) is not int or size < 1:
            raise ValueError(f"{stem}: font size must be a positive integer")
        font_path = asset(root, label.get("font") or config["font"])
        font = ImageFont.truetype(
            str(font_path), size, index=label.get("font_index", 0)
        )
        draw_label(layer, text, label, font)
        captions.append(text)
    output = stage / f"{stem}.png"
    encoded_profile = PROFILE.tobytes()
    composed = Image.alpha_composite(image.convert("RGBA"), layer).convert("RGB")
    composed.save(output, icc_profile=encoded_profile)
    with Image.open(output) as check:
        check.load()
        if (
            check.size != canvas
            or check.mode != "RGB"
            or check.info.get("icc_profile") != encoded_profile
        ):
            raise ValueError(f"{stem}: exported PNG failed verification")
    result = {
        "id": stem,
        "title": spec.get("title", stem),
        "sources": sources,
        "base": spec["base"],
        "base_sha256": spec["sha256"],
        "file": output.name,
        "sha256": digest(output.read_bytes()),
        "size": canvas,
        "labels": captions,
    }
    if stem == "cover":
        path = stage / "cover-text.png"
        layer.save(path, icc_profile=encoded_profile)
        result.update(text_layer=path.name, text_layer_sha256=digest(path.read_bytes()))
    if digest(base.read_bytes()) != spec["sha256"]:
        raise ValueError(f"{stem}: source changed during rendering")
    return result


def write_archive(stage: Path, items: list[dict]) -> str:
    """Package story images in reading order and verify every member."""
    path = stage / "images.zip"
    with zipfile.ZipFile(path, "w") as archive:
        for item in items:
            archive.write(stage / item["file"], item["file"])
    with zipfile.ZipFile(path) as archive:
        if (
            archive.namelist() != [i["file"] for i in items]
            or archive.testzip() is not None
        ):
            raise ValueError("ZIP membership or CRC mismatch")
        for item in items:
            if digest(archive.read(item["file"])) != item["sha256"]:
                raise ValueError(f"ZIP checksum mismatch: {item['file']}")
    return digest(path.read_bytes())


def write_sheet(stage: Path, items: list[dict]) -> None:
    """Make an optional, numbered contact sheet for comparing adjacent shots."""
    cols = min(4, len(items))
    rows = (len(items) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * 256, rows * 222), "white")
    draw = ImageDraw.Draw(sheet)
    for index, item in enumerate(items):
        x, y = index % cols * 256, index // cols * 222
        with Image.open(stage / item["file"]) as thumb:
            thumb.thumbnail((244, 192), Image.Resampling.LANCZOS)
            sheet.paste(thumb, (x + (256 - thumb.width) // 2, y))
        draw.text((x + 6, y + 195), item["id"], fill="black")
    sheet.save(stage / "contact-sheet.jpg", quality=90, icc_profile=PROFILE.tobytes())


def write_review_page(stage: Path, title: str, items: list[dict]) -> None:
    """Create an offline page referencing the current edition's actual files."""
    title = html.escape(title)
    cards = []
    for item in items:
        url = item["file"] + "?v=" + item["sha256"][:12]
        name = html.escape(item["title"])
        cards.append(
            f'<figure><a href="{url}"><img loading="lazy" src="{url}" alt="{name}"></a>'
            f"<figcaption>{name}</figcaption></figure>"
        )
    sheet_link = (
        ' · <a href="contact-sheet.jpg">图序总览</a>'
        if (stage / "contact-sheet.jpg").is_file()
        else ""
    )
    body = (
        f'<!doctype html><html lang="zh"><meta charset="utf-8">'
        f'<meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title>'
        "<style>body{max-width:62rem;margin:2rem auto;padding:0 1rem;font:1rem/1.6 system-ui}"
        "img{display:block;max-width:100%;height:auto}figure{margin:2rem 0}</style>"
        f'<main><h1>{title}</h1><a href="images.zip">下载插画</a> · '
        '<a href="manifest.json">文件清单</a>'
        + sheet_link
        + "".join(cards)
        + "</main></html>"
    )
    (stage / "index.html").write_text(body, encoding="utf-8")


def export(config_path: Path, out: Path, contact_sheet: bool = False) -> dict[str, Any]:
    """Publish one complete edition in a new directory after all checks pass."""
    config_path = config_path.resolve(strict=True)
    root = config_path.parent
    config = json.loads(config_path.read_text(encoding="utf-8"))
    paragraphs = config["paragraphs"]
    if (
        not isinstance(paragraphs, dict)
        or not paragraphs
        or not all(isinstance(v, str) and v.strip() for v in paragraphs.values())
    ):
        raise ValueError("paragraphs must map IDs to non-empty original text")
    ids = [item["id"] for item in config["images"]]
    if (
        not ids
        or len(set(ids)) != len(ids)
        or not all(re.fullmatch(r"[0-9]+", i) for i in ids)
    ):
        raise ValueError("images needs distinct numeric string IDs in reading order")
    out = out.absolute()
    if out.exists() or out.is_symlink():
        raise ValueError(
            f"Output already exists; choose a new edition directory: {out}"
        )
    out.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".illustrate-", dir=out.parent) as temp:
        stage = Path(temp) / "edition"
        stage.mkdir()
        items = [
            render(root, stage, config, spec, spec["id"]) for spec in config["images"]
        ]
        manifest = {
            "title": config["title"],
            "images": items,
            "zip_sha256": write_archive(stage, items),
        }
        cards = items
        if "cover" in config:
            cover = render(root, stage, config, config["cover"], "cover")
            manifest["cover"] = cover
            cards = [cover, *items]
        if contact_sheet:
            write_sheet(stage, items)
            manifest["contact_sheet"] = "contact-sheet.jpg"
        write_review_page(stage, config["title"], cards)
        (stage / "manifest.json").write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        os.rename(stage, out)
    return {
        "output": str(out),
        "images": len(items),
        "zip_sha256": manifest["zip_sha256"],
    }


def main() -> int:
    """Run the non-interactive export CLI."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("config", type=Path, help="UTF-8 project JSON")
    parser.add_argument("--out", type=Path, required=True, help="new output directory")
    parser.add_argument(
        "--contact-sheet",
        action="store_true",
        help="also export a numbered JPEG overview",
    )
    args = parser.parse_args()
    try:
        print(
            json.dumps(
                export(args.config, args.out, args.contact_sheet), ensure_ascii=False
            )
        )
    except (ValueError, KeyError, TypeError, OSError, ImageCms.PyCMSError) as error:
        print(f"Export failed: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
