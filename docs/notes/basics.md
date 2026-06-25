# Notes: Basics

This page covers the core API of `paperforge_notes`: themes, headings, body, and footers. By the end of this page you'll be able to construct a structured PDF document.

## Setting the theme

```python
import paperforge_notes as pn
pn.set_theme(pn.OCEAN_DARK)
```

Explore other themes: `DARK`, `LIGHT`, `FOREST_DARK`, `SUNSET_DARK`, `MIDNIGHT_DARK`, `OCEAN_LIGHT`, `SEPIA`, `CATPPUCCIN_LATTE`, `CATPPUCCIN_MOCHA`, `NOTION`, `GITHUB`, `LINEAR`, `ACADEMIC`, `TEXTBOOK`.

## The story

All helpers append into a global `story` list. To use PaperForge with a custom story list, redirect it:

```python
my_story = []
pn.set_story(my_story)
# ... add content ...
pn.build_doc("output.pdf")
```

You can inspect the current story with `pn.get_story()`. Set `pn.bookmarks_enabled = False` temporarily to suppress PDF outline/meta bookmarks without rewriting content.

This is useful for sandboxing multi-document compilations.

## Headings

| Helper | Visual | Auto-bookmarked? |
| ------ | ------ | ---------------- |
| `part_box("Unit I", subtitle=..., topics=[...])` | Large bordered card (Section Hero Page) | No |
| `chap_box("Chapter 1")` | Medium bordered card | Yes |
| `section("Subsection")` | Cyan-ruled heading | Yes |
| `subsection("Sub-subtopic")` | Smaller heading | Yes |

`part_box` serves as a premium section hero page when supplied with optional `subtitle` (str) and `topics` (list[str]). For example:
```python
pn.part_box(
    "Unit I: Basic Algorithms",
    subtitle="Big-O notation and sorting algorithms",
    topics=["Asymptotic Complexity", "Comparison Sorts", "Divide & Conquer"]
)
```

## Body content

```python
pn.body("Justified paragraph with HTML tags.")
pn.bullet(["First", "Second", "Third"])
pn.sp(8)        # 8pt vertical space
pn.rule()        # Cyan divider line
pn.br()          # Page break
```

`body()` supports inline HTML tags: `<b>`, `<i>`, `<font color="...">`, etc.

## Layout constants

```python
PAGE_W = 595  # A4 width (pt)
PAGE_H = 842  # A4 height
PM     = 51.02 # 1.8 cm margins
CW     = 493.0 # Content width = PAGE_W - 2*PM
```

## Footers and headers

```python
# Global footer
pn.set_global_footer(left="Course Notes", right="Session", show_page_num=True)

# Per-page footer override
pn.footer(left="Page specific", show_page_num=False, page_only=True)

# Suppress footer/header on a single page
pn.suppress_footer(page_only=True)

# Suppress footer for all pages after this point
pn.suppress_footer()

# Three-column header
pn.set_global_header(
    left="Algorithms",
    center="Unit I",
    right="Spring 2026"
)

# Per-page header override
pn.header(
    left="Chapter 1",
    visible=True,
    page_only=True
)
```

## Code blocks and tables

```python
# Syntax-highlighted code block
pn.code_block("""
public static void main(String[] args) {
    System.out.println("Hello, World!");
}
""", lang="java", theme="dracula")
```

Syntax-highlighting themes: `dracula`, `monokai`, `github-dark`, or any built-in `NotesTheme` name.

```python
# Information table with custom column widths
pn.info_table(
    ["Algorithm", "Best Case", "Worst Case"],
    [
        ["Quick Sort", "O(N log N)", "O(N^2)"],
        ["Merge Sort", "O(N log N)", "O(N log N)"],
    ],
    col_widths=["40%", "30%", "30%"]
)
```

## Page borders

```python
# Single-page border
pn.page_border(enabled=True, margin=15.0, color="#ffffff", page_only=True)

# Global double concentric border
pn.page_border(enabled=True, margin=15.0, gap=3.0)
```

## Page numbering

```python
# Default Arabic numerals
pn.page_numbering(style="arabic")

# Roman numerals for front matter
pn.page_numbering(style="roman")

# Reset counter on a new page
pn.page_numbering(style="arabic", reset_to=1)
```

## Cover pages

```python
pn.bookmark("Cover Page")
pn.suppress_footer(page_only=True)
pn.sp(40)
# Create a premium modern cover page
pn.cover_card(
    title="Discrete Mathematics",
    subtitle="Unit I: Logic",
    style="modern",
    author="Bharat Dangi",
    date="Spring 2026",
    ornament="diamond"
)
pn.br()
```

One-line `cover_preset()` bundles an icon, tags, and style for instant professional covers:

```python
pn.cover_preset("engineering", title="Computer Networks", subtitle="Complete Study Guide")
pn.br()

pn.cover_preset("networking", title="CCNA Notes", subtitle="Semester IV")
pn.br()
```

Built-in presets: `engineering`, `research-paper`, `course-notes`, `networking`, `database`, `programming`.

Add a faint SVG background illustration with `cover_image()`:

```python
pn.cover_image(
    "asset_images/network_topology.svg",
    opacity=0.06,
    placement="background"
)
```

Or use the convenience `add_cover()` helper which automates the bookmark/suppress/break boilerplate:

```python
pn.add_cover(
    title="My Notes",
    subtitle="Unit I",
    author="Bharat Dangi",
    style="modern",
    ornament="dots"
)
```

Supported cover page styles: `linear`, `notion`, `academic_modern`, `catppuccin`, `hero`, `book`, `diagram`, `modern`, `minimal`, `corporate`, `gradient`, `standard`, `academic`, `textbook`. Use `cover_theme` as a synonym for `style` when you prefer that naming. Supported ornaments: `diamond`, `dots`, `line`.

## Building the document

```python
pn.build_doc("output.pdf", title="Algorithms Notes", author="Bharat Dangi")
```

Additional output formats:

```python
pn.build_html("output/")             # Writes index.html into output directory
pn.build_pptx("output.pptx")         # PowerPoint with theme-matched slide backgrounds
```

Flashcard exports (`.csv`, `.json`, `.apkg`) are written automatically beside the PDF when `pn.flashcard()` is used.

## Next

- [Callouts](callouts.md)
- [Study helpers](study.md)
- [Advanced topics](advanced.md)
