from __future__ import annotations

from typing import Any
from .base import DiagramBase
from .theme import DiagramTheme
from . import shapes as S
from .layout import auto_layout_graph


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

    def auto_layout(self) -> None:
        item_names = list(self._items.keys())
        edges = [(r[0], r[1]) for r in self._relations]
        # Layout items hierarchically with spacious node and layer separation
        coords = auto_layout_graph(
            item_names,
            edges,
            self.width,
            self.height,
            node_spacing=180.0,
            layer_spacing=120.0,
        )
        for name in self._items:
            x, y = coords[name]
            self._items[name]["x"] = x
            self._items[name]["y"] = y
        self._normalize_bounds()

    def _normalize_bounds(self) -> None:
        if not self._items:
            return
        min_x, max_x = float("inf"), float("-inf")
        min_y, max_y = float("inf"), float("-inf")
        for item in self._items.values():
            min_x = min(min_x, item["x"] - self._item_w / 2.0)
            max_x = max(max_x, item["x"] + self._item_w / 2.0)
            min_y = min(min_y, item["y"] - self._item_h / 2.0)
            max_y = max(max_y, item["y"] + self._item_h / 2.0)

        margin = 40.0
        calculated_width = max_x - min_x + margin * 2
        calculated_height = max_y - min_y + margin * 2
        shift_x = margin - min_x
        shift_y = margin - min_y
        for item in self._items.values():
            item["x"] += shift_x
            item["y"] += shift_y

        self.width = calculated_width
        self.height = calculated_height
        if hasattr(self, "drawing") and self.drawing:
            self.drawing.width = self.width
            self.drawing.height = self.height

    def build(self) -> None:
        self.auto_layout()
        t = self.theme

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

        # Register item bounding boxes to prevent overlapping labels
        self._label_rects = []
        for name, item in self._items.items():
            self._label_rects.append((item["x"], item["y"], self._item_w, self._item_h))

        # Determine theme darkness for edge color palette
        is_dark = t.surface.startswith("#1") or t.surface.startswith("#0") or t.surface.startswith("#2")
        if is_dark:
            edge_colors = ["#38bdf8", "#34d399", "#f472b6", "#fb923c", "#a78bfa", "#facc15"]
        else:
            edge_colors = ["#0284c7", "#059669", "#db2777", "#ea580c", "#7c3aed", "#ca8a04"]

        # Pre-calculate connection path segments for line obstacle avoidance
        relation_paths: list[list[tuple[float, float, float, float]]] = []
        for rel_idx, (from_item, to_item, label) in enumerate(self._relations):
            if from_item not in self._items or to_item not in self._items:
                relation_paths.append([])
                continue

            it1 = self._items[from_item]
            it2 = self._items[to_item]
            x1, y1 = it1["x"], it1["y"]
            x2, y2 = it2["x"], it2["y"]
            dx = x2 - x1
            dy = y2 - y1
            segments = []

            if abs(dx) > abs(dy):
                if dx > 0:
                    p1_x = x1 + self._item_w / 2.0
                    p2_x = x2 - self._item_w / 2.0
                else:
                    p1_x = x1 - self._item_w / 2.0
                    p2_x = x2 + self._item_w / 2.0

                mid_x = (p1_x + p2_x) / 2.0 + (-12.0 + (rel_idx % 3) * 12.0)
                min_x = min(p1_x, p2_x) + 25.0
                max_x = max(p1_x, p2_x) - 25.0
                if max_x > min_x:
                    mid_x = max(min_x, min(max_x, mid_x))
                else:
                    mid_x = (p1_x + p2_x) / 2.0

                segments.append((p1_x, y1, mid_x, y1))
                segments.append((mid_x, y1, mid_x, y2))
                segments.append((mid_x, y2, p2_x, y2))
            else:
                if dy > 0:
                    p1_y = y1 + self._item_h / 2.0
                    p2_y = y2 - self._item_h / 2.0
                else:
                    p1_y = y1 - self._item_h / 2.0
                    p2_y = y2 + self._item_h / 2.0

                mid_y = (p1_y + p2_y) / 2.0 + (-12.0 + (rel_idx % 3) * 12.0)
                min_y = min(p1_y, p2_y) + 25.0
                max_y = max(p1_y, p2_y) - 25.0
                if max_y > min_y:
                    mid_y = max(min_y, min(max_y, mid_y))
                else:
                    mid_y = (p1_y + p2_y) / 2.0

                segments.append((x1, p1_y, x1, mid_y))
                segments.append((x1, mid_y, x2, mid_y))
                segments.append((x2, mid_y, x2, p2_y))

            relation_paths.append(segments)

        # Draw relationships (orthogonal routing with labels)
        for rel_idx, (from_item, to_item, label) in enumerate(self._relations):
            if from_item not in self._items or to_item not in self._items:
                continue

            # Collect segments of all other connections as obstacles
            other_segments = []
            for j, segments in enumerate(relation_paths):
                if j != rel_idx:
                    other_segments.extend(segments)

            it1 = self._items[from_item]
            it2 = self._items[to_item]

            x1, y1 = it1["x"], it1["y"]
            x2, y2 = it2["x"], it2["y"]

            dx = x2 - x1
            dy = y2 - y1
            line_color = edge_colors[rel_idx % len(edge_colors)]

            if abs(dx) > abs(dy):
                # Side-to-side routing
                if dx > 0:
                    p1_x = x1 + self._item_w / 2.0
                    p2_x = x2 - self._item_w / 2.0
                else:
                    p1_x = x1 - self._item_w / 2.0
                    p2_x = x2 + self._item_w / 2.0

                # Offset vertical segment slightly based on rel_idx
                mid_x = (p1_x + p2_x) / 2.0 + (-12.0 + (rel_idx % 3) * 12.0)
                
                # Clamp mid_x to be at least 25 pt away from both node edges
                min_x = min(p1_x, p2_x) + 25.0
                max_x = max(p1_x, p2_x) - 25.0
                if max_x > min_x:
                    mid_x = max(min_x, min(max_x, mid_x))
                else:
                    mid_x = (p1_x + p2_x) / 2.0

                self._add(
                    S.solid_line(
                        p1_x, y1, mid_x, y1, color=line_color, width=1.2
                    )
                )
                self._add(
                    S.solid_line(
                        mid_x, y1, mid_x, y2, color=line_color, width=1.2
                    )
                )
                self._add(
                    S.arrow_line(
                        mid_x,
                        y2,
                        p2_x,
                        y2,
                        color=line_color,
                        width=1.2,
                        arrow_end=True,
                        arrow_size=6.0,
                    )
                )

                if label:
                    lw = S.text_width(label, font=t.font_name_italic, size=7.0)
                    pill_w = lw + 12.0
                    pill_h = 14.0
                    # Dynamically find segment label position along the vertical mid segment
                    lx, ly = self.get_segment_label_position(mid_x, y1, mid_x, y2, pill_w, pill_h, "vertical", "middle", other_segments)
                    self._add(
                        S.pill_label(
                            lx,
                            ly,
                            label,
                            font=t.font_name_italic,
                            size=7.0,
                            text_color=line_color,
                            bg_color=t.surface,
                            border_color=line_color,
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

                # Offset horizontal segment slightly based on rel_idx
                mid_y = (p1_y + p2_y) / 2.0 + (-12.0 + (rel_idx % 3) * 12.0)
                
                # Clamp mid_y to be at least 25 pt away from both node edges
                min_y = min(p1_y, p2_y) + 25.0
                max_y = max(p1_y, p2_y) - 25.0
                if max_y > min_y:
                    mid_y = max(min_y, min(max_y, mid_y))
                else:
                    mid_y = (p1_y + p2_y) / 2.0

                self._add(
                    S.solid_line(
                        x1, p1_y, x1, mid_y, color=line_color, width=1.2
                    )
                )
                self._add(
                    S.solid_line(
                        x1, mid_y, x2, mid_y, color=line_color, width=1.2
                    )
                )
                self._add(
                    S.arrow_line(
                        x2,
                        mid_y,
                        x2,
                        p2_y,
                        color=line_color,
                        width=1.2,
                        arrow_end=True,
                        arrow_size=6.0,
                    )
                )

                if label:
                    lw = S.text_width(label, font=t.font_name_italic, size=7.0)
                    pill_w = lw + 12.0
                    pill_h = 14.0
                    lx, ly = self.get_segment_label_position(x1, mid_y, x2, mid_y, pill_w, pill_h, "horizontal", "middle", other_segments)
                    self._add(
                        S.pill_label(
                            lx,
                            ly,
                            label,
                            font=t.font_name_italic,
                            size=7.0,
                            text_color=line_color,
                            bg_color=t.surface,
                            border_color=line_color,
                        )
                    )
