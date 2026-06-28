"""
flowchart.py -- Flowchart diagram builder.

Supports all standard ANSI/ISO flowchart symbols:
  process      -- rectangle
  decision     -- diamond
  terminal     -- stadium (pill shape)
  io           -- parallelogram
  connector    -- small circle
  predefined   -- rectangle with double vertical side lines

Edges support optional yes/no branch labels and directed arrows.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Literal, Callable

from pydantic import BaseModel, model_validator

if TYPE_CHECKING:
    pass

from . import shapes as S
from .base import DiagramBase
from .layout import (
    auto_layout_graph,
    edge_clip_circle,
)
from .theme import DiagramTheme

NodeKind = Literal[
    "process", "decision", "terminal", "io", "connector", "predefined", "custom"
]
Branch = str


# Default node dimensions
_NODE_W = 90.0
_NODE_H = 28.0
_DIAMOND_W = 70.0
_DIAMOND_H = 36.0
_CONN_R = 12.0
_TERM_W = 90.0
_TERM_H = 26.0
_MAX_LABEL_W = 132.0
_MAX_DECISION_LABEL_W = 76.0


class _FCNode(BaseModel):
    id: str
    label: str
    kind: NodeKind
    x: float | None = None
    y: float | None = None

    @model_validator(mode="after")
    def validate_id(self) -> "_FCNode":
        if not self.id.strip():
            raise ValueError("Node id must not be empty")
        return self


class _FCEdge(BaseModel):
    from_id: str
    to_id: str
    label: str = ""
    branch: Branch = ""
    path: list[tuple[float, float]] | None = None
    orthogonal: bool = False


class Flowchart(DiagramBase):
    """
    Flowchart diagram builder.

    Usage::

        fc = Flowchart(width=300, height=300, caption="Algorithm Flowchart")
        fc.terminal("start", "START", x=150, y=270)
        fc.process("init", "Initialize i = 0", x=150, y=220)
        fc.decision("cond", "i < N?", x=150, y=165)
        fc.process("body", "Process item[i]", x=260, y=165)
        fc.process("inc", "i = i + 1", x=260, y=110)
        fc.terminal("end", "END", x=150, y=60)
        fc.edge("start", "init")
        fc.edge("init", "cond")
        fc.edge("cond", "body", branch="yes")
        fc.edge("body", "inc")
        fc.edge("inc", "cond")
        fc.edge("cond", "end", branch="no")
        story.extend(fc.as_flowable())
    """

    def __init__(
        self,
        width: float,
        height: float,
        theme: DiagramTheme | None = None,
        caption: str | None = None,
        direction: str = "TB",
        scale_factor: float | None = None,
    ) -> None:
        super().__init__(width, height, theme, caption)
        self.direction = direction
        self._user_scale_factor = scale_factor
        self._nodes: list[_FCNode] = []
        self._edges: list[_FCEdge] = []
        self._node_index: dict[str, _FCNode] = {}
        self._custom_drawers: dict[
            str, Callable[["Flowchart", float, float, str, str], None]
        ] = {}
        if scale_factor is not None:
            self.scale_factor = scale_factor
        else:
            w_scale = self.width / 650.0
            h_scale = self.height / 550.0
            self.scale_factor = max(0.85, min(1.25, (w_scale * 0.5 + h_scale * 0.5)))

    def _register(self, node: _FCNode) -> "Flowchart":
        if node.id in self._node_index:
            raise ValueError(f"Duplicate node id: '{node.id}'")
        self._nodes.append(node)
        self._node_index[node.id] = node
        return self

    def custom(
        self,
        id: str,
        label: str,
        x: float | None = None,
        y: float | None = None,
        custom_draw: "Callable[[Flowchart, float, float, str, str], None] | None" = None,
    ) -> "Flowchart":
        """Add a custom shape node."""
        self._register(_FCNode(id=id, label=label, kind="custom", x=x, y=y))
        if custom_draw is not None:
            self._custom_drawers[id] = custom_draw
        return self

    def process(
        self, id: str, label: str, x: float | None = None, y: float | None = None
    ) -> "Flowchart":
        """Add a process (rectangle) node."""
        return self._register(_FCNode(id=id, label=label, kind="process", x=x, y=y))

    def decision(
        self, id: str, label: str, x: float | None = None, y: float | None = None
    ) -> "Flowchart":
        """Add a decision (diamond) node."""
        return self._register(_FCNode(id=id, label=label, kind="decision", x=x, y=y))

    def terminal(
        self, id: str, label: str, x: float | None = None, y: float | None = None
    ) -> "Flowchart":
        """Add a terminal (pill) node -- start or end."""
        return self._register(_FCNode(id=id, label=label, kind="terminal", x=x, y=y))

    def io_box(
        self, id: str, label: str, x: float | None = None, y: float | None = None
    ) -> "Flowchart":
        """Add an I/O (parallelogram) node."""
        return self._register(_FCNode(id=id, label=label, kind="io", x=x, y=y))

    def connector(
        self, id: str, label: str, x: float | None = None, y: float | None = None
    ) -> "Flowchart":
        """Add a connector (circle) node -- off-page or on-page connector."""
        return self._register(_FCNode(id=id, label=label, kind="connector", x=x, y=y))

    def predefined(
        self, id: str, label: str, x: float | None = None, y: float | None = None
    ) -> "Flowchart":
        """Add a predefined-process node (rectangle with double vertical lines)."""
        return self._register(_FCNode(id=id, label=label, kind="predefined", x=x, y=y))

    def edge(
        self,
        from_id: str,
        to_id: str,
        label: str = "",
        branch: Branch = "",
        path: list[tuple[float, float]] | None = None,
        orthogonal: bool = False,
    ) -> "Flowchart":
        """
        Add a directed edge from from_id to to_id.
        branch: 'yes' or 'no' for decision branches.
        path: list of intermediate waypoints.
        orthogonal: whether to auto-route orthogonally.
        Raises ValueError if either node id is unknown.
        """
        for nid in (from_id, to_id):
            if nid not in self._node_index:
                raise ValueError(
                    f"Node id '{nid}' not found. Add node before adding edges."
                )
        self._edges.append(
            _FCEdge(
                from_id=from_id,
                to_id=to_id,
                label=label,
                branch=branch,
                path=path,
                orthogonal=orthogonal,
            )
        )
        return self

    # -- Geometry helpers --

    def _text_style(self, node: _FCNode) -> tuple[str, float]:
        scale = getattr(self, "scale_factor", 1.0)
        if node.kind == "terminal":
            return self.theme.font_name_bold, 8.5 * scale
        if node.kind == "connector":
            return self.theme.font_name_bold, 7.5 * scale
        if node.kind == "decision":
            return self.theme.font_name, 8.0 * scale
        return self.theme.font_name, 8.5 * scale

    def _label_lines(self, node: _FCNode) -> list[str]:
        font, size = self._text_style(node)
        scale = getattr(self, "scale_factor", 1.0)
        if node.kind == "connector":
            max_width = _CONN_R * scale * 1.3
        elif node.kind == "decision":
            max_width = _MAX_DECISION_LABEL_W * scale
        else:
            max_width = _MAX_LABEL_W * scale
        return S.wrap_text(node.label, max_width, font=font, size=size)

    def _get_size(self, node: _FCNode) -> tuple[float, float]:
        font, size = self._text_style(node)
        lines = self._label_lines(node)
        widest = max(S.text_width(line, font, size) for line in lines)
        line_height = size * 1.2
        scale = getattr(self, "scale_factor", 1.0)
        if node.kind == "decision":
            w = max(_DIAMOND_W * scale, widest * 2.0 + 26.0 * scale)
            h = max(_DIAMOND_H * scale, len(lines) * line_height + 28.0 * scale)
            return w, h
        if node.kind == "connector":
            return _CONN_R * 2 * scale, _CONN_R * 2 * scale
        needed_w = widest + 22.0 * scale
        needed_h = len(lines) * line_height + 12.0 * scale
        if node.kind == "terminal":
            return max(_TERM_W * scale, needed_w), max(_TERM_H * scale, needed_h)
        if node.kind == "io":
            return max(_NODE_W * scale, needed_w + 10.0 * scale), max(
                _NODE_H * scale, needed_h
            )
        # process, predefined
        return max(_NODE_W * scale, needed_w), max(_NODE_H * scale, needed_h)

    def _node_bounds(self, node: _FCNode) -> tuple[float, float, float, float]:
        """Return (cx, cy, w, h) for clip calculations."""
        assert node.x is not None and node.y is not None
        w, h = self._get_size(node)
        return node.x, node.y, w, h

    def _clip_node(self, node: _FCNode, tx: float, ty: float) -> tuple[float, float]:
        """Clip an edge to one of the four cardinal ports of the node."""
        cx, cy, w, h = self._node_bounds(node)
        dx = tx - cx
        dy = ty - cy
        if node.kind == "connector":
            return edge_clip_circle(cx, cy, w / 2.0, tx, ty)
        if abs(dx) > abs(dy):
            if dx > 0:
                return cx + w / 2.0, cy
            else:
                return cx - w / 2.0, cy
        else:
            if dy > 0:
                return cx, cy + h / 2.0
            else:
                return cx, cy - h / 2.0

    def _draw_node_label(self, node: _FCNode, max_width: float) -> None:
        assert node.x is not None and node.y is not None
        font, size = self._text_style(node)
        if node.kind == "decision":
            fill_color = self.theme.decision_fill
            text_color_theme = self.theme.decision_text
        elif node.kind == "terminal":
            fill_color = self.theme.terminal_fill
            text_color_theme = self.theme.terminal_text
        else:
            fill_color = self.theme.process_fill
            text_color_theme = self.theme.process_text

        color = S.get_contrast_color(
            fill_color, light_fg=text_color_theme, dark_fg="#0f172a"
        )

        scale = getattr(self, "scale_factor", 1.0)
        self._add(
            S.centered_wrapped_label(
                node.x + ((5.0 * scale) if node.kind == "io" else 0.0),
                node.y,
                node.label,
                max_width=max_width,
                font=font,
                size=size,
                color=color,
            )
        )

    def _draw_node(self, node: _FCNode) -> None:
        t = self.theme
        assert node.x is not None and node.y is not None
        cx, cy = node.x, node.y
        w, h = self._get_size(node)
        scale = getattr(self, "scale_factor", 1.0)
        if node.kind == "process":
            ex = cx - w / 2
            ey = cy - h / 2
            self._add(
                S.rounded_rect(
                    ex,
                    ey,
                    w,
                    h,
                    rx=4 * scale,
                    fill=t.process_fill,
                    stroke=t.process_stroke,
                )
            )
            process_color = S.get_contrast_color(
                t.process_fill, light_fg=t.process_text, dark_fg="#0f172a"
            )
            self._add(
                S.centered_wrapped_label(
                    cx,
                    cy,
                    node.label,
                    max_width=w - 18.0 * scale,
                    font=t.font_name,
                    size=8.5 * scale,
                    color=process_color,
                )
            )

        elif node.kind == "decision":
            self._add(
                S.diamond(
                    cx,
                    cy,
                    w,
                    h,
                    fill=t.decision_fill,
                    stroke=t.decision_stroke,
                )
            )
            self._draw_node_label(node, _MAX_DECISION_LABEL_W * scale)

        elif node.kind == "terminal":
            ex = cx - w / 2
            ey = cy - h / 2
            self._add(
                S.stadium(
                    ex,
                    ey,
                    w,
                    h,
                    fill=t.terminal_fill,
                    stroke=t.terminal_stroke,
                )
            )
            self._draw_node_label(node, w - 20.0 * scale)

        elif node.kind == "io":
            ex = cx - w / 2
            ey = cy - h / 2
            self._add(S.parallelogram(ex, ey, w, h, fill=t.io_fill, stroke=t.io_stroke))
            self._draw_node_label(node, w - 25.0 * scale)

        elif node.kind == "connector":
            self._add(
                S.circle(
                    cx, cy, w / 2, fill=t.connector_fill, stroke=t.connector_stroke
                )
            )
            self._draw_node_label(node, w * 0.75)

        elif node.kind == "predefined":
            ex = cx - w / 2
            ey = cy - h / 2
            self._add(
                S.rounded_rect(
                    ex,
                    ey,
                    w,
                    h,
                    rx=2 * scale,
                    fill=t.predefined_fill,
                    stroke=t.predefined_stroke,
                )
            )
            # Double vertical lines on left and right
            inset = 8.0 * scale
            self._add(
                S.solid_line(
                    ex + inset,
                    ey,
                    ex + inset,
                    ey + h,
                    color=t.predefined_stroke,
                    width=0.9 * scale,
                )
            )
            self._add(
                S.solid_line(
                    ex + w - inset,
                    ey,
                    ex + w - inset,
                    ey + h,
                    color=t.predefined_stroke,
                    width=0.9 * scale,
                )
            )
            self._draw_node_label(node, w - inset * 2 - 8.0 * scale)

        elif node.kind == "custom":
            drawer = self._custom_drawers.get(node.id)
            if drawer is not None:
                drawer(self, cx, cy, t.process_fill, t.process_stroke)
            else:
                ex = cx - w / 2
                ey = cy - h / 2
                self._add(
                    S.rounded_rect(
                        ex,
                        ey,
                        w,
                        h,
                        rx=4 * scale,
                        fill=t.process_fill,
                        stroke=t.process_stroke,
                    )
                )
            self._draw_node_label(node, w - 18.0 * scale)

    def _draw_edge(self, edge: _FCEdge) -> None:
        t = self.theme
        fn = self._node_index[edge.from_id]
        tn = self._node_index[edge.to_id]
        fcx, fcy, _, _ = self._node_bounds(fn)
        tcx, tcy, _, _ = self._node_bounds(tn)

        points: list[tuple[float, float]] = []

        if edge.path:
            points = [(fcx, fcy)] + edge.path + [(tcx, tcy)]
        elif edge.orthogonal:
            dx = tcx - fcx
            dy = tcy - fcy
            if abs(dy) < 2.0:
                points = [(fcx, fcy), (tcx, tcy)]
            elif abs(dx) < 2.0 and tcy < fcy:
                points = [(fcx, fcy), (tcx, tcy)]
            elif tcy > fcy:
                # Going upwards (back-loop)
                # Route outwards horizontally, then up, then back in
                mid_x = self.width / 2.0
                if fcx < mid_x:
                    x_out = min(fcx - 35.0, 20.0)
                    x_out = max(15.0, x_out)
                else:
                    x_out = max(fcx + 35.0, self.width - 20.0)
                    x_out = min(self.width - 15.0, x_out)
                points = [(fcx, fcy), (x_out, fcy), (x_out, tcy), (tcx, tcy)]
            else:
                # Going downwards
                if fn.kind == "decision":
                    # Exits horizontally from the side of the diamond, then vertically down
                    points = [(fcx, fcy), (tcx, fcy), (tcx, tcy)]
                else:
                    # Going downwards: step-down route
                    mid_y = fcy + dy / 2.0
                    points = [(fcx, fcy), (fcx, mid_y), (tcx, mid_y), (tcx, tcy)]
        else:
            points = [(fcx, fcy), (tcx, tcy)]

        # Clip endpoints to node borders
        if len(points) >= 2:
            cx1, cy1 = self._clip_node(fn, points[1][0], points[1][1])
            points[0] = (cx1, cy1)
            cx2, cy2 = self._clip_node(tn, points[-2][0], points[-2][1])
            points[-1] = (cx2, cy2)

        scale = getattr(self, "scale_factor", 1.0)
        # Draw segments
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]
            is_last = i == len(points) - 2
            self._add(
                S.arrow_line(
                    x1,
                    y1,
                    x2,
                    y2,
                    color=t.flow_line_color,
                    width=1.3 * scale,
                    arrow_end=is_last,
                    arrow_size=7.0 * scale,
                )
            )

        # Branch / edge labels
        combined = ""
        if edge.branch.lower() == "yes":
            combined = f"Yes  {edge.label}".strip()
        elif edge.branch.lower() == "no":
            combined = f"No  {edge.label}".strip()
        elif edge.branch:
            combined = f"{edge.branch}  {edge.label}".strip()
        else:
            combined = edge.label

        if combined:
            # Place label on first segment
            x1, y1 = points[0]
            x2, y2 = points[1]
            fraction = 0.5
            mx = x1 + (x2 - x1) * fraction
            my = y1 + (y2 - y1) * fraction

            font_size = 7.5 * scale
            pad_x = 3.5 * scale
            pad_y = 2.0 * scale

            lines = combined.splitlines() or [""]
            tw = max(
                S.text_width(line, t.font_name_italic, font_size) for line in lines
            )
            lh = font_size * 1.2
            pill_w = tw + 2 * pad_x
            pill_h = font_size + (len(lines) - 1) * lh + 2 * pad_y

            if abs(y2 - y1) < 2.0:
                # Horizontal segment
                lx, ly = mx, my + 6 * scale + pill_h / 2.0
            elif abs(x2 - x1) < 2.0:
                # Vertical segment
                lx, ly = mx + 6 * scale + pill_w / 2.0, my
            else:
                # Diagonal segment
                lx, ly = mx + 6 * scale + pill_w / 2.0, my

            rx, ry = self.get_non_overlapping_position(lx, ly, pill_w, pill_h)
            pill_text_color = S.get_contrast_color(
                t.surface, light_fg=t.flow_label_color, dark_fg="#0f172a"
            )

            self._add(
                S.pill_label(
                    rx,
                    ry,
                    combined,
                    font=t.font_name_italic,
                    size=font_size,
                    text_color=pill_text_color,
                    bg_color=t.surface,
                    border_color=t.process_stroke,
                    pad_x=pad_x,
                    pad_y=pad_y,
                )
            )

    def auto_layout(self) -> None:
        # Scale up canvas to prevent overlaps and squishing
        self.width = max(self.width, 350.0)
        self.height = max(self.height, 120.0)
        if self._user_scale_factor is not None:
            self.scale_factor = self._user_scale_factor
        else:
            w_scale = self.width / 650.0
            h_scale = self.height / 550.0
            self.scale_factor = max(0.85, min(1.25, (w_scale * 0.5 + h_scale * 0.5)))
        if hasattr(self, "drawing") and self.drawing:
            self.drawing.width = self.width
            self.drawing.height = self.height

        node_ids = [n.id for n in self._nodes]
        edges = [(e.from_id, e.to_id) for e in self._edges]
        coords = auto_layout_graph(
            node_ids, edges, self.width, self.height, direction=self.direction
        )
        for n in self._nodes:
            if n.x is None or n.y is None:
                x, y = coords[n.id]
                if n.x is None:
                    n.x = x
                if n.y is None:
                    n.y = y

        self._normalize_bounds()

    def _normalize_bounds(self) -> None:
        # Normalization / Bounding Box adjustment
        min_x, max_x = float("inf"), float("-inf")
        min_y, max_y = float("inf"), float("-inf")
        for n in self._nodes:
            w, h = self._get_size(n)
            assert n.x is not None and n.y is not None
            min_x = min(min_x, n.x - w / 2)
            max_x = max(max_x, n.x + w / 2)
            min_y = min(min_y, n.y - h / 2)
            max_y = max(max_y, n.y + h / 2)

        margin = 35.0
        shift_x = margin - min_x
        shift_y = margin - min_y
        for n in self._nodes:
            assert n.x is not None and n.y is not None
            n.x += shift_x
            n.y += shift_y

        for edge in self._edges:
            if edge.path:
                edge.path = [(px + shift_x, py + shift_y) for px, py in edge.path]

        self.width = max_x - min_x + margin * 2
        self.height = max_y - min_y + margin * 2
        if hasattr(self, "drawing") and self.drawing:
            self.drawing.width = self.width
            self.drawing.height = self.height

    def build(self) -> None:
        if self._user_scale_factor is not None:
            self.scale_factor = self._user_scale_factor
        unspecified = any(n.x is None or n.y is None for n in self._nodes)
        if unspecified:
            self.auto_layout()
        else:
            self._normalize_bounds()

        # Register node bounding boxes to prevent overlapping labels
        self._label_rects = []
        for node in self._nodes:
            cx, cy, w, h = self._node_bounds(node)
            self._label_rects.append((cx, cy, w, h))

        for edge in self._edges:
            self._draw_edge(edge)
        for node in self._nodes:
            self._draw_node(node)
