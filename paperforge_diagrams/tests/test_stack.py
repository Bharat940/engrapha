"""
test_stack.py -- Tests for the LayeredStack diagram builder.
"""

from __future__ import annotations

import pytest
from reportlab.platypus import Flowable

from paperforge_diagrams.stack import LayeredStack


class TestLayeredStackBuilder:
    def test_layer_added(self) -> None:
        ls = LayeredStack(width=300, height=200)
        ls.layer("Application")
        assert len(ls._layers) == 1
        assert ls._layers[0].label == "Application"

    def test_sublabel_stored(self) -> None:
        ls = LayeredStack(width=300, height=200)
        ls.layer("Application", sublabel="HTTP, FTP")
        assert ls._layers[0].sublabel == "HTTP, FTP"

    def test_custom_fill_stored(self) -> None:
        ls = LayeredStack(width=300, height=200)
        ls.layer("Layer", fill="#ff0000")
        assert ls._layers[0].fill == "#ff0000"

    def test_divider_without_layer_raises(self) -> None:
        ls = LayeredStack(width=300, height=200)
        with pytest.raises(ValueError, match="layer()"):
            ls.divider()

    def test_divider_marks_layer(self) -> None:
        ls = LayeredStack(width=300, height=200)
        ls.layer("Upper")
        ls.divider()
        assert ls._layers[-1].divider_after is True

    def test_multiple_layers(self) -> None:
        ls = LayeredStack(width=300, height=300)
        for i in range(5):
            ls.layer(f"Layer {i}")
        assert len(ls._layers) == 5

    def test_fluent_api(self) -> None:
        ls = LayeredStack(width=300, height=200)
        result = ls.layer("App")
        assert result is ls

    def test_custom_height_per_layer(self) -> None:
        ls = LayeredStack(width=300, height=200)
        ls.layer("Tall", height=50.0)
        assert ls._layers[0].height == 50.0


class TestLayeredStackBuild:
    def test_osi_model_builds(self) -> None:
        ls = LayeredStack(width=340, height=260, caption="OSI Reference Model")
        ls.layer("Layer 7 - Application", sublabel="HTTP, FTP, SMTP, DNS")
        ls.layer("Layer 6 - Presentation", sublabel="SSL/TLS, JPEG, MPEG")
        ls.layer("Layer 5 - Session", sublabel="NetBIOS, RPC")
        ls.divider()
        ls.layer("Layer 4 - Transport", sublabel="TCP, UDP")
        ls.layer("Layer 3 - Network", sublabel="IP, ICMP, ARP")
        ls.layer("Layer 2 - Data Link", sublabel="Ethernet, PPP, HDLC")
        ls.layer("Layer 1 - Physical", sublabel="Cables, Fiber, Radio")
        flowables = ls.as_flowable()
        assert len(flowables) > 0
        for f in flowables:
            assert isinstance(f, Flowable)

    def test_tcpip_model_builds(self) -> None:
        ls = LayeredStack(width=280, height=180)
        ls.layer("Application", sublabel="HTTP, FTP, DNS, SMTP")
        ls.layer("Transport", sublabel="TCP, UDP")
        ls.layer("Internet", sublabel="IP, ICMP, ARP")
        ls.layer("Network Access", sublabel="Ethernet, Wi-Fi")
        flowables = ls.as_flowable()
        assert len(flowables) > 0

    def test_empty_diagram_builds(self) -> None:
        ls = LayeredStack(width=300, height=200)
        flowables = ls.as_flowable()
        assert len(flowables) > 0

    def test_color_cycles_through_theme(self) -> None:
        from paperforge_diagrams.theme import DARK
        ls = LayeredStack(width=300, height=400, theme=DARK)
        # Add more layers than there are colors to test cycling
        for i in range(len(DARK.stack_colors) + 2):
            ls.layer(f"Layer {i}")
        # Should not raise
        flowables = ls.as_flowable()
        assert len(flowables) > 0
