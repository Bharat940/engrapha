# Why Engrapha?

Several tools can help you produce diagrams or notes. Engrapha's value is combining all of them into one Python toolkit with vector-native graphics, consistent theming, and multi-format exports.

## Feature comparison

<div class="grid cards" markdown>

| Tool | Notes | Diagrams | PDF | HTML | PPTX |
| ---- | ----- | -------- | --- | ---- | ---- |
| **ReportLab** | ❌ | ❌ | ✅ | ❌ | ❌ |
| **Mermaid** | ❌ | ✅ | ❌ | ❌ | ❌ |
| **PlantUML** | ❌ | ✅ | ❌ | ❌ | ❌ |
| **Matplotlib** | ❌ | Limited | ✅ | ❌ | ❌ |
| **Pandoc** | ✅ | Limited | ✅ | ✅ | ❌ |
| **Typst** | ✅ | Limited | ✅ | ✅ | ❌ |
| **LaTeX** | ✅ | Limited | ✅ | ❌ | ❌ |
| **Engrapha** | ✅ | ✅ | ✅ | ✅ | ✅ |

</div>

## What makes Engrapha different

### 1. Vector-native diagrams inside your PDF

Every diagram is drawn as ReportLab vector primitives. No PNG rasters, no missing fonts, no JavaScript runtime. The same drawing renders at any zoom level and stays editable.

```python
fc = ed.Flowchart(width=en.CW, height=180)
fc.terminal("start", "START")
fc.process("step", "Main")
fc.terminal("end", "END")
fc.edge("start", "step").edge("step", "end")
en.add(fc.as_flowable())
```

### 2. Unified themes across notes and diagrams

Apply the same theme to body text, callouts, tables, code blocks, **and** every diagram. Switch from `DARK` to `OCEAN_DARK` to `SEPIA` with one call:

```python
en.set_theme(en.OCEAN_DARK)
diag_theme = ed.DiagramTheme.from_notes_theme(en.get_theme())
fc = ed.Flowchart(theme=diag_theme, ...)
```

### 3. Multi-format export from one source

Generate PDF, HTML, PPTX, and Anki flashcards from the same Python script (or Markdown file).

```python
en.build_doc("notes.pdf")        # PDF
en.build_html("notes/")          # HTML (writes index.html into directory)
en.build_pptx("notes.pptx")      # Presentation
# Flashcards auto-exported to *_flashcards.csv/json/.apkg
```

### 4. Zero external tooling

No need to install `chrome`, `puppeteer`, `lualatex`, `java`, `node`, or an internet connection. Engrapha works on any machine that can run pip + Python.

### 5. Markdown-first CLI

Write notes in Markdown, get a themed PDF. Diagram fences, alert boxes, code blocks, and tables all compile natively.

```bash
Engrapha notes.md --theme catppuccin-mocha
```

## When to use Engrapha

Pick Engrapha if you:

- Need a **single Python script** that produces both notes and diagrams
- Want **no external binaries** (no LaTeX, no PlantUML Java)
- Care about **visual consistency** between text and graphics
- Are building **academic content** (study notes, question banks, slides)
- Need **multiple output formats** from one source

Pick something else if you:

- Are building a static **web-only** documentation site (**Pick**: Material for MkDocs, Docusaurus)
- Need **collaborative** real-time editing (**Pick**: Notion, HackMD)
- Want full **LaTeX control** with macros (**Pick**: LuaLaTeX or Typst)

## Next steps

- [Install Engrapha](getting-started.md)
- [Browse the gallery](gallery/index.md)
- [Make themed notes](notes/basics.md)

