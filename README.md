![PaperForge](assets/paperforge_logo_black.svg)
# PaperForge

Generate beautiful PDFs, notes, diagrams, slides, and flashcards from Python or Markdown.

PaperForge unifies two packages in a single monorepo:

- **`paperforge_notes`**: semantic layout, theming, and typography for ReportLab Platypus.
- **`paperforge_diagrams`**: vector-native diagram library (flowchart, ER, sequence, network, AWS, …).

## Repository Layout

```
PaperForge

├── paperforge_notes
│   PDF
│   HTML
│   PPTX
│   Flashcards

├── paperforge_diagrams
│   Flowcharts
│   UML
│   AWS
│   ER
│   C4

└── paperforge
    Meta package
```

## Installation

```bash
# Everything (notes + diagrams + full extras)
pip install paperforge

# Or pick what you need
pip install paperforge_notes
pip install paperforge_notes[full]
pip install paperforge_diagrams
```

For local development:

```bash
pip install -e ./paperforge_diagrams -e ./paperforge_notes[dev]
```

## Quick Start

```python
import paperforge_notes as pn
import paperforge_diagrams as pd

pn.set_theme(pn.OCEAN_DARK)
pn.footer(left="Intro to Algorithms", show_page_num=True)

pn.part_box(
    "Unit I: Basic Algorithms",
    subtitle="Big-O analysis and fundamental sorting methods",
    topics=["Complexity & Insertion Sort", "Visual Pipelines"]
)
pn.chap_box("1.1 Sorting Fundamentals")
pn.section("Insertion Sort")
pn.body("Insertion Sort builds a sorted array one item at a time.")
pn.tip("Time complexity: O(N^2) worst case, O(N) best case.")

fc = pd.Flowchart(width=pn.CW, height=180, caption="Fig 1: Loop invariant step")
fc.terminal("start", "START").process("step", "Compare").terminal("end", "END")
fc.edge("start", "step").edge("step", "end")

pn.add(fc.as_flowable())
pn.build_doc("quickstart.pdf")
```

## Features

### Cover Gallery
PaperForge acts as a true **Publishing Framework**. It ships with screenshot-worthy cover page presets and styles:

**Built-in Presets** (`pn.cover_preset(name)`):
| Preset | Style | Icon | Best For |
| ------ | ----- | ---- | -------- |
| `engineering` | `linear` | 💻 | SaaS docs, engineering guides |
| `research-paper` | `academic_modern` | 📐 | Research papers, peer review |
| `course-notes` | `catppuccin` | 📘 | Course notes, study guides |
| `networking` | `notion` | 🔗 | CCNA, network diagrams |
| `database` | `academic_modern` | 🗃️ | Database systems, SQL |
| `programming` | `linear` | 🐘 | Programming, software engineering |

**Cover Styles** (`pn.cover_card(style=...)`):
| Style | Best For |
| ----- | -------- |
| `linear` | SaaS docs, engineering guides — huge typography, gradient corner |
| `notion` | Clean, minimalist docs — icon-heavy, generous whitespace |
| `academic_modern` | O'Reilly / Manning inspired — structured, professional |
| `catppuccin` | Developer-focused — soft pastels, rounded cards |
| `textbook` | Student notes — thick accent bar, nested metadata |
| `modern` | General purpose — rounded card with accent border |
| `minimal` | Ultra clean — thin left bar, elegant typography |
| `gradient` | Colorful — diagonal corner split with dual accents |
| `corporate` | Business — top/bottom frame layout |
| `academic` | Formal — double frame with corner ornaments |
| `standard` | Legacy boxed card |
| `hero` | Massive typography, generous whitespace |
| `book` | Classic textbook aesthetic with surface color blocks |
| `diagram` | SVG background illustration with accent text |

### Core Features
- **Notes**: 15 preset themes, premium cover pages, semantic tags (`tags=["Networking", "Exam Notes"]`), SVG background illustrations, callouts, and LaTeX formulas.
- **Diagrams**: 13 diagram types, orthogonal routing, matching theme presets.
- **Export**: PDF, HTML, PPTX, Anki APKG / CSV / JSON — all from one source.
- **CLI**: `paperforge notes.md --theme catppuccin-mocha` for Markdown users.
- **Zero dependencies** beyond Python + pip (`svglib` is optionally supported for SVG backgrounds).

## Documentation

Full documentation, gallery, and API reference:

**[docs.paperforge.dev](https://docs.paperforge.dev)**

- [Getting Started](https://docs.paperforge.dev/getting-started)
- [Notes Guide](https://docs.paperforge.dev/notes/basics)
- [Diagrams Guide](https://docs.paperforge.dev/diagrams/overview)
- [Gallery](https://docs.paperforge.dev/gallery/index)
- [API Reference](https://docs.paperforge.dev/api/notes)

## Markdown Compiler

Compile Markdown directly to themed PDFs. Supports headings, tables, code blocks, alert boxes, and eight diagram block types:

```bash
paperforge notes.md --output notes.pdf --theme catppuccin-mocha
```

## License

MIT License. See [LICENSE](LICENSE).
