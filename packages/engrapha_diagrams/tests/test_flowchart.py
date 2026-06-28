"""
test_flowchart.py -- Tests for the Flowchart diagram builder.
"""

from __future__ import annotations

import pytest
from reportlab.platypus import Flowable

from engrapha_diagrams.flowchart import Flowchart


class TestFlowchartBuilder:
    def test_process_added(self) -> None:
        fc = Flowchart(width=300, height=300)
        fc.process("p1", "Step 1", x=150, y=200)
        assert len(fc._nodes) == 1
        assert fc._nodes[0].kind == "process"

    def test_decision_added(self) -> None:
        fc = Flowchart(width=300, height=300)
        fc.decision("d1", "Yes?", x=150, y=150)
        assert fc._nodes[0].kind == "decision"

    def test_terminal_added(self) -> None:
        fc = Flowchart(width=300, height=300)
        fc.terminal("t1", "START", x=150, y=260)
        assert fc._nodes[0].kind == "terminal"

    def test_io_box_added(self) -> None:
        fc = Flowchart(width=300, height=300)
        fc.io_box("io1", "Read x", x=150, y=200)
        assert fc._nodes[0].kind == "io"

    def test_connector_added(self) -> None:
        fc = Flowchart(width=300, height=300)
        fc.connector("c1", "A", x=150, y=200)
        assert fc._nodes[0].kind == "connector"

    def test_predefined_added(self) -> None:
        fc = Flowchart(width=300, height=300)
        fc.predefined("pre1", "Sort()", x=150, y=200)
        assert fc._nodes[0].kind == "predefined"

    def test_duplicate_node_id_raises(self) -> None:
        fc = Flowchart(width=300, height=300)
        fc.process("p1", "Step", x=150, y=200)
        with pytest.raises(ValueError, match="Duplicate"):
            fc.process("p1", "Other", x=150, y=100)

    def test_edge_unknown_from_raises(self) -> None:
        fc = Flowchart(width=300, height=300)
        fc.process("p1", "Step", x=150, y=200)
        with pytest.raises(ValueError, match="not found"):
            fc.edge("unknown", "p1")

    def test_edge_unknown_to_raises(self) -> None:
        fc = Flowchart(width=300, height=300)
        fc.process("p1", "Step", x=150, y=200)
        with pytest.raises(ValueError, match="not found"):
            fc.edge("p1", "unknown")

    def test_edge_with_branch(self) -> None:
        fc = Flowchart(width=300, height=300)
        fc.decision("d1", "Check", x=150, y=200)
        fc.process("p1", "Do it", x=250, y=150)
        fc.edge("d1", "p1", branch="yes")
        assert fc._edges[0].branch == "yes"

    def test_fluent_api(self) -> None:
        fc = Flowchart(width=300, height=300)
        result = fc.process("p1", "Step", x=150, y=200)
        assert result is fc

    def test_empty_id_raises(self) -> None:
        with pytest.raises(Exception):
            Flowchart(width=300, height=300).process("", "Label", x=100, y=100)


class TestFlowchartBuild:
    def test_long_process_label_wraps_and_increases_height(self) -> None:
        fc = Flowchart(width=300, height=300)
        fc.process("p", "Validate all submitted invoice line items before payment", x=150, y=200)
        node = fc._nodes[0]
        width, height = fc._get_size(node)
        assert width < 160
        assert height > 25
        assert len(fc._label_lines(node)) > 1

    def test_decision_edges_clip_to_diamond_border(self) -> None:
        fc = Flowchart(width=300, height=300)
        fc.decision("d", "A == B?", x=100, y=100)
        decision = fc._nodes[0]
        x, y = fc._clip_node(decision, 200, 200)
        width, height = fc._get_size(decision)
        normalized = abs(x - 100) / (width / 2) + abs(y - 100) / (height / 2)
        assert normalized == pytest.approx(1.0)

    def test_simple_flowchart_builds(self) -> None:
        fc = Flowchart(width=300, height=300)
        fc.terminal("start", "START", x=150, y=260)
        fc.process("proc", "Do Work", x=150, y=200)
        fc.decision("dec", "Done?", x=150, y=140)
        fc.terminal("end", "END", x=150, y=60)
        fc.edge("start", "proc")
        fc.edge("proc", "dec")
        fc.edge("dec", "end", branch="yes")
        fc.edge("dec", "proc", branch="no")
        flowables = fc.as_flowable()
        assert len(flowables) > 0
        for f in flowables:
            assert isinstance(f, Flowable)

    def test_all_node_kinds_build(self) -> None:
        fc = Flowchart(width=300, height=400)
        fc.terminal("t", "START", x=150, y=370)
        fc.process("p", "Process", x=150, y=310)
        fc.decision("d", "Check", x=150, y=250)
        fc.io_box("io", "Input", x=150, y=190)
        fc.connector("c", "A", x=150, y=130)
        fc.predefined("pre", "Sort()", x=150, y=70)
        fc.edge("t", "p")
        fc.edge("p", "d")
        fc.edge("d", "io", branch="yes")
        fc.edge("io", "c")
        fc.edge("c", "pre")
        flowables = fc.as_flowable()
        assert len(flowables) > 0
