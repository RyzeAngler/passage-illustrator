# Passage Illustrator · 原文配图

[English](../../README.md)

给 Agent 一段原文，它可以选景、绘制插画、打开成图对照原文核查并返修。连续图组还会追踪同一人物、道具和现场在不同镜头里的状态。适合小说章节、散文、诗文和已有插画项目。

初次绘画、跨镜续画和局部编辑各有一份内置提示词模板。调用时 Agent 依据本镜原文、分镜和有效设定，把模板展开成可以直接提交的完整绘画说明。[三份生图提示词模板](references/prompts.md) · [逐图编写标准与提交前检查](SKILL.md#提示词编写标准)

> 潮水刚退。灰色石阶的最低一级上，留着一枚白贝壳。

![俯视海边灰色石阶，水边的湿石面上留着一枚白贝壳](examples/tide-line/base.png)

这幅插画把水面、最后一级石阶和贝壳放在同一个观察角度。读者能从石阶外缘辨认贝壳的位置，也能从深浅不同的石面看出退潮留下的湿痕。[原文与导出配置](examples/tide-line/project.json) · [分镜和实际审阅](examples/tide-line/scene.md) · [完整提示词](examples/tide-line/prompt.txt)

## 安装

### 从 GitHub 安装

在要使用插画技能的项目根目录，用 [Vercel Skills CLI](https://github.com/vercel-labs/skills) 安装。需要 Node.js 和 npx。以下命令安装中文版。

~~~sh
# Codex
npx skills add https://github.com/RyzeAngler/passage-illustrator/tree/main/zh/passage-illustrator --skill passage-illustrator -a codex

# Claude Code
npx skills add https://github.com/RyzeAngler/passage-illustrator/tree/main/zh/passage-illustrator --skill passage-illustrator -a claude-code
~~~

按使用的客户端选一条。两个客户端都用时，写成 `-a codex claude-code` 即可一次安装。默认安装到当前项目；要让自己的所有项目都能使用，加 `-g`。英文版的命令见[英文安装说明](../../README.md#from-github)。

| 客户端 | 项目级技能入口 | 安装后调用 |
| --- | --- | --- |
| Codex | `.agents/skills/passage-illustrator/` | 在对话中输入 `$passage-illustrator` |
| Claude Code | `.claude/skills/passage-illustrator/` | 在会话中输入 `/passage-illustrator` |

Codex 也可在对话中使用其内置安装器，例如 `$skill-installer 从 GitHub 仓库 RyzeAngler/passage-illustrator 安装技能，源路径为 zh/passage-illustrator，安装名为 passage-illustrator`。Claude Code 会发现项目级技能和个人目录 `~/.claude/skills/` 中的技能。其 `/plugin install` 命令用于通过插件市场分发的插件。[Codex 技能文档](https://developers.openai.com/codex/skills) · [Claude Code 技能文档](https://code.claude.com/docs/en/skills)

### 从本地源码或 ZIP 安装

将源码检出或把 ZIP 解压到项目技能目录以外的临时位置。假设解压后的 `passage-illustrator/` 与目标项目位于同一父目录，在目标项目根目录执行：

~~~sh
npx skills add ../passage-illustrator --skill passage-illustrator -a codex claude-code
~~~

其他位置可直接使用含 `SKILL.md` 的目录的绝对路径。只需一个客户端时，保留对应的 `-a` 参数值。中英文版共用技能名，每个安装位置选择一种语言。

## 调用

- “用 $passage-illustrator 为下面这段散文画一张无字横幅。”
- “依据附件第三章制作一组插画，人物造型沿用上一章，配文直接选原句。请交付成图和下载包。”
- “对照原文和前图检查这张画。道具归属有误，请局部修正，再导出原版式。”
- “只交付分镜与逐图提示词，画幅和画风沿用项目设定。”

制作图像需要宿主提供图像生成与看图能力。精确局部修改还取决于编辑接口；文字环境可独立完成读本、分镜和提示词。技能可以接入已有美术资产和出版工具。作品的画风、语言、配文、封面与画幅由本次任务决定。

## 复现样例

在当前目录运行，需要 uv；或者在有 Python 3.10+ 和 Pillow 10.1+ 的环境中去掉命令开头的 uv run。

~~~sh
uv run python scripts/export.py examples/tide-line/project.json --out ./tide-edition
~~~

打开 tide-edition/index.html 查看实际成图，或用 images.zip 取出图像。配文、竖排、衬底、封面及可选总览的设置见[导出配置](references/export-format.md)。

## 维护与许可

[技能入口](SKILL.md)链接到各制作阶段的操作说明。[行为验收用例](evals/cases.md)覆盖选景、连续分镜、返修和触发边界。导出工具的自动化检查可从本目录运行：

~~~sh
uv run --group dev pytest -q
~~~

本仓库的技能、脚本、文档与随附原创样例按 [MIT License](LICENSE) 提供。示例插图由内置图像生成工具生成。使用者自行提供的原文、字体和参考图沿用其各自的授权。
