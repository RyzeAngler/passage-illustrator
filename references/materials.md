# Production files and retention

Maintain one authoritative source for each kind of information. Record the decisions the production currently needs. The following records can live in the project's existing files.

| Material | What to retain |
| --- | --- |
| Global art direction and asset index | The built-in style ID and skill version, the applied fixed prompt paragraph and its reviewed production reference, output and layout specifications, stable entity IDs, design versions, and actual reference files. Keep these at work level and update them across chapters. |
| Source text and provenance | Ordered paragraphs or lines of verse with stable IDs, content types, and original wording. Record the file, edition, chapter or page location, and SHA-256 for a file-based source. Keep the relevant image evidence for undeciphered characters. Preserve paragraph breaks in pasted text. |
| Storyboard | The overview gives the passage boundaries, image count and rationale, omissions, chronology, and any departure from the usual specifications. Each entry identifies its evidence, depicted instant, composition, artistic choices, and review criteria. |
| Image prompts | One current, complete prompt per illustration. In a file-based project, retain it as plain text. Fold accepted local edits into the full prompt. |
| Production and reference assignments | For each image ID, record the prompt, character or asset identity, story stage, design version, files actually supplied and their purpose, and path and hash of the accepted master. Record model and parameter values only when the tool provides them. |
| Captions and layout | Wording, quotation sources, editorial titles, coordinates, font, layout, crop position, and cover configuration. Verify each change in the finished image. |
| Exports | Finished illustrations, cover and transparent type layer, image manifest, review page, download archive, and results of the technical checks performed. Generate the manifest during export. |
| Visual review | Link each master and finished image to its current file hash, source passage, reference versions, and individual findings. Track production review and user sign-off separately. |

Image IDs designate reading order. Use the same ID for the master, finished illustration, and prompt. Track character identity, story stage, and design version independently. Resolve shared assets and templates relative to the work's root. Scene files and exports may be relative to the current production directory. Declare the base in the configuration. Resolve Markdown links relative to their document.

For the bundled exporter, every input path is relative to the project configuration. Its `paragraphs` field supplies the source text for that export. If the project already maintains an authoritative text elsewhere, derive the field from it. Generate reading copies or a contact sheet when needed.

## Workspace layout

Use the established Journey to the West production layout below. The source filename and chapter directory change with the work. Keep the shared assets, series cover sources, chapter files, and numbered deliverables in these positions. The Chinese path labels identify production files. Code filenames use English ASCII.

~~~text
project-root/
├── README.md
├── 原著目录.json
├── 原著.epub
├── 美术资产库/                    # Shared index, designs, versions, and reference assets
├── 账号物料/系列封面/             # Shared series cover artwork and template
├── tools/
│   ├── typeset_chapter.py
│   └── render_cover.py
└── 回目目录/
    ├── README.md                 # Current status, review and download links
    ├── 原文依据/
    │   ├── 正文.json
    │   └── 来源记录.json          # Keep source-page and glyph evidence as needed
    ├── 02_N张画面脚本.json        # Chapter overview, storyboards, and review criteria
    ├── 04_生图任务.json           # Current tasks, reference assignments, and active files
    ├── 生图提示词/               # One current complete prompt per image
    ├── 底图/                     # Masters accepted in production review
    ├── 排版/配文与排字.json
    ├── 成图/
    ├── 封面/
    │   ├── 封面配置.json
    │   ├── 回数_封面.png
    │   └── 回数_文字层.png
    ├── 检查/
    │   ├── 目视审阅.json          # Current visual findings for masters, exports, and covers
    │   └── 交付检查.json          # Current technical check results
    ├── 05_审阅总览.html
    ├── 06_图文成图清单.json
    └── 回数_N张图文成图.zip       # Story images only; cover delivered separately
~~~

Global modeling takes place after the passage has been extracted and read, before storyboarding and the first story generation. Keep the shared index at `美术资产库/资产索引.json`. Character designs belong in `人物库/`, settings in `场景库/`, and objects in `物件库/`, under the same asset library. Keep the fixed style's production references in `风格库/`. Use the existing asset, design, source-evidence, and version records. Each chapter's `04_生图任务.json` binds the actual entity, stage, version, and reference file used.

Keep the shared cover background, full background prompt, and `封面模板.json` in `账号物料/系列封面/`. Each chapter's `封面/封面配置.json` points to that template and supplies the chapter wording. Put the flattened cover and transparent type layer in that chapter's `封面/` directory.

Resolve asset and production-task paths from the work root. Resolve storyboard, typesetting, image-manifest, and visual-review paths from the chapter directory. Resolve the cover template from the work root and Markdown links from their document.

Keep project code under `tools/` with English ASCII filenames such as `typeset_chapter.py` and `render_cover.py`. Update callers and documentation together when renaming existing scripts. Preserve the project's current production logic.

The bundled `scripts/export.py` is a lower-level renderer with its own flat output and configuration format. To use it with this layout, derive its inputs temporarily from the authoritative source paragraphs, typesetting configuration, and cover template. Copy the actual image and font inputs under that temporary configuration directory so the renderer's path checks pass. Use a project helper with an English filename when this conversion is required. Place the accepted results in `成图/` and `封面/`, and generate the chapter-level review page, manifest, technical checks, and ZIP with paths matching their final locations. Remove the temporary staging directory after verification. Keep the established layout as the retained production record.

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
