# Production files and retention

Maintain one authoritative source for each kind of information. Record the decisions the production currently needs. The following records can live in the project's existing files.

| Material | What to retain |
| --- | --- |
| Global art direction and asset index | One named style or full visual specification, its reusable prompt paragraph and reviewed style reference, output and layout specifications, stable entity IDs, design versions, and actual reference files. Keep these at work level and update them across chapters. |
| Source text and provenance | Ordered paragraphs or lines of verse with stable IDs, content types, and original wording. Record the file, edition, chapter or page location, and SHA-256 for a file-based source. Keep the relevant image evidence for undeciphered characters. Preserve paragraph breaks in pasted text. |
| Storyboard | The overview gives the passage boundaries, image count and rationale, omissions, chronology, and any departure from the usual specifications. Each entry identifies its evidence, depicted instant, composition, artistic choices, and review criteria. |
| Image prompts | One current, complete prompt per illustration. In a file-based project, retain it as plain text. Fold accepted local edits into the full prompt. |
| Production and reference assignments | For each image ID, record the prompt, character or asset identity, story stage, design version, files actually supplied and their purpose, and path and hash of the accepted master. Record model and parameter values only when the tool provides them. |
| Captions and layout | Wording, quotation sources, editorial titles, coordinates, font, layout, crop position, and cover configuration. Verify each change in the finished image. |
| Exports | Finished illustrations, cover and transparent type layer, image manifest, review page, download archive, and results of the technical checks performed. Generate the manifest during export. |
| Visual review | Link each master and finished image to its current file hash, source passage, reference versions, and individual findings. Track production review and user sign-off separately. |

Image IDs designate reading order. Use the same ID for the master, finished illustration, and prompt. Track character identity, story stage, and design version independently. Resolve shared assets and templates relative to the work's root. Scene files and exports may be relative to the current production directory. Declare the base in the configuration. Resolve Markdown links relative to their document.

For the bundled exporter, every input path is relative to the project configuration. Its `paragraphs` field supplies the source text for that export. If the project already maintains an authoritative text elsewhere, derive the field from it. Generate reading copies or a contact sheet when needed.

## What to keep

Retain the materials still needed to revise, reuse, re-export, or review the work. Update the record responsible for each decision.

| Material | Retention |
| --- | --- |
| Source text, provenance, and necessary textual evidence | Keep as the basis for events and quotations. |
| Current storyboard, complete prompts, and production list | Keep one authoritative version of each. |
| Current assets, master artwork, typesetting files, and cover sources | Keep all active inputs, including versions still used in other chapters. |
| Finished images, cover and type layer, manifest, review page, ZIP, and current findings | Keep the current deliverables. |
| Reading copies of the text or storyboard, and JPEG contact sheets | Generate on demand. Refresh or withdraw stale links after the source changes. |
| Candidates, temporary crops, magnified details, composites, comparison pages, masks, and patches | Use as needed during production. Remove temporary material after accepted work has been incorporated and dependencies have been checked. |
| Superseded prompts, failed attempts, per-edit instructions, discussions, old manifests, and duplicate specifications | Exclude from routine production deliverables. |
| Temporary scripts, caches, and unreferenced trials | Remove after checking for active dependencies. Moving them to a second archive creates the same maintenance burden. |

Before cleanup, inventory current files and cross-chapter references. Move accepted material to its permanent location, update tasks, configuration, and links, then verify that the files open and can be exported again. Only then remove obsolete temporary files.

Preserve master artwork, shared cover backgrounds, current multi-view references, and the evidence behind review findings. A filename containing “candidate,” “version,” or “patch” says nothing about whether the file is still in use. Limit cleanup to the work in scope and preserve review decisions. When a tool starts producing fewer default outputs, adjust its links and assess older works against their actual dependencies.
