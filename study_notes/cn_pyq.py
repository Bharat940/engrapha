"""
Computer Networks IT-411/IT503 -- Previous Year Questions & Answers
UIT-RGPV (Autonomous) Bhopal | Semester IV/V
MST-2 | MST-3 | May-June 2024 | Dec 2024
Run: python cn_pyq.py
Output: CN_PYQ_Answers.pdf
"""

from __future__ import annotations


from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.platypus import (
    Paragraph,
    Table,
    TableStyle,
)

import engrapha_diagrams as ed

PAGE_W, PAGE_H = A4
PM = 1.8 * cm
CW = PAGE_W - 2 * PM
print(f"Page size: {PAGE_W} x {PAGE_H} points, Content width: {CW} points")

# -- Color palette & Theme configuration ---------------------------------------
import sys
import engrapha_notes as en

# Parse command line theme selection
theme_name = "dark"
for arg in sys.argv[1:]:
    if arg.startswith("--theme="):
        theme_name = arg.split("=")[1].lower()
    elif arg == "--light":
        theme_name = "light"

theme_map = {
    "dark": en.DARK,
    "light": en.LIGHT,
    "ocean_dark": en.OCEAN_DARK,
    "forest_dark": en.FOREST_DARK,
    "sunset_dark": en.SUNSET_DARK,
    "midnight_dark": en.MIDNIGHT_DARK,
    "ocean_light": en.OCEAN_LIGHT,
    "sepia": en.SEPIA,
}

active_theme = theme_map.get(theme_name, en.DARK)
en.set_theme(active_theme)
print(f"Using theme: {active_theme.name}")

# Import styles and helpers from engrapha_notes
from engrapha_notes import (
    COVER_H1, COVER_H2, COVER_SUB,
    add, sp, rule, br,
    part_box, chap_box, section, subsection,
    body, definition, highlight, tip, note,
    bullet, code_block, info_table,
    frame_format, packet_format,
    CW, PM, PAGE_W, PAGE_H,
    story,
    build_doc,
)


# =============================================================================
#  COVER PAGE
# =============================================================================

sp(24)
t = Table(
    [
        [Paragraph("COMPUTER NETWORKS", COVER_H1)],
        [Paragraph("IT-411 / IT503", COVER_H2)],
    ],
    colWidths=[CW],
)
t.setStyle(
    TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, -1), active_theme.rl(active_theme.surface)),
            ("TOPPADDING", (0, 0), (-1, -1), 24),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 24),
            ("LEFTPADDING", (0, 0), (-1, -1), 20),
            ("RIGHTPADDING", (0, 0), (-1, -1), 20),
            ("BOX", (0, 0), (-1, -1), 2, active_theme.rl(active_theme.accent)),
        ]
    )
)
add(t)
sp(14)
add(Paragraph("Previous Year Questions and Answers", COVER_H2))
add(Paragraph("MST-2  |  MST-3  |  May-June 2024  |  Dec 2024  |  May-June 2025", COVER_SUB))
add(Paragraph("UIT-RGPV (Autonomous) Bhopal  |  Semester IV/V", COVER_SUB))
sp(10)
rule(active_theme.rl(active_theme.accent), 1.5)
sp(8)

info_table(
    ["Section", "Coverage"],
    [
        [
            "Section 1: MST-3 (10 marks)",
            "Internetworking devices, QoS, IntServ/DiffServ, Process-to-process delivery, Congestion control, UDP/TCP headers",
        ],
        [
            "Section 2: MST-2",
            "PDU, X.25, OSI layers, TCP/IP, Switching, ARQ protocols, HDLC, Sliding window, LAP",
        ],
        [
            "Section 3: May-June 2024 ESE",
            "OSI/TCP-IP models, Error detection, MAC protocols, ALOHA, IEEE 802.4/802.5, Routing, IPv4/IPv6, QoS",
        ],
        [
            "Section 4: Dec 2024 ESE",
            "Topologies, X.25, ARPANET, Sliding window, ALOHA, Token Ring, Dijkstra, IP addressing, TCP sequence numbers",
        ],
        [
            "Section 5: May-June 2025 ESE",
            "Types of networks, DLL flow/error control, Channel allocation, Unicast/Multicast, Dijkstra, Class A IP addressing, QoS",
        ],
        [
            "Section 6: Formula Reference",
            "Key formulas for ALOHA, CRC, Dijkstra, Congestion Control, IP addressing",
        ],
    ],
)
br()


# =============================================================================
#  SECTION 1: MST-3
# =============================================================================
part_box("SECTION 1 -- MST-3 QUESTIONS (10 Marks Each)")

# -----------------------------------------------------------------------------
#  MST-3 Q1: Bridge, Router, Hub, Gateway
# -----------------------------------------------------------------------------
chap_box("MST-3 Q1 [10 Marks]: Differentiate between Bridge, Router, Hub, and Gateway")

section("Overview of Internetworking Devices")
definition(
    "<b>Internetworking devices</b> connect network segments or separate networks together. "
    "They operate at different layers of the OSI model and perform different functions: "
    "hubs blindly broadcast, bridges filter by MAC, routers route by IP, and gateways "
    "perform full protocol translation between incompatible networks."
)

section("Device Comparison Table")
info_table(
    ["Device", "OSI Layer", "Function", "Filtering", "Example"],
    [
        [
            "Hub",
            "Layer 1 (Physical)",
            "Broadcasts all signals to all ports. No intelligence -- simply regenerates electrical signals.",
            "None -- all frames forwarded to all ports",
            "10/100 Mbps Ethernet hub",
        ],
        [
            "Bridge",
            "Layer 2 (Data Link)",
            "Filters and forwards frames based on MAC address. Segments a LAN into collision domains.",
            "Filters by MAC address using a forwarding table",
            "IEEE 802.1D transparent bridge",
        ],
        [
            "Router",
            "Layer 3 (Network)",
            "Routes packets between different networks using IP addresses and a routing table.",
            "Routes by IP address -- connects different subnets/networks",
            "Cisco router, home broadband router",
        ],
        [
            "Gateway",
            "Layer 4-7 (Transport to Application)",
            "Full protocol translation between incompatible networks or protocols (e.g., TCP/IP to SNA).",
            "Protocol conversion -- translates between incompatible formats",
            "Email relay gateway, VoIP gateway, IBM SNA gateway",
        ],
    ],
)

section("Key Differences")
bullet(
    [
        "<b>Hub (L1):</b> Dumb device -- no filtering. Creates one large collision domain. Signal regeneration only.",
        "<b>Bridge (L2):</b> Learns MAC addresses. Reduces collision domains. Cannot separate broadcast domains.",
        "<b>Router (L3):</b> Separates both collision and broadcast domains. Connects different network addresses. Requires routing tables.",
        "<b>Gateway (L4-L7):</b> Most intelligent device. Can translate between entirely different protocols (not just different LANs).",
        "Hub and bridge work at physical/data-link level -- protocol independent.",
        "Router is protocol dependent at L3 but protocol independent at L2.",
        "Gateway is fully application-aware and protocol-specific.",
    ]
)

section("Network Topology Diagram")
net = ed.NetworkDiagram(
    width=CW, height=200, caption="Fig 1.1: Hub -> Switch -> Router -> Gateway topology"
)
net.node("h1", "PC-A", x=35, y=145, kind="host")
net.node("h2", "PC-B", x=35, y=55, kind="host")
net.node("hub", "Hub (L1)", x=115, y=100, kind="hub")
net.node("sw", "Switch/Bridge (L2)", x=205, y=100, kind="switch")
net.node("rtr", "Router (L3)", x=295, y=100, kind="router")
net.node("gw", "Gateway (L4-L7)", x=385, y=100, kind="server")
net.node("wan", "WAN/Internet", x=455, y=100, kind="cloud")
net.link("h1", "hub")
net.link("h2", "hub")
net.link("hub", "sw", label="Segments")
net.link("sw", "rtr", label="Routes")
net.link("rtr", "gw", label="Protocol translate")
net.link("gw", "wan")
story.extend(net.as_flowable())

tip(
    "OSI layers for devices: Hub=L1, Bridge/Switch=L2, Router=L3, Gateway=L4-L7. "
    "Hub: single collision domain. Bridge: multiple collision domains, one broadcast domain. "
    "Router: separates broadcast domains. Gateway: protocol translation."
)
br()

# -----------------------------------------------------------------------------
#  MST-3 Q2: IntServ, DiffServ, QoS
# -----------------------------------------------------------------------------
chap_box("MST-3 Q2 [10 Marks]: Integrated Services, Differentiated Services, and QoS")

section("Quality of Service (QoS)")
definition(
    "<b>Quality of Service (QoS):</b> A set of technologies and mechanisms that manage "
    "network traffic to ensure that high-priority or time-sensitive applications receive "
    "the network resources they require. QoS prioritizes certain types of traffic over others "
    "to meet performance guarantees for bandwidth, delay, jitter, and packet loss."
)

section("QoS Parameters")
info_table(
    ["QoS Parameter", "Definition", "Critical For"],
    [
        [
            "Bandwidth",
            "Maximum data rate a flow can use (bps)",
            "Video streaming, file transfer",
        ],
        [
            "Delay (Latency)",
            "Time for packet to travel from source to destination",
            "VoIP, interactive gaming, video conferencing",
        ],
        [
            "Jitter",
            "Variation in packet delay (delay variance)",
            "VoIP, real-time audio/video -- causes choppy audio",
        ],
        [
            "Packet Loss",
            "Percentage of packets dropped during transmission",
            "All applications -- TCP retransmits, UDP drops",
        ],
        [
            "Availability",
            "Percentage of time the network is operational",
            "Mission-critical, financial applications",
        ],
    ],
)

section("Integrated Services (IntServ)")
definition(
    "<b>IntServ (Integrated Services):</b> A per-flow, connection-oriented QoS architecture "
    "that uses the <b>RSVP (Resource Reservation Protocol)</b> to reserve resources along "
    "the entire path from source to destination before data flows. Each router maintains "
    "per-flow state information. Defined in RFC 1633."
)
bullet(
    [
        "<b>Approach:</b> Flow-based resource reservation using RSVP signalling before data transmission.",
        "<b>Granularity:</b> Per-flow -- every individual flow gets dedicated bandwidth.",
        "<b>Guarantee:</b> Hard guarantees -- guaranteed bandwidth, bounded delay.",
        "<b>Scalability:</b> Poor -- routers must maintain state for every flow. Not scalable for the Internet.",
        "<b>Use case:</b> ATM networks, controlled enterprise environments.",
    ]
)

section("Differentiated Services (DiffServ)")
definition(
    "<b>DiffServ (Differentiated Services):</b> A scalable, class-based QoS architecture "
    "that marks packets with a <b>DSCP (Differentiated Services Code Point)</b> value "
    "in the IP header. Routers classify and handle packets based on their DSCP class -- "
    "no per-flow state is required. Defined in RFC 2474/2475."
)
bullet(
    [
        "<b>Approach:</b> Packets are marked at the network edge with a DSCP value (6 bits).",
        "<b>Granularity:</b> Per-class -- all packets of the same class treated equally.",
        "<b>Guarantee:</b> Relative guarantees -- higher-priority classes get better service.",
        "<b>Scalability:</b> Excellent -- no per-flow state. Scales to the Internet.",
        "<b>Use case:</b> Enterprise networks, Internet service providers.",
    ]
)

tip(
    "DSCP Values: EF (Expedited Forwarding) = 46 (decimal) = 101110 (binary) -- for VoIP. "
    "AF (Assured Forwarding) classes: AF11=10, AF12=12, AF13=14, AF21=18, AF22=20, AF23=22, "
    "AF31=26, AF32=28, AF33=30, AF41=34, AF42=36, AF43=38. "
    "BE (Best Effort) = 0. CS classes: CS1=8 through CS7=56."
)

section("IntServ vs DiffServ Comparison")
info_table(
    ["Feature", "IntServ", "DiffServ"],
    [
        ["Granularity", "Per-flow", "Per-class"],
        [
            "Signalling Protocol",
            "RSVP (Resource Reservation Protocol)",
            "None -- edge marking only",
        ],
        ["Router State", "Per-flow state at every router", "No per-flow state"],
        [
            "Guarantee Type",
            "Hard guarantee (bounded delay, reserved BW)",
            "Relative/soft guarantee",
        ],
        [
            "Scalability",
            "Poor -- not Internet-scalable",
            "Excellent -- Internet-scalable",
        ],
        [
            "Setup Required",
            "Yes -- RSVP PATH/RESV messages before flow",
            "No -- packet marking only",
        ],
        ["RFC", "RFC 1633", "RFC 2474/2475"],
        [
            "Use Case",
            "Real-time multimedia in controlled networks",
            "ISP backbone, enterprise QoS",
        ],
    ],
)
br()

# -----------------------------------------------------------------------------
#  MST-3 Q3: Process-to-Process Delivery + Congestion Control
# -----------------------------------------------------------------------------
chap_box("MST-3 Q3 [10 Marks]: Process-to-Process Delivery and Congestion Control")

section("Process-to-Process Delivery")
definition(
    "<b>Process-to-Process Delivery:</b> The transport layer delivers data from a specific "
    "application process on the source host to a specific application process on the "
    "destination host. While the network layer handles host-to-host delivery using IP addresses, "
    "the transport layer uses <b>port numbers</b> (16-bit identifiers) to identify specific "
    "processes (applications) on each host."
)
bullet(
    [
        "<b>Socket:</b> Combination of (IP address + Port number) -- uniquely identifies a process on the network.",
        "<b>Multiplexing (at sender):</b> Multiple applications share the same transport layer; segments from different apps are combined.",
        "<b>Demultiplexing (at receiver):</b> Transport layer delivers each incoming segment to the correct application using port numbers.",
        "<b>Well-known ports (0-1023):</b> Assigned by IANA. HTTP=80, HTTPS=443, FTP=21, SMTP=25, DNS=53, SSH=22.",
        "<b>Registered ports (1024-49151):</b> Used by application vendors. MySQL=3306, RDP=3389.",
        "<b>Dynamic/Ephemeral ports (49152-65535):</b> Used temporarily by client applications.",
    ]
)

code_block("""
 PORT NUMBER RANGES:
 =====================================================================
 Range           | Type            | Usage Examples
 ----------------|-----------------|----------------------------------
 0 - 1023        | Well-known      | HTTP=80, FTP=21, SSH=22, DNS=53
 1024 - 49151    | Registered      | MySQL=3306, RDP=3389
 49152 - 65535   | Dynamic/Ephemeral| Client source ports (temporary)

 SOCKET EXAMPLE:
   Server: 192.168.1.10:80   (web server listening on port 80)
   Client: 10.0.0.5:52341    (client ephemeral port)
   Connection identified by: (src_IP, src_port, dst_IP, dst_port, protocol)
""")

section("TCP Congestion Control")
definition(
    "<b>Congestion Control:</b> Mechanisms used by TCP to prevent a sender from "
    "overwhelming the network with more data than it can handle. TCP uses an "
    "end-to-end congestion control algorithm based on the <b>congestion window (cwnd)</b> "
    "to limit the transmission rate."
)
bullet(
    [
        "<b>Slow Start:</b> cwnd begins at 1 MSS, doubles each RTT (exponential growth) until ssthresh is reached.",
        "<b>Congestion Avoidance (AIMD):</b> After ssthresh, cwnd increases by 1 MSS per RTT (linear/additive increase). On loss: multiplicative decrease (halve ssthresh).",
        "<b>Fast Retransmit:</b> On 3 duplicate ACKs, retransmit the missing segment immediately without waiting for timeout.",
        "<b>Fast Recovery:</b> After fast retransmit, enter congestion avoidance (not slow start). ssthresh = cwnd/2, cwnd = ssthresh.",
        "<b>Timeout:</b> On timeout, ssthresh = cwnd/2, cwnd = 1 MSS, restart slow start.",
    ]
)

code_block("""
 TCP CONGESTION WINDOW TRACE EXAMPLE:
 =====================================================================
 RTT | Phase             | cwnd  | Event
 ----|-------------------|-------|-----------------------------------
   1 | Slow Start        |   1   | Initial
   2 | Slow Start        |   2   | cwnd doubles
   3 | Slow Start        |   4   | cwnd doubles
   4 | Slow Start        |   8   | cwnd doubles (ssthresh=16)
   5 | Congestion Avoid  |   9   | +1 per RTT (additive increase)
   6 | Congestion Avoid  |  10   | +1 per RTT
   7 | Congestion Avoid  |  11   | Triple-dup ACK! -> Fast Retransmit
     | Fast Recovery     |   6   | ssthresh=5 (cwnd/2), cwnd=ssthresh+3
   8 | Congestion Avoid  |   6   | Linear increase resumes
   9 | Timeout event!    |   1   | ssthresh=3, cwnd=1, Slow Start restart
  10 | Slow Start        |   2   | cwnd doubles (ssthresh=3)
  11 | Slow Start        |   4   | Reaches ssthresh
  12 | Congestion Avoid  |   5   | +1 linear increase
""")

section("TCP Congestion Control State Machine")
sm = ed.StateMachine(
    width=CW, height=200, caption="Fig 1.2: TCP Congestion Control States"
)
sm.state("ss", "Slow Start", initial=True)
sm.state("ca", "Congestion Avoidance")
sm.state("fr", "Fast Recovery")
sm.transition("ss", "ca", label="cwnd>=ssthresh")
sm.transition("ca", "ss", label="timeout")
sm.transition("ca", "fr", label="3 dup ACKs")
sm.transition("fr", "ca", label="new ACK")
sm.transition("fr", "ss", label="timeout")
story.extend(sm.as_flowable())

tip(
    "Slow start: cwnd doubles per RTT (exponential). Congestion avoidance: cwnd +1 per RTT (linear). "
    "On 3 dup ACKs: fast retransmit + fast recovery (ssthresh=cwnd/2, cwnd=ssthresh). "
    "On timeout: ssthresh=cwnd/2, cwnd=1, restart slow start."
)
br()

# -----------------------------------------------------------------------------
#  MST-3 Q4: UDP Header + TCP Services
# -----------------------------------------------------------------------------
chap_box("MST-3 Q4 [10 Marks]: UDP Header Format and TCP Services")

section("UDP Header Format")
definition(
    "<b>UDP (User Datagram Protocol):</b> A connectionless, unreliable transport layer "
    "protocol. It provides a minimal service model with a fixed 8-byte header. There is "
    "no handshake, no acknowledgement, no sequencing, and no flow or congestion control. "
    "UDP is used when speed is more important than reliability."
)

packet_format(
    "UDP Header (8 bytes total)",
    [
        ("Source Port", 16),
        ("Destination Port", 16),
        ("Length", 16),
        ("Checksum", 16),
    ],
)

bullet(
    [
        "<b>Source Port (16 bits):</b> Port number of the sending application (optional -- can be 0).",
        "<b>Destination Port (16 bits):</b> Port number of the receiving application process.",
        "<b>Length (16 bits):</b> Total length of the UDP datagram (header + data) in bytes. Minimum = 8 bytes (header only).",
        "<b>Checksum (16 bits):</b> Optional error detection covering header + data + pseudo-header. If unused, set to 0.",
        "UDP datagram = UDP Header (8 bytes) + Data payload.",
        "Port range: 0-65535 (16-bit); well-known ports 0-1023.",
    ]
)

section("TCP Services")
definition(
    "<b>TCP (Transmission Control Protocol):</b> A connection-oriented, reliable, "
    "full-duplex transport layer protocol. TCP provides a byte-stream service with "
    "comprehensive error control, flow control, congestion control, and ordered delivery."
)
bullet(
    [
        "<b>1. Reliable Transfer:</b> Guarantees delivery using acknowledgements (ACK) and retransmission on timeout or error.",
        "<b>2. Ordered Delivery:</b> Sequence numbers ensure data is reassembled in the correct order at the receiver.",
        "<b>3. Connection-Oriented:</b> Three-way handshake (SYN, SYN-ACK, ACK) establishes connection before data transfer.",
        "<b>4. Full-Duplex:</b> Simultaneous bidirectional data transfer on a single connection.",
        "<b>5. Flow Control:</b> Sliding window mechanism prevents sender from overwhelming receiver buffer (rwnd).",
        "<b>6. Congestion Control:</b> Slow start, AIMD, fast retransmit -- prevents network congestion.",
        "<b>7. Byte-Stream Service:</b> TCP treats data as a continuous stream of bytes; application message boundaries not preserved.",
    ]
)

section("TCP Header Format")
packet_format(
    "TCP Header (20-60 bytes)",
    [
        ("Source Port", 16),
        ("Destination Port", 16),
        ("Sequence Number", 32),
        ("Acknowledgement Number", 32),
        ("DO", 4),
        ("Rsvd", 4),
        ("CWR", 1),
        ("ECE", 1),
        ("URG", 1),
        ("ACK", 1),
        ("PSH", 1),
        ("RST", 1),
        ("SYN", 1),
        ("FIN", 1),
        ("Window Size", 16),
        ("Checksum", 16),
        ("Urgent Pointer", 16),
        ("Options and Padding", 32),
    ],
)
bullet(
    [
        "<b>Sequence Number (32 bits):</b> Byte position of the first data byte in this segment.",
        "<b>ACK Number (32 bits):</b> Next expected byte from the other side (cumulative ACK).",
        "<b>Data Offset (DO, 4 bits):</b> TCP header length in 32-bit words (min=5 for 20-byte header).",
        "<b>SYN:</b> Synchronize -- used during connection setup (3-way handshake).",
        "<b>ACK:</b> Acknowledgement field is valid.",
        "<b>FIN:</b> Finish -- sender has no more data (connection teardown).",
        "<b>RST:</b> Reset -- abort connection immediately.",
        "<b>Window Size (16 bits):</b> Receive buffer space available (for flow control).",
        "<b>Checksum (16 bits):</b> Error detection over header + data + pseudo-header.",
        "<b>Urgent Pointer (16 bits):</b> Valid when URG flag set; points to urgent data end.",
    ]
)

tip(
    "UDP: 8-byte header, connectionless, no reliability, fast. Used for DNS, VoIP, streaming. "
    "TCP: 20-60 byte header, connection-oriented, reliable, ordered, flow+congestion control. "
    "TCP 3-way handshake: SYN -> SYN-ACK -> ACK. Teardown: FIN -> FIN-ACK -> FIN -> ACK."
)
br()


# =============================================================================
#  SECTION 2: MST-2
# =============================================================================
part_box("SECTION 2 -- MST-2 QUESTIONS")

# -----------------------------------------------------------------------------
#  MST-2 Q1: PDU
# -----------------------------------------------------------------------------
chap_box("MST-2 Q1 [4 Marks]: PDU -- Protocol Data Unit Frame Format")

section("PDU, SDU, and PCI")
definition(
    "<b>PDU (Protocol Data Unit):</b> The unit of data specified by a protocol at a given "
    "layer of the OSI model. At each layer, the PDU consists of the service data unit (SDU) "
    "received from the layer above, plus a protocol control information (PCI) header "
    "(and sometimes a trailer) added by the current layer's protocol."
)
bullet(
    [
        "<b>SDU (Service Data Unit):</b> Data received from the layer above -- the payload to be transmitted.",
        "<b>PCI (Protocol Control Information):</b> Header/trailer added by the current layer (addresses, sequence numbers, error checks).",
        "<b>PDU = PCI (header) + SDU (data from above layer)</b>",
        "PDUs are given different names at each OSI layer to reflect what they contain.",
    ]
)

section("PDU Names at Each OSI Layer")
info_table(
    ["Layer Number", "Layer Name", "PDU Name", "Header Added By"],
    [
        [
            "Layer 7",
            "Application",
            "Data / Message",
            "Application protocols (HTTP, SMTP, FTP)",
        ],
        ["Layer 6", "Presentation", "Data", "Encryption, compression headers"],
        ["Layer 5", "Session", "Data", "Session tokens, synchronization"],
        [
            "Layer 4",
            "Transport",
            "Segment (TCP) / Datagram (UDP)",
            "TCP/UDP header (ports, seq#, ACK#)",
        ],
        ["Layer 3", "Network", "Packet", "IP header (src/dst IP, TTL, protocol)"],
        [
            "Layer 2",
            "Data Link",
            "Frame",
            "MAC header (src/dst MAC, type) + FCS trailer",
        ],
        ["Layer 1", "Physical", "Bits", "No header -- raw electrical/optical signals"],
    ],
)

stack1 = ed.LayeredStack(
    width=CW, height=220, caption="Fig 2.1: PDU names at each OSI layer"
)
stack1.layer(
    "Application / Presentation / Session (L5-L7)", sublabel="PDU: Data / Message"
)
stack1.layer("Transport (L4)", sublabel="PDU: Segment (TCP) or Datagram (UDP)")
stack1.layer("Network (L3)", sublabel="PDU: Packet")
stack1.layer("Data Link (L2)", sublabel="PDU: Frame")
stack1.layer("Physical (L1)", sublabel="PDU: Bits (electrical/optical signals)")
story.extend(stack1.as_flowable())
br()

# -----------------------------------------------------------------------------
#  MST-2 Q2: X.25 and PLP
# -----------------------------------------------------------------------------
chap_box("MST-2 Q2 [4 Marks]: X.25 Layers and PLP Packet Types")

section("X.25 Protocol Architecture")
definition(
    "<b>X.25:</b> An ITU-T standard for packet-switched Wide Area Network (WAN) communication. "
    "Defined in the 1970s, X.25 provides a connection-oriented packet-switching service "
    "using virtual circuits. It uses three protocol layers corresponding roughly to the "
    "lower three OSI layers."
)

stack2 = ed.LayeredStack(
    width=CW, height=175, caption="Fig 2.2: X.25 three-layer architecture"
)
stack2.layer(
    "Packet Layer (PLP -- X.25 Packet Layer Protocol)",
    sublabel="Virtual circuits, packet sequencing, flow control",
)
stack2.layer(
    "Data Link Layer (LAPB -- Link Access Procedure Balanced)",
    sublabel="Frame delimiting, error control, flow control on the link",
)
stack2.layer(
    "Physical Layer (X.21 / EIA-232)",
    sublabel="Physical signalling and bit transmission on the physical medium",
)
story.extend(stack2.as_flowable())

section("PLP Packet Types")
info_table(
    ["Phase", "Packet Type", "Description"],
    [
        [
            "Call Setup",
            "CALL REQUEST",
            "Originating DTE requests virtual circuit to destination",
        ],
        ["Call Setup", "CALL ACCEPTED", "Destination DTE accepts the incoming call"],
        ["Call Setup", "CALL CONNECTED", "Network confirms that call is established"],
        ["Data Transfer", "DATA", "User data packets numbered with sequence numbers"],
        [
            "Data Transfer",
            "RR (Receive Ready)",
            "Ready to receive more data; acknowledges received packets",
        ],
        [
            "Data Transfer",
            "RNR (Receive Not Ready)",
            "Temporarily unable to receive -- flow control pause",
        ],
        [
            "Data Transfer",
            "REJ (Reject)",
            "Reject packet -- request retransmission from sequence number",
        ],
        [
            "Call Clearing",
            "CLEAR REQUEST",
            "DTE or DCE requests to terminate the virtual circuit",
        ],
        [
            "Call Clearing",
            "CLEAR CONFIRMATION",
            "Other side confirms the virtual circuit is cleared",
        ],
        [
            "Reset/Restart",
            "RESET REQUEST",
            "Reset a virtual circuit to initial sequence state",
        ],
        [
            "Reset/Restart",
            "RESTART REQUEST",
            "Restart all virtual circuits (network-level reset)",
        ],
    ],
)
br()

# -----------------------------------------------------------------------------
#  MST-2 Q3: Physical + Data Link Layer Functions
# -----------------------------------------------------------------------------
chap_box("MST-2 Q3 [8 Marks]: Functions of Physical Layer and Data Link Layer")

section("Physical Layer (Layer 1) -- Functions")
definition(
    "<b>Physical Layer (Layer 1):</b> The lowest layer of the OSI model. Responsible for "
    "the actual transmission of raw bits over a physical medium. It defines the electrical, "
    "mechanical, and functional specifications for the physical connection between devices."
)
bullet(
    [
        "<b>Bit Transmission:</b> Transmits raw binary bits (0s and 1s) as electrical, optical, or radio signals over the physical medium.",
        "<b>Encoding/Decoding:</b> Converts bits into signals (NRZ, Manchester, 4B/5B encoding) and vice versa.",
        "<b>Modulation:</b> Encodes digital data onto an analog carrier (AM, FM, PM, QAM for modems).",
        "<b>Physical Media Specification:</b> Defines cable types (coaxial, twisted pair, fiber optic), connectors (RJ-45), and wireless frequencies.",
        "<b>Synchronization:</b> Ensures sender and receiver bit clocks are synchronized for correct bit recovery.",
        "<b>Network Topology:</b> Physical topology -- how devices are physically connected (bus, star, ring, mesh).",
    ]
)

section("Data Link Layer (Layer 2) -- Functions")
definition(
    "<b>Data Link Layer (Layer 2):</b> Provides reliable node-to-node data transfer over "
    "a single physical link. It packages raw bits from the physical layer into <b>frames</b> "
    "and handles error detection, flow control, and access to the shared medium. "
    "Divided into two sublayers: LLC (Logical Link Control) and MAC (Media Access Control)."
)
bullet(
    [
        "<b>Framing:</b> Packages bits from the physical layer into frames with defined start/end boundaries (flags, length fields).",
        "<b>Physical Addressing:</b> Uses MAC addresses (48-bit) in frame headers to identify source and destination nodes on the same network.",
        "<b>Flow Control:</b> Prevents a fast sender from overwhelming a slow receiver (stop-and-wait, sliding window).",
        "<b>Error Control:</b> Detects (CRC, parity) and corrects (ARQ -- Go-Back-N, Selective Repeat) transmission errors.",
        "<b>Access Control (MAC sublayer):</b> Determines which device can use the shared channel at any time (CSMA/CD, token passing, TDMA).",
        "<b>Piggybacking:</b> ACK for received frames is attached (piggybacked) to outgoing data frames to improve efficiency.",
        "<b>LLC sublayer (IEEE 802.2):</b> Provides a uniform interface to the network layer regardless of the underlying MAC technology.",
    ]
)

section("Comparison: Physical vs Data Link Layer")
info_table(
    ["Feature", "Physical Layer (L1)", "Data Link Layer (L2)"],
    [
        ["Primary Unit", "Bit", "Frame"],
        [
            "Addressing",
            "None (uses voltages/frequencies)",
            "MAC address (48-bit hardware address)",
        ],
        [
            "Error Handling",
            "None -- just transmits bits",
            "Error detection (CRC) and ARQ retransmission",
        ],
        ["Flow Control", "None", "Stop-and-wait, sliding window"],
        ["Access Control", "None", "CSMA/CD, Token Passing, TDMA (MAC sublayer)"],
        ["Framing", "No concept of frames", "Defines frame boundaries (flags, length)"],
        [
            "Examples",
            "Ethernet cable, fiber, radio waves",
            "Ethernet (802.3), Wi-Fi (802.11), PPP, HDLC",
        ],
        ["Sublayers", "None", "LLC (802.2) + MAC (802.3/802.11)"],
    ],
)
br()

# -----------------------------------------------------------------------------
#  MST-2 Q4: TCP/IP Architecture
# -----------------------------------------------------------------------------
chap_box("MST-2 Q4 [8 Marks]: TCP/IP Protocol Suite Architecture")

section("TCP/IP Four-Layer Model")
definition(
    "<b>TCP/IP Protocol Suite:</b> The foundational communication protocol stack of the Internet. "
    "Developed by DARPA in the 1970s, it uses a 4-layer model: Application, Transport, Internet, "
    "and Network Access. Unlike OSI (7 layers), TCP/IP merges presentation, session, and application "
    "into a single Application layer."
)

stack3 = ed.LayeredStack(
    width=CW, height=210, caption="Fig 2.3: TCP/IP four-layer architecture"
)
stack3.layer(
    "Application Layer", sublabel="HTTP, HTTPS, FTP, SMTP, DNS, SNMP, SSH, Telnet, DHCP"
)
stack3.layer(
    "Transport Layer",
    sublabel="TCP (reliable, connection-oriented), UDP (unreliable, connectionless), SCTP",
)
stack3.layer("Internet Layer", sublabel="IP (IPv4/IPv6), ICMP, ARP, IGMP, OSPF, BGP")
stack3.layer(
    "Network Access Layer (Link Layer)",
    sublabel="Ethernet (802.3), Wi-Fi (802.11), PPP, Frame Relay, ATM",
)
story.extend(stack3.as_flowable())

section("TCP/IP Layer Details")
info_table(
    ["Layer", "Protocols", "PDU", "Key Functions"],
    [
        [
            "Application",
            "HTTP, FTP, SMTP, DNS, DHCP, SSH, Telnet, SNMP",
            "Message / Data",
            "User-facing services; data formatting, encoding, session management",
        ],
        [
            "Transport",
            "TCP, UDP, SCTP",
            "Segment (TCP) / Datagram (UDP)",
            "Process-to-process delivery, port numbers, reliability (TCP), flow/congestion control",
        ],
        [
            "Internet",
            "IP, ICMP, ARP, IGMP",
            "Packet / Datagram",
            "Host-to-host delivery across networks, logical addressing (IP), routing, fragmentation",
        ],
        [
            "Network Access",
            "Ethernet, Wi-Fi, PPP, Frame Relay",
            "Frame / Bits",
            "Physical addressing (MAC), framing, error detection on single link, media access",
        ],
    ],
)

section("TCP/IP vs OSI Model Comparison")
info_table(
    ["OSI Layer", "OSI Name", "TCP/IP Layer", "TCP/IP Name", "TCP/IP Protocols"],
    [
        ["7", "Application", "4", "Application", "HTTP, FTP, DNS, SMTP, SSH"],
        ["6", "Presentation", "4", "Application", "(merged into Application layer)"],
        ["5", "Session", "4", "Application", "(merged into Application layer)"],
        ["4", "Transport", "3", "Transport", "TCP, UDP, SCTP"],
        ["3", "Network", "2", "Internet", "IP, ICMP, ARP, IGMP"],
        ["2", "Data Link", "1", "Network Access", "Ethernet, Wi-Fi, PPP"],
        ["1", "Physical", "1", "Network Access", "(cables, signals, interfaces)"],
    ],
)
note(
    "See also Section 3, Q1(d) for the full ISO-OSI 7-layer model with detailed functions."
)
br()

# -----------------------------------------------------------------------------
#  MST-2 Q5: Crossbar vs Multistage Switches
# -----------------------------------------------------------------------------
chap_box("MST-2 Q5 [3 Marks]: Crossbar vs Multistage Switches in Circuit Switching")

section("Crossbar Switch")
definition(
    "<b>Crossbar Switch:</b> A switching fabric consisting of an N x N grid of crosspoints "
    "(on/off switches). Each input is connected to each output via a crosspoint. To connect "
    "input i to output j, the crosspoint at position (i,j) is activated. Simple but the "
    "number of crosspoints grows as N^2."
)

section("Multistage Switch")
definition(
    "<b>Multistage Switch:</b> A switching fabric built from multiple stages of smaller "
    "crossbar switches connected together. The Clos network is the classic example: "
    "three stages (input stage, middle stage, output stage). Reduces the number of "
    "crosspoints from O(N^2) to O(N*sqrt(N)) but introduces the possibility of internal blocking."
)

info_table(
    ["Property", "Crossbar Switch", "Multistage Switch"],
    [
        [
            "Crosspoints required",
            "N^2 crosspoints for N inputs/outputs",
            "O(N * sqrt(N)) -- fewer crosspoints",
        ],
        [
            "Blocking",
            "Non-blocking -- any input connects to any free output",
            "May be blocking (Clos can be rearrangeably non-blocking)",
        ],
        [
            "Complexity",
            "Simple control -- activate one crosspoint",
            "Complex control -- path finding through stages required",
        ],
        [
            "Cost",
            "Expensive for large N (quadratic growth)",
            "More economical for large N",
        ],
        [
            "Scalability",
            "Poor -- impractical for large N",
            "Good -- used in telephone exchanges",
        ],
        [
            "Example",
            "Small PBX switches, ATM fabric",
            "Telephone central office, large IP routers",
        ],
    ],
)

section("2x2 Crossbar Grid Diagram")
net2 = ed.NetworkDiagram(
    width=CW, height=180, caption="Fig 2.4: 2x2 Crossbar switch (4 crosspoints)"
)
net2.node("i1", "Input 1", kind="host")
net2.node("i2", "Input 2", kind="host")
net2.node("x11", "CP(1,1)", kind="generic")
net2.node("x12", "CP(1,2)", kind="generic")
net2.node("x21", "CP(2,1)", kind="generic")
net2.node("x22", "CP(2,2)", kind="generic")
net2.node("o1", "Output 1", kind="server")
net2.node("o2", "Output 2", kind="server")
net2.link("i1", "x11")
net2.link("i1", "x12")
net2.link("i2", "x21")
net2.link("i2", "x22")
net2.link("x11", "o1")
net2.link("x21", "o1")
net2.link("x12", "o2")
net2.link("x22", "o2")
story.extend(net2.as_flowable())
br()

# -----------------------------------------------------------------------------
#  MST-2 Q6: Selective Reject ARQ + Go-Back-N
# -----------------------------------------------------------------------------
chap_box("MST-2 Q6 [4 Marks]: Selective Reject ARQ and Go-Back-N ARQ")

section("Go-Back-N ARQ (GBN)")
definition(
    "<b>Go-Back-N ARQ:</b> A sliding window error control protocol where the sender can "
    "have up to <b>N (window size) unacknowledged frames</b> in transit at once. If any "
    "frame is lost or corrupted, the sender must <b>go back and retransmit that frame AND "
    "all subsequent frames</b> -- even those that may have already been received correctly "
    "at the receiver."
)
bullet(
    [
        "Sender window size: up to N frames (N = 2^n - 1 for n-bit sequence numbers).",
        "Receiver window size: 1 -- receiver only accepts frames in order.",
        "Receiver discards out-of-order frames and sends ACK for the last in-order frame.",
        "Simple receiver implementation but wastes bandwidth on retransmission of good frames.",
    ]
)

section("Go-Back-N Sequence Diagram")
seq1 = ed.SequenceDiagram(
    width=CW, height=260, caption="Fig 2.5: Go-Back-N (frame 1 lost, retransmit 1,2,3)"
)
seq1.actor("snd", "Sender")
seq1.actor("rcv", "Receiver")
seq1.message("snd", "rcv", "Frame 0", arrow="solid")
seq1.message("rcv", "snd", "ACK 0", arrow="dashed")
seq1.message("snd", "rcv", "Frame 1 [LOST]", arrow="solid")
seq1.message("snd", "rcv", "Frame 2 (buffered but discarded)", arrow="solid")
seq1.message("snd", "rcv", "Frame 3 (buffered but discarded)", arrow="solid")
seq1.divider("Timeout -- Go-Back-N: retransmit all from frame 1")
seq1.message("snd", "rcv", "Frame 1 (retransmit)", arrow="solid")
seq1.message("rcv", "snd", "ACK 1", arrow="dashed")
seq1.message("snd", "rcv", "Frame 2 (retransmit)", arrow="solid")
seq1.message("rcv", "snd", "ACK 2", arrow="dashed")
seq1.message("snd", "rcv", "Frame 3 (retransmit)", arrow="solid")
seq1.message("rcv", "snd", "ACK 3", arrow="dashed")
story.extend(seq1.as_flowable())

section("Selective Reject (Selective Repeat) ARQ")
definition(
    "<b>Selective Reject ARQ (SR-ARQ):</b> A sliding window protocol where only the "
    "specific lost or corrupted frame is retransmitted. The receiver has a buffer and "
    "can accept and store out-of-order frames. Only the erroneous frame is retransmitted, "
    "making it much more bandwidth-efficient than GBN."
)
bullet(
    [
        "Sender window size: up to N/2 (= 2^(n-1)) for n-bit sequence numbers.",
        "Receiver window size: N/2 -- can buffer out-of-order frames.",
        "Only the specific NAK'd or timed-out frame is retransmitted.",
        "More complex receiver but better throughput on noisy links.",
    ]
)

section("GBN vs SR Comparison")
info_table(
    ["Feature", "Go-Back-N (GBN)", "Selective Reject (SR)"],
    [
        ["Sender Window Size", "Up to 2^n - 1", "Up to 2^(n-1)"],
        ["Receiver Window Size", "1 (in-order only)", "2^(n-1) (out-of-order buffer)"],
        [
            "On Error",
            "Retransmit ALL frames from error frame onwards",
            "Retransmit ONLY the specific error frame",
        ],
        [
            "Receiver Buffer",
            "Not required (discard out-of-order)",
            "Required (buffer out-of-order frames)",
        ],
        [
            "Efficiency",
            "Lower on noisy links (multiple retransmissions)",
            "Higher on noisy links (minimal retransmissions)",
        ],
        [
            "Complexity",
            "Simpler receiver",
            "More complex receiver and buffer management",
        ],
        [
            "Use Case",
            "Low-error links (e.g., fiber)",
            "High-error links (e.g., wireless, satellite)",
        ],
    ],
)
br()

# -----------------------------------------------------------------------------
#  MST-2 Q7: HDLC
# -----------------------------------------------------------------------------
chap_box("MST-2 Q7 [8 Marks]: HDLC -- High-Level Data Link Control")

section("HDLC Overview")
definition(
    "<b>HDLC (High-Level Data Link Control):</b> A bit-oriented, synchronous data link "
    "layer protocol developed by ISO. It supports both point-to-point and multipoint "
    "configurations and provides framing, error control (CRC), flow control (sliding window), "
    "and multiple operational modes. HDLC is the basis for many other protocols (LAPB, LAPD, PPP)."
)

section("HDLC Operational Modes")
info_table(
    ["Mode", "Full Name", "Description", "Used In"],
    [
        [
            "NRM",
            "Normal Response Mode",
            "Secondary station can only transmit when primary grants permission. Primary controls the link.",
            "Legacy mainframe to terminal (master-slave)",
        ],
        [
            "ARM",
            "Asynchronous Response Mode",
            "Secondary station can initiate transmission without explicit permission from primary, but primary still controls link configuration.",
            "Rarely used; some half-duplex WAN links",
        ],
        [
            "ABM",
            "Asynchronous Balanced Mode",
            "Both stations are equal peers (combined stations). Either can initiate transmission at any time. Full-duplex.",
            "LAPB (X.25), LAPD (ISDN), modern WAN links -- most common mode",
        ],
    ],
)

section("HDLC Frame Format")
info_table(
    ["Field", "Size", "Description", "Value/Notes"],
    [
        [
            "Flag",
            "8 bits",
            "Frame delimiter -- marks start and end of frame",
            "01111110 (0x7E) -- always this value",
        ],
        [
            "Address",
            "8 bits (or multiples)",
            "Address of the secondary station",
            "Extended by setting LSB=0 in each byte",
        ],
        [
            "Control",
            "8 or 16 bits",
            "Frame type (I, S, U) and sequence numbers",
            "I-frame=data, S-frame=supervisory, U-frame=unnumbered",
        ],
        [
            "Information",
            "Variable",
            "User data payload (only in I-frames)",
            "Any length; absent in S and U frames",
        ],
        [
            "FCS",
            "16 or 32 bits",
            "Frame Check Sequence -- CRC error detection",
            "CRC-CCITT (16-bit) or CRC-32",
        ],
        [
            "Flag",
            "8 bits",
            "End-of-frame delimiter",
            "01111110 (0x7E) -- same as opening flag",
        ],
    ],
)

section("Bit Stuffing")
definition(
    "<b>Bit Stuffing:</b> A technique used in HDLC to prevent the appearance of the flag "
    "pattern (01111110) inside the data payload. After every five consecutive 1-bits in the "
    "data stream, the transmitter inserts (stuffs) a 0-bit. The receiver removes this extra "
    "0-bit after detecting five consecutive 1s."
)
code_block("""
 BIT STUFFING EXAMPLE:
 =====================================================================
 Original data : 0 1 1 1 1 1 1 0 0 1 1 1 1 1 0
                           ^^^^^           ^^^^^
                      5 ones here!   5 ones here!

 After stuffing: 0 1 1 1 1 1 [0] 1 0 0 1 1 1 1 1 [0] 0
                              ^                   ^
                      Zero stuffed after       Zero stuffed after
                      5 consecutive ones       5 consecutive ones

 At receiver: remove every 0 that follows 5 consecutive 1s
 Result: original data recovered = 0 1 1 1 1 1 1 0 0 1 1 1 1 1 0
""")

section("Piggybacking")
definition(
    "<b>Piggybacking:</b> The technique of combining an acknowledgement (ACK) for received "
    "data frames with an outgoing data frame traveling in the opposite direction. Instead of "
    "sending a separate ACK frame, the ACK is 'piggybacked' in the control field of the next "
    "data frame, improving channel efficiency."
)
tip(
    "HDLC key facts: Flag=01111110, bit stuffing after 5 ones, three modes: NRM/ARM/ABM. "
    "ABM is most common (used in LAPB, LAPD). Control field types: I-frame (data+seq#), "
    "S-frame (RR/RNR/REJ supervisory), U-frame (unnumbered -- setup/disconnect commands)."
)
br()

# -----------------------------------------------------------------------------
#  MST-2 Q8: Sliding Window + Stop-and-Wait + LAP
# -----------------------------------------------------------------------------
chap_box("MST-2 Q8 [8 Marks]: Sliding Window, Stop-and-Wait ARQ, and LAP Types")

section("Sliding Window Protocol")
definition(
    "<b>Sliding Window Protocol:</b> A flow control and error control mechanism that allows "
    "the sender to transmit multiple frames before waiting for an acknowledgement. The "
    "window represents the number of unacknowledged frames that can be in transit. As ACKs "
    "are received, the window 'slides' forward, allowing new frames to be sent."
)
bullet(
    [
        "<b>SND.UNA:</b> Sequence number of the oldest unacknowledged (sent but not ACK'd) frame.",
        "<b>SND.NXT:</b> Sequence number of the next frame to be sent.",
        "<b>SND.WND:</b> Size of the sender's window -- maximum number of unACK'd frames allowed.",
        "<b>RCV.WND:</b> Receiver's window -- how many frames it can accept (buffer space).",
        "Window size determines throughput: Throughput = Window_size x Frame_size / RTT.",
        "For n-bit sequence numbers: GBN window = 2^n - 1; SR window = 2^(n-1).",
    ]
)

section("Sliding Window Flowchart")
fc_sw = ed.Flowchart(
    width=CW, height=320, caption="Fig 2.6: Sliding Window sender logic"
)
fc_sw.terminal("start", "START")
fc_sw.process("init", "Init: SND.UNA=0, SND.NXT=0")
fc_sw.decision("window_ok", "SND.NXT - SND.UNA < SND.WND?")
fc_sw.process("send_frame", "Send frame SND.NXT; SND.NXT++")
fc_sw.decision("ack_recv", "ACK received?")
fc_sw.process("slide", "Slide: SND.UNA = ACK+1")
fc_sw.decision("timeout", "Timeout / Error?")
fc_sw.process("retrans", "Retransmit from SND.UNA")
fc_sw.terminal("done", "All frames ACK'd -- END")
fc_sw.edge("start", "init")
fc_sw.edge("init", "window_ok")
fc_sw.edge("window_ok", "send_frame", branch="yes")
fc_sw.edge("window_ok", "ack_recv", branch="no")
fc_sw.edge("send_frame", "ack_recv")
fc_sw.edge("ack_recv", "slide", branch="yes")
fc_sw.edge("slide", "done")
fc_sw.edge("ack_recv", "timeout", branch="no")
fc_sw.edge("timeout", "retrans", branch="yes")
fc_sw.edge("retrans", "window_ok")
fc_sw.edge("timeout", "window_ok", branch="no")
story.extend(fc_sw.as_flowable())

section("Stop-and-Wait ARQ")
definition(
    "<b>Stop-and-Wait ARQ (Automatic Repeat reQuest):</b> The simplest ARQ protocol. "
    "The sender transmits one frame and then stops, waiting for an acknowledgement (ACK) "
    "before sending the next frame. If a timeout occurs (no ACK received), the frame is "
    "retransmitted. Window size = 1."
)
code_block("""
 STOP-AND-WAIT ARQ EXAMPLE:
 =====================================================================
 Sender                              Receiver
   |--- Frame 0 ------------------>  |
   |<-- ACK 0 -----------------------|
   |--- Frame 1 ------------------>  |  (Frame 1 lost!)
   |    [TIMEOUT -- no ACK]          |
   |--- Frame 1 (retransmit) ----->  |
   |<-- ACK 1 -----------------------|
   |--- Frame 2 ------------------>  |
   |<-- ACK 2 -----------------------|

 Efficiency = T_frame / (T_frame + 2*T_prop) = 1 / (1 + 2a)
 where a = T_propagation / T_frame (propagation-transmission ratio)
 For long-distance high-speed links, a >> 1, making SAW very inefficient.
""")

section("LAP -- Link Access Procedure Types")
info_table(
    ["LAP Type", "Full Name", "Standard", "Used In", "Mode"],
    [
        [
            "LAPB",
            "Link Access Procedure, Balanced",
            "ITU-T X.25",
            "X.25 packet-switched WAN links (point-to-point)",
            "ABM -- balanced mode (peer stations)",
        ],
        [
            "LAPD",
            "Link Access Procedure, D-channel",
            "ITU-T Q.921",
            "ISDN D-channel (signalling channel for call setup)",
            "ABM -- used for ISDN signalling",
        ],
        [
            "LAPM",
            "Link Access Procedure, Modems",
            "ITU-T V.42",
            "Dial-up modems (V.34, V.90) for error correction",
            "ABM -- modem-to-modem error control",
        ],
        [
            "LAPF",
            "Link Access Procedure, Frame Mode",
            "ITU-T Q.922",
            "Frame Relay networks -- simplified LAPD",
            "Connection-oriented frame relay",
        ],
    ],
)

tip(
    "Stop-and-Wait efficiency = 1/(1+2a). Sliding window improves efficiency: W/(1+2a) for W = window size. "
    "For full utilization: W >= 1 + 2a. LAP types: LAPB=X.25, LAPD=ISDN D-channel, LAPM=modems."
)
br()


# =============================================================================
#  SECTION 3: MAY-JUNE 2024 ESE
# =============================================================================
part_box("SECTION 3 -- MAY-JUNE 2024 END SEMESTER EXAM")

# -----------------------------------------------------------------------------
#  MJ2024 Q1(a): Broadcast vs Point-to-Point
# -----------------------------------------------------------------------------
chap_box("May-June 2024 Q1(a) [3 Marks]: Broadcast vs Point-to-Point Networks")

section("Broadcast vs Point-to-Point")
info_table(
    ["Feature", "Broadcast Network", "Point-to-Point Network"],
    [
        [
            "Definition",
            "Single shared channel; all nodes receive every transmitted packet",
            "Dedicated link between exactly two nodes; only those two communicate",
        ],
        [
            "Addressing",
            "Must address packets to intended recipient; others ignore them",
            "No addressing needed (only two endpoints on the link)",
        ],
        [
            "Examples",
            "Ethernet LAN (bus/hub), Wi-Fi (802.11), satellite TV, cable TV",
            "Leased lines (T1/E1), PPP dial-up, fiber between two routers",
        ],
        [
            "Topology",
            "Bus, ring (logical), wireless (star with AP)",
            "Point-to-point (direct link)",
        ],
        [
            "Collision Risk",
            "Yes -- multiple nodes share medium (requires CSMA/CD or token)",
            "No -- full channel dedicated to two endpoints",
        ],
        [
            "Scalability",
            "Limited -- more nodes = more collisions/overhead",
            "Good -- each link dedicated, no shared medium",
        ],
    ],
)
note("See also Dec 2024 Q1(a) -- same question, cross-reference applies.")
br()

# -----------------------------------------------------------------------------
#  MJ2024 Q1(b): Interfaces and Services
# -----------------------------------------------------------------------------
chap_box(
    "May-June 2024 Q1(b) [4 Marks]: Interfaces and Services for Computer Network Model"
)

section("Services, Interfaces, and Protocols")
definition(
    "In the OSI reference model, each layer provides a set of <b>services</b> to the layer above "
    "through a <b>service interface</b>, and uses the services of the layer below. The "
    "<b>protocol</b> is the set of rules governing communication between peer entities (same layer "
    "on different machines). Service primitives are the operations that can be requested."
)
bullet(
    [
        "<b>Service:</b> What a layer provides to the layer above it (e.g., Layer 3 provides host-to-host delivery to Layer 4).",
        "<b>Interface (SAP -- Service Access Point):</b> The boundary between two adjacent layers through which services are accessed.",
        "<b>Protocol:</b> Rules governing communication between peer entities at the same layer on different machines.",
        "<b>Service Primitive:</b> An abstract operation invoked across the layer interface (REQUEST, INDICATION, RESPONSE, CONFIRM).",
    ]
)

section("OSI Service Primitives")
info_table(
    ["Primitive", "Direction", "Description", "Example"],
    [
        [
            "REQUEST",
            "Layer N user to Layer N",
            "Entity requests a service from the layer below",
            "Transport layer asks network layer to establish a connection",
        ],
        [
            "INDICATION",
            "Layer N to Layer N user",
            "Layer notifies its user that an event has occurred",
            "Network layer informs transport layer that a connection is requested",
        ],
        [
            "RESPONSE",
            "Layer N user to Layer N",
            "Entity responds to an indication primitive",
            "Transport layer accepts or rejects an incoming connection",
        ],
        [
            "CONFIRM",
            "Layer N to Layer N user",
            "Layer confirms that a request has been completed",
            "Network layer confirms the connection has been established",
        ],
    ],
)
br()

# -----------------------------------------------------------------------------
#  MJ2024 Q1(c): Connection-Oriented vs Connectionless
# -----------------------------------------------------------------------------
chap_box(
    "May-June 2024 Q1(c) [4 Marks]: Connection-Oriented vs Connectionless Services"
)

section("Comparison")
definition(
    "<b>Connection-Oriented Service:</b> Before data transfer, a connection must be established "
    "(setup phase), data is transferred, then the connection is released (teardown). Analogous "
    "to a telephone call. Provides reliable, ordered delivery.<br/>"
    "<b>Connectionless Service:</b> Each packet (datagram) is sent independently without "
    "prior setup. Each packet may take a different route. Analogous to postal service."
)

info_table(
    ["Feature", "Connection-Oriented", "Connectionless"],
    [
        [
            "Setup required",
            "Yes -- explicit connection establishment before data",
            "No setup -- data sent immediately",
        ],
        [
            "Reliability",
            "Reliable -- ACK, retransmission, ordering guaranteed",
            "Unreliable -- best effort (no ACK or ordering)",
        ],
        [
            "Ordering",
            "Packets always arrive in order",
            "Packets may arrive out of order",
        ],
        [
            "Routing",
            "Fixed path established for entire connection (virtual circuit)",
            "Each packet routed independently",
        ],
        [
            "Overhead",
            "Higher setup overhead, lower per-packet overhead",
            "No setup overhead, but more per-packet overhead (full address each time)",
        ],
        [
            "Examples",
            "TCP, X.25, ATM, telephone PSTN",
            "IP, UDP, Ethernet (without connection), datagram networks",
        ],
        [
            "Analogy",
            "Telephone call (circuit switched)",
            "Postal mail (packet switched)",
        ],
    ],
)
br()

# -----------------------------------------------------------------------------
#  MJ2024 Q1(d): ISO-OSI Model
# -----------------------------------------------------------------------------
chap_box("May-June 2024 Q1(d) [10 Marks]: ISO-OSI Reference Model")

section("OSI Model Overview")
definition(
    "<b>ISO-OSI (Open Systems Interconnection) Reference Model:</b> A conceptual 7-layer "
    "framework developed by ISO in 1984 that standardizes how different computer systems "
    "communicate over a network. Each layer has well-defined functions and interfaces with "
    "adjacent layers. It separates protocols into seven logical layers from physical "
    "transmission up to user-facing applications."
)

stack4 = ed.LayeredStack(
    width=CW, height=280, caption="Fig 3.1: ISO-OSI 7-layer reference model"
)
stack4.layer(
    "7 -- Application Layer",
    sublabel="HTTP, FTP, SMTP, DNS, Telnet -- user-facing network services",
)
stack4.layer(
    "6 -- Presentation Layer",
    sublabel="Data encoding, encryption (SSL/TLS), compression, format conversion",
)
stack4.layer(
    "5 -- Session Layer",
    sublabel="Session management, synchronization, dialog control (RPC, NetBIOS)",
)
stack4.layer(
    "4 -- Transport Layer",
    sublabel="Process-to-process delivery, TCP (reliable) and UDP (unreliable)",
)
stack4.layer(
    "3 -- Network Layer",
    sublabel="Host-to-host routing, IP addressing, fragmentation (IP, ICMP, ARP)",
)
stack4.layer(
    "2 -- Data Link Layer",
    sublabel="Node-to-node framing, MAC addressing, error/flow control (Ethernet, PPP)",
)
stack4.layer(
    "1 -- Physical Layer",
    sublabel="Bit transmission -- electrical/optical signals, cables, connectors",
)
story.extend(stack4.as_flowable())

section("OSI Layer Functions Detail")
info_table(
    ["Layer", "No.", "PDU", "Key Functions", "Protocols/Standards"],
    [
        [
            "Application",
            "7",
            "Data",
            "Provides network services to user applications; file transfer, email, web browsing",
            "HTTP, FTP, SMTP, DNS, DHCP, SNMP, Telnet",
        ],
        [
            "Presentation",
            "6",
            "Data",
            "Data translation, encryption/decryption, compression/decompression, data format conversion",
            "SSL/TLS, JPEG, MPEG, ASCII, EBCDIC, XDR",
        ],
        [
            "Session",
            "5",
            "Data",
            "Establishes, manages, terminates sessions; synchronization checkpoints; dialog control",
            "RPC, NetBIOS, NFS, SQL sessions",
        ],
        [
            "Transport",
            "4",
            "Segment/Datagram",
            "End-to-end delivery, port numbers, reliability (TCP), flow and congestion control",
            "TCP, UDP, SCTP",
        ],
        [
            "Network",
            "3",
            "Packet",
            "Logical addressing (IP), routing, path determination, fragmentation and reassembly",
            "IP, ICMP, ARP, OSPF, BGP, RIP",
        ],
        [
            "Data Link",
            "2",
            "Frame",
            "Physical addressing (MAC), framing, error detection (CRC), flow control, media access",
            "Ethernet 802.3, Wi-Fi 802.11, PPP, HDLC",
        ],
        [
            "Physical",
            "1",
            "Bits",
            "Bit transmission, signal encoding, media type, topology, synchronization, modulation",
            "RS-232, RJ-45, fiber, coaxial, DSL, Bluetooth",
        ],
    ],
)

note(
    "Cross-reference: See Section 2, Q4 (MST-2) for the TCP/IP model comparison with OSI. "
    "See also Dec 2024 Q1(e) -- same question. Mnemonic: 'All People Seem To Need Data Processing' (L7 to L1)."
)
br()

# -----------------------------------------------------------------------------
#  MJ2024 Q1(e): TCP/IP Model -- Cross-reference
# -----------------------------------------------------------------------------
chap_box("May-June 2024 Q1(e) [10 Marks]: TCP/IP Model")
note(
    "This question is fully answered in Section 2, Q4 (MST-2) with LayeredStack diagram, "
    "protocol table, and OSI comparison. Please refer to that section."
)
br()

# -----------------------------------------------------------------------------
#  MJ2024 Q2(b): Switching, Pipelining, Piggybacking
# -----------------------------------------------------------------------------
chap_box("May-June 2024 Q2(b) [4 Marks]: Switching Types, Pipelining, and Piggybacking")

section("Switching Types")
info_table(
    ["Type", "Description", "Advantage", "Disadvantage", "Example"],
    [
        [
            "Circuit Switching",
            "Dedicated physical path established before communication. Path reserved for entire session.",
            "Guaranteed bandwidth and constant delay",
            "Wasted capacity if no data; long setup time",
            "PSTN telephone network",
        ],
        [
            "Datagram Packet Switching",
            "Each packet routed independently -- may take different paths",
            "Efficient bandwidth use; robust to link failures",
            "Variable delay (jitter); out-of-order delivery",
            "Internet (IP)",
        ],
        [
            "Virtual Circuit Packet Switching",
            "Logical path established; packets follow same route but share links",
            "Ordered delivery; less overhead than circuit",
            "Requires setup; virtual circuit state at routers",
            "ATM, X.25, MPLS",
        ],
        [
            "Message Switching",
            "Complete message stored at each intermediate node before forwarding (store-and-forward)",
            "No dedicated circuit; flexible routing",
            "High latency and storage requirements at nodes",
            "Older telegram/telex networks",
        ],
    ],
)

section("Pipelining")
definition(
    "<b>Pipelining:</b> A technique in data link protocols where the sender transmits "
    "multiple frames without waiting for an acknowledgement for each individual frame. "
    "The efficiency improvement depends on the window size relative to the propagation delay. "
    "Formula: Efficiency = W / (1 + 2a) where W = window size, a = T_prop/T_frame."
)

section("Piggybacking")
definition(
    "<b>Piggybacking:</b> Attaching an acknowledgement for received data to an outgoing "
    "data frame travelling in the opposite direction, instead of sending a separate ACK frame. "
    "This reduces the number of frames on the channel and improves efficiency."
)
br()

# -----------------------------------------------------------------------------
#  MJ2024 Q2(c): DLL Design Issues
# -----------------------------------------------------------------------------
chap_box("May-June 2024 Q2(c) [4 Marks]: Data Link Layer Design Issues")

section("Design Issues")
bullet(
    [
        "<b>Framing:</b> How to delineate the start and end of each frame. Methods: character count, flag bytes with byte stuffing, bit stuffing (HDLC), physical layer coding violations.",
        "<b>Error Control:</b> Detecting and correcting transmission errors. Uses CRC (error detection) combined with ARQ (retransmission) protocols.",
        "<b>Flow Control:</b> Preventing a fast sender from overwhelming a slow receiver. Methods: feedback-based (stop-and-wait, sliding window), rate-based.",
        "<b>Link Management:</b> Establishing, maintaining, and terminating data link connections (e.g., PPP LCP negotiation).",
        "<b>Addressing:</b> Physical (MAC) addressing to identify source and destination nodes on the same link.",
        "<b>Access Control:</b> Determining which station transmits on a shared medium at any time (CSMA/CD, token passing).",
    ]
)
br()

# -----------------------------------------------------------------------------
#  MJ2024 Q2(d): Error Detection and Correction
# -----------------------------------------------------------------------------
chap_box("May-June 2024 Q2(d) [10 Marks]: Error Detection and Correction")

section("Types of Errors")
bullet(
    [
        "<b>Single-bit error:</b> Only one bit in the data unit changes (0 to 1 or 1 to 0).",
        "<b>Burst error:</b> Multiple consecutive bits are corrupted (more common in real channels).",
        "<b>Error detection:</b> Detects that an error has occurred -- requires retransmission (ARQ).",
        "<b>Error correction:</b> Detects AND corrects errors without retransmission -- uses redundant bits (FEC).",
    ]
)

section("Parity Check")
definition(
    "<b>Parity Check:</b> A simple error detection scheme where one extra bit (parity bit) "
    "is added to make the total number of 1-bits either even (even parity) or odd (odd parity). "
    "Detects single-bit errors only -- cannot detect all burst errors or double-bit errors."
)

section("CRC -- Cyclic Redundancy Check")
definition(
    "<b>CRC (Cyclic Redundancy Check):</b> A powerful error detection technique based on "
    "polynomial division. The sender treats the data as a binary polynomial and divides "
    "by a generator polynomial (G(x)). The remainder (CRC) is appended to the data. "
    "The receiver performs the same division -- if remainder is 0, no error detected."
)

code_block("""
 CRC WORKED EXAMPLE:
 =====================================================================
 Data bits (M)  : 1101          (to transmit)
 Generator (G)  : 1011          (degree 3 -- so append 3 zeros to M)
 Augmented M    : 1101 000      (M shifted left by degree of G)

 LONG DIVISION (XOR):
       1 1 1 1  <- quotient (not important)
      --------
 1011 | 1101 000
        1011
       --------
         110 0
         101 1
        ------
          01 10
           0 00
          ----
           1 10 0   <- bring down
           1 01 1
           ------
             0 01   <- Remainder = 001

 CRC remainder    = 001
 Transmitted data = 1101 001  (original + CRC appended)

 RECEIVER CHECK:
 1101 001 / 1011 = remainder 0 -> No error detected!
""")

section("Hamming Code -- Error Correction")
definition(
    "<b>Hamming Code:</b> A forward error correction (FEC) code that can detect "
    "up to 2-bit errors and correct single-bit errors. It adds redundant parity bits "
    "at positions that are powers of 2 (positions 1, 2, 4, 8, ...). For m data bits, "
    "requires r parity bits such that 2^r >= m + r + 1."
)
code_block("""
 HAMMING CODE EXAMPLE (4 data bits, 3 parity bits):
 =====================================================================
 Data bits: d1 d2 d3 d4 = 1 0 1 1
 Parity bit positions: p1(pos 1), p2(pos 2), p4(pos 4)

 Arrangement: p1 p2 d1 p4 d2 d3 d4
 Position:     1   2  3   4  5  6  7

 p1 covers bits at positions: 1,3,5,7 -> p1 xor d1 xor d2 xor d4 = 0 xor 1 xor 0 xor 1 = 0
 p2 covers bits at positions: 2,3,6,7 -> p2 xor d1 xor d3 xor d4 = 0 xor 1 xor 1 xor 1 = 1
 p4 covers bits at positions: 4,5,6,7 -> p4 xor d2 xor d3 xor d4 = 1 xor 0 xor 1 xor 1 = 1

 Codeword: 0 1 1 1 0 1 1

 Error detection: recalculate parity; non-zero syndrome indicates bit position of error.
""")

tip(
    "CRC detects all single-bit, double-bit, odd-bit, and burst errors up to the degree of G(x). "
    "Hamming code: for m data bits, need r parity bits s.t. 2^r >= m+r+1. "
    "CRC-16 uses G(x)=x16+x15+x2+1. CRC-32 used in Ethernet."
)
br()

# -----------------------------------------------------------------------------
#  MJ2024 Q2(e): MAC sublayer vs DLL
# -----------------------------------------------------------------------------
chap_box("May-June 2024 Q2(e) [10 Marks]: Media Access Sublayer vs Data Link Layer")

section("MAC Sublayer")
definition(
    "<b>MAC (Media Access Control) Sublayer:</b> The lower sublayer of the Data Link Layer "
    "(Layer 2 of OSI). It controls how devices on a shared network medium (e.g., Ethernet bus, "
    "Wi-Fi) gain access to the channel. Without access control, multiple simultaneous transmissions "
    "cause collisions, making communication impossible."
)

section("LLC vs MAC Sublayers")
info_table(
    ["Feature", "LLC Sublayer (IEEE 802.2)", "MAC Sublayer (IEEE 802.3/802.11)"],
    [
        ["Position", "Upper part of Data Link Layer", "Lower part of Data Link Layer"],
        [
            "Function",
            "Interface with network layer; flow and error control (SAP addressing)",
            "Channel access control; physical addressing (MAC addresses)",
        ],
        [
            "Hardware dependent",
            "No -- same LLC for all 802.x networks",
            "Yes -- different MAC for Ethernet, Wi-Fi, Token Ring",
        ],
        [
            "Addressing",
            "DSAP and SSAP (service access points)",
            "48-bit MAC address (hardware address)",
        ],
        [
            "Protocols",
            "IEEE 802.2 SNAP",
            "CSMA/CD (Ethernet), CSMA/CA (Wi-Fi), Token Passing",
        ],
    ],
)

section("Random Access Protocols")
bullet(
    [
        "<b>Pure ALOHA:</b> Transmit anytime. If collision, wait random time and retransmit. Throughput: S = G*e^(-2G), max 18.4% at G=0.5.",
        "<b>Slotted ALOHA:</b> Transmit only at slot boundaries. Throughput: S = G*e^(-G), max 36.8% at G=1.0.",
        "<b>CSMA (Carrier Sense Multiple Access):</b> Listen before transmit -- if channel busy, wait. Reduces but does not eliminate collisions.",
        "<b>CSMA/CD (Collision Detection):</b> Listen while transmitting. If collision detected, abort, send jam signal, wait random time (binary exponential backoff). Used in Ethernet.",
        "<b>CSMA/CA (Collision Avoidance):</b> Avoid collisions using ACK, IFS (interframe spacing), and random backoff. Used in Wi-Fi (802.11) -- cannot detect collisions due to hidden node problem.",
    ]
)
br()

# -----------------------------------------------------------------------------
#  MJ2024 Q3(a): MAC Layer Protocols
# -----------------------------------------------------------------------------
chap_box("May-June 2024 Q3(a) [3 Marks]: MAC Layer Protocols")

section("Categories of MAC Protocols")
bullet(
    [
        "<b>Random Access (Contention-based):</b> No coordination; stations compete for channel. ALOHA (Pure and Slotted), CSMA, CSMA/CD (Ethernet 802.3), CSMA/CA (Wi-Fi 802.11).",
        "<b>Controlled Access (Deterministic):</b> Access is granted in a controlled manner. Polling (primary polls secondaries), Token Passing (802.4 Token Bus, 802.5 Token Ring), Reservation.",
        "<b>Channelization (Multiple Access):</b> Channel divided into sub-channels. FDMA (Frequency Division Multiple Access), TDMA (Time Division Multiple Access), CDMA (Code Division Multiple Access -- spread spectrum).",
    ]
)
br()

# -----------------------------------------------------------------------------
#  MJ2024 Q3(b): FDDI
# -----------------------------------------------------------------------------
chap_box("May-June 2024 Q3(b) [4 Marks]: FDDI -- Fiber Distributed Data Interface")

section("FDDI Overview")
definition(
    "<b>FDDI (Fiber Distributed Data Interface):</b> A high-speed LAN standard that uses "
    "optical fiber as the transmission medium at 100 Mbps. It uses a <b>dual counter-rotating "
    "token ring</b> topology for fault tolerance. FDDI was widely used in the 1990s as a "
    "backbone network technology. Defined by ANSI X3T9.5."
)
bullet(
    [
        "<b>Speed:</b> 100 Mbps over optical fiber (multimode or single-mode).",
        "<b>Topology:</b> Dual counter-rotating ring -- primary ring for normal data, secondary ring for fault recovery.",
        "<b>Encoding:</b> 4B/5B encoding (converts 4 data bits to 5-bit code groups) + NRZI signalling.",
        "<b>Token:</b> Timed Token Rotation (TTR) -- each station gets the token for a defined time. Target Token Rotation Time (TTRT) negotiated.",
        "<b>Fault Tolerance:</b> If primary ring fails, traffic wraps onto secondary ring automatically (self-healing ring).",
        "<b>Distance:</b> Up to 200 km total ring length; up to 2 km between stations on single-mode fiber.",
        "<b>Classes:</b> Class A stations connect to both rings; Class B stations connect to primary ring only.",
    ]
)
note(
    "FDDI is largely obsolete, replaced by Fast Ethernet (100BASE-TX), Gigabit Ethernet, and now 10GbE. "
    "See also Dec 2024 Q3(c) for the same question."
)
br()

# -----------------------------------------------------------------------------
#  MJ2024 Q3(c): CSMA Techniques
# -----------------------------------------------------------------------------
chap_box("May-June 2024 Q3(c) [4 Marks]: CSMA Techniques")

section("CSMA -- Carrier Sense Multiple Access")
definition(
    "<b>CSMA:</b> A media access protocol where a station listens to the channel (carrier sense) "
    "before transmitting. If the channel is sensed idle, the station transmits. If the channel "
    "is busy, different CSMA variants handle the situation differently."
)

info_table(
    [
        "Variant",
        "Listen Before Transmit",
        "If Channel Busy",
        "If Idle",
        "Collision Probability",
    ],
    [
        [
            "1-Persistent CSMA",
            "Yes",
            "Wait and retransmit immediately when channel becomes idle (persistent)",
            "Transmit with probability 1",
            "High -- everyone waiting transmits at once",
        ],
        [
            "Non-Persistent CSMA",
            "Yes",
            "Wait a random time, then sense again",
            "Transmit",
            "Lower -- random wait reduces simultaneous attempts",
        ],
        [
            "p-Persistent CSMA",
            "Yes",
            "Wait until idle",
            "Transmit with probability p; defer with probability (1-p)",
            "Lower than 1-persistent; depends on p",
        ],
        [
            "CSMA/CD",
            "Yes + collision detection",
            "Wait; if collision detected: jam + backoff",
            "Transmit; monitor for collision",
            "Lowest -- immediate detection and backoff",
        ],
    ],
)
bullet(
    [
        "<b>1-Persistent:</b> Highest throughput at low load but highest collision rate at high load (used in original Ethernet).",
        "<b>Non-Persistent:</b> Good performance at high load; wastes channel idle time.",
        "<b>p-Persistent:</b> Compromise; p is tuned to balance utilization and collision rate.",
        "<b>CSMA/CA (802.11):</b> Uses IFS (SIFS, DIFS) + random backoff + virtual carrier sense (NAV) to avoid collisions in wireless.",
    ]
)
br()

# -----------------------------------------------------------------------------
#  MJ2024 Q3(d): IEEE 802.4 and 802.5
# -----------------------------------------------------------------------------
chap_box(
    "May-June 2024 Q3(d) [10 Marks]: IEEE 802.4 Token Bus and IEEE 802.5 Token Ring"
)

section("IEEE 802.4 -- Token Bus")
definition(
    "<b>IEEE 802.4 Token Bus:</b> A LAN standard that uses token passing for access control "
    "on a bus topology. Physically it is a bus (coaxial cable), but logically it forms a ring "
    "for token passing. Stations are assigned a logical order and a token circulates in this "
    "logical ring. Only the station holding the token can transmit. Deterministic access -- "
    "maximum delay is bounded."
)
bullet(
    [
        "Physical topology: Bus (coaxial cable); logical topology: ring (token circulation).",
        "Deterministic access -- guaranteed maximum delay, suitable for industrial/real-time applications.",
        "Used in industrial networks (MAP -- Manufacturing Automation Protocol).",
        "Token is passed to the station with the next lower logical address.",
        "If station has no data, it immediately passes the token.",
        "Now largely obsolete -- replaced by Industrial Ethernet.",
    ]
)

section("IEEE 802.5 -- Token Ring")
definition(
    "<b>IEEE 802.5 Token Ring:</b> A LAN standard using a logical and physical ring topology "
    "with token passing for access control. A 3-byte free token circulates the ring. When a "
    "station wishes to transmit, it captures the free token, changes it to a busy token, "
    "appends its data frame, and transmits. The frame circulates around the ring and is "
    "removed by the originating station. The token is then released."
)

section("Token Ring Frame Format")
info_table(
    ["Field", "Size", "Description"],
    [
        [
            "SD (Starting Delimiter)",
            "1 byte",
            "Marks start of frame using signal violations",
        ],
        [
            "AC (Access Control)",
            "1 byte",
            "Token bit (T), Priority (PPP), Monitor bit (M), Reservation (RRR)",
        ],
        [
            "FC (Frame Control)",
            "1 byte",
            "Frame type: MAC frame (LLC=0) or data frame (LLC=1)",
        ],
        ["DA (Destination Address)", "6 bytes", "48-bit destination MAC address"],
        ["SA (Source Address)", "6 bytes", "48-bit source MAC address"],
        [
            "Data",
            "Variable",
            "LLC data payload (up to 4500 bytes at 4 Mbps; 18000 bytes at 16 Mbps)",
        ],
        ["FCS (Frame Check Sequence)", "4 bytes", "CRC-32 error detection"],
        [
            "ED (Ending Delimiter)",
            "1 byte",
            "Marks end of frame; includes E-bit (error) and I-bit (intermediate frame)",
        ],
        [
            "FS (Frame Status)",
            "1 byte",
            "A-bit (address recognized) and C-bit (frame copied) set by destination",
        ],
    ],
)

section("IEEE 802.4 vs IEEE 802.5 Comparison")
info_table(
    ["Feature", "IEEE 802.4 Token Bus", "IEEE 802.5 Token Ring"],
    [
        ["Physical Topology", "Bus", "Ring (star-wired with MAU hub)"],
        ["Logical Topology", "Ring (logical)", "Ring"],
        ["Medium", "Coaxial cable (75-ohm)", "Shielded twisted pair (STP)"],
        ["Speed", "1, 5, 10 Mbps", "4 Mbps or 16 Mbps"],
        [
            "Access Method",
            "Token passing on logical ring",
            "Token passing on physical ring",
        ],
        ["Deterministic", "Yes", "Yes"],
        [
            "Failure Recovery",
            "Dedicated procedures for lost/duplicate token",
            "Dedicated Monitor station recovers lost token",
        ],
        [
            "Usage",
            "Industrial automation (MAP)",
            "Corporate LANs (1980s-1990s, IBM installations)",
        ],
    ],
)
br()

# -----------------------------------------------------------------------------
#  MJ2024 Q3(e): ALOHA + Classful vs Classless
# -----------------------------------------------------------------------------
chap_box("May-June 2024 Q3(e) [10 Marks]: ALOHA and Classful vs Classless Addressing")

section("Pure ALOHA")
definition(
    "<b>Pure ALOHA:</b> The simplest random access protocol. Any station may transmit "
    "at any time. If a collision occurs (overlapping transmissions), the frame is destroyed. "
    "Each station waits a random time before retransmitting. No synchronization required."
)
bullet(
    [
        "Throughput: <b>S = G * e^(-2G)</b> where G = offered load (frames/slot), S = throughput.",
        "Maximum throughput: <b>18.4%</b> at G = 0.5 (S = 0.5 * e^(-1) = 0.184).",
        "Vulnerable period = 2 * T_frame (a frame sent at t can collide with frames sent in [t-T, t+T]).",
    ]
)

section("Slotted ALOHA")
definition(
    "<b>Slotted ALOHA:</b> An improvement over Pure ALOHA where time is divided into discrete "
    "slots of one frame duration. Stations can only begin transmitting at the start of a slot. "
    "This halves the vulnerable period, doubling the maximum throughput."
)
bullet(
    [
        "Throughput: <b>S = G * e^(-G)</b>.",
        "Maximum throughput: <b>36.8%</b> at G = 1.0 (S = 1 * e^(-1) = 0.368).",
        "Vulnerable period = 1 * T_frame (only within the current slot).",
        "Requires synchronized clocks across all stations.",
    ]
)

code_block("""
 ALOHA THROUGHPUT CALCULATIONS:
 =====================================================================
 Pure ALOHA   : S = G * e^(-2G)    Max S = 0.184 (18.4%) at G = 0.5
 Slotted ALOHA: S = G * e^(-G)     Max S = 0.368 (36.8%) at G = 1.0

 Example calculations:
   Pure ALOHA,    G=0.5: S = 0.5 * e^(-1.0) = 0.5 * 0.368 = 0.184
   Pure ALOHA,    G=1.0: S = 1.0 * e^(-2.0) = 1.0 * 0.135 = 0.135
   Slotted ALOHA, G=1.0: S = 1.0 * e^(-1.0) = 1.0 * 0.368 = 0.368
   Slotted ALOHA, G=0.5: S = 0.5 * e^(-0.5) = 0.5 * 0.607 = 0.303
""")

section("Classful IP Addressing")
definition(
    "<b>Classful Addressing:</b> The original IPv4 addressing scheme where addresses are "
    "divided into classes A, B, C, D, E based on the leading bits. The class determines "
    "the split between network and host bits."
)

info_table(
    [
        "Class",
        "First Bits",
        "Network Bits",
        "Host Bits",
        "Address Range",
        "Max Hosts",
        "Use",
    ],
    [
        [
            "A",
            "0",
            "8",
            "24",
            "0.0.0.0 - 127.255.255.255",
            "16,777,214",
            "Large ISPs, governments",
        ],
        [
            "B",
            "10",
            "16",
            "16",
            "128.0.0.0 - 191.255.255.255",
            "65,534",
            "Medium organisations",
        ],
        ["C", "110", "24", "8", "192.0.0.0 - 223.255.255.255", "254", "Small networks"],
        [
            "D",
            "1110",
            "N/A",
            "N/A",
            "224.0.0.0 - 239.255.255.255",
            "N/A",
            "Multicast groups",
        ],
        [
            "E",
            "11110",
            "N/A",
            "N/A",
            "240.0.0.0 - 255.255.255.255",
            "N/A",
            "Reserved/Experimental",
        ],
    ],
)

section("Classless / CIDR Addressing")
definition(
    "<b>CIDR (Classless Inter-Domain Routing):</b> Introduced in 1993 to address IPv4 "
    "address exhaustion. Uses a prefix notation (IP/prefix-length) instead of fixed classes. "
    "The prefix length specifies exactly how many bits are the network ID, regardless of class."
)
code_block("""
 CIDR EXAMPLE:
 =====================================================================
 Network: 192.168.1.0/26
   Prefix length = 26 bits -> Subnet mask = 255.255.255.192
   Network bits  = 26   -> 64 addresses per subnet
   Host bits     = 6    -> 2^6 - 2 = 62 usable host addresses
   Range         : 192.168.1.0 to 192.168.1.63
   Network addr  : 192.168.1.0   (all host bits = 0)
   Broadcast addr: 192.168.1.63  (all host bits = 1)
   Usable hosts  : 192.168.1.1 to 192.168.1.62

 Subnet mask calculation:
   /26 = 11111111.11111111.11111111.11000000 = 255.255.255.192
""")
br()

# -----------------------------------------------------------------------------
#  MJ2024 Q4(a): Logical, Physical, Port Addresses
# -----------------------------------------------------------------------------
chap_box("May-June 2024 Q4(a) [3 Marks]: Logical, Physical, and Port Addresses")

section("Three Types of Network Addresses")
info_table(
    ["Address Type", "Size", "Layer", "Used By", "Example", "Assigned By"],
    [
        [
            "Physical (MAC)",
            "48 bits (6 bytes)",
            "Layer 2 (Data Link)",
            "Ethernet frames, ARP; node-to-node delivery",
            "AA:BB:CC:DD:EE:FF",
            "Manufacturer (burned into NIC)",
        ],
        [
            "Logical (IP)",
            "32 bits (IPv4) / 128 bits (IPv6)",
            "Layer 3 (Network)",
            "IP packets; end-to-end host-to-host delivery across networks",
            "192.168.1.100 / 2001:db8::1",
            "Network administrator / ISP / DHCP",
        ],
        [
            "Port Number",
            "16 bits (0-65535)",
            "Layer 4 (Transport)",
            "TCP/UDP; process-to-process delivery within a host",
            "Port 80 (HTTP), Port 443 (HTTPS), Port 22 (SSH)",
            "IANA (well-known) / OS (ephemeral)",
        ],
    ],
)
note("See also Dec 2024 Q4(a) -- same question.")
br()

# -----------------------------------------------------------------------------
#  MJ2024 Q4(b): Subnet Mask
# -----------------------------------------------------------------------------
chap_box("May-June 2024 Q4(b) [4 Marks]: Subnet Mask and Subnet Calculation")

section("Subnet Mask")
definition(
    "<b>Subnet Mask:</b> A 32-bit number that divides an IP address into the network "
    "portion (bits set to 1) and the host portion (bits set to 0). It is applied using "
    "a bitwise AND operation with the IP address to extract the network address."
)
code_block("""
 SUBNET MASK EXAMPLE -- 192.168.1.100/26:
 =====================================================================
 IP Address   : 192.168.1.100
 Binary       : 11000000.10101000.00000001.01100100
 Subnet mask  : 255.255.255.192
 Binary mask  : 11111111.11111111.11111111.11000000
                                              ^^
                                    26 network bits | 6 host bits

 AND operation:
   IP       : 11000000.10101000.00000001.01100100
   Mask     : 11111111.11111111.11111111.11000000
   --------------------------------------------- AND
   Network  : 11000000.10101000.00000001.01000000 = 192.168.1.64

 Results:
   Network address   : 192.168.1.64
   Broadcast address : 192.168.1.127  (all host bits = 1)
   Usable host range : 192.168.1.65 to 192.168.1.126
   Usable hosts      : 2^6 - 2 = 62 hosts
""")
br()

# -----------------------------------------------------------------------------
#  MJ2024 Q4(c): Routing Algorithms Overview
# -----------------------------------------------------------------------------
chap_box("May-June 2024 Q4(c) [4 Marks]: Routing Algorithms Overview")

section("Classification of Routing Algorithms")
bullet(
    [
        "<b>Non-Adaptive (Static) Routing:</b> Routes are pre-configured and do not change based on network conditions.",
        "  -- <b>Flooding:</b> Every incoming packet sent out on every outgoing link except arrival. Guaranteed delivery, very inefficient.",
        "  -- <b>Fixed Routing (Static routes):</b> Routes manually configured in routing table. Simple but inflexible.",
        "<b>Adaptive (Dynamic) Routing:</b> Routes change dynamically based on current network topology and traffic.",
        "  -- <b>Distance Vector (Bellman-Ford):</b> Each router shares its routing table with neighbours. RIP uses DV. Slow convergence, count-to-infinity problem.",
        "  -- <b>Link State (Dijkstra SPF):</b> Each router floods link state info to all routers; each builds complete topology map, runs Dijkstra's algorithm. OSPF uses LS. Fast convergence.",
        "  -- <b>Path Vector:</b> Extension of DV that includes the full path (AS path). BGP uses path vector. Prevents routing loops.",
    ]
)

info_table(
    ["Algorithm Type", "Protocol", "Algorithm Used", "Info Shared", "Convergence"],
    [
        [
            "Distance Vector",
            "RIP",
            "Bellman-Ford",
            "Routing table (distance + next hop)",
            "Slow (30-sec updates, count-to-infinity)",
        ],
        [
            "Link State",
            "OSPF, IS-IS",
            "Dijkstra SPF",
            "Link State Advertisements (LSAs) -- full topology",
            "Fast (event-driven flooding)",
        ],
        [
            "Path Vector",
            "BGP",
            "Path vector",
            "Full AS path to destination",
            "Moderate (policy-driven)",
        ],
        [
            "Static/Flooding",
            "None (built-in)",
            "None",
            "No sharing",
            "Instant (no convergence needed)",
        ],
    ],
)
br()

# -----------------------------------------------------------------------------
#  MJ2024 Q4(d): Congestion Control
# -----------------------------------------------------------------------------
chap_box("May-June 2024 Q4(d) [10 Marks]: Congestion Control Algorithms")

section("What is Congestion?")
definition(
    "<b>Congestion:</b> A condition in which too many packets are present in a network or "
    "part of a network, causing degraded performance -- increased delay, packet loss, and "
    "potentially network collapse (congestion collapse). Occurs when offered load exceeds "
    "network capacity."
)

section("Open-Loop Congestion Control (Prevention)")
bullet(
    [
        "<b>Good design:</b> Careful network design to avoid congestion before it occurs.",
        "<b>Admission Control:</b> New connections are only accepted if the network has sufficient resources (used in IntServ/RSVP).",
        "<b>Traffic Shaping -- Leaky Bucket:</b> Output rate is constant regardless of bursty input. Smooths traffic to a fixed rate. Token bucket allows controlled bursts.",
        "<b>Traffic Shaping -- Token Bucket:</b> Tokens accumulate at a fixed rate; each packet needs a token. Allows bursts up to token bucket size.",
        "<b>Packet Discarding:</b> Drop packets probabilistically before buffer is full (RED -- Random Early Detection).",
    ]
)

section("Closed-Loop Congestion Control (Reaction)")
bullet(
    [
        "<b>Back Pressure:</b> A congested node notifies the previous node to slow down; propagates upstream.",
        "<b>Choke Packets:</b> Congested router sends a choke packet to the source, telling it to reduce its sending rate.",
        "<b>Implicit Signalling:</b> Source infers congestion from increased RTT or packet loss (TCP uses this).",
        "<b>Explicit Signalling:</b> Routers mark packets (ECN -- Explicit Congestion Notification) to signal congestion to endpoints.",
    ]
)

section("TCP Congestion Control (Specific)")
bullet(
    [
        "<b>Slow Start:</b> cwnd = 1 MSS initially; doubles every RTT. Grows exponentially until ssthresh.",
        "<b>Congestion Avoidance (AIMD):</b> After ssthresh, cwnd increases by 1 MSS per RTT. On loss: ssthresh = cwnd/2, cwnd = 1.",
        "<b>Fast Retransmit:</b> 3 duplicate ACKs -> retransmit immediately without waiting for timeout.",
        "<b>Fast Recovery:</b> After fast retransmit: ssthresh = cwnd/2, cwnd = ssthresh; enter congestion avoidance.",
    ]
)

info_table(
    ["Algorithm", "Type", "Mechanism", "TCP Example"],
    [
        [
            "Leaky Bucket",
            "Open-loop (prevention)",
            "Constant output rate regardless of burst input",
            "Traffic policer at ISP edge",
        ],
        [
            "Token Bucket",
            "Open-loop (prevention)",
            "Tokens accumulate; allows bursts up to bucket size",
            "CBR shaping for VoIP",
        ],
        [
            "Admission Control",
            "Open-loop (prevention)",
            "Reject new flows if insufficient resources",
            "IntServ/RSVP bandwidth reservation",
        ],
        [
            "Choke Packets",
            "Closed-loop (reaction)",
            "Router sends ICMP source quench to reduce rate",
            "Legacy mechanism (deprecated)",
        ],
        [
            "ECN",
            "Closed-loop (reaction)",
            "Routers mark CE bit in IP header; endpoints react",
            "TCP ECN (RFC 3168)",
        ],
        [
            "Slow Start",
            "Closed-loop (TCP)",
            "cwnd starts at 1 MSS; doubles each RTT",
            "TCP initial connection",
        ],
        [
            "AIMD",
            "Closed-loop (TCP)",
            "Additive increase, multiplicative decrease on loss",
            "TCP congestion avoidance phase",
        ],
        [
            "Fast Retransmit",
            "Closed-loop (TCP)",
            "3 dup ACKs -> immediate retransmit",
            "TCP Reno, TCP NewReno",
        ],
    ],
)
note("Cross-reference: See also Dec 2024 Q5(b) for the same question.")
br()

# -----------------------------------------------------------------------------
#  MJ2024 Q4(e): IPv4 and IPv6
# -----------------------------------------------------------------------------
chap_box("May-June 2024 Q4(e) [10 Marks]: IPv4 and IPv6")

section("IPv4 Header Format")
definition(
    "<b>IPv4:</b> The fourth version of the Internet Protocol. Uses 32-bit addresses "
    "(4.3 billion total). Header is variable-length (20-60 bytes). Supports fragmentation "
    "by routers. Has known limitations: address exhaustion, complex header, no built-in security."
)

packet_format(
    "IPv4 Header (minimum 20 bytes)",
    [
        ("Version", 4),
        ("IHL", 4),
        ("Type of Service", 8),
        ("Total Length", 16),
        ("Identification", 16),
        ("Flags", 3),
        ("Fragment Offset", 13),
        ("TTL", 8),
        ("Protocol", 8),
        ("Header Checksum", 16),
        ("Source IP Address", 32),
        ("Destination IP Address", 32),
        ("Options and Padding", 32),
    ],
)

section("IPv6 Overview")
definition(
    "<b>IPv6:</b> The sixth version of the Internet Protocol. Uses 128-bit addresses "
    "(3.4 x 10^38 total). Fixed 40-byte header (simpler than IPv4). No fragmentation "
    "by routers -- source does Path MTU Discovery. Built-in IPsec support. Flow label "
    "for QoS. No header checksum (relies on L2/L4)."
)

section("IPv4 vs IPv6 Comparison")
info_table(
    ["Feature", "IPv4", "IPv6"],
    [
        ["Address Size", "32 bits (4 bytes)", "128 bits (16 bytes)"],
        ["Address Space", "~4.3 billion (2^32)", "~3.4 x 10^38 (2^128)"],
        ["Header Size", "Variable: 20-60 bytes", "Fixed: 40 bytes"],
        ["Fragmentation", "By routers and source", "Only by source (PMTUD)"],
        [
            "Header Checksum",
            "Yes (recalculated at each hop)",
            "No (eliminated for speed)",
        ],
        [
            "Security (IPsec)",
            "Optional/external",
            "Built-in (mandatory in original spec)",
        ],
        [
            "Configuration",
            "Manual or DHCP",
            "Stateless Autoconfiguration (SLAAC) or DHCPv6",
        ],
        ["Broadcast", "Yes (255.255.255.255)", "No -- replaced by multicast/anycast"],
        ["Flow Label", "No", "Yes (20-bit flow label for QoS)"],
        [
            "NAT Required",
            "Often (due to address scarcity)",
            "No -- enough addresses for all devices",
        ],
    ],
)
br()

# -----------------------------------------------------------------------------
#  MJ2024 Q5(a): ping command
# -----------------------------------------------------------------------------
chap_box("May-June 2024 Q5(a) [3 Marks]: The ping Command")

section("ping -- Packet InterNet Groper")
definition(
    "<b>ping:</b> A network diagnostic utility that uses ICMP (Internet Control Message Protocol) "
    "Echo Request and Echo Reply messages to test connectivity between two hosts and measure "
    "round-trip time (RTT). It is the most basic network troubleshooting tool."
)
bullet(
    [
        "Sends ICMP Echo Request to the target host.",
        "Target host replies with ICMP Echo Reply.",
        "Reports: RTT (round-trip time), TTL remaining, and packet loss.",
    ]
)

code_block("""
 PING SAMPLE OUTPUT:
 =====================================================================
 C:\\> ping 8.8.8.8

 Pinging 8.8.8.8 with 32 bytes of data:
 Reply from 8.8.8.8: bytes=32 time=14ms TTL=117
 Reply from 8.8.8.8: bytes=32 time=13ms TTL=117
 Reply from 8.8.8.8: bytes=32 time=15ms TTL=117
 Reply from 8.8.8.8: bytes=32 time=14ms TTL=117

 Ping statistics for 8.8.8.8:
   Packets: Sent = 4, Received = 4, Lost = 0 (0% loss)
 Approximate round trip times in milli-seconds:
   Minimum = 13ms, Maximum = 15ms, Average = 14ms

 FIELD MEANINGS:
 bytes = payload size of each ICMP echo request
 time  = round-trip time (RTT) in milliseconds
 TTL   = Time To Live remaining when reply reached our host
         Original TTL - number of hops traversed
         Windows default TTL = 128; Linux = 64; Cisco = 255
""")

bullet(
    [
        "<b>Troubleshooting order:</b> ping 127.0.0.1 (loopback) -> ping own IP -> ping default gateway -> ping remote IP -> ping hostname.",
        "If ping loopback fails: TCP/IP stack is not functioning on local machine.",
        "If ping own IP fails: NIC or IP configuration problem.",
        "If ping gateway fails: Link to gateway (cable/switch) problem.",
        "If ping remote IP works but hostname fails: DNS resolution problem.",
    ]
)
br()

# -----------------------------------------------------------------------------
#  MJ2024 Q5(b): IntServ vs DiffServ -- Cross-reference
# -----------------------------------------------------------------------------
chap_box("May-June 2024 Q5(b) [4 Marks]: IntServ vs DiffServ")
note(
    "This question is fully answered in Section 1, Q2 (MST-3 Q2) with complete definitions, "
    "comparison table, and DSCP values. Please refer to that section."
)
br()

# -----------------------------------------------------------------------------
#  MJ2024 Q5(c): Transport Layer Services Categories
# -----------------------------------------------------------------------------
chap_box("May-June 2024 Q5(c) [4 Marks]: Five Categories of Transport Layer Services")

section("Transport Layer Service Categories")
bullet(
    [
        "<b>1. Connection Control:</b> Establishes, maintains, and terminates connections between processes. TCP uses 3-way handshake (SYN, SYN-ACK, ACK) and 4-step teardown (FIN, FIN-ACK, FIN, ACK).",
        "<b>2. Addressing (Port Numbers):</b> Uses port numbers to identify specific application processes. Enables multiple simultaneous connections (multiplexing/demultiplexing).",
        "<b>3. Reliable Transfer:</b> Guarantees data arrives correctly and completely using ACK, retransmission on timeout, and sequence numbers. TCP is reliable; UDP is not.",
        "<b>4. Flow Control:</b> Prevents the sender from overwhelming the receiver. TCP uses sliding window (rwnd -- receiver window) to advertise available buffer space.",
        "<b>5. Multiplexing / Demultiplexing:</b> Multiple processes on a host share the same transport layer. Multiplexing combines them; demultiplexing delivers incoming segments to the correct process using port numbers.",
    ]
)
br()

# -----------------------------------------------------------------------------
#  MJ2024 Q5(d): TCP vs UDP Comparison
# -----------------------------------------------------------------------------
chap_box(
    "May-June 2024 Q5(d) [10 Marks]: TCP vs UDP Transport Layer Protocol Comparison"
)

section("Detailed Comparison")
info_table(
    ["Feature", "TCP", "UDP"],
    [
        [
            "Connection",
            "Connection-oriented (3-way handshake required)",
            "Connectionless (no setup needed)",
        ],
        [
            "Reliability",
            "Reliable -- ACK + retransmission on loss/error",
            "Unreliable -- best effort, no ACK",
        ],
        [
            "Ordering",
            "In-order delivery guaranteed (sequence numbers)",
            "No ordering guarantee -- may arrive out-of-order",
        ],
        [
            "Error Checking",
            "Checksum (header + data + pseudo-header); retransmit on error",
            "Checksum (optional in IPv4, mandatory in IPv6); no retransmit",
        ],
        [
            "Flow Control",
            "Sliding window (rwnd) -- receiver controls sender rate",
            "None -- sender not constrained by receiver",
        ],
        [
            "Congestion Control",
            "Slow start, AIMD, fast retransmit, fast recovery",
            "None -- application must handle or ignore congestion",
        ],
        ["Header Size", "20-60 bytes (variable due to options)", "8 bytes (fixed)"],
        [
            "Speed",
            "Slower due to overhead, handshake, and control mechanisms",
            "Faster -- minimal overhead, immediate transmission",
        ],
        [
            "Full-Duplex",
            "Yes -- simultaneous bidirectional communication",
            "Yes -- but independent datagrams in each direction",
        ],
        [
            "Use Cases",
            "HTTP/S, FTP, SMTP, SSH, Telnet, database connections",
            "DNS, VoIP, streaming media, online gaming, SNMP, DHCP, TFTP",
        ],
        ["PDU Name", "Segment", "Datagram"],
        [
            "Byte Stream",
            "Yes -- treats data as continuous byte stream",
            "No -- preserves message boundaries (datagram)",
        ],
    ],
)
definition(
    "<b>SCTP (Stream Control Transmission Protocol):</b> A newer transport protocol combining "
    "features of TCP (reliable, ordered delivery) and UDP (message-oriented). Supports "
    "multi-homing (multiple IP addresses per endpoint) and multi-streaming. Used in SS7 over IP "
    "(SIGTRAN) and some telecom applications."
)
br()

# -----------------------------------------------------------------------------
#  MJ2024 Q5(e): Internetworking Devices (extended)
# -----------------------------------------------------------------------------
chap_box("May-June 2024 Q5(e) [10 Marks]: Internetworking Devices -- Extended")

section("Extended Device Comparison")
definition(
    "Internetworking devices operate at different OSI layers to connect network segments. "
    "The devices range from simple signal repeaters (Layer 1) to full protocol translators (Layer 7)."
)

info_table(
    [
        "Device",
        "OSI Layer",
        "Function",
        "Filtering/Forwarding",
        "Protocol Dependency",
        "Example",
    ],
    [
        [
            "Repeater",
            "Layer 1 (Physical)",
            "Regenerates and amplifies the physical signal. Extends cable distance.",
            "None -- all bits forwarded",
            "Protocol independent",
            "Coaxial cable repeater",
        ],
        [
            "Hub",
            "Layer 1 (Physical)",
            "Multi-port repeater. Broadcasts incoming signal to all ports.",
            "None -- all signals broadcast",
            "Protocol independent",
            "10/100 Mbps Ethernet hub",
        ],
        [
            "Bridge",
            "Layer 2 (Data Link)",
            "Filters and forwards frames based on MAC address. Connects LAN segments.",
            "Forwards by MAC address (learning bridge)",
            "Protocol independent at L2",
            "IEEE 802.1D bridge",
        ],
        [
            "Switch",
            "Layer 2 (Data Link)",
            "Multi-port bridge with dedicated bandwidth per port. Microsegmentation.",
            "Forwards by MAC address (CAM table)",
            "Protocol independent at L2",
            "Cisco Catalyst switch",
        ],
        [
            "Router",
            "Layer 3 (Network)",
            "Routes packets between different networks using IP routing tables.",
            "Routes by destination IP address",
            "IP protocol specific (L3)",
            "Cisco, Juniper router",
        ],
        [
            "Gateway",
            "Layer 4-7",
            "Protocol conversion between incompatible networks or applications.",
            "Full application-aware translation",
            "Application protocol specific",
            "VoIP gateway, email relay",
        ],
    ],
)

note(
    "Cross-reference: MST-3 Q1 covers Hub, Bridge, Router, Gateway in detail with network diagram. "
    "Repeater and Switch are added here for completeness."
)
br()


# =============================================================================
#  SECTION 4: DEC 2024 ESE
# =============================================================================
part_box("SECTION 4 -- DECEMBER 2024 END SEMESTER EXAM")

# -----------------------------------------------------------------------------
#  Dec2024 Q1(a): Broadcast vs P2P -- Cross-reference
# -----------------------------------------------------------------------------
chap_box("Dec 2024 Q1(a) [3 Marks]: Broadcast vs Point-to-Point")
note(
    "This question is fully answered in Section 3, May-June 2024 Q1(a). "
    "Please refer to that section for the complete comparison table."
)
br()

# -----------------------------------------------------------------------------
#  Dec2024 Q1(b): Network Topologies
# -----------------------------------------------------------------------------
chap_box("Dec 2024 Q1(b) [4 Marks]: Network Topologies")

section("Physical Network Topologies")
info_table(
    ["Topology", "Description", "Advantage", "Disadvantage", "Example"],
    [
        [
            "Bus",
            "Single backbone cable; all nodes connect to it. Terminators at each end.",
            "Simple, cheap; easy to install",
            "Single point of failure (cable); limited length; collisions",
            "Early 10BASE2/10BASE5 Ethernet",
        ],
        [
            "Star",
            "All nodes connect to a central hub or switch. Hub/switch is the central point.",
            "Easy to add/remove nodes; failure of one node does not affect others",
            "Central hub/switch is single point of failure; more cable needed",
            "Modern Ethernet (twisted pair + switch)",
        ],
        [
            "Ring",
            "Nodes connected in a closed loop; data travels in one direction.",
            "No collisions (token); equal access for all nodes",
            "Failure of one node or cable breaks ring; troubleshooting difficult",
            "Token Ring (802.5), FDDI",
        ],
        [
            "Mesh",
            "Every node connects to every other node (full mesh) or multiple nodes (partial mesh).",
            "Highly fault tolerant; multiple paths available",
            "Very expensive; complex wiring (N*(N-1)/2 links for full mesh)",
            "WAN backbone, Internet core routers",
        ],
        [
            "Tree (Hierarchical)",
            "Hierarchical structure of star networks. Root node at top, branches extend down.",
            "Scalable; easy to extend; hierarchical management",
            "Root node is single point of failure; complex cabling",
            "Enterprise LAN (access/distribution/core)",
        ],
        [
            "Hybrid",
            "Combination of two or more topologies.",
            "Flexible; can combine advantages of multiple topologies",
            "Complex design; expensive",
            "Large enterprise networks combining star and mesh",
        ],
    ],
)
br()

# -----------------------------------------------------------------------------
#  Dec2024 Q1(c): Straight/Cross Cable + Connection vs Connectionless
# -----------------------------------------------------------------------------
chap_box("Dec 2024 Q1(c) [4 Marks]: Cable Types and Connection vs Connectionless")

section("Straight-Through vs Crossover Cable")
definition(
    "<b>Straight-Through Cable:</b> Both ends use the same wiring standard (T568A-T568A "
    "or T568B-T568B). Used to connect <b>different</b> device types (PC to switch, switch to router).<br/>"
    "<b>Crossover Cable:</b> One end uses T568A, the other T568B. The TX and RX pairs are crossed. "
    "Used to connect <b>same</b> device types (PC to PC, switch to switch, router to router)."
)

info_table(
    ["Connection Type", "Cable Used", "Examples"],
    [
        ["PC to Switch/Hub", "Straight-through", "PC connected to office switch port"],
        ["PC to Router", "Straight-through", "PC directly to router Ethernet port"],
        ["Switch to Router", "Straight-through", "LAN switch uplink to router"],
        [
            "PC to PC (direct)",
            "Crossover",
            "Two PCs connected back-to-back without switch",
        ],
        ["Switch to Switch", "Crossover (or Auto-MDI-X)", "Cascading two switches"],
        ["Router to Router", "Crossover", "Direct router-to-router Ethernet link"],
    ],
)
note(
    "Modern devices with Auto-MDI-X (automatic crossover detection) automatically adjust, "
    "so the cable type does not matter. Most devices since 2000 support Auto-MDI-X."
)
note("For Connection-Oriented vs Connectionless services, see Section 3, Q1(c).")
br()

# -----------------------------------------------------------------------------
#  Dec2024 Q1(d): X.25 and ARPANET
# -----------------------------------------------------------------------------
chap_box("Dec 2024 Q1(d) [10 Marks]: X.25 and ARPANET")

section("X.25 -- Packet-Switched WAN Standard")
definition(
    "<b>X.25:</b> An ITU-T standard for public packet-switched data networks (PSDN), developed "
    "in the 1970s. X.25 provides a connection-oriented, reliable, virtual-circuit packet-switching "
    "service over error-prone analog telephone lines. It was the dominant WAN technology before "
    "Frame Relay and ATM replaced it."
)
bullet(
    [
        "<b>Three protocol layers:</b> Physical (X.21), Data Link (LAPB), Packet (PLP -- X.25 Packet Layer Protocol).",
        "<b>Virtual Circuits:</b> Two types: PVC (Permanent Virtual Circuit -- always established) and SVC (Switched Virtual Circuit -- established on demand via CALL REQUEST).",
        "<b>Error control:</b> Implemented at every hop (node-to-node) due to unreliable analog links.",
        "<b>Flow control:</b> At both packet layer (D-bit, W-bit) and LAPB layer (sliding window).",
        "<b>Data rates:</b> 2400 bps to 64 kbps (slow by modern standards).",
        "<b>Usage:</b> ATM networks (1970s-1990s), bank terminals, point-of-sale systems, airline reservation systems.",
    ]
)

section("ARPANET -- The Ancestor of the Internet")
definition(
    "<b>ARPANET (Advanced Research Projects Agency Network):</b> The world's first operational "
    "packet-switched network, funded by the US Department of Defense's DARPA. It went online "
    "in October 1969 with 4 nodes (UCLA, UCSB, SRI, Utah). ARPANET is the direct predecessor "
    "of the modern Internet."
)
bullet(
    [
        "<b>First packet-switched network:</b> Used store-and-forward packet switching -- each node stores the complete packet before forwarding.",
        "<b>First nodes (1969):</b> UCLA, Stanford Research Institute (SRI), UC Santa Barbara (UCSB), University of Utah.",
        "<b>NCP (Network Control Protocol):</b> The original host-to-host protocol used before TCP/IP.",
        "<b>TCP/IP transition:</b> January 1, 1983 ('Flag Day') -- ARPANET switched from NCP to TCP/IP.",
        "<b>Email (1972):</b> First email sent by Ray Tomlinson using ARPANET; introduced the @ symbol in addresses.",
        "<b>Decommissioned:</b> 1990 -- replaced by the NSFNET backbone (which became the modern Internet).",
        "<b>Key contribution:</b> Proved that packet switching works; established the architecture for the Internet.",
    ]
)

section("X.25 vs Modern IP Networks")
info_table(
    ["Feature", "X.25", "Modern IP (Internet)"],
    [
        [
            "Switching",
            "Virtual Circuit (connection-oriented)",
            "Datagram (connectionless)",
        ],
        [
            "Error control",
            "At every node (node-to-node, reliable hop)",
            "End-to-end only (IP is best-effort)",
        ],
        ["Flow control", "At every node", "End-to-end (TCP flow control)"],
        ["Speed", "Up to 64 kbps", "Gbps and above"],
        [
            "Design for",
            "Error-prone analog telephone networks",
            "High-reliability digital fiber links",
        ],
        [
            "Addressing",
            "X.121 address (up to 15 digits)",
            "32-bit IPv4 or 128-bit IPv6 addresses",
        ],
    ],
)
note("Cross-reference: X.25 layers also covered in Section 2, Q2 (MST-2 Q2).")
br()

# -----------------------------------------------------------------------------
#  Dec2024 Q1(e): ISO-OSI Model -- Cross-reference
# -----------------------------------------------------------------------------
chap_box("Dec 2024 Q1(e) [10 Marks]: ISO-OSI Reference Model")
note(
    "This question is fully answered in Section 3, May-June 2024 Q1(d) with the full 7-layer "
    "diagram, PDU names, functions, and protocols table. Please refer to that section."
)
br()

# -----------------------------------------------------------------------------
#  Dec2024 Q2(a): Circuit vs Packet Switching
# -----------------------------------------------------------------------------
chap_box("Dec 2024 Q2(a) [3 Marks]: Circuit Switching vs Packet Switching")

section("Comparison Table")
info_table(
    ["Feature", "Circuit Switching", "Packet Switching"],
    [
        [
            "Path setup",
            "Dedicated physical path established before communication",
            "No path setup -- each packet routed independently",
        ],
        [
            "Bandwidth",
            "Fixed, reserved bandwidth for entire call duration",
            "Dynamic -- bandwidth shared among users; used only when sending",
        ],
        [
            "Delay",
            "Constant propagation delay (no queuing after setup)",
            "Variable delay (queuing delay at each router)",
        ],
        [
            "Efficiency",
            "Inefficient -- reserved bandwidth wasted during silence",
            "Efficient -- bandwidth used only when needed",
        ],
        [
            "Failure recovery",
            "Connection breaks if any link fails -- must re-establish",
            "Packets can be re-routed around failed links",
        ],
        [
            "Example",
            "Traditional telephone (PSTN), ISDN",
            "Internet (IP), Frame Relay, ATM",
        ],
    ],
)
br()

# -----------------------------------------------------------------------------
#  Dec2024 Q2(b): IEEE 802.2 LLC Frame
# -----------------------------------------------------------------------------
chap_box("Dec 2024 Q2(b) [4 Marks]: IEEE 802.2 LLC Frame Format")

section("LLC Frame Format")
definition(
    "<b>IEEE 802.2 LLC (Logical Link Control):</b> The upper sublayer of the Data Link Layer. "
    "It provides a common interface to the network layer independent of the underlying MAC "
    "technology. The LLC frame contains DSAP, SSAP, and Control fields."
)

packet_format(
    "IEEE 802.2 LLC Frame",
    [
        ("DSAP", 8),
        ("SSAP", 8),
        ("Control", 8),
        ("Information (Data Payload)", 32),
    ],
)

info_table(
    ["Field", "Size", "Description"],
    [
        [
            "DSAP",
            "8 bits (1 byte)",
            "Destination Service Access Point -- identifies the receiving layer-3 protocol (e.g., 0x42=STP, 0xAA=SNAP, 0x06=IP)",
        ],
        [
            "SSAP",
            "8 bits (1 byte)",
            "Source Service Access Point -- identifies the sending layer-3 protocol",
        ],
        [
            "Control",
            "8 or 16 bits",
            "Frame type: I-frame (8-bit=U-frame, 16-bit=I or S frame). Contains N(S), N(R), P/F bits.",
        ],
        [
            "Information",
            "Variable",
            "Data payload from network layer; absent in supervisory frames",
        ],
    ],
)
br()

# -----------------------------------------------------------------------------
#  Dec2024 Q2(c): Flow Control and Error Control
# -----------------------------------------------------------------------------
chap_box("Dec 2024 Q2(c) [4 Marks]: Flow Control and Error Control in Data Link Layer")

section("Flow Control")
definition(
    "<b>Flow Control:</b> A mechanism to prevent the sender from transmitting data faster "
    "than the receiver can process it. Without flow control, the receiver's buffer may overflow, "
    "causing frame loss."
)
bullet(
    [
        "<b>Stop-and-Wait:</b> Sender transmits one frame and waits for ACK before sending the next. Simple but inefficient (low utilization for long propagation delays).",
        "<b>Sliding Window:</b> Sender can transmit up to W frames before needing an ACK. Window 'slides' as ACKs are received. W = 1 gives Stop-and-Wait. Efficiency = W/(1+2a) for W < 1+2a.",
    ]
)

section("Error Control")
definition(
    "<b>Error Control:</b> Mechanisms to detect and handle transmission errors in data link frames. "
    "Consists of error detection (finding that an error occurred) and error recovery (ARQ retransmission)."
)
bullet(
    [
        "<b>Error Detection:</b> Parity bits (simple, detects single-bit errors), CRC (powerful, detects burst errors), Checksum (IP/UDP/TCP).",
        "<b>ARQ (Automatic Repeat Request):</b> On error detection, receiver sends NACK or no ACK; sender retransmits.",
        "<b>Stop-and-Wait ARQ:</b> One frame in transit; retransmit on timeout or NACK.",
        "<b>Go-Back-N ARQ:</b> Multiple frames; on error, retransmit from error frame onwards.",
        "<b>Selective Reject ARQ:</b> Only retransmit specific errored frame; receiver buffers out-of-order.",
    ]
)
note("See Section 2, Q6 (MST-2 Q6) for detailed GBN and SR ARQ comparison.")
br()

# -----------------------------------------------------------------------------
#  Dec2024 Q2(d): Sliding Window -- Cross-reference
# -----------------------------------------------------------------------------
chap_box("Dec 2024 Q2(d) [10 Marks]: Sliding Window Protocol")
note(
    "This question is fully answered in Section 2, Q8 (MST-2 Q8) with complete definition, "
    "SND.UNA/NXT/WND variables, flowchart diagram, and efficiency formula. Please refer to that section."
)
br()

# -----------------------------------------------------------------------------
#  Dec2024 Q2(e): Go-Back-N for Pipelining -- Cross-reference
# -----------------------------------------------------------------------------
chap_box("Dec 2024 Q2(e) [10 Marks]: Go-Back-N for Pipelining")
note(
    "Go-Back-N ARQ is fully covered in Section 2, Q6 (MST-2 Q6) with definition, sequence diagram, "
    "and comparison table. Pipelining efficiency is covered in MST-2 Q8. Please refer to those sections."
)
br()

# -----------------------------------------------------------------------------
#  Dec2024 Q3(a): Static vs Dynamic Channel Allocation
# -----------------------------------------------------------------------------
chap_box("Dec 2024 Q3(a) [3 Marks]: Static vs Dynamic Channel Allocation")

section("Channel Allocation Methods")
info_table(
    ["Property", "Static Allocation (FDMA/TDMA)", "Dynamic Allocation (ALOHA/CSMA)"],
    [
        [
            "Allocation time",
            "Pre-allocated before transmission",
            "On demand -- allocated when needed",
        ],
        [
            "Waste",
            "Wastes capacity during silence (dedicated but unused)",
            "Efficient -- channel used only when data available",
        ],
        [
            "Collision",
            "No collisions (dedicated sub-channels)",
            "Collisions possible (shared channel)",
        ],
        [
            "Complexity",
            "Simple -- no contention resolution needed",
            "Complex -- requires collision detection/avoidance",
        ],
        [
            "Suitability",
            "Predictable traffic (voice telephony, broadcast)",
            "Bursty traffic (data networks, Internet)",
        ],
    ],
)
br()

# -----------------------------------------------------------------------------
#  Dec2024 Q3(b): 1-persistent vs p-persistent CSMA
# -----------------------------------------------------------------------------
chap_box("Dec 2024 Q3(b) [4 Marks]: 1-Persistent vs p-Persistent CSMA")

section("CSMA Variants")
info_table(
    ["Property", "1-Persistent", "p-Persistent", "Non-Persistent"],
    [
        ["Transmit when idle", "Always (prob=1)", "With probability p", "Always"],
        [
            "When channel busy",
            "Wait, then retransmit immediately when idle",
            "Wait until idle, then transmit with prob p",
            "Wait random time, then resense",
        ],
        [
            "Collision risk",
            "High -- all waiting stations transmit at once",
            "Lower -- controlled by probability p",
            "Lower -- random backoff prevents simultaneous retransmit",
        ],
        [
            "Channel utilization",
            "High at low load; poor at high load",
            "Tunable -- depends on p value",
            "Good at high load",
        ],
        [
            "Example",
            "Original Ethernet (10BASE5)",
            "802.11 uses modified p-persistent",
            "Some cable systems",
        ],
    ],
)
bullet(
    [
        "<b>CSMA/CD (Collision Detection):</b> Used in wired Ethernet. Detects collision while transmitting; sends jam signal; binary exponential backoff. Min frame size = 2*propagation_delay * bit_rate.",
        "<b>CSMA/CA (Collision Avoidance):</b> Used in Wi-Fi (802.11). Cannot detect collisions (hidden node problem). Uses IFS (SIFS, DIFS), random backoff in slots, and ACKs to avoid/confirm delivery.",
    ]
)
br()

# -----------------------------------------------------------------------------
#  Dec2024 Q3(c): FDDI -- Cross-reference
# -----------------------------------------------------------------------------
chap_box("Dec 2024 Q3(c) [4 Marks]: FDDI Features")
note(
    "FDDI is fully covered in Section 3, May-June 2024 Q3(b) with complete definition, "
    "speed, encoding, dual-ring topology, fault tolerance, and distance specifications."
)
br()

# -----------------------------------------------------------------------------
#  Dec2024 Q3(d): Slotted ALOHA
# -----------------------------------------------------------------------------
chap_box("Dec 2024 Q3(d) [10 Marks]: Slotted ALOHA -- Working and Comparison")

section("Slotted ALOHA Working Principle")
definition(
    "<b>Slotted ALOHA:</b> An improvement over Pure ALOHA where time is divided into fixed-length "
    "slots equal to one frame transmission time. Stations are synchronized and can only begin "
    "transmitting at the beginning of a slot. This eliminates the 'partial collision' problem of "
    "Pure ALOHA, effectively halving the vulnerable collision period."
)
bullet(
    [
        "Time is divided into slots of duration = T_frame (one frame transmission time).",
        "All stations are synchronized to slot boundaries (requires global clock).",
        "A station with a frame to send waits until the next slot boundary to transmit.",
        "If collision occurs (multiple stations transmit in same slot), each station waits a random number of slots before retrying.",
        "Vulnerable period = 1 slot (vs. 2 slots for Pure ALOHA).",
    ]
)

section("Slotted ALOHA Sequence Diagram")
seq2 = ed.SequenceDiagram(
    width=CW,
    height=260,
    caption="Fig 4.1: Slotted ALOHA -- 3 stations, slot-based transmission",
)
seq2.actor("s1", "Station 1")
seq2.actor("s2", "Station 2")
seq2.actor("s3", "Station 3")
seq2.actor("ch", "Channel")
seq2.divider("Slot 1: Only Station 1 transmits")
seq2.message("s1", "ch", "Frame [Slot 1 -- SUCCESS]", arrow="solid")
seq2.divider("Slot 2: Station 2 and 3 both transmit -- COLLISION")
seq2.message("s2", "ch", "Frame [Slot 2]", arrow="solid")
seq2.message("s3", "ch", "Frame [Slot 2 -- COLLISION!]", arrow="solid")
seq2.divider("Slot 3: Station 2 retransmits, Station 3 waits")
seq2.message("s2", "ch", "Frame [Slot 3 -- SUCCESS]", arrow="solid")
seq2.divider("Slot 4: Station 3 retransmits")
seq2.message("s3", "ch", "Frame [Slot 4 -- SUCCESS]", arrow="solid")
story.extend(seq2.as_flowable())

section("Throughput Calculations")
code_block("""
 ALOHA THROUGHPUT FORMULAS AND CALCULATIONS:
 =====================================================================
 Pure ALOHA   : S = G * e^(-2G)
 Slotted ALOHA: S = G * e^(-G)

 Where:
   G = average number of frames transmitted per slot (offered load)
   S = average number of successful transmissions per slot (throughput)

 PURE ALOHA maximum:
   dS/dG = e^(-2G) + G*(-2)*e^(-2G) = 0
   -> 1 - 2G = 0 -> G = 0.5
   S_max = 0.5 * e^(-1.0) = 0.5 * 0.3679 = 0.1839 ≈ 18.4%

 SLOTTED ALOHA maximum:
   dS/dG = e^(-G) + G*(-1)*e^(-G) = 0
   -> 1 - G = 0 -> G = 1.0
   S_max = 1.0 * e^(-1.0) = 1.0 * 0.3679 = 0.3679 ≈ 36.8%

 COMPARISON TABLE at different load values:
 G    | Pure ALOHA S = G*e^-2G | Slotted ALOHA S = G*e^-G
 -----|------------------------|---------------------------
 0.1  |  0.082 (8.2%)          |  0.090 (9.0%)
 0.5  |  0.184 (18.4%) <- MAX  |  0.303 (30.3%)
 1.0  |  0.135 (13.5%)         |  0.368 (36.8%) <- MAX
 2.0  |  0.037 (3.7%)          |  0.271 (27.1%)
 3.0  |  0.007 (0.7%)          |  0.149 (14.9%)
""")

section("Pure vs Slotted ALOHA Comparison")
info_table(
    ["Property", "Pure ALOHA", "Slotted ALOHA"],
    [
        [
            "Synchronization",
            "Not required -- transmit anytime",
            "Required -- synchronized slot boundaries",
        ],
        ["Vulnerable period", "2 * T_frame", "1 * T_frame (half of Pure ALOHA)"],
        ["Maximum throughput", "18.4% at G=0.5", "36.8% at G=1.0 (double Pure ALOHA)"],
        ["Throughput formula", "S = G * e^(-2G)", "S = G * e^(-G)"],
        [
            "Complexity",
            "Very simple -- no synchronization",
            "Simple but requires clock synchronization",
        ],
        [
            "Collision types",
            "Full + partial collisions possible",
            "Only full collisions (within a slot)",
        ],
    ],
)
br()

# -----------------------------------------------------------------------------
#  Dec2024 Q3(e): IEEE 802.5 Token Ring Frame + Token Circulation
# -----------------------------------------------------------------------------
chap_box(
    "Dec 2024 Q3(e) [10 Marks]: IEEE 802.5 Token Ring Frame Format and Token Circulation"
)

section("Token Frame Format")
definition(
    "<b>Token Frame:</b> A special 3-byte frame that circulates around the ring when no data "
    "is being transmitted. When a station captures the free token and converts it to a busy token, "
    "it can then transmit a data frame."
)
info_table(
    ["Field", "Size", "Description"],
    [
        [
            "SD (Starting Delimiter)",
            "1 byte",
            "Marks start using signal violations (J and K symbols). Non-data patterns cannot appear in data.",
        ],
        [
            "AC (Access Control)",
            "1 byte",
            "PPP (Priority) T (Token bit -- 0=token, 1=data frame) M (Monitor) RRR (Reservation)",
        ],
        [
            "ED (Ending Delimiter)",
            "1 byte",
            "Marks end of token or frame using signal violations. I-bit indicates intermediate frame.",
        ],
    ],
)

section("Data Frame Format")
packet_format(
    "IEEE 802.5 Token Ring Data Frame",
    [
        ("SD", 8),
        ("AC", 8),
        ("FC", 8),
        ("DA (high 16 bits)", 16),
        ("DA (low 32 bits)", 32),
        ("SA (high 16 bits)", 16),
        ("SA (low 32 bits)", 32),
        ("Data Payload", 32),
        ("FCS", 32),
        ("ED", 8),
        ("FS", 8),
    ],
)
note(
    "The DA and SA fields are each 48 bits (6 bytes). Shown split across rows for the 32-bit diagram. "
    "The Data field is variable length. FCS is 32-bit CRC."
)

section("Token Circulation and Frame Transmission")
bullet(
    [
        "<b>Step 1 -- Wait for token:</b> Station monitors the ring waiting for a free token (T-bit=0 in AC field).",
        "<b>Step 2 -- Capture token:</b> When free token arrives, station changes T-bit from 0 to 1, converting it to a busy token.",
        "<b>Step 3 -- Transmit frame:</b> Station appends its data frame immediately after the busy token and transmits.",
        "<b>Step 4 -- Frame propagates:</b> Frame travels around the ring; destination copies the data and sets A-bit and C-bit in FS field.",
        "<b>Step 5 -- Remove frame:</b> When frame returns to originating station (after full ring traversal), originating station removes it.",
        "<b>Step 6 -- Release token:</b> After frame removal, station releases a new free token to the ring for the next station.",
        "<b>Priority mechanism:</b> AC field contains PPP (priority of current frame) and RRR (reservation for next token). Higher-priority stations can request the token.",
        "<b>Monitor station:</b> One station is designated as Active Monitor. Detects and removes persistently busy tokens; reinjects token if lost.",
    ]
)
br()

# -----------------------------------------------------------------------------
#  Dec2024 Q4(a): Addresses -- Cross-reference
# -----------------------------------------------------------------------------
chap_box("Dec 2024 Q4(a) [3 Marks]: Logical, Physical, and Port Addresses")
note(
    "This question is fully answered in Section 3, May-June 2024 Q4(a) with the complete "
    "comparison table of Physical (MAC), Logical (IP), and Port addresses."
)
br()

# -----------------------------------------------------------------------------
#  Dec2024 Q4(b): IPv4 Fragmentation
# -----------------------------------------------------------------------------
chap_box("Dec 2024 Q4(b) [4 Marks]: IPv4 Fragmentation and Reassembly")

section("IPv4 Fragmentation")
definition(
    "<b>IPv4 Fragmentation:</b> When an IP packet is larger than the MTU (Maximum Transmission Unit) "
    "of a network link, the router splits the packet into smaller fragments. Each fragment has its "
    "own IP header. Fragments are reassembled only at the destination host (not at intermediate routers)."
)
bullet(
    [
        "<b>MTU (Maximum Transmission Unit):</b> Maximum payload size for the data link layer. Ethernet MTU = 1500 bytes.",
        "<b>Identification field:</b> All fragments of the same original packet share the same ID.",
        "<b>Flags field (3 bits):</b> Bit 0 reserved. Bit 1 = DF (Don't Fragment). Bit 2 = MF (More Fragments -- set in all fragments except last).",
        "<b>Fragment Offset (13 bits):</b> Position of this fragment's data in the original packet, in units of 8 bytes.",
        "Reassembly at destination: uses ID + source IP; MF=0 and offset of last fragment gives total original size.",
    ]
)

code_block("""
 IPv4 FRAGMENTATION EXAMPLE:
 =====================================================================
 Original datagram: 4000 bytes total (20 byte IP header + 3980 bytes data)
 Link MTU         : 1500 bytes (Ethernet)
 Max data per frag: 1500 - 20 (IP header) = 1480 bytes

 Fragmentation:
 Fragment 1:
   IP header: 20 bytes
   Data     : 1480 bytes (bytes 0 to 1479 of original data)
   Total    : 1500 bytes
   Flags    : MF=1 (more fragments follow)
   Offset   : 0 / 8 = 0

 Fragment 2:
   IP header: 20 bytes
   Data     : 1480 bytes (bytes 1480 to 2959 of original data)
   Total    : 1500 bytes
   Flags    : MF=1
   Offset   : 1480 / 8 = 185

 Fragment 3:
   IP header: 20 bytes
   Data     : 1020 bytes (bytes 2960 to 3979 -- last fragment)
   Total    : 1040 bytes
   Flags    : MF=0 (last fragment)
   Offset   : 2960 / 8 = 370

 VERIFICATION: 1480 + 1480 + 1020 = 3980 bytes of data (correct!)
""")

tip(
    "Fragment offset is in units of 8 bytes (multiply/divide by 8). "
    "MF=1 means more fragments follow; MF=0 means this is the last fragment. "
    "DF=1 means don't fragment -- router sends ICMP Fragmentation Needed if packet too large. "
    "IPv6 does NOT fragment at routers -- source does PMTU Discovery."
)
br()

# -----------------------------------------------------------------------------
#  Dec2024 Q4(c): IPv4 vs IPv6 -- Cross-reference
# -----------------------------------------------------------------------------
chap_box("Dec 2024 Q4(c) [4 Marks]: IPv4 vs IPv6")
note(
    "IPv4 vs IPv6 is fully covered in Section 3, May-June 2024 Q4(e) with the complete "
    "comparison table (10 features) and IPv4 header packet format diagram."
)
br()

# -----------------------------------------------------------------------------
#  Dec2024 Q4(d): Dijkstra Shortest Path
# -----------------------------------------------------------------------------
chap_box("Dec 2024 Q4(d) [10 Marks]: Dijkstra Shortest Path Algorithm")

section("Graph Definition")
definition(
    "<b>Dijkstra's Algorithm:</b> A greedy algorithm that finds the shortest path from a "
    "source vertex to all other vertices in a weighted graph with non-negative edge weights. "
    "At each step it selects the unvisited vertex with the smallest known distance."
)

section(
    "Given Graph: A-B:6, A-C:7, B-C:6, B-D:2, B-E:5, C-D:3, C-F:6, D-F:5, D-E:4, E-F:3, F-G:8, E-G:7"
)

# Dijkstra graph: manual x,y placement for clear 2D topology
# Layout: A(left) -> B/C(center-left) -> D(center) -> E/F(center-right) -> G(right)
# CW ~ 493pt; keep all nodes inside with margin
net3 = ed.NetworkDiagram(
    width=CW, height=240, caption="Fig 4.2: Weighted graph for Dijkstra algorithm"
)
net3.node("A", "A", x=55, y=120, kind="generic")
net3.node("B", "B", x=165, y=175, kind="generic")
net3.node("C", "C", x=165, y=65, kind="generic")
net3.node("D", "D", x=275, y=120, kind="generic")
net3.node("E", "E", x=375, y=175, kind="generic")
net3.node("F", "F", x=375, y=65, kind="generic")
net3.node("G", "G", x=460, y=120, kind="generic")
net3.link("A", "B", label="6")
net3.link("A", "C", label="7")
net3.link("B", "C", label="6")
net3.link("B", "D", label="2")
net3.link("B", "E", label="5")
net3.link("C", "D", label="3")
net3.link("C", "F", label="6")
net3.link("D", "F", label="5")
net3.link("D", "E", label="4")
net3.link("E", "F", label="3")
net3.link("F", "G", label="8")
net3.link("E", "G", label="7")
story.extend(net3.as_flowable())

section("Dijkstra Step-by-Step Trace")
code_block("""
 DIJKSTRA'S ALGORITHM -- Source: A
 =====================================================================
 Initial: A=0, B=inf, C=inf, D=inf, E=inf, F=inf, G=inf
 Visited: {}

 Step 1 -- Visit A (dist=0):
   Update neighbors: B=min(inf, 0+6)=6, C=min(inf, 0+7)=7
   Visited: {A}      Distances: A=0, B=6, C=7, D=inf, E=inf, F=inf, G=inf

 Step 2 -- Visit B (dist=6, smallest unvisited):
   Update neighbors:
     C=min(7, 6+6)=7 (no change), D=min(inf,6+2)=8, E=min(inf,6+5)=11
   Visited: {A,B}    Distances: A=0, B=6, C=7, D=8, E=11, F=inf, G=inf

 Step 3 -- Visit C (dist=7):
   Update neighbors:
     B already visited. D=min(8, 7+3)=10? No, 7+3=10 > 8 -> no change
     F=min(inf, 7+6)=13
   Visited: {A,B,C}  Distances: A=0, B=6, C=7, D=8, E=11, F=13, G=inf

 Step 4 -- Visit D (dist=8):
   Update neighbors:
     B,C already visited. E=min(11, 8+4)=12? No, 8+4=12 > 11 -> no change
     F=min(13, 8+5)=13? 8+5=13, tie -> no change
   Visited: {A,B,C,D} Distances: A=0, B=6, C=7, D=8, E=11, F=13, G=inf

 Step 5 -- Visit E (dist=11):
   Update neighbors:
     B,D already visited. F=min(13, 11+3)=14? No, 14 > 13 -> no change
     G=min(inf, 11+7)=18
   Visited: {A,B,C,D,E} Distances: A=0, B=6, C=7, D=8, E=11, F=13, G=18

 Step 6 -- Visit F (dist=13):
   Update neighbors:
     G=min(18, 13+8)=21? No, 21 > 18 -> no change
   Visited: {A,B,C,D,E,F} Distances: A=0, B=6, C=7, D=8, E=11, F=13, G=18

 Step 7 -- Visit G (dist=18): DONE -- all nodes visited.

 =====================================================================
 SHORTEST PATH TABLE:
 Node | Shortest Distance from A | Path
 -----|--------------------------|------------------
  A   |          0               | A
  B   |          6               | A -> B
  C   |          7               | A -> C
  D   |          8               | A -> B -> D
  E   |         11               | A -> B -> E
  F   |         13               | A -> B -> D -> F  (or A->C->F, same cost)
  G   |         18               | A -> B -> E -> G  ***

 ANSWER: Shortest path A to G = A -> B -> E -> G, total cost = 18
         (6 + 5 + 7 = 18)
""")

highlight(
    "<b>ANSWER:</b> Shortest path from A to G is <b>A -&gt; B -&gt; E -&gt; G</b>, "
    "total cost = 6 + 5 + 7 = <b>18</b>. "
    "Path via F: A-&gt;B-&gt;D-&gt;F-&gt;G = 6+2+5+8 = 21 (longer). "
    "Path via C: A-&gt;C-&gt;D-&gt;E-&gt;G = 7+3+4+7 = 21 (longer)."
)
br()

# -----------------------------------------------------------------------------
#  Dec2024 Q4(e): NetID/HostID Class C + IP Calculations
# -----------------------------------------------------------------------------
chap_box("Dec 2024 Q4(e) [10 Marks]: NetID/HostID for Class C + IP Address Analysis")

section("Class C Address Structure")
definition(
    "<b>Class C:</b> First 3 bits of address = 110. Network bits = 24, Host bits = 8. "
    "Range: 192.0.0.0 to 223.255.255.255. Default mask: 255.255.255.0 (/24). "
    "Maximum hosts per network: 2^8 - 2 = 254 (subtract network and broadcast addresses)."
)

section("IP Address Analysis")
code_block("""
 IP ADDRESS ANALYSIS:
 =====================================================================

 Address: 136.1.3.2
 First octet: 136
 Binary first octet: 10001000
 First two bits: 10 -> CLASS B (128.0.0.0 to 191.255.255.255)

 CLASS B analysis:
   Network bits: 16     Host bits: 16
   NetID: 136.1.0.0     HostID: 0.3.2 -> 3.2
   Subnet mask: 255.255.0.0 (/16)
   Network address: 136.1.0.0
   Broadcast: 136.1.255.255
   Host range: 136.1.0.1 to 136.1.255.254

 =====================================================================

 Address: 100.0.0.0
 First octet: 100
 Binary first octet: 01100100
 First bit: 0 -> CLASS A (0.0.0.0 to 127.255.255.255)

 CLASS A analysis:
   Network bits: 8     Host bits: 24
   NetID: 100.0.0.0    HostID: 0.0.0 (this IS the network address)
   Subnet mask: 255.0.0.0 (/8)
   Network address: 100.0.0.0
   Broadcast: 100.255.255.255
   Host range: 100.0.0.1 to 100.255.255.254
   Max hosts: 2^24 - 2 = 16,777,214

 =====================================================================

 Class C example: 200.45.67.89
 First octet: 200 (binary: 11001000) -> first 3 bits = 110 -> CLASS C
   NetID: 200.45.67.0    HostID: 89
   Subnet mask: 255.255.255.0 (/24)
   Network: 200.45.67.0
   Broadcast: 200.45.67.255
   Host range: 200.45.67.1 to 200.45.67.254
   Max hosts: 2^8 - 2 = 254
""")

section("Class Summary Table")
info_table(
    [
        "Class",
        "First Bits",
        "First Octet Range",
        "Net Bits",
        "Host Bits",
        "Max Networks",
        "Max Hosts/Net",
    ],
    [
        ["A", "0", "1 - 126", "8", "24", "126 (2^7-2)", "16,777,214 (2^24-2)"],
        ["B", "10", "128 - 191", "16", "16", "16,384 (2^14)", "65,534 (2^16-2)"],
        ["C", "110", "192 - 223", "24", "8", "2,097,152 (2^21)", "254 (2^8-2)"],
        ["D", "1110", "224 - 239", "N/A (multicast)", "N/A", "N/A", "N/A"],
        ["E", "11110", "240 - 255", "N/A (reserved)", "N/A", "N/A", "N/A"],
    ],
)
br()

# -----------------------------------------------------------------------------
#  Dec2024 Q5(a): Two Internetworking Devices -- Cross-reference
# -----------------------------------------------------------------------------
chap_box("Dec 2024 Q5(a) [3 Marks]: Two Internetworking Devices")
note(
    "Internetworking devices are covered in Section 1, Q1 (MST-3 Q1) and Section 3, Q5(e) "
    "(May-June 2024 Q5(e)) with complete tables and network diagram."
)
br()

# -----------------------------------------------------------------------------
#  Dec2024 Q5(b): Congestion Control Techniques -- Cross-reference
# -----------------------------------------------------------------------------
chap_box("Dec 2024 Q5(b) [4 Marks]: Congestion Control Techniques")
note(
    "Congestion control is fully covered in Section 3, May-June 2024 Q4(d) with open-loop "
    "(leaky bucket, token bucket, admission control) and closed-loop (choke packets, ECN, "
    "TCP slow start, AIMD, fast retransmit) techniques, plus a comprehensive comparison table."
)
br()

# -----------------------------------------------------------------------------
#  Dec2024 Q5(c): ACK and Sequence Numbers in TCP
# -----------------------------------------------------------------------------
chap_box("Dec 2024 Q5(c) [4 Marks]: ACK and Sequence Numbers in TCP")

section("TCP Sequence and Acknowledgement Numbers")
definition(
    "<b>Sequence Number (32 bits):</b> Identifies the byte position of the first data byte "
    "in the current TCP segment within the byte stream. TCP treats the data as a continuous "
    "stream of bytes, numbered from the initial sequence number (ISN) negotiated during the "
    "3-way handshake.<br/>"
    "<b>Acknowledgement Number (32 bits):</b> The sequence number of the NEXT byte the "
    "receiver expects to receive from the sender. Cumulative ACK -- acknowledges all bytes "
    "up to (but not including) this number."
)
bullet(
    [
        "Sequence numbers prevent duplicates and enable in-order delivery.",
        "ACK numbers implement cumulative positive acknowledgement.",
        "Initial Sequence Number (ISN) is randomly selected during SYN (prevents attacks).",
        "Each byte of data 'consumes' one sequence number.",
        "SYN and FIN control bits each consume one sequence number.",
    ]
)

code_block("""
 TCP SEQUENCE/ACK NUMBER EXAMPLE:
 =====================================================================
 Assume TCP connection established. ISN = 100.

 Sender A has 150 bytes of data to send (bytes 101-250):

 Sender A -> Receiver B:
   SEQ = 101  (first byte of this segment)
   Data: bytes 101 to 150 (50 bytes)
   Next SEQ = 151

 Receiver B -> Sender A:
   ACK = 151  (next expected byte = 101+50 = 151)
   (B has received bytes 101-150 correctly)

 Sender A -> Receiver B:
   SEQ = 151  (next segment starts here)
   Data: bytes 151 to 250 (100 bytes)

 Receiver B -> Sender A:
   ACK = 251  (next expected byte = 151+100 = 251)
   (B has received bytes 101-250 correctly)

 If a segment is lost:
   Receiver keeps sending ACK = 151 (duplicate ACKs)
   Sender retransmits from SEQ = 151
   This is the Fast Retransmit mechanism (3 dup ACKs -> retransmit)
""")
br()

# -----------------------------------------------------------------------------
#  Dec2024 Q5(d): UDP Frame Format -- Cross-reference
# -----------------------------------------------------------------------------
chap_box("Dec 2024 Q5(d) [10 Marks]: UDP Frame Format and Field Explanation")
note(
    "UDP header format is fully covered in Section 1, Q4 (MST-3 Q4) with the packet_format "
    "diagram and detailed field-by-field explanation of all 4 fields (Source Port, Dest Port, "
    "Length, Checksum)."
)
br()

# -----------------------------------------------------------------------------
#  Dec2024 Q5(e): Throughput, Delay, QoS Parameters
# -----------------------------------------------------------------------------
chap_box("Dec 2024 Q5(e) [10 Marks]: Throughput, Delay, and QoS Parameters")

section("Throughput")
definition(
    "<b>Throughput:</b> The actual rate at which data is successfully delivered from source "
    "to destination over a network connection. Measured in bits per second (bps). Throughput "
    "is always less than or equal to the bandwidth (channel capacity) due to overhead, "
    "errors, retransmissions, and protocol efficiency."
)
bullet(
    [
        "<b>Formula:</b> Throughput = (Total data transferred) / (Total time for transfer)",
        "<b>Effective throughput:</b> Accounts for overhead -- Throughput_eff = (Data_bits / (Data_bits + Header_bits)) x Raw_throughput",
        "<b>Throughput vs Bandwidth:</b> Bandwidth = maximum theoretical capacity. Throughput = actual achieved rate (always <= bandwidth).",
        "<b>Factors limiting throughput:</b> Congestion, packet loss, latency (RTT), window size (TCP), interference, protocol overhead.",
    ]
)

section("Delay (Latency)")
definition(
    "<b>Delay (Latency):</b> The time taken for a packet to travel from source to destination. "
    "Total delay is the sum of four components."
)

info_table(
    ["Delay Component", "Formula", "Cause", "Typical Value"],
    [
        [
            "Propagation Delay",
            "d_prop = d / v (d=distance, v=propagation speed ~2x10^8 m/s)",
            "Speed of signal in medium -- cannot be reduced",
            "5 ms/1000 km (fiber)",
        ],
        [
            "Transmission Delay",
            "d_trans = L / R (L=packet size, R=link rate)",
            "Time to push bits onto the wire -- depends on link speed",
            "0.12 ms for 1500B at 100Mbps",
        ],
        [
            "Queuing Delay",
            "Variable -- depends on traffic intensity L*a/R (a=avg arrival rate)",
            "Waiting in router buffer for link to be free",
            "0-100s ms under congestion",
        ],
        [
            "Processing Delay",
            "Fixed per router (typically microseconds)",
            "Router checks header, looks up routing table, error check",
            "< 1 ms on modern routers",
        ],
    ],
)

section("QoS Parameters for Applications")
info_table(
    ["Application", "Bandwidth Needed", "Max Delay", "Max Jitter", "Max Packet Loss"],
    [
        [
            "VoIP (voice call)",
            "64 kbps - 128 kbps per call",
            "< 150 ms one-way",
            "< 30 ms",
            "< 1%",
        ],
        [
            "Video Conferencing",
            "1-10 Mbps (HD)",
            "< 150 ms one-way",
            "< 30 ms",
            "< 0.1%",
        ],
        [
            "Video Streaming",
            "1-25 Mbps (buffered)",
            "< 5 seconds (buffering OK)",
            "High tolerance (buffered)",
            "< 0.1%",
        ],
        [
            "File Transfer (FTP)",
            "As much as available",
            "No strict limit",
            "No limit",
            "0% (TCP retransmits)",
        ],
        [
            "Email (SMTP)",
            "Low (kbps)",
            "Seconds to minutes OK",
            "No limit",
            "0% (TCP retransmits)",
        ],
        ["Online Gaming", "1-10 Mbps", "< 50-100 ms (competitive)", "< 20 ms", "< 1%"],
    ],
)

tip(
    "QoS parameters: Bandwidth (rate), Delay (latency), Jitter (delay variation), "
    "Packet Loss (%), Availability (uptime %). "
    "VoIP is most sensitive to jitter (causes choppy audio). "
    "FTP is most sensitive to packet loss (TCP retransmits, throughput degrades). "
    "Video streaming can tolerate higher jitter due to client-side buffering."
)
br()


# =============================================================================
#  SECTION 5: MAY-JUNE 2025 ESE (IT-411)
# =============================================================================
part_box("SECTION 5 -- MAY-JUNE 2025 ESE QUESTIONS & ANSWERS")

# -----------------------------------------------------------------------------
#  Q1(a) [3 Marks]: Types of computer networks based on size
# -----------------------------------------------------------------------------
chap_box("Q1(a) [3 Marks]: Types of Computer Networks Based on Size")
section("Types of Networks by Scale")
definition(
    "Computer networks are categorized based on their geographic span, ownership, and scale: "
    "<b>LAN</b> (Local Area Network) covers a small area like a room/building; "
    "<b>MAN</b> (Metropolitan Area Network) covers a town or city; "
    "<b>WAN</b> (Wide Area Network) spans countries, continents, or the entire globe."
)
info_table(
    ["Network Type", "Geographic Span", "Ownership", "Data Rate & Error Rate"],
    [
        ["<b>LAN</b> (Local Area Network)", "10 m to 1 km (room, office, building)", "Private (Single organization)", "High speed (100Mbps-10Gbps), Low error rate"],
        ["<b>MAN</b> (Metropolitan Area Network)", "5 km to 50 km (city, campus)", "Private or Public (Cable TV, City Gov)", "Moderate speed (100Mbps-1Gbps), Moderate error rate"],
        ["<b>WAN</b> (Wide Area Network)", "100 km to 10,000+ km (country, globe)", "Usually leased/public (Telecom, Internet)", "Lower speed (Mbps to Gbps), Higher error rate due to distance"]
    ]
)
br()

# -----------------------------------------------------------------------------
#  Q1(b), (c), (d), (e): Cross-references
# -----------------------------------------------------------------------------
chap_box("Q1(b) [4 Marks]: Network Topologies")
note("Network topologies are fully discussed in Section 4, Dec 2024 ESE, Q1(b) with comparison table.")
sp(10)

chap_box("Q1(c) [4 Marks]: Network Comparisons (Broadcast/P2P, Connection-Oriented/Connectionless)")
subsection("i. Broadcast vs. Point-to-Point Networks")
note("See Section 3, May-June 2024 ESE, Q1(a) for the comparison table.")
subsection("ii. Connection-Oriented vs. Connectionless Services")
note("See Section 3, May-June 2024 ESE, Q1(c) for the comparison table.")
sp(10)

chap_box("Q1(d) [10 Marks]: ARPANET and TCP/IP")
subsection("i. ARPANET")
note("See Section 4, Dec 2024 ESE, Q1(d) for detailed historical architecture.")
subsection("ii. TCP/IP Protocol Suite")
note("See Section 2, MST-2, Q4 for full architecture stack and protocols.")
sp(10)

chap_box("Q1(e) [10 Marks]: ISO/OSI Model Architecture & connectivity using PDU")
note("See Section 3, May-June 2024 ESE, Q1(d) for the 7-layer stack architecture and PDU definitions.")
br()

# -----------------------------------------------------------------------------
#  Q2(a), (b), (c), (d), (e)
# -----------------------------------------------------------------------------
chap_box("Q2(a) [3 Marks]: Circuit vs. Packet Switching")
note("See Section 2, MST-2, Q5 & Section 3, Q2(b) for the complete comparison tables.")
sp(10)

chap_box("Q2(b) [4 Marks]: Error Detection and Correction Techniques")
note("See Section 3, May-June 2024 ESE, Q2(d) for details on Parity, CRC (with worked example), and Hamming Code.")
sp(10)

chap_box("Q2(c) [4 Marks]: Flow Control and Error Control in Data Link Layer")
section("Flow Control and Error Control")
definition(
    "<b>Flow Control:</b> A mechanism that prevents the sender from overwhelming the receiver with data "
    "by coordinating the transmission rate. <i>Example:</i> <b>Stop-and-Wait</b> or <b>Sliding Window</b>.<br/><br/>"
    "<b>Error Control:</b> A mechanism to detect and correct errors (corrupted/lost frames) during transmission. "
    "<i>Example:</i> <b>ARQ (Automatic Repeat Request)</b> schemes (Stop-and-Wait ARQ, Go-Back-N, Selective Repeat)."
)
body(
    "<b>Justification of Need:</b><br/>"
    "1. <b>Buffer Overflow Prevention:</b> Receivers have limited buffer capacity and processing speeds. "
    "Flow control ensures that the sender does not send data faster than the receiver can consume it.<br/>"
    "2. <b>Transmission Reliability:</b> Physical communication media are noisy and error-prone. Error control "
    "guarantees that all frames are eventually delivered error-free and in the correct order."
)
sp(10)

chap_box("Q2(d) [10 Marks]: Working of Sliding Window Protocol")
note("See Section 2, MST-2, Q8 for sliding window details and flowchart.")
sp(10)

chap_box("Q2(e) [10 Marks]: Go-Back-N ARQ Protocol")
note("See Section 2, MST-2, Q6 for Go-Back-N description, window calculations, and sequence diagram.")
br()

# -----------------------------------------------------------------------------
#  Q3(a) [3 Marks]: Static vs. Dynamic Channel Allocation
# -----------------------------------------------------------------------------
chap_box("Q3(a) [3 Marks]: Static vs. Dynamic Channel Allocation")
section("Channel Allocation Schemes")
definition(
    "<b>Channel Allocation</b> determines how a shared communication medium is shared among multiple competing stations. "
    "In <b>static allocation</b>, capacity is partitioned into fixed portions, whereas in <b>dynamic allocation</b>, "
    "the channel is assigned on-demand dynamically."
)
info_table(
    ["Property", "Static Channel Allocation", "Dynamic Channel Allocation"],
    [
        ["<b>Basic Concept</b>", "Channel is divided into fixed slots using FDM, TDM, or CDM.", "Channel is allocated on-demand as stations have packets to send."],
        ["<b>Efficiency</b>", "Poor for bursty traffic (idle stations waste bandwidth).", "High for bursty traffic (bandwidth is utilized as needed)."],
        ["<b>Delay</b>", "Fixed delay (must wait for assigned slot, but no collision).", "Variable delay (depends on collision probability and traffic)."],
        ["<b>Examples</b>", "FDMA, TDMA, CDMA in cellular systems.", "ALOHA, CSMA, CSMA/CD, CSMA/CA in LANs."]
    ]
)
sp(10)

chap_box("Q3(b) [4 Marks]: 1-persistent and p-persistent CSMA")
note("See Section 3, May-June 2024 ESE, Q3(c) for CSMA persistence variants table.")
sp(10)

chap_box("Q3(c) [4 Marks]: FDDI Features and Importance")
note("See Section 3, May-June 2024 ESE, Q3(b) for dual ring counter-rotating ring details.")
sp(10)

chap_box("Q3(d) [10 Marks]: Slotted ALOHA Working and Comparison")
note("See Section 3, May-June 2024 ESE, Q3(e) for formulas, throughput, and sequence diagrams.")
sp(10)

chap_box("Q3(e) [10 Marks]: IEEE 802.4 Frame Format & Token Circulation")
note("See Section 3, May-June 2024 ESE, Q3(d) for Token Bus frame fields and token passing logic.")
br()

# -----------------------------------------------------------------------------
#  Q4(a) [3 Marks]: Unicast vs. Multicast Routing Protocols
# -----------------------------------------------------------------------------
chap_box("Q4(a) [3 Marks]: Unicast vs. Multicast Routing Protocols")
section("Routing Paradigms")
definition(
    "<b>Unicast Routing:</b> Directs traffic from a single source to a single specific destination (one-to-one). "
    "<b>Multicast Routing:</b> Directs traffic from a single source to a group of registered destinations (one-to-many)."
)
info_table(
    ["Feature", "Unicast Routing Protocols", "Multicast Routing Protocols"],
    [
        ["<b>Transmission</b>", "One-to-One (Single recipient).", "One-to-Many (Group of registered recipients)."],
        ["<b>Path Construction</b>", "Builds a shortest-path tree from source to destination.", "Builds a spanning tree (Source-based or Shared group tree)."],
        ["<b>Group Management</b>", "No group memberships required.", "Uses IGMP/MLD to manage active group memberships on routers."],
        ["<b>Protocols</b>", "RIP (Distance Vector), OSPF (Link State), BGP (Path Vector).", "DVMRP, MOSPF, PIM (Protocol Independent Multicast)."]
    ]
)
sp(10)

# -----------------------------------------------------------------------------
#  Q4(b), (c): Cross-references
# -----------------------------------------------------------------------------
chap_box("Q4(b) [4 Marks]: Fragmentation and Reassembly in IPv4")
note("See Section 4, Dec 2024 ESE, Q4(b) for fragmentation examples and offsets.")
sp(10)

chap_box("Q4(c) [4 Marks]: Compare IPv4 and IPv6")
note("See Section 3, May-June 2024 ESE, Q4(e) for IPv4 vs IPv6 comparison table.")
sp(10)

# -----------------------------------------------------------------------------
#  Q4(d) [10 Marks]: Dijkstra Shortest Path (New Graph)
# -----------------------------------------------------------------------------
chap_box("Q4(d) [10 Marks]: Dijkstra Shortest Path Algorithm (A to C)")
section("New Given Graph")
body(
    "<b>Vertices:</b> A, B, C, D, E, F<br/>"
    "<b>Edges & Weights:</b> A-C: 2, A-B: 1, A-F: 4, C-D: 2, B-D: 8, D-E: 3, E-F: 6, B-F: 5"
)

# NetworkDiagram with manual coordinate layout for 2D topology
net4 = ed.NetworkDiagram(
    width=CW, height=200, caption="Fig 5.1: Weighted graph for May-June 2025 Dijkstra problem"
)
net4.node("A", "A", x=55,  y=100, kind="generic")
net4.node("B", "B", x=165, y=160, kind="generic")
net4.node("C", "C", x=165, y=40,  kind="generic")
net4.node("D", "D", x=275, y=40,  kind="generic")
net4.node("F", "F", x=275, y=160, kind="generic")
net4.node("E", "E", x=385, y=100, kind="generic")
net4.link("A", "B", label="1")
net4.link("A", "C", label="2")
net4.link("A", "F", label="4")
net4.link("C", "D", label="2")
net4.link("B", "D", label="8")
net4.link("D", "E", label="3")
net4.link("E", "F", label="6")
net4.link("B", "F", label="5")
story.extend(net4.as_flowable())

subsection("Dijkstra Step-by-Step Trace (Source: A)")
code_block("""
 DIJKSTRA'S ALGORITHM -- Source: A
 =====================================================================
 Initial: A=0, B=inf, C=inf, D=inf, E=inf, F=inf
 Visited: {}

 Step 1 -- Visit A (dist=0):
   Update neighbors:
     B = min(inf, 0+1) = 1
     C = min(inf, 0+2) = 2
     F = min(inf, 0+4) = 4
   Visited: {A}       Distances: A=0, B=1, C=2, D=inf, E=inf, F=4

 Step 2 -- Visit B (dist=1, smallest unvisited):
   Update neighbors:
     D = min(inf, 1+8) = 9
     F = min(4, 1+5) = 4 (no change)
   Visited: {A, B}    Distances: A=0, B=1, C=2, D=9, E=inf, F=4

 Step 3 -- Visit C (dist=2):
   Update neighbors:
     D = min(9, 2+2) = 4
   Visited: {A, B, C}  Distances: A=0, B=1, C=2, D=4, E=inf, F=4

 Step 4 -- Visit D (dist=4):
   Update neighbors:
     E = min(inf, 4+3) = 7
   Visited: {A, B, C, D} Distances: A=0, B=1, C=2, D=4, E=7, F=4

 Step 5 -- Visit F (dist=4):
   Update neighbors:
     E = min(7, 4+6) = 7 (no change)
   Visited: {A, B, C, D, F} Distances: A=0, B=1, C=2, D=4, E=7, F=4

 Step 6 -- Visit E (dist=7):
   No unvisited neighbors left.
   Visited: {A, B, C, D, F, E}
""")

subsection("Shortest Path Iterations Summary Table")
info_table(
    ["Iteration", "Visited Node", "A", "B", "C", "D", "E", "F"],
    [
        ["Initial", "-", "0", "inf", "inf", "inf", "inf", "inf"],
        ["1", "A", "0 (perm)", "1 (parent A)", "2 (parent A)", "inf", "inf", "4 (parent A)"],
        ["2", "B", "0 (perm)", "1 (perm)", "2 (parent A)", "9 (parent B)", "inf", "4 (parent A)"],
        ["3", "C", "0 (perm)", "1 (perm)", "2 (perm)", "4 (parent C)", "inf", "4 (parent A)"],
        ["4", "D", "0 (perm)", "1 (perm)", "2 (perm)", "4 (perm)", "7 (parent D)", "4 (parent A)"],
        ["5", "F", "0 (perm)", "1 (perm)", "2 (perm)", "4 (perm)", "7 (parent D)", "4 (perm)"],
        ["6", "E", "0 (perm)", "1 (perm)", "2 (perm)", "4 (perm)", "7 (perm)", "4 (perm)"],
    ]
)
body(
    "<b>Shortest path from A to C:</b> A &rarr; C directly<br/>"
    "<b>Shortest cost from A to C:</b> <b>2</b>"
)
sp(10)

chap_box("Q4(d) OR [10 Marks]: NetID/HostID Class A & IP Addressing Problems")
section("Part 1: Class A NetID and HostID")
definition(
    "<b>Class A Structure:</b> Class A IP addresses allocate <b>8 bits</b> for the Network ID (NetID) "
    "and <b>24 bits</b> for the Host ID (HostID).<br/>"
    "<b>NetID Range:</b> 1.0.0.0 to 126.0.0.0 (0 and 127 are reserved; 127 is for loopback testing).<br/>"
    "<b>Total Networks:</b> 126 usable networks.<br/>"
    "<b>Hosts per Network:</b> 2^24 - 2 = 16,777,214 usable host addresses per Class A network."
)

section("Part 2: IP Address 254.31.8.2")
body(
    "The first octet is <b>254</b>.<br/>"
    "IP Address class ranges:<br/>"
    "Class A: 1-126, Class B: 128-191, Class C: 192-223, Class D (Multicast): 224-239, Class E (Experimental): 240-255.<br/>"
    "Therefore, <b>254.31.8.2 belongs to Class E</b>."
)

section("Part 3: IP Address 172.4.0.0")
body(
    "The first octet is <b>172</b>, which falls in the Class B range (128-191).<br/>"
    "In Class B, the first two octets represent the NetID.<br/>"
    "1. <b>NetID:</b> <b>172.4</b> (or 172.4.0.0/16)<br/>"
    "2. <b>Network Address Range:</b> <b>172.4.0.0 to 172.4.255.255</b>"
)
br()

# -----------------------------------------------------------------------------
#  Q5(a), (b), (c), (d), (e)
# -----------------------------------------------------------------------------
chap_box("Q5(a) [3 Marks]: Internetworking Devices")
note("See Section 1 (MST-3), Q1 & Section 3, Q5(e) for bridge, router, hub, switch, and gateway comparison.")
sp(10)

chap_box("Q5(b) [4 Marks]: Congestion Control Techniques")
note("See Section 3, May-June 2024 ESE, Q4(d) for open-loop and closed-loop congestion control classification.")
sp(10)

chap_box("Q5(c) [4 Marks]: Integrated vs. Differentiated Services")
note("See Section 1, MST-3, Q2 for IntServ vs DiffServ details.")
sp(10)

chap_box("Q5(d) [10 Marks]: UDP Frame Format and Fields")
note("See Section 1, MST-3, Q4 for the 32-bit aligned packet format diagram and field explanations.")
sp(10)

chap_box("Q5(e) [10 Marks]: Performance Metrics (Throughput/Delay) and QoS")
section("Network Performance Metrics")
definition(
    "<b>Throughput:</b> The actual rate at which data is successfully delivered over a communication channel, "
    "measured in bits per second (bps, kbps, Mbps). It is bounded by channel bandwidth and degraded by overhead and collisions.<br/><br/>"
    "<b>Delay (Latency):</b> The total time taken for a packet to travel from the sender to the receiver. "
    "Delay consists of four components: "
    "Total Delay = Processing Delay + Queuing Delay + Transmission Delay + Propagation Delay"
)
body(
    "<b>Components of Latency:</b><br/>"
    "1. <b>Processing Delay (T_proc):</b> Time spent by routers checking headers and routes.<br/>"
    "2. <b>Queuing Delay (T_queue):</b> Time the packet spends waiting in router queues before transmission.<br/>"
    "3. <b>Transmission Delay (T_trans):</b> Time to push packet bits onto the link. T_trans = Packet Size (L) / Bandwidth (R).<br/>"
    "4. <b>Propagation Delay (T_prop):</b> Time for a bit to travel through the physical medium. T_prop = Distance (d) / Propagation Speed (s)."
)
section("Quality of Service (QoS) Parameters")
body(
    "QoS is the ability of a network to provide better service to selected network traffic. The five key QoS parameters are:<br/>"
    "1. <b>Bandwidth:</b> Max data rate supported by the link.<br/>"
    "2. <b>Delay (Latency):</b> Time for a packet to reach the destination.<br/>"
    "3. <b>Jitter:</b> The variance in packet arrival times (delay variation). Crucial for real-time applications like VoIP.<br/>"
    "4. <b>Packet Loss:</b> Percentage of packets dropped due to congestion or corruption.<br/>"
    "5. <b>Availability:</b> The uptime percentage of network resources."
)
br()


# =============================================================================
#  SECTION 6: QUICK FORMULA REFERENCE
# =============================================================================
part_box("SECTION 6 -- QUICK FORMULA AND FACT REFERENCE")

chap_box("Key Formulas for Exam")

section("ALOHA Throughput Formulas")
highlight(
    "<b>Pure ALOHA:</b>  S = G * e^(-2G)  -- Maximum 18.4% at G = 0.5<br/>"
    "<b>Slotted ALOHA:</b>  S = G * e^(-G)  -- Maximum 36.8% at G = 1.0<br/>"
    "Where G = offered load (frames/slot), S = throughput (successful frames/slot)"
)

section("ARQ Window and Efficiency")
highlight(
    "<b>Stop-and-Wait efficiency:</b>  eta = 1 / (1 + 2a)  where a = T_prop / T_frame<br/>"
    "<b>Sliding Window efficiency:</b>  eta = W / (1 + 2a)  for W &lt; 1 + 2a<br/>"
    "<b>Go-Back-N window:</b>  W_max = 2^n - 1  (n = sequence number bits)<br/>"
    "<b>Selective Repeat window:</b>  W_max = 2^(n-1)<br/>"
    "<b>Full efficiency condition:</b>  W &gt;= 1 + 2a"
)

section("IP Addressing Formulas")
highlight(
    "<b>Usable hosts per subnet:</b>  H = 2^h - 2  (h = host bits; subtract network and broadcast)<br/>"
    "<b>Number of subnets:</b>  N = 2^s  (s = borrowed subnet bits; some subtract 2 for old rules)<br/>"
    "<b>Fragment offset:</b>  Offset = (byte position of fragment start) / 8<br/>"
    "<b>Class A:</b> First octet 1-126 (/8). <b>Class B:</b> 128-191 (/16). <b>Class C:</b> 192-223 (/24)<br/>"
    "<b>CIDR /26:</b> mask=255.255.255.192, 64 addresses, 62 hosts<br/>"
    "<b>CIDR /27:</b> mask=255.255.255.224, 32 addresses, 30 hosts"
)

section("TCP Congestion Control")
highlight(
    "<b>Slow Start:</b> cwnd doubles each RTT until ssthresh<br/>"
    "<b>Congestion Avoidance (AIMD):</b> cwnd += 1 MSS per RTT<br/>"
    "<b>On timeout:</b> ssthresh = cwnd/2, cwnd = 1 MSS, restart slow start<br/>"
    "<b>On 3 dup ACKs (fast retransmit):</b> ssthresh = cwnd/2, cwnd = ssthresh (fast recovery)<br/>"
    "<b>TCP throughput (approx):</b> Throughput = (0.75 * W * MSS) / RTT"
)

section("Dijkstra Shortest Path")
highlight(
    "<b>Graph:</b> A-B:6, A-C:7, B-C:6, B-D:2, B-E:5, C-D:3, C-F:6, D-F:5, D-E:4, E-F:3, F-G:8, E-G:7<br/>"
    "<b>Shortest path A to G: A -&gt; B -&gt; E -&gt; G, cost = 6+5+7 = 18</b><br/>"
    "All distances from A: B=6, C=7, D=8, E=11, F=13, G=18"
)

section("CRC Generation and Check")
highlight(
    "<b>CRC Generation:</b> Append r zeros to data (r = degree of generator). Divide by G(x). Append remainder to data.<br/>"
    "<b>CRC Check:</b> Divide received data by G(x). If remainder = 0, no error detected.<br/>"
    "<b>Example:</b> Data=1101, G=1011 (degree 3). Augmented: 1101000. Remainder=001. Transmitted: 1101001."
)

section("OSI vs TCP/IP Quick Reference")
info_table(
    ["OSI Layer", "Name", "PDU", "TCP/IP Layer", "Key Protocols"],
    [
        ["7", "Application", "Data", "Application", "HTTP, FTP, DNS, SMTP, SSH, DHCP"],
        ["6", "Presentation", "Data", "Application", "SSL/TLS, JPEG, MPEG"],
        ["5", "Session", "Data", "Application", "RPC, NetBIOS"],
        ["4", "Transport", "Segment/Datagram", "Transport", "TCP, UDP, SCTP"],
        ["3", "Network", "Packet", "Internet", "IP, ICMP, ARP, OSPF, BGP"],
        ["2", "Data Link", "Frame", "Network Access", "Ethernet, Wi-Fi, PPP, HDLC"],
        ["1", "Physical", "Bits", "Network Access", "RS-232, fiber, coaxial, RJ-45"],
    ],
)

section("Device vs OSI Layer")
info_table(
    ["Device", "OSI Layer", "PDU Handled", "Key Feature"],
    [
        ["Repeater", "L1", "Bits", "Signal regeneration; extends cable length"],
        ["Hub", "L1", "Bits", "Multi-port repeater; broadcasts to all ports"],
        ["Bridge", "L2", "Frames", "Filters by MAC; reduces collision domains"],
        ["Switch", "L2", "Frames", "Multi-port bridge; dedicated bandwidth per port"],
        ["Router", "L3", "Packets", "Routes by IP; separates broadcast domains"],
        ["Gateway", "L4-L7", "All", "Protocol translation; application-aware"],
    ],
)

tip(
    "Mnemonic for OSI layers (top to bottom): 'All People Seem To Need Data Processing' "
    "(Application, Presentation, Session, Transport, Network, Data Link, Physical). "
    "Bottom to top: 'Please Do Not Throw Sausage Pizza Away'. "
    "TCP = reliable, connection-oriented, 20-60B header. UDP = fast, connectionless, 8B header."
)

# =============================================================================
#  APPENDIX: FRAME FORMAT REFERENCE SHEET
# =============================================================================
br()
part_box("APPENDIX -- COMPLETE FRAME FORMAT REFERENCE SHEET")
body(
    "All protocol headers and frame formats used across Units 1-5, in two complementary styles: "
    "<b>Horizontal Field Layout</b> (frame_format) for overall field sequence, and "
    "<b>32-bit RFC-style Bit Grid</b> (packet_format) for precise bit-level layout."
)
sp(8)

# --- 1. HDLC Frame (Unit 2) ---
chap_box("HDLC -- High-Level Data Link Control Frame Format (Unit 2)")
section("Horizontal Field Layout")
frame_format(
    "HDLC Frame Format -- flag / address / control / information / FCS / flag",
    [
        ("FLAG", "8 bits  01111110"),
        ("ADDRESS", "8 bits"),
        ("CONTROL", "8 or 16 bits"),
        ("INFORMATION", "Variable"),
        ("FCS", "16 or 32 bits"),
        ("FLAG", "8 bits  01111110"),
    ],
)
bullet([
    "<b>FLAG (0x7E):</b> Marks frame start/end. Bit stuffing prevents this pattern in data.",
    "<b>ADDRESS:</b> Secondary station ID in multipoint links.",
    "<b>CONTROL:</b> I-frame (data), S-frame (supervisory), U-frame (unnumbered). Carries N(S)/N(R).",
    "<b>FCS:</b> CRC-16 or CRC-32 over Address+Control+Information.",
])
sp(10)

# --- 2. IEEE 802.2 LLC Frame (Unit 2) ---
chap_box("IEEE 802.2 LLC Frame Format (Unit 2)")
section("Horizontal Field Layout")
frame_format(
    "IEEE 802.2 LLC Frame -- DSAP / SSAP / Control / Data",
    [
        ("DSAP", "8 bits"),
        ("SSAP", "8 bits"),
        ("CONTROL", "8 or 16 bits"),
        ("DATA (Upper-layer PDU)", "Variable"),
    ],
)
bullet([
    "<b>DSAP:</b> Destination Service Access Point -- identifies the receiving upper-layer protocol (e.g. 0x06 = IP).",
    "<b>SSAP:</b> Source Service Access Point -- identifies the sending upper-layer protocol.",
    "<b>CONTROL:</b> Type 1 (UI, 8-bit) or Type 2 (numbered, 16-bit) -- same structure as HDLC.",
])
sp(10)

# --- 3. IEEE 802.3 Ethernet Frame (Units 2 & 3) ---
chap_box("IEEE 802.3 Ethernet Frame Format (Units 2 & 3)")
section("Horizontal Field Layout")
frame_format(
    "IEEE 802.3 Ethernet Frame -- Preamble / SFD / DST / SRC / Len-Type / Data / FCS",
    [
        ("PREAMBLE", "7 bytes"),
        ("SFD", "1 byte"),
        ("DST MAC", "6 bytes"),
        ("SRC MAC", "6 bytes"),
        ("LEN/TYPE", "2 bytes"),
        ("DATA (Payload)", "46-1500 bytes"),
        ("FCS (CRC-32)", "4 bytes"),
    ],
)
bullet([
    "<b>PREAMBLE:</b> 10101010 × 7 bytes — clock synchronization.",
    "<b>SFD (10101011):</b> Signals start of DST MAC address.",
    "<b>LEN/TYPE:</b> ≤1500 = length (802.3); ≥1536 = EtherType (Ethernet II: 0x0800=IPv4, 0x0806=ARP, 0x86DD=IPv6).",
    "<b>DATA:</b> 46–1500 bytes (padded to 46 if shorter). Min frame = 64 bytes for CSMA/CD collision detection.",
    "<b>FCS:</b> CRC-32 over DST+SRC+LEN/TYPE+DATA.",
])
sp(10)

# --- 4. IEEE 802.4 Token Bus Frame (Unit 3) ---
chap_box("IEEE 802.4 Token Bus Frame Format (Unit 3)")
section("Horizontal Field Layout")
frame_format(
    "IEEE 802.4 Token Bus Frame -- Preamble / SD / FC / DST / SRC / Data / FCS / ED",
    [
        ("PREAMBLE", "1+ bytes"),
        ("SD", "1 byte"),
        ("FC", "1 byte"),
        ("DST", "2 or 6 bytes"),
        ("SRC", "2 or 6 bytes"),
        ("DATA (Payload)", "0-8182 bytes"),
        ("FCS", "4 bytes"),
        ("ED", "1 byte"),
    ],
)
bullet([
    "<b>SD/ED:</b> Start/End Delimiters — frame boundaries.",
    "<b>FC:</b> Frame Control — LLC data, token, claim_token, who_follows, resolve_contention.",
    "<b>Token Frame:</b> FC=token, DST=next station address. No data field.",
    "Used in factory automation (MAP). Physical bus, logical token ring. Deterministic.",
])
sp(10)

# --- 5. IEEE 802.5 Token Ring Frame (Unit 3) ---
chap_box("IEEE 802.5 Token Ring Frame Format (Unit 3)")
section("Token Frame (3 bytes)")
frame_format(
    "IEEE 802.5 Token Frame -- SD / AC / ED",
    [
        ("SD (Start Delimiter)", "1 byte"),
        ("AC (Access Control)", "1 byte -- T bit selects free/busy"),
        ("ED (End Delimiter)", "1 byte"),
    ],
)
section("Data Frame")
frame_format(
    "IEEE 802.5 Data Frame -- SD / AC / FC / DST / SRC / Data / FCS / ED / FS",
    [
        ("SD", "1 byte"),
        ("AC", "1 byte"),
        ("FC", "1 byte"),
        ("DST", "2 or 6 bytes"),
        ("SRC", "2 or 6 bytes"),
        ("DATA", "0-17800 bytes"),
        ("FCS", "4 bytes"),
        ("ED", "1 byte"),
        ("FS (Frame Status)", "1 byte -- A + C bits"),
    ],
)
bullet([
    "<b>AC byte:</b> Priority (PPP), Token bit (T: 0=free, 1=busy), Monitor (M) bits.",
    "<b>FS byte (set by destination):</b> A (Address Recognized) and C (Frame Copied) bits — source reads these to confirm delivery.",
    "<b>Free Token = SD + AC(T=0) + ED</b> — only 3 bytes, no data payload.",
])
sp(10)

# --- 6. FDDI Frame (Unit 3) ---
chap_box("FDDI Frame Format (Unit 3)")
section("Horizontal Field Layout")
frame_format(
    "FDDI Frame -- PA / SD / FC / DST / SRC / Data / FCS / ED / FS",
    [
        ("PA (Preamble)", "16 bytes"),
        ("SD", "1 byte"),
        ("FC", "1 byte"),
        ("DST", "6 bytes"),
        ("SRC", "6 bytes"),
        ("DATA", "0-4478 bytes"),
        ("FCS", "4 bytes"),
        ("ED", "1 byte"),
        ("FS", "1 byte"),
    ],
)
bullet([
    "<b>PA:</b> 16-byte preamble using IDLE symbols (4B/5B encoding).",
    "<b>SD:</b> JK non-data symbol pair — frame start marker.",
    "<b>FC:</b> Synchronous vs asynchronous; LLC vs MAC control frame.",
    "<b>DATA:</b> Up to 4478 bytes — larger than Ethernet's 1500B MTU.",
    "<b>Token format:</b> PA + SD + FC + ED (no DST/SRC/Data).",
    "Uses <b>4B/5B encoding + NRZI</b> — no bit stuffing needed.",
])
sp(10)

# --- 7. Classful IP Address Format (Unit 4) ---
chap_box("IPv4 Classful Addressing Format (Unit 4)")
section("32-bit Bit Grid")
packet_format(
    "Classful IPv4 Address Formats (Class A, B, C)",
    [
        ("0", 1), ("Net ID", 7), ("Host ID", 24),
        ("10", 2), ("Net ID", 14), ("Host ID", 16),
        ("110", 3), ("Net ID", 21), ("Host ID", 8),
    ],
    bit_ruler=True,
)
bullet([
    "<b>Class A:</b> 1-126 in first octet (/8). 7-bit Net ID, 24-bit Host ID. 16.7M hosts/network.",
    "<b>Class B:</b> 128-191 (/16). 14-bit Net ID, 16-bit Host ID. 65,534 hosts/network.",
    "<b>Class C:</b> 192-223 (/24). 21-bit Net ID, 8-bit Host ID. 254 hosts/network.",
    "<b>Class D:</b> 224-239 — Multicast. <b>Class E:</b> 240-255 — Reserved/Experimental.",
])
sp(10)

# --- 8. ARP Packet Format (Unit 4) ---
chap_box("ARP Packet Format (Unit 4)")
section("32-bit Bit Grid")
packet_format(
    "ARP Packet Format (28 bytes for Ethernet/IPv4)",
    [
        ("Hardware Type", 16), ("Protocol Type", 16),
        ("HLen", 8), ("PLen", 8), ("Operation", 16),
        ("Sender MAC (Octets 0-3)", 32),
        ("Sender MAC (Octets 4-5)", 16), ("Sender IP (Octets 0-1)", 16),
        ("Sender IP (Octets 2-3)", 16), ("Target MAC (Octets 0-1)", 16),
        ("Target MAC (Octets 2-5)", 32),
        ("Target IP (Octets 0-3)", 32),
    ],
)
bullet([
    "<b>Hardware Type:</b> 1 = Ethernet. <b>Protocol Type:</b> 0x0800 = IPv4.",
    "<b>Operation:</b> 1=ARP Request, 2=ARP Reply, 3=RARP Request, 4=RARP Reply.",
    "<b>ARP Request:</b> broadcast; Target MAC = 00:00:00:00:00:00 (unknown). <b>Reply:</b> unicast back.",
])
sp(10)

# --- 9. IPv4 Header Format (Unit 4) ---
chap_box("IPv4 Header Format (Unit 4)")
section("32-bit Bit Grid")
packet_format(
    "IPv4 Header Format (min 20 bytes, max 60 bytes)",
    [
        ("Version", 4), ("IHL", 4), ("DSCP/ECN", 8), ("Total Length", 16),
        ("Identification", 16), ("Flags", 3), ("Fragment Offset", 13),
        ("TTL", 8), ("Protocol", 8), ("Header Checksum", 16),
        ("Source IP Address", 32),
        ("Destination IP Address", 32),
        ("Options + Padding", 32),
    ],
)
bullet([
    "<b>IHL:</b> Header length in 32-bit words; min=5 (20B), max=15 (60B).",
    "<b>Flags:</b> Bit1=DF (Don't Fragment), Bit2=MF (More Fragments).",
    "<b>Fragment Offset:</b> Position of this fragment in units of 8 bytes. First fragment = 0.",
    "<b>TTL:</b> Decremented at each hop; packet dropped when 0 (prevents loops).",
    "<b>Protocol:</b> 1=ICMP, 6=TCP, 17=UDP, 89=OSPF.",
    "<b>Header Checksum:</b> One's complement sum of header only. Recalculated at every router.",
])
sp(10)

# --- 10. IPv6 Header Format (Unit 4) ---
chap_box("IPv6 Base Header Format (Unit 4)")
section("32-bit Bit Grid")
packet_format(
    "IPv6 Base Header Format (fixed 40 bytes)",
    [
        ("Version", 4), ("Traffic Class", 8), ("Flow Label", 20),
        ("Payload Length", 16), ("Next Header", 8), ("Hop Limit", 8),
        ("Source Address", 128),
        ("Destination Address", 128),
    ],
)
bullet([
    "<b>Version:</b> Always 6. <b>Traffic Class:</b> DSCP (6b) + ECN (2b) for QoS.",
    "<b>Flow Label (20b):</b> NEW in IPv6 — identifies a traffic flow for special handling.",
    "<b>Next Header:</b> Identifies next extension header or transport protocol (6=TCP, 17=UDP, 58=ICMPv6).",
    "<b>Hop Limit:</b> Replaces IPv4 TTL. No Header Checksum field (removed for router speed).",
    "<b>Source/Dest Addresses:</b> 128 bits each (vs. 32 bits in IPv4).",
    "No fragmentation fields in base header — fragmentation via Extension Header only (source-side).",
])
sp(10)

# --- 11. UDP Header Format (Unit 5) ---
chap_box("UDP Header Format (Unit 5)")
section("32-bit Bit Grid")
packet_format(
    "UDP Datagram Header (fixed 8 bytes)",
    [
        ("Src Port", 16), ("Dst Port", 16),
        ("Length", 16), ("Checksum", 16),
    ],
    bit_ruler=True,
)
bullet([
    "<b>Source Port (16b):</b> Sending process port. Optional (may be 0).",
    "<b>Destination Port (16b):</b> Receiving process port — used for demultiplexing.",
    "<b>Length (16b):</b> Total UDP datagram length (header + data). Min = 8 bytes.",
    "<b>Checksum (16b):</b> Optional in IPv4 (0 = disabled); <b>mandatory in IPv6</b>. Covers pseudo-header + UDP header + data.",
    "Well-known UDP ports: DNS=53, DHCP=67/68, SNMP=161, TFTP=69, NTP=123.",
])
sp(10)

# --- 12. TCP Header Format (Unit 5) ---
chap_box("TCP Segment Header Format (Unit 5)")
section("32-bit Bit Grid")
packet_format(
    "TCP Segment Header (min 20 bytes, max 60 bytes with options)",
    [
        ("Src Port", 16), ("Dst Port", 16),
        ("Sequence Number", 32),
        ("Acknowledgement Number", 32),
        ("DO", 4), ("Rsvd", 6), ("URG", 1), ("ACK", 1), ("PSH", 1), ("RST", 1), ("SYN", 1), ("FIN", 1),
        ("Window Size", 16),
        ("Checksum", 16), ("Urgent Pointer", 16),
        ("Options + Padding (0-40 bytes)", 32),
    ],
    bit_ruler=True,
)
bullet([
    "<b>Sequence Number:</b> Byte position of first byte in this segment. ISN if SYN is set.",
    "<b>ACK Number:</b> Next seq# the sender expects — confirms all bytes up to (ACK-1) received.",
    "<b>DO (Data Offset):</b> Header length in 32-bit words; min=5 (20B), max=15 (60B).",
    "<b>Flags:</b> URG, ACK, PSH, RST, SYN, FIN — control connection lifecycle and data delivery.",
    "<b>Window Size:</b> Receiver buffer space available — limits sender's unacknowledged data (flow control).",
    "<b>Checksum:</b> Mandatory — covers pseudo-header + TCP header + data.",
    "Well-known TCP ports: HTTP=80, HTTPS=443, FTP=21, SSH=22, Telnet=23, SMTP=25.",
])

tip(
    "Quick memory aid -- frame sizes: HDLC=variable, LLC=variable, Ethernet=64-1518B, "
    "802.4 Token Bus data=0-8182B, 802.5 Token Ring data=0-17800B, FDDI data=0-4478B, "
    "ARP=28B, IPv4 header=20-60B, IPv6 header=40B (fixed), UDP header=8B (fixed), TCP header=20-60B."
)

sp(20)
body(
    "<b>End of CN PYQ Answers -- Computer Networks IT-411/IT503</b><br/>"
    "UIT-RGPV (Autonomous) Bhopal | Semester IV/V | MST-2, MST-3, May-June 2024, Dec 2024, May-June 2025"
)

# =============================================================================
#  BUILD PDF
# =============================================================================
# Determine output filename based on theme
if active_theme.name == "Dark":
    output_filename = "CN_PYQ_Answers.pdf"
else:
    suffix = active_theme.name.replace(" ", "")
    output_filename = f"CN_PYQ_Answers_{suffix}.pdf"

build_doc(output_filename, story)
