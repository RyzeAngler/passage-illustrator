<img src="assets/icon.png" width="64" height="64" alt="">

# Passage Illustrator

[简体中文](zh/passage-illustrator/README.md)

Turn a passage into an illustration or a sequence grounded in the text. The agent selects a moment to depict, writes the image prompt, generates the artwork, and opens the result to check it against the passage. Across a sequence, it tracks who holds each object, what has changed in the setting, and which details identify a returning character.

For a new work, the skill establishes an explicit art direction and shared character, setting, and prop designs before story generation. A standard chapter or series includes a separate cover and story images typeset with scene titles and source quotations. Explicit requests can select wordless art or a particular stage.

The skill includes four prompt templates for first illustrations, subsequent scenes, local corrections, and dedicated cover artwork. The agent fills each template from the passage, storyboard, and design references. [Image prompt templates](references/prompts.md) · [Prompt-writing standard](SKILL.md#writing-image-prompts)

> The tide had just gone out. A single white shell lay on the lowest of the gray stone steps.

![A white scallop shell rests on the wet gray stone of the lowest step, just above the waterline.](examples/tide-line/base.png)

The edge of the tread tells the reader exactly where the shell lies. The change from dark, wet stone to lighter stone farther up suggests how recently the tide receded. This English edition retains the artwork generated for the original Chinese passage. [Scene brief and review](examples/tide-line/scene.md) · [English prompt](examples/tide-line/prompt.txt) · [Original generation prompt](examples/tide-line/prompt.zh.txt) · [Export configuration](examples/tide-line/project.json)

See [Project setup](references/project-setup.md) for the first-production requirements and [Reference assets and continuity](references/continuity.md) for managing designs across chapters.

## Install

### From GitHub

Run the [Vercel Skills CLI](https://github.com/vercel-labs/skills) from the project where you want to use the skill. You need Node.js and npx. The commands below install the English edition.

~~~sh
# Codex
npx skills add RyzeAngler/passage-illustrator --skill passage-illustrator -a codex

# Claude Code
npx skills add RyzeAngler/passage-illustrator --skill passage-illustrator -a claude-code
~~~

Choose the command for your client. To install for both in one command, use `-a codex claude-code`. The default scope is the current project. Add `-g` to make the skill available across your projects. For the Chinese edition, follow the [Chinese installation instructions](zh/passage-illustrator/README.md#从-github-安装).

| Client | Project skill location | How to invoke it |
| --- | --- | --- |
| Codex | `.agents/skills/passage-illustrator/` | Type `$passage-illustrator` in a conversation. |
| Claude Code | `.claude/skills/passage-illustrator/` | Type `/passage-illustrator` in a session. |

Codex also provides a built-in installer. In a Codex conversation, enter `$skill-installer Install the skill from GitHub repository RyzeAngler/passage-illustrator, using source path . and the installation name passage-illustrator`. Claude Code discovers standalone skills in its project skill location or in the personal directory `~/.claude/skills/`. Its `/plugin install` command is for plugins distributed through a marketplace. [Codex skills documentation](https://developers.openai.com/codex/skills) · [Claude Code skills documentation](https://code.claude.com/docs/en/skills)

### From a local checkout or ZIP

Check out the source or extract the ZIP outside the project's skill directories. If the extracted `passage-illustrator/` directory and your target project share a parent directory, run the following from the target project's root:

~~~sh
npx skills add ../passage-illustrator --skill passage-illustrator -a codex claude-code
~~~

For other layouts, use the absolute path to the directory containing `SKILL.md`. To target one client, keep only its name after `-a`. The English and Chinese editions share a skill ID. Install one edition per skill location.

## Requests you can make

- “Use $passage-illustrator to create a wordless landscape illustration for this passage.”
- “Illustrate chapter three of the attached book. Carry the character designs forward from chapter two, use quotations for the captions, and deliver the finished images and a download archive.”
- “Check this image against the passage and the previous illustration. The wrong character is holding the object. Fix the handoff and export it in the existing layout.”
- “Deliver only the storyboard and the prompt for each image. Use the project's established style and aspect ratio.”

Producing and checking artwork requires image generation and image viewing in the host application. The precision of a local correction also depends on the available editing tools. A text-only host can prepare the source text, storyboard, and prompts. Existing art assets and publishing tools can be used throughout. The work determines the style, language, captions, cover design, and dimensions.

## Export the example

Run this command from the skill directory with uv installed. With Python 3.10+ and Pillow 10.1+ already available, omit the initial `uv run`.

~~~sh
uv run python scripts/export.py examples/tide-line/project.json --out ./tide-edition
~~~

Open `tide-edition/index.html` to review the finished illustration, or extract it from `images.zip`. For captions, vertical type, caption backings, covers, and optional contact sheets, see [Export configuration](references/export-format.md).

## Maintenance and license

The [skill entry point](SKILL.md) links to the instructions for each production stage. The [behavioral evaluation cases](evals/cases.md) cover scene selection, continuity, revisions, and skill activation. Run the export tests from this directory.

~~~sh
uv run --group dev pytest -q
~~~

The skill, scripts, documentation, and original example are distributed under the [MIT License](LICENSE). The example illustration was generated with the host's built-in image tool. User-supplied texts, fonts, and reference images retain their respective licenses.
