"""
test_layout.py -- Tests for layout.py geometry helpers.
"""

from __future__ import annotations

import math

import pytest

from paperforge_diagrams.layout import (
    column_positions,
    distribute_around,
    edge_clip_circle,
    edge_clip_rect,
    grid_positions,
    midpoint,
    route_orthogonal,
    row_positions,
    sequence_x_positions,
)


class TestGridPositions:
    def test_single_item(self) -> None:
        pos = grid_positions(1, cols=1, cell_w=100, cell_h=50)
        assert len(pos) == 1
        assert pos[0] == (50.0, 25.0)

    def test_two_cols(self) -> None:
        pos = grid_positions(4, cols=2, cell_w=100, cell_h=50)
        assert len(pos) == 4

    def test_invalid_cols_raises(self) -> None:
        with pytest.raises(ValueError, match="cols"):
            grid_positions(4, cols=0, cell_w=100, cell_h=50)

    def test_count_respected(self) -> None:
        pos = grid_positions(3, cols=5, cell_w=60, cell_h=40)
        assert len(pos) == 3


class TestRowPositions:
    def test_empty(self) -> None:
        pos = row_positions(0, spacing=50)
        assert pos == []

    def test_single(self) -> None:
        pos = row_positions(1, spacing=50, origin_x=100, y=80)
        assert len(pos) == 1
        assert pos[0] == (100.0, 80.0)

    def test_three_evenly_spaced(self) -> None:
        pos = row_positions(3, spacing=60, origin_x=60, y=0)
        xs = [p[0] for p in pos]
        assert xs[1] - xs[0] == pytest.approx(60.0)
        assert xs[2] - xs[1] == pytest.approx(60.0)


class TestColumnPositions:
    def test_empty(self) -> None:
        pos = column_positions(0, spacing=30)
        assert pos == []

    def test_three_items(self) -> None:
        pos = column_positions(3, spacing=40, x=10, origin_y=0)
        ys = [p[1] for p in pos]
        assert ys[1] - ys[0] == pytest.approx(40.0)


class TestDistributeAround:
    def test_four_points_square(self) -> None:
        pos = distribute_around(0, 0, 10, 4, start_angle_deg=90)
        assert len(pos) == 4
        # All points should be at distance 10 from origin
        for x, y in pos:
            assert abs(math.hypot(x, y) - 10) < 1e-6

    def test_empty(self) -> None:
        pos = distribute_around(0, 0, 10, 0)
        assert pos == []


class TestMidpoint:
    def test_basic(self) -> None:
        mx, my = midpoint(0, 0, 100, 100)
        assert mx == 50.0
        assert my == 50.0


class TestRouteOrthogonal:
    def test_horizontal_first(self) -> None:
        pts = route_orthogonal(0, 0, 100, 50, prefer="horizontal")
        assert len(pts) == 4
        assert pts[0] == (0, 0)
        assert pts[-1] == (100, 50)

    def test_vertical_first(self) -> None:
        pts = route_orthogonal(0, 0, 100, 50, prefer="vertical")
        assert len(pts) == 4


class TestEdgeClip:
    def test_clip_rect_right(self) -> None:
        # Source at (0,0), target at (200,0), rect w=60 h=30
        x, y = edge_clip_rect(0, 0, 60, 30, 200, 0)
        assert x == pytest.approx(30.0)  # half-width
        assert y == pytest.approx(0.0)

    def test_clip_circle(self) -> None:
        x, y = edge_clip_circle(0, 0, 20, 100, 0)
        assert x == pytest.approx(20.0)
        assert y == pytest.approx(0.0)

    def test_clip_circle_diagonal(self) -> None:
        x, y = edge_clip_circle(0, 0, 10, 10, 10)
        dist = math.hypot(x, y)
        assert abs(dist - 10) < 1e-5


class TestSequenceXPositions:
    def test_single_actor(self) -> None:
        xs = sequence_x_positions(1, 400)
        assert len(xs) == 1
        assert xs[0] == pytest.approx(200.0)

    def test_two_actors(self) -> None:
        xs = sequence_x_positions(2, 400, margin=50)
        assert len(xs) == 2
        assert xs[0] == pytest.approx(50.0)
        assert xs[1] == pytest.approx(350.0)

    def test_empty(self) -> None:
        xs = sequence_x_positions(0, 400)
        assert xs == []
