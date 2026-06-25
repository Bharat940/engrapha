"""
test_class_diagram.py -- Tests for the ClassDiagram builder.
"""

from __future__ import annotations

import pytest
from reportlab.platypus import Flowable

from paperforge_diagrams.class_diagram import ClassDiagram, _parse_member


class TestParseMember:
    def test_public_visibility(self) -> None:
        vis, rest = _parse_member("+name: String")
        assert vis == "+"
        assert rest == "name: String"

    def test_private_visibility(self) -> None:
        vis, rest = _parse_member("-secret: int")
        assert vis == "-"

    def test_protected_visibility(self) -> None:
        vis, rest = _parse_member("#helper(): void")
        assert vis == "#"

    def test_package_visibility(self) -> None:
        vis, rest = _parse_member("~internal: bool")
        assert vis == "~"

    def test_no_visibility_defaults_to_public(self) -> None:
        vis, rest = _parse_member("plainMethod()")
        assert vis == "+"
        assert rest == "plainMethod()"

    def test_whitespace_stripped(self) -> None:
        vis, rest = _parse_member("  + name : String  ")
        assert vis == "+"


class TestClassDiagramBuilder:
    def test_class_added(self) -> None:
        cd = ClassDiagram(width=400, height=200)
        cd.uml_class("Animal", "Animal", x=200, y=150)
        assert len(cd._classes) == 1

    def test_duplicate_class_raises(self) -> None:
        cd = ClassDiagram(width=400, height=200)
        cd.uml_class("A", "Animal", x=200, y=150)
        with pytest.raises(ValueError, match="Duplicate"):
            cd.uml_class("A", "Other", x=100, y=100)

    def test_relate_unknown_raises(self) -> None:
        cd = ClassDiagram(width=400, height=200)
        cd.uml_class("A", "Animal", x=200, y=150)
        with pytest.raises(ValueError, match="not found"):
            cd.relate("A", "UNKNOWN", kind="inheritance")

    def test_attributes_stored(self) -> None:
        cd = ClassDiagram(width=400, height=200)
        cd.uml_class(
            "Animal", "Animal", x=200, y=150, attributes=["+name: String", "-age: int"]
        )
        assert len(cd._classes[0].attributes) == 2

    def test_methods_stored(self) -> None:
        cd = ClassDiagram(width=400, height=200)
        cd.uml_class("Animal", "Animal", x=200, y=150, methods=["+ speak(): void"])
        assert len(cd._classes[0].methods) == 1

    def test_stereotype_stored(self) -> None:
        cd = ClassDiagram(width=400, height=200)
        cd.uml_class("Shape", "Shape", x=200, y=150, stereotype="abstract")
        assert cd._classes[0].stereotype == "abstract"

    def test_all_relation_kinds_accepted(self) -> None:
        kinds = [
            "inheritance",
            "realization",
            "composition",
            "aggregation",
            "association",
            "dependency",
        ]
        cd = ClassDiagram(width=500, height=300)
        cd.uml_class("A", "A", x=100, y=200)
        cd.uml_class("B", "B", x=300, y=200)
        for i, kind in enumerate(kinds):
            cd.uml_class(f"C{i}", f"C{i}", x=100 + i * 30, y=100)
            cd.relate("A", f"C{i}", kind=kind)  # type: ignore[arg-type]
        assert len(cd._relations) == len(kinds)

    def test_fluent_api(self) -> None:
        cd = ClassDiagram(width=400, height=200)
        result = cd.uml_class("A", "A", x=100, y=100)
        assert result is cd


class TestClassDiagramBuild:
    def test_simple_hierarchy_builds(self) -> None:
        cd = ClassDiagram(width=420, height=220, caption="Class Diagram")
        cd.uml_class(
            "Animal",
            "Animal",
            x=210,
            y=160,
            attributes=["+name: String"],
            methods=["+speak(): void"],
        )
        cd.uml_class("Dog", "Dog", x=120, y=70, methods=["+fetch(): void"])
        cd.uml_class("Cat", "Cat", x=300, y=70, methods=["+purr(): void"])
        cd.relate("Dog", "Animal", kind="inheritance")
        cd.relate("Cat", "Animal", kind="inheritance")
        flowables = cd.as_flowable()
        assert len(flowables) > 0
        for f in flowables:
            assert isinstance(f, Flowable)

    def test_multiplicity_stored(self) -> None:
        cd = ClassDiagram(width=400, height=200)
        cd.uml_class("A", "A", x=100, y=100)
        cd.uml_class("B", "B", x=300, y=100)
        cd.relate("A", "B", kind="association", from_mult="1", to_mult="*")
        assert cd._relations[0].from_mult == "1"
        assert cd._relations[0].to_mult == "*"

    def test_empty_diagram_builds(self) -> None:
        cd = ClassDiagram(width=300, height=150)
        flowables = cd.as_flowable()
        assert len(flowables) > 0

    def test_auto_height_builds(self) -> None:
        cd = ClassDiagram(width=420, height=None, caption="Auto height")
        cd.uml_class("Base", "Base", attributes=["+id: int"], methods=["+save(): void"])
        cd.uml_class("Child", "Child", methods=["+render(): void"])
        cd.relate("Child", "Base", kind="inheritance")
        flowables = cd.as_flowable()
        assert len(flowables) > 0
        assert cd.height > 1.0
