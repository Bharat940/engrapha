"""
test_er_diagram.py -- Tests for the ERDiagram builder.
"""

from __future__ import annotations

import pytest
from reportlab.graphics.shapes import Drawing
from reportlab.platypus import Flowable

from engrapha_diagrams.er_diagram import ERDiagram


class TestERDiagramBuilder:
    def test_entity_added(self) -> None:
        er = ERDiagram(width=400, height=200)
        er.entity("STUDENT", x=100, y=100)
        assert len(er._entities) == 1
        assert er._entities[0].name == "STUDENT"

    def test_relationship_added(self) -> None:
        er = ERDiagram(width=400, height=200)
        er.relationship("ENROLLS", x=200, y=100)
        assert len(er._relationships) == 1

    def test_attribute_added(self) -> None:
        er = ERDiagram(width=400, height=200)
        er.entity("STUDENT", x=100, y=100)
        er.attribute("ID", parent="STUDENT", x=50, y=160, pk=True)
        assert len(er._attributes) == 1
        assert er._attributes[0].pk is True

    def test_multiple_attribute_flags_raises(self) -> None:
        er = ERDiagram(width=400, height=200)
        er.entity("E", x=100, y=100)
        with pytest.raises(ValueError, match="only one"):
            er.attribute("X", parent="E", x=50, y=160, pk=True, derived=True)

    def test_connect_unknown_from_raises(self) -> None:
        er = ERDiagram(width=400, height=200)
        er.entity("A", x=50, y=100)
        with pytest.raises(ValueError, match="not found"):
            er.connect("UNKNOWN", "A")

    def test_connect_unknown_to_raises(self) -> None:
        er = ERDiagram(width=400, height=200)
        er.entity("A", x=50, y=100)
        with pytest.raises(ValueError, match="not found"):
            er.connect("A", "UNKNOWN")

    def test_connect_entity_to_relationship(self) -> None:
        er = ERDiagram(width=400, height=200)
        er.entity("STUDENT", x=80, y=100)
        er.relationship("ENROLLS", x=220, y=100)
        er.connect("STUDENT", "ENROLLS", card_from="M", card_to="N")
        assert len(er._connections) == 1

    def test_weak_entity_flag(self) -> None:
        er = ERDiagram(width=400, height=200)
        er.entity("ORDER_ITEM", x=100, y=100, weak=True)
        assert er._entities[0].weak is True

    def test_identifying_relationship_flag(self) -> None:
        er = ERDiagram(width=400, height=200)
        er.relationship("HAS", x=200, y=100, identifying=True)
        assert er._relationships[0].identifying is True

    def test_fluent_api_returns_self(self) -> None:
        er = ERDiagram(width=400, height=200)
        result = er.entity("E", x=100, y=100)
        assert result is er

    def test_empty_entity_name_raises(self) -> None:
        with pytest.raises(Exception):
            ERDiagram(width=400, height=200).entity("", x=100, y=100)

    def test_entity_attributes_layout(self) -> None:
        er = ERDiagram(width=400, height=200)
        er.entity("STUDENT", x=100, y=100)
        er.entity_attributes(
            "STUDENT",
            [
                ("ID", {"pk": True}),
                "Name",
                ("Phone", {"multivalued": True}),
                ("GPA", {"derived": True}),
            ],
            distance=60.0,
        )
        assert len(er._attributes) == 4
        assert er._attributes[0].name == "ID"
        assert er._attributes[0].pk is True
        assert er._attributes[1].name == "Name"
        assert er._attributes[2].name == "Phone"
        assert er._attributes[2].multivalued is True
        assert er._attributes[3].name == "GPA"
        assert er._attributes[3].derived is True


class TestERDiagramBuild:
    def test_build_produces_drawing(self) -> None:
        er = ERDiagram(width=400, height=200)
        er.entity("A", x=100, y=100)
        er.as_flowable()
        assert isinstance(er.drawing, Drawing)

    def test_as_flowable_returns_flowables(self) -> None:
        er = ERDiagram(width=400, height=200)
        er.entity("STUDENT", x=100, y=100)
        flowables = er.as_flowable()
        assert len(flowables) > 0
        for f in flowables:
            assert isinstance(f, Flowable)

    def test_full_er_diagram_builds(self) -> None:
        er = ERDiagram(width=450, height=220)
        er.entity("STUDENT", x=80, y=110)
        er.entity("COURSE", x=370, y=110)
        er.relationship("ENROLLS", x=225, y=110)
        er.attribute("Student_ID", parent="STUDENT", x=80, y=170, pk=True)
        er.attribute("Grade", parent="ENROLLS", x=225, y=55)
        er.attribute("Duration", parent="COURSE", x=370, y=55, derived=True)
        er.attribute("Phones", parent="STUDENT", x=20, y=110, multivalued=True)
        er.connect("STUDENT", "ENROLLS", card_from="M", card_to="N", total_from=True)
        er.connect("ENROLLS", "COURSE", card_from="N", card_to="1")
        flowables = er.as_flowable()
        assert len(flowables) > 0

    def test_caption_included_in_flowables(self) -> None:
        er = ERDiagram(width=300, height=150, caption="Test ER")
        er.entity("E", x=100, y=75)
        flowables = er.as_flowable()
        # KeepTogether wraps both diagram and caption
        assert len(flowables) >= 1
