"""
er_diagram.py -- Entity-Relationship diagram builder.

Supports: entities (strong/weak), relationships (regular/identifying),
attributes (simple, primary key, derived, multivalued, composite),
connections with cardinality and participation (total/partial).
"""

from __future__ import annotations

import math

from pydantic import BaseModel, model_validator

from . import shapes as S
from .base import DiagramBase
from .layout import distribute_around, edge_clip_rect, auto_layout_graph
from .theme import DiagramTheme

# Default geometry constants (in points)
_ENTITY_W = 90.0
_ENTITY_H = 28.0
_REL_W = 60.0
_REL_H = 28.0
_ATTR_RX = 36.0
_ATTR_RY = 14.0


# ---------------------------------------------------------------------------
# Pydantic models
# ---------------------------------------------------------------------------


class _Entity(BaseModel):
    name: str
    x: float | None = None
    y: float | None = None
    weak: bool = False

    @model_validator(mode="after")
    def validate_name(self) -> "_Entity":
        if not self.name.strip():
            raise ValueError("Entity name must not be empty")
        return self


class _Relationship(BaseModel):
    name: str
    x: float | None = None
    y: float | None = None
    identifying: bool = False

    @model_validator(mode="after")
    def validate_name(self) -> "_Relationship":
        if not self.name.strip():
            raise ValueError("Relationship name must not be empty")
        return self


class _Attribute(BaseModel):
    name: str
    parent: str  # entity or relationship name this attribute belongs to
    x: float | None = None
    y: float | None = None
    pk: bool = False
    derived: bool = False
    multivalued: bool = False


class _Connection(BaseModel):
    from_name: str
    to_name: str
    card_from: str = "1"
    card_to: str = "N"
    total_from: bool = False
    total_to: bool = False


# ---------------------------------------------------------------------------
# Builder
# ---------------------------------------------------------------------------


class ERDiagram(DiagramBase):
    """
    ER diagram builder using Chen notation.

    Usage::

        er = ERDiagram(width=450, height=220, caption="University ER Diagram")
        er.entity("STUDENT", x=80, y=110)
        er.entity("COURSE", x=370, y=110)
        er.relationship("ENROLLS", x=225, y=110)
        er.attribute("Student_ID", parent="STUDENT", x=80, y=170, pk=True)
        er.attribute("Grade", parent="ENROLLS", x=225, y=55)
        er.connect("STUDENT", "ENROLLS", card_from="M", card_to="N", total_from=True)
        er.connect("ENROLLS", "COURSE", card_from="N", card_to="1")
        story.extend(er.as_flowable())
    """

    def __init__(
        self,
        width: float,
        height: float,
        theme: DiagramTheme | None = None,
        caption: str | None = None,
        entity_w: float = _ENTITY_W,
        entity_h: float = _ENTITY_H,
        rel_w: float = _REL_W,
        rel_h: float = _REL_H,
        attr_rx: float = _ATTR_RX,
        attr_ry: float = _ATTR_RY,
    ) -> None:
        super().__init__(width, height, theme, caption)
        self.entity_w = entity_w
        self.entity_h = entity_h
        self.rel_w = rel_w
        self.rel_h = rel_h
        self.attr_rx = attr_rx
        self.attr_ry = attr_ry

        self._entities: list[_Entity] = []
        self._relationships: list[_Relationship] = []
        self._attributes: list[_Attribute] = []
        self._connections: list[_Connection] = []

    # -- Fluent builder methods --

    def entity(
        self,
        name: str,
        x: float | None = None,
        y: float | None = None,
        weak: bool = False,
    ) -> "ERDiagram":
        """Add a strong (default) or weak entity."""
        self._entities.append(_Entity(name=name, x=x, y=y, weak=weak))
        return self

    def relationship(
        self,
        name: str,
        x: float | None = None,
        y: float | None = None,
        identifying: bool = False,
    ) -> "ERDiagram":
        """Add a relationship diamond. identifying=True draws a double diamond."""
        self._relationships.append(
            _Relationship(name=name, x=x, y=y, identifying=identifying)
        )
        return self

    def attribute(
        self,
        name: str,
        parent: str,
        x: float | None = None,
        y: float | None = None,
        pk: bool = False,
        derived: bool = False,
        multivalued: bool = False,
    ) -> "ERDiagram":
        """
        Add an attribute ellipse connected to parent entity/relationship.
        Only one of pk, derived, multivalued should be True.
        """
        if sum([pk, derived, multivalued]) > 1:
            raise ValueError(
                f"Attribute '{name}': only one of pk/derived/multivalued may be True"
            )
        self._attributes.append(
            _Attribute(
                name=name,
                parent=parent,
                x=x,
                y=y,
                pk=pk,
                derived=derived,
                multivalued=multivalued,
            )
        )
        return self

    def entity_attributes(
        self,
        entity_id: str,
        attrs: list[str | tuple[str, dict[str, bool]]],
        distance: float = 70.0,
        start_angle: float = 90.0,
    ) -> "ERDiagram":
        """
        Automatically layouts and adds multiple attributes positioned in a circle
        around the parent entity.
        attrs: list of strings (simple attribute names) or tuples: (name, options_dict)
               e.g. [("Student_ID", {"pk": True}), "Name", ("Phone", {"multivalued": True})]
        """
        ent = next((e for e in self._entities if e.name == entity_id), None)
        if not ent:
            raise ValueError(f"Entity '{entity_id}' not found")
        cx, cy = ent.x, ent.y

        if cx is None or cy is None:
            for item in attrs:
                if isinstance(item, tuple):
                    name, opts = item
                else:
                    name, opts = item, {}
                pk = opts.get("pk", False)
                derived = opts.get("derived", False)
                multivalued = opts.get("multivalued", False)
                self.attribute(
                    name=name,
                    parent=entity_id,
                    x=None,
                    y=None,
                    pk=pk,
                    derived=derived,
                    multivalued=multivalued,
                )
        else:
            # Auto-compute safe minimum distance to prevent attribute overlap
            ew, _ = self._get_size(entity_id)
            min_dist = (ew / 2.0) + self.attr_rx + 15.0
            actual_distance = max(distance, min_dist)

            count = len(attrs)
            positions = distribute_around(cx, cy, actual_distance, count, start_angle)
            for (ax, ay), item in zip(positions, attrs):
                if isinstance(item, tuple):
                    name, opts = item
                else:
                    name, opts = item, {}

                pk = opts.get("pk", False)
                derived = opts.get("derived", False)
                multivalued = opts.get("multivalued", False)

                self.attribute(
                    name=name,
                    parent=entity_id,
                    x=ax,
                    y=ay,
                    pk=pk,
                    derived=derived,
                    multivalued=multivalued,
                )
        return self

    def connect(
        self,
        from_name: str,
        to_name: str,
        card_from: str = "1",
        card_to: str = "N",
        total_from: bool = False,
        total_to: bool = False,
    ) -> "ERDiagram":
        """
        Add a connection between an entity and a relationship (or vice versa).
        Raises ValueError if either name is not found.
        """
        all_names = {e.name for e in self._entities} | {
            r.name for r in self._relationships
        }
        for name in (from_name, to_name):
            if name not in all_names:
                raise ValueError(
                    f"Name '{name}' not found. Add entity or relationship before connecting."
                )
        self._connections.append(
            _Connection(
                from_name=from_name,
                to_name=to_name,
                card_from=card_from,
                card_to=card_to,
                total_from=total_from,
                total_to=total_to,
            )
        )
        return self

    # -- Internal helpers --

    def _get_center(self, name: str) -> tuple[float, float]:
        for e in self._entities:
            if e.name == name:
                assert e.x is not None and e.y is not None
                return e.x, e.y
        for r in self._relationships:
            if r.name == name:
                assert r.x is not None and r.y is not None
                return r.x, r.y
        for a in self._attributes:
            if a.name == name:
                assert a.x is not None and a.y is not None
                return a.x, a.y
        raise KeyError(f"No element named '{name}'")

    def _get_size(self, name: str) -> tuple[float, float]:
        for e in self._entities:
            if e.name == name:
                w = max(self.entity_w, len(e.name) * 6.0 + 16.0)
                return w, self.entity_h
        for r in self._relationships:
            if r.name == name:
                words = r.name.split()
                max_w_len = max(len(w) for w in words) if words else len(r.name)
                w = max(self.rel_w, max_w_len * 6.0 + 20.0)
                return w, self.rel_h
        for a in self._attributes:
            if a.name == name:
                rx = max(self.attr_rx, len(a.name) * 3.0 + 10.0)
                return rx * 2, self.attr_ry * 2
        return self.attr_rx * 2, self.attr_ry * 2

    def _is_entity(self, name: str) -> bool:
        return any(e.name == name for e in self._entities)

    def _is_relationship(self, name: str) -> bool:
        return any(r.name == name for r in self._relationships)

    def auto_layout(self) -> None:
        """Automatically layout nodes and attributes."""
        self.auto_layout_nodes()
        self.auto_layout_attributes()

    def auto_layout_nodes(self) -> None:
        # Scale up canvas to prevent overlaps and squishing
        self.width = max(self.width, 850.0)
        self.height = max(self.height, 580.0)
        if hasattr(self, "drawing") and self.drawing:
            self.drawing.width = self.width
            self.drawing.height = self.height

        node_names = [e.name for e in self._entities] + [
            r.name for r in self._relationships
        ]
        edges = [(c.from_name, c.to_name) for c in self._connections]
        coords = auto_layout_graph(
            node_names,
            edges,
            self.width,
            self.height,
            node_spacing=240.0,
            layer_spacing=150.0,
        )
        for e in self._entities:
            if e.x is None or e.y is None:
                x, y = coords[e.name]
                if e.x is None:
                    e.x = x
                if e.y is None:
                    e.y = y
        for r in self._relationships:
            if r.x is None or r.y is None:
                x, y = coords[r.name]
                if r.x is None:
                    r.x = x
                if r.y is None:
                    r.y = y

    def auto_layout_attributes(self) -> None:
        for parent_name in [e.name for e in self._entities] + [
            r.name for r in self._relationships
        ]:
            attrs = [
                a
                for a in self._attributes
                if a.parent == parent_name and (a.x is None or a.y is None)
            ]
            if not attrs:
                continue

            px, py = self._get_center(parent_name)
            pw, _ = self._get_size(parent_name)
            distance = (pw / 2.0) + self.attr_rx + 15.0

            # Compute which angular directions are already occupied by connections
            # so that attributes are placed in the largest unoccupied angular gap.
            occupied_angles: list[float] = []
            for conn in self._connections:
                neighbor_name: str | None = None
                if conn.from_name == parent_name:
                    neighbor_name = conn.to_name
                elif conn.to_name == parent_name:
                    neighbor_name = conn.from_name
                if neighbor_name is None:
                    continue
                try:
                    nx, ny = self._get_center(neighbor_name)
                    angle = math.degrees(math.atan2(ny - py, nx - px)) % 360.0
                    occupied_angles.append(angle)
                except KeyError:
                    pass

            if not occupied_angles:
                # No connections: distribute around the whole circle
                positions = distribute_around(
                    px, py, distance, len(attrs), start_angle_deg=90.0
                )
            else:
                # Find the center of the largest gap
                sorted_occ = sorted(set(occupied_angles))
                n = len(sorted_occ)
                
                if n == 1:
                    # Only 1 connection at theta
                    theta = sorted_occ[0]
                    theta_mid = (theta + 180.0) % 360.0
                    gap_size = 360.0
                    max_spread = 240.0  # safe sector opposite to connection
                else:
                    # Multiple connections: find the largest gap
                    best_start = sorted_occ[0]
                    best_gap = 0.0
                    for i in range(n):
                        a1 = sorted_occ[i]
                        a2 = sorted_occ[(i + 1) % n]
                        gap = (a2 - a1) % 360.0
                        if gap > best_gap:
                            best_gap = gap
                            best_start = a1
                    
                    theta_mid = (best_start + best_gap / 2.0) % 360.0
                    gap_size = best_gap
                    
                    # Safe range inside the gap
                    margin_angle = 30.0
                    max_spread = max(0.0, gap_size - 2 * margin_angle)
                
                count = len(attrs)
                if count == 1:
                    spread = 0.0
                    step = 0.0
                else:
                    # Calculate required step dynamically to prevent overlap based on attribute widths
                    required_steps = []
                    for idx in range(count - 1):
                        w1, _ = self._get_size(attrs[idx].name)
                        w2, _ = self._get_size(attrs[idx+1].name)
                        # Center-to-center distance must cover half widths + 10 pt gap
                        dx_req = (w1 + w2) / 2.0 + 10.0
                        ratio = dx_req / (2.0 * distance)
                        if ratio >= 1.0:
                            step_deg = 90.0
                        else:
                            step_deg = math.degrees(2.0 * math.asin(ratio))
                        required_steps.append(step_deg)
                    
                    preferred_step = max(required_steps) if required_steps else 40.0
                    preferred_step = max(40.0, preferred_step)
                    
                    spread = (count - 1) * preferred_step
                    if spread > max_spread:
                        spread = max_spread
                        step = spread / (count - 1)
                    else:
                        step = preferred_step
                
                # Place attributes symmetrically around theta_mid
                positions = []
                if count == 1:
                    rad = math.radians(theta_mid)
                    positions.append((px + distance * math.cos(rad), py + distance * math.sin(rad)))
                else:
                    start_angle = (theta_mid - spread / 2.0) % 360.0
                    for i in range(count):
                        angle = (start_angle + i * step) % 360.0
                        rad = math.radians(angle)
                        positions.append((px + distance * math.cos(rad), py + distance * math.sin(rad)))

            for a, (ax, ay) in zip(attrs, positions):
                if a.x is None:
                    a.x = ax
                if a.y is None:
                    a.y = ay

    def _normalize_bounds(self) -> None:
        # Normalization / Bounding Box adjustment
        min_x, max_x = float("inf"), float("-inf")
        min_y, max_y = float("inf"), float("-inf")
        for e in self._entities:
            assert e.x is not None and e.y is not None
            w, h = self._get_size(e.name)
            min_x = min(min_x, e.x - w / 2)
            max_x = max(max_x, e.x + w / 2)
            min_y = min(min_y, e.y - h / 2)
            max_y = max(max_y, e.y + h / 2)
        for r in self._relationships:
            assert r.x is not None and r.y is not None
            w, h = self._get_size(r.name)
            min_x = min(min_x, r.x - w / 2)
            max_x = max(max_x, r.x + w / 2)
            min_y = min(min_y, r.y - h / 2)
            max_y = max(max_y, r.y + h / 2)
        for a in self._attributes:
            assert a.x is not None and a.y is not None
            w, h = self._get_size(a.name)
            min_x = min(min_x, a.x - w / 2)
            max_x = max(max_x, a.x + w / 2)
            min_y = min(min_y, a.y - h / 2)
            max_y = max(max_y, a.y + h / 2)

        margin = 40.0
        shift_x = margin - min_x
        shift_y = margin - min_y
        for e in self._entities:
            assert e.x is not None and e.y is not None
            e.x += shift_x
            e.y += shift_y
        for r in self._relationships:
            assert r.x is not None and r.y is not None
            r.x += shift_x
            r.y += shift_y
        for a in self._attributes:
            assert a.x is not None and a.y is not None
            a.x += shift_x
            a.y += shift_y

        self.width = max_x - min_x + margin * 2
        self.height = max_y - min_y + margin * 2
        if hasattr(self, "drawing") and self.drawing:
            self.drawing.width = self.width
            self.drawing.height = self.height

    def build(self) -> None:
        nodes_unspecified = any(
            e.x is None or e.y is None for e in self._entities
        ) or any(r.x is None or r.y is None for r in self._relationships)
        if nodes_unspecified:
            self.auto_layout_nodes()

        self.auto_layout_attributes()
        self._normalize_bounds()

        # Register node bounding boxes to prevent badge overlap
        self._label_rects = []
        for e in self._entities:
            assert e.x is not None and e.y is not None
            w, h = self._get_size(e.name)
            self._label_rects.append((e.x, e.y, w, h))
        for r in self._relationships:
            assert r.x is not None and r.y is not None
            w, h = self._get_size(r.name)
            self._label_rects.append((r.x, r.y, w, h))
        for a in self._attributes:
            assert a.x is not None and a.y is not None
            w, h = self._get_size(a.name)
            self._label_rects.append((a.x, a.y, w, h))

        t = self.theme
        badges_to_draw = []

        # 1. Attribute connector lines (drawn first, below everything)
        for attr in self._attributes:
            assert attr.x is not None and attr.y is not None
            ax, ay = attr.x, attr.y
            try:
                px, py = self._get_center(attr.parent)
            except KeyError:
                continue
            self._add(S.solid_line(ax, ay, px, py, color=t.line_color, width=1.0))

        # 2. Entity-relationship connection lines
        for conn in self._connections:
            fx, fy = self._get_center(conn.from_name)
            tx, ty = self._get_center(conn.to_name)
            fw, fh = self._get_size(conn.from_name)
            tw, th = self._get_size(conn.to_name)

            # Clip line endpoints to node borders
            ex1, ey1 = edge_clip_rect(fx, fy, fw, fh, tx, ty)
            ex2, ey2 = edge_clip_rect(tx, ty, tw, th, fx, fy)

            if conn.total_from:
                self._add(S.double_line(ex1, ey1, ex2, ey2, color=t.double_line_color))
            else:
                self._add(S.solid_line(ex1, ey1, ex2, ey2, color=t.line_color))

            # Cardinality badges positioned along the line outside the node boundaries
            dx = ex2 - ex1
            dy = ey2 - ey1
            dist = math.hypot(dx, dy)
            if dist > 36.0:
                ux, uy = dx / dist, dy / dist
                # Perpendicular unit vector (90° rotation of the line direction)
                # This shifts badges BESIDE the line instead of sitting on it.
                perp_x, perp_y = -uy, ux
                perp_off = 10.0
                along_off = 22.0
                card_from_x = ex1 + ux * along_off + perp_x * perp_off
                card_from_y = ey1 + uy * along_off + perp_y * perp_off
                card_to_x = ex2 - ux * along_off + perp_x * perp_off
                card_to_y = ey2 - uy * along_off + perp_y * perp_off
            else:
                card_from_x = ex1 + dx * 0.3
                card_from_y = ey1 + dy * 0.3
                card_to_x = ex2 - dx * 0.3
                card_to_y = ey2 - dy * 0.3

            badge_w, badge_h = 14.0, 14.0
            bx1, by1 = self.get_non_overlapping_position(
                card_from_x, card_from_y, badge_w, badge_h
            )
            bx2, by2 = self.get_non_overlapping_position(
                card_to_x, card_to_y, badge_w, badge_h
            )

            badges_to_draw.append(
                S.badge(
                    bx1,
                    by1,
                    conn.card_from,
                    bg=t.bg,
                    fg=t.cardinality_color,
                    border=t.cardinality_color,
                )
            )
            badges_to_draw.append(
                S.badge(
                    bx2,
                    by2,
                    conn.card_to,
                    bg=t.bg,
                    fg=t.cardinality_color,
                    border=t.cardinality_color,
                )
            )

        # 3. Relationships (drawn before entities so entity sits on top at intersections)
        for rel in self._relationships:
            assert rel.x is not None and rel.y is not None
            rw, rh = self._get_size(rel.name)
            if rel.identifying:
                outer = S.diamond(
                    rel.x,
                    rel.y,
                    rw + 10,
                    rh + 10,
                    fill=t.relation_fill,
                    stroke=t.relation_stroke,
                )
                self._add(outer)
            d = S.diamond(
                rel.x,
                rel.y,
                rw,
                rh,
                fill=t.relation_fill,
                stroke=t.relation_stroke,
            )
            self._add(d)
            lines = rel.name.split()
            lh = 9.0
            start_y = rel.y + (len(lines) - 1) * lh / 2
            for i, word in enumerate(lines):
                word_color = S.get_contrast_color(
                    t.relation_fill, light_fg=t.relation_text, dark_fg="#0f172a"
                )
                self._add(
                    S.label(
                        rel.x,
                        start_y - i * lh,
                        word,
                        font=t.font_name_bold,
                        size=8.0,
                        color=word_color,
                        anchor="middle",
                    )
                )

        # 4. Entities
        for ent in self._entities:
            assert ent.x is not None and ent.y is not None
            ew, eh = self._get_size(ent.name)
            ex = ent.x - ew / 2
            ey = ent.y - eh / 2
            if ent.weak:
                self._add(
                    S.double_border_rect(
                        ex - 3,
                        ey - 3,
                        ew + 6,
                        eh + 6,
                        fill=t.weak_entity_fill,
                        stroke=t.weak_entity_stroke,
                    )
                )
            self._add(
                S.plain_rect(
                    ex,
                    ey,
                    ew,
                    eh,
                    fill=t.entity_fill,
                    stroke=t.entity_stroke,
                )
            )
            entity_color = S.get_contrast_color(
                t.entity_fill, light_fg=t.entity_text, dark_fg="#0f172a"
            )
            self._add(
                S.label(
                    ent.x,
                    ent.y - 4.0,
                    ent.name,
                    font=t.font_name_bold,
                    size=9.0,
                    color=entity_color,
                    anchor="middle",
                )
            )

        # 5. Attributes (drawn last, on top)
        for attr in self._attributes:
            assert attr.x is not None and attr.y is not None
            ax, ay = attr.x, attr.y
            aw, ah = self._get_size(attr.name)
            rx = aw / 2
            ry = ah / 2
            if attr.multivalued:
                self._add(
                    S.double_oval(
                        ax,
                        ay,
                        rx,
                        ry,
                        fill=t.multi_fill,
                        stroke=t.multi_stroke,
                    )
                )
            elif attr.derived:
                self._add(
                    S.oval(
                        ax,
                        ay,
                        rx,
                        ry,
                        fill=t.derived_fill,
                        stroke=t.derived_stroke,
                        dashed=True,
                    )
                )
            elif attr.pk:
                self._add(
                    S.oval(
                        ax,
                        ay,
                        rx,
                        ry,
                        fill=t.pk_fill,
                        stroke=t.pk_stroke,
                    )
                )
            else:
                self._add(
                    S.oval(
                        ax,
                        ay,
                        rx,
                        ry,
                        fill=t.attr_fill,
                        stroke=t.attr_stroke,
                    )
                )

            # Label
            if attr.pk:
                pk_text_color = S.get_contrast_color(
                    t.pk_fill, light_fg=t.pk_text, dark_fg="#0f172a"
                )
                self._add(
                    S.underlined_label(
                        ax,
                        ay - 3.5,
                        attr.name,
                        font=t.font_name_bold,
                        size=8.0,
                        color=pk_text_color,
                    )
                )
            elif attr.derived:
                derived_text_color = S.get_contrast_color(
                    t.derived_fill, light_fg=t.derived_stroke, dark_fg="#0f172a"
                )
                self._add(
                    S.label(
                        ax,
                        ay - 3.5,
                        attr.name,
                        font=t.font_name_italic,
                        size=8.0,
                        color=derived_text_color,
                        anchor="middle",
                    )
                )
            else:
                fill_color = t.multi_fill if attr.multivalued else t.attr_fill
                theme_text_color = t.multi_stroke if attr.multivalued else t.attr_text
                attr_text_color = S.get_contrast_color(
                    fill_color, light_fg=theme_text_color, dark_fg="#0f172a"
                )
                self._add(
                    S.label(
                        ax,
                        ay - 3.5,
                        attr.name,
                        font=t.font_name,
                        size=8.0,
                        color=attr_text_color,
                        anchor="middle",
                    )
                )

        # 6. Cardinality badges drawn last (on top of everything)
        for b in badges_to_draw:
            self._add(b)
