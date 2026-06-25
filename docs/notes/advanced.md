# Notes: Advanced

Advanced ingredients you will need for full-length textbooks, lab reports, and research notes.

## TOC and bookmarks

```python
# Automatic multi-page Table of Contents
pn.toc(style="index")           # 'standard', 'minimal', 'detailed', 'grid', 'index'

# Manual bookmarks (rarely needed — most sections auto-register)
pn.bookmark("Appendix")
```

TOC styles:

| Style | Best for |
|-------|----------|
| `standard` | Clean TOC |
| `minimal` | Minimalist TOC |
| `detailed` | With page numbers |
| `grid` | Tabular TOC |
| `index` | Multi-column grid best for appendix/keyword indexes |

## Images

```python
# Local
pn.image("asset_images/von_neumann.png", width=200, height=120,
         caption="Fig 1: Von Neumann architecture",
         link="https://en.wikipedia.org/wiki/Von_Neumann_architecture")

# Remote (cached automatically)
pn.image("https://.../photo.png", width=200, height=120,
         caption="Remote image",
         fallbacks=[
             "https://alternative/mirror.png",
             "asset_images/local_backup.png",
         ])
```

If all sources fail, PaperForge renders a styled placeholder instead of crashing.

## LaTeX formulas

Inline formulas auto-cache PNG images:

```python
pn.body(f"The area is A = {pn.formula('\\pi r^2')}.")
```

Display math equations:

```python
pn.formula_block(r"\int_a^b f(x)\, dx = F(b) - F(a)")
```

These use matplotlib's mathtext engine (no LaTeX installation required).

## References and index

```python
pn.section("Advanced Sorting")

pn.label("sec_adv_sort")

pn.body(
    f"We can use random pivots"
    f"{pn.footnote('A random pivot yields expected O(N log N) time.')}."
)

pn.index_entry("Randomized Quick Sort")

pn.body(
    f"For details see the section on Page {pn.ref('sec_adv_sort')}."
)

# Print the index at the end of the document
pn.print_index()
```

## Modular compilation

```python
pn.include_chapter("chapter_01.py")       # Run and merge a Python script
pn.include_markdown("chapter_02.md")      # Parse and merge Markdown
pn.build_split_doc(                       # Split into chapter PDFs
    "output_prefix_",
    split_by="chapter",                   # 'chapter' or integer
)
```

## Page numbering resets

```python
pn.page_numbering(style="arabic")

# Per-page header override
pn.header(
    left="Chapter 1",
    visible=True,
    page_only=True
)

# Reset counter on a new page
pn.page_numbering(style="roman", reset_to=1)
```

## Packet and frame formats

Draw horizontal hardware frames or RFC-style 32-bit aligned packet grid layouts:

```python
# 1. Horizontal frame structure
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

# 2. RFC-style 32-bit packet grid
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

## Next

- [Export formats](export.md)
- [Templates](templates.md)
