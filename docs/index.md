---
title: Home
description: Generate beautiful PDFs, notes, diagrams, slides, and flashcards from Python or Markdown.
---

<div align="center" style="margin-bottom: 2rem;" markdown="1">

# <span class="logo-light"><img src="assets/paperforge_logo_black.svg" alt="PaperForge" width="320"/></span><span class="logo-dark"><img src="assets/paperforge_logo.svg" alt="PaperForge" width="320"/></span> PaperForge

### Beautiful PDFs from Python or Markdown
<br>

[Get Started](getting-started.md){ .md-button .md-button--primary }
[Browse Gallery](gallery/index.md){ .md-button }
[:material-github: GitHub](https://github.com/Bharat940/paperforge){ .md-button }

</div>

---

## Why PaperForge?

<div class="grid cards" markdown>

-   :material-feature-search: **13 Diagram Types**

    Flowcharts · ER · Sequence · Network · Architecture · C4 · AWS · State Machine · Git · Stack · Timing · Class · Schema

-   :material-palette: **10 Themes**

    Dark · Light · Ocean · Forest · Sunset · Midnight · Sepia · Catppuccin Latte/Mocha

-   :material-file-pdf-box: **Multi-Format Export**

    PDF · HTML · PPTX · Anki APKG / CSV / JSON from the same source

-   :material-language-markdown: **Markdown CLI**

    `paperforge notes.md --theme catppuccin-mocha` — no Python required

-   :material-lock: **Zero Dependencies**

    No LaTeX · No Java · No Node · No internet. Just Python + pip.

-   :material-vector-bezier: **Vector-Native**

    Every diagram is ReportLab vector graphics. No PNG rasters. No missing fonts.

</div>

---

## Quick Start

```python
import paperforge_notes as pn
import paperforge_diagrams as pd

pn.set_theme(pn.OCEAN_DARK)
pn.footer(left="Intro to Algorithms", show_page_num=True)

pn.part_box("Unit I: Basic Algorithms")
pn.chap_box("1.1 Sorting Fundamentals")
pn.section("Insertion Sort")
pn.body("Insertion Sort builds a sorted array one item at a time.")
pn.tip("Time complexity: O(N²) worst case, O(N) best case.")

fc = pd.Flowchart(width=pn.CW, height=180, caption="Fig 1: Loop invariant step")
fc.terminal("start", "START").process("step", "Compare").terminal("end", "END")
fc.edge("start", "step").edge("step", "end")

pn.add(fc.as_flowable())
pn.build_doc("quickstart.pdf")
```

## Ecosystem

<div class="grid cards" markdown>

-   :material-book-open-page-variant: **[paperforge_notes](notes/basics.md)**

    Semantic layout · Theming engine · Typography · ReportLab Platypus

-   :material-graph: **[paperforge_diagrams](diagrams/overview.md)**

    Vector-native diagram library · No external compilers · Theme-matched

</div>

---

## Feature Matrix

| Capability | PaperForge | ReportLab | Mermaid | Pandoc | LaTeX |
|:---|:---:|:---:|:---:|:---:|:---:|
| Themed PDF notes | :material-check: | :material-close: | :material-close: | Partial | :material-check: |
| Vector diagrams | :material-check: | :material-close: | :material-check: | Partial | Partial |
| HTML export | :material-check: | :material-close: | :material-close: | :material-check: | :material-close: |
| PPTX export | :material-check: | :material-close: | :material-close: | :material-close: | :material-close: |
| Flashcards / Anki | :material-check: | :material-close: | :material-close: | :material-close: | :material-close: |
| Zero external tools | :material-check: | :material-check: | :material-close: | :material-check: | :material-close: |
| Markdown CLI | :material-check: | :material-close: | :material-close: | :material-check: | :material-close: |
| Python API | :material-check: | :material-check: | :material-check: | :material-close: | Partial |

---

## What to read next

<div class="grid cards" markdown>

-   :material-rocket-launch: **[Getting Started](getting-started.md)**
-   :material-book-open-page-variant: **[Notes Basics](notes/basics.md)**
-   :material-image-multiple: **[Diagram Gallery](gallery/index.md)**
-   :material-puzzle: **[Why PaperForge?](why-paperforge.md)**
-   :material-code-tags: **[API Reference](api/notes.md)**

</div>

---

---

For a semantic overview of all documentation, see [sitemap.md](sitemap.md).

For an index of all available documentation, see [llms.txt](llms.txt).

---

## License

MIT — see [LICENSE](https://github.com/Bharat940/paperforge/blob/main/LICENSE).
