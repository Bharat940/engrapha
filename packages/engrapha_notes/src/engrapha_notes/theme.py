from __future__ import annotations

from dataclasses import dataclass, replace
from typing import Any

from reportlab.lib.colors import HexColor


def hex_to_rgb(hex_str: str) -> str:
    """Return a hex string for callers that accept either RGB or hex values."""
    return hex_str


@dataclass
class NotesTheme:
    name: str = "Dark"
    bg: str = "#0d1117"
    surface: str = "#161b22"
    surface_alt: str = "#1c2333"
    card_mid: str = "#1c2333"
    text: str = "#f0f6fc"
    text_dim: str = "#9da7b3"
    text_code: str = "#dbeafe"
    accent: str = "#79c0ff"
    accent2: str = "#bc8cff"
    accent_dim: str = "#2c5b96"
    accent_surface: str = "#1a3b5c"
    cyan: str = "#79c0ff"
    green: str = "#3fb950"
    green_bg: str = "#0d2119"
    yellow: str = "#d29922"
    yellow_bg: str = "#1f1a0a"
    red: str = "#f85149"
    red_bg: str = "#1e0d0d"
    purple: str = "#bc8cff"
    purple_bg: str = "#180d2b"
    white: str = "#f0f6fc"
    danger: str = "#f85149"
    success: str = "#3fb950"
    warning: str = "#d29922"
    info: str = "#79c0ff"
    border: str = "#30363d"
    table_hdr: str = "#1f6feb"
    table_bdr: str = "#30363d"
    code_bg: str = "#161b22"
    body_font: str = "Helvetica"
    heading_font: str = "Helvetica-Bold"
    code_font: str = "Courier"
    size_body: float = 10.0
    size_question: float = 10.0
    border_thickness: float = 1.0
    border_color: str | None = None
    show_headers: bool = False
    divider_thickness: float = 1.0
    left_margin: float = 51.0236220472
    right_margin: float = 51.0236220472
    top_margin: float = 51.0236220472
    bottom_margin: float = 51.0236220472
    double_page_border: bool = False
    page_border_margin: float = 12.0
    page_border_gap: float = 3.0
    page_border_color: str | None = None
    plain_questions: bool = False

    def rl(self, color_value: str | Any) -> Any:
        """Convert hex strings to ReportLab colors while preserving color objects."""
        return HexColor(color_value) if isinstance(color_value, str) else color_value

    def copy_with(self, **kwargs: Any) -> "NotesTheme":
        """Return a modified copy of the theme."""
        return replace(self, **kwargs)

    @classmethod
    def from_accent(cls, accent: str, dark: bool = True, name: str | None = None) -> "NotesTheme":
        """Build a practical theme from one accent color."""
        base = DARK if dark else LIGHT
        return base.copy_with(name=name or f"Accent {accent}", accent=accent, cyan=accent)


class ThemeBuilder:
    """Small fluent builder for custom note themes."""

    def __init__(self) -> None:
        self._theme = NotesTheme()

    def set_colors(self, bg: str, surface: str, accent: str) -> "ThemeBuilder":
        self._theme.bg = bg
        self._theme.surface = surface
        self._theme.surface_alt = surface
        self._theme.card_mid = surface
        self._theme.accent = accent
        self._theme.cyan = accent
        return self

    def set_fonts(self, body_font: str, heading_font: str, size_body: float, size_question: float | None = None) -> "ThemeBuilder":
        self._theme.body_font = body_font
        self._theme.heading_font = heading_font
        self._theme.size_body = size_body
        if size_question is not None:
            self._theme.size_question = size_question
        return self

    def set_borders(self, thickness: float, color: str) -> "ThemeBuilder":
        self._theme.border_thickness = thickness
        self._theme.border_color = color
        return self

    def set_double_border(self, enabled: bool, margin: float = 12.0, gap: float = 3.0, color: str | None = None) -> "ThemeBuilder":
        self._theme.double_page_border = enabled
        self._theme.page_border_margin = margin
        self._theme.page_border_gap = gap
        self._theme.page_border_color = color
        return self

    def set_header_footer(self, show_headers: bool, divider_thickness: float) -> "ThemeBuilder":
        self._theme.show_headers = show_headers
        self._theme.divider_thickness = divider_thickness
        return self

    def build(self) -> NotesTheme:
        return self._theme


DARK = NotesTheme(name="Dark")
LIGHT = NotesTheme(
    name="Light",
    bg="#ffffff",
    surface="#f8fafc",
    surface_alt="#e5e7eb",
    card_mid="#e5e7eb",
    text="#111827",
    text_dim="#4b5563",
    text_code="#111827",
    accent="#2563eb",
    accent2="#7c3aed",
    cyan="#2563eb",
    green="#15803d",
    green_bg="#dcfce7",
    yellow="#a16207",
    yellow_bg="#fef9c3",
    red="#dc2626",
    red_bg="#fee2e2",
    purple="#7c3aed",
    purple_bg="#ede9fe",
    white="#111827",
    table_hdr="#2563eb",
    table_bdr="#cbd5e1",
    code_bg="#f1f5f9",
)
OCEAN_DARK = DARK.copy_with(
    name="Ocean Dark",
    bg="#020c14",
    surface="#082032",
    surface_alt="#0f2f46",
    card_mid="#0f2f46",
    accent="#22d3ee",
    cyan="#22d3ee",
)
FOREST_DARK = DARK.copy_with(
    name="Forest Dark",
    bg="#0b1512",
    surface="#10231c",
    surface_alt="#173528",
    card_mid="#173528",
    accent="#4ade80",
    cyan="#4ade80",
)
SUNSET_DARK = DARK.copy_with(
    name="Sunset Dark",
    bg="#0c0811",
    surface="#211225",
    surface_alt="#321a2f",
    card_mid="#321a2f",
    accent="#fb923c",
    cyan="#fb923c",
)
MIDNIGHT_DARK = DARK.copy_with(
    name="Midnight Dark",
    bg="#07050f",
    surface="#111026",
    surface_alt="#19183a",
    card_mid="#19183a",
    accent="#818cf8",
    cyan="#818cf8",
)
OCEAN_LIGHT = LIGHT.copy_with(
    name="Ocean Light",
    bg="#f0f9ff",
    surface="#ffffff",
    surface_alt="#e0f2fe",
    card_mid="#e0f2fe",
    accent="#0891b2",
    cyan="#0891b2",
)
SEPIA = LIGHT.copy_with(
    name="Sepia",
    bg="#faf7f0",
    surface="#fffaf0",
    surface_alt="#f3ead8",
    card_mid="#f3ead8",
    accent="#92400e",
    cyan="#92400e",
)
CATPPUCCIN_LATTE = LIGHT.copy_with(
    name="Catppuccin Latte",
    bg="#eff1f5",
    surface="#e6e9ef",
    surface_alt="#dce0e8",
    card_mid="#dce0e8",
    accent="#1e66f5",
    cyan="#1e66f5",
)
CATPPUCCIN_MOCHA = DARK.copy_with(
    name="Catppuccin Mocha",
    bg="#1e1e2e",
    surface="#313244",
    surface_alt="#45475a",
    card_mid="#45475a",
    accent="#89b4fa",
    cyan="#89b4fa",
)
NOTION = LIGHT.copy_with(
    name="Notion",
    bg="#ffffff",
    surface="#f1f1ef",
    surface_alt="#e3e2e0",
    card_mid="#e3e2e0",
    text="#37352f",
    text_dim="#787774",
    accent="#2383e2",
    cyan="#2383e2",
    table_hdr="#2383e2",
    table_bdr="#e3e2e0",
    code_bg="#f7f6f3",
)
GITHUB = LIGHT.copy_with(
    name="GitHub",
    bg="#ffffff",
    surface="#f6f8fa",
    surface_alt="#afb8c1",
    card_mid="#afb8c1",
    text="#24292f",
    text_dim="#57606a",
    accent="#0969da",
    cyan="#0969da",
    table_hdr="#0969da",
    table_bdr="#d0d7de",
    code_bg="#f6f8fa",
)
LINEAR = DARK.copy_with(
    name="Linear",
    bg="#0e0e10",
    surface="#151518",
    surface_alt="#222227",
    card_mid="#222227",
    text="#f4f4f5",
    text_dim="#a1a1aa",
    accent="#5e6ad2",
    cyan="#5e6ad2",
    table_hdr="#5e6ad2",
    table_bdr="#222227",
    code_bg="#151518",
)
ACADEMIC = LIGHT.copy_with(
    name="Academic",
    bg="#ffffff",
    surface="#ffffff",
    surface_alt="#f3f4f6",
    card_mid="#f3f4f6",
    text="#111111",
    text_dim="#374151",
    accent="#111111",
    cyan="#111111",
    table_hdr="#111111",
    table_bdr="#e5e7eb",
    code_bg="#f3f4f6",
    body_font="Times-Roman",
    heading_font="Times-Bold",
)
TEXTBOOK = LIGHT.copy_with(
    name="Textbook",
    bg="#fafafa",
    surface="#f4f4f5",
    surface_alt="#e4e4e7",
    card_mid="#e4e4e7",
    text="#18181b",
    text_dim="#52525b",
    accent="#0f766e",
    cyan="#0f766e",
    table_hdr="#0f766e",
    table_bdr="#e4e4e7",
    code_bg="#f4f4f5",
)

ALL_THEMES = [
    DARK,
    LIGHT,
    OCEAN_DARK,
    FOREST_DARK,
    SUNSET_DARK,
    MIDNIGHT_DARK,
    OCEAN_LIGHT,
    SEPIA,
    CATPPUCCIN_LATTE,
    CATPPUCCIN_MOCHA,
    NOTION,
    GITHUB,
    LINEAR,
    ACADEMIC,
    TEXTBOOK,
]

DRACULA = "dracula"
MONOKAI = "monokai"
GITHUB_DARK = "github-dark"

_current_theme = DARK


def set_theme(theme: NotesTheme) -> None:
    global _current_theme
    _current_theme = theme


def get_theme() -> NotesTheme:
    return _current_theme


def EngineeringNotes(dark: bool = True) -> NotesTheme:
    theme = (DARK if dark else LIGHT).copy_with(
        name="Engineering Notes",
        body_font="Helvetica",
        heading_font="Helvetica-Bold",
        size_body=10.0,
    )
    set_theme(theme)
    return theme


def QuestionBank(dark: bool = False) -> NotesTheme:
    theme = (DARK if dark else LIGHT).copy_with(
        name="Question Bank",
        body_font="Times-Roman",
        heading_font="Times-Bold",
        size_body=9.5,
    )
    set_theme(theme)
    return theme
