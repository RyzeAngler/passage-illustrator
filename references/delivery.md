# Lettering, export, and delivery

## Captions, lettering within the scene, and page layout

For inscriptions, signs, and other lettering within the scene, use the wording, letterforms, and writing conventions appropriate to the text and setting. Proofread each character. Check the surface it belongs to and how perspective, texture, and light affect the lettering. Text that matters to the story must remain legible at delivery size.

Choose editorial captions from lines of verse, narration, or dialogue that illuminate the scene. Preserve the sense of the passage before deciding how much to quote. Mark omissions in the configuration when joining nonconsecutive excerpts. Record editorial titles, summaries, transcriptions, translations, and direct quotations according to their actual status. A legible place name within the scene may make a separate location label redundant. Keep paragraph IDs, provenance, review status, and generation notes in the production records.

Establish the work's layout specifications once and record variations for individual illustrations as needed. Specify dimensions in output pixels and identify a font file the production environment can read.

| Element | Settings to establish |
| --- | --- |
| Canvas and crop | Dimensions, reading direction, fit method, crop position for each image, and coordinate origin. |
| Main text | Font file and face index, type size, character advance, line or column spacing, and color. |
| Editorial titles and location labels | Position, size, color, and when each should appear. |
| Caption backing and edges | Color, opacity, padding around the combined bounds of the lettering, and feather radius. Keep the underlying texture visible. |
| Clear space | Allow for the entire text block and feathered edge. Keep faces, hands, principal actions, key objects, and lettering within the scene clear. |

Link each layout to its image ID, title, master artwork path and hash, source paragraphs, wording, and text positions. After replacing a master, update the hash and check composition, crop, and clear space again. Fit the master to its final dimensions in one operation. Check the actual output. Automated checks cover quotations, bounds, and pixels. Inspect the artwork to judge whether type obscures an action or sits well with the illustration.

## Covers and export

A series with a common cover design uses dedicated cover artwork and a shared template. Store the background, canvas, fonts, and title positions in the template. Set the installment identifier and title for each cover. For long titles, inspect the bounds and reading order, then adjust position and type size as needed. Retain the flattened cover, its transparent type layer, the source background, the font information, and the relevant hashes for future editions.

Use the project's existing tools or the bundled exporter. The bundled tool produces illustration PNGs, an HTML review page, a manifest, and an ordered ZIP of the illustrations. A configured cover also produces a separate cover image and transparent type layer. Request a JPEG contact sheet when useful. See [Export configuration](export-format.md).

| Change | What to update and inspect |
| --- | --- |
| Caption, editorial title, location label, or typography | Edit the typesetting configuration and re-export from the same master. Proofread the finished text and check for occlusion. |
| Content of one illustration | Update its complete prompt, master, reference assignments, hash, and visual findings. Then typeset, rebuild the manifest, and package the images again. |
| Shared identity, story stage, prop, or setting | Update the active design, affected reference assignments, prompts, and findings for every affected image. |
| Chapter identifier or title | Update the cover configuration, export the cover and type layer, and inspect the title arrangement and bounds. |

## Visual review of the finished work

Read the sequence in order. Then inspect each illustration in full and at detail scale. Check narrative order and transitions, recurring figures and props, and continuity of place. Confirm that cropping and typesetting leave the essential relationships visible.

Proofread lettering within the scene on its actual surface. For editorial captions, check glyphs, typeface, reading direction, line and column breaks, backing, and legibility at the intended reading size. For the cover, check the artwork, installment identifier, title, and reading order. Record observations against the current finished file.

## Technical checks and delivery

1. Check image numbering, unique filenames, and the count against the configuration. Count the cover separately.
2. Verify dimensions, format, and color space against the work's specifications. The bundled tool exports RGB PNGs with an embedded sRGB ICC profile. The cover type layer is an RGBA PNG of the same dimensions as the cover.
3. Compare hashes across the masters, configuration, manifest, and files on disk. Preserve the masters' original pixels and sufficient material to typeset and export again.
4. Trace each quotation to the source. Document transcription and omissions, and distinguish editorial titles from quotations.
5. Open the files and links used by production tasks, assets, prompts, typesetting, covers, and the review page.
6. Check that the review page displays the current images and links to a contact sheet only when one was generated for this export.
7. Check that the illustration archive contains exactly the agreed images in reading order. Verify ZIP member order, CRCs, and the SHA-256 digest of each member.
8. Report only the technical checks actually performed. Associate visual findings with the current masters, exports, and reference versions. Record user review as it stands.

Deliver the images, separate cover, and illustration archive according to the request. For a series, provide a README or existing project entry point and a working review page with current status and links.
