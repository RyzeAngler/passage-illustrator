# Export configuration

Keep the UTF-8 JSON configuration, master artwork, and any fonts in the same project directory. Input paths are relative to the configuration file and may point into subdirectories. Set `skill_dir` to the installed skill directory and `work_dir` to the project directory.

~~~sh
uv run --project "$skill_dir" python "$skill_dir/scripts/export.py" "$work_dir/project.json" --out "$work_dir/edition-01"
~~~

You can also run the script directly with Python 3.10+ and Pillow 10.1+. Choose a new output directory for each edition. Add `--contact-sheet` to generate a numbered JPEG overview. The bundled `examples/tide-line/project.json` can be run as supplied without any fonts.

## Project fields

| Field | Meaning |
| --- | --- |
| `title`, `canvas` | Work title and output dimensions in pixels as `[width, height]`. An individual image can override `canvas`. |
| `paragraphs` | An object mapping paragraph IDs to the verbatim source text, in reading order. |
| `images` | Illustrations in final reading order. Each entry supplies `id` (a unique string of digits), `title`, `base`, `sha256`, and `sources` (paragraph IDs in source order). |
| `centering` | Optional crop position for an image. Each axis takes a fraction from 0 to 1. The default is centered. The image is scaled proportionally and cropped to fill the canvas. |
| `font` | Relative path to a readable font file when adding type. Set `font_index` on a text block to select a face from a font collection. Supply a font appropriate to the script and licensed for the work. |
| `labels` | Editorial text blocks for one image. Omit for an unlettered illustration. |
| `cover` | Optional cover with dedicated artwork. Uses the same artwork and type settings as an illustration and can specify its own canvas. Supply `sources` if the cover quotes the text. |

Calculate SHA-256 from the accepted master and record it during visual review. Use `shasum -a 256` on macOS or `sha256sum` on Linux. A hash mismatch means the file differs from the one reviewed. Open it, assess the affected areas, and update the hash after accepting it.

## Editorial text blocks

Place the following array in an image's `labels` field. This example quotes the English passage in the bundled project. Supply a suitable `font` path before rendering it. Each block uses `xy` for its starting position on the final canvas and `size` for its type size, both in pixels. The chosen font and coordinates determine the actual glyph bounds. Position text for each illustration at delivery size.

~~~json
[
  {
    "quote": [{"source": "p1", "text": "The tide had just gone out."}],
    "xy": [70, 62],
    "size": 38,
    "color": "#213b38",
    "paper": {"color": "#f6f2dc", "opacity": 145, "padding": 12, "blur": 4}
  }
]
~~~

- Use `quote` for verbatim text. Each fragment must occur in a paragraph named in that image's `sources`, and fragments must follow source order. The exporter joins excerpts with an ellipsis. Keep a continuous quotation in one fragment. To position separate lines or vertical columns, use separate blocks and check reading order.
- Use `text` for editorial titles, location labels, and translations of the project's source text. Record the basis for a translation or transcription alongside the configuration. Use the work's own typesetting tools if it requires complex shaping, specialized punctuation spacing, or alignment of parallel translations.
- Text runs horizontally by default. For a simple vertical column of upright characters, set `direction` to `vertical` and specify the character advance with `step`. Give each column a separate origin. Use RGB colors. Individual blocks can override `font` and `font_index` and specify a `paper` backing.
- The exporter writes RGB PNGs in sRGB. It converts images with embedded color profiles to sRGB and treats untagged RGB artwork as sRGB. Flatten transparent artwork onto the intended background before recording it as a master. After quotation and bounds checks pass, inspect glyph coverage, line breaks, and any obscured artwork in the rendered image.

Run a provisional export with the actual font before finalizing text positions. Soft backings extend beyond the glyph bounds and adjacent blocks need enough space for their padding and feathered edges. If the exporter reports an overlap, adjust spacing, padding, or backing and export again. Check the resulting PNG at its intended reading size.

## Outputs and diagnostics

Each image ID corresponds to a PNG. `manifest.json` records reading order, paragraph IDs, SHA-256 hashes of masters and finished images, actual dimensions, and rendered wording. Open `index.html` for offline review. `images.zip` contains the illustrations in manifest order. A cover produces `cover.png` and `cover-text.png` separately. A requested contact sheet is saved as `contact-sheet.jpg`.

On success the command prints JSON with the output directory, image count, and archive hash. On failure it exits with a nonzero status before publishing a partial edition. Review the full sequence in the HTML page and open the individual PNGs. Keep visual findings in the work's review record and associate them with the hashes in the manifest. To change a caption, typeset again from the same master. Keep the master, its prompt, and its design references in the project directory.
