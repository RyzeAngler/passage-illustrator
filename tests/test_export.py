"""Exercise the public export command with isolated illustration projects."""

import hashlib
import json
import subprocess
import sys
import zipfile
from pathlib import Path

import pytest
from PIL import Image, ImageFont

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "export.py"


def project(root: Path) -> dict:
    """Write a small real source image and return the matching config."""
    base = root / "base.png"
    Image.new("RGB", (160, 120), "ivory").save(base)
    item = {
        "id": "01",
        "title": "Tide",
        "base": base.name,
        "sha256": hashlib.sha256(base.read_bytes()).hexdigest(),
        "sources": ["p1"],
    }
    return {
        "title": "Tide",
        "canvas": [120, 90],
        "paragraphs": {"p1": "Low tide."},
        "images": [item],
    }


def run(root: Path, config: dict, *options: str) -> subprocess.CompletedProcess:
    """Invoke the same command used by an installed skill."""
    path = root / "work.json"
    path.write_text(json.dumps(config), encoding="utf-8")
    return subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            str(path),
            "--out",
            str(root / "edition"),
            *options,
        ],
        capture_output=True,
        text=True,
        check=False,
    )


def test_export(root: Path) -> None:
    """The archive, manifest and review page agree with actual pixels."""
    config = project(root)
    result = run(root, config)
    assert result.returncode == 0, result.stderr
    out = root / "edition"
    manifest = json.loads((out / "manifest.json").read_text())
    item = manifest["images"][0]
    with Image.open(out / item["file"]) as image:
        assert image.size == (120, 90) and image.mode == "RGB"
        assert image.info["icc_profile"]
    with zipfile.ZipFile(out / "images.zip") as archive:
        assert archive.namelist() == [item["file"]]
        assert hashlib.sha256(archive.read(item["file"])).hexdigest() == item["sha256"]
    assert item["file"] in (out / "index.html").read_text()
    assert "contact-sheet.jpg" not in (out / "index.html").read_text()
    assert run(root, config).returncode != 0


@pytest.fixture
def root(tmp_path: Path) -> Path:
    """Use a different directory for each CLI invocation."""
    return tmp_path


@pytest.mark.parametrize(
    ("fault", "error"),
    [
        ("hash", "hash changed"),
        ("source", "paragraph IDs"),
        ("quote", "Quotation not found"),
        ("duplicate", "distinct numeric"),
        ("escape", "external project"),
        ("cover_id", "distinct numeric"),
    ],
)
def test_rejects_bad_input(root: Path, fault: str, error: str) -> None:
    """Reject stale or contradictory inputs before publishing any files."""
    config = project(root)
    item = config["images"][0]
    if fault == "hash":
        item["sha256"] = "0" * 64
    elif fault == "source":
        item["sources"] = ["missing"]
    elif fault == "quote":
        item["labels"] = [{"quote": [{"source": "p1", "text": "High tide."}]}]
    elif fault == "duplicate":
        config["images"].append(item)
    elif fault == "escape":
        item["base"] = "../base.png"
    else:
        item["id"] = "cover"
    result = run(root, config)
    assert result.returncode != 0 and not (root / "edition").exists()
    assert error in result.stderr


def test_text_and_cover(root: Path) -> None:
    """Both directions support text, and cover layers stay outside the story ZIP."""
    config = project(root)
    # Pillow wheels and OS distributions resolve a test font differently.
    candidates = [
        "DejaVuSans.ttf",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "C:/Windows/Fonts/arial.ttf",
    ]
    for name in candidates:
        try:
            font = Path(ImageFont.truetype(name, 16).path)
            break
        except OSError:
            continue
    else:
        pytest.skip("No test font installed")
    (root / "font.ttf").write_bytes(font.read_bytes())
    config["font"] = "font.ttf"
    item = config["images"][0]
    item["labels"] = [
        {
            "quote": [{"source": "p1", "text": "Low tide."}],
            "xy": [12, 12],
            "size": 14,
            "paper": {"padding": 3, "blur": 2, "color": "#ffffff"},
        }
    ]
    config["cover"] = {
        **item,
        "labels": [{"text": "AB", "direction": "vertical", "xy": [2, 2], "size": 15}],
    }
    result = run(root, config, "--contact-sheet")
    assert result.returncode == 0, result.stderr
    out = root / "edition"
    assert (out / "contact-sheet.jpg").is_file() and "contact-sheet.jpg" in (
        out / "index.html"
    ).read_text()
    with Image.open(out / "01.png") as rendered:
        assert rendered.getpixel((119, 89)) == (255, 255, 240)
        assert len(rendered.getcolors(120 * 90)) > 2
    with Image.open(out / "cover-text.png") as layer:
        assert layer.mode == "RGBA" and layer.getchannel("A").getbbox()
    with zipfile.ZipFile(out / "images.zip") as archive:
        assert archive.namelist() == ["01.png"]
