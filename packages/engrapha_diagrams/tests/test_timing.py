"""
test_timing.py -- Tests for the TimingDiagram builder.
"""

from __future__ import annotations

import pytest
from reportlab.platypus import Flowable

from engrapha_diagrams.timing import TimingDiagram


class TestTimingDiagramBuilder:
    def test_signal_added(self) -> None:
        td = TimingDiagram(width=400, height=150)
        td.signal("DATA", transitions=[(0, 0), (10, 1), (20, 0)])
        assert len(td._signals) == 1
        assert td._signals[0].name == "DATA"

    def test_signal_invalid_level_raises(self) -> None:
        td = TimingDiagram(width=400, height=150)
        with pytest.raises(Exception, match="0 or 1"):
            td.signal("X", transitions=[(0, 2)])

    def test_signal_empty_transitions_raises(self) -> None:
        td = TimingDiagram(width=400, height=150)
        with pytest.raises(Exception, match="at least one"):
            td.signal("X", transitions=[])

    def test_clock_added(self) -> None:
        td = TimingDiagram(width=400, height=150)
        td.clock("CLK", period=20.0, cycles=4)
        assert len(td._signals) == 1

    def test_clock_invalid_duty_raises(self) -> None:
        td = TimingDiagram(width=400, height=150)
        with pytest.raises(ValueError, match="duty"):
            td.clock("CLK", period=20.0, duty=1.5)

    def test_clock_zero_duty_raises(self) -> None:
        td = TimingDiagram(width=400, height=150)
        with pytest.raises(ValueError, match="duty"):
            td.clock("CLK", period=20.0, duty=0.0)

    def test_clock_invalid_cycles_raises(self) -> None:
        td = TimingDiagram(width=400, height=150)
        with pytest.raises(ValueError, match="cycles"):
            td.clock("CLK", period=20.0, cycles=0)

    def test_fluent_api(self) -> None:
        td = TimingDiagram(width=400, height=150)
        result = td.signal("X", transitions=[(0, 0), (5, 1)])
        assert result is td

    def test_multiple_signals(self) -> None:
        td = TimingDiagram(width=400, height=200)
        td.clock("CLK", period=10.0, cycles=8)
        td.signal("DATA", transitions=[(0, 0), (20, 1), (40, 0)])
        td.signal("OUT", transitions=[(0, 1), (30, 0), (50, 1)])
        assert len(td._signals) == 3


class TestTimingDiagramBuild:
    def test_simple_clock_builds(self) -> None:
        td = TimingDiagram(width=400, height=120, caption="Clock Signal")
        td.clock("CLK", period=20.0, cycles=6)
        flowables = td.as_flowable()
        assert len(flowables) > 0
        for f in flowables:
            assert isinstance(f, Flowable)

    def test_multi_signal_builds(self) -> None:
        td = TimingDiagram(width=400, height=180)
        td.clock("CLK", period=20.0, cycles=8)
        td.signal("DATA", transitions=[(0, 0), (20, 1), (60, 0), (100, 1)])
        td.signal("CS", transitions=[(0, 1), (10, 0), (90, 1)])
        flowables = td.as_flowable()
        assert len(flowables) > 0

    def test_empty_diagram_builds(self) -> None:
        td = TimingDiagram(width=300, height=100)
        flowables = td.as_flowable()
        assert len(flowables) > 0
