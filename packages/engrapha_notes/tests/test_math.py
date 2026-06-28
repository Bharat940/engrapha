from __future__ import annotations

import os
from typing import cast

import pytest
import engrapha_notes as en
from engrapha_notes.document import LaTeXFlowable
from reportlab.platypus import Table

pytest.importorskip("matplotlib")

def test_inline_formula() -> None:
    # Set the theme to ensure colors are consistent
    en.set_theme(en.DARK)
    
    # Generate an inline formula markup string
    img_tag = en.formula(r"x^2 + y^2 = z^2")
    
    # It should return a valid HTML <img> tag with src pointing to the cached PNG
    assert img_tag.startswith("<img src=")
    assert "width=" in img_tag
    assert "height=" in img_tag
    assert "valign=" in img_tag
    
    # Verify that the cached PNG file exists under .engrapha_cache/
    cache_dir = os.path.join(os.getcwd(), ".engrapha_cache")
    assert os.path.exists(cache_dir)
    assert len(os.listdir(cache_dir)) > 0

def test_formula_block() -> None:
    # Clear the global story
    en.get_story().clear()
    
    # Append a centered block formula
    en.formula_block(r"\sum_{i=1}^n i = \frac{n(n+1)}{2}")
    
    story = en.get_story()
    assert len(story) == 2  # Table + Spacer
    
    # The first flowable is a Table wrapping the LaTeXFlowable
    table = cast(Table, story[0])
    cellvalues = getattr(table, "_cellvalues", [])
    
    # Get the wrapped LaTeXFlowable from cellvalues
    cell_val = cellvalues[0][0]
    assert isinstance(cell_val, LaTeXFlowable)
    assert cell_val.latex_str == r"\sum_{i=1}^n i = \frac{n(n+1)}{2}"

def test_latex_flowable_dimensions() -> None:
    # Test dimension estimation and scaling of LaTeXFlowable
    en.set_theme(en.DARK)
    
    flow = LaTeXFlowable(r"E = mc^2", fontsize=12.0)
    
    # Scale factor is fontsize / 10.0 = 1.2
    assert flow.fontsize == 12.0
    assert flow.scale == 1.2
    
    # Width and height should be positive floats
    assert flow.width > 0
    assert flow.height > 0
    assert flow.depth >= 0
    
    # wrap() should return (width, height + depth)
    w, h = flow.wrap(400, 300)
    assert w == flow.width
    assert h == flow.height + flow.depth
