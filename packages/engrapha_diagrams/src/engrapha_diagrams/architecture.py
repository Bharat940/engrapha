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
        self._connections: list[tuple[str, str, str] | tuple[str, str, str, str]] = []
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
        self, from_node: str, to_node: str, label: str = "", label_pos: str = "middle"
    ) -> "ArchitectureDiagram":
        """Connect two nodes with an orthogonal line."""
        self._connections.append((from_node, to_node, label, label_pos))
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
        # Dynamically determine y/x coordinates for occupied tiers to prevent empty spaces
        occupied_tiers = []
        if clients:
            occupied_tiers.append("client")
        if services:
            occupied_tiers.append("service")
        if bottoms:
            occupied_tiers.append("bottom")

        tier_coords = {}
        if self.orientation == "vertical":
            if len(occupied_tiers) == 1:
                tier_coords[occupied_tiers[0]] = self.height / 2.0
            else:
                usable_h = self.height - 2.0 * margin - self._node_h
                spacing_y = usable_h / (len(occupied_tiers) - 1)
                # Map tiers from bottom to top
                for idx, tier in enumerate(occupied_tiers[::-1]):
                    tier_coords[tier] = margin + self._node_h / 2.0 + idx * spacing_y

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

            layout_rank(clients, tier_coords.get("client", 0.0))
            layout_rank(services, tier_coords.get("service", 0.0))
            layout_rank(bottoms, tier_coords.get("bottom", 0.0))
        else:  # horizontal
            if len(occupied_tiers) == 1:
                tier_coords[occupied_tiers[0]] = self.width / 2.0
            else:
                usable_w = self.width - 2.0 * margin - self._node_w
                spacing_x = usable_w / (len(occupied_tiers) - 1)
                # Map tiers from left to right
                for idx, tier in enumerate(occupied_tiers):
                    tier_coords[tier] = margin + self._node_w / 2.0 + idx * spacing_x

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

            layout_rank_h(clients, tier_coords.get("client", 0.0))
            layout_rank_h(services, tier_coords.get("service", 0.0))
            layout_rank_h(bottoms, tier_coords.get("bottom", 0.0))

        # Pre-calculate connection path segments for line obstacle avoidance
        connection_paths: list[list[tuple[float, float, float, float]]] = []
        for conn_idx, conn_tuple in enumerate(self._connections):
            if len(conn_tuple) == 4:
                from_n, to_n, label, label_pos = conn_tuple  # type: ignore
            else:
                from_n, to_n, label = conn_tuple  # type: ignore

            if from_n not in self._nodes or to_n not in self._nodes:
                connection_paths.append([])
                continue

            nd1 = self._nodes[from_n]
            nd2 = self._nodes[to_n]
            x1, y1 = nd1["x"], nd1["y"]
            x2, y2 = nd2["x"], nd2["y"]
            segments = []

            if self.orientation == "vertical":
                if abs(y1 - y2) > 10.0 and abs(x1 - x2) >= 10.0:
                    if y1 > y2:
                        p1_y = y1 - self._node_h / 2.0
                        p2_y = y2 + self._node_h / 2.0
                    else:
                        p1_y = y1 + self._node_h / 2.0
                        p2_y = y2 - self._node_h / 2.0

                    mid_y = (p1_y + p2_y) / 2.0 + (-12.0 + (conn_idx % 3) * 12.0)
                    min_y = min(p1_y, p2_y) + 25.0
                    max_y = max(p1_y, p2_y) - 25.0
                    if max_y > min_y:
                        mid_y = max(min_y, min(max_y, mid_y))
                    else:
                        mid_y = (p1_y + p2_y) / 2.0

                    segments.append((x1, p1_y, x1, mid_y))
                    segments.append((x1, mid_y, x2, mid_y))
                    segments.append((x2, mid_y, x2, p2_y))
                elif abs(y1 - y2) > 10.0 and abs(x1 - x2) < 10.0:
                    if y1 > y2:
                        p1_y = y1 - self._node_h / 2.0
                        p2_y = y2 + self._node_h / 2.0
                    else:
                        p1_y = y1 + self._node_h / 2.0
                        p2_y = y2 - self._node_h / 2.0
                    segments.append((x1, p1_y, x2, p2_y))
                else:
                    if x1 < x2:
                        p1_x = x1 + self._node_w / 2.0
                        p2_x = x2 - self._node_w / 2.0
                    else:
                        p1_x = x1 - self._node_w / 2.0
                        p2_x = x2 + self._node_w / 2.0
                    segments.append((p1_x, y1, p2_x, y2))
            else:  # horizontal orientation
                if abs(x1 - x2) > 10.0 and abs(y1 - y2) >= 10.0:
                    if x1 < x2:
                        p1_x = x1 + self._node_w / 2.0
                        p2_x = x2 - self._node_w / 2.0
                    else:
                        p1_x = x1 - self._node_w / 2.0
                        p2_x = x2 + self._node_w / 2.0

                    mid_x = (p1_x + p2_x) / 2.0 + (-12.0 + (conn_idx % 3) * 12.0)
                    min_x = min(p1_x, p2_x) + 25.0
                    max_x = max(p1_x, p2_x) - 25.0
                    if max_x > min_x:
                        mid_x = max(min_x, min(max_x, mid_x))
                    else:
                        mid_x = (p1_x + p2_x) / 2.0

                    segments.append((p1_x, y1, mid_x, y1))
                    segments.append((mid_x, y1, mid_x, y2))
                    segments.append((mid_x, y2, p2_x, y2))
                elif abs(x1 - x2) > 10.0 and abs(y1 - y2) < 10.0:
                    if x1 < x2:
                        p1_x = x1 + self._node_w / 2.0
                        p2_x = x2 - self._node_w / 2.0
                    else:
                        p1_x = x1 - self._node_w / 2.0
                        p2_x = x2 + self._node_w / 2.0
                    segments.append((p1_x, y1, p2_x, y2))
                else:
                    if y1 > y2:
                        p1_y = y1 - self._node_h / 2.0
                        p2_y = y2 + self._node_h / 2.0
                    else:
                        p1_y = y1 + self._node_h / 2.0
                        p2_y = y2 - self._node_h / 2.0
                    segments.append((x1, p1_y, x2, p2_y))

            connection_paths.append(segments)

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

        # Register node bounding boxes to prevent overlapping labels
        self._label_rects = []
        for name, nd in self._nodes.items():
            self._label_rects.append((nd["x"], nd["y"], self._node_w, self._node_h))

        # Draw orthogonal routed connections
        # Determine theme darkness for edge color palette
        is_dark = (
            t.surface.startswith("#1")
            or t.surface.startswith("#0")
            or t.surface.startswith("#2")
        )
        if is_dark:
            edge_colors = [
                "#38bdf8",
                "#34d399",
                "#f472b6",
                "#fb923c",
                "#a78bfa",
                "#facc15",
            ]
        else:
            edge_colors = [
                "#0284c7",
                "#059669",
                "#db2777",
                "#ea580c",
                "#7c3aed",
                "#ca8a04",
            ]

        # Draw orthogonal routed connections
        for conn_idx, conn_tuple in enumerate(self._connections):
            # Support both 3-tuple and 4-tuple connections for backwards compatibility
            if len(conn_tuple) == 4:
                from_n, to_n, label, label_pos = conn_tuple  # type: ignore
            else:
                from_n, to_n, label = conn_tuple  # type: ignore
                label_pos = "middle"

            if from_n not in self._nodes or to_n not in self._nodes:
                continue

            # Collect segments of all other connections as obstacles
            other_segments = []
            for j, segments in enumerate(connection_paths):
                if j != conn_idx:
                    other_segments.extend(segments)

            nd1 = self._nodes[from_n]
            nd2 = self._nodes[to_n]

            x1, y1 = nd1["x"], nd1["y"]
            x2, y2 = nd2["x"], nd2["y"]
            line_color = edge_colors[conn_idx % len(edge_colors)]

            if self.orientation == "vertical":
                if abs(y1 - y2) > 10.0 and abs(x1 - x2) >= 10.0:
                    if y1 > y2:
                        p1_y = y1 - self._node_h / 2.0
                        p2_y = y2 + self._node_h / 2.0
                    else:
                        p1_y = y1 + self._node_h / 2.0
                        p2_y = y2 - self._node_h / 2.0

                    # Offset vertical segment midpoint slightly to prevent exact line overlaps
                    mid_y = (p1_y + p2_y) / 2.0 + (-12.0 + (conn_idx % 3) * 12.0)
                    
                    # Clamp mid_y to be at least 25 pt away from both p1_y and p2_y to prevent mushing
                    min_y = min(p1_y, p2_y) + 25.0
                    max_y = max(p1_y, p2_y) - 25.0
                    if max_y > min_y:
                        mid_y = max(min_y, min(max_y, mid_y))
                    else:
                        mid_y = (p1_y + p2_y) / 2.0

                    # 3-segment route: vertical -> horizontal -> vertical (entering target vertically)
                    self._add(S.solid_line(x1, p1_y, x1, mid_y, color=line_color, width=1.2))
                    self._add(S.solid_line(x1, mid_y, x2, mid_y, color=line_color, width=1.2))
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
                        # Dynamically find segment label position along the horizontal mid segment
                        lx, ly = self.get_segment_label_position(x1, mid_y, x2, mid_y, pill_w, pill_h, "horizontal", label_pos, other_segments)
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
                elif abs(y1 - y2) > 10.0 and abs(x1 - x2) < 10.0:
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
                        # Dynamically find segment label position along the vertical arrow
                        lx, ly = self.get_segment_label_position(x1, p1_y, x2, p2_y, pill_w, pill_h, "vertical", label_pos, other_segments)
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
                        # Dynamically find segment label position along the horizontal arrow
                        lx, ly = self.get_segment_label_position(p1_x, y1, p2_x, y1, pill_w, pill_h, "horizontal", label_pos, other_segments)
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
            else:  # horizontal orientation
                if abs(x1 - x2) > 10.0 and abs(y1 - y2) >= 10.0:
                    if x1 < x2:
                        p1_x = x1 + self._node_w / 2.0
                        p2_x = x2 - self._node_w / 2.0
                    else:
                        p1_x = x1 - self._node_w / 2.0
                        p2_x = x2 + self._node_w / 2.0

                    # Offset horizontal segment midpoint slightly to prevent exact line overlaps
                    mid_x = (p1_x + p2_x) / 2.0 + (-12.0 + (conn_idx % 3) * 12.0)
                    
                    # Clamp mid_x to be at least 25 pt away from both p1_x and p2_x to prevent mushing
                    min_x = min(p1_x, p2_x) + 25.0
                    max_x = max(p1_x, p2_x) - 25.0
                    if max_x > min_x:
                        mid_x = max(min_x, min(max_x, mid_x))
                    else:
                        mid_x = (p1_x + p2_x) / 2.0

                    # 3-segment route: horizontal -> vertical -> horizontal (entering target horizontally)
                    self._add(S.solid_line(p1_x, y1, mid_x, y1, color=line_color, width=1.2))
                    self._add(S.solid_line(mid_x, y1, mid_x, y2, color=line_color, width=1.2))
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
                        lx, ly = self.get_segment_label_position(mid_x, y1, mid_x, y2, pill_w, pill_h, "vertical", label_pos, other_segments)
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
                elif abs(x1 - x2) > 10.0 and abs(y1 - y2) < 10.0:
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
                        # Dynamically find segment label position along the horizontal arrow
                        lx, ly = self.get_segment_label_position(p1_x, y1, p2_x, y2, pill_w, pill_h, "horizontal", label_pos, other_segments)
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
                        # Dynamically find segment label position along the vertical arrow
                        lx, ly = self.get_segment_label_position(x1, p1_y, x1, p2_y, pill_w, pill_h, "vertical", label_pos, other_segments)
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
