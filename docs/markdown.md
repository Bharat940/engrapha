# Markdown Compiler

PaperForge ships with a CLI tool that compiles standard Markdown files into themed PDFs. Two commands, `paperforge` and `pdfnotes`, are installed by the `paperforge-notes` package.

## Quick Start

```bash
paperforge notes.md --output notes.pdf --theme catppuccin-mocha
```

Other supported themes: `dark`, `light`, `ocean-dark`, `forest-dark`, `sunset-dark`, `midnight-dark`, `ocean-light`, `sepia`, `catppuccin-latte`, `catppuccin-mocha`.

## CLI Reference

### Basic usage

```bash
paperforge input.md -o output.pdf -t catppuccin-mocha --title "My Notes" --author "Your Name"
```

### Flags

| Flag | Purpose |
| ---- | ------- |
| `input` | Required: path to input `.md` file |
| `-o, --output` | Custom output path. Defaults to `input.md` → `input.pdf`. |
| `-t, --theme` | Theme name. Default: `dark`. |
| `--title` | Document title metadata. |
| `--author` | Document author metadata. |

### Front matter (YAML)

Optional YAML front matter at the top of the file:

```markdown
---
title: Java Programming
author: Bharat Dangi
theme: ocean-dark
---

# Chapter 1
```

`title`, `author`, and `theme` keys are honoured.

## Supported Markdown Features

### Headings

```markdown
# Header 1 → pn.part_box()
## Header 2 → pn.chap_box()
### Header 3 → pn.section()
#### Header 4 → pn.subsection()
```

### Body text

All paragraphs are rendered with `pn.body()`.

### Code blocks

````markdown
```python
pn.set_theme(pn.DARK)
pn.body("Hello.")
```
````

### Tables

```markdown
| Algorithm | Best | Worst | Average |
| --------- | ---- | ----- | ------- |
| Quick Sort | O(N log N) | O(N^2) | O(N log N) |
| Merge Sort | O(N log N) | O(N log N) | O(N log N) |
```

### Bullets

```markdown
- First item
- Second item
- Third item
```

### Alert Boxes

GitHub-style alert blocks map to PaperForge callouts:

```markdown
> [!NOTE]
> Yellow bordered note box (via `pn.note()`).

> [!TIP]
> Green tip box (via `pn.tip()`).

> [!WARNING]
> Yellow-bordered highlight box (via `pn.highlight()`).

> [!CAUTION]
> Yellow-bordered highlight box (via `pn.highlight()`).
```

### Diagram Fences

Eight built-in diagram block types are supported. Each block compiles to a vector diagram inside the Markdown.

```markdown
```flowchart
width = 400
height = 200
caption = Figure 1: Basic Process Flow
direction = LR
terminal start "START"
process step "Compute Value"
terminal end "END"

edge start step
edge step end
```
```

Supported block types: `flowchart`, `sequence`, `layeredstack`, `schema`/`er`, `git`, `architecture`/`arch`, `c4`/`c4container`, `aws`/`cloud`.

Diagram-specific configuration values are passed at the top of the block as `key = value`.

## What gets compiled

The CLI invokes the same parser used by `pn.include_markdown()`. Each block is mapped to the most appropriate PaperForge API. Unknown code-block languages are treated as syntax-highlighted code (using Pygments).

## Limitations

- Heading levels < 4 are supported; deeper than `<img_src>` HTML tags inside paragraphs are passed through verbatim.
- Front matter block must begin on line 1 of the file.
- No `LaTeX` math rendering yet (use `formula()` directly in Python instead).

## Programmatic alternative

For more control, use Python's `compile_markdown_to_pdf()`:

```python
from paperforge_notes.cli import compile_markdown_to_pdf
compile_markdown_to_pdf(
    input_file="notes.md",
    output_file="notes.pdf",
    theme_name="catppuccin-mocha",
)
```

## Next

- [Diagram overview](diagrams/overview.md)
- [Themes](themes.md)
