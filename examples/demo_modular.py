"""
demo_modular.py -- Dedicated demo for compiling multiple source scripts and markdown files into one PDF.

Run:
    python demo_modular.py

To test document splitting:
    python demo_modular.py --split
"""

from __future__ import annotations
import sys
import paperforge_notes as pn

# Set visual theme
pn.set_theme(pn.OCEAN_DARK)

# 1. Cover page
pn.bookmark("Cover Page")
pn.suppress_footer(page_only=True)
pn.sp(40)
pn.cover_card("Modular Notes Compiler", "Feature Showcase")
pn.cover_subtitle(
    "Compiling multiple scripts & markdown documents into one cohesive PDF"
)
pn.br()

# 2. Table of Contents
pn.suppress_footer(page_only=True)
pn.toc()

# Set footer for the rest of the document
pn.footer(left="Modular Notes Demo", right="PaperForge Ecosystem", show_page_num=True)

# 3. Compile modular documents into the story flow
pn.part_box("Unit I: Root Document Flow")
pn.chap_box("1. Main Document Section")
pn.body(
    "This is the root Python file content. Below, we dynamically compile external "
    "files (both Python scripts and Markdown) into this single story sequence."
)

# Include Python sub-script chapter 1
pn.include_chapter("temp_chapter.py")

# Include Markdown sub-chapter
pn.include_markdown("temp_markdown.md")

# Include Python sub-script chapter 2 (with diagrams)
pn.include_chapter("temp_chapter2.py")

# 4. Build output PDF
if "--split" in sys.argv:
    # Build and split document by part boundary
    pn.build_split_doc("demo_modular.pdf", split_by="part")
    print("Generated split modular PDFs starting with demo_modular...")
else:
    # Build standard single cohesive PDF
    pn.build_doc("demo_modular.pdf")
    print("Generated unified: demo_modular.pdf")
