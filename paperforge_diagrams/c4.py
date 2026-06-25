from __future__ import annotations

from typing import Any
from .base import DiagramBase
from .theme import DiagramTheme
from . import shapes as S
import math


class C4ContainerDiagram(DiagramBase):
    """
    C4 Model Container Diagram builder.
    Visualizes Systems, Containers (with tech & description), and relations.
    """

    def __init__(
        self,
        width: float,
        height: float,
        theme: DiagramTheme | None = None,
        caption: str | None = None,
    ) -> None:
        super().__init__(width, height, theme, caption)
        self._items: dict[str, dict[str, Any]] = {}
        self._relations: list[tuple[str, str, str]] = []
        self._item_w = 110.0
        self._item_h = 55.0

    def system(self, name: str, desc: str = "") -> "C4ContainerDiagram":
        """Add a software system context node."""
        self._items[name] = {
            "type": "system",
            "desc": desc,
            "tech": "",
            "x": 0.0,
            "y": 0.0,
        }
        return self

    def container(
        self, name: str, tech: str = "", desc: str = ""
    ) -> "C4ContainerDiagram":
        """Add a container node (e.g. Web App, Database)."""
        self._items[name] = {
            "type": "container",
            "desc": desc,
            "tech": tech,
            "x": 0.0,
            "y": 0.0,
        }
        return self

    def relate(
        self, from_item: str, to_item: str, label: str = ""
    ) -> "C4ContainerDiagram":
        """Add a relationship line between two items."""
        self._relations.append((from_item, to_item, label))
        return self

    def build(self) -> None:
        t = self.theme

        # Auto-layout in a simple grid
        num_items = len(self._items)
        if num_items > 0:
            cols = math.ceil(math.sqrt(num_items))
            rows = math.ceil(num_items / cols)

            cell_w = self.width / cols
            cell_h = self.height / rows

            for idx, name in enumerate(sorted(self._items.keys())):
                r = idx // cols
                c = idx % cols
                self._items[name]["x"] = (
                    c * cell_w + (cell_w - self._item_w) / 2.0 + self._item_w / 2.0
                )
                self._items[name]["y"] = (
                    self.height
                    - (r * cell_h + (cell_h + self._item_h) / 2.0)
                    + self._item_h / 2.0
                )

        # Draw nodes
        for name, item in self._items.items():
            ix, iy = item["x"], item["y"]
            itype = item["type"]
            tech = item["tech"]
            desc = item["desc"]

            x_left = ix - self._item_w / 2.0
            y_bottom = iy - self._item_h / 2.0

            # C4 styling
            if itype == "system":
                # External system / Software boundary context (Dark Blue/Gray)
                fill_color = t.entity_fill
                stroke_color = t.entity_stroke
            else:
                # Container (Lighter Blue/Purple)
                fill_color = t.surface_alt
                stroke_color = t.node_stroke

            # Draw card body
            self._add(
                S.rounded_rect(
                    x_left,
                    y_bottom,
                    self._item_w,
                    self._item_h,
                    rx=3.0,
                    fill=fill_color,
                    stroke=stroke_color,
                    stroke_width=1.5,
                )
            )

            # Node name
            self._add(
                S.label(
                    ix,
                    iy + self._item_h / 2.0 - 12.0,
                    name,
                    font=t.font_name_bold,
                    size=9.0,
                    color=t.text,
                    anchor="middle",
                )
            )

            # Technology label if container
            y_cursor = iy + self._item_h / 2.0 - 22.0
            if tech:
                tech_str = f"[{tech}]"
                self._add(
                    S.label(
                        ix,
                        y_cursor,
                        tech_str,
                        font=t.font_name_bold,
                        size=6.5,
                        color=t.text_dim,
                        anchor="middle",
                    )
                )
                y_cursor -= 10.0

            # Description wrapped
            if desc:
                self._add(
                    S.centered_wrapped_label(
                        ix,
                        y_bottom + 15.0,
                        desc,
                        self._item_w - 12.0,
                        font=t.font_name_italic,
                        size=6.5,
                        color=t.text_dim,
                    )
                )

        # Draw relationships (orthogonal routing with labels)
        for from_item, to_item, label in self._relations:
            if from_item not in self._items or to_item not in self._items:
                continue

            it1 = self._items[from_item]
            it2 = self._items[to_item]

            x1, y1 = it1["x"], it1["y"]
            x2, y2 = it2["x"], it2["y"]

            dx = x2 - x1
            dy = y2 - y1

            if abs(dx) > abs(dy):
                # Side-to-side routing
                if dx > 0:
                    p1_x = x1 + self._item_w / 2.0
                    p2_x = x2 - self._item_w / 2.0
                else:
                    p1_x = x1 - self._item_w / 2.0
                    p2_x = x2 + self._item_w / 2.0

                mid_x = (p1_x + p2_x) / 2.0

                self._add(
                    S.solid_line(
                        p1_x, y1, mid_x, y1, color=t.flow_line_color, width=1.2
                    )
                )
                self._add(
                    S.solid_line(
                        mid_x, y1, mid_x, y2, color=t.flow_line_color, width=1.2
                    )
                )
                self._add(
                    S.arrow_line(
                        mid_x,
                        y2,
                        p2_x,
                        y2,
                        color=t.flow_line_color,
                        width=1.2,
                        arrow_end=True,
                        arrow_size=6.0,
                    )
                )

                if label:
                    pill_color = S.get_contrast_color(
                        t.surface, light_fg=t.flow_label_color, dark_fg="#0f172a"
                    )
                    self._add(
                        S.pill_label(
                            mid_x,
                            (y1 + y2) / 2.0,
                            label,
                            font=t.font_name_italic,
                            size=7.0,
                            text_color=pill_color,
                            bg_color=t.surface,
                            border_color=t.node_stroke,
                        )
                    )
            else:
                # Top-to-bottom routing
                if dy > 0:
                    p1_y = y1 + self._item_h / 2.0
                    p2_y = y2 - self._item_h / 2.0
                else:
                    p1_y = y1 - self._item_h / 2.0
                    p2_y = y2 + self._item_h / 2.0

                mid_y = (p1_y + p2_y) / 2.0

                self._add(
                    S.solid_line(
                        x1, p1_y, x1, mid_y, color=t.flow_line_color, width=1.2
                    )
                )
                self._add(
                    S.solid_line(
                        x1, mid_y, x2, mid_y, color=t.flow_line_color, width=1.2
                    )
                )
                self._add(
                    S.arrow_line(
                        x2,
                        mid_y,
                        x2,
                        p2_y,
                        color=t.flow_line_color,
                        width=1.2,
                        arrow_end=True,
                        arrow_size=6.0,
                    )
                )

                if label:
                    pill_color = S.get_contrast_color(
                        t.surface, light_fg=t.flow_label_color, dark_fg="#0f172a"
                    )
                    self._add(
                        S.pill_label(
                            (x1 + x2) / 2.0,
                            mid_y,
                            label,
                            font=t.font_name_italic,
                            size=7.0,
                            text_color=pill_color,
                            bg_color=t.surface,
                            border_color=t.node_stroke,
                        )
                    )
