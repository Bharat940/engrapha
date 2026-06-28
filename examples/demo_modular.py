"""
demo_modular.py -- Dedicated demo for compiling multiple source scripts and markdown files into one PDF.

Run:
    python demo_modular.py

To test document splitting:
    python demo_modular.py --split
"""

from __future__ import annotations
import sys
import engrapha_notes as en

# Set visual theme
en.set_theme(en.OCEAN_DARK)

# 1. Cover page
en.bookmark("Cover Page")
en.suppress_footer(page_only=True)
en.sp(40)
en.cover_card("Modular Notes Compiler", "Feature Showcase")
# en.cover_subtitle(
#     "Compiling multiple scripts & markdown documents into one cohesive PDF"
# )
en.br()

# 2. Table of Contents
en.suppress_footer(page_only=True)
en.toc()

# Set footer for the rest of the document
en.footer(left="Modular Notes Demo", right="engrapha Ecosystem", show_page_num=True)

# 3. Compile modular documents into the story flow
en.part_box("Unit I: Root Document Flow")
en.chap_box("1. Main Document Section")
en.body(
    "This is the root Python file content. Below, we dynamically compile external "
    "files (both Python scripts and Markdown) into this single story sequence."
)

# Include Python sub-script chapter 1
en.include_chapter("examples/temp_chapter.py")

# Include Markdown sub-chapter
en.include_markdown("examples/temp_markdown.md")

# Include Python sub-script chapter 2 (with diagrams)
en.include_chapter("examples/temp_chapter2.py")

# 4. Build output PDF
if "--split" in sys.argv:
    # Build and split document by part boundary
    en.build_split_doc("demo_modular.pdf", split_by="part")
    print("Generated split modular PDFs starting with demo_modular...")
else:
    # Build standard single cohesive PDF
    en.build_doc("demo_modular.pdf")
    print("Generated unified: demo_modular.pdf")
