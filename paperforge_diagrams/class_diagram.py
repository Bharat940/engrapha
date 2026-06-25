"""
class_diagram.py -- UML Class diagram builder.

Supports:
  - Classes with stereotype, attributes, and methods
  - Shorthand string parsing: "+name: String", "-calc(x: int): bool"
  - Relationship kinds: inheritance, realization, composition,
    aggregation, association, dependency
  - Multiplicity labels on relation endpoints
"""

from __future__ import annotations

import re
from typing import Any, Literal

from pydantic import BaseModel, Field, model_validator

from . import shapes as S
from .base import DiagramBase
from .layout import edge_clip_rect, midpoint, auto_layout_graph
from .theme import DiagramTheme

Visibility = Literal["+", "-", "#", "~"]
RelationKind = Literal[
    "inheritance",
    "realization",
    "composition",
    "aggregation",
    "association",
    "dependency",
]

_CLASS_W = 100.0
_HEADER_H = 28.0
_ROW_H = 14.0
_SECTION_PAD = 6.0
_MIN_BODY_H = 16.0

_VIS_PATTERN = re.compile(r"^([+\-#~])\s*(.+)$")


def _parse_member(raw: str) -> tuple[Visibility, str]:
    """Parse a shorthand member string into (visibility, rest). Defaults to '+'."""
    m = _VIS_PATTERN.match(raw.strip())
    if m:
        vis = m.group(1)
        if vis in ("+", "-", "#", "~"):
            return vis, m.group(2)  # type: ignore[return-value]
    return "+", raw.strip()


class _UMLClass(BaseModel):
    id: str
    name: str
    stereotype: str = ""
    attributes: list[str] = Field(default_factory=list)
    methods: list[str] = Field(default_factory=list)
    x: float | None = None
    y: float | None = None
    width: float = 100.0

    @model_validator(mode="after")
    def validate_id(self) -> "_UMLClass":
        if not self.id.strip():
            raise ValueError("Class id must not be empty")
        return self


class _UMLRelation(BaseModel):
    from_id: str
    to_id: str
    kind: RelationKind
    label: str = ""
    from_mult: str = ""
    to_mult: str = ""


class ClassDiagram(DiagramBase):
    """
    UML Class diagram builder.

    Usage::

        cd = ClassDiagram(width=420, height=200, caption="Inheritance Example")
        cd.uml_class("Animal", "Animal", x=210, y=150,
                     attributes=["+name: String", "+age: int"],
                     methods=["+speak(): void"])
        cd.uml_class("Dog", "Dog", x=120, y=60,
                     methods=["+fetch(): void"])
        cd.uml_class("Cat", "Cat", x=300, y=60,
                     methods=["+purr(): void"])
        cd.relate("Dog", "Animal", kind="inheritance")
        cd.relate("Cat", "Animal", kind="inheritance")
        story.extend(cd.as_flowable())
    """

    def __init__(
        self,
        width: float,
        height: float | None = None,
        theme: DiagramTheme | None = None,
        caption: str | None = None,
        class_w: float = _CLASS_W,
    ) -> None:
        super().__init__(width, height if height is not None else 1.0, theme, caption)
        self.class_w = class_w
        self._height_auto = height is None
        self._classes: list[_UMLClass] = []
        self._relations: list[_UMLRelation] = []
        self._class_index: dict[str, _UMLClass] = {}

    def uml_class(
        self,
        id: str,
        name: str,
        x: float | None = None,
        y: float | None = None,
        stereotype: str = "",
        attributes: list[str] | None = None,
        methods: list[str] | None = None,
        width: float | None = None,
    ) -> "ClassDiagram":
        """
        Add a UML class box. x, y is the center of the class.
        attributes and methods accept shorthand strings like '+name: String'.
        """
        if id in self._class_index:
            raise ValueError(f"Duplicate class id: '{id}'")

        if width is None:
            max_chars = len(name)
            if stereotype:
                max_chars = max(max_chars, len(stereotype) + 4)
            for attr in attributes or []:
                max_chars = max(max_chars, len(attr) + 2)
            for meth in methods or []:
                max_chars = max(max_chars, len(meth) + 2)
            # Estimate width: 5.4 points per char + padding
            width = max(self.class_w, max_chars * 5.4 + 18.0)

        cls = _UMLClass(
            id=id,
            name=name,
            x=x,
            y=y,
            stereotype=stereotype,
            attributes=attributes or [],
            methods=methods or [],
            width=width,
        )
        self._classes.append(cls)
        self._class_index[id] = cls
        return self

    def relate(
        self,
        from_id: str,
        to_id: str,
        kind: RelationKind,
        label: str = "",
        from_mult: str = "",
        to_mult: str = "",
    ) -> "ClassDiagram":
        """Add a UML relationship between two classes."""
        for cid in (from_id, to_id):
            if cid not in self._class_index:
                raise ValueError(
                    f"Class id '{cid}' not found. Add class before relating."
                )
        self._relations.append(
            _UMLRelation(
                from_id=from_id,
                to_id=to_id,
                kind=kind,
                label=label,
                from_mult=from_mult,
                to_mult=to_mult,
            )
        )
        return self

    # -- Geometry --

    def _class_header_height(self, cls: _UMLClass) -> float:
        lines_count = len(cls.name.split("\n"))
        if cls.stereotype:
            lines_count += 1
        return max(_HEADER_H, lines_count * 10.0 + 8.0)

    def _class_height(self, cls: _UMLClass) -> float:
        attr_h = max(len(cls.attributes) * _ROW_H + _SECTION_PAD * 2, _MIN_BODY_H)
        meth_h = max(len(cls.methods) * _ROW_H + _SECTION_PAD * 2, _MIN_BODY_H)
        return self._class_header_height(cls) + attr_h + meth_h

    def _draw_class(self, cls: _UMLClass) -> None:
        t = self.theme
        assert cls.x is not None and cls.y is not None
        cw = cls.width
        ch = self._class_height(cls)
        hh = self._class_header_height(cls)
        x = cls.x - cw / 2
        y = cls.y - ch / 2

        # Header section
        self._add(
            S.plain_rect(
                x,
                y + ch - hh,
                cw,
                hh,
                fill=t.class_header_fill,
                stroke=t.class_stroke,
            )
        )
        header_text_color = S.get_contrast_color(
            t.class_header_fill, light_fg=t.class_header_text, dark_fg="#0f172a"
        )
        stereotype_text_color = S.get_contrast_color(
            t.class_header_fill, light_fg=t.stereotype_text, dark_fg="#0f172a"
        )

        lines = []
        is_italic = []
        if cls.stereotype:
            lines.append(f"<<{cls.stereotype}>>")
            is_italic.append(True)
        for part in cls.name.split("\n"):
            lines.append(part)
            is_italic.append(False)

        first_baseline = y + ch - hh / 2 + (len(lines) - 1) * 5.0 - 3.5
        for i, line in enumerate(lines):
            line_y = first_baseline - i * 10.0
            font = t.font_name_italic if is_italic[i] else t.font_name_bold
            color = stereotype_text_color if is_italic[i] else header_text_color
            size = 7.0 if is_italic[i] else 9.0
            self._add(
                S.label(
                    cls.x,
                    line_y,
                    line,
                    font=font,
                    size=size,
                    color=color,
                    anchor="middle",
                )
            )

        # Attribute section
        attr_h = max(len(cls.attributes) * _ROW_H + _SECTION_PAD * 2, _MIN_BODY_H)
        meth_h = max(len(cls.methods) * _ROW_H + _SECTION_PAD * 2, _MIN_BODY_H)
        attr_y = y + meth_h
        self._add(
            S.plain_rect(
                x,
                attr_y,
                cw,
                attr_h,
                fill=t.class_body_fill,
                stroke=t.class_stroke,
                stroke_width=0.7,
            )
        )
        attr_text_color = S.get_contrast_color(
            t.class_body_fill, light_fg=t.class_attr_text, dark_fg="#0f172a"
        )
        for i, raw in enumerate(cls.attributes):
            vis, rest = _parse_member(raw)
            text = f"{vis} {rest}"
            row_y = attr_y + attr_h - _SECTION_PAD - (i + 1) * _ROW_H + _ROW_H * 0.3
            self._add(
                S.label(
                    x + 6,
                    row_y,
                    text,
                    font=t.font_name,
                    size=7.5,
                    color=attr_text_color,
                    anchor="start",
                )
            )

        # Method section
        self._add(
            S.plain_rect(
                x,
                y,
                cw,
                meth_h,
                fill=t.class_body_fill,
                stroke=t.class_stroke,
                stroke_width=0.7,
            )
        )
        method_text_color = S.get_contrast_color(
            t.class_body_fill, light_fg=t.class_method_text, dark_fg="#0f172a"
        )
        for i, raw in enumerate(cls.methods):
            vis, rest = _parse_member(raw)
            is_abstract = False
            if rest.startswith("<<abstract>>"):
                is_abstract = True
                rest = rest.replace("<<abstract>>", "").strip()
            elif rest.startswith("{abstract}"):
                is_abstract = True
                rest = rest.replace("{abstract}", "").strip()

            text = f"{vis} {rest}"
            font = t.font_name_italic if is_abstract else t.font_name
            row_y = y + meth_h - _SECTION_PAD - (i + 1) * _ROW_H + _ROW_H * 0.3
            self._add(
                S.label(
                    x + 6,
                    row_y,
                    text,
                    font=font,
                    size=7.5,
                    color=method_text_color,
                    anchor="start",
                )
            )

    def _draw_relation(self, rel: _UMLRelation) -> None:
        t = self.theme
        fc = self._class_index[rel.from_id]
        tc = self._class_index[rel.to_id]
        assert fc.x is not None and fc.y is not None
        assert tc.x is not None and tc.y is not None
        fch = self._class_height(fc)
        tch = self._class_height(tc)
        x1, y1 = edge_clip_rect(fc.x, fc.y, fc.width, fch, tc.x, tc.y)
        x2, y2 = edge_clip_rect(tc.x, tc.y, tc.width, tch, fc.x, fc.y)
        dx, dy = x2 - x1, y2 - y1
        dashed = rel.kind in ("realization", "dependency")
        color = t.class_stroke
        head_size = 9.0

        # Shorten connection lines so they don't bleed through arrowheads
        ux, uy = S._normalize(dx, dy)
        lx1, ly1 = x1, y1
        lx2, ly2 = x2, y2

        if rel.kind in ("inheritance", "realization", "association", "dependency"):
            lx2 -= ux * head_size
            ly2 -= uy * head_size
        elif rel.kind in ("composition", "aggregation"):
            lx1 += ux * (head_size * 2)
            ly1 += uy * (head_size * 2)

        # Draw line
        if dashed:
            self._add(S.dashed_line(lx1, ly1, lx2, ly2, color=color, width=1.2))
        else:
            self._add(S.solid_line(lx1, ly1, lx2, ly2, color=color, width=1.2))

        # Arrowhead on target/source end
        if rel.kind in ("inheritance", "realization"):
            self._add(_arrowhead_open_triangle(x2, y2, dx, dy, head_size, color))
        elif rel.kind == "composition":
            self._add(S.filled_diamond_head(x1, y1, -dx, -dy, head_size, color))
        elif rel.kind == "aggregation":
            self._add(S.open_diamond_head(x1, y1, -dx, -dy, head_size, color))
        elif rel.kind in ("association", "dependency"):
            self._add(_arrowhead_open_triangle(x2, y2, dx, dy, head_size, color))

        # Multiplicity labels
        mult_text_color = S.get_contrast_color(
            t.bg, light_fg=t.class_attr_text, dark_fg="#0f172a"
        )
        if rel.from_mult:
            mx1, my1 = x1 + dx * 0.14, y1 + dy * 0.14 + 5
            font_size = 7.5
            tw = S.text_width(rel.from_mult, t.font_name, font_size)
            rx, ry = self.get_non_overlapping_position(
                mx1, my1, tw + 4.0, font_size + 2.0
            )
            self._add(
                S.label(
                    rx,
                    ry,
                    rel.from_mult,
                    font=t.font_name,
                    size=font_size,
                    color=mult_text_color,
                    anchor="middle",
                )
            )
        if rel.to_mult:
            mx2, my2 = x2 - dx * 0.14, y2 - dy * 0.14 + 5
            font_size = 7.5
            tw = S.text_width(rel.to_mult, t.font_name, font_size)
            rx, ry = self.get_non_overlapping_position(
                mx2, my2, tw + 4.0, font_size + 2.0
            )
            self._add(
                S.label(
                    rx,
                    ry,
                    rel.to_mult,
                    font=t.font_name,
                    size=font_size,
                    color=mult_text_color,
                    anchor="middle",
                )
            )
        if rel.label:
            mx, my = midpoint(x1, y1, x2, y2)
            font_size = 7.5
            tw = S.text_width(rel.label, t.font_name_italic, font_size)
            rx, ry = self.get_non_overlapping_position(
                mx, my + 6, tw + 4.0, font_size + 2.0
            )
            self._add(
                S.label(
                    rx,
                    ry,
                    rel.label,
                    font=t.font_name_italic,
                    size=font_size,
                    color=mult_text_color,
                    anchor="middle",
                )
            )

    def auto_layout(self) -> None:
        # Build DAG adjacency list and calculate ranks
        adj: dict[str, list[str]] = {c.id: [] for c in self._classes}
        for rel in self._relations:
            if rel.kind in ("inheritance", "realization"):
                adj[rel.to_id].append(rel.from_id)
            else:
                adj[rel.from_id].append(rel.to_id)

        ranks: dict[str, int] = {c.id: 0 for c in self._classes}
        for _ in range(len(self._classes)):
            changed = False
            for u in adj:
                for v in adj[u]:
                    if ranks[v] <= ranks[u]:
                        ranks[v] = ranks[u] + 1
                        changed = True
            if not changed:
                break

        layer_max_h: dict[int, float] = {}
        for c in self._classes:
            r = ranks[c.id]
            ch = self._class_height(c)
            layer_max_h[r] = max(layer_max_h.get(r, 0.0), ch)

        num_layers = len(layer_max_h)
        if num_layers > 1:
            total_class_h = sum(layer_max_h.values())
            min_gap = 35.0
            margin_y = 40.0
            required_h = total_class_h + min_gap * (num_layers - 1) + margin_y * 2
            self.height = max(self.height, required_h)

        # Scale up canvas to prevent overlaps and squishing
        self.width = max(self.width, 750.0)
        self.height = max(self.height, 500.0)
        if hasattr(self, "drawing") and self.drawing:
            self.drawing.width = self.width
            self.drawing.height = self.height

        class_ids = [c.id for c in self._classes]
        edges = []
        for rel in self._relations:
            if rel.kind in ("inheritance", "realization"):
                edges.append((rel.to_id, rel.from_id))
            else:
                edges.append((rel.from_id, rel.to_id))

        coords = auto_layout_graph(class_ids, edges, self.width, self.height)
        for c in self._classes:
            if c.x is None or c.y is None:
                x, y = coords[c.id]
                if c.x is None:
                    c.x = x
                if c.y is None:
                    c.y = y

        self._normalize_bounds()

    def _normalize_bounds(self) -> None:
        # Normalization / Bounding Box adjustment
        min_x, max_x = float("inf"), float("-inf")
        min_y, max_y = float("inf"), float("-inf")
        for c in self._classes:
            assert c.x is not None and c.y is not None
            ch = self._class_height(c)
            min_x = min(min_x, c.x - c.width / 2)
            max_x = max(max_x, c.x + c.width / 2)
            min_y = min(min_y, c.y - ch / 2)
            max_y = max(max_y, c.y + ch / 2)

        margin = 35.0
        calculated_width = max_x - min_x + margin * 2
        calculated_height = max_y - min_y + margin * 2
        final_width = max(self.width, calculated_width)
        extra_x = max(0.0, final_width - calculated_width) / 2.0
        shift_x = margin - min_x + extra_x
        shift_y = margin - min_y
        for c in self._classes:
            assert c.x is not None and c.y is not None
            c.x += shift_x
            c.y += shift_y

        self.width = final_width
        self.height = (
            calculated_height
            if self._height_auto
            else max(self.height, calculated_height)
        )
        if hasattr(self, "drawing") and self.drawing:
            self.drawing.width = self.width
            self.drawing.height = self.height

    def build(self) -> None:
        unspecified = any(c.x is None or c.y is None for c in self._classes)
        if unspecified:
            self.auto_layout()
        else:
            self._normalize_bounds()

        # Register class boxes in self._label_rects
        self._label_rects = []
        for cls in self._classes:
            assert cls.x is not None and cls.y is not None
            ch = self._class_height(cls)
            self._label_rects.append((cls.x, cls.y, cls.width, ch))

        for rel in self._relations:
            self._draw_relation(rel)
        for cls in self._classes:
            self._draw_class(cls)


# ---------------------------------------------------------------------------
# Local helper (open triangle arrowhead for inheritance)
# ---------------------------------------------------------------------------


def _arrowhead_open_triangle(
    tip_x: float,
    tip_y: float,
    dx: float,
    dy: float,
    size: float,
    color: str,
) -> Any:
    from reportlab.graphics.shapes import Polygon

    ux, uy = S._normalize(dx, dy)
    px, py = -uy, ux
    half = size * 0.40
    base_x = tip_x - ux * size
    base_y = tip_y - uy * size
    points = [
        tip_x,
        tip_y,
        base_x + px * half,
        base_y + py * half,
        base_x - px * half,
        base_y - py * half,
    ]
    poly = Polygon(points)
    poly.strokeColor = S._hex(color)
    poly.strokeWidth = 1.1
    poly.fillColor = None
    return poly
