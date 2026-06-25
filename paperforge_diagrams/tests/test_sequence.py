"""
test_sequence.py -- Tests for the SequenceDiagram builder.
"""

from __future__ import annotations

import pytest
from reportlab.platypus import Flowable

from paperforge_diagrams.sequence import SequenceDiagram


class TestSequenceDiagramBuilder:
    def test_actor_added(self) -> None:
        seq = SequenceDiagram(width=400, height=200)
        seq.actor("client", "Client")
        assert len(seq._actors) == 1
        assert seq._actors[0].label == "Client"

    def test_duplicate_actor_raises(self) -> None:
        seq = SequenceDiagram(width=400, height=200)
        seq.actor("a", "Alice")
        with pytest.raises(ValueError, match="Duplicate"):
            seq.actor("a", "Another")

    def test_message_unknown_actor_raises(self) -> None:
        seq = SequenceDiagram(width=400, height=200)
        seq.actor("a", "Alice")
        with pytest.raises(ValueError, match="not found"):
            seq.message("a", "unknown", "Hi")

    def test_message_added(self) -> None:
        seq = SequenceDiagram(width=400, height=200)
        seq.actor("a", "Alice")
        seq.actor("b", "Bob")
        seq.message("a", "b", "Hello", arrow="solid")
        assert len(seq._events) == 1

    def test_self_message_valid(self) -> None:
        seq = SequenceDiagram(width=400, height=200)
        seq.actor("a", "Alice")
        seq.message("a", "a", "think()")
        assert len(seq._events) == 1

    def test_row_increments(self) -> None:
        seq = SequenceDiagram(width=400, height=200)
        seq.actor("a", "A")
        seq.actor("b", "B")
        seq.message("a", "b", "msg1")
        seq.message("b", "a", "msg2")
        from paperforge_diagrams.sequence import _SeqMessage

        msgs = [e for e in seq._events if isinstance(e, _SeqMessage)]
        assert msgs[0].row == 1
        assert msgs[1].row == 2

    def test_activate_deactivate(self) -> None:
        seq = SequenceDiagram(width=400, height=200)
        seq.actor("s", "Server")
        seq.activate("s")
        seq.deactivate("s")
        assert len(seq._activations) == 1

    def test_deactivate_without_activate_raises(self) -> None:
        seq = SequenceDiagram(width=400, height=200)
        seq.actor("s", "Server")
        with pytest.raises(ValueError, match="No open activation"):
            seq.deactivate("s")

    def test_divider_added(self) -> None:
        seq = SequenceDiagram(width=400, height=200)
        from paperforge_diagrams.sequence import _SeqDivider

        seq.divider("Section Break")
        dividers = [e for e in seq._events if isinstance(e, _SeqDivider)]
        assert len(dividers) == 1

    def test_fluent_api(self) -> None:
        seq = SequenceDiagram(width=400, height=200)
        result = seq.actor("a", "A")
        assert result is seq


class TestSequenceDiagramBuild:
    def test_sequence_grows_to_contain_all_event_rows(self) -> None:
        seq = SequenceDiagram(width=400, height=100)
        seq.actor("a", "A")
        seq.actor("b", "B")
        for index in range(10):
            seq.message("a", "b", f"Message {index}")
        seq.as_flowable()
        assert seq.height > 100
        assert seq._lifeline_bottom() >= 10
        assert seq.drawing.height == seq.height

    def test_tcp_handshake_builds(self) -> None:
        seq = SequenceDiagram(width=400, height=200, caption="TCP 3-Way Handshake")
        seq.actor("client", "Client")
        seq.actor("server", "Server")
        seq.message("client", "server", "SYN")
        seq.message("server", "client", "SYN-ACK")
        seq.message("client", "server", "ACK")
        flowables = seq.as_flowable()
        assert len(flowables) > 0
        for f in flowables:
            assert isinstance(f, Flowable)

    def test_all_arrow_types_build(self) -> None:
        seq = SequenceDiagram(width=400, height=300)
        seq.actor("a", "A")
        seq.actor("b", "B")
        seq.message("a", "b", "solid", arrow="solid")
        seq.message("b", "a", "dashed", arrow="dashed")
        seq.message("a", "b", "solid_open", arrow="solid_open")
        seq.message("b", "a", "dashed_open", arrow="dashed_open")
        flowables = seq.as_flowable()
        assert len(flowables) > 0

    def test_with_divider_builds(self) -> None:
        seq = SequenceDiagram(width=400, height=250)
        seq.actor("a", "A")
        seq.actor("b", "B")
        seq.message("a", "b", "init")
        seq.divider("--- Processing ---")
        seq.message("b", "a", "done")
        flowables = seq.as_flowable()
        assert len(flowables) > 0
