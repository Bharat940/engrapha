from __future__ import annotations

from typing import Any
from .base import DiagramBase
from .theme import DiagramTheme
from . import shapes as S


class ArchitectureDiagram(DiagramBase):
    """
    Architecture Diagram builder.
    Lays out nodes hierarchically: clients at the top, services in the middle, and databases/queues at the bottom.
    Supports orthogonal routing connections.
    """

    def __init__(
        self,
        width: float,
        height: float,
        theme: DiagramTheme | None = None,
        caption: str | None = None,
        orientation: str = "horizontal",
    ) -> None:
        super().__init__(width, height, theme, caption)
        self._nodes: dict[str, dict[str, Any]] = {}
        self._connections: list[tuple[str, str, str]] = []
        self._node_w = 80.0
        self._node_h = 32.0
        self.orientation = orientation

    def _add_node(
        self,
        name: str,
        kind: str,
        label: str = "",
        x: float | None = None,
        y: float | None = None,
    ) -> None:
        self._nodes[name] = {
            "kind": kind,
            "label": label or name,
            "x": x,
            "y": y,
        }

    def client(
        self,
        name: str,
        label: str = "",
        x: float | None = None,
        y: float | None = None,
    ) -> "ArchitectureDiagram":
        """Add a client node (top tier)."""
        self._add_node(name, "client", label, x, y)
        return self

    def service(
        self,
        name: str,
        label: str = "",
        x: float | None = None,
        y: float | None = None,
    ) -> "ArchitectureDiagram":
        """Add a microservice node (middle tier)."""
        self._add_node(name, "service", label, x, y)
        return self

    def database(
        self,
        name: str,
        label: str = "",
        x: float | None = None,
        y: float | None = None,
    ) -> "ArchitectureDiagram":
        """Add a database cylinder node (bottom tier)."""
        self._add_node(name, "database", label, x, y)
        return self

    def queue(
        self,
        name: str,
        label: str = "",
        x: float | None = None,
        y: float | None = None,
    ) -> "ArchitectureDiagram":
        """Add a queue horizontal pill node (bottom tier)."""
        self._add_node(name, "queue", label, x, y)
        return self

    def connect(
        self, from_node: str, to_node: str, label: str = ""
    ) -> "ArchitectureDiagram":
        """Connect two nodes with an orthogonal line."""
        self._connections.append((from_node, to_node, label))
        return self

    def build(self) -> None:
        t = self.theme

        # Group nodes by rank
        clients = [n for n, c in self._nodes.items() if c["kind"] == "client"]
        services = [n for n, c in self._nodes.items() if c["kind"] == "service"]
        bottoms = [
            n for n, c in self._nodes.items() if c["kind"] in ("database", "queue")
        ]

        margin = 30.0

        # Lay out each rank depending on orientation
        if self.orientation == "vertical":
            top_y = self.height - margin - self._node_h / 2.0
            mid_y = self.height / 2.0
            bot_y = margin + self._node_h / 2.0

            def layout_rank(names: list[str], coord: float) -> None:
                if not names:
                    return
                n = len(names)
                if n == 1:
                    name = names[0]
                    if self._nodes[name]["x"] is None:
                        self._nodes[name]["x"] = self.width / 2.0
                    if self._nodes[name]["y"] is None:
                        self._nodes[name]["y"] = coord
                else:
                    spacing = (self.width - 2.0 * margin - self._node_w) / (n - 1)
                    for i, name in enumerate(sorted(names)):
                        if self._nodes[name]["x"] is None:
                            self._nodes[name]["x"] = (
                                margin + self._node_w / 2.0 + i * spacing
                            )
                        if self._nodes[name]["y"] is None:
                            self._nodes[name]["y"] = coord

            layout_rank(clients, top_y)
            layout_rank(services, mid_y)
            layout_rank(bottoms, bot_y)
        else:  # horizontal
            left_x = margin + self._node_w / 2.0
            mid_x = self.width / 2.0
            right_x = self.width - margin - self._node_w / 2.0

            def layout_rank_h(names: list[str], coord: float) -> None:
                if not names:
                    return
                n = len(names)
                if n == 1:
                    name = names[0]
                    if self._nodes[name]["x"] is None:
                        self._nodes[name]["x"] = coord
                    if self._nodes[name]["y"] is None:
                        self._nodes[name]["y"] = self.height / 2.0
                else:
                    spacing = (self.height - 2.0 * margin - self._node_h) / (n - 1)
                    for i, name in enumerate(sorted(names)):
                        if self._nodes[name]["x"] is None:
                            self._nodes[name]["x"] = coord
                        if self._nodes[name]["y"] is None:
                            self._nodes[name]["y"] = (
                                margin + self._node_h / 2.0 + i * spacing
                            )

            layout_rank_h(clients, left_x)
            layout_rank_h(services, mid_x)
            layout_rank_h(bottoms, right_x)

        # Draw nodes
        for name, nd in self._nodes.items():
            nx, ny = nd["x"], nd["y"]
            kind = nd["kind"]
            label_text = nd["label"]

            x_left = nx - self._node_w / 2.0
            y_bottom = ny - self._node_h / 2.0

            if kind == "client":
                # Clean laptop or terminal box
                self._add(
                    S.rounded_rect(
                        x_left,
                        y_bottom,
                        self._node_w,
                        self._node_h,
                        rx=4.0,
                        fill=t.surface_alt,
                        stroke=t.node_stroke,
                        stroke_width=1.5,
                    )
                )
                self._add(
                    S.centered_wrapped_label(
                        nx,
                        ny,
                        label_text,
                        self._node_w - 8.0,
                        font=t.font_name_bold,
                        size=8.5,
                        color=t.text,
                    )
                )
            elif kind == "service":
                # Microservice rounded rect
                self._add(
                    S.rounded_rect(
                        x_left,
                        y_bottom,
                        self._node_w,
                        self._node_h,
                        rx=4.0,
                        fill=t.process_fill,
                        stroke=t.process_stroke,
                        stroke_width=1.5,
                    )
                )
                self._add(
                    S.centered_wrapped_label(
                        nx,
                        ny,
                        label_text,
                        self._node_w - 8.0,
                        font=t.font_name_bold,
                        size=8.5,
                        color=t.process_text,
                    )
                )
            elif kind == "database":
                # Cylinder database shape
                self._add(
                    S.cylinder(
                        x_left,
                        y_bottom,
                        self._node_w,
                        self._node_h,
                        fill=t.surface,
                        stroke=t.node_stroke,
                        stroke_width=1.5,
                    )
                )
                self._add(
                    S.centered_wrapped_label(
                        nx,
                        ny - 1.5,
                        label_text,
                        self._node_w - 10.0,
                        font=t.font_name_bold,
                        size=8.0,
                        color=t.text,
                    )
                )
            elif kind == "queue":
                # Stadium pill shape
                self._add(
                    S.stadium(
                        x_left,
                        y_bottom,
                        self._node_w,
                        self._node_h,
                        fill=t.decision_fill,
                        stroke=t.decision_stroke,
                        stroke_width=1.5,
                    )
                )
                self._add(
                    S.centered_wrapped_label(
                        nx,
                        ny,
                        label_text,
                        self._node_w - 12.0,
                        font=t.font_name_bold,
                        size=8.0,
                        color=t.decision_text,
                    )
                )

        # Draw orthogonal routed connections
        for from_n, to_n, label in self._connections:
            if from_n not in self._nodes or to_n not in self._nodes:
                continue

            nd1 = self._nodes[from_n]
            nd2 = self._nodes[to_n]

            x1, y1 = nd1["x"], nd1["y"]
            x2, y2 = nd2["x"], nd2["y"]

            if self.orientation == "vertical":
                if abs(y1 - y2) > 10.0:
                    if y1 > y2:
                        p1_y = y1 - self._node_h / 2.0
                        p2_y = y2 + self._node_h / 2.0
                    else:
                        p1_y = y1 + self._node_h / 2.0
                        p2_y = y2 - self._node_h / 2.0

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
                else:
                    if x1 < x2:
                        p1_x = x1 + self._node_w / 2.0
                        p2_x = x2 - self._node_w / 2.0
                    else:
                        p1_x = x1 - self._node_w / 2.0
                        p2_x = x2 + self._node_w / 2.0

                    self._add(
                        S.arrow_line(
                            p1_x,
                            y1,
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
                                (p1_x + p2_x) / 2.0,
                                y1,
                                label,
                                font=t.font_name_italic,
                                size=7.0,
                                text_color=pill_color,
                                bg_color=t.surface,
                                border_color=t.node_stroke,
                            )
                        )
            else:  # horizontal orientation
                if abs(x1 - x2) > 10.0:
                    if x1 < x2:
                        p1_x = x1 + self._node_w / 2.0
                        p2_x = x2 - self._node_w / 2.0
                    else:
                        p1_x = x1 - self._node_w / 2.0
                        p2_x = x2 + self._node_w / 2.0

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
                    if y1 > y2:
                        p1_y = y1 - self._node_h / 2.0
                        p2_y = y2 + self._node_h / 2.0
                    else:
                        p1_y = y1 + self._node_h / 2.0
                        p2_y = y2 - self._node_h / 2.0

                    self._add(
                        S.arrow_line(
                            x1,
                            p1_y,
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
                                x1,
                                (p1_y + p2_y) / 2.0,
                                label,
                                font=t.font_name_italic,
                                size=7.0,
                                text_color=pill_color,
                                bg_color=t.surface,
                                border_color=t.node_stroke,
                            )
                        )
