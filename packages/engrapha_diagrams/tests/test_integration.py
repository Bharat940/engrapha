"""
test_integration.py -- Integration tests that generate real PDF output.

These tests verify the full pipeline: diagram builder -> Drawing -> Flowable -> PDF bytes.
All output is written to BytesIO (no files on disk).
"""

from __future__ import annotations

from io import BytesIO

from reportlab.lib.pagesizes import A4
from reportlab.platypus import Flowable, SimpleDocTemplate

import engrapha_diagrams as ed


def _render_to_bytes(*flowable_lists: list[Flowable]) -> bytes:
    """Build a PDF from one or more as_flowable() results and return the raw bytes."""
    buf = BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=A4)
    story: list[Flowable] = []
    for fl in flowable_lists:
        story.extend(fl)
    doc.build(story)
    buf.seek(0)
    return buf.read()


class TestPDFOutput:
    def test_er_diagram_produces_pdf(self) -> None:
        er = ed.ERDiagram(width=450, height=220, caption="ER Integration Test")
        er.entity("STUDENT", x=80, y=110)
        er.entity("COURSE", x=370, y=110)
        er.relationship("ENROLLS", x=225, y=110)
        er.attribute("Student_ID", parent="STUDENT", x=80, y=170, pk=True)
        er.connect("STUDENT", "ENROLLS", card_from="M", card_to="N", total_from=True)
        er.connect("ENROLLS", "COURSE", card_from="N", card_to="1")
        data = _render_to_bytes(er.as_flowable())
        assert data[:4] == b"%PDF"
        assert len(data) > 1000

    def test_flowchart_produces_pdf(self) -> None:
        fc = ed.Flowchart(width=300, height=280)
        fc.terminal("s", "START", x=150, y=250)
        fc.process("p", "Process", x=150, y=190)
        fc.decision("d", "Done?", x=150, y=130)
        fc.terminal("e", "END", x=150, y=60)
        fc.edge("s", "p")
        fc.edge("p", "d")
        fc.edge("d", "e", branch="yes")
        fc.edge("d", "p", branch="no")
        data = _render_to_bytes(fc.as_flowable())
        assert data[:4] == b"%PDF"

    def test_network_star_produces_pdf(self) -> None:
        net = ed.NetworkDiagram(width=400, height=280)
        net.star_topology("sw", "Switch", ["A", "B", "C", "D"])
        data = _render_to_bytes(net.as_flowable())
        assert data[:4] == b"%PDF"

    def test_sequence_produces_pdf(self) -> None:
        seq = ed.SequenceDiagram(width=400, height=200)
        seq.actor("client", "Client")
        seq.actor("server", "Server")
        seq.message("client", "server", "SYN")
        seq.message("server", "client", "SYN-ACK")
        seq.message("client", "server", "ACK")
        data = _render_to_bytes(seq.as_flowable())
        assert data[:4] == b"%PDF"

    def test_class_diagram_produces_pdf(self) -> None:
        cd = ed.ClassDiagram(width=420, height=220)
        cd.uml_class("Animal", "Animal", x=210, y=160,
                     attributes=["+name: String"],
                     methods=["+speak(): void"])
        cd.uml_class("Dog", "Dog", x=120, y=70)
        cd.relate("Dog", "Animal", kind="inheritance")
        data = _render_to_bytes(cd.as_flowable())
        assert data[:4] == b"%PDF"

    def test_state_machine_produces_pdf(self) -> None:
        sm = ed.StateMachine(width=380, height=180)
        sm.state("q0", "q0", x=60, y=90, initial=True)
        sm.state("q1", "q1", x=190, y=90)
        sm.state("q2", "q2", x=320, y=90, accepting=True)
        sm.transition("q0", "q1", label="a")
        sm.transition("q1", "q2", label="b")
        sm.transition("q1", "q1", label="c")
        data = _render_to_bytes(sm.as_flowable())
        assert data[:4] == b"%PDF"

    def test_timing_diagram_produces_pdf(self) -> None:
        td = ed.TimingDiagram(width=400, height=150)
        td.clock("CLK", period=20.0, cycles=6)
        td.signal("DATA", transitions=[(0, 0), (20, 1), (60, 0), (100, 1)])
        data = _render_to_bytes(td.as_flowable())
        assert data[:4] == b"%PDF"

    def test_layered_stack_produces_pdf(self) -> None:
        ls = ed.LayeredStack(width=300, height=220, caption="OSI Model")
        ls.layer("Application", sublabel="HTTP, FTP, SMTP")
        ls.layer("Transport", sublabel="TCP, UDP")
        ls.layer("Network", sublabel="IP, ICMP")
        ls.layer("Data Link", sublabel="Ethernet")
        ls.layer("Physical", sublabel="Cables")
        data = _render_to_bytes(ls.as_flowable())
        assert data[:4] == b"%PDF"

    def test_all_diagrams_in_one_pdf(self) -> None:
        """All 8 diagram types rendered into a single PDF document."""
        er = ed.ERDiagram(width=400, height=180)
        er.entity("A", x=80, y=90)
        er.entity("B", x=320, y=90)
        er.relationship("R", x=200, y=90)
        er.connect("A", "R")
        er.connect("R", "B")

        fc = ed.Flowchart(width=300, height=200)
        fc.terminal("s", "START", x=150, y=170)
        fc.process("p", "Work", x=150, y=110)
        fc.terminal("e", "END", x=150, y=50)
        fc.edge("s", "p")
        fc.edge("p", "e")

        net = ed.NetworkDiagram(width=400, height=200)
        net.ring_topology(["A", "B", "C", "D"])

        seq = ed.SequenceDiagram(width=350, height=180)
        seq.actor("a", "Alice")
        seq.actor("b", "Bob")
        seq.message("a", "b", "Hello")
        seq.message("b", "a", "Hi")

        cd = ed.ClassDiagram(width=350, height=180)
        cd.uml_class("Base", "Base", x=175, y=130)
        cd.uml_class("Child", "Child", x=175, y=50)
        cd.relate("Child", "Base", kind="inheritance")

        sm = ed.StateMachine(width=350, height=150)
        sm.state("s0", "S0", x=60, y=75, initial=True)
        sm.state("s1", "S1", x=200, y=75)
        sm.state("s2", "S2", x=330, y=75, accepting=True)
        sm.transition("s0", "s1", label="0")
        sm.transition("s1", "s2", label="1")

        td = ed.TimingDiagram(width=350, height=130)
        td.clock("CLK", period=20.0, cycles=5)

        ls = ed.LayeredStack(width=300, height=200)
        ls.layer("Application")
        ls.layer("Transport")
        ls.layer("Network")
        ls.layer("Physical")

        data = _render_to_bytes(
            er.as_flowable(), fc.as_flowable(), net.as_flowable(),
            seq.as_flowable(), cd.as_flowable(), sm.as_flowable(),
            td.as_flowable(), ls.as_flowable(),
        )
        assert data[:4] == b"%PDF"
        assert len(data) > 5000

    def test_light_theme_produces_pdf(self) -> None:
        er = ed.ERDiagram(width=400, height=180, theme=ed.LIGHT)
        er.entity("X", x=100, y=90)
        er.entity("Y", x=300, y=90)
        er.relationship("Z", x=200, y=90)
        er.connect("X", "Z")
        er.connect("Z", "Y")
        data = _render_to_bytes(er.as_flowable())
        assert data[:4] == b"%PDF"
