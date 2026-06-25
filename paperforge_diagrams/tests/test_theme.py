"""
test_theme.py -- Tests for DiagramTheme Pydantic model and DARK/LIGHT presets.
"""

from __future__ import annotations

import pytest
from pydantic import ValidationError
from reportlab.lib.colors import Color

from paperforge_diagrams.theme import DARK, LIGHT, DiagramTheme


class TestDiagramThemeValidation:
    def test_dark_preset_is_valid(self) -> None:
        assert isinstance(DARK, DiagramTheme)

    def test_light_preset_is_valid(self) -> None:
        assert isinstance(LIGHT, DiagramTheme)

    def test_dark_bg_is_hex(self) -> None:
        assert DARK.bg.startswith("#")

    def test_light_bg_is_white(self) -> None:
        assert DARK.bg != LIGHT.bg

    def test_stack_colors_not_empty(self) -> None:
        assert len(DARK.stack_colors) > 0
        assert len(LIGHT.stack_colors) > 0

    def test_invalid_bg_raises(self) -> None:
        with pytest.raises(ValidationError, match="hex"):
            DiagramTheme(**{**DARK.model_dump(), "bg": "not-a-hex"})

    def test_theme_is_immutable(self) -> None:
        with pytest.raises(Exception):
            DARK.bg = "#ffffff"

    def test_rl_color_returns_hex_color(self) -> None:
        result = DARK.rl_color(DARK.entity_stroke)
        assert isinstance(result, Color)

    def test_font_names_are_strings(self) -> None:
        assert isinstance(DARK.font_name, str)
        assert isinstance(DARK.font_name_bold, str)
        assert isinstance(DARK.font_name_mono, str)
