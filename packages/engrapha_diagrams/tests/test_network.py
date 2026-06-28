"""
test_network.py -- Tests for the NetworkDiagram builder.
"""

from __future__ import annotations

import pytest
from reportlab.lib.colors import Color
from reportlab.platypus import Flowable

from engrapha_diagrams.network import NetworkDiagram


class TestNetworkDiagramBuilder:
    def test_node_added(self) -> None:
        net = NetworkDiagram(width=400, height=200)
        net.node("r1", "Router", x=100, y=100, kind="router")
        assert len(net._nodes) == 1
        assert net._nodes[0].kind == "router"

    def test_duplicate_node_raises(self) -> None:
        net = NetworkDiagram(width=400, height=200)
        net.node("n1", "Node", x=100, y=100)
        with pytest.raises(ValueError, match="Duplicate"):
            net.node("n1", "Other", x=200, y=100)

    def test_link_unknown_node_raises(self) -> None:
        net = NetworkDiagram(width=400, height=200)
        net.node("n1", "A", x=100, y=100)
        with pytest.raises(ValueError, match="not found"):
            net.link("n1", "unknown")

    def test_link_added(self) -> None:
        net = NetworkDiagram(width=400, height=200)
        net.node("a", "A", x=80, y=100)
        net.node("b", "B", x=200, y=100)
        net.link("a", "b", label="10Mbps")
        assert len(net._edges) == 1
        assert net._edges[0].label == "10Mbps"

    def test_fluent_api(self) -> None:
        net = NetworkDiagram(width=400, height=200)
        result = net.node("n1", "Node", x=100, y=100)
        assert result is net

    def test_all_node_kinds_accepted(self) -> None:
        kinds = [
            "host",
            "router",
            "switch",
            "hub",
            "server",
            "cloud",
            "database",
            "firewall",
            "wireless",
            "load_balancer",
            "printer",
            "storage",
            "mobile",
            "generic",
        ]
        net = NetworkDiagram(width=900, height=200)
        for i, kind in enumerate(kinds):
            net.node(f"n{i}", kind, x=50 + i * 60, y=100, kind=kind)  # type: ignore[arg-type]
        assert len(net._nodes) == len(kinds)

    def test_long_label_wraps_below_node(self) -> None:
        net = NetworkDiagram(width=400, height=200)
        net.node("lb", "External Application Load Balancer", kind="load_balancer")
        assert len(net._label_lines(net._nodes[0])) > 1

    def test_custom_node_receives_size_and_colors(self) -> None:
        seen: list[tuple[float, float, float, float, Color, Color]] = []

        def draw_custom(
            diagram: NetworkDiagram,
            cx: float,
            cy: float,
            width: float,
            height: float,
            fill: Color,
            stroke: Color,
        ) -> None:
            seen.append((cx, cy, width, height, fill, stroke))

        net = NetworkDiagram(width=300, height=180)
        net.node("custom", "Custom", x=100, y=100, kind="custom", custom_draw=draw_custom)
        net.as_flowable()
        assert seen
        assert seen[0][2:4] == (56.0, 28.0)
        assert isinstance(seen[0][4], Color)


class TestNetworkPresetLayouts:
    def test_star_topology_node_count(self) -> None:
        net = NetworkDiagram(width=400, height=300)
        net.star_topology("sw", "Switch", ["h1", "h2", "h3", "h4"])
        # 1 center + 4 spokes
        assert len(net._nodes) == 5

    def test_star_topology_edge_count(self) -> None:
        net = NetworkDiagram(width=400, height=300)
        net.star_topology("sw", "Switch", ["h1", "h2", "h3"])
        assert len(net._edges) == 3

    def test_ring_topology_node_count(self) -> None:
        net = NetworkDiagram(width=400, height=300)
        net.ring_topology(["A", "B", "C", "D"])
        assert len(net._nodes) == 4

    def test_ring_topology_edge_count(self) -> None:
        net = NetworkDiagram(width=400, height=300)
        net.ring_topology(["A", "B", "C", "D"])
        # Ring: each node connects to next (and last to first)
        assert len(net._edges) == 4

    def test_mesh_topology_edge_count(self) -> None:
        net = NetworkDiagram(width=400, height=300)
        net.mesh_topology(["A", "B", "C", "D"])
        # Full mesh: n*(n-1)/2 = 4*3/2 = 6
        assert len(net._edges) == 6

    def test_tree_topology(self) -> None:
        net = NetworkDiagram(width=400, height=300)
        parent_child = {"root": ["child1", "child2"], "child1": ["leaf1", "leaf2"]}
        net.tree_topology(parent_child)
        assert len(net._nodes) == 5
        assert len(net._edges) == 4

    def test_mismatched_labels_raises(self) -> None:
        net = NetworkDiagram(width=400, height=300)
        with pytest.raises(ValueError, match="same length"):
            net.ring_topology(["A", "B"], labels=["only_one"])

    def test_star_mismatched_labels_raises(self) -> None:
        net = NetworkDiagram(width=400, height=300)
        with pytest.raises(ValueError, match="same length"):
            net.star_topology("sw", "Switch", ["h1", "h2"], spoke_labels=["only"])


class TestNetworkBuild:
    def test_manual_diagram_builds(self) -> None:
        net = NetworkDiagram(width=400, height=200)
        net.node("r", "Router", x=200, y=120, kind="router")
        net.node("h1", "Host A", x=80, y=60, kind="host")
        net.node("h2", "Host B", x=320, y=60, kind="host")
        net.link("r", "h1")
        net.link("r", "h2")
        flowables = net.as_flowable()
        assert len(flowables) > 0

    def test_star_preset_builds(self) -> None:
        net = NetworkDiagram(width=400, height=300)
        net.star_topology("sw", "Switch", ["A", "B", "C"])
        flowables = net.as_flowable()
        assert len(flowables) > 0
        for f in flowables:
            assert isinstance(f, Flowable)

    def test_ring_preset_builds(self) -> None:
        net = NetworkDiagram(width=400, height=300)
        net.ring_topology(["A", "B", "C", "D", "E"])
        flowables = net.as_flowable()
        assert len(flowables) > 0

    def test_mesh_preset_builds(self) -> None:
        net = NetworkDiagram(width=400, height=300)
        net.mesh_topology(["A", "B", "C", "D"])
        flowables = net.as_flowable()
        assert len(flowables) > 0

    def test_auto_layout(self) -> None:
        net = NetworkDiagram(width=400, height=200)
        net.node("r", "Router", kind="router")
        net.node("h1", "Host A", kind="host")
        net.node("h2", "Host B", kind="host")
        net.link("r", "h1")
        net.link("r", "h2")
        for n in net._nodes:
            assert n.x is None
            assert n.y is None
        net.build()
        for n in net._nodes:
            assert n.x is not None
            assert n.y is not None
