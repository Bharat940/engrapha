![PaperForge](../assets/paperforge_logo_black.svg)
# 📝 paperforge_notes

[![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Format](https://img.shields.io/badge/format-PDF%20%7C%20HTML%20%7C%20PPTX%20%7C%20Anki-orange.svg)](#)

A themed ReportLab notes template generator with a built-in markdown compiler CLI. 

It provides a simple, structured Python API to build beautiful academic notes, question banks, study guides, slides, and flashcards with unified dark/light themes and native vector diagrams.

---

## 🚀 Features

* **Premium Cover Pages**: Screenshot-worthy covers with `linear`, `notion`, `academic_modern`, `catppuccin`, `hero`, `book`, `diagram`, `modern`, `minimal`, `corporate`, `gradient`, `standard`, `academic`, and `textbook` styles. Tags, icons, and SVG background illustrations.
* **Built-in Presets**: One-line presets (`pn.cover_preset()`) for instant professional covers: `engineering`, `research-paper`, `course-notes`, `networking`, `database`, `programming`.
* **Table Column Control & Wrapping**: Custom column widths in `pn.info_table` and `pn.toc(style="index")`. Cells automatically wrap long words (>24 characters) using zero-width font-size spaces, avoiding clipping and missing-glyph black boxes in standard PDF fonts.
* **Mathematical Formulas**: Render LaTeX syntax inline or as centered equation blocks (`pn.formula()`, `pn.formula_block()`).
* **Textbook Callouts**: Semantic helper blocks including `warning()`, `important()`, `exam()`, `definition()`, `theorem()`, and `proof()`.
* **Study & Revision**: Build integrated study materials using `pn.question()`, `pn.qbox()`, `pn.answer()`, and `pn.mcq()`.
* **Flashcards & Anki Export**: Automatically compile definitions into interactive flashcards via `pn.flashcard()` and export directly to Anki `.apkg` format.
* **Multi-Format Publishing**: Export a single source document to PDF, HTML (`pn.build_html()`), and PowerPoint (`pn.build_pptx()`).
* **Themed Layouts**: 15 preset configurations for document-wide visual themes (Notion, GitHub, Linear, Academic, Textbook, Catppuccin, Sepia, etc.).
* **ThemeBuilder**: Custom dynamic theming engine to construct bespoke document layouts.
* **Prebuilt Templates**: Optimized formatting defaults like `EngineeringNotes` (technical manuals) and `QuestionBank` (exam papers/worksheets).
* **LaTeX-like Features**: Support for footnotes, cross-reference anchors, and compiled index tables.
* **Modular Compilation**: Combine multiple sub-scripts or markdown chapters using `pn.include_chapter()` and `pn.include_markdown()`.
* **Document Splitting**: Automate partitioning large documents by chapter boundaries or page ranges via `pn.build_split_doc()`.
* **Markdown CLI Compiler**: Compile standard Markdown files (with alerts and diagram blocks) directly to themed PDFs.

---

## 📦 Installation

Install the package locally:

```bash
# Core: notes, diagrams, PDF export, syntax highlighting
pip install ./paperforge_notes

# Full: adds PPTX export, document splitting, and Anki export
pip install ./paperforge_notes[full]
```

---

## 🐍 Python API Usage

### 1. Premium Cover Pages

Create screenshot-worthy covers with modern styles, tags, icons, and background illustrations.

```python
import paperforge_notes as pn

# Simple cover with built-in preset
pn.cover_preset(
    "engineering",
    title="Computer Networks",
    subtitle="Complete Study Guide",
    author="Bharat Dangi",
    date="June 2026",
)

# Or build a custom premium cover
pn.cover_card(
    title="Computer Networks",
    subtitle="Complete Engineering Notes",
    author="Bharat Dangi",
    cover_theme="linear",          # or style="linear"
    icon="&#128187;",              # emoji or text icon
    tags=[
        "Networking",
        "Semester IV",
        "Exam Notes"
    ],
)

# Add a faint SVG background illustration (optional svglib for native vector)
pn.cover_image(
    "asset_images/network_topology.svg",
    opacity=0.06,
    placement="background",
)

pn.br()
```

### Cover Gallery

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

### 2. Basic Note Structuring

```python
import paperforge_notes as pn

# Choose a theme
pn.set_theme(pn.DARK)

# Create a cover page
pn.bookmark("Cover Page")
pn.suppress_footer(page_only=True)
pn.sp(40)
pn.cover_card("Computer Science Notes", "Unit I: Basics", style="modern", author="Bharat Dangi")
pn.br()

# IMPORTANT: Do not call pn.bookmark() manually for standard sections!
# pn.chap_box() and pn.section() automatically register themselves in the TOC.

# Add Table of Contents
pn.suppress_footer(page_only=True)
pn.toc(style="standard")

# Main content
pn.footer(left="Algorithms", right="Unit I", show_page_num=True)
pn.part_box(
    "Unit I: Basic Algorithms",
    subtitle="Analysis of sorting and search methods",
    topics=["Complexity Theory", "Divide & Conquer", "Pivot Selection"]
)
pn.chap_box("1.1 Sorting")
pn.section("Quick Sort")
pn.body("Quick Sort is a divide-and-conquer sorting algorithm.")
pn.tip("Average case time complexity is O(N log N).")
pn.note("Worst case time complexity is O(N^2) when the pivot is poorly chosen.")

# Compile the document
pn.build_doc("sorting_notes.pdf")
```

### 3. Code Blocks and Tables

```python
import paperforge_notes as pn

# Syntax-highlighted code block with Dracula theme
pn.code_block("""
public static void main(String[] args) {
    System.out.println("Hello, World!");
}
""", lang="java", theme=pn.DRACULA)

# Multi-column information tables with custom column widths
pn.info_table(
    ["Algorithm", "Best Case", "Worst Case"],
    [
        ["Quick Sort", "O(N log N)", "O(N^2)"],
        ["Merge Sort", "O(N log N)", "O(N log N)"],
    ],
    col_widths=["40%", "30%", "30%"]
)
```

### 4. Images (Local & Remote)

You can render images from local paths or remote URLs directly into your document. Remote URLs are automatically downloaded and cached locally in `.paperforge_cache/images` for offline access and speed.

#### Sizing and Hyperlink Example

```python
import paperforge_notes as pn

# Local image with caption and hyperlink
pn.image(
    "asset_images/von_neumann.png",
    caption="Fig 1: Von Neumann Architecture (Local)",
    link="https://en.wikipedia.org/wiki/Von_Neumann_architecture"
)

# Remote image from a URL (will be auto-cached) with specific size
pn.image(
    "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png",
    caption="Fig 2: Google Logo (Remote)",
    width=200,
    height=68,
    link="https://www.google.com"
)
```

#### Fallbacks & Warning Placeholders

The image system includes two layers of fallback protection:
1. **User-defined Fallbacks**: You can supply one or more fallback image sources via the `fallbacks` parameter.
2. **Default Placeholder Box**: If all sources fail, the compiler renders a styled warning placeholder box.

```python
import paperforge_notes as pn

pn.image(
    "https://invalid-domain.com/nonexistent_image.png",
    fallbacks=[
        "https://alternative-invalid.com/backup.jpg",
        "asset_images/von_neumann.png"
    ],
    caption="Von Neumann (Loaded via Fallbacks)"
)
```

### 5. LaTeX-like Features & References

```python
# Label a section
pn.section("Advanced Sorting")
pn.label("sec_adv_sort")

# Add a footnote and index entry
pn.body(f"We can use random pivots{pn.footnote('A random pivot yields O(N log N) average complexity with high probability.')}.")
pn.index_entry("Randomized Quick Sort")

# Cross-reference
pn.body(f"For details on advanced sorting, see the section on Page {pn.ref('sec_adv_sort')}.")

# Print the generated index table
pn.print_index()
```

### 6. Advanced Styling, Custom Layouts & Overrides

```python
import paperforge_notes as pn

# Custom Print Theme with Double Page Borders
print_theme = pn.LIGHT.copy_with(
    name="Print Light",
    body_font="Times-Roman",
    heading_font="Times-Bold",
    size_body=10.0,
    size_question=12.0,
    double_page_border=True,
    page_border_margin=15.0,
    page_border_gap=3.0,
    plain_questions=True,
)
pn.set_theme(print_theme)

# Three-Column Running Headers & Footers
pn.set_global_header(
    left="Indian Constitution Notes",
    center="Semester – IV",
    right="Session-Jan-June 2025"
)
pn.set_global_footer(
    left="Name: Bharat Dangi",
    center="Enrollment no: 0101IT241013",
    show_page_num=True
)

# Suppression of Headers/Footers on Specific Pages
pn.bookmark("Cover Page")
pn.suppress_header(page_only=True)
pn.suppress_footer(page_only=True)
pn.cover_card("Indian Constitution", "Unit 1: Basics")
pn.br()

# Multi-Page Grid-Based INDEX / Table of Contents
pn.toc(style="index", col_widths=["10%", "29%", "10%", "16%", "14%", "7%", "14%"])

# Component-Level Typography and Color Overrides
pn.qbox(
    "What is Constitutionalism?",
    font_name="Times-Bold",
    font_size=12,
    text_color="#ff0000",
    bg_color="#ffffff",
    border_color="#000000"
)
pn.body("Constitutionalism refers to the limitation of government by law.")
```

### 7. Textbook Callouts & Study Helpers

```python
import paperforge_notes as pn

pn.warning("High voltage! Do not touch or operate this equipment without safety gear.")
pn.important("Amdahl's Law defines the theoretical speedup in latency of execution.")
pn.exam("Amdahl's law is a frequent question on computer organization exams!")
pn.theorem("For any right-angled triangle, a^2 + b^2 = c^2.")
pn.proof("By constructing four identical triangles around a square...")

pn.question("State the difference between latency and throughput.")
pn.answer("Latency is the time delay for a single task; throughput is tasks per unit time.")
pn.qbox("Draw and explain the Von Neumann architecture.")

pn.mcq(
    "Which algorithm is quickest in the worst-case scenario?",
    ["Quick Sort", "Bubble Sort", "Merge Sort", "Insertion Sort"],
    correct_index=2
)

pn.revision_card("Key Metrics", [
    "Average Latency",
    "Tail Latency (p99)",
    "Throughput",
    "Resource Utilization"
])

pn.flashcard("Von Neumann Bottleneck", "The throughput limitation between CPU and memory.")
```

### 8. Frame and Packet Formats

```python
import paperforge_notes as pn

pn.frame_format(
    "Ethernet Frame Structure",
    [
        ("PREAMBLE", "7B"),
        ("SFD", "1B"),
        ("DEST MAC", "6B"),
        ("SRC MAC", "6B"),
        ("TYPE", "2B"),
        ("PAYLOAD", "46-1500B"),
        ("FCS", "4B"),
    ]
)

pn.packet_format(
    "IPv4 Header Format",
    [
        ("Version", 4),
        ("IHL", 4),
        ("DSCP", 6),
        ("ECN", 2),
        ("Total Length", 16),
        ("Identification", 16),
        ("Flags", 3),
        ("Fragment Offset", 13),
        ("TTL", 8),
        ("Protocol", 8),
        ("Header Checksum", 16),
        ("Source IP Address", 32),
        ("Destination IP Address", 32),
    ],
    bit_ruler=True
)
```

---

## 💻 Markdown CLI Compiler

You can compile markdown notes files directly to PDF via the command line interface using either `paperforge` or `pdfnotes`:

```bash
paperforge input.md --output output.pdf --theme catppuccin-mocha
```

### Options:
* `input`: Path to input markdown file.
* `-o, --output`: Custom output path (defaults to input path with `.pdf` extension).
* `-t, --theme`: Theme name (default: `dark`).
* `--title`: Custom document title.
* `--author`: Custom document author.

### Supported Themes:
* `dark` (default)
* `light`
* `ocean-dark`
* `forest-dark`
* `sunset-dark`
* `midnight-dark`
* `ocean-light`
* `sepia`
* `catppuccin-latte`
* `catppuccin-mocha`

### Alert Boxes Mapping:
GitHub-style alert blocks are parsed and compiled automatically:
* `> [!NOTE]` &rarr; Yellow note box (via `pn.note`)
* `> [!TIP]` &rarr; Green exam-tip box (via `pn.tip`)
* `> [!WARNING]` / `> [!CAUTION]` &rarr; Yellow-bordered container box (via `pn.highlight`)

### Embedded Diagrams Syntax:
You can embed diagrams inside markdown using simple text DSL blocks:

```markdown
```flowchart
width = 400
height = 200
caption = Fig 1: Basic Process Flow
direction = LR
scale_factor = 1.0
terminal start "START"
process step "Compute Value"
terminal end "END"

edge start step
edge step end
```
```

*Supported diagram block types:* `flowchart`, `sequence`, `layeredstack`, `schema`/`er`, `git`, `architecture`/`arch`, `c4`/`c4container`, `aws`/`cloud`. (Other diagram types like `classdiagram` or `statemachine` must be compiled using Python script).

---

## 📝 Diagram Integration & Static Type Checking

When integrating diagrams created with `paperforge_diagrams` into a notes document, always use `pn.add(diagram.as_flowable())` instead of manipulating the internal `story` list directly.

### Resolving Pyright / Pylance Warnings
Static type checkers (like Pyright or Pylance in VS Code) might flag a type mismatch warning when passing a diagram list to `add()` if the signature is not correctly handled:
> `Argument of type "list[Unknown]" cannot be assigned to parameter "x" of type "Flowable" in function "add"`

This happens because `as_flowable()` returns a `list[Flowable]` (which packages the drawing flowable along with its optional caption Paragraph flowable) rather than a single `Flowable`.

**Solution:**
The `pn.add()` API accepts a union of a single flowable or a list of flowables and flattens them automatically:
```python
def add(x: Flowable | list[Flowable] | tuple[Flowable, ...]) -> None:
```

---

## 📋 Requirements & License

* **Python** >= 3.11
* **reportlab** >= 4.5.1
* **pygments** >= 2.20.0
* **paperforge-diagrams** >= 0.1.0

Optional (extended features — install with `[full]`):
* **pymupdf** >= 1.25.0 (PPTX export, document splitting)
* **genanki** >= 0.13.1 (Anki `.apkg` export)

Licensed under the **MIT License**.
