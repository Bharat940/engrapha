"""
Computer Networks (IT-411) -- Unit I Notes
UIT-RGPV (Autonomous) Bhopal | Semester IV
Complete exam notes with vector diagrams.
Run: python cn_unit1_notes.py
Output: CN_Unit1_Notes.pdf
"""

from __future__ import annotations

from typing import Any

from reportlab.lib import colors
from reportlab.lib.colors import Color
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.platypus import (
    BaseDocTemplate,
    Flowable,
    HRFlowable,
    PageBreak,
    Paragraph,
    Preformatted,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

import paperforge_diagrams as pd
from paperforge_diagrams.network import NodeKind

PAGE_W, PAGE_H = A4
PM = 1.8 * cm
CW = PAGE_W - 2 * PM

# ── Colour palette ────────────────────────────────────────────────────────────
BG = colors.HexColor("#0d1117")
CARD_DARK = colors.HexColor("#161b22")
CARD_MID = colors.HexColor("#1c2333")
CYAN = colors.HexColor("#79c0ff")
GREEN = colors.HexColor("#3fb950")
GREEN_CARD = colors.HexColor("#0d2119")
YELLOW = colors.HexColor("#d29922")
YELLOW_CARD = colors.HexColor("#1f1a0a")
RED = colors.HexColor("#f85149")
RED_CARD = colors.HexColor("#1e0d0d")
PURPLE = colors.HexColor("#bc8cff")
PURPLE_CARD = colors.HexColor("#180d2b")
WHITE = colors.HexColor("#f0f6fc")
WHITE_DIM = colors.HexColor("#9da7b3")
TABLE_HDR = colors.HexColor("#1f6feb")
TABLE_R1 = colors.HexColor("#161b22")
TABLE_R2 = colors.HexColor("#1b2230")
TABLE_BDR = colors.HexColor("#30363d")
CODE_BG = colors.HexColor("#161b22")
CODE_GREEN = colors.HexColor("#7ee787")


# ── Style definitions ─────────────────────────────────────────────────────────
def S(name: str, **kw: Any) -> ParagraphStyle:
    return ParagraphStyle(name, **kw)


COVER_H1 = S(
    "CH1",
    fontSize=34,
    textColor=WHITE,
    fontName="Helvetica-Bold",
    alignment=TA_CENTER,
    leading=42,
    spaceAfter=8,
)
COVER_H2 = S(
    "CH2",
    fontSize=16,
    textColor=CYAN,
    fontName="Helvetica",
    alignment=TA_CENTER,
    leading=24,
    spaceAfter=4,
)
COVER_SUB = S(
    "CS",
    fontSize=11,
    textColor=WHITE_DIM,
    fontName="Helvetica",
    alignment=TA_CENTER,
    leading=18,
)
PART_ST = S(
    "PT",
    fontSize=26,
    textColor=WHITE,
    fontName="Helvetica-Bold",
    alignment=TA_CENTER,
    leading=34,
)
CHAP_ST = S(
    "CP",
    fontSize=17,
    textColor=WHITE,
    fontName="Helvetica-Bold",
    alignment=TA_LEFT,
    leading=26,
)
SECT_ST = S(
    "SC",
    fontSize=13,
    textColor=CYAN,
    fontName="Helvetica-Bold",
    spaceBefore=12,
    spaceAfter=5,
    leading=20,
)
SUB_ST = S(
    "SB",
    fontSize=11,
    textColor=CYAN,
    fontName="Helvetica-Bold",
    spaceBefore=8,
    spaceAfter=4,
    leading=17,
)
BODY_ST = S(
    "BD",
    fontSize=10,
    textColor=WHITE,
    fontName="Helvetica",
    leading=17,
    spaceAfter=5,
    alignment=TA_JUSTIFY,
)
BOLD_ST = S(
    "BL",
    fontSize=10,
    textColor=WHITE,
    fontName="Helvetica-Bold",
    leading=17,
    spaceAfter=4,
)
BULLET_ST = S(
    "BU",
    fontSize=10,
    textColor=WHITE,
    fontName="Helvetica",
    leading=16,
    leftIndent=16,
    spaceAfter=3,
)
DEF_ST = S(
    "DF",
    fontSize=10,
    textColor=WHITE,
    fontName="Helvetica",
    leading=16,
    leftIndent=10,
    spaceAfter=4,
    alignment=TA_JUSTIFY,
)
TIP_ST = S(
    "TP",
    fontSize=9.5,
    textColor=GREEN,
    fontName="Helvetica-Bold",
    leading=15,
    leftIndent=6,
    spaceAfter=5,
)
NOTE_ST = S(
    "NT",
    fontSize=9.5,
    textColor=YELLOW,
    fontName="Helvetica-Oblique",
    leading=15,
    leftIndent=6,
    spaceAfter=4,
)
CODE_ST = S(
    "CD",
    fontSize=8,
    textColor=CODE_GREEN,
    fontName="Courier",
    leading=12,
    backColor=CODE_BG,
    borderWidth=1,
    borderColor=CYAN,
    leftIndent=8,
    rightIndent=8,
    spaceBefore=6,
    spaceAfter=10,
)
CAP_ST = S(
    "CAP",
    fontSize=9,
    textColor=WHITE_DIM,
    fontName="Helvetica-Oblique",
    alignment=TA_CENTER,
    leading=14,
    spaceAfter=6,
)
Q_ST = S(
    "QST",
    fontSize=11,
    textColor=YELLOW,
    fontName="Helvetica-Bold",
    leading=18,
    spaceAfter=4,
    spaceBefore=10,
)

story: list[Flowable] = []


# ── Core helpers ──────────────────────────────────────────────────────────────
def add(x: Flowable) -> None:
    story.append(x)


def sp(h: float = 8) -> None:
    add(Spacer(1, h))


def rule(c: Color = CYAN, t: float = 0.6) -> None:
    add(HRFlowable(width="100%", thickness=t, color=c, spaceAfter=6, spaceBefore=2))


def br() -> None:
    add(PageBreak())


# ── Layout blocks ─────────────────────────────────────────────────────────────
def part_box(text: str) -> None:
    t = Table([[Paragraph(text, PART_ST)]], colWidths=[CW])
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), CARD_DARK),
                ("TOPPADDING", (0, 0), (-1, -1), 22),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 22),
                ("LEFTPADDING", (0, 0), (-1, -1), 20),
                ("RIGHTPADDING", (0, 0), (-1, -1), 20),
                ("BOX", (0, 0), (-1, -1), 2.5, CYAN),
            ]
        )
    )
    add(t)
    sp(14)


def chap_box(text: str) -> None:
    t = Table([[Paragraph(text, CHAP_ST)]], colWidths=[CW])
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), CARD_MID),
                ("TOPPADDING", (0, 0), (-1, -1), 10),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
                ("LEFTPADDING", (0, 0), (-1, -1), 14),
                ("RIGHTPADDING", (0, 0), (-1, -1), 14),
                ("BOX", (0, 0), (-1, -1), 1.5, CYAN),
            ]
        )
    )
    add(t)
    sp(8)


def section(text: str) -> None:
    add(Paragraph(text, SECT_ST))
    rule(CYAN, 0.5)


def subsection(text: str) -> None:
    add(Paragraph(text, SUB_ST))


def body(text: str) -> None:
    add(Paragraph(text, BODY_ST))


def definition(text: str, bg: Color = CARD_MID, border: Color = CYAN) -> None:
    t = Table([[Paragraph(text, DEF_ST)]], colWidths=[CW])
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), bg),
                ("TOPPADDING", (0, 0), (-1, -1), 9),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
                ("LEFTPADDING", (0, 0), (-1, -1), 12),
                ("RIGHTPADDING", (0, 0), (-1, -1), 12),
                ("BOX", (0, 0), (-1, -1), 1.2, border),
            ]
        )
    )
    add(t)
    sp(7)


def highlight(text: str, bg: Color = CARD_MID, border: Color = YELLOW) -> None:
    t = Table(
        [
            [
                Paragraph(
                    text,
                    S(
                        "HL",
                        fontSize=10,
                        textColor=WHITE,
                        fontName="Helvetica",
                        leading=16,
                    ),
                )
            ]
        ],
        colWidths=[CW],
    )
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), bg),
                ("TOPPADDING", (0, 0), (-1, -1), 9),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
                ("LEFTPADDING", (0, 0), (-1, -1), 12),
                ("RIGHTPADDING", (0, 0), (-1, -1), 12),
                ("BOX", (0, 0), (-1, -1), 1.4, border),
            ]
        )
    )
    add(t)
    sp(7)


def tip(text: str) -> None:
    p = Paragraph(f"<b>EXAM TIP:</b> {text}", TIP_ST)
    t = Table([[p]], colWidths=[CW])
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), GREEN_CARD),
                ("BOX", (0, 0), (-1, -1), 1.2, GREEN),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
                ("LEFTPADDING", (0, 0), (-1, -1), 12),
                ("RIGHTPADDING", (0, 0), (-1, -1), 12),
            ]
        )
    )
    add(t)
    sp(6)


def note(text: str) -> None:
    p = Paragraph(f"<b>NOTE:</b> {text}", NOTE_ST)
    t = Table([[p]], colWidths=[CW])
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), YELLOW_CARD),
                ("BOX", (0, 0), (-1, -1), 1.2, YELLOW),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
                ("LEFTPADDING", (0, 0), (-1, -1), 12),
                ("RIGHTPADDING", (0, 0), (-1, -1), 12),
            ]
        )
    )
    add(t)
    sp(6)


def bullet(items: list[str]) -> None:
    h = "79c0ff"
    for item in items:
        add(Paragraph(f'<font color="#{h}">&#8226;</font> {item}', BULLET_ST))
    sp(4)


def code_block(text: str) -> None:
    add(Preformatted(text.strip(), CODE_ST))


def info_table(
    headers: list[str], rows: list[list[str]], hdr_color: Color = TABLE_HDR
) -> None:
    th = S(
        "TH2",
        fontSize=9,
        textColor=WHITE,
        fontName="Helvetica-Bold",
        alignment=TA_CENTER,
        leading=14,
    )
    td = S("TD2", fontSize=9, textColor=WHITE, fontName="Helvetica", leading=14)
    data = [[Paragraph(str(h), th) for h in headers]]
    for row in rows:
        data.append([Paragraph(str(c), td) for c in row])
    cw = CW / len(headers)
    t = Table(data, colWidths=[cw] * len(headers), repeatRows=1)
    style = [
        ("BACKGROUND", (0, 0), (-1, 0), hdr_color),
        ("GRID", (0, 0), (-1, -1), 0.4, TABLE_BDR),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]
    for i in range(1, len(rows) + 1):
        style.append(
            ("BACKGROUND", (0, i), (-1, i), TABLE_R1 if i % 2 == 1 else TABLE_R2)
        )
    t.setStyle(TableStyle(style))
    add(t)
    sp(10)


# ── Page decoration ───────────────────────────────────────────────────────────
def page_decor(canvas: Canvas, doc: BaseDocTemplate) -> None:
    canvas.saveState()
    canvas.setFillColor(BG)
    canvas.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
    canvas.setFillColor(WHITE_DIM)
    canvas.setFont("Helvetica", 9)
    canvas.drawRightString(PAGE_W - PM, PM / 2, str(doc.page))
    canvas.restoreState()


# ═════════════════════════════════════════════════════════════════════════════
#  COVER PAGE
# ═════════════════════════════════════════════════════════════════════════════
sp(24)
t = Table([[Paragraph("COMPUTER NETWORKS", COVER_H1)]], colWidths=[CW])
t.setStyle(
    TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, -1), CARD_DARK),
            ("TOPPADDING", (0, 0), (-1, -1), 28),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 28),
            ("LEFTPADDING", (0, 0), (-1, -1), 20),
            ("RIGHTPADDING", (0, 0), (-1, -1), 20),
            ("BOX", (0, 0), (-1, -1), 2, CYAN),
        ]
    )
)
add(t)
sp(14)
add(Paragraph("Unit I -- Complete Exam Notes", COVER_H2))
add(Paragraph("Subject Code: IT-411  |  UIT-RGPV (Autonomous) Bhopal", COVER_SUB))
add(Paragraph("Semester IV  |  Based on University Syllabus 2024-25", COVER_SUB))
sp(10)
rule(CYAN, 1.5)
sp(8)

info_table(
    ["Topic", "Coverage"],
    [
        [
            "1.1 Importance of Computer Networks",
            "Applications, advantages, resource sharing",
        ],
        ["1.2 Broadcast vs Point-to-Point Networks", "Transmission modes, comparisons"],
        ["1.3 LAN and WAN", "Definitions, characteristics, differences"],
        ["1.4 Network Topologies", "Bus, Star, Ring, Mesh, Tree, Hybrid"],
        ["1.5 ISO-OSI Reference Model", "7 layers, functions, PDUs, interfaces"],
        ["1.6 TCP/IP Reference Model", "4 layers, protocols, comparison with OSI"],
        ["1.7 Connection-Oriented vs Connectionless", "Services, primitives, examples"],
        ["1.8 Novel Netware, Arpanet, X.25", "Historical networks and standards"],
        ["1.9 Physical Layer Standards", "RJ-45, NIC, Cat5/6/7, cable coding"],
        ["1.10 Quick Revision Summary", "Key formulas and exam flashcards"],
    ],
)
br()


# ═════════════════════════════════════════════════════════════════════════════
#  UNIT I DIVIDER
# ═════════════════════════════════════════════════════════════════════════════
part_box("UNIT I -- INTRODUCTION TO COMPUTER NETWORKS")


# ─────────────────────────────────────────────────────────────────────────────
#  1.1  IMPORTANCE OF COMPUTER NETWORKS
# ─────────────────────────────────────────────────────────────────────────────
chap_box("1.1  Importance of Computer Networks")
section("Definition")
definition(
    "<b>Computer Network:</b> A collection of autonomous computers and other devices "
    "interconnected by a communication medium (wired or wireless) to share resources, "
    "exchange information, and provide services to users. A network enables hardware "
    "(printers, storage), software (applications, databases), and data to be shared "
    "among many users simultaneously."
)
section("Why Are Networks Important?")
bullet(
    [
        "<b>Resource Sharing:</b> Hardware (printers, scanners, servers) and software can be shared across users, reducing cost.",
        "<b>Data Communication:</b> Email, instant messaging, video conferencing, and file transfer are all enabled by networks.",
        "<b>Centralized Data Management:</b> Data stored on central servers is easier to back up, secure, and manage.",
        "<b>Reliability:</b> Data can be replicated on multiple machines so that a single hardware failure does not cause data loss.",
        "<b>Cost Efficiency:</b> A single high-speed printer shared by 50 users is far cheaper than 50 individual printers.",
        "<b>Scalability:</b> Networks can easily grow by adding new nodes without disrupting existing services.",
        "<b>Remote Access:</b> Users can access organizational resources from anywhere via VPN or cloud services.",
        "<b>E-Commerce and Banking:</b> Online shopping, UPI payments, ATM networks -- all depend on computer networks.",
    ]
)
tip(
    "In a 2-mark exam answer: define a network, then list at least 4 benefits with one-line explanations."
)
sp(6)


# ─────────────────────────────────────────────────────────────────────────────
#  1.2  BROADCAST VS POINT-TO-POINT NETWORKS
# ─────────────────────────────────────────────────────────────────────────────
chap_box("1.2  Broadcast and Point-to-Point Networks")
section("Broadcast Networks")
definition(
    "<b>Broadcast Network:</b> A network in which a single communication channel is "
    "shared by ALL machines. When any machine sends a packet, every other machine on "
    "the network receives it. The packet contains an address field; machines check "
    "the address and discard packets not intended for them."
)
bullet(
    [
        "All nodes share the same transmission medium.",
        "A special broadcast address (e.g. 255.255.255.255 in IP) causes every machine to process the packet.",
        "A multicast address delivers a packet to a subset of machines (a group).",
        "Examples: Ethernet (bus topology), Wi-Fi (802.11), cable TV networks, early Token Ring.",
        "Simpler to wire but limited in scale -- adding nodes increases collision risk.",
    ]
)

section("Point-to-Point Networks")
definition(
    "<b>Point-to-Point Network:</b> A network made up of many individual connections "
    "between pairs of machines. A packet travelling from source to destination may "
    "pass through several intermediate nodes (routers), each forwarding the packet "
    "towards the destination. Also called a <b>unicast</b> network at the link level."
)
bullet(
    [
        "Each link connects exactly two devices.",
        "Routing algorithms determine the best path through the network.",
        "More complex to manage but highly scalable and flexible.",
        "Examples: The Internet (IP routing), leased-line WANs, optical fiber backbone links.",
        "Better security -- data is not broadcast to all nodes.",
    ]
)

section("Comparison Table")
info_table(
    ["Feature", "Broadcast Network", "Point-to-Point Network"],
    [
        [
            "Channel",
            "Single shared medium for all nodes",
            "Dedicated link between each pair",
        ],
        [
            "Packet delivery",
            "Every node receives; address checked",
            "Only destination node receives",
        ],
        ["Routing", "Not needed -- all on same channel", "Routing algorithms required"],
        ["Scale", "Limited (collisions increase with nodes)", "Highly scalable"],
        [
            "Security",
            "Lower -- all nodes see all traffic",
            "Higher -- traffic is directed",
        ],
        [
            "Examples",
            "Ethernet (classic), Wi-Fi, cable TV",
            "Internet (IP), leased lines, WAN",
        ],
        ["Cost", "Cheaper -- less cabling", "More cabling but better performance"],
    ],
)
sp(4)

# Diagram: broadcast vs point-to-point side by side
bcast = pd.NetworkDiagram(
    width=CW * 0.44, height=165, caption="Fig 1a: Broadcast (Bus)"
)
bcast.bus_topology(["PC-A", "PC-B", "PC-C", "PC-D"])

p2p = pd.NetworkDiagram(
    width=CW * 0.44, height=165, caption="Fig 1b: Point-to-Point (Mesh)"
)
p2p.mesh_topology(["R1", "R2", "R3", "R4"])

bcast.as_flowable()
p2p.as_flowable()
side_tbl = Table(
    [
        [
            pd.ResponsiveDrawingFlowable(bcast.drawing),
            pd.ResponsiveDrawingFlowable(p2p.drawing),
        ]
    ],
    colWidths=[CW * 0.48, CW * 0.48],
)
side_tbl.setStyle(
    TableStyle(
        [
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 4),
            ("RIGHTPADDING", (0, 0), (-1, -1), 4),
            ("TOPPADDING", (0, 0), (-1, -1), 0),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ]
    )
)
add(side_tbl)
add(
    Paragraph(
        "Fig 1a (left): Broadcast -- all nodes share one bus  |  Fig 1b (right): Point-to-point mesh routing",
        CAP_ST,
    )
)
sp(8)
br()


# ─────────────────────────────────────────────────────────────────────────────
#  1.3  LAN AND WAN
# ─────────────────────────────────────────────────────────────────────────────
chap_box("1.3  Local Area Networks (LAN) and Wide Area Networks (WAN)")
section("Local Area Network (LAN)")
definition(
    "<b>LAN (Local Area Network):</b> A network that interconnects computers and devices "
    "within a limited geographic area such as a single building, floor, campus, or home. "
    "LANs are privately owned, provide high data rates (100 Mbps to 10 Gbps), and have "
    "low error rates due to short distances."
)
bullet(
    [
        "Geographic range: up to a few kilometres (typically one building or campus).",
        "Speed: 100 Mbps (Fast Ethernet), 1 Gbps (Gigabit Ethernet), up to 10/40 Gbps.",
        "Media: Twisted pair (UTP Cat5e/6/7), Fiber optic, Wi-Fi (802.11).",
        "Ownership: Privately owned and managed by the organization.",
        "Topology: Star (most common), Bus (legacy), Ring.",
        "Error rate: Very low -- short cables, controlled environment.",
        "Examples: Office LAN, university campus network, home Wi-Fi.",
    ]
)

section("Wide Area Network (WAN)")
definition(
    "<b>WAN (Wide Area Network):</b> A network that spans a large geographic area -- "
    "a country, continent, or the globe. WANs typically connect multiple LANs via leased "
    "telephone lines, fiber optic cables, satellite links, or the public Internet. "
    "WANs are usually managed by telecom carriers."
)
bullet(
    [
        "Geographic range: cities, countries, or worldwide.",
        "Speed: Varies widely -- 56 Kbps (old dial-up) to 100 Gbps (backbone fiber).",
        "Media: Leased lines, optical fiber (SONET/SDH), satellite, microwave, PSTN.",
        "Ownership: Usually public (operated by ISPs / telecom companies).",
        "Technology: MPLS, Frame Relay, ATM, SD-WAN, the Internet.",
        "Error rate: Higher than LAN due to long distances and shared infrastructure.",
        "Examples: The Internet, SWIFT (banking), corporate VPN over Internet.",
    ]
)

section("MAN -- Metropolitan Area Network")
definition(
    "<b>MAN (Metropolitan Area Network):</b> A network that covers a city or metropolitan "
    "area (5 -- 50 km). Larger than a LAN but smaller than a WAN. Examples: cable TV "
    "networks, city-wide Wi-Fi, university systems spanning multiple campuses in a city."
)

section("Comparison: LAN vs MAN vs WAN")
info_table(
    ["Parameter", "LAN", "MAN", "WAN"],
    [
        [
            "Geographic Range",
            "Room / Building / Campus (up to 1 km)",
            "City (5-50 km)",
            "Country / Worldwide (>50 km)",
        ],
        [
            "Speed",
            "100 Mbps -- 10 Gbps",
            "10 Mbps -- 1 Gbps",
            "56 Kbps -- 100 Gbps (varies)",
        ],
        [
            "Ownership",
            "Private (organization)",
            "Private or Public",
            "Public (ISPs, Telecom)",
        ],
        ["Error Rate", "Very low", "Low to moderate", "Higher"],
        ["Propagation Delay", "Very short", "Moderate", "High"],
        ["Setup Cost", "Low", "Moderate", "High"],
        [
            "Technology",
            "Ethernet, Wi-Fi (802.11)",
            "WiMAX (802.16), Cable TV",
            "MPLS, Internet, Satellite, SONET",
        ],
        [
            "Examples",
            "Home network, office LAN",
            "City-wide broadband",
            "The Internet, corporate WAN",
        ],
    ],
)
tip(
    "Remember: LAN = building, MAN = city, WAN = country/world. Exam often asks for at least 3 differences between LAN and WAN."
)
sp(6)

# Diagram: WAN connecting two LANs
net_wan = pd.NetworkDiagram(
    width=CW,
    height=180,
    caption="Fig 2: WAN connecting two remote LANs via a router cloud",
)
net_wan.node("sw1", "LAN Switch A", x=70, y=130, kind="switch")
net_wan.node("pc1", "Host A1", x=30, y=60, kind="host")
net_wan.node("pc2", "Host A2", x=110, y=60, kind="host")
net_wan.node("r1", "Router A", x=175, y=130, kind="router")
net_wan.node("wan", "WAN / Internet", x=290, y=130, kind="cloud")
net_wan.node("r2", "Router B", x=405, y=130, kind="router")
net_wan.node("sw2", "LAN Switch B", x=470, y=130, kind="switch")
net_wan.node("pc3", "Host B1", x=430, y=60, kind="host")
net_wan.node("pc4", "Host B2", x=510, y=60, kind="host")
net_wan.link("sw1", "pc1")
net_wan.link("sw1", "pc2")
net_wan.link("sw1", "r1")
net_wan.link("r1", "wan", label="Leased Line")
net_wan.link("wan", "r2", label="Leased Line")
net_wan.link("r2", "sw2")
net_wan.link("sw2", "pc3")
net_wan.link("sw2", "pc4")
story.extend(net_wan.as_flowable())
sp(4)
br()


# ─────────────────────────────────────────────────────────────────────────────
#  1.4  NETWORK TOPOLOGIES
# ─────────────────────────────────────────────────────────────────────────────
chap_box("1.4  Network Topologies")
section("What is Network Topology?")
definition(
    "<b>Network Topology:</b> The physical or logical arrangement of nodes (computers, "
    "switches, routers) and the communication links connecting them in a network. "
    "Physical topology describes how devices are physically wired; logical topology "
    "describes how data flows through the network."
)

section("1. Bus Topology")
body(
    "All nodes are connected to a single shared backbone cable called the <b>bus</b>. "
    "Data transmitted by any node travels along the entire bus in both directions. "
    "Terminators at each end absorb signals to prevent reflections."
)
bullet(
    [
        "Simple and cheap -- least amount of cable needed.",
        "A break in the backbone cable brings down the entire network.",
        "Performance degrades as more devices are added (more collisions).",
        "CSMA/CD used for access control in Ethernet bus networks.",
        "Used in: 10BASE2 (Thin Ethernet), 10BASE5 (Thick Ethernet) -- both now legacy.",
    ]
)

section("2. Star Topology")
body(
    "Every node connects directly to a central device -- a <b>hub</b> or <b>switch</b>. "
    "All communication passes through the central device. This is the most widely "
    "deployed topology in modern LANs."
)
bullet(
    [
        "Easy fault isolation -- one cable fault only affects one node.",
        "Easy to add or remove nodes without disrupting the network.",
        "Central hub/switch is a single point of failure (SPOF).",
        "Requires more cable than bus topology.",
        "Used in: Modern Ethernet LANs (100BASE-TX, Gigabit Ethernet), Wi-Fi (AP as center).",
    ]
)

section("3. Ring Topology")
body(
    "Each node is connected to exactly two other nodes, forming a closed loop. "
    "Data travels in one direction (unidirectional) or both directions (bidirectional "
    "dual ring). Token Ring and FDDI use this topology."
)
bullet(
    [
        "Token passing ensures orderly, collision-free access.",
        "Predictable performance -- maximum wait time is bounded.",
        "A single node or cable failure can break the entire ring (unless dual ring).",
        "Adding or removing nodes requires temporarily halting the network.",
        "Used in: IEEE 802.5 Token Ring, FDDI (dual ring for fault tolerance).",
    ]
)

section("4. Mesh Topology")
body(
    "Every node has a dedicated point-to-point link to every other node. "
    "A full mesh of <b>n</b> nodes requires <b>n(n-1)/2</b> links. "
    "Partial mesh is more practical -- only critical nodes are fully interconnected."
)
bullet(
    [
        "Highest fault tolerance -- multiple paths exist between any two nodes.",
        "No single point of failure.",
        "Very expensive -- large amount of cabling and interface ports.",
        "Used in: Internet backbone routers, military networks, WAN core infrastructure.",
    ]
)

section("5. Tree (Hierarchical) Topology")
body(
    "Nodes are arranged in a hierarchy -- a root switch at the top, distribution "
    "switches in the middle, and access switches or hosts at the leaves. "
    "This is the dominant design in enterprise campus networks."
)

section("6. Hybrid Topology")
body(
    "A combination of two or more topologies. For example, a star-bus topology "
    "connects several star networks together using a bus backbone. Most real-world "
    "enterprise networks are hybrid topologies."
)

section("Topology Comparison Table")
info_table(
    [
        "Topology",
        "Cable Required",
        "Fault Tolerance",
        "Cost",
        "Scalability",
        "Real Example",
    ],
    [
        ["Bus", "Least", "Low", "Very low", "Low", "10BASE2 Ethernet (legacy)"],
        ["Star", "More", "Medium", "Medium", "High", "Modern office Ethernet"],
        [
            "Ring",
            "Moderate",
            "Low (single ring)",
            "Medium",
            "Medium",
            "Token Ring, FDDI",
        ],
        [
            "Mesh",
            "Most",
            "Very high",
            "Very high",
            "Limited",
            "Internet backbone, WANs",
        ],
        ["Tree", "Moderate", "Medium", "Medium", "Very high", "Enterprise campus LAN"],
        ["Hybrid", "Varies", "High", "High", "Very high", "Most real-world networks"],
    ],
)
sp(4)

# Diagram: star and ring side by side
topo_star = pd.NetworkDiagram(
    width=CW * 0.44, height=180, caption="Fig 3a: Star Topology"
)
topo_star.star_topology(
    "sw", "Core Switch", ["PC-A", "PC-B", "Server", "Printer"], spoke_kind="host"
)

topo_ring = pd.NetworkDiagram(
    width=CW * 0.44, height=180, caption="Fig 3b: Ring Topology"
)
topo_ring.ring_topology(["Node A", "Node B", "Node C", "Node D"])

topo_star.as_flowable()
topo_ring.as_flowable()
tbl2 = Table(
    [
        [
            pd.ResponsiveDrawingFlowable(topo_star.drawing),
            pd.ResponsiveDrawingFlowable(topo_ring.drawing),
        ]
    ],
    colWidths=[CW * 0.48, CW * 0.48],
)
tbl2.setStyle(
    TableStyle(
        [
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 4),
            ("RIGHTPADDING", (0, 0), (-1, -1), 4),
            ("TOPPADDING", (0, 0), (-1, -1), 0),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ]
    )
)
add(tbl2)
add(
    Paragraph(
        "Fig 3a (left): Star -- central switch  |  Fig 3b (right): Ring -- closed loop",
        CAP_ST,
    )
)
sp(8)

# Diagram: tree topology
topo_tree = pd.NetworkDiagram(
    width=CW,
    height=220,
    caption="Fig 3c: Tree (Hierarchical) Topology -- typical enterprise campus design",
)
tree_struct = {
    "core": ["dist1", "dist2"],
    "dist1": ["acc1", "acc2"],
    "dist2": ["acc3", "acc4"],
}
tree_kinds: dict[str, NodeKind] = {
    "core": "switch",
    "dist1": "switch",
    "dist2": "switch",
    "acc1": "host",
    "acc2": "host",
    "acc3": "host",
    "acc4": "host",
}
tree_labels = {
    "core": "Core Switch",
    "dist1": "Dist SW 1",
    "dist2": "Dist SW 2",
    "acc1": "Access SW1",
    "acc2": "Access SW2",
    "acc3": "Access SW3",
    "acc4": "Access SW4",
}
topo_tree.tree_topology(tree_struct, node_labels=tree_labels, node_kinds=tree_kinds)
story.extend(topo_tree.as_flowable())
tip(
    "Mesh needs n(n-1)/2 links. For 5 nodes: 5x4/2 = 10 links. For 6 nodes: 15 links. This formula is frequently asked in exams."
)
br()


# ─────────────────────────────────────────────────────────────────────────────
#  1.5  ISO-OSI REFERENCE MODEL
# ─────────────────────────────────────────────────────────────────────────────
chap_box("1.5  ISO-OSI Reference Model")
section("Overview")
definition(
    "<b>ISO-OSI (Open Systems Interconnection) Reference Model:</b> A conceptual framework "
    "developed by the International Organization for Standardization (ISO) in 1984. "
    "It divides network communication into <b>7 layers</b>, each with specific functions. "
    "It defines how different systems can communicate with each other regardless of their "
    "underlying architecture -- it is a <b>reference model</b>, not a protocol specification."
)
body(
    "The OSI model enables interoperability between products from different vendors. "
    "Each layer provides services to the layer above it and uses services from the layer "
    "below it. Communication between peer layers on different systems is governed by "
    "<b>protocols</b>. Communication between adjacent layers on the same system uses "
    "<b>interfaces</b> (Service Access Points -- SAPs)."
)

section("The 7 Layers -- Detailed")

subsection("Layer 7: Application Layer")
body(
    "The topmost layer -- the only layer that directly interacts with the end user and "
    "application software. It provides <b>network services to applications</b> such as "
    "file transfer, email, web browsing, and remote login."
)
bullet(
    [
        "Provides: file transfer (FTP), email (SMTP, POP3, IMAP), web (HTTP/HTTPS), DNS, DHCP, Telnet, SNMP.",
        "PDU: <b>Data (Message)</b>",
        "Does NOT include the application programs themselves -- it provides the interface.",
    ]
)

subsection("Layer 6: Presentation Layer")
body(
    "Responsible for <b>data translation, encryption, and compression</b>. Ensures that "
    "data sent by one system can be understood by another system even if they use "
    "different internal data representations."
)
bullet(
    [
        "Data translation: ASCII <-> EBCDIC, big-endian <-> little-endian.",
        "Encryption and decryption: SSL/TLS operates here.",
        "Data compression: JPEG, MPEG, ZIP.",
        "PDU: <b>Data</b>",
    ]
)

subsection("Layer 5: Session Layer")
body(
    "Establishes, manages, and terminates <b>sessions</b> (dialogues) between communicating "
    "applications. A session is a temporary connection between two processes."
)
bullet(
    [
        "Session establishment, maintenance, and termination.",
        "Dialog control: half-duplex or full-duplex communication.",
        "Synchronization: inserts checkpoints (sync points) so a long transfer can be resumed after a failure.",
        "Examples: NetBIOS, RPC (Remote Procedure Call), PPTP.",
        "PDU: <b>Data</b>",
    ]
)

subsection("Layer 4: Transport Layer")
body(
    "Provides <b>end-to-end (process-to-process) delivery</b> of data between applications "
    "on different hosts. It is responsible for reliability, flow control, and error recovery."
)
bullet(
    [
        "Segmentation and reassembly of data.",
        "Connection-oriented (TCP) or connectionless (UDP) communication.",
        "Flow control: prevents sender from overwhelming receiver (sliding window).",
        "Error control: detects and retransmits lost or corrupted segments.",
        "Port numbers identify specific processes (e.g., HTTP=80, FTP=21, DNS=53).",
        "PDU: <b>Segment</b> (TCP) / <b>Datagram</b> (UDP)",
    ]
)

subsection("Layer 3: Network Layer")
body(
    "Responsible for <b>host-to-host (logical) delivery</b> of packets across multiple "
    "networks. It determines the best path (routing) for data to travel from source to "
    "destination across interconnected networks."
)
bullet(
    [
        "Logical addressing: IP addresses (IPv4, IPv6).",
        "Routing: selects the best path through the internet (RIP, OSPF, BGP).",
        "Packet forwarding: moves packets from input link to output link.",
        "Fragmentation and reassembly: large packets may be split for smaller MTU links.",
        "PDU: <b>Packet</b>",
        "Key protocols: IP, ICMP, ARP, RARP, OSPF, BGP.",
    ]
)

subsection("Layer 2: Data Link Layer")
body(
    "Provides <b>node-to-node delivery</b> of frames on a single network link. "
    "It packages raw bits into frames, handles physical addressing (MAC addresses), "
    "and provides error detection for the physical layer."
)
bullet(
    [
        "Framing: encapsulates packets into frames with header and trailer.",
        "Physical (MAC) addressing: 48-bit MAC addresses in Ethernet.",
        "Error detection: CRC (Cyclic Redundancy Check) in the trailer.",
        "Flow control at link level.",
        "Media Access Control (MAC): determines which device can use the shared medium.",
        "PDU: <b>Frame</b>",
        "Sublayers: LLC (Logical Link Control) and MAC (Media Access Control).",
        "Key protocols: Ethernet (802.3), Wi-Fi (802.11), PPP, HDLC.",
    ]
)

subsection("Layer 1: Physical Layer")
body(
    "The lowest layer -- deals with the actual <b>physical transmission</b> of raw bits "
    "over a communication medium. Defines the electrical, optical, and mechanical "
    "characteristics of the physical link."
)
bullet(
    [
        "Bit representation: encoding of 0s and 1s as voltage levels, light pulses, or radio waves.",
        "Transmission rate: defines bits per second (bps).",
        "Physical medium: twisted pair, coaxial cable, fiber optic, radio waves.",
        "Connector types: RJ-45 (Ethernet), SC/LC (fiber), BNC (coax).",
        "Synchronization of bits: clocking.",
        "PDU: <b>Bits</b>",
        "Standards: RS-232, V.35, RJ-45, IEEE 802.3 physical specifications.",
    ]
)

section("OSI Layers Summary Table")
info_table(
    ["Layer", "Name", "PDU", "Key Function", "Key Protocols / Standards"],
    [
        [
            "7",
            "Application",
            "Data",
            "User interface to network services",
            "HTTP, FTP, SMTP, DNS, DHCP, Telnet",
        ],
        [
            "6",
            "Presentation",
            "Data",
            "Data translation, encryption, compression",
            "SSL/TLS, JPEG, ASCII, MPEG",
        ],
        [
            "5",
            "Session",
            "Data",
            "Session setup, sync, dialog control",
            "NetBIOS, RPC, PPTP, SIP",
        ],
        [
            "4",
            "Transport",
            "Segment",
            "End-to-end delivery, flow/error ctrl",
            "TCP, UDP, SCTP",
        ],
        [
            "3",
            "Network",
            "Packet",
            "Host-to-host routing, logical address",
            "IP, ICMP, ARP, OSPF, BGP",
        ],
        [
            "2",
            "Data Link",
            "Frame",
            "Node-to-node delivery, MAC addressing",
            "Ethernet, Wi-Fi, PPP, HDLC",
        ],
        [
            "1",
            "Physical",
            "Bits",
            "Raw bit transmission over medium",
            "RS-232, RJ-45, 802.3 Physical",
        ],
    ],
)

# OSI layered stack diagram
osi_stack = pd.LayeredStack(
    width=CW,
    height=310,
    caption="Fig 4: ISO-OSI 7-Layer Reference Model with PDUs and Protocols",
)
osi_stack.layer(
    "7  Application", sublabel="HTTP, FTP, SMTP, DNS, DHCP, Telnet  |  PDU: Data"
)
osi_stack.layer(
    "6  Presentation", sublabel="SSL/TLS, JPEG, ASCII, MPEG           |  PDU: Data"
)
osi_stack.layer(
    "5  Session", sublabel="NetBIOS, RPC, PPTP, SIP              |  PDU: Data"
)
osi_stack.divider()
osi_stack.layer(
    "4  Transport",
    sublabel="TCP (reliable), UDP (fast)           |  PDU: Segment / Datagram",
)
osi_stack.layer(
    "3  Network", sublabel="IP, ICMP, ARP, OSPF, BGP             |  PDU: Packet"
)
osi_stack.layer(
    "2  Data Link", sublabel="Ethernet 802.3, Wi-Fi, PPP, HDLC     |  PDU: Frame"
)
osi_stack.layer(
    "1  Physical", sublabel="RS-232, RJ-45, Fiber, Radio           |  PDU: Bits"
)
story.extend(osi_stack.as_flowable())

highlight(
    "<b>Mnemonic for OSI Layers (top to bottom):</b>  "
    "All People Seem To Need Data Processing  "
    "(Application, Presentation, Session, Transport, Network, Data Link, Physical)",
    CARD_DARK,
    CYAN,
)
tip(
    "Exam frequently asks: (1) Name all 7 layers with functions. (2) PDU at each layer. (3) Which layer adds IP address? (Layer 3). Which adds MAC? (Layer 2). Which adds port numbers? (Layer 4)."
)
br()


# ─────────────────────────────────────────────────────────────────────────────
#  1.6  TCP/IP REFERENCE MODEL
# ─────────────────────────────────────────────────────────────────────────────
chap_box("1.6  TCP/IP Reference Model")
section("Overview")
definition(
    "<b>TCP/IP Reference Model:</b> The practical networking model on which the Internet "
    "is built. Developed by the U.S. Department of Defense (DARPA) in the 1970s as part "
    "of the ARPANET project. It has <b>4 layers</b> and is a prescriptive model -- actual "
    "protocols (TCP, IP, etc.) were designed alongside it."
)

section("The 4 Layers")

subsection("Layer 4: Application Layer")
body(
    "Combines the OSI Application, Presentation, and Session layers into one. "
    "Handles all high-level protocols and user-facing services."
)
bullet(
    [
        "HTTP/HTTPS: web browsing",
        "FTP/TFTP: file transfer",
        "SMTP/POP3/IMAP: email",
        "DNS: domain name to IP resolution",
        "DHCP: automatic IP configuration",
        "Telnet/SSH: remote terminal access",
        "SNMP: network management",
    ]
)

subsection("Layer 3: Transport Layer")
body(
    "Provides process-to-process communication using port numbers. Contains two core protocols:"
)
bullet(
    [
        "<b>TCP (Transmission Control Protocol):</b> Connection-oriented, reliable, ordered delivery. Uses 3-way handshake. Provides flow control (sliding window) and congestion control.",
        "<b>UDP (User Datagram Protocol):</b> Connectionless, unreliable, fast. No handshake. Used where speed > reliability (DNS, VoIP, streaming, gaming).",
    ]
)

subsection("Layer 2: Internet Layer")
body(
    "Corresponds to OSI Layer 3. Provides host-to-host delivery across multiple networks using IP addresses."
)
bullet(
    [
        "<b>IPv4:</b> 32-bit addressing, connectionless, best-effort delivery.",
        "<b>IPv6:</b> 128-bit addressing, designed to replace IPv4.",
        "<b>ICMP:</b> Error reporting and diagnostics (ping uses ICMP Echo).",
        "<b>ARP:</b> Maps IP addresses to MAC addresses.",
        "<b>RARP:</b> Maps MAC to IP (now replaced by DHCP).",
        "<b>OSPF, BGP, RIP:</b> Routing protocols that build routing tables.",
    ]
)

subsection("Layer 1: Network Access Layer (Link Layer)")
body(
    "Combines OSI Layers 1 and 2. Handles the physical transmission of frames on a single link."
)
bullet(
    [
        "Ethernet (IEEE 802.3): dominant wired LAN technology.",
        "Wi-Fi (IEEE 802.11): wireless LAN.",
        "PPP (Point-to-Point Protocol): dial-up and DSL connections.",
        "HDLC: synchronous serial links.",
        "Defines MAC addressing, framing, and physical signalling.",
    ]
)

section("TCP/IP Layer Stack Diagram")
tcpip_stack = pd.LayeredStack(
    width=CW, height=230, caption="Fig 5: TCP/IP 4-Layer Model with Protocols"
)
tcpip_stack.layer(
    "Application Layer", sublabel="HTTP, FTP, SMTP, DNS, DHCP, Telnet, SSH, SNMP"
)
tcpip_stack.layer(
    "Transport Layer",
    sublabel="TCP (connection-oriented, reliable)  /  UDP (connectionless, fast)",
)
tcpip_stack.layer(
    "Internet Layer", sublabel="IPv4, IPv6, ICMP, ARP, RARP, OSPF, BGP, RIP"
)
tcpip_stack.layer(
    "Network Access Layer", sublabel="Ethernet (802.3), Wi-Fi (802.11), PPP, HDLC, ARP"
)
story.extend(tcpip_stack.as_flowable())
sp(6)

section("OSI vs TCP/IP Comparison")
info_table(
    ["Feature", "OSI Model", "TCP/IP Model"],
    [
        [
            "Developed by",
            "ISO (International Std. Org.), 1984",
            "DARPA (US Dept of Defense), 1970s",
        ],
        ["Number of layers", "7 layers", "4 layers"],
        [
            "Layer names",
            "Physical, Data Link, Network, Transport, Session, Presentation, Application",
            "Network Access, Internet, Transport, Application",
        ],
        [
            "Protocol design",
            "Model first, then protocols designed",
            "Protocols first, model described later",
        ],
        [
            "Usage",
            "Reference / teaching model. Not widely implemented directly.",
            "Practical model -- the Internet runs on TCP/IP.",
        ],
        [
            "Transport",
            "Layer 4 -- connection and connectionless",
            "Layer 3 (Transport) -- TCP and UDP",
        ],
        [
            "Network",
            "Layer 3 -- connectionless only",
            "Layer 2 (Internet) -- connectionless IP",
        ],
        [
            "Session layer",
            "Separate Session layer (Layer 5)",
            "No separate session layer (merged into Application)",
        ],
        [
            "Presentation",
            "Separate Presentation layer (Layer 6)",
            "No separate layer (handled by applications)",
        ],
        [
            "Flexibility",
            "Strict layer boundaries",
            "More flexible -- fewer layers, easier to implement",
        ],
        ["Complexity", "More complex -- 7 layers", "Simpler -- 4 layers"],
    ],
)

# Side-by-side OSI vs TCP/IP stacks
osi_cmp = pd.LayeredStack(width=CW * 0.44, height=240, caption="OSI Model (7 Layers)")
osi_cmp.layer("7 Application")
osi_cmp.layer("6 Presentation")
osi_cmp.layer("5 Session")
osi_cmp.divider()
osi_cmp.layer("4 Transport")
osi_cmp.layer("3 Network")
osi_cmp.layer("2 Data Link")
osi_cmp.layer("1 Physical")

tcp_cmp = pd.LayeredStack(
    width=CW * 0.44, height=240, caption="TCP/IP Model (4 Layers)"
)
tcp_cmp.layer("Application", sublabel="(OSI 5+6+7)")
tcp_cmp.divider()
tcp_cmp.layer("Transport", sublabel="(OSI 4)")
tcp_cmp.layer("Internet", sublabel="(OSI 3)")
tcp_cmp.layer("Network Access", sublabel="(OSI 1+2)")

osi_cmp.as_flowable()
tcp_cmp.as_flowable()
cmp_tbl = Table(
    [
        [
            pd.ResponsiveDrawingFlowable(osi_cmp.drawing),
            pd.ResponsiveDrawingFlowable(tcp_cmp.drawing),
        ]
    ],
    colWidths=[CW * 0.48, CW * 0.48],
)
cmp_tbl.setStyle(
    TableStyle(
        [
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 4),
            ("RIGHTPADDING", (0, 0), (-1, -1), 4),
            ("TOPPADDING", (0, 0), (-1, -1), 0),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ]
    )
)
add(cmp_tbl)
add(Paragraph("Fig 6: OSI (left) vs TCP/IP (right) -- layer mapping", CAP_ST))
tip(
    "OSI Session and Presentation layers have NO equivalent in TCP/IP -- those functions are merged into the Application layer. This is the most common comparison question."
)
br()


# ─────────────────────────────────────────────────────────────────────────────
#  1.7  SERVICES, PDUs, CONNECTION-ORIENTED vs CONNECTIONLESS
# ─────────────────────────────────────────────────────────────────────────────
chap_box("1.7  Interfaces, Services, PDUs and Service Primitives")
section("Interfaces and Services")
definition(
    "<b>Service:</b> A set of operations that a layer provides to the layer above it. "
    "The service is the <i>what</i> -- what the layer promises to do. "
    "<b>Protocol:</b> The set of rules that govern how peer entities at the same layer "
    "communicate across the network -- the <i>how</i>. "
    "<b>Interface:</b> The boundary between adjacent layers on the same machine, "
    "defined by a Service Access Point (SAP)."
)
bullet(
    [
        "Each layer provides a service to the layer immediately above it.",
        "Each layer uses the services of the layer immediately below it.",
        "Layers communicate with their peer on the remote machine via protocols.",
        "Adjacent layers on the same machine communicate via well-defined interfaces.",
    ]
)

section("Protocol Data Units (PDUs)")
definition(
    "<b>PDU (Protocol Data Unit):</b> The unit of data at each layer. Each layer wraps "
    "the data from the layer above with its own header (and sometimes trailer), "
    "creating a new PDU. This process is called <b>encapsulation</b>."
)
info_table(
    ["Layer", "PDU Name", "Header Added", "What It Contains"],
    [
        [
            "Application (Layer 7/4)",
            "Message / Data",
            "Application header",
            "User data (e.g. HTTP request)",
        ],
        [
            "Transport (Layer 4/3)",
            "Segment / Datagram",
            "TCP/UDP header (port numbers, seq no.)",
            "Message + Transport header",
        ],
        [
            "Network (Layer 3/2)",
            "Packet",
            "IP header (src/dst IP)",
            "Segment + IP header",
        ],
        [
            "Data Link (Layer 2/1)",
            "Frame",
            "MAC header + FCS trailer",
            "Packet + MAC header/trailer",
        ],
        [
            "Physical (Layer 1)",
            "Bits",
            "None (encoding only)",
            "Frame serialized to bits",
        ],
    ],
)

section("Connection-Oriented vs Connectionless Services")
definition(
    "<b>Connection-Oriented Service:</b> Modelled after the telephone system. A connection "
    "is established before data transfer, used during transfer, and then released after "
    "transfer is complete. Guarantees ordered, reliable delivery."
)
definition(
    "<b>Connectionless Service:</b> Modelled after the postal system. Each message "
    "(packet/datagram) is routed independently through the network. No setup phase. "
    "Packets may arrive out of order or be lost."
)
info_table(
    ["Feature", "Connection-Oriented", "Connectionless"],
    [
        ["Setup phase", "Required (3-way handshake for TCP)", "Not required"],
        [
            "Path",
            "Fixed path established for session",
            "Each packet routed independently",
        ],
        ["Ordering", "Packets arrive in order", "Packets may arrive out of order"],
        [
            "Reliability",
            "Guaranteed (retransmission on loss)",
            "Not guaranteed (best effort)",
        ],
        ["Overhead", "Higher (connection setup overhead)", "Lower (no setup)"],
        ["Speed", "Slower (due to handshake and ACKs)", "Faster"],
        ["Error control", "End-to-end error recovery", "None (or only at link level)"],
        ["Example", "TCP (Transport), X.25 (Network)", "UDP (Transport), IP (Network)"],
        ["Analogy", "Telephone call", "Postal letter / courier service"],
    ],
)

section("Service Primitives")
body(
    "Service primitives are the abstract operations used by one layer to request or "
    "signal services from the adjacent layer. The OSI model defines four standard primitives:"
)
info_table(
    ["Primitive", "Direction", "Meaning"],
    [
        [
            "REQUEST",
            "User -> Provider",
            "The service user requests a service from the provider (e.g., initiate connection).",
        ],
        [
            "INDICATION",
            "Provider -> User",
            "The provider notifies the user that an event has occurred (e.g., incoming connection request).",
        ],
        [
            "RESPONSE",
            "User -> Provider",
            "The user responds to an indication (e.g., accept or reject an incoming connection).",
        ],
        [
            "CONFIRM",
            "Provider -> User",
            "The provider confirms that the requested service has been completed (e.g., connection is established).",
        ],
    ],
)
body(
    "Example -- Connection Establishment using primitives: "
    "Client calls CONNECT.REQUEST -> Network sends CONNECT.INDICATION to server -> "
    "Server calls CONNECT.RESPONSE -> Network delivers CONNECT.CONFIRM to client."
)

# Sequence diagram of connection setup primitives
seq_conn = pd.SequenceDiagram(
    width=CW,
    height=230,
    caption="Fig 7: Service Primitives -- Connection-Oriented Setup",
)
seq_conn.actor("cli", "Client (User A)")
seq_conn.actor("net", "Network (Provider)")
seq_conn.actor("srv", "Server (User B)")
seq_conn.message("cli", "net", "CONNECT.request", arrow="solid")
seq_conn.message("net", "srv", "CONNECT.indication", arrow="solid")
seq_conn.message("srv", "net", "CONNECT.response", arrow="dashed")
seq_conn.message("net", "cli", "CONNECT.confirm", arrow="dashed")
seq_conn.divider("Connection Established -- Data Transfer Phase")
seq_conn.message("cli", "net", "DATA.request", arrow="solid")
seq_conn.message("net", "srv", "DATA.indication", arrow="solid")
story.extend(seq_conn.as_flowable())
tip(
    "Service primitives are often asked in theory. Remember the 4 types: Request, Indication, Response, Confirm. Applies to both connection setup and data transfer."
)
br()


# ─────────────────────────────────────────────────────────────────────────────
#  1.8  NOVEL NETWARE, ARPANET, X.25
# ─────────────────────────────────────────────────────────────────────────────
chap_box("1.8  Novel Netware, ARPANET, and X.25")
section("ARPANET")
definition(
    "<b>ARPANET (Advanced Research Projects Agency NETwork):</b> The world's first "
    "operational packet-switched network, funded by the U.S. Department of Defense (DARPA). "
    "It became operational in 1969, connecting four universities. ARPANET is the direct "
    "predecessor of the modern Internet."
)
bullet(
    [
        "First nodes (1969): UCLA, UCSB, Stanford Research Institute, University of Utah.",
        "Pioneered packet switching (replacing circuit switching for data networks).",
        "Introduced the TCP/IP protocol suite (Cerf and Kahn, 1974).",
        "Used NCP (Network Control Protocol) initially, later replaced by TCP/IP in 1983.",
        "Decommissioned in 1990; the Internet grew out of its infrastructure.",
        "Key concept proven: a distributed packet-switched network can survive partial node failures.",
    ]
)

section("Novel Netware")
definition(
    "<b>Novell NetWare:</b> A network operating system (NOS) developed by Novell Inc. "
    "in the early 1980s. It was dominant in the corporate LAN market through the 1980s "
    "and early 1990s, before being displaced by Windows NT and Unix/Linux servers."
)
bullet(
    [
        "Used IPX/SPX (Internetwork Packet Exchange / Sequenced Packet Exchange) as its protocol stack.",
        "IPX is similar to IP (connectionless, network layer); SPX is similar to TCP (connection-oriented, transport).",
        "Provided file and print sharing services for DOS/Windows clients.",
        "Used NDS (Novell Directory Services) for centralized user and resource management.",
        "Later versions (NetWare 5 and later) added native TCP/IP support.",
        "Largely replaced by Microsoft Windows Server and Active Directory by the late 1990s.",
    ]
)

section("X.25")
definition(
    "<b>X.25:</b> An ITU-T standard (1976) defining a packet-switched WAN protocol suite. "
    "It was the dominant WAN technology before Frame Relay and ATM. X.25 provides a "
    "connection-oriented network service (virtual circuits) and includes extensive "
    "error checking at every node (designed for unreliable telephone networks)."
)
bullet(
    [
        "Defines 3 layers: Physical (X.21 / RS-232), Data Link (LAPB -- Link Access Protocol Balanced), and Packet (network layer).",
        "Uses <b>virtual circuits</b>: either PVC (Permanent Virtual Circuit) or SVC (Switched Virtual Circuit).",
        "Every node does error checking and retransmission -- suitable for noisy analog phone lines.",
        "Maximum data rate: 64 Kbps (typical), up to 2 Mbps (later revisions).",
        "Largely replaced by Frame Relay and ATM in the 1990s; now mostly obsolete.",
        "Was widely used for ATM networks, credit card verification networks, airline reservation systems.",
    ]
)

info_table(
    ["Network", "Era", "Technology", "Key Feature", "Status"],
    [
        [
            "ARPANET",
            "1969-1990",
            "Packet switching",
            "Ancestor of the Internet; proved TCP/IP",
            "Decommissioned (gave birth to Internet)",
        ],
        [
            "Novell NetWare",
            "1983-2000s",
            "IPX/SPX over LAN",
            "Dominant corporate LAN NOS in 1980s-90s",
            "Largely replaced by Windows Server",
        ],
        [
            "X.25",
            "1976-2000s",
            "Virtual circuit WAN",
            "Reliable WAN over noisy phone lines",
            "Obsolete; replaced by Frame Relay/MPLS",
        ],
    ],
)
sp(6)
br()


# ─────────────────────────────────────────────────────────────────────────────
#  1.9  PHYSICAL LAYER STANDARDS: RJ-45, NIC, CABLE CATEGORIES, CABLE CODING
# ─────────────────────────────────────────────────────────────────────────────
chap_box("1.9  Physical Layer Standards -- RJ-45, NIC, Cable Categories, Cable Coding")
section("RJ-45 Connector")
definition(
    "<b>RJ-45 (Registered Jack 45):</b> The standard 8-pin modular connector used to "
    "terminate twisted pair Ethernet cables (Cat5, Cat5e, Cat6, Cat6a, Cat7). "
    "It is the most common connector for wired Ethernet networks."
)
bullet(
    [
        "Has 8 pins (positions 1-8), each connected to one wire of the cable.",
        "Used with TIA/EIA-568 wiring standards (T568A and T568B).",
        "Supports data speeds from 10 Mbps (Cat3) to 10 Gbps (Cat6a) and beyond.",
        "The male connector (plug) is crimped onto the cable; the female connector (jack) is mounted in wall outlets or switch/router ports.",
    ]
)

section("Network Interface Card (NIC)")
definition(
    "<b>NIC (Network Interface Card):</b> A hardware component (chip or expansion card) "
    "that connects a computer to a network. It implements the Physical and Data Link "
    "layers -- handles signal transmission, reception, framing, and MAC addressing."
)
bullet(
    [
        "Every NIC has a globally unique <b>MAC address</b> (48-bit, burned into hardware by manufacturer).",
        "MAC address format: 6 bytes in hex, e.g. 00:1A:2B:3C:4D:5E. First 3 bytes = OUI (manufacturer), last 3 = device ID.",
        "Modern computers have NICs integrated on the motherboard.",
        "Supports speeds: 10 Mbps, 100 Mbps, 1 Gbps, 10 Gbps.",
        "Wireless NIC (WNIC) supports Wi-Fi (802.11a/b/g/n/ac/ax).",
    ]
)

section("Rack")
body(
    "A <b>rack</b> (server rack / network rack) is a standardized metal frame used to "
    "mount networking equipment (switches, routers, patch panels, servers, UPS) in a "
    "structured and space-efficient manner. Standard rack widths are 19 inches, and "
    "height is measured in <b>rack units (U)</b> where 1U = 1.75 inches."
)

section("Cable Categories -- Cat 5, 6, and 7")
info_table(
    [
        "Category",
        "Max Bandwidth",
        "Max Speed",
        "Max Distance",
        "Pairs",
        "Shielding",
        "Typical Use",
    ],
    [
        [
            "Cat 5",
            "100 MHz",
            "100 Mbps",
            "100 m",
            "4 (2 used)",
            "None (UTP)",
            "Legacy Fast Ethernet (100BASE-TX)",
        ],
        [
            "Cat 5e",
            "100 MHz",
            "1 Gbps",
            "100 m",
            "4 (all)",
            "None (UTP)",
            "Gigabit Ethernet -- most common deployed cable",
        ],
        [
            "Cat 6",
            "250 MHz",
            "1 Gbps (10G to 55m)",
            "100 m (55m for 10G)",
            "4",
            "Optional (U/UTP or F/UTP)",
            "Gigabit LAN, small data centers",
        ],
        [
            "Cat 6a",
            "500 MHz",
            "10 Gbps",
            "100 m",
            "4",
            "Shielded (F/UTP or S/FTP)",
            "10GbE, data centers, large offices",
        ],
        [
            "Cat 7",
            "600 MHz",
            "10 Gbps",
            "100 m",
            "4",
            "Shielded (S/FTP)",
            "Data centers, high-performance environments",
        ],
        [
            "Cat 8",
            "2000 MHz",
            "25/40 Gbps",
            "30 m",
            "4",
            "Shielded (S/FTP)",
            "Data center server-to-switch, very short runs",
        ],
    ],
)

section("Cross-Connection and Straight-Through Cables")
subsection("Straight-Through Cable (Patch Cable)")
body(
    "Both ends are wired using the <b>same</b> wiring standard (both T568A or both T568B). "
    "Pin 1 at one end connects to Pin 1 at the other, Pin 2 to Pin 2, and so on."
)
bullet(
    [
        "Used to connect <b>unlike devices</b>: PC to Switch, PC to Hub, Switch to Router.",
        "The most common cable type -- standard patch cables are straight-through.",
    ]
)

subsection("Crossover Cable")
body(
    "One end uses T568A and the other end uses T568B. Transmit pins at one end "
    "connect to receive pins at the other end, allowing direct connection without a switch."
)
bullet(
    [
        "Used to connect <b>like devices</b> directly: PC to PC, Switch to Switch, Hub to Hub, Router to Router.",
        "Modern switches and NICs support Auto-MDI/MDIX, which can automatically detect cable type and swap TX/RX internally -- making crossover cables largely unnecessary.",
    ]
)

subsection("Rollover Cable (Console Cable)")
body(
    "Pin 1 connects to Pin 8, Pin 2 to Pin 7, etc. (completely reversed). "
    "Used exclusively to connect a PC serial/USB port to the <b>console port</b> of a "
    "Cisco router or switch for initial configuration."
)

section("TIA/EIA-568 Cable Coding Standards")
info_table(
    [
        "Standard",
        "Pin 1",
        "Pin 2",
        "Pin 3",
        "Pin 4",
        "Pin 5",
        "Pin 6",
        "Pin 7",
        "Pin 8",
    ],
    [
        [
            "T568A",
            "White/Green",
            "Green",
            "White/Orange",
            "Blue",
            "White/Blue",
            "Orange",
            "White/Brown",
            "Brown",
        ],
        [
            "T568B",
            "White/Orange",
            "Orange",
            "White/Green",
            "Blue",
            "White/Blue",
            "Green",
            "White/Brown",
            "Brown",
        ],
    ],
)
body(
    "T568B is the more commonly used standard in North America. T568A is preferred in "
    "government installations and some European countries. <b>Both ends must use the same "
    "standard for a straight-through cable</b>. A crossover uses T568A on one end and "
    "T568B on the other."
)
code_block("""
 T568B PIN ASSIGNMENTS (most common standard):
 ============================================================
 Pin 1: White/Orange  --  Transmit Data + (TX+)
 Pin 2: Orange        --  Transmit Data - (TX-)
 Pin 3: White/Green   --  Receive Data  + (RX+)
 Pin 4: Blue          --  (unused in 10/100 Mbps; used for PoE and Gigabit)
 Pin 5: White/Blue    --  (unused in 10/100 Mbps; used for PoE and Gigabit)
 Pin 6: Green         --  Receive Data  - (RX-)
 Pin 7: White/Brown   --  (unused in 10/100 Mbps; used for PoE and Gigabit)
 Pin 8: Brown         --  (unused in 10/100 Mbps; used for PoE and Gigabit)

 CROSSOVER CABLE MAPPING (T568A <-> T568B):
 End A (T568A)         End B (T568B)
 Pin 1 White/Green  -> Pin 3 White/Green
 Pin 2 Green        -> Pin 6 Green
 Pin 3 White/Orange -> Pin 1 White/Orange
 Pin 6 Orange       -> Pin 2 Orange
 ============================================================
""")
tip(
    "Exam favourite: Draw/list T568A and T568B pin assignments. State the difference between straight-through and crossover. Give one use case for each."
)
br()


# ═════════════════════════════════════════════════════════════════════════════
#  1.10  QUICK REVISION SUMMARY
# ═════════════════════════════════════════════════════════════════════════════
part_box(
    "UNIT I -- QUICK REVISION SUMMARY",
)
chap_box("Key Concepts at a Glance")

info_table(
    ["Topic", "Key Point to Remember"],
    [
        [
            "Computer Network",
            "Interconnected autonomous computers sharing resources. Benefits: resource sharing, reliability, cost, remote access.",
        ],
        [
            "Broadcast Network",
            "Single shared channel. All nodes receive every packet. Example: Ethernet bus, Wi-Fi.",
        ],
        [
            "Point-to-Point",
            "Dedicated links between pairs. Routing needed. Example: Internet routers, leased WAN lines.",
        ],
        [
            "LAN",
            "Up to a few km, private, 100 Mbps to 10 Gbps, low error rate, Ethernet/Wi-Fi.",
        ],
        [
            "WAN",
            "Country/worldwide, public (ISP-operated), variable speed, higher error rate, MPLS/Internet.",
        ],
        [
            "Bus Topology",
            "Shared backbone cable. Cheapest. Entire LAN fails if bus breaks. Legacy Ethernet.",
        ],
        [
            "Star Topology",
            "Central hub/switch. Easy fault isolation. SPOF at center. Modern Ethernet.",
        ],
        [
            "Ring Topology",
            "Closed loop. Token passing. One break = failure (unless dual ring). Token Ring, FDDI.",
        ],
        [
            "Mesh Topology",
            "Every node linked to every other. Links = n(n-1)/2. Fault-tolerant. Internet backbone.",
        ],
        [
            "OSI Model",
            "7 layers: Physical, Data Link, Network, Transport, Session, Presentation, Application. Mnemonic: PDN-TSPA.",
        ],
        [
            "OSI PDUs",
            "Bits (Layer 1), Frame (L2), Packet (L3), Segment (L4), Data (L5-L7).",
        ],
        [
            "TCP/IP Model",
            "4 layers: Network Access, Internet, Transport, Application. Practical Internet model.",
        ],
        [
            "OSI vs TCP/IP",
            "OSI: 7 layers, reference model. TCP/IP: 4 layers, actual Internet protocols.",
        ],
        [
            "Connection-Oriented",
            "Setup -> Transfer -> Teardown. Ordered, reliable. TCP, X.25. Like a phone call.",
        ],
        [
            "Connectionless",
            "No setup. Each packet independent. Faster, unreliable. UDP, IP. Like postal mail.",
        ],
        [
            "Service Primitives",
            "Request, Indication, Response, Confirm. Used between adjacent layers.",
        ],
        [
            "ARPANET",
            "First packet-switched network (1969). Predecessor of the Internet. Proved TCP/IP.",
        ],
        [
            "Novell NetWare",
            "1980s-90s dominant LAN NOS. IPX/SPX protocols. Replaced by Windows Server.",
        ],
        [
            "X.25",
            "1976 WAN standard. Virtual circuits. Per-hop error checking. Obsolete today.",
        ],
        [
            "RJ-45",
            "8-pin modular connector for twisted pair Ethernet. Used with T568A/B standard.",
        ],
        [
            "NIC",
            "Hardware implementing Layers 1-2. Has unique 48-bit MAC address (OUI + device ID).",
        ],
        ["Cat 5e", "1 Gbps, 100 MHz, 100 m. Most common cable deployed in offices."],
        ["Cat 6", "1 Gbps (10G up to 55m), 250 MHz. Slightly better than Cat 5e."],
        [
            "Cat 6a",
            "10 Gbps, 500 MHz, 100 m. Standard for new enterprise installations.",
        ],
        ["Cat 7", "10 Gbps, 600 MHz. Shielded (S/FTP). Data centers."],
        [
            "T568B",
            "Most common wiring: W/O, O, W/G, B, W/B, G, W/Br, Br. Both ends same = straight-through.",
        ],
        [
            "Straight-Through",
            "Same standard both ends. PC to Switch, PC to Hub. Most common patch cable.",
        ],
        [
            "Crossover",
            "T568A one end, T568B other. PC to PC, Switch to Switch. Modern NICs use Auto-MDI/MDIX.",
        ],
    ],
)

highlight(
    "<b>UNIT I EXAM BLUEPRINT:</b>  "
    "2-mark questions: Define LAN/WAN, OSI layers list, PDU names, primitive types. "
    "5-mark questions: Compare OSI vs TCP/IP, compare connection-oriented vs connectionless, draw OSI stack with protocols. "
    "10-mark questions: Explain OSI 7 layers in detail with functions and PDUs, explain TCP/IP model with diagram, explain topologies with advantages/disadvantages.",
    YELLOW_CARD,
    YELLOW,
)

# ═════════════════════════════════════════════════════════════════════════════
#  BUILD PDF
# ═════════════════════════════════════════════════════════════════════════════
doc = SimpleDocTemplate(
    "CN_Unit1_Notes.pdf",
    pagesize=A4,
    leftMargin=PM,
    rightMargin=PM,
    topMargin=PM,
    bottomMargin=PM,
    title="Computer Networks IT-411 Unit I Notes",
    author="UIT-RGPV (Autonomous) Bhopal",
)
doc.build(story, onFirstPage=page_decor, onLaterPages=page_decor)
print("Generated: CN_Unit1_Notes.pdf")
