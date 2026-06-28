# Notes: Templates

Engrapha ships built-in helpers for common document types. Each returns a ready-to-use `NotesTheme`, so you do not have to configure fonts, colors, and layout manually.

## EngineeringNotes

```python
en.EngineeringNotes(dark=True)
```

Dark-themed, monospaced-code-friendly, optimized for CS/IT lecture notes.

## QuestionBank

```python
en.QuestionBank(dark=False)
```

Light-mode, Times-Roman serif, exam-paper aesthetic.

## ThemeBuilder

Use the fluent `ThemeBuilder` to construct a custom theme from scratch:

```python
custom = (
    en.ThemeBuilder()
    .set_colors(bg="#0a0e27", surface="#1b2540", accent="#fbbf24")
    .set_fonts(body_font="Times-Roman", heading_font="Times-Bold",
               size_body=10.0, size_question=11.5)
    .set_borders(thickness=1.2, color="#fbbf24")
    .set_double_border(enabled=True, margin=15.0, gap=3.0,
                       color="#fbbf24")
    .set_header_footer(show_headers=True, divider_thickness=0.6)
    .build()
)
en.set_theme(custom)
```

## Code block syntax themes

Pass a theme name string to `en.code_block()` for syntax highlighting:

```python
en.code_block("print('hello')", lang="python", theme="dracula")
en.code_block("fn main() {}", lang="rust", theme="monokai")
en.code_block("SELECT * FROM users", lang="sql", theme="github-dark")
```

Available option strings: `dracula`, `monokai`, `github-dark`. Any built-in theme preset name (e.g. `DARK`, `LIGHT`, `CATPPUCCIN_MOCHA`) also works.

## Custom templates via copy_with

Extend any existing preset with `copy_with`:

```python
print_theme = en.LIGHT.copy_with(
    name="Print Light",
    body_font="Times-Roman",
    heading_font="Times-Bold",
    double_page_border=True,
    page_border_margin=15.0,
    page_border_gap=3.0,
    plain_questions=True,
)
en.set_theme(print_theme)
```

## Expected templates (coming soon)

| Template | Target use case |
| -------- | --------------- |
| `ResearchPaper()` | IEEE / CMU formatted research papers |
| `Resume()` | ATS-friendly resume |
| `LabReport()` | Lab notebook format |
| `Assignment()` | Student assignment / worksheet |
| `CheatSheet()` | Double-column compact cheat sheet |

Open issues requesting these are tracked on GitHub.

## Next

- [Export formats](export.md)

