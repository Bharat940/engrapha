from __future__ import annotations

import re
from typing import ClassVar

from pydantic import BaseModel, ConfigDict, field_validator
from reportlab.lib.colors import Color, HexColor

_HEX_RE = re.compile(r"^#[0-9a-fA-F]{6}$")


class DiagramTheme(BaseModel):
    """Color and font contract shared by every diagram builder."""

    model_config = ConfigDict(arbitrary_types_allowed=True, frozen=True)

    _COLOR_FIELDS: ClassVar[set[str]] = set()

    font_name: str = "Helvetica"
    font_name_bold: str = "Helvetica-Bold"
    font_name_italic: str = "Helvetica-Oblique"
    font_name_mono: str = "Courier"

    bg: str | Color = "#0d1117"
    text: str | Color = "#f0f6fc"
    text_dim: str | Color = "#9da7b3"
    surface: str | Color = "#161b22"
    surface_alt: str | Color = "#1c2333"

    node_fill: str | Color = "#1c2333"
    node_stroke: str | Color = "#79c0ff"
    node_text: str | Color = "#f0f6fc"
    edge_color: str | Color = "#9da7b3"
    edge_label_color: str | Color = "#f0f6fc"
    line_color: str | Color = "#9da7b3"
    double_line_color: str | Color = "#79c0ff"

    process_fill: str | Color = "#1c2333"
    process_stroke: str | Color = "#79c0ff"
    process_text: str | Color = "#f0f6fc"
    decision_fill: str | Color = "#1f2a44"
    decision_stroke: str | Color = "#d29922"
    decision_text: str | Color = "#f0f6fc"
    terminal_fill: str | Color = "#0d2119"
    terminal_stroke: str | Color = "#3fb950"
    terminal_text: str | Color = "#f0f6fc"
    io_fill: str | Color = "#180d2b"
    io_stroke: str | Color = "#bc8cff"
    io_text: str | Color = "#f0f6fc"
    connector_fill: str | Color = "#30363d"
    connector_stroke: str | Color = "#9da7b3"
    connector_text: str | Color = "#f0f6fc"
    predefined_fill: str | Color = "#161b22"
    predefined_stroke: str | Color = "#79c0ff"
    predefined_text: str | Color = "#f0f6fc"
    flow_line_color: str | Color = "#9da7b3"
    flow_label_color: str | Color = "#f0f6fc"

    class_header_fill: str | Color = "#1f6feb"
    class_header_text: str | Color = "#ffffff"
    stereotype_text: str | Color = "#dbeafe"
    class_body_fill: str | Color = "#161b22"
    class_body_text: str | Color = "#f0f6fc"
    class_stroke: str | Color = "#79c0ff"
    class_attr_text: str | Color = "#dbeafe"
    class_method_text: str | Color = "#f0f6fc"

    entity_fill: str | Color = "#1c2333"
    entity_stroke: str | Color = "#79c0ff"
    entity_text: str | Color = "#f0f6fc"
    weak_entity_fill: str | Color = "#1e0d0d"
    weak_entity_stroke: str | Color = "#f85149"
    relation_fill: str | Color = "#180d2b"
    relation_stroke: str | Color = "#bc8cff"
    relation_text: str | Color = "#f0f6fc"
    relationship_fill: str | Color = "#180d2b"
    relationship_stroke: str | Color = "#bc8cff"
    relationship_text: str | Color = "#f0f6fc"
    attr_fill: str | Color = "#161b22"
    attr_stroke: str | Color = "#79c0ff"
    attr_text: str | Color = "#f0f6fc"
    attribute_fill: str | Color = "#161b22"
    attribute_stroke: str | Color = "#79c0ff"
    attribute_text: str | Color = "#f0f6fc"
    pk_fill: str | Color = "#1f1a0a"
    pk_stroke: str | Color = "#d29922"
    pk_text: str | Color = "#fff7cc"
    multi_fill: str | Color = "#0d2119"
    multi_stroke: str | Color = "#3fb950"
    derived_fill: str | Color = "#22272e"
    derived_stroke: str | Color = "#9da7b3"
    er_line_color: str | Color = "#9da7b3"
    er_label_color: str | Color = "#f0f6fc"
    cardinality_color: str | Color = "#d29922"

    net_node_fill: str | Color = "#1c2333"
    net_node_stroke: str | Color = "#79c0ff"
    net_node_text: str | Color = "#f0f6fc"
    net_line_color: str | Color = "#9da7b3"
    net_label_color: str | Color = "#f0f6fc"

    actor_fill: str | Color = "#1c2333"
    actor_stroke: str | Color = "#79c0ff"
    actor_text: str | Color = "#f0f6fc"
    seq_actor_fill: str | Color = "#1c2333"
    seq_actor_stroke: str | Color = "#79c0ff"
    seq_actor_text: str | Color = "#f0f6fc"
    seq_line_color: str | Color = "#9da7b3"
    seq_note_border: str | Color = "#9da7b3"
    seq_activation_fill: str | Color = "#30363d"
    lifeline_color: str | Color = "#6e7681"
    activation_fill: str | Color = "#30363d"
    activation_stroke: str | Color = "#79c0ff"
    message_color: str | Color = "#79c0ff"
    message_text: str | Color = "#f0f6fc"
    note_stroke: str | Color = "#d29922"

    state_fill: str | Color = "#1c2333"
    state_stroke: str | Color = "#79c0ff"
    state_text: str | Color = "#f0f6fc"
    state_line_color: str | Color = "#9da7b3"
    state_label_color: str | Color = "#f0f6fc"
    transition_color: str | Color = "#79c0ff"
    transition_label_color: str | Color = "#f0f6fc"
    initial_fill: str | Color = "#3fb950"
    accepting_stroke: str | Color = "#d29922"

    stack_colors: tuple[str | Color, ...] = (
        "#1f6feb",
        "#0891b2",
        "#238636",
        "#9a6700",
        "#8250df",
        "#cf222e",
        "#6f42c1",
    )
    stack_stroke: str | Color = "#79c0ff"
    stack_text: str | Color = "#ffffff"
    stack_sublabel_text: str | Color = "#dbeafe"
    layer_fill: str | Color = "#1c2333"
    layer_stroke: str | Color = "#79c0ff"
    layer_text: str | Color = "#f0f6fc"

    timing_line_color: str | Color = "#79c0ff"
    timing_label_color: str | Color = "#f0f6fc"
    timing_fill: str | Color = "#1c2333"
    timing_stroke: str | Color = "#79c0ff"
    timing_text: str | Color = "#f0f6fc"
    signal_label_color: str | Color = "#f0f6fc"
    signal_high_color: str | Color = "#3fb950"
    signal_low_color: str | Color = "#6e7681"
    time_axis_color: str | Color = "#9da7b3"
    time_tick_color: str | Color = "#9da7b3"

    schema_header_fill: str | Color = "#1f6feb"
    schema_header_text: str | Color = "#ffffff"
    schema_body_fill: str | Color = "#161b22"
    schema_stroke: str | Color = "#79c0ff"
    schema_text: str | Color = "#f0f6fc"
    schema_line_color: str | Color = "#9da7b3"

    arch_fill: str | Color = "#1c2333"
    arch_stroke: str | Color = "#79c0ff"
    arch_text: str | Color = "#f0f6fc"
    arch_line_color: str | Color = "#9da7b3"
    arch_label_color: str | Color = "#f0f6fc"
    c4_fill: str | Color = "#1c2333"
    c4_stroke: str | Color = "#79c0ff"
    c4_text: str | Color = "#f0f6fc"
    c4_line_color: str | Color = "#9da7b3"
    c4_label_color: str | Color = "#f0f6fc"
    git_commit_fill: str | Color = "#1c2333"
    git_commit_stroke: str | Color = "#79c0ff"
    git_commit_text: str | Color = "#f0f6fc"
    git_line_color: str | Color = "#9da7b3"
    git_label_color: str | Color = "#f0f6fc"
    cloud_fill: str | Color = "#1c2333"
    cloud_stroke: str | Color = "#79c0ff"

    @field_validator("*", mode="before")
    @classmethod
    def _validate_hex_colors(cls, value: object, info) -> object:
        if info.field_name and (
            info.field_name.endswith("_font")
            or info.field_name.startswith("font_name")
            or info.field_name == "stack_colors"
        ):
            return value
        if isinstance(value, Color):
            return value
        if isinstance(value, str):
            if _HEX_RE.match(value):
                return value
            raise ValueError(f"{info.field_name} must be a #RRGGBB hex color")
        return value

    def rl(self, color_value: str | Color) -> Color:
        """Return a ReportLab color for a theme color value."""
        if isinstance(color_value, Color):
            return color_value
        return HexColor(color_value)

    def rl_color(self, color_value: str | Color) -> Color:
        """Backward-compatible alias used by custom node callbacks."""
        return self.rl(color_value)

    @classmethod
    def from_notes_theme(cls, notes_theme: object) -> "DiagramTheme":
        """Create a diagram theme from the active engrapha_notes theme."""
        bg_color = str(getattr(notes_theme, "bg", "#0d1117")).strip()
        
        is_light = False
        if bg_color.startswith("#") and len(bg_color) >= 7:
            try:
                r = int(bg_color[1:3], 16)
                g = int(bg_color[3:5], 16)
                b = int(bg_color[5:7], 16)
                luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255.0
                is_light = luminance > 0.5
            except ValueError:
                pass
                
        base = LIGHT if is_light else DARK

        accent = getattr(notes_theme, "accent", base.node_stroke)
        text = getattr(notes_theme, "text", base.text)
        text_dim = getattr(notes_theme, "text_dim", base.text_dim)
        surface = getattr(notes_theme, "surface", base.surface)
        surface_alt = getattr(notes_theme, "surface_alt", base.surface_alt)
        bg = getattr(notes_theme, "bg", base.bg)
        yellow = getattr(notes_theme, "yellow", base.decision_stroke)
        green = getattr(notes_theme, "green", base.terminal_stroke)
        red = getattr(notes_theme, "red", base.weak_entity_stroke)
        purple = getattr(notes_theme, "purple", base.io_stroke)

        return base.model_copy(
            update={
                "bg": bg,
                "text": text,
                "text_dim": text_dim,
                "surface": surface,
                "surface_alt": surface_alt,
                "node_stroke": accent,
                "process_stroke": accent,
                "terminal_stroke": green,
                "decision_stroke": yellow,
                "io_stroke": purple,
                "flow_line_color": text_dim,
                "class_header_fill": accent,
                "class_stroke": accent,
                "entity_stroke": accent,
                "weak_entity_stroke": red,
                "relation_stroke": purple,
                "pk_stroke": yellow,
                "multi_stroke": green,
                "net_node_stroke": accent,
                "actor_stroke": accent,
                "seq_actor_stroke": accent,
                "message_color": accent,
                "activation_fill": surface_alt,
                "state_stroke": accent,
                "transition_color": text_dim,
                "cloud_stroke": accent,
            }
        )


DARK = DiagramTheme()
LIGHT = DiagramTheme(
    bg="#ffffff",
    text="#111827",
    text_dim="#4b5563",
    surface="#f8fafc",
    surface_alt="#e5e7eb",
    node_fill="#ffffff",
    node_text="#111827",
    process_fill="#ffffff",
    process_text="#111827",
    decision_fill="#fff7ed",
    decision_text="#111827",
    terminal_fill="#ecfdf5",
    terminal_text="#111827",
    io_fill="#f5f3ff",
    io_text="#111827",
    class_body_fill="#ffffff",
    class_body_text="#111827",
    entity_fill="#ffffff",
    weak_entity_fill="#fee2e2",
    relation_fill="#f5f3ff",
    relationship_fill="#f5f3ff",
    attr_fill="#ffffff",
    attribute_fill="#ffffff",
    pk_fill="#fef9c3",
    multi_fill="#ecfdf5",
    derived_fill="#f1f5f9",
    entity_text="#111827",
    attr_text="#111827",
    relationship_text="#111827",
    relation_text="#111827",
    actor_fill="#ffffff",
    actor_text="#111827",
    state_fill="#ffffff",
    state_text="#111827",
    schema_body_fill="#ffffff",
    schema_text="#111827",
    stack_text="#111827",
    layer_text="#111827",
)

OCEAN_DARK = DARK.model_copy(
    update={
        "bg": "#020c14",
        "surface": "#082032",
        "surface_alt": "#0f2f46",
        "node_stroke": "#22d3ee",
    }
)
FOREST_DARK = DARK.model_copy(
    update={
        "bg": "#0b1512",
        "surface": "#10231c",
        "surface_alt": "#173528",
        "node_stroke": "#4ade80",
    }
)
SUNSET_DARK = DARK.model_copy(
    update={
        "bg": "#0c0811",
        "surface": "#211225",
        "surface_alt": "#321a2f",
        "node_stroke": "#fb923c",
    }
)
MIDNIGHT_DARK = DARK.model_copy(
    update={
        "bg": "#07050f",
        "surface": "#111026",
        "surface_alt": "#19183a",
        "node_stroke": "#818cf8",
    }
)
OCEAN_LIGHT = LIGHT.model_copy(
    update={
        "bg": "#f0f9ff",
        "surface": "#ffffff",
        "surface_alt": "#e0f2fe",
        "node_stroke": "#0891b2",
    }
)
SEPIA = LIGHT.model_copy(
    update={
        "bg": "#faf7f0",
        "surface": "#fffaf0",
        "surface_alt": "#f3ead8",
        "node_stroke": "#92400e",
    }
)
CATPPUCCIN_LATTE = LIGHT.model_copy(
    update={
        "bg": "#eff1f5",
        "surface": "#e6e9ef",
        "surface_alt": "#dce0e8",
        "node_stroke": "#1e66f5",
    }
)
CATPPUCCIN_MOCHA = DARK.model_copy(
    update={
        "bg": "#1e1e2e",
        "surface": "#313244",
        "surface_alt": "#45475a",
        "node_stroke": "#89b4fa",
    }
)
NOTION = LIGHT.model_copy(
    update={
        "bg": "#ffffff",
        "surface": "#f1f1ef",
        "surface_alt": "#e3e2e0",
        "text": "#37352f",
        "text_dim": "#787774",
        "node_stroke": "#37352f",
        "node_fill": "#f1f1ef",
        "node_text": "#37352f",
    }
)
GITHUB = LIGHT.model_copy(
    update={
        "bg": "#ffffff",
        "surface": "#f6f8fa",
        "surface_alt": "#afb8c1",
        "text": "#24292f",
        "text_dim": "#57606a",
        "node_stroke": "#0969da",
        "node_fill": "#f6f8fa",
        "node_text": "#24292f",
    }
)
LINEAR = DARK.model_copy(
    update={
        "bg": "#0e0e10",
        "surface": "#151518",
        "surface_alt": "#222227",
        "text": "#f4f4f5",
        "text_dim": "#a1a1aa",
        "node_stroke": "#5e6ad2",
        "node_fill": "#151518",
        "node_text": "#f4f4f5",
    }
)
ACADEMIC = LIGHT.model_copy(
    update={
        "bg": "#ffffff",
        "surface": "#ffffff",
        "surface_alt": "#f3f4f6",
        "text": "#111111",
        "text_dim": "#374151",
        "node_stroke": "#111111",
        "node_fill": "#ffffff",
        "node_text": "#111111",
        "font_name": "Times-Roman",
        "font_name_bold": "Times-Bold",
        "font_name_italic": "Times-Italic",
    }
)
TEXTBOOK = LIGHT.model_copy(
    update={
        "bg": "#fafafa",
        "surface": "#f4f4f5",
        "surface_alt": "#e4e4e7",
        "text": "#18181b",
        "text_dim": "#52525b",
        "node_stroke": "#0f766e",
        "node_fill": "#f4f4f5",
        "node_text": "#18181b",
    }
)
MODERN = MIDNIGHT_DARK.model_copy(
    update={
        "node_stroke": "#cba6f7",
        "node_fill": "#111026",
    }
)
