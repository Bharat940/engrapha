"""
test_state_machine.py -- Tests for the StateMachine diagram builder.
"""

from __future__ import annotations

import pytest
from reportlab.platypus import Flowable

from engrapha_diagrams.state_machine import StateMachine


class TestStateMachineBuilder:
    def test_state_added(self) -> None:
        sm = StateMachine(width=400, height=200)
        sm.state("q0", "q0", x=60, y=100, initial=True)
        assert len(sm._states) == 1
        assert sm._states[0].initial is True

    def test_accepting_state(self) -> None:
        sm = StateMachine(width=400, height=200)
        sm.state("q2", "q2", x=300, y=100, accepting=True)
        assert sm._states[0].accepting is True

    def test_duplicate_state_raises(self) -> None:
        sm = StateMachine(width=400, height=200)
        sm.state("q0", "q0", x=60, y=100)
        with pytest.raises(ValueError, match="Duplicate"):
            sm.state("q0", "q0_dup", x=200, y=100)

    def test_transition_unknown_from_raises(self) -> None:
        sm = StateMachine(width=400, height=200)
        sm.state("q0", "q0", x=60, y=100)
        with pytest.raises(ValueError, match="not found"):
            sm.transition("unknown", "q0", label="a")

    def test_transition_unknown_to_raises(self) -> None:
        sm = StateMachine(width=400, height=200)
        sm.state("q0", "q0", x=60, y=100)
        with pytest.raises(ValueError, match="not found"):
            sm.transition("q0", "unknown", label="a")

    def test_transition_added(self) -> None:
        sm = StateMachine(width=400, height=200)
        sm.state("q0", "q0", x=60, y=100)
        sm.state("q1", "q1", x=200, y=100)
        sm.transition("q0", "q1", label="a")
        assert len(sm._transitions) == 1
        assert sm._transitions[0].label == "a"

    def test_self_loop_transition(self) -> None:
        sm = StateMachine(width=400, height=200)
        sm.state("q0", "q0", x=100, y=100)
        sm.transition("q0", "q0", label="b")
        assert sm._transitions[0].from_id == sm._transitions[0].to_id

    def test_fluent_api(self) -> None:
        sm = StateMachine(width=400, height=200)
        result = sm.state("q0", "q0", x=60, y=100)
        assert result is sm

    def test_long_state_label_wraps(self) -> None:
        sm = StateMachine(width=400, height=200, state_label_max_width=52)
        sm.state("q0", "Waiting for validated browser environment", x=80, y=100)
        assert len(sm._state_label_lines(sm._states[0])) > 1

    def test_long_transition_label_wraps(self) -> None:
        sm = StateMachine(width=400, height=200, transition_label_max_width=60)
        lines = sm._transition_label_lines("browser returns to applet document")
        assert len(lines) > 1

    def test_empty_id_raises(self) -> None:
        with pytest.raises(Exception):
            StateMachine(width=400, height=200).state("", "q0", x=60, y=100)


class TestStateMachineBuild:
    def test_simple_dfa_builds(self) -> None:
        sm = StateMachine(width=380, height=180, caption="Simple DFA")
        sm.state("q0", "q0", x=60, y=90, initial=True)
        sm.state("q1", "q1", x=190, y=90)
        sm.state("q2", "q2", x=320, y=90, accepting=True)
        sm.transition("q0", "q1", label="a")
        sm.transition("q1", "q2", label="b")
        sm.transition("q1", "q0", label="a")
        sm.transition("q2", "q2", label="a,b")
        flowables = sm.as_flowable()
        assert len(flowables) > 0
        for f in flowables:
            assert isinstance(f, Flowable)

    def test_process_state_diagram_builds(self) -> None:
        sm = StateMachine(width=450, height=200)
        sm.state("new", "New", x=60, y=100, initial=True)
        sm.state("ready", "Ready", x=180, y=100)
        sm.state("running", "Running", x=300, y=100)
        sm.state("terminated", "Terminated", x=420, y=100, accepting=True)
        sm.transition("new", "ready", label="admit")
        sm.transition("ready", "running", label="dispatch")
        sm.transition("running", "ready", label="interrupt")
        sm.transition("running", "terminated", label="exit")
        flowables = sm.as_flowable()
        assert len(flowables) > 0

    def test_no_states_builds_empty(self) -> None:
        sm = StateMachine(width=200, height=100)
        flowables = sm.as_flowable()
        assert len(flowables) > 0

    def test_custom_state_drawer_can_receive_radius(self) -> None:
        seen: list[tuple[float, float, float, str, str]] = []

        def draw_custom(
            diagram: StateMachine,
            cx: float,
            cy: float,
            radius: float,
            fill: str,
            stroke: str,
        ) -> None:
            seen.append((cx, cy, radius, fill, stroke))

        sm = StateMachine(width=300, height=180)
        sm.state("env", "Browser JVM Environment", x=120, y=90, custom_draw=draw_custom)
        sm.as_flowable()
        assert seen
        assert seen[0][2] >= sm.state_r
