# Getting Started

PaperForge lets you produce themed academic PDFs, vector diagrams, and flashcards with just a few lines of Python.

## Requirements

- **Python** >= 3.11
- **reportlab** >= 4.5.1
- **pydantic** >= 2.13.4 (transitive via `paperforge-diagrams`)
- **pygments** >= 2.20.0 (included in core install)

Optional (for extended features):
- **fitz** >= 1.25.0 — required only for PPTX export and `build_split_doc()`
- **genanki** >= 2.1.0 — required only for Anki `.apkg` flashcard export

## Install

```bash
# Everything in one package
pip install paperforge

# Or pick what you need
pip install paperforge_notes
pip install paperforge_notes[full]
pip install paperforge_diagrams
```

### Editable installs for local development

```bash
pip install -e ./paperforge -e ./paperforge_diagrams -e ./paperforge_notes[dev]
```

## Package Feature Comparison

The monorepo is split into two packages. You can install them separately depending on your project needs:

| Feature / Capability | `paperforge_diagrams` | `paperforge_notes` |
| :--- | :---: | :---: |
| **Primary Focus** | Native vector diagramming for ReportLab | Semantic document layout & theming engine |
| **Dependencies** | `reportlab`, `pydantic` | `reportlab`, `pygments`, `paperforge-diagrams` |
| **Output formats** | Standalone vector PDF, SVG, PNG | Multi-page PDF, HTML pages, PPTX slides, Anki decks |
| **Vector Drawings** | Yes (13 diagram types, connectors, auto-routing) | No (uses `paperforge_diagrams` for rendering) |
| **Topologies & Layouts**| Yes (Star, bus, ring, tree, mesh layout methods) | No |
| **Textbook Callouts** | No | Yes (note, tip, warning, theorem, proof, definition) |
| **Theming Engine** | Base theme (colors, fonts) | Full document themes, presets, ThemeBuilder |
| **Math Formatting** | No | Yes (LaTeX math inline & block equation formats) |
| **Study & Flashcards** | No | Yes (questions, answers, MCQs, revision cards, flashcards) |
| **CLI Compiler** | No | Yes (`paperforge` / `pdfnotes` compiling markdown to PDF) |


## 5-Line Quickstart

```python
import paperforge_notes as pn

pn.set_theme(pn.DARK)
pn.footer(left="Quickstart", show_page_num=True)
pn.cover_preset("engineering", title="My First Document")
pn.body("PaperForge builds themed academic notes in 5 lines.")
pn.build_doc("quickstart.pdf")
```

## Full Quickstart Example

```python title="quickstart.py"
import paperforge_notes as pn
import paperforge_diagrams as pd

# 1. Initialize theme and footer
pn.set_theme(pn.OCEAN_DARK)
pn.footer(left="Algorithms", right="Unit I", show_page_num=True)
pn.cover_preset("course-notes", title="Algorithms", subtitle="Unit I: Basics")

# 2. Add content
pn.part_box("Unit I: Basic Algorithms")
pn.chap_box("1.1 Sorting Fundamentals")
pn.section("Insertion Sort")
pn.body("Insertion Sort builds a sorted array one item at a time.")
pn.tip("Time complexity: O(N²) worst case, O(N) best case.")
pn.note("Worst case occurs when the array is reverse sorted.")

# 3. Create and embed a vector diagram
fc = pd.Flowchart(width=pn.CW, height=180, caption="Fig 1: Loop invariant step")
fc.terminal("start", "START")
fc.process("step", "Compare Key with element")
fc.terminal("end", "END")
fc.edge("start", "step").edge("step", "end")
pn.add(fc.as_flowable())

# 4. Build the document
pn.build_doc("quickstart.pdf")
```

Run it:

```bash
python quickstart.py
```

## What to read next

<div class="grid cards" markdown>

-   :material-image-multiple: **[Browse the diagram gallery](gallery/index.md)**
-   :material-book-open-page-variant: **[Notes basics](notes/basics.md)**
-   :material-graph: **[Diagrams overview](diagrams/overview.md)**
-   :material-puzzle: **[Why PaperForge?](why-paperforge.md)**

</div>

## Next

Themed notes → [Notes: Basics](notes/basics.md)
Diagrams only → [Diagrams: Overview](diagrams/overview.md)
Full comparison → [Why PaperForge?](why-paperforge.md)
