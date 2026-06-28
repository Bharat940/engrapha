"""
test_base.py -- Tests for DiagramBase and the Platypus Flowable integration.
"""

from __future__ import annotations

import pytest
from typing import Any
from reportlab.graphics.shapes import Drawing
from reportlab.platypus import Flowable

from engrapha_diagrams.base import DiagramBase
from engrapha_diagrams.theme import DARK


class _ConcreteMinimal(DiagramBase):
    """Minimal concrete subclass for testing the base class."""

    def build(self) -> None:
        pass  # empty drawing


class _ConcreteFailing(DiagramBase):
    """Subclass whose build() always raises."""

    def build(self) -> None:
        raise RuntimeError("Intentional build failure")


class TestDiagramBaseValidation:
    def test_valid_construction(self) -> None:
        d = _ConcreteMinimal(width=200, height=100)
        assert d.width == 200
        assert d.height == 100

    def test_zero_width_raises(self) -> None:
        with pytest.raises(ValueError, match="width"):
            _ConcreteMinimal(width=0, height=100)

    def test_negative_height_raises(self) -> None:
        with pytest.raises(ValueError, match="height"):
            _ConcreteMinimal(width=200, height=-10)

    def test_default_theme_is_dark(self) -> None:
        d = _ConcreteMinimal(width=200, height=100)
        assert d.theme is DARK

    def test_caption_stored(self) -> None:
        d = _ConcreteMinimal(width=200, height=100, caption="Test caption")
        assert d.caption == "Test caption"


class TestDiagramBaseFlowable:
    def test_as_flowable_returns_list(self) -> None:
        d = _ConcreteMinimal(width=200, height=100)
        result = d.as_flowable()
        assert isinstance(result, list)
        assert len(result) > 0

    def test_as_flowable_items_are_flowables(self) -> None:
        d = _ConcreteMinimal(width=200, height=100)
        for item in d.as_flowable():
            assert isinstance(item, Flowable)

    def test_build_called_once(self, monkeypatch: pytest.MonkeyPatch) -> None:
        call_count = 0

        class _Counter(DiagramBase):
            def build(self) -> None:
                nonlocal call_count
                call_count += 1

        d = _Counter(width=200, height=100)
        d.as_flowable()
        d.as_flowable()  # second call should not re-build
        assert call_count == 1

    def test_drawing_is_drawing_instance(self) -> None:
        d = _ConcreteMinimal(width=200, height=100)
        d.as_flowable()
        assert isinstance(d.drawing, Drawing)

    def test_drawing_dimensions(self) -> None:
        d = _ConcreteMinimal(width=300, height=150)
        d.as_flowable()
        assert d.drawing.width == 300
        assert d.drawing.height == 150

    def test_build_error_raises_runtime(self) -> None:
        d = _ConcreteFailing(width=200, height=100)
        with pytest.raises(RuntimeError, match="Intentional build failure"):
            d.as_flowable()

    def test_responsive_flowable_scales_down(self) -> None:
        from engrapha_diagrams.base import ResponsiveDrawingFlowable
        from reportlab.graphics.shapes import Drawing

        drawing = Drawing(400, 200)
        flowable = ResponsiveDrawingFlowable(drawing)

        w, h = flowable.wrap(500, 300)
        assert w == 400
        assert h == 200
        assert flowable.scale_factor == 1.0

        w, h = flowable.wrap(200, 300)
        assert w == 200
        assert h == 100
        assert flowable.scale_factor == 0.5

    def test_save_method(self, tmp_path: Any) -> None:
        import os

        d = _ConcreteMinimal(width=200, height=100)

        pdf_path = os.path.join(tmp_path, "test.pdf")
        svg_path = os.path.join(tmp_path, "test.svg")
        png_path = os.path.join(tmp_path, "test.png")

        # Save to PDF
        d.save(pdf_path)
        assert os.path.exists(pdf_path)

        # Save to SVG
        d.save(svg_path)
        assert os.path.exists(svg_path)

        # Save to PNG (handle missing Cairo backend gracefully in test environment)
        try:
            d.save(png_path)
            assert os.path.exists(png_path)
        except RuntimeError as exc:
            if "rlpycairo" in str(exc):
                # Expected when cairo dependencies are missing
                pass
            else:
                raise

        # Save to invalid format
        with pytest.raises(RuntimeError, match="Unsupported export file format"):
            d.save(os.path.join(tmp_path, "test.invalid"))
