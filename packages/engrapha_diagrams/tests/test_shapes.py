"""
test_shapes.py -- Tests for the shapes.py primitive builder functions.
"""

from __future__ import annotations

import math

from reportlab.graphics.shapes import (
    Circle,
    Ellipse,
    Group,
    Line,
    Polygon,
    Rect,
    String,
)

from engrapha_diagrams import shapes as S


class TestBasicShapes:
    def test_rounded_rect_returns_rect(self) -> None:
        r = S.rounded_rect(0, 0, 100, 50)
        assert isinstance(r, Rect)

    def test_rounded_rect_dimensions(self) -> None:
        r = S.rounded_rect(10, 20, 80, 40)
        assert r.x == 10
        assert r.y == 20
        assert r.width == 80
        assert r.height == 40

    def test_plain_rect_no_radius(self) -> None:
        r = S.plain_rect(0, 0, 60, 30)
        assert isinstance(r, Rect)

    def test_diamond_returns_polygon(self) -> None:
        d = S.diamond(50, 50, 40, 20)
        assert isinstance(d, Polygon)

    def test_diamond_has_four_points(self) -> None:
        d = S.diamond(50, 50, 40, 20)
        # Polygon points are a flat list [x0, y0, x1, y1, ...]
        assert len(d.points) == 8  # 4 points * 2 coordinates

    def test_oval_returns_ellipse(self) -> None:
        e = S.oval(50, 50, 30, 15)
        assert isinstance(e, Ellipse)

    def test_oval_dashed(self) -> None:
        e = S.oval(50, 50, 30, 15, dashed=True)
        assert e.strokeDashArray is not None

    def test_oval_not_dashed_by_default(self) -> None:
        e = S.oval(50, 50, 30, 15)
        assert not e.strokeDashArray

    def test_circle_returns_circle(self) -> None:
        c = S.circle(50, 50, 20)
        assert isinstance(c, Circle)

    def test_double_oval_returns_group(self) -> None:
        g = S.double_oval(50, 50, 30, 15)
        assert isinstance(g, Group)

    def test_double_circle_returns_group(self) -> None:
        g = S.double_circle(50, 50, 20)
        assert isinstance(g, Group)

    def test_stadium_returns_rect(self) -> None:
        r = S.stadium(0, 0, 80, 24)
        assert isinstance(r, Rect)
        assert r.rx == 12.0  # h/2

    def test_hexagon_has_six_points(self) -> None:
        h = S.hexagon(50, 50, 20)
        assert isinstance(h, Polygon)
        assert len(h.points) == 12  # 6 points * 2

    def test_octagon_has_eight_points(self) -> None:
        o = S.octagon(50, 50, 20)
        assert isinstance(o, Polygon)
        assert len(o.points) == 16  # 8 points * 2

    def test_parallelogram_has_four_points(self) -> None:
        p = S.parallelogram(0, 0, 80, 30)
        assert isinstance(p, Polygon)
        assert len(p.points) == 8

    def test_cylinder_returns_group(self) -> None:
        g = S.cylinder(0, 0, 60, 40)
        assert isinstance(g, Group)

    def test_cloud_returns_group(self) -> None:
        g = S.cloud(50, 50, 80, 40)
        assert isinstance(g, Group)


class TestLines:
    def test_solid_line_returns_line(self) -> None:
        ln = S.solid_line(0, 0, 100, 100)
        assert isinstance(ln, Line)

    def test_solid_line_endpoints(self) -> None:
        ln = S.solid_line(10, 20, 30, 40)
        assert ln.x1 == 10
        assert ln.y1 == 20
        assert ln.x2 == 30
        assert ln.y2 == 40

    def test_dashed_line_has_dash_array(self) -> None:
        ln = S.dashed_line(0, 0, 100, 0)
        assert ln.strokeDashArray is not None

    def test_double_line_returns_group(self) -> None:
        g = S.double_line(0, 0, 100, 0)
        assert isinstance(g, Group)

    def test_arrow_line_returns_group(self) -> None:
        g = S.arrow_line(0, 0, 100, 0)
        assert isinstance(g, Group)

    def test_arrow_line_no_arrow(self) -> None:
        # Without arrowhead, group should contain just the line
        g = S.arrow_line(0, 0, 100, 0, arrow_end=False, arrow_start=False)
        assert isinstance(g, Group)


class TestLabels:
    def test_label_returns_string(self) -> None:
        s = S.label(50, 50, "Hello")
        assert isinstance(s, String)

    def test_label_text(self) -> None:
        s = S.label(0, 0, "Test")
        assert s.text == "Test"

    def test_label_anchor(self) -> None:
        s = S.label(50, 50, "X", anchor="start")
        assert s.textAnchor == "start"

    def test_multiline_label_returns_group(self) -> None:
        g = S.multiline_label(50, 80, ["Line 1", "Line 2"])
        assert isinstance(g, Group)

    def test_wrap_text_respects_available_width(self) -> None:
        lines = S.wrap_text("Validate a very long user request before processing", 58.0)
        assert len(lines) > 1
        assert all(S.text_width(line) <= 58.0 for line in lines)

    def test_wrap_text_splits_long_token(self) -> None:
        lines = S.wrap_text("ExtremelyLongUnbrokenIdentifierValue", 34.0)
        assert len(lines) > 1
        assert all(S.text_width(line) <= 34.0 for line in lines)

    def test_underlined_label_returns_group(self) -> None:
        g = S.underlined_label(50, 50, "ID")
        assert isinstance(g, Group)

    def test_badge_returns_group(self) -> None:
        g = S.badge(50, 50, "N")
        assert isinstance(g, Group)


class TestHelpers:
    def test_normalize_unit_vector(self) -> None:
        ux, uy = S._normalize(3.0, 4.0)
        assert abs(math.hypot(ux, uy) - 1.0) < 1e-6

    def test_normalize_zero_vector(self) -> None:
        ux, uy = S._normalize(0.0, 0.0)
        assert ux == 1.0
        assert uy == 0.0

    def test_angle_point_right(self) -> None:
        x, y = S._angle_point(0, 0, 10, 0)
        assert abs(x - 10) < 1e-6
        assert abs(y) < 1e-6

    def test_angle_point_top(self) -> None:
        x, y = S._angle_point(0, 0, 10, 90)
        assert abs(x) < 1e-6
        assert abs(y - 10) < 1e-6
