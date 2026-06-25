from __future__ import annotations

import pytest
import paperforge_notes as pn
import paperforge_diagrams as pd

def test_pptx_and_html_compilers(tmp_path) -> None:
    pytest.importorskip("pptx")
    pn.get_story().clear()
    
    # Add various structural items to test partitioning
    pn.part_box("Unit I: Overview")
    pn.chap_box("Chapter 1: Intro")
    pn.section("1.1 Background")
    pn.body("This is some body text.")
    
    # Add a custom diagram flowable to test slide diagram rendering
    fc = pd.Flowchart(width=200, height=100)
    fc.terminal("start", "Start")
    pn.get_story().extend(fc.as_flowable())
    
    # Export slide deck
    pptx_path = tmp_path / "presentation.pptx"
    pn.build_pptx(str(pptx_path))
    assert pptx_path.exists()
    assert pptx_path.stat().st_size > 1000
    
    # Export HTML static site
    html_dir = tmp_path / "website"
    pn.build_html(str(html_dir))
    index_file = html_dir / "index.html"
    assert index_file.exists()
    assert index_file.stat().st_size > 1000
    
    # Verify index.html contains the HTML structure, the title, and the flowchart diagram svg block
    with open(index_file, "r", encoding="utf-8") as f:
        html_content = f.read()
    assert "Unit I: Overview" in html_content
    assert "Chapter 1: Intro" in html_content
    assert "<svg" in html_content
    assert "Start" in html_content

def test_anki_flashcard_exporter(tmp_path) -> None:
    pn.get_story().clear()
    
    # Register some study cards
    pn.flashcard("What is TCP?", "Transmission Control Protocol - reliable and connection-oriented.")
    pn.flashcard("Formula for Circle Area", "$A = \\pi r^2$")
    
    pdf_path = tmp_path / "document.pdf"
    pn.build_doc(str(pdf_path))
    
    # Verify Anki and text files were created next to the output PDF
    apkg_path = tmp_path / "document.apkg"
    csv_path = tmp_path / "document_flashcards.csv"
    json_path = tmp_path / "document_flashcards.json"
    
    assert pdf_path.exists()
    assert apkg_path.exists()
    assert csv_path.exists()
    assert json_path.exists()
    
    assert apkg_path.stat().st_size > 1000
    
    # Verify CSV content
    with open(csv_path, "r", encoding="utf-8") as f:
        csv_text = f.read()
    assert "What is TCP?" in csv_text
    assert "Transmission Control Protocol" in csv_text
    assert "Circle Area" in csv_text
