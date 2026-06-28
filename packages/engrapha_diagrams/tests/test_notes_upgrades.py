from __future__ import annotations

import pytest
from io import BytesIO
import engrapha_notes as en

def test_code_block_with_theme() -> None:
    # Test that code_block with custom Pygments theme appends the styled table to the story
    en.get_story().clear()
    en.code_block("print('hello')", lang="python", theme=en.DRACULA)
    
    story = en.get_story()
    assert len(story) > 0
    # There should be a Table flowable in the story representing the code block
    table_flowables = [x for x in story if x.__class__.__name__ in ("Table", "CodeBlockTable")]
    assert len(table_flowables) == 1

def test_theme_builder() -> None:
    # Test creating a custom theme using ThemeBuilder
    builder = en.ThemeBuilder()
    builder.set_colors(bg="#112233", surface="#223344", accent="#556677")
    builder.set_fonts(body_font="Courier", heading_font="Courier-Bold", size_body=12.0)
    builder.set_borders(thickness=2.0, color="#ffffff")
    builder.set_header_footer(show_headers=False, divider_thickness=1.5)
    
    custom_theme = builder.build()
    
    assert custom_theme.bg == "#112233"
    assert custom_theme.surface == "#223344"
    assert custom_theme.accent == "#556677"
    assert custom_theme.body_font == "Courier"
    assert custom_theme.heading_font == "Courier-Bold"
    assert custom_theme.size_body == 12.0
    assert custom_theme.border_thickness == 2.0
    assert custom_theme.border_color == "#ffffff"
    assert custom_theme.show_headers is False
    assert custom_theme.divider_thickness == 1.5

def test_latex_features() -> None:
    # Test footnotes, cross-references, and index generation
    en.get_story().clear()
    
    # 1. Footnotes
    tag = en.footnote("A test footnote")
    assert tag == "<sup>1</sup>"
    
    # 2. Cross-references
    en.label("my-ref")
    en.body(f"Link to {en.ref('my-ref')}")
    
    # 3. Indexing
    en.index_entry("TestKeyword")
    en.print_index()
    
    story = en.get_story()
    # Verify they were added to story
    assert len(story) > 0
    
    # Render to bytes to verify multi-pass compilation works
    buf = BytesIO()
    en.build_doc(buf, story=story)
    pdf_data = buf.getvalue()
    
    assert pdf_data.startswith(b"%PDF")
    assert len(pdf_data) > 1000

def test_modular_compilation_and_splitting(tmp_path) -> None:
    pytest.importorskip("fitz")
    # 1. Create temporary py and md files
    py_file = tmp_path / "chapter1.py"
    py_file.write_text("import engrapha_notes as en\nen.chap_box('Chapter 1 Title')\nen.body('Chapter 1 content')", encoding="utf-8")

    md_file = tmp_path / "chapter2.md"
    md_file.write_text("---\ntitle: Submarkdown\n---\n# Chapter 2 Title\nMarkdown body content", encoding="utf-8")

    en.get_story().clear()
    en.include_chapter(str(py_file))
    en.include_markdown(str(md_file))

    story = en.get_story()
    assert len(story) > 0
    # There should be chap_box and part_box flowables
    assert any(getattr(x, "_is_chap_box", False) for x in story)
    assert any(getattr(x, "_is_part_box", False) for x in story)

    # Test splitting by section
    out_pdf = tmp_path / "main.pdf"
    en.build_split_doc(str(out_pdf), split_by="chapter", reset_page_numbers=False)

    # Check that it generated split files
    split_files = list(tmp_path.glob("main_*.pdf"))
    assert len(split_files) == 2
    # Verify both exist and are valid PDFs
    for f in split_files:
        assert f.stat().st_size > 1000

    # Test splitting by page range (interval)
    en.get_story().clear()
    en.chap_box("Topic 1")
    en.body("Short text")
    en.br()
    en.chap_box("Topic 2")
    en.body("More text")

    out_interval_pdf = tmp_path / "interval.pdf"
    en.build_split_doc(str(out_interval_pdf), page_interval=1)
    
    interval_files = list(tmp_path.glob("interval_pages_*.pdf"))
    assert len(interval_files) >= 2

def test_educational_templates() -> None:
    # Test EngineeringNotes
    eng_theme = en.EngineeringNotes(dark=True)
    assert eng_theme.name == "Engineering Notes"
    assert eng_theme.body_font == "Helvetica"
    assert eng_theme.heading_font == "Helvetica-Bold"
    assert eng_theme.size_body == 10.0
    assert en.get_theme() == eng_theme

    # Test QuestionBank
    qb_theme = en.QuestionBank(dark=False)
    assert qb_theme.name == "Question Bank"
    assert qb_theme.body_font == "Times-Roman"
    assert qb_theme.heading_font == "Times-Bold"
    assert qb_theme.size_body == 9.5
    assert en.get_theme() == qb_theme
