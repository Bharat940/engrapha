"""
stack.py -- Layered stack diagram builder.

Renders stacked horizontal layers. Useful for:
  - OSI / TCP-IP reference models
  - Memory hierarchy (registers, cache, RAM, disk)
  - Software architecture tiers (presentation, business, data)
  - CPU pipeline stages

Layers are drawn top-to-bottom in insertion order.
Colors cycle through the theme's stack_colors palette if not specified per layer.
"""

from __future__ import annotations

from pydantic import BaseModel

from . import shapes as S
from .base import DiagramBase
from .theme import DiagramTheme

_DEFAULT_LAYER_H = 30.0
_DEFAULT_MARGIN = 12.0
_LABEL_FONT_SIZE = 9.5
_SUBLABEL_FONT_SIZE = 8.0


class _Layer(BaseModel):
    label: str
    sublabel: str = ""
    fill: str | None = None  # None = use auto cycling from theme.stack_colors
    stroke: str | None = None
    height: float = _DEFAULT_LAYER_H
    divider_after: bool = False  # draw a thicker separator after this layer


class LayeredStack(DiagramBase):
    """
    Layered stack diagram builder.

    Usage (OSI Model)::

        osi = LayeredStack(width=340, height=260, caption="OSI Reference Model")
        osi.layer("Layer 7 -- Application",  sublabel="HTTP, FTP, SMTP, DNS")
        osi.layer("Layer 6 -- Presentation", sublabel="SSL/TLS, JPEG, MPEG")
        osi.layer("Layer 5 -- Session",      sublabel="NetBIOS, RPC")
        osi.divider()
        osi.layer("Layer 4 -- Transport",    sublabel="TCP, UDP")
        osi.layer("Layer 3 -- Network",      sublabel="IP, ICMP, ARP")
        osi.layer("Layer 2 -- Data Link",    sublabel="Ethernet, PPP, HDLC")
        osi.layer("Layer 1 -- Physical",     sublabel="Cables, Fiber, Radio")
        story.extend(osi.as_flowable())
    """

    def __init__(
        self,
        width: float,
        height: float,
        theme: DiagramTheme | None = None,
        caption: str | None = None,
        margin: float = _DEFAULT_MARGIN,
        layer_h: float = _DEFAULT_LAYER_H,
        corner_radius: float = 5.0,
    ) -> None:
        super().__init__(width, height, theme, caption)
        self.margin = margin
        self.layer_h = layer_h
        self.corner_radius = corner_radius
        self._layers: list[_Layer] = []
        self._color_cursor = 0

    def layer(
        self,
        label: str,
        sublabel: str = "",
        fill: str | None = None,
        stroke: str | None = None,
        height: float | None = None,
    ) -> "LayeredStack":
        """Add a layer. Layers are rendered top-to-bottom in the order they are added."""
        self._layers.append(
            _Layer(
                label=label,
                sublabel=sublabel,
                fill=fill,
                stroke=stroke,
                height=height if height is not None else self.layer_h,
            )
        )
        return self

    def divider(self) -> "LayeredStack":
        """
        Mark that the last added layer should be followed by a thicker divider.
        Useful for grouping layers (e.g. upper vs lower OSI layers).
        """
        if not self._layers:
            raise ValueError("Call layer() before divider()")
        self._layers[-1] = self._layers[-1].model_copy(update={"divider_after": True})
        return self

    def build(self) -> None:
        if not self._layers:
            return

        t = self.theme
        lx = self.margin
        lw = self.width - self.margin * 2

        # Calculate total used height and auto-scale if needed
        total_h = sum(ly.height for ly in self._layers) + (len(self._layers) - 1) * 3
        available_h = self.height - self.margin * 2
        scale = min(1.0, available_h / max(total_h, 1))

        # Draw from top to bottom
        cursor_y = self.height - self.margin

        for i, ly in enumerate(self._layers):
            lh = ly.height * scale
            layer_y = cursor_y - lh

            # Fill color: explicit > theme cycling
            if ly.fill:
                fill = ly.fill
            else:
                palette = t.stack_colors
                fill = palette[self._color_cursor % len(palette)]
                self._color_cursor += 1

            stroke = ly.stroke or t.stack_stroke

            self._add(
                S.rounded_rect(
                    lx,
                    layer_y,
                    lw,
                    lh,
                    rx=self.corner_radius,
                    fill=fill,
                    stroke=stroke,
                    stroke_width=1.2,
                )
            )

            # Label centered vertically in the layer (responsively wrapped if too long)
            max_text_w = lw - 12.0  # 6pt padding on left/right

            # Wrap label and sublabel text if they exceed the width
            lbl_lines = S.wrap_text(
                ly.label, max_text_w, font=t.font_name_bold, size=_LABEL_FONT_SIZE
            )
            sub_lines = (
                S.wrap_text(
                    ly.sublabel,
                    max_text_w,
                    font=t.font_name_italic,
                    size=_SUBLABEL_FONT_SIZE,
                )
                if ly.sublabel
                else []
            )

            lbl_lh = _LABEL_FONT_SIZE * 1.2
            sub_lh = _SUBLABEL_FONT_SIZE * 1.2

            lbl_h = len(lbl_lines) * lbl_lh
            sub_h = len(sub_lines) * sub_lh
            gap = 3.0 if sub_lines else 0.0
            total_text_h = lbl_h + sub_h + gap

            # Center the entire text block vertically within the layer
            y_center = layer_y + lh / 2.0
            lbl_first_baseline = (
                y_center + total_text_h / 2.0 - lbl_lh + _LABEL_FONT_SIZE * 0.15
            )

            # Add label group
            self._add(
                S.multiline_label(
                    lx + lw / 2.0,
                    lbl_first_baseline,
                    lbl_lines,
                    font=t.font_name_bold,
                    size=_LABEL_FONT_SIZE,
                    color=t.stack_text,
                    line_height=lbl_lh,
                    anchor="middle",
                )
            )

            # Add sublabel group if present
            if sub_lines:
                sub_first_baseline = lbl_first_baseline - lbl_h - gap
                self._add(
                    S.multiline_label(
                        lx + lw / 2.0,
                        sub_first_baseline,
                        sub_lines,
                        font=t.font_name_italic,
                        size=_SUBLABEL_FONT_SIZE,
                        color=t.stack_sublabel_text,
                        line_height=sub_lh,
                        anchor="middle",
                    )
                )

            # Divider after this layer
            if ly.divider_after and i < len(self._layers) - 1:
                div_y = layer_y - 1.5
                self._add(
                    S.solid_line(
                        lx + 4,
                        div_y,
                        lx + lw - 4,
                        div_y,
                        color=t.stack_sublabel_text,
                        width=1.5,
                    )
                )

            cursor_y = layer_y - 3 * scale
