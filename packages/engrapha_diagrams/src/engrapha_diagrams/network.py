"""
network.py -- Network topology diagram builder.

Node kinds and their shapes:
  host      -- rectangle
  router    -- hexagon
  switch    -- octagon
  hub       -- circle
  server    -- rectangle with rack lines
  cloud     -- cloud (overlapping circles)
  database  -- cylinder
  firewall  -- rectangle with diagonal cross-hatch lines
  wireless  -- access point antenna
  load_balancer -- traffic distribution appliance
  printer   -- printer endpoint
  storage   -- storage appliance
  mobile    -- mobile endpoint
  generic   -- circle

Preset topology methods: bus, star, ring, mesh.
"""

from __future__ import annotations

from typing import Literal, Mapping, Callable, cast
from reportlab.lib.colors import Color

from pydantic import BaseModel, model_validator

from . import shapes as S
from .shapes import pill_label as _pill
from .base import DiagramBase
from .layout import (
    bus_line_y,
    distribute_around,
    edge_clip_cloud,
    edge_clip_circle,
    edge_clip_rect,
    midpoint,
    auto_layout_graph,
)
from .theme import DiagramTheme

NodeKind = Literal[
    "host",
    "router",
    "switch",
    "hub",
    "server",
    "cloud",
    "database",
    "firewall",
    "wireless",
    "load_balancer",
    "printer",
    "storage",
    "mobile",
    "generic",
    "custom",
    "bus",
    "text",
]

_NODE_W = 56.0
_NODE_H = 28.0
_CIRC_R = 16.0
_MAX_LABEL_W = 86.0


class _NetNode(BaseModel):
    id: str
    label: str
    kind: str
    x: float | None = None
    y: float | None = None
    label_pos: str = "auto"

    @model_validator(mode="after")
    def validate_id(self) -> "_NetNode":
        if not self.id.strip():
            raise ValueError("Node id must not be empty")
        return self


class _NetEdge(BaseModel):
    from_id: str
    to_id: str
    label: str = ""
    bidirectional: bool = True


class NetworkDiagram(DiagramBase):
    """
    Network topology diagram builder.

    Usage::

        net = NetworkDiagram(width=400, height=160, caption="Star Topology")
        net.node("sw", "Switch", x=200, y=80, kind="switch")
        net.node("h1", "Host A", x=80, y=140, kind="host")
        net.node("h2", "Host B", x=200, y=140, kind="host")
        net.node("h3", "Host C", x=320, y=140, kind="host")
        net.link("sw", "h1")
        net.link("sw", "h2")
        net.link("sw", "h3")
        story.extend(net.as_flowable())

    Or use a preset layout::

        net = NetworkDiagram(width=400, height=180)
        net.ring_topology(["A", "B", "C", "D", "E"])
        story.extend(net.as_flowable())
    """

    def __init__(
        self,
        width: float,
        height: float,
        theme: DiagramTheme | None = None,
        caption: str | None = None,
    ) -> None:
        super().__init__(width, height, theme, caption)
        self._nodes: list[_NetNode] = []
        self._edges: list[_NetEdge] = []
        self._node_index: dict[str, _NetNode] = {}
        self._custom_drawers: dict[
            str,
            Callable[[NetworkDiagram, float, float, float, float, Color, Color], None],
        ] = {}
        self._custom_clippers: dict[
            str,
            Callable[[float, float, float, float, float, float], tuple[float, float]],
        ] = {}

    def node(
        self,
        id: str,
        label: str,
        x: float | None = None,
        y: float | None = None,
        kind: NodeKind = "generic",
        custom_draw: (
            Callable[[NetworkDiagram, float, float, float, float, Color, Color], None]
            | None
        ) = None,
        label_pos: str = "auto",
        custom_clip: (
            Callable[[float, float, float, float, float, float], tuple[float, float]]
            | None
        ) = None,
    ) -> "NetworkDiagram":
        """Add a network node at (x, y)."""
        if id in self._node_index:
            raise ValueError(f"Duplicate node id: '{id}'")
        n = _NetNode(id=id, label=label, kind=kind, x=x, y=y, label_pos=label_pos)
        self._nodes.append(n)
        self._node_index[id] = n
        if custom_draw is not None:
            self._custom_drawers[id] = custom_draw
        if custom_clip is not None:
            self._custom_clippers[id] = custom_clip
        return self

    def link(
        self,
        from_id: str,
        to_id: str,
        label: str = "",
        bidirectional: bool = True,
    ) -> "NetworkDiagram":
        """Add an edge (link) between two nodes."""
        for nid in (from_id, to_id):
            if nid not in self._node_index:
                raise ValueError(f"Node id '{nid}' not found. Add node before linking.")
        self._edges.append(
            _NetEdge(
                from_id=from_id, to_id=to_id, label=label, bidirectional=bidirectional
            )
        )
        return self

    # -- Preset topology helpers --

    def bus_topology(
        self,
        node_ids: list[str],
        labels: list[str] | None = None,
        kind: NodeKind = "host",
        bus_y: float | None = None,
        margin: float = 30.0,
    ) -> "NetworkDiagram":
        """
        Create a bus topology: a horizontal backbone line with nodes hanging off it.
        node_ids and labels define the nodes; positions are computed automatically.
        """
        if labels is None:
            labels = node_ids
        if len(node_ids) != len(labels):
            raise ValueError("node_ids and labels must have the same length")

        count = len(node_ids)
        bx = bus_y if bus_y is not None else bus_line_y(self.height)
        spacing = (self.width - margin * 2) / max(count - 1, 1)

        # Bus backbone node (invisible anchor)
        for i, (nid, lbl) in enumerate(zip(node_ids, labels)):
            nx = margin + i * spacing
            self.node(nid, lbl, nx, bx - 40, kind=kind)

        # Backbone line drawn manually in build
        self._bus_y = bx
        self._bus_x1 = margin
        self._bus_x2 = self.width - margin

        for nid in node_ids:
            self._node_index[nid]
            self._edges.append(
                _NetEdge(from_id=nid, to_id=nid, label="__bus__", bidirectional=False)
            )
        return self

    def star_topology(
        self,
        center_id: str,
        center_label: str,
        spoke_ids: list[str],
        spoke_labels: list[str] | None = None,
        center_kind: NodeKind = "switch",
        spoke_kind: NodeKind = "host",
    ) -> "NetworkDiagram":
        """Create a star topology. Center node at diagram center, spokes arranged around it."""
        if spoke_labels is None:
            spoke_labels = spoke_ids
        if len(spoke_ids) != len(spoke_labels):
            raise ValueError("spoke_ids and spoke_labels must have the same length")

        cx, cy = self.width / 2, self.height / 2
        self.node(center_id, center_label, cx, cy, kind=center_kind)

        radius = min(self.width, self.height) * 0.36
        positions = distribute_around(cx, cy, radius, len(spoke_ids))
        for (sx, sy), sid, slbl in zip(positions, spoke_ids, spoke_labels):
            self.node(sid, slbl, sx, sy, kind=spoke_kind)
            self.link(center_id, sid)
        return self

    def ring_topology(
        self,
        node_ids: list[str],
        labels: list[str] | None = None,
        kind: NodeKind = "host",
    ) -> "NetworkDiagram":
        """Create a ring topology. Nodes arranged in a circle with edges connecting neighbors."""
        if labels is None:
            labels = node_ids
        if len(node_ids) != len(labels):
            raise ValueError("node_ids and labels must have the same length")

        cx, cy = self.width / 2, self.height / 2
        radius = min(self.width, self.height) * 0.36
        positions = distribute_around(cx, cy, radius, len(node_ids))
        for (nx, ny), nid, lbl in zip(positions, node_ids, labels):
            self.node(nid, lbl, nx, ny, kind=kind)
        for i, nid in enumerate(node_ids):
            next_id = node_ids[(i + 1) % len(node_ids)]
            self.link(nid, next_id)
        return self

    def mesh_topology(
        self,
        node_ids: list[str],
        labels: list[str] | None = None,
        kind: NodeKind = "router",
    ) -> "NetworkDiagram":
        """Full mesh topology -- every node connected to every other node."""
        if labels is None:
            labels = node_ids
        if len(node_ids) != len(labels):
            raise ValueError("node_ids and labels must have the same length")

        cx, cy = self.width / 2, self.height / 2
        radius = min(self.width, self.height) * 0.36
        positions = distribute_around(cx, cy, radius, len(node_ids))
        for (nx, ny), nid, lbl in zip(positions, node_ids, labels):
            self.node(nid, lbl, nx, ny, kind=kind)
        for i in range(len(node_ids)):
            for j in range(i + 1, len(node_ids)):
                self.link(node_ids[i], node_ids[j])
        return self

    def tree_topology(
        self,
        parent_child_map: dict[str, list[str]],
        node_labels: dict[str, str] | None = None,
        node_kinds: Mapping[str, NodeKind] | None = None,
        margin_x: float = 40.0,
        margin_y: float = 35.0,
    ) -> "NetworkDiagram":
        """
        Create a tree/hierarchical topology.
        Positions are automatically computed level-by-level using BFS,
        and links are automatically added from parents to children.
        """
        all_nodes: set[str] = set()
        has_parent: set[str] = set()
        for parent, children in parent_child_map.items():
            all_nodes.add(parent)
            for child in children:
                all_nodes.add(child)
                has_parent.add(child)

        roots = [n for n in all_nodes if n not in has_parent]
        if not roots:
            roots = [list(parent_child_map.keys())[0]] if parent_child_map else []

        # Find BFS depths
        depths: dict[str, int] = {}
        visited = set(roots)
        queue = [(r, 0) for r in roots]
        while queue:
            node, depth = queue.pop(0)
            depths[node] = depth
            for c in parent_child_map.get(node, []):
                if c not in visited:
                    visited.add(c)
                    queue.append((c, depth + 1))

        unvisited = all_nodes - visited
        for node in sorted(unvisited):
            depths[node] = 0

        # Number of levels
        if depths:
            num_levels = max(depths.values()) + 1
        else:
            num_levels = 1

        usable_w = self.width - margin_x * 2
        usable_h = self.height - margin_y * 2

        # Compute horizontal positions recursively
        positions: dict[str, float] = {}

        def position_subtree(nid: str, xmin: float, xmax: float) -> None:
            cx = (xmin + xmax) / 2.0
            positions[nid] = cx
            children = parent_child_map.get(nid, [])
            if not children:
                return
            num_children = len(children)
            child_w = (xmax - xmin) / num_children
            for idx, child in enumerate(children):
                c_xmin = xmin + idx * child_w
                c_xmax = c_xmin + child_w
                position_subtree(child, c_xmin, c_xmax)

        # Position roots
        num_roots = len(roots)
        if num_roots > 0:
            root_w = usable_w / num_roots
            for idx, r in enumerate(roots):
                r_xmin = margin_x + idx * root_w
                r_xmax = r_xmin + root_w
                position_subtree(r, r_xmin, r_xmax)

        # Now draw the nodes
        for nid in all_nodes:
            d = depths.get(nid, 0)
            if num_levels > 1:
                ny = self.height - margin_y - d * (usable_h / (num_levels - 1))
            else:
                ny = self.height / 2

            nx = positions.get(nid, self.width / 2.0)
            lbl = node_labels.get(nid, nid) if node_labels else nid
            kind = node_kinds.get(nid, "generic") if node_kinds else "generic"
            self.node(nid, lbl, nx, ny, kind=kind)

        for parent, children in parent_child_map.items():
            for child in children:
                self.link(parent, child)

        return self

    # -- Internal node geometry --

    def _node_center(self, node: _NetNode) -> tuple[float, float]:
        assert node.x is not None and node.y is not None
        return node.x, node.y

    def _label_lines(self, node: _NetNode) -> list[str]:
        return S.wrap_text(
            node.label, _MAX_LABEL_W, font=self.theme.font_name_bold, size=8.0
        )

    def _label_height(self, node: _NetNode) -> float:
        return len(self._label_lines(node)) * 9.6

    def _node_size(self, node: _NetNode) -> tuple[float, float]:
        if node.kind == "text":
            return 0.0, 0.0
        if node.kind == "bus":
            return 410.0, 16.0
        if node.kind == "cloud":
            return _NODE_W * 1.4, _NODE_H * 1.4
        if node.kind == "mobile":
            return 20.0, 34.0
        if node.kind == "printer":
            return 38.0, 32.0
        if node.kind in (
            "host",
            "server",
            "firewall",
            "database",
            "load_balancer",
            "storage",
            "custom",
        ):
            return _NODE_W, _NODE_H
        return _CIRC_R * 2, _CIRC_R * 2

    def _clip_to_node(
        self, node: _NetNode, tx: float, ty: float
    ) -> tuple[float, float]:
        assert node.x is not None and node.y is not None
        cx, cy = node.x, node.y
        if node.kind == "text":
            return cx, cy
        width, height = self._node_size(node)
        if node.kind == "custom" and node.id in self._custom_clippers:
            return self._custom_clippers[node.id](cx, cy, width, height, tx, ty)
        if node.kind in (
            "host",
            "server",
            "firewall",
            "database",
            "load_balancer",
            "printer",
            "storage",
            "mobile",
            "custom",
            "bus",
        ):
            return edge_clip_rect(cx, cy, width, height, tx, ty)
        if node.kind == "cloud":
            w, h = self._node_size(node)
            return edge_clip_cloud(cx, cy, w, h, tx, ty)
        return edge_clip_circle(cx, cy, _CIRC_R, tx, ty)

    def _draw_node(self, node: _NetNode) -> None:
        t = self.theme
        assert node.x is not None and node.y is not None
        cx, cy = node.x, node.y
        fill = t.node_fill
        stroke = t.node_stroke
        text_color = t.node_text
        _, node_height = self._node_size(node)

        if node.kind == "host":
            self._add(
                S.rounded_rect(
                    cx - _NODE_W / 2,
                    cy - _NODE_H / 2,
                    _NODE_W,
                    _NODE_H,
                    rx=4,
                    fill=fill,
                    stroke=stroke,
                )
            )
            self._add(
                S.label(
                    cx,
                    cy - 3.5,
                    node.kind.upper(),
                    font=t.font_name,
                    size=6.0,
                    color=stroke,
                    anchor="middle",
                )
            )

        elif node.kind == "router":
            self._add(S.hexagon(cx, cy, _CIRC_R, fill=fill, stroke=stroke))

        elif node.kind == "switch":
            self._add(S.octagon(cx, cy, _CIRC_R, fill=fill, stroke=stroke))

        elif node.kind == "hub":
            self._add(S.circle(cx, cy, _CIRC_R, fill=fill, stroke=stroke))

        elif node.kind == "server":
            self._add(
                S.rounded_rect(
                    cx - _NODE_W / 2,
                    cy - _NODE_H / 2,
                    _NODE_W,
                    _NODE_H,
                    rx=3,
                    fill=fill,
                    stroke=stroke,
                )
            )
            self._add(
                S.rack_lines(
                    cx - _NODE_W / 2, cy - _NODE_H / 2, _NODE_W, _NODE_H, color=stroke
                )
            )

        elif node.kind == "cloud":
            self._add(
                S.cloud(cx, cy, _NODE_W * 1.4, _NODE_H * 1.4, fill=fill, stroke=stroke)
            )

        elif node.kind == "database":
            self._add(
                S.cylinder(
                    cx - _NODE_W / 2,
                    cy - _NODE_H / 2,
                    _NODE_W,
                    _NODE_H,
                    fill=fill,
                    stroke=stroke,
                )
            )

        elif node.kind == "firewall":
            w, h = _NODE_W, _NODE_H
            self._add(
                S.plain_rect(
                    cx - w / 2,
                    cy - h / 2,
                    w,
                    h,
                    fill=fill,
                    stroke=stroke,
                )
            )
            self._add(
                S.solid_line(
                    cx - w / 2,
                    cy - h / 6,
                    cx + w / 2,
                    cy - h / 6,
                    color=stroke,
                    width=0.6,
                )
            )
            self._add(
                S.solid_line(
                    cx - w / 2,
                    cy + h / 6,
                    cx + w / 2,
                    cy + h / 6,
                    color=stroke,
                    width=0.6,
                )
            )
            self._add(
                S.solid_line(
                    cx - w / 4,
                    cy + h / 6,
                    cx - w / 4,
                    cy + h / 2,
                    color=stroke,
                    width=0.6,
                )
            )
            self._add(
                S.solid_line(
                    cx + w / 4,
                    cy + h / 6,
                    cx + w / 4,
                    cy + h / 2,
                    color=stroke,
                    width=0.6,
                )
            )
            self._add(
                S.solid_line(cx, cy - h / 6, cx, cy + h / 6, color=stroke, width=0.6)
            )
            self._add(
                S.solid_line(
                    cx - w / 2.5,
                    cy - h / 6,
                    cx - w / 2.5,
                    cy + h / 6,
                    color=stroke,
                    width=0.6,
                )
            )
            self._add(
                S.solid_line(
                    cx + w / 2.5,
                    cy - h / 6,
                    cx + w / 2.5,
                    cy + h / 6,
                    color=stroke,
                    width=0.6,
                )
            )
            self._add(
                S.solid_line(
                    cx - w / 4,
                    cy - h / 2,
                    cx - w / 4,
                    cy - h / 6,
                    color=stroke,
                    width=0.6,
                )
            )
            self._add(
                S.solid_line(
                    cx + w / 4,
                    cy - h / 2,
                    cx + w / 4,
                    cy - h / 6,
                    color=stroke,
                    width=0.6,
                )
            )

        elif node.kind == "wireless":
            self._add(S.solid_line(cx, cy - 10, cx, cy + 3, color=stroke, width=1.5))
            self._add(
                S.circle(cx, cy + 5, 2.5, fill=fill, stroke=stroke, stroke_width=1.0)
            )
            self._add(
                S.solid_line(cx - 3, cy + 9, cx - 6, cy + 6, color=stroke, width=0.9)
            )
            self._add(
                S.solid_line(cx - 6, cy + 6, cx - 3, cy + 3, color=stroke, width=0.9)
            )
            self._add(
                S.solid_line(cx + 3, cy + 9, cx + 6, cy + 6, color=stroke, width=0.9)
            )
            self._add(
                S.solid_line(cx + 6, cy + 6, cx + 3, cy + 3, color=stroke, width=0.9)
            )
            self._add(
                S.solid_line(cx - 5, cy + 12, cx - 9, cy + 6, color=stroke, width=0.7)
            )
            self._add(S.solid_line(cx - 9, cy + 6, cx - 5, cy, color=stroke, width=0.7))
            self._add(
                S.solid_line(cx + 5, cy + 12, cx + 9, cy + 6, color=stroke, width=0.7)
            )
            self._add(S.solid_line(cx + 9, cy + 6, cx + 5, cy, color=stroke, width=0.7))

        elif node.kind == "load_balancer":
            self._add(
                S.rounded_rect(
                    cx - _NODE_W / 2,
                    cy - _NODE_H / 2,
                    _NODE_W,
                    _NODE_H,
                    rx=5,
                    fill=fill,
                    stroke=stroke,
                )
            )
            self._add(S.solid_line(cx - 15, cy, cx + 13, cy, color=stroke, width=1.0))
            self._add(S.solid_line(cx, cy, cx + 13, cy + 8, color=stroke, width=1.0))
            self._add(S.solid_line(cx, cy, cx + 13, cy - 8, color=stroke, width=1.0))

        elif node.kind == "printer":
            self._add(
                S.rounded_rect(cx - 19, cy - 10, 38, 18, rx=2, fill=fill, stroke=stroke)
            )
            self._add(S.plain_rect(cx - 13, cy + 5, 26, 10, fill=fill, stroke=stroke))
            self._add(S.plain_rect(cx - 13, cy - 13, 26, 9, fill=fill, stroke=stroke))

        elif node.kind == "storage":
            self._add(
                S.rounded_rect(
                    cx - _NODE_W / 2,
                    cy - _NODE_H / 2,
                    _NODE_W,
                    _NODE_H,
                    rx=3,
                    fill=fill,
                    stroke=stroke,
                )
            )
            for offset in (-7.0, 0.0, 7.0):
                self._add(
                    S.solid_line(
                        cx - 20,
                        cy + offset,
                        cx + 20,
                        cy + offset,
                        color=stroke,
                        width=0.8,
                    )
                )

        elif node.kind == "mobile":
            self._add(
                S.rounded_rect(cx - 10, cy - 17, 20, 34, rx=3, fill=fill, stroke=stroke)
            )
            self._add(S.circle(cx, cy - 12, 1.5, fill=stroke, stroke=stroke))

        elif node.kind == "custom":
            drawer = self._custom_drawers.get(node.id)
            if drawer is not None:
                width, height = self._node_size(node)
                drawer(
                    self,
                    cx,
                    cy,
                    width,
                    height,
                    t.rl_color(fill),
                    t.rl_color(stroke),
                )
            else:
                self._add(S.circle(cx, cy, _CIRC_R, fill=fill, stroke=stroke))

        elif node.kind == "bus":
            w, h = self._node_size(node)
            self._add(
                S.rounded_rect(
                    cx - w / 2,
                    cy - h / 2,
                    w,
                    h,
                    rx=3,
                    fill=fill,
                    stroke=stroke,
                    stroke_width=1.5,
                )
            )
            text_color_bus = S.get_contrast_color(
                fill, light_fg=t.node_text, dark_fg="#0f172a"
            )
            self._add(
                S.label(
                    cx,
                    cy - 2.5,
                    node.label,
                    font=t.font_name_bold,
                    size=8.0,
                    color=text_color_bus,
                    anchor="middle",
                )
            )

        elif node.kind == "text":
            pass

        else:  # generic
            self._add(S.circle(cx, cy, _CIRC_R, fill=fill, stroke=stroke))

        # Label positioning (above, below, left, right, or auto based on edges)
        if node.kind != "bus":
            label_height = self._label_height(node)
            lines = self._label_lines(node)
            (
                max(S.text_width(line, t.font_name_bold, 8.0) for line in lines)
                if lines
                else 0.0
            )

            pos = node.label_pos
            if pos == "auto":
                go_down = 0
                go_up = 0
                for edge in self._edges:
                    if edge.label == "__bus__":
                        continue
                    other_id = None
                    if edge.from_id == node.id:
                        other_id = edge.to_id
                    elif edge.to_id == node.id:
                        other_id = edge.from_id

                    if other_id and other_id in self._node_index:
                        other = self._node_index[other_id]
                        if other.y is not None and node.y is not None:
                            if other.y < node.y:
                                go_down += 1
                            elif other.y > node.y:
                                go_up += 1
                pos = "above" if go_down > go_up else "below"

            # Calculate label center coordinate offsets
            node_width, node_height = self._node_size(node)
            anchor = "middle"
            if pos == "above":
                lbl_x = cx
                lbl_y_centered = cy + node_height / 2.0 + 4.0 + label_height / 2.0
            elif pos == "below":
                lbl_x = cx
                lbl_y_centered = cy - node_height / 2.0 - 4.0 - label_height / 2.0
            elif pos == "left":
                lbl_x = cx - node_width / 2.0 - 10.0
                lbl_y_centered = cy
                anchor = "end"
            elif pos == "right":
                lbl_x = cx + node_width / 2.0 + 10.0
                lbl_y_centered = cy
                anchor = "start"
            else:
                lbl_x = cx
                lbl_y_centered = cy - node_height / 2.0 - 4.0 - label_height / 2.0

            label_text_color = S.get_contrast_color(
                t.bg, light_fg=text_color, dark_fg="#0f172a"
            )
            self._add(
                S.centered_wrapped_label(
                    lbl_x,
                    lbl_y_centered,
                    node.label,
                    max_width=_MAX_LABEL_W,
                    font=t.font_name_bold,
                    size=8.0,
                    color=label_text_color,
                    anchor=cast(Literal["start", "middle", "end"], anchor),
                )
            )

    def _draw_edge(self, edge: _NetEdge) -> None:
        if edge.label == "__bus__":
            return  # bus backbone drawn separately
        t = self.theme
        fn = self._node_index[edge.from_id]
        tn = self._node_index[edge.to_id]
        assert fn.x is not None and fn.y is not None
        assert tn.x is not None and tn.y is not None

        # Straight vertical connections for bus
        if fn.kind == "bus":
            _, bus_h = self._node_size(fn)
            y1 = fn.y + (bus_h / 2.0 if tn.y > fn.y else -bus_h / 2.0)
            x1 = tn.x
            x2, y2 = self._clip_to_node(tn, x1, y1)
        elif tn.kind == "bus":
            _, bus_h = self._node_size(tn)
            y2 = tn.y + (bus_h / 2.0 if fn.y > tn.y else -bus_h / 2.0)
            x2 = fn.x
            x1, y1 = self._clip_to_node(fn, x2, y2)
        else:
            x1, y1 = self._clip_to_node(fn, tn.x, tn.y)
            x2, y2 = self._clip_to_node(tn, fn.x, fn.y)

        if not edge.bidirectional:
            self._add(
                S.arrow_line(
                    x1,
                    y1,
                    x2,
                    y2,
                    color=t.edge_color,
                    width=1.3,
                    arrow_end=True,
                    arrow_start=False,
                    arrow_size=6.0,
                )
            )
        else:
            self._add(S.solid_line(x1, y1, x2, y2, color=t.edge_color, width=1.3))

        if edge.label:
            mx, my = midpoint(x1, y1, x2, y2)
            # If the midpoint is on/near the horizontal bus backbone, shift the label vertically
            # to prevent it from overlapping the bus shape.
            if hasattr(self, "_bus_y") and abs(my - self._bus_y) < 15.0:
                if y1 > y2:
                    my += 25.0
                else:
                    my -= 25.0

            font_size = 7.0
            pad_x = 3.5
            pad_y = 2.0

            lines = edge.label.splitlines() or [""]
            tw = max(
                S.text_width(line, t.font_name_italic, font_size) for line in lines
            )
            lh = font_size * 1.2
            pill_w = tw + 2 * pad_x
            pill_h = font_size + (len(lines) - 1) * lh + 2 * pad_y

            lx, ly = self.get_non_overlapping_position(mx, my + 4, pill_w, pill_h)
            pill_text_color = S.get_contrast_color(
                t.surface, light_fg=t.edge_label_color, dark_fg="#0f172a"
            )

            self._add(
                _pill(
                    lx,
                    ly,
                    edge.label,
                    font=t.font_name_italic,
                    size=font_size,
                    text_color=pill_text_color,
                    bg_color=t.surface,
                    border_color=t.node_stroke,
                    pad_x=pad_x,
                    pad_y=pad_y,
                )
            )

    def auto_layout(self) -> None:
        # Scale up canvas to prevent overlaps and squishing
        self.width = max(self.width, 650.0)
        self.height = max(self.height, 400.0)
        if hasattr(self, "drawing") and self.drawing:
            self.drawing.width = self.width
            self.drawing.height = self.height

        node_ids = [n.id for n in self._nodes]
        edges = [(e.from_id, e.to_id) for e in self._edges]
        coords = auto_layout_graph(node_ids, edges, self.width, self.height)
        for n in self._nodes:
            if n.x is None or n.y is None:
                x, y = coords[n.id]
                if n.x is None:
                    n.x = x
                if n.y is None:
                    n.y = y

        # Normalization / Bounding Box adjustment
        min_x, max_x = float("inf"), float("-inf")
        min_y, max_y = float("inf"), float("-inf")
        for n in self._nodes:
            assert n.x is not None and n.y is not None
            w, h = self._node_size(n)
            min_x = min(min_x, n.x - w / 2, n.x - _MAX_LABEL_W / 2)
            max_x = max(max_x, n.x + w / 2, n.x + _MAX_LABEL_W / 2)
            min_y = min(min_y, n.y - h / 2 - 13.0 - self._label_height(n))
            max_y = max(max_y, n.y + h / 2)

        margin = 35.0
        shift_x = margin - min_x
        shift_y = margin - min_y
        for n in self._nodes:
            assert n.x is not None and n.y is not None
            n.x += shift_x
            n.y += shift_y

        self.width = max_x - min_x + margin * 2
        self.height = max_y - min_y + margin * 2
        if hasattr(self, "drawing") and self.drawing:
            self.drawing.width = self.width
            self.drawing.height = self.height

    def build(self) -> None:
        unspecified = any(n.x is None or n.y is None for n in self._nodes)
        if unspecified:
            self.auto_layout()

        # Register node bounding boxes to prevent labels from overlapping them
        self._label_rects = []
        for node in self._nodes:
            assert node.x is not None and node.y is not None
            nw, nh = self._node_size(node)
            lines = self._label_lines(node)
            lbl_w = (
                max(
                    S.text_width(line, self.theme.font_name_bold, 8.0) for line in lines
                )
                if lines
                else 0.0
            )

            lbl_h = len(lines) * 9.6

            pos = node.label_pos
            if pos == "auto":
                go_down = 0
                go_up = 0
                for edge in self._edges:
                    if edge.label == "__bus__":
                        continue
                    other_id = None
                    if edge.from_id == node.id:
                        other_id = edge.to_id
                    elif edge.to_id == node.id:
                        other_id = edge.from_id

                    if other_id and other_id in self._node_index:
                        other = self._node_index[other_id]
                        if other.y is not None and node.y is not None:
                            if other.y < node.y:
                                go_down += 1
                            elif other.y > node.y:
                                go_up += 1
                pos = "above" if go_down > go_up else "below"

            # Register bounding box depending on label position
            if pos == "above":
                cy_offset = lbl_h / 2.0
                cx_offset = 0.0
                rect_w = max(nw, lbl_w)
                rect_h = nh + lbl_h + 8.0
            elif pos == "below":
                cy_offset = -lbl_h / 2.0
                cx_offset = 0.0
                rect_w = max(nw, lbl_w)
                rect_h = nh + lbl_h + 8.0
            elif pos == "left":
                cy_offset = 0.0
                cx_offset = -lbl_w / 2.0
                rect_w = nw + lbl_w + 12.0
                rect_h = max(nh, lbl_h)
            elif pos == "right":
                cy_offset = 0.0
                cx_offset = lbl_w / 2.0
                rect_w = nw + lbl_w + 12.0
                rect_h = max(nh, lbl_h)
            else:
                cy_offset = -lbl_h / 2.0
                cx_offset = 0.0
                rect_w = max(nw, lbl_w)
                rect_h = nh + lbl_h + 8.0

            self._label_rects.append(
                (node.x + cx_offset, node.y + cy_offset, rect_w, rect_h)
            )

        t = self.theme
        # Bus backbone (if bus_topology was used)
        if hasattr(self, "_bus_y"):
            self._add(
                S.solid_line(
                    self._bus_x1,
                    self._bus_y,
                    self._bus_x2,
                    self._bus_y,
                    color=t.edge_color,
                    width=2.5,
                )
            )
            # Vertical stubs from nodes to bus
            for node in self._nodes:
                assert node.x is not None and node.y is not None
                self._add(
                    S.solid_line(
                        node.x,
                        node.y + _NODE_H / 2,
                        node.x,
                        self._bus_y,
                        color=t.edge_color,
                        width=1.3,
                    )
                )

        # Merge parallel edges for drawing to avoid duplicate overlapping lines and labels
        merged_edges: list[_NetEdge] = []
        edge_groups: dict[tuple[str, str], list[_NetEdge]] = {}
        for edge in self._edges:
            sorted_nodes = sorted([edge.from_id, edge.to_id])
            pair = (sorted_nodes[0], sorted_nodes[1])
            edge_groups.setdefault(pair, []).append(edge)

        for pair, group in edge_groups.items():
            if len(group) == 1:
                merged_edges.append(group[0])
            else:
                # Merge labels
                labels = [e.label for e in group if e.label]
                seen_labels = []
                for lbl in labels:
                    if lbl not in seen_labels:
                        seen_labels.append(lbl)
                merged_label = " & ".join(seen_labels) if seen_labels else ""

                # Determine bidirectional
                has_bidirectional = any(e.bidirectional for e in group)
                directions = set((e.from_id, e.to_id) for e in group)
                is_bidirectional = has_bidirectional or len(directions) > 1

                first = group[0]
                merged_edges.append(
                    _NetEdge(
                        from_id=first.from_id,
                        to_id=first.to_id,
                        label=merged_label,
                        bidirectional=is_bidirectional,
                    )
                )

        for edge in merged_edges:
            self._draw_edge(edge)
        for node in self._nodes:
            self._draw_node(node)
