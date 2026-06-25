# Themes

PaperForge comes with **10 preset themes** for `paperforge_diagrams` and **15 preset themes** for `paperforge_notes`.

## Preset themes

| Theme | Best for |
| ----- | -------- |
| `DARK` (default) | General-purpose dark mode |
| `LIGHT` | Daylight reading |
| `OCEAN_DARK` | Fullscreen programming and maths |
| `FOREST_DARK` | Calmer, green-accented dark mode |
| `SUNSET_DARK` | Warm, orange-tinted dark mode |
| `MIDNIGHT_DARK` | Indigo/purple accent dark mode |
| `OCEAN_LIGHT` | Bright cyan-accented light mode |
| `SEPIA` | Print-blended warm light mode |
| `CATPPUCCIN_LATTE` | Catppuccin Latte (light) |
| `CATPPUCCIN_MOCHA` | Catppuccin Mocha (dark) |
| `NOTION` | Clean, Notion-like light design |
| `GITHUB` | Standard light mode resembling GitHub |
| `LINEAR` | Sleek, dark mode resembling Linear |
| `ACADEMIC` | Serif-heavy, formal print layout |
| `TEXTBOOK` | High-contrast teal and white print layout |

## Apply a theme

```python
import paperforge_notes as pn
pn.set_theme(pn.OCEAN_DARK)
```

## Match Diagrams to Notes

Every diagram accepts a theme. To make diagrams inherit the active notes theme:

```python
import paperforge_diagrams as pd
fc = pd.Flowchart(theme=pd.DiagramTheme.from_notes_theme(pn.get_theme()))
```

All element colors (fill, stroke, text) carry over from the notes theme to the diagram.

## Build your own theme

Use the fluent `ThemeBuilder` to construct a custom theme:

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

### Builder methods

| Method | Purpose |
| ------ | ------- |
| `set_colors(bg, surface, accent)` | Set primary colors |
| `set_fonts(body_font, heading_font, size_body, size_question)` | Set font family and sizes |
| `set_borders(thickness, color)` | Set callout border thickness and color |
| `set_double_border(enabled, margin, gap, color)` | Configure concentric page borders |
| `set_header_footer(show_headers, divider_thickness)` | Configure header line visibility |

## Theme-from-Accent

For quick experimentation, build a theme from a single accent color:

```python
from paperforge_notes.theme import NotesTheme
custom = NotesTheme.from_accent("#22d3ee", dark=True, name="My Cyan")
pn.set_theme(custom)
```

## Predefined templates

`paperforge_notes` ships with two named template helpers:

```python
pn.EngineeringNotes()  # Helvetica body, dark mode
pn.QuestionBank()      # Times-Roman, light mode, exam-friendly
```

These are ready-to-use helpers that call `set_theme()` for you.

## Print-friendly themes

For ink-saving printouts, you can override the print theme:

```python
print_theme = pn.LIGHT.copy_with(
    name="Print Light",
    body_font="Times-Roman",
    heading_font="Times-Bold",
    double_page_border=True,
    page_border_margin=15.0,
    page_border_gap=3.0,
    plain_questions=True,
)
pn.set_theme(print_theme)
```

## Inspecting the active theme

```python
t = pn.get_theme()
print(t.name)
print(t.accent, t.text, t.bg)
```

## Next

- [Notes basics](notes/basics.md)
- [Diagram overview](diagrams/overview.md)
