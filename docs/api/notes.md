# API Reference: paperforge_notes

Quick reference grouped by purpose. Full docstrings are in the source.

## Theme

```python
pn.set_theme(theme)           # Set active theme
pn.get_theme()                # Return current NotesTheme
pn.DARK / pn.LIGHT            # Presets
pn.OCEAN_DARK, ...           # (15 total)
pn.EngineeringNotes(dark=True)
pn.QuestionBank(dark=False)
```

```python
import paperforge_notes as pn
from paperforge_notes import ThemeBuilder

custom = (
    ThemeBuilder()
    .set_colors(bg="#0a0e27", surface="#1b2540", accent="#fbbf24")
    .set_fonts(body_font="Times-Roman", heading_font="Times-Bold",
               size_body=10.0, size_question=11.5)
    .set_borders(thickness=1.2, color="#fbbf24")
    .set_double_border(enabled=True, margin=15.0, gap=3.0,
                       color="#fbbf24")
    .set_header_footer(show_headers=True, divider_thickness=0.6)
    .build()
)
pn.set_theme(custom)
```

## Constants

```python
PAGE_W, PAGE_H, PM, CW     # A4 constants
```

## Story management

```python
pn.set_story(list)           # Replace global story
pn.get_story()               # Inspect it
pn.add(flowable_or_list)     # Append anything
pn.sp(h=8)                   # Vertical spacer
```

## Structure and headings

```python
pn.part_box(text, subtitle=None, topics=None)
pn.chap_box(text, bookmark=True)
pn.section(text, bookmark=True, keep_with_next=True)
pn.subsection(text, bookmark=True)
pn.cover_card(title, subtitle=None, width=None, style="standard", author=None, date=None, ornament=None, tags=None, icon=None, cover_theme=None)
```

## Body and lists

```python
pn.body(text, font_name, font_size, text_color, leading)
pn.bullet(items)
pn.rule(color, thickness, keepWithNext)
pn.br()
```

## Callouts

| Helper | Use case |
| -------- | -------- |
| `tip(text)` | Green exam tip |
| `note(text)` | Yellow note |
| `warning(text)` | Red safety warning |
| `important(text)` | Purple key concept |
| `exam(text)` | Yellow exam focus |
| `highlight(text)` | Yellow generic emphasis |
| `definition(text)` | Light surface box |
| `theorem(text)` | Purple theorem box |
| `proof(text)` | Italic indented proof ending in Q.E.D. |

```python
pn.tip("Average O(N log N)")
pn.note("Uses random pivot")
pn.warning("Crash if list empty")
pn.important("Revisit this")
pn.exam("Exam: 2023-03 Q1")
pn.highlight("Remember this invariant")
pn.definition("In-place algorithm when O(1) extra space")
pn.theorem("Fermat's Last Theorem")
pn.proof("By contradiction, ...")
```

## Study helpers

```python
pn.question(text, ...)        # Left-bordered question
pn.qbox(text, ...)           # Boxed question card (full border)
pn.answer(text, ...)         # Green left border
pn.mcq(question, options, correct_index=None)
pn.revision_card(title, points)
pn.flashcard(question, answer)
```

## Advanced layout

```python
pn.toc(style="index", bookmark=True, ...)  # 'standard', 'minimal', 'detailed', 'grid', 'index'
pn.bookmark(name_or_key)
pn.label(ref_id)             # Anchor for cross-reference
pn.footnote(text)            # Inline footnote
pn.ref(ref_id)               # Resolved page number
pn.index_entry(keyword)      # Register in index
pn.print_index()             # Render compiled index table
pn.suppress_header(page_only=True)
pn.suppress_footer(page_only=True)
pn.set_global_header(left, center, right, ...)
pn.set_global_footer(left, center, right, show_page_num, ...)
pn.header(left, center, right, visible, page_only, ...)  # Per-page header override
pn.page_border(enabled, margin, gap, color, double, page_only)
pn.page_numbering(style, reset_to)
```

## Figures and content

```python
pn.code_block(text, lang=None, theme=None)   # Pygments syntax highlight
pn.formula(latex_str)                          # Inline SVG/PNG formula
pn.formula_block(latex_str)                    # Centered display math
pn.image(src, width, height, caption, link, fallbacks)
pn.info_table(headers, rows, col_widths, hdr_color, hdr_text_color)
pn.frame_format(caption, fields)              # Horizontal frame
pn.packet_format(caption, fields, bit_ruler=True)  # 32-bit bit-grid
```

## Modular compilation

```python
pn.include_chapter(py_file_path)
pn.include_markdown(md_file_path)
pn.build_split_doc(filename, split_by="chapter", page_interval=None)    # 'chapter', 'part', or integer page_interval
```

## Build targets

```python
pn.build_doc(filename, title, author)     # PDF
pn.build_html(output_dir)                  # HTML (writes index.html into directory)
pn.build_pptx(filename)                    # PPTX
# Flashcards (CSV, JSON, APKG) auto-exported beside PDF
```

## Output constants

```python
pn.BG, pn.CYAN, pn.GREEN, pn.YELLOW, pn.WHITE  # Palette
pn.BODY_ST, pn.SECT_ST, pn.CODE_ST, ...        # Paragraph styles
pn.COVER_H1, pn.COVER_H2, ...                  # Cover styles
pn.H1, pn.H2, pn.H3, pn.H4, pn.H5, pn.H6     # Heading styles
```
