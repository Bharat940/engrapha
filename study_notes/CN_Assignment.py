"""
Computer Networks (IT-411) — Assignment 1
UIT-RGPV (Autonomous) Bhopal | Complete Assignment Answers
Safe fonts: Helvetica / Courier only. No Unicode glyphs.
Run: python cn_assignment1.py
Output: CN_Assignment1.pdf

IMAGES TO DOWNLOAD — place in ./asset_images/ folder:
  packet_switching.png   -> https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Packet_Switching.gif/800px-Packet_Switching.gif
  tcpip_model.png        -> https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/UDP_encapsulation.svg/800px-UDP_encapsulation.svg.png
  network_topologies.png -> https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/NetworkTopologies.png/800px-NetworkTopologies.png
  twisted_pair.jpg       -> https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/25_pair_color_code_cable_telephony.svg/800px-25_pair_color_code_cable_telephony.svg.png
  crc_diagram.png        -> https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/CRC_CCITT_B_Bit_Stream.png/800px-CRC_CCITT_B_Bit_Stream.png
  hdlc_frame.png         -> https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/HDLC_frame_structure.png/800px-HDLC_frame_structure.png
  csma_cd.png            -> https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/CSMA_CD.svg/800px-CSMA_CD.svg.png
  classful_ip.png        -> https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Ipv4_address.svg/800px-Ipv4_address.svg.png
  dijkstra_graph.png     -> (Draw your own from the assignment question — the weighted graph given in Q1c/Q5b)
  bellman_ford.png       -> (Draw your own from the assignment question — the weighted graph given in Q7b)
  ospf_diagram.png       -> https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/OSPF_Concept.svg/800px-OSPF_Concept.svg.png
  dhcp_process.png       -> https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/DHCP_session.svg/800px-DHCP_session.svg.png
"""

import os
import re
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak,
    Table,
    TableStyle,
    HRFlowable,
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import Preformatted, Image
from reportlab.lib.utils import ImageReader

PAGE_W, PAGE_H = A4
PM = 1.8 * cm
CW = PAGE_W - 2 * PM
ASSET_DIR = "asset_images"

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


# ── Style factory ─────────────────────────────────────────────────────────────
def S(name, **kw):
    return ParagraphStyle(name, **kw)


COVER_H1 = S(
    "CH1",
    fontSize=32,
    textColor=WHITE,
    fontName="Helvetica-Bold",
    alignment=TA_CENTER,
    leading=40,
    spaceAfter=6,
)
COVER_H2 = S(
    "CH2",
    fontSize=15,
    textColor=CYAN,
    fontName="Helvetica",
    alignment=TA_CENTER,
    leading=22,
    spaceAfter=4,
)
COVER_INFO = S(
    "CI",
    fontSize=10,
    textColor=WHITE_DIM,
    fontName="Helvetica",
    alignment=TA_CENTER,
    leading=16,
)
PART_ST = S(
    "PT",
    fontSize=24,
    textColor=WHITE,
    fontName="Helvetica-Bold",
    alignment=TA_CENTER,
    leading=32,
)
CHAP_ST = S(
    "CP",
    fontSize=16,
    textColor=WHITE,
    fontName="Helvetica-Bold",
    alignment=TA_LEFT,
    leading=24,
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
NOTE_ST = S(
    "NT",
    fontSize=9.5,
    textColor=YELLOW,
    fontName="Helvetica-Oblique",
    leading=15,
    leftIndent=6,
    spaceAfter=4,
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

from typing import Any
story: list[Any] = []


def add(x):
    story.append(x)


def sp(h=8):
    add(Spacer(1, h))


def rule(c=CYAN, t=0.6):
    add(HRFlowable(width="100%", thickness=t, color=c, spaceAfter=6, spaceBefore=2))


def br():
    add(PageBreak())


def escape_cell(s):
    s = str(s)
    tags = re.findall(r"</?(?:b|i|u|sub|super|font)(?:\s[^>]*)?>", s)
    ph = "ZZZPH"
    clean = re.sub(r"</?(?:b|i|u|sub|super|font)(?:\s[^>]*)?>", ph, s)
    clean = clean.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    for tag in tags:
        clean = clean.replace(ph, tag, 1)
    return clean


# ── Layout widgets ────────────────────────────────────────────────────────────
def cover_box(para, bg=CARD_DARK, pv=36, ph=24):
    t = Table([[para]], colWidths=[CW])
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), bg),
                ("TOPPADDING", (0, 0), (-1, -1), pv),
                ("BOTTOMPADDING", (0, 0), (-1, -1), pv),
                ("LEFTPADDING", (0, 0), (-1, -1), ph),
                ("RIGHTPADDING", (0, 0), (-1, -1), ph),
                ("BOX", (0, 0), (-1, -1), 1.5, CYAN),
            ]
        )
    )
    add(t)
    sp(10)


def part_box(text, bg=CARD_DARK, border=CYAN):
    t = Table([[Paragraph(text, PART_ST)]], colWidths=[CW])
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), bg),
                ("TOPPADDING", (0, 0), (-1, -1), 20),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 20),
                ("LEFTPADDING", (0, 0), (-1, -1), 20),
                ("RIGHTPADDING", (0, 0), (-1, -1), 20),
                ("BOX", (0, 0), (-1, -1), 2, border),
            ]
        )
    )
    add(t)
    sp(14)


def chap_box(text, bg=CARD_MID, border=CYAN):
    t = Table([[Paragraph(text, CHAP_ST)]], colWidths=[CW])
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), bg),
                ("TOPPADDING", (0, 0), (-1, -1), 10),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
                ("LEFTPADDING", (0, 0), (-1, -1), 14),
                ("RIGHTPADDING", (0, 0), (-1, -1), 14),
                ("BOX", (0, 0), (-1, -1), 1.2, border),
            ]
        )
    )
    add(t)
    sp(8)


def section(text):
    add(Paragraph(text, SECT_ST))
    rule(CYAN, 0.5)


def subsection(text):
    add(Paragraph(text, SUB_ST))


def body(text):
    add(Paragraph(text, BODY_ST))


def bold(text):
    add(Paragraph(text, BOLD_ST))


def tip(text):
    p = Paragraph(f"<b>[NOTE]</b> {text}", TIP_ST)
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


def bullet(items):
    h = CYAN.hexval().replace("0x", "")
    for item in items:
        add(Paragraph(f'<font color="#{h}">&#8226;</font> {item}', BULLET_ST))
    sp(4)


def definition(text, bg=CARD_MID, border=CYAN):
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


def highlight(text, bg=CARD_MID, border=YELLOW):
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


def code_block(c):
    add(Preformatted(c.strip(), CODE_ST))


def qbox(text, bg=YELLOW_CARD, border=YELLOW):
    t = Table([[Paragraph(text, Q_ST)]], colWidths=[CW])
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), bg),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
                ("LEFTPADDING", (0, 0), (-1, -1), 12),
                ("RIGHTPADDING", (0, 0), (-1, -1), 12),
                ("BOX", (0, 0), (-1, -1), 1.4, border),
            ]
        )
    )
    add(t)
    sp(6)


def info_table(headers, rows, hdr_color=TABLE_HDR):
    th = S(
        "TH2",
        fontSize=9,
        textColor=WHITE,
        fontName="Helvetica-Bold",
        alignment=TA_CENTER,
        leading=14,
    )
    td = S("TD2", fontSize=9, textColor=WHITE, fontName="Helvetica", leading=14)
    data = [[Paragraph(escape_cell(h), th) for h in headers]]
    for row in rows:
        data.append([Paragraph(escape_cell(c), td) for c in row])
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


def web_image(local_name, caption=None, fallback_ascii=None):
    """Load image from asset_images folder. Falls back to ASCII art if not found."""
    local_path = os.path.join(ASSET_DIR, local_name)
    if os.path.exists(local_path):
        try:
            img_reader = ImageReader(local_path)
            orig_w, orig_h = img_reader.getSize()
            w = CW * 0.88
            scale = min(w / orig_w, (CW * 0.55) / orig_h)
            img = Image(local_path, width=orig_w * scale, height=orig_h * scale)
            t = Table([[img]], colWidths=[CW])
            t.setStyle(
                TableStyle(
                    [
                        ("BACKGROUND", (0, 0), (-1, -1), CARD_DARK),
                        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                        ("BOX", (0, 0), (-1, -1), 1, CYAN),
                    ]
                )
            )
            add(t)
            if caption:
                add(Paragraph(f"<i>{caption}</i>", CAP_ST))
            sp(8)
            return True
        except Exception as e:
            print(f"[IMG] Load failed for {local_name}: {e}")
    # Fallback
    if fallback_ascii:
        code_block(fallback_ascii)
        if caption:
            add(Paragraph(f"<i>{caption}</i>", CAP_ST))
    return False


def draw_dark_page(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(BG)
    canvas.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
    canvas.restoreState()


def page_number(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(WHITE_DIM)
    canvas.setFont("Helvetica", 9)
    canvas.drawRightString(PAGE_W - PM, PM / 2, str(doc.page))
    canvas.restoreState()


def page_decor(canvas, doc):
    draw_dark_page(canvas, doc)
    page_number(canvas, doc)


# ════════════════════════════════════════════════════════════════════════════
#  COVER PAGE
# ════════════════════════════════════════════════════════════════════════════
sp(18)
cover_box(Paragraph("COMPUTER NETWORKS", COVER_H1))
sp(6)
add(Paragraph("Assignment 1 — Complete Answers", COVER_H2))
add(Paragraph("Subject Code: IT-411 | UIT-RGPV (Autonomous) Bhopal", COVER_INFO))
add(
    Paragraph(
        "Date: 26/03/2026                Date of Submission: 24/04/2026", COVER_INFO
    )
)
sp(4)
rule(CYAN, 1.5)
sp(6)
info_table(
    ["Q. No.", "Topics Covered"],
    [
        ["Q1 a,b,c", "Packet-switched networks, TCP/IP model, Network topologies"],
        ["Q2 a", "Guided transmission media, Twisted pair cable"],
        ["Q3 a,b,c", "CRC error detection, HDLC frame format, ALOHA vs Slotted ALOHA"],
        [
            "Q4 a,b",
            "Bit-oriented framing / byte stuffing, CSMA/CD & collision-free protocols",
        ],
        ["Q5 a,b,c", "Classful IP addressing, Dijkstra's algorithm, ISP subnetting"],
        ["Q6 a,b,c", "Bellman-Ford program, OSPF protocol, DHCP"],
        [
            "Q7 a,b",
            "Transport Layer / Process-to-Process Communication, Bellman-Ford worked example",
        ],
    ],
)
br()

# ════════════════════════════════════════════════════════════════════════════
#  Q1 a
# ════════════════════════════════════════════════════════════════════════════
qbox(
    "Q1a. Describe the operation of a connectionless packet-switched network with the help of a neat diagram."
)
section("Answer")
definition(
    "<b>Connectionless Packet Switching (Datagram Network):</b> A network in which each packet (datagram) is treated as an independent unit. Each packet carries the full source and destination address. Routers make independent forwarding decisions for each packet based on their routing tables. Packets belonging to the same message may take different paths and arrive out of order."
)
subsection("Key Characteristics")
bullet(
    [
        "No connection is established before data transfer begins.",
        "Each packet carries a complete header with source and destination address.",
        "Each router independently decides the next hop for every packet using routing tables.",
        "Packets may arrive out of order — the receiver must reorder them.",
        "No resources are reserved in advance; the network is shared dynamically.",
        "Example protocols: IP (Internet Protocol), UDP.",
    ]
)
subsection("Operation Steps")
bullet(
    [
        "<b>Step 1:</b> The sender breaks the message into fixed or variable-length packets.",
        "<b>Step 2:</b> Each packet is given a sequence number and full destination address.",
        "<b>Step 3:</b> Packets are injected into the network independently.",
        "<b>Step 4:</b> Each router receives a packet, looks up its routing table, and forwards it to the best next hop.",
        "<b>Step 5:</b> Different packets may travel via different routes (dynamic routing).",
        "<b>Step 6:</b> The destination collects all packets, reorders them, and reconstructs the original message.",
    ]
)
web_image(
    "packet_switching.png",
    caption="Fig 1: Connectionless packet-switched (datagram) network — each packet takes an independent route",
    fallback_ascii="""
 CONNECTIONLESS PACKET-SWITCHED NETWORK (DATAGRAM):
 =================================================================

  SENDER                                              RECEIVER
  +------+   Packet 1 (via A->B->D)  +-----------+  +------+
  |      |-->----->----->------------>| Router D  |->|      |
  | Host |   Packet 2 (via A->C->D)  +-----------+  | Host |
  |  S   |-->----->----->------------>| Router D  |->|  R   |
  |      |   Packet 3 (via A->B->D)  +-----------+  |      |
  +------+                                           +------+

  Network topology:
      [S]---[A]---[B]---[D]---[R]
               \       /
               [C]----+

  Packet 1: S -> A -> B -> D -> R
  Packet 2: S -> A -> C -> D -> R   (different path!)
  Packet 3: S -> A -> B -> D -> R

  Each router checks its routing table independently for each packet.
  Packets may arrive at R out of order: 1, 3, 2 -> reordered by R.

 =================================================================
 KEY POINT: No prior connection needed. Each packet = independent datagram.
""",
)
subsection("Advantages and Disadvantages")
info_table(
    ["Advantages", "Disadvantages"],
    [
        [
            "No call setup delay before data transfer.",
            "Packets may arrive out of order — receiver must reorder.",
        ],
        [
            "Network resources shared efficiently — no wasted reserved bandwidth.",
            "Each packet carries full address overhead — less efficient header-to-data ratio.",
        ],
        [
            "Robust: if one router fails, packets take alternate routes.",
            "Variable delay (jitter) — packets experience different queuing delays.",
        ],
        [
            "Simpler network — no connection state to maintain.",
            "No guaranteed delivery or quality of service (unless added by upper layers).",
        ],
    ],
)
sp(6)

# ════════════════════════════════════════════════════════════════════════════
#  Q1 b
# ════════════════════════════════════════════════════════════════════════════
qbox(
    "Q1b. What is meant by logical connection in TCP/IP? Explain the TCP/IP reference model with diagram."
)
section("Answer")
subsection("Logical Connection in TCP/IP")
definition(
    "<b>Logical Connection:</b> A virtual path established between two communicating processes over the network without requiring a dedicated physical circuit. In TCP/IP, a logical connection at the Transport layer (TCP) means both sides agree on connection parameters (sequence numbers, window sizes) before data is exchanged — even though no physical link is reserved. "
    "The underlying packets may travel via different physical paths, but from the application's view, they share a reliable, ordered, bidirectional communication channel."
)
bullet(
    [
        "TCP provides a <b>connection-oriented</b> logical connection using the 3-way handshake (SYN, SYN-ACK, ACK).",
        "UDP provides a <b>connectionless</b> logical communication — no handshake, no guarantee.",
        "Logical connections exist only at the process level; the IP layer below is always connectionless.",
    ]
)
subsection("TCP/IP Reference Model — 4 Layers")
web_image(
    "tcpip_model.png",
    caption="Fig 2: TCP/IP Reference Model — 4 layers with corresponding protocols",
    fallback_ascii="""
 TCP/IP REFERENCE MODEL:
 =================================================================
  +----------------------------------------------------------+
  |  LAYER 4 — APPLICATION LAYER                            |
  |  Protocols: HTTP, FTP, SMTP, DNS, SNMP, Telnet, DHCP   |
  |  Provides: User-facing services, data representation   |
  +----------------------------------------------------------+
  |  LAYER 3 — TRANSPORT LAYER                              |
  |  Protocols: TCP (reliable), UDP (unreliable)            |
  |  Provides: Process-to-process delivery, port numbers   |
  |  TCP: connection-oriented, flow/error control           |
  +----------------------------------------------------------+
  |  LAYER 2 — INTERNET (NETWORK) LAYER                     |
  |  Protocols: IP (IPv4/IPv6), ICMP, ARP, RARP, OSPF      |
  |  Provides: Host-to-host delivery, logical addressing   |
  |  IP addressing (dotted decimal), routing                |
  +----------------------------------------------------------+
  |  LAYER 1 — NETWORK ACCESS (LINK) LAYER                  |
  |  Protocols: Ethernet, Wi-Fi, PPP, HDLC, Token Ring     |
  |  Provides: Node-to-node delivery on same network       |
  |  MAC addressing, framing, physical transmission         |
  +----------------------------------------------------------+
  |  PHYSICAL MEDIUM — Cables, Fiber, Radio waves           |
  +----------------------------------------------------------+
 =================================================================
""",
)
info_table(
    ["Layer", "Name", "Function", "Key Protocols"],
    [
        [
            "4",
            "Application",
            "Provides services directly to user applications. Handles data representation, session management.",
            "HTTP, FTP, SMTP, DNS, DHCP, Telnet, SNMP",
        ],
        [
            "3",
            "Transport",
            "Provides process-to-process (end-to-end) communication using port numbers. Handles segmentation, flow control, error control.",
            "TCP (reliable, connection-oriented), UDP (unreliable, connectionless)",
        ],
        [
            "2",
            "Internet",
            "Provides host-to-host (logical) delivery across multiple networks. Performs routing using IP addresses.",
            "IP (IPv4/v6), ICMP, ARP, RARP, OSPF, BGP",
        ],
        [
            "1",
            "Network Access",
            "Provides node-to-node delivery on a single physical link. Handles framing, MAC addressing, and physical transmission.",
            "Ethernet, Wi-Fi (802.11), PPP, HDLC",
        ],
    ],
)
tip(
    "TCP/IP has 4 layers; OSI has 7. TCP/IP combines OSI's Session + Presentation + Application into one Application layer, and combines Physical + Data Link into Network Access layer."
)
sp(6)

# ════════════════════════════════════════════════════════════════════════════
#  Q1 c
# ════════════════════════════════════════════════════════════════════════════
qbox(
    "Q1c. Explain the four basic topologies used in networks. List advantages and disadvantages of each."
)
section("Answer")
body(
    "A <b>network topology</b> describes the physical or logical arrangement of nodes (computers, switches) and links (cables, connections) in a network."
)
web_image(
    "network_topologies.png",
    caption="Fig 3: Four basic network topologies — Bus, Star, Ring, Mesh",
    fallback_ascii="""
 NETWORK TOPOLOGIES:
 =================================================================
 BUS:          STAR:         RING:         MESH:
 [A]-[B]-[C]   [A] [B]       [A]---[B]    [A]---[B]
  |       |     \ | /         |       |    |\ /  /|
 [D]-----[E]    [HUB]        [D]---[C]    | X  / |
                /|  \                     |/ \ /  |
              [C] [D] [E]               [D]--[C]--+
 =================================================================
""",
)
info_table(
    ["Topology", "Description", "Advantages", "Disadvantages"],
    [
        [
            "<b>Bus</b>",
            "All nodes connected to a single shared backbone cable (bus). Data travels in both directions.",
            "Simple and cheap to install. Easy to extend. Less cable required.",
            "Entire network fails if backbone cable breaks. Performance drops with more devices. Difficult to troubleshoot.",
        ],
        [
            "<b>Star</b>",
            "All nodes connect to a central hub or switch. All communication goes through the central device.",
            "Easy to add/remove nodes. Fault isolation is easy — one node failure doesn't affect others. Easy to manage.",
            "Single point of failure: if central hub fails, entire network goes down. Requires more cable than bus. Hub cost.",
        ],
        [
            "<b>Ring</b>",
            "Each node connects to exactly two other nodes forming a closed loop. Data travels in one direction (or both in dual ring).",
            "Equal access for all nodes (token passing). Predictable performance. No collisions.",
            "Failure of one node or cable can break the entire ring. Adding/removing nodes disrupts the network. Difficult to troubleshoot.",
        ],
        [
            "<b>Mesh</b>",
            "Every node has a dedicated point-to-point link to every other node. Full mesh: n(n-1)/2 links for n nodes.",
            "Highly fault-tolerant — multiple paths exist. High bandwidth. No traffic congestion.",
            "Very expensive — large amount of cabling and ports needed. Complex to install and manage. Not practical for large networks.",
        ],
    ],
)
sp(6)
br()

# ════════════════════════════════════════════════════════════════════════════
#  Q2 a
# ════════════════════════════════════════════════════════════════════════════
qbox("Q2a. What are guided transmission media? Explain twisted pair cable in detail.")
section("Answer")
subsection("Guided Transmission Media")
definition(
    "<b>Guided Transmission Media (Wired Media):</b> Physical cables or conductors that guide (direct) electromagnetic signals along a specific path from sender to receiver. The signal is confined within the medium. Examples: Twisted Pair Cable, Coaxial Cable, Fiber Optic Cable."
)
bullet(
    [
        "<b>Twisted Pair Cable (UTP/STP):</b> Two insulated copper wires twisted together. Most common for LANs and telephone.",
        "<b>Coaxial Cable:</b> Central conductor surrounded by insulation, metallic shield, and outer jacket. Used for cable TV and early Ethernet.",
        "<b>Fiber Optic Cable:</b> Transmits light pulses through glass or plastic fiber. Highest bandwidth and longest distance.",
    ]
)
subsection("Twisted Pair Cable — Detailed Explanation")
web_image(
    "twisted_pair.jpg",
    caption="Fig 4: Twisted pair cable — UTP (left) and STP (right) with color-coded pairs",
    fallback_ascii="""
 TWISTED PAIR CABLE STRUCTURE:
 =================================================================
  UTP (Unshielded Twisted Pair):
   ___________________________________________
  |  Pair 1   |  Pair 2   |  Pair 3  |Pair 4|
  | (White/   | (White/   |(White/   |(White |
  |  Blue &   |  Orange & | Green &  | &    |
  |  Blue)    |  Orange)  | Green)   |Brown)|
  |___________|___________|__________|______|
  Outer Plastic Jacket (PVC)
  No shielding — relies on twisting to cancel noise

  STP (Shielded Twisted Pair):
  Outer Jacket -> Metallic Foil Shield -> Twisted Pairs
  Extra protection against EMI interference
 =================================================================
""",
)
body(
    "A <b>twisted pair cable</b> consists of two separately insulated copper wires that are twisted around each other. The twisting cancels out electromagnetic interference (EMI) from external sources — a principle called <b>noise cancellation</b>."
)
subsection("Why Twist the Wires?")
body(
    "When two parallel wires carry a signal, external electromagnetic fields induce noise in both wires equally. Since the two wires in a twisted pair carry opposite polarity signals, the induced noise (common-mode noise) cancels out when the signals are subtracted at the receiver (differential signaling). More twists per meter = better noise rejection."
)
info_table(
    ["Property", "UTP (Unshielded Twisted Pair)", "STP (Shielded Twisted Pair)"],
    [
        [
            "Structure",
            "Two insulated copper wires twisted, with outer plastic jacket. No metallic shield.",
            "Same as UTP but with a metallic foil or braided shield around each pair or all pairs.",
        ],
        ["Cost", "Cheap — most widely used.", "More expensive than UTP."],
        [
            "Noise Immunity",
            "Lower — relies only on twisting for noise rejection.",
            "Higher — metallic shield provides extra EMI/RFI protection.",
        ],
        [
            "Installation",
            "Easier — flexible, lightweight.",
            "Harder — less flexible, heavier, grounding required.",
        ],
        [
            "Speed",
            "Up to 10 Gbps (Cat 6a, Cat 7)",
            "Up to 10 Gbps and beyond (Cat 7, Cat 8)",
        ],
        [
            "Use Cases",
            "Home/office LAN (Ethernet), telephone lines, DSL.",
            "Industrial environments, high-interference areas, server rooms.",
        ],
    ],
)
subsection("Categories of UTP Cable")
info_table(
    ["Category", "Bandwidth", "Max Speed", "Typical Use"],
    [
        ["Cat 3", "16 MHz", "10 Mbps", "Old telephone, 10BASE-T Ethernet"],
        ["Cat 5", "100 MHz", "100 Mbps", "Fast Ethernet (100BASE-TX)"],
        ["Cat 5e", "100 MHz", "1 Gbps", "Gigabit Ethernet — most common today"],
        ["Cat 6", "250 MHz", "1 Gbps (10 Gbps up to 55m)", "Gigabit LAN, data centers"],
        ["Cat 6a", "500 MHz", "10 Gbps", "10GbE, large offices"],
        ["Cat 7", "600 MHz", "10 Gbps", "Data centers, high-performance LAN"],
    ],
)
sp(6)
br()

# ════════════════════════════════════════════════════════════════════════════
#  Q3 a
# ════════════════════════════════════════════════════════════════════════════
qbox("Q3a. Solve using Cyclic Redundancy Check (CRC). Dataword: 1001, Divisor: 1011.")
section("Answer")
definition(
    "<b>CRC (Cyclic Redundancy Check):</b> An error-detection technique used in data link layer. The sender appends a checksum (CRC remainder) to the dataword. The receiver divides the received frame by the same divisor; if the remainder is 0, no error occurred."
)
subsection("Given")
bullet(
    ["Dataword = 1001", "Divisor (Generator) = 1011  (degree 3, so we append 3 zeros)"]
)
subsection("Step 1: Append zeros to Dataword")
body("Divisor has 4 bits, so degree = 4-1 = 3. Append 3 zeros to the dataword:")
highlight("Dividend = Dataword + 000 = 1001 000", CARD_DARK, CYAN)
subsection("Step 2: Perform Binary Division (XOR division)")
code_block(
    """
 DIVIDEND  :  1001000
 DIVISOR   :  1011

 Step-by-step XOR division:

       1 0 0 0 0 0 0        <- Quotient (we don't need it)
      _______________
 1011 ) 1 0 0 1 0 0 0
         1 0 1 1            <- XOR with 1011 (MSB of divisor aligned with MSB of dividend)
         ---------
           0 1 0 0          <- Result of XOR, bring down next bit -> 0100 0
             0 0 0 0        <- 0100 < 1011, so bring next bit: 01000
               0 0 0 0      <- still less, bring next bit: 010001
                0 0 0 0 0   <- still less, bring: 0100010
                             (only 4-bit groups >= divisor are XOR'd)

 Proper long division:

   1001000
   1011            (align at left, XOR)
   -------
    010000
      (1001 at position 3: 1001 < 1011? No: 1001 < 1011 so bring down)
   Let me redo carefully:

   Position: 1 0 0 1 0 0 0
             _ _ _ _ _ _ _
   Take 4 bits: 1001
   1001 XOR 1011 = 0010  -> bring down next bit -> 0100
   0100 < 1011 (MSB=0), so quotient bit = 0, bring next -> 01000
   01000 -> take 4 bits from left = 0100, still < 1011
   Bring next -> 010001 -> take 4 bits: 0100 < 1011
   Bring next -> 0100010 -> 4 bits: 0100 < 1011
   Hmm, let me redo as standard CRC modulo-2 division:

   Dividend:  1 0 0 1 0 0 0
              ^
   Step 1: Take 1001 (first 4 bits)
           1001 XOR 1011 = 0010
           Remainder so far: 010, bring down next bit (0) -> 0100

   Step 2: 0100 — MSB=0, so quotient=0.
           Cannot divide (< divisor with leading 0 treated as 0000).
           XOR with 0000 -> 0100, bring down next bit (0) -> 01000

   Step 3: 1000 (drop leading 0) -> but we keep 4 bits: 0100 with next=0 -> 01000
           Take 4 bits from group: 1000
           1000 < 1011? 1000=8, 1011=11, YES 8 < 11 -> XOR with 0000
           Remainder: 1000, bring down next (0) -> 10000?

   Standard approach (shown as modulo-2 long division):

              1 0 1 0
           ___________
   1011  | 1 0 0 1 0 0 0
           1 0 1 1
           ---------
             0 1 0 0 0
               0 0 0 0
               -------
               1 0 0 0 0
               1 0 1 1
               ---------
                 0 1 1 0
                   0 0 0 0
                   -------
                   1 1 0 0
                   (remainder is 3 bits so we still need to align)

   CLEAN STANDARD CRC LONG DIVISION:

   1001000  divided by  1011:

   Step 1: 1001 XOR 1011 = 0010, drop leading zero: bring down -> 0100
   Step 2: 0100 < 1011 (leading 0): use 0000 XOR, result=0100, bring down -> 01000
   Step 3: 1000 XOR 1011 = 0011, bring down -> 0110
   Step 4: 0110 < 1011: use 0000 XOR, result=0110

   REMAINDER = 110 (last 3 bits = degree of divisor - 1)

 REMAINDER = 110
"""
)
subsection("Step 3: Form the Transmitted Frame")
highlight(
    "Transmitted Frame = Dataword + Remainder = 1001 + 110 = <b>1001110</b>",
    CARD_DARK,
    CYAN,
)
subsection("Step 4: Verification at Receiver")
code_block(
    """
 Receiver gets: 1001110
 Divide by 1011:

   1001110 XOR division by 1011:
   1001 XOR 1011 = 0010, bring -> 0101
   0101 < 1011: bring -> 01011
   1011 XOR 1011 = 0000, bring -> 0001
   0001 < 1011: 0001 is remainder (padded) = 000

   REMAINDER = 000 -> NO ERROR DETECTED
"""
)
tip(
    "If remainder = 000, transmission is error-free. If remainder != 000, an error occurred. CRC detects all single-bit, double-bit, and burst errors shorter than the generator polynomial."
)
sp(6)

# ════════════════════════════════════════════════════════════════════════════
#  Q3 b
# ════════════════════════════════════════════════════════════════════════════
qbox("Q3b. Write the Frame format of HDLC and explain the individual fields of it.")
section("Answer")
definition(
    "<b>HDLC (High-level Data Link Control):</b> A bit-oriented synchronous data link layer protocol. It uses a frame structure to package data for transmission over a point-to-point or multipoint link. HDLC is the basis for many modern protocols (PPP, Frame Relay, SDLC)."
)
web_image(
    "hdlc_frame.png",
    caption="Fig 5: HDLC frame format showing all fields",
    fallback_ascii="""
 HDLC FRAME FORMAT:
 =================================================================
 | FLAG  | ADDRESS | CONTROL | INFORMATION | FCS     | FLAG  |
 | 8 bits| 8 bits  | 8/16bits| Variable    | 16/32   | 8 bits|
 | 01111110|        |         |             | bits    |01111110|
 =================================================================
""",
)
info_table(
    ["Field", "Size", "Description"],
    [
        [
            "FLAG",
            "8 bits",
            "01111110 (0x7E). Marks the start and end of every HDLC frame. Used for frame synchronization. Bit stuffing is used to prevent 01111110 from appearing inside the frame.",
        ],
        [
            "ADDRESS",
            "8 bits (or multiples)",
            "Identifies the secondary station (receiver) in a multi-drop configuration. In point-to-point links, it identifies the sender or receiver role. Can be extended to multiple bytes.",
        ],
        [
            "CONTROL",
            "8 or 16 bits",
            "Identifies the frame type (I-frame, S-frame, U-frame) and contains sequence numbers for ordering and acknowledgment. Critical for flow and error control.",
        ],
        [
            "INFORMATION",
            "Variable",
            "The actual user data (payload). Present only in I-frames (Information frames). Length depends on the protocol and negotiated MTU.",
        ],
        [
            "FCS",
            "16 or 32 bits",
            "Frame Check Sequence — CRC-based error detection value. The sender calculates CRC over Address + Control + Information fields. Receiver recalculates and compares.",
        ],
        [
            "FLAG",
            "8 bits",
            "01111110 — closing delimiter. Same as opening flag. Signals end of frame.",
        ],
    ],
)
subsection("HDLC Frame Types (Control Field)")
info_table(
    ["Frame Type", "Control Field Pattern", "Purpose"],
    [
        [
            "I-frame (Information)",
            "0 + N(S) + P/F + N(R)",
            "Carries user data. N(S)=send sequence number, N(R)=receive sequence number (piggybacked ACK).",
        ],
        [
            "S-frame (Supervisory)",
            "10 + code + P/F + N(R)",
            "Flow and error control. Subtypes: RR (Receive Ready / ACK), RNR (Receive Not Ready / flow control), REJ (Reject / NAK for Go-Back-N), SREJ (Selective Reject).",
        ],
        [
            "U-frame (Unnumbered)",
            "11 + code + P/F + code",
            "Link management — setup, disconnect, mode setting, error reporting. No sequence numbers.",
        ],
    ],
)
subsection("Bit Stuffing in HDLC")
body(
    "To prevent the flag pattern 01111110 from appearing inside the data, HDLC uses <b>bit stuffing</b>: the sender inserts a 0 bit after every five consecutive 1-bits in the data. The receiver removes any 0 that follows five 1s."
)
code_block(
    """
 BIT STUFFING EXAMPLE:
 Original data:  011111110011
 After stuffing: 0111110110011   (0 inserted after five 1s: 11111 -> 111110)
 Receiver sees:  0111110 -> removes stuffed 0 -> 011111
"""
)
sp(6)

# ════════════════════════════════════════════════════════════════════════════
#  Q3 c
# ════════════════════════════════════════════════════════════════════════════
qbox("Q3c. What is the difference between ALOHA and Slotted ALOHA?")
section("Answer")
definition(
    "<b>ALOHA Protocols:</b> Random access MAC protocols used in shared wireless or satellite channels. Stations transmit whenever they have data; collisions are resolved by retransmission after a random delay."
)
info_table(
    ["Feature", "Pure ALOHA", "Slotted ALOHA"],
    [
        [
            "Transmission Time",
            "Station can transmit at ANY time — completely random.",
            "Station can only transmit at the BEGINNING of a fixed time slot.",
        ],
        [
            "Synchronization",
            "No synchronization required among stations.",
            "All stations must be synchronized to the same global clock/slot boundaries.",
        ],
        [
            "Vulnerable Period",
            "2 * T (two full frame times) — frame must not collide with any frame started in the interval [t-T, t+T].",
            "T (one frame time) — only stations starting in the SAME slot can collide.",
        ],
        [
            "Throughput (S)",
            "S = G * e^(-2G). Maximum = 18.4% at G=0.5.",
            "S = G * e^(-G). Maximum = 36.8% at G=1.0.",
        ],
        ["Maximum Efficiency", "18.4%", "36.8% — exactly double that of Pure ALOHA."],
        [
            "Collision Handling",
            "After collision, each station waits a random backoff time before retransmitting.",
            "After collision, each station waits a random number of slots before retransmitting.",
        ],
        [
            "Complexity",
            "Simpler to implement — no slot management.",
            "Slightly more complex — requires time slot synchronization mechanism.",
        ],
        [
            "Usage",
            "Early satellite systems, simple IoT devices.",
            "802.11 Wi-Fi uses a variant. Widely used in practice.",
        ],
    ],
)
highlight(
    "<b>Key Formula:</b>  Throughput S = G * e^(-aG)  where  a=2 for Pure ALOHA,  a=1 for Slotted ALOHA.  "
    "Maximum throughput of Slotted ALOHA is exactly TWICE that of Pure ALOHA.",
    YELLOW_CARD,
    YELLOW,
)
sp(6)
br()

# ════════════════════════════════════════════════════════════════════════════
#  Q4 a
# ════════════════════════════════════════════════════════════════════════════
qbox(
    "Q4a. What is bit-oriented framing and its frame pattern? Explain byte stuffing and unstuffing in bit-oriented framing with example."
)
section("Answer")
subsection("Bit-Oriented Framing")
definition(
    "<b>Bit-Oriented Framing:</b> A framing technique where the frame boundaries are defined using a specific bit pattern called a <b>flag</b>, rather than character counts or special characters. The entire frame is treated as a stream of bits. HDLC is the most common bit-oriented protocol."
)
bullet(
    [
        "Frame delimiter (flag): <b>01111110</b> (hex 0x7E) — marks start and end of every frame.",
        "Any bit pattern can appear in the data, including control characters.",
        "Problem: The flag pattern 01111110 might appear in the data itself, causing false frame boundaries.",
        "Solution: <b>Bit Stuffing</b> — automatically prevent the flag from appearing in data.",
    ]
)
subsection("Bit Stuffing (Sender Side)")
body(
    "The sender scans the outgoing bit stream. After every five consecutive 1-bits, it inserts (stuffs) a 0-bit. This ensures 01111110 can never appear inside the data field."
)
code_block(
    """
 BIT STUFFING — SENDER:
 =================================================================
 Rule: After FIVE consecutive 1s in data, insert a 0.

 Original Data:   0 1 1 1 1 1 1 0 1 1 1 1 1 0
                              ^                 <- 6 ones here, stuff after 5th
 After Stuffing:  0 1 1 1 1 1[0]1 0 1 1 1 1 1[0]0
                  (0 inserted after every 5 consecutive 1s)

 Another Example:
 Data:            1 1 1 1 1 1 1 1 (eight ones)
 After Stuffing:  1 1 1 1 1 [0] 1 1 1 [0] <- wait, let me redo
                  Count 5: 11111, insert 0 -> 111110
                  Continue with remaining 3 ones: 111
                  Result: 1 1 1 1 1 0 1 1 1
 =================================================================

 COMPLETE EXAMPLE:
 Original Frame Data: 01111101111110
 Step by step (count consecutive 1s):
   0 -> not 1, reset count
   1 -> count=1
   1 -> count=2
   1 -> count=3
   1 -> count=4
   1 -> count=5 -> INSERT 0 now
   0 -> transmitted, reset count
   1 -> count=1
   1 -> count=2
   1 -> count=3
   1 -> count=4
   1 -> count=5 -> INSERT 0
   1 -> count=1
   0 -> transmitted, reset

 Stuffed: 0 11111 [0] 0 11111 [0] 1 0
          01111100111110 10
"""
)
subsection("Bit Unstuffing (Receiver Side)")
body(
    "The receiver performs the reverse. It scans the received bit stream. After every five consecutive 1-bits, it removes (deletes) the very next bit — it must be a stuffed 0. If it finds 01111110 at this point, it's a flag."
)
code_block(
    """
 BIT UNSTUFFING — RECEIVER:
 =================================================================
 Rule: After FIVE consecutive 1s, delete the next bit (it is a stuffed 0).

 Received (after removing flags):
   0 1 1 1 1 1 0 1 1 1 1 1 0 1 0

 Process:
   0 -> pass through
   1,1,1,1,1 -> five ones found!
   Next bit = 0 -> DISCARD IT (stuffed bit)
   Next: 1,1,1,1,1 -> five ones found!
   Next bit = 0 -> DISCARD IT
   Next: 1 -> pass through
   Next: 0 -> pass through

 Recovered Data: 0 1 1 1 1 1 1 1 1 1 1 0
 (matches original data before stuffing)
 =================================================================
"""
)
tip(
    "Bit stuffing is transparent to the upper layers — it happens automatically at the data link layer. The original data is always recovered perfectly."
)
sp(6)

# ════════════════════════════════════════════════════════════════════════════
#  Q4 b
# ════════════════════════════════════════════════════════════════════════════
qbox("Q4b. Explain the flow diagram of CSMA/CD and explain collision-free protocols.")
section("Answer")
subsection("CSMA/CD (Carrier Sense Multiple Access with Collision Detection)")
definition(
    "<b>CSMA/CD:</b> A MAC protocol used in wired Ethernet (IEEE 802.3). Before transmitting, a station senses the channel. If free, it transmits. While transmitting, it continues to monitor for collisions. If a collision is detected, it stops, sends a jam signal, waits a random backoff time, and retries."
)
web_image(
    "csma_cd.png",
    caption="Fig 6: CSMA/CD flow diagram — sense, transmit, detect collision, backoff",
    fallback_ascii="""
 CSMA/CD FLOW DIAGRAM:
 =================================================================
          START: Frame ready to send
                   |
                   v
        +--> Is channel IDLE? <--+
        |      |         |       |
        |      YES       NO      |
        |      |         |       |
        |      v      WAIT and   |
        |  Start        sense    |
        | Transmitting  again ---+
        |      |
        |      v
        |  Collision
        | Detected?
        |   |      |
        |   NO    YES
        |   |      |
        |   v      v
        | Trans- Send JAM signal
        | mission (48 bits)
        | complete  |
        |           v
        +--    Increment attempt
               counter
                   |
               Attempt > 16?
               |         |
              YES         NO
               |          |
               v          v
          Abort Frame  Compute random
                       backoff time
                           |
                           v
                       Wait backoff
                       time slots
                           |
                           +---> back to START
 =================================================================
""",
)
body(
    "The <b>backoff algorithm</b> used in CSMA/CD is the <b>Binary Exponential Backoff (BEB)</b>:"
)
code_block(
    """
 BINARY EXPONENTIAL BACKOFF:
   After k-th collision, wait a random number of slot times r,
   where r is chosen from {0, 1, 2, ..., 2^k - 1}
   k = min(attempt number, 10)
   Maximum attempts before aborting: 16

 Example:
   After 1st collision: wait 0 or 1 slot times
   After 2nd collision: wait 0, 1, 2, or 3 slot times
   After 3rd collision: wait 0-7 slot times
   After 10th collision: wait 0-1023 slot times
"""
)
subsection("Collision-Free Protocols")
body(
    "Collision-free protocols eliminate collisions entirely by controlling which station can transmit at any given time. They are more efficient under heavy load."
)
info_table(
    ["Protocol", "Mechanism", "Advantage", "Disadvantage"],
    [
        [
            "<b>Token Passing</b> (Token Ring / Token Bus)",
            "A special control frame called a 'token' circulates around the ring or bus. Only the station holding the token may transmit. After transmission, the token is passed to the next station.",
            "No collisions. Deterministic access — guaranteed maximum wait time. Fair.",
            "Token overhead. If token is lost (station failure), the ring must regenerate it. Complex management.",
        ],
        [
            "<b>Bitmap Protocol</b>",
            "A reservation phase precedes data transmission. Each station uses one bit slot to announce if it has data. After the bitmap, stations transmit in order.",
            "No collisions. Order is known in advance.",
            "High overhead for the reservation bitmap when traffic is light.",
        ],
        [
            "<b>Binary Countdown</b>",
            "Stations broadcast their address bits (MSB first) during a contention period. Lower-priority stations drop out when they see a higher-priority bit.",
            "No collisions. High-priority stations always win.",
            "Low-priority stations can starve. Address overhead.",
        ],
        [
            "<b>Limited Contention (Adaptive Tree Walk)</b>",
            "Divides stations into groups. Uses a tree-based search to find exactly which stations want to transmit, avoiding wasteful collisions.",
            "Efficient under both light and heavy load. Adapts dynamically.",
            "More complex algorithm. Slight delay from tree search.",
        ],
    ],
)
sp(6)
br()

# ════════════════════════════════════════════════════════════════════════════
#  Q5 a
# ════════════════════════════════════════════════════════════════════════════
qbox("Q5a. Explain the classful addressing system with a neat diagram.")
section("Answer")
definition(
    "<b>Classful IP Addressing (IPv4):</b> The original IP addressing scheme (pre-1993) in which the 32-bit IP address is divided into fixed classes (A, B, C, D, E) based on the leading bits of the address. The class determines how many bits are used for the network ID and how many for the host ID."
)
web_image(
    "classful_ip.png",
    caption="Fig 7: Classful IPv4 addressing — Class A, B, C, D, E ranges",
    fallback_ascii="""
 CLASSFUL IP ADDRESSING:
 =================================================================
 32-bit IP address split into: Network ID | Host ID

 CLASS A:  0xxxxxxx . -------- . -------- . --------
           8-bit net ID (first bit=0), 24-bit host ID
           Range: 0.0.0.0 to 127.255.255.255
           Networks: 128 (2^7)   Hosts per network: 16,777,214 (2^24 - 2)

 CLASS B:  10xxxxxx . xxxxxxxx . -------- . --------
           16-bit net ID (first 2 bits=10), 16-bit host ID
           Range: 128.0.0.0 to 191.255.255.255
           Networks: 16,384 (2^14)   Hosts: 65,534 (2^16 - 2)

 CLASS C:  110xxxxx . xxxxxxxx . xxxxxxxx . --------
           24-bit net ID (first 3 bits=110), 8-bit host ID
           Range: 192.0.0.0 to 223.255.255.255
           Networks: 2,097,152 (2^21)  Hosts: 254 (2^8 - 2)

 CLASS D:  1110xxxx . xxxxxxxx . xxxxxxxx . xxxxxxxx
           First 4 bits = 1110
           Range: 224.0.0.0 to 239.255.255.255
           Purpose: MULTICAST (no network/host split)

 CLASS E:  11110xxx . xxxxxxxx . xxxxxxxx . xxxxxxxx
           Range: 240.0.0.0 to 255.255.255.255
           Purpose: Reserved / Experimental
 =================================================================
""",
)
info_table(
    [
        "Class",
        "Leading Bits",
        "Network Bits",
        "Host Bits",
        "IP Range",
        "Default Mask",
        "Max Hosts",
    ],
    [
        ["A", "0", "8", "24", "0.0.0.0 – 127.255.255.255", "255.0.0.0", "16,777,214"],
        ["B", "10", "16", "16", "128.0.0.0 – 191.255.255.255", "255.255.0.0", "65,534"],
        ["C", "110", "24", "8", "192.0.0.0 – 223.255.255.255", "255.255.255.0", "254"],
        ["D", "1110", "-", "-", "224.0.0.0 – 239.255.255.255", "-", "Multicast"],
        ["E", "11110", "-", "-", "240.0.0.0 – 255.255.255.255", "-", "Reserved"],
    ],
)
body(
    "The two host IDs subtracted (2^n - 2) account for: network address (all host bits = 0) and broadcast address (all host bits = 1), which cannot be assigned to hosts."
)
tip(
    "Classful addressing was replaced by CIDR (Classless Inter-Domain Routing) in 1993 because it wasted large blocks of addresses. For example, a company needing 300 hosts had to get a Class B block (65,534 addresses) — wasting 65,000+ addresses."
)
sp(6)

# ════════════════════════════════════════════════════════════════════════════
#  Q5 b
# ════════════════════════════════════════════════════════════════════════════
qbox(
    "Q5b. Show how to form the least cost tree using Dijkstra's Algorithm with an example."
)
section("Answer")
definition(
    "<b>Dijkstra's Algorithm:</b> A greedy shortest-path algorithm that finds the minimum-cost path from a single source node to ALL other nodes in a weighted graph with non-negative edge weights. It builds a 'least cost tree' rooted at the source."
)
subsection("Algorithm Steps")
bullet(
    [
        "Initialize: distance to source = 0, all others = infinity. Mark all nodes as unvisited.",
        "Select the unvisited node with the smallest known distance — this is the current node.",
        "For each unvisited neighbor of the current node: calculate tentative distance = current distance + edge weight. If this is less than the known distance, update it.",
        "Mark the current node as visited (permanently settled). It will not be revisited.",
        "Repeat steps 2-4 until all nodes are visited.",
    ]
)
subsection("Example Graph")
code_block(
    """
 GRAPH:
        2       3
   A -------- B -------- C
   |         /|          |
  4|       1/ |5         |6
   |       /  |          |
   D ----- E  +--------- F
        3             2

 More explicitly (weighted edges):
   A-B: 2    A-D: 4
   B-C: 3    B-D: 1    B-E: (none)
   B-F: 5    C-F: 6
   D-E: 3    E-F: 2

 ADJACENCY (use simple 5-node example for clarity):
     A
    /|\\
  2/ | \\4
  /  |  \\
 B   |3   C
 |\\  |  /|
1|  \\|/ 2|
 |   D   |
  \\     /
  3\\   /3
    \\ /
     E
 Edge list: A-B=2, A-C=4, A-D=3, B-C=3, B-E=1, C-E=2, D-E=3
"""
)
subsection("Dijkstra Execution — Source: A")
info_table(
    [
        "Step",
        "Current Node",
        "Visited Set",
        "dist[A]",
        "dist[B]",
        "dist[C]",
        "dist[D]",
        "dist[E]",
    ],
    [
        ["Init", "-", "{}", "0", "INF", "INF", "INF", "INF"],
        ["1", "A", "{A}", "0", "2", "4", "3", "INF"],
        ["2", "B", "{A,B}", "0", "2", "4(vs5)", "3", "3 (2+1)"],
        ["3", "B<->E (tie)", "{A,B}", "0", "2", "4", "3", "3"],
        ["4", "E", "{A,B,E}", "0", "2", "4 (vs 3+2=5? 4<5)", "3", "3"],
        ["5", "D", "{A,B,D,E}", "0", "2", "4", "3", "3"],
        ["6", "C", "{A,B,C,D,E}", "0", "2", "4", "3", "3"],
    ],
)
code_block(
    """
 DIJKSTRA — CLEAN STEP-BY-STEP:
 Nodes: A B C D E   Edges: A-B=2, A-C=4, A-D=3, B-C=3, B-E=1, C-E=2, D-E=3
 Source: A

 Initial:  dist = {A:0, B:INF, C:INF, D:INF, E:INF}
           prev = {A:-, B:-,   C:-,   D:-,   E:-  }
           Unvisited = {A, B, C, D, E}

 Iteration 1: Pick A (dist=0, smallest unvisited)
   Update neighbors:
     B: dist[B] = min(INF, 0+2) = 2   prev[B] = A
     C: dist[C] = min(INF, 0+4) = 4   prev[C] = A
     D: dist[D] = min(INF, 0+3) = 3   prev[D] = A
   Mark A visited. Unvisited = {B, C, D, E}
   dist = {A:0, B:2, C:4, D:3, E:INF}

 Iteration 2: Pick B (dist=2, smallest unvisited)
   Update neighbors:
     C: dist[C] = min(4, 2+3) = min(4,5) = 4  (no change)
     E: dist[E] = min(INF, 2+1) = 3   prev[E] = B
   Mark B visited. Unvisited = {C, D, E}
   dist = {A:0, B:2, C:4, D:3, E:3}

 Iteration 3: Pick D (dist=3) or E (dist=3) — pick D (alphabetical)
   Update neighbors:
     E: dist[E] = min(3, 3+3) = min(3,6) = 3  (no change)
   Mark D visited. Unvisited = {C, E}

 Iteration 4: Pick E (dist=3)
   Update neighbors:
     C: dist[C] = min(4, 3+2) = min(4,5) = 4  (no change)
   Mark E visited. Unvisited = {C}

 Iteration 5: Pick C (dist=4)
   No unvisited neighbors.
   Mark C visited. Done!

 FINAL SHORTEST DISTANCES FROM A:
   A -> A : 0      (trivial)
   A -> B : 2      path: A -> B
   A -> C : 4      path: A -> C
   A -> D : 3      path: A -> D
   A -> E : 3      path: A -> B -> E

 LEAST COST TREE:
        A
       /|\\
      2 3  4
     B  D   C
     |
     1
     E
"""
)
tip(
    "For exam: Always show the table with all iterations. Write the shortest path explicitly for each node. Time complexity of Dijkstra: O(V^2) with adjacency matrix, O((V+E) log V) with priority queue."
)
sp(6)

# ════════════════════════════════════════════════════════════════════════════
#  Q5 c
# ════════════════════════════════════════════════════════════════════════════
qbox(
    "Q5c. An ISP is granted block 16.12.64.0/20. Allocate addresses for 8 organizations, each with 256 addresses. Find: (i) ISP block size and range, (ii) each org's range and unallocated addresses, (iii) forwarding table."
)
section("Answer")
subsection("Part (i): ISP Block Analysis")
code_block(
    """
 ISP Block: 16.12.64.0 / 20

 Prefix length = 20 bits
 Number of addresses in ISP block = 2^(32-20) = 2^12 = 4096 addresses

 Network address : 16.12.64.0
 In binary:
   16  = 00010000
   12  = 00001100
   64  = 01000000
   0   = 00000000

 Full binary: 00010000.00001100.01000000.00000000
 First 20 bits (network): 00010000.00001100.0100
 Remaining 12 bits (host): 0000.00000000

 First address (Network): 16.12.64.0
 Last address (Broadcast): 16.12.79.255
   (flip all 12 host bits to 1:
    00010000.00001100.01001111.11111111 = 16.12.79.255)

 ISP Block Range: 16.12.64.0 to 16.12.79.255  (4096 addresses)
"""
)
subsection("Part (ii): Organization Allocation")
body(
    "Each organization needs 256 addresses = 2^8, so each gets a /24 block (32 - 8 = 24 prefix bits)."
)
body(
    "ISP has 4096 addresses / 256 per org = 16 possible /24 blocks. We allocate 8 of them."
)
info_table(
    ["Org", "Block (CIDR)", "First Address", "Last Address", "# Addresses"],
    [
        ["Org 1", "16.12.64.0/24", "16.12.64.0", "16.12.64.255", "256"],
        ["Org 2", "16.12.65.0/24", "16.12.65.0", "16.12.65.255", "256"],
        ["Org 3", "16.12.66.0/24", "16.12.66.0", "16.12.66.255", "256"],
        ["Org 4", "16.12.67.0/24", "16.12.67.0", "16.12.67.255", "256"],
        ["Org 5", "16.12.68.0/24", "16.12.68.0", "16.12.68.255", "256"],
        ["Org 6", "16.12.69.0/24", "16.12.69.0", "16.12.69.255", "256"],
        ["Org 7", "16.12.70.0/24", "16.12.70.0", "16.12.70.255", "256"],
        ["Org 8", "16.12.71.0/24", "16.12.71.0", "16.12.71.255", "256"],
        [
            "<b>UNALLOCATED</b>",
            "16.12.72.0/21 (approx)",
            "16.12.72.0",
            "16.12.79.255",
            "2048",
        ],
    ],
)
code_block(
    """
 UNALLOCATED ADDRESSES:
   8 orgs x 256 = 2048 addresses used
   ISP total     = 4096 addresses
   Unallocated   = 4096 - 2048 = 2048 addresses
   Range         : 16.12.72.0 to 16.12.79.255
"""
)
subsection("Part (iii): Forwarding Table (ISP Router)")
info_table(
    ["Destination Block", "Mask", "Next Hop / Interface"],
    [
        ["16.12.64.0/24", "255.255.255.0", "Interface to Org 1"],
        ["16.12.65.0/24", "255.255.255.0", "Interface to Org 2"],
        ["16.12.66.0/24", "255.255.255.0", "Interface to Org 3"],
        ["16.12.67.0/24", "255.255.255.0", "Interface to Org 4"],
        ["16.12.68.0/24", "255.255.255.0", "Interface to Org 5"],
        ["16.12.69.0/24", "255.255.255.0", "Interface to Org 6"],
        ["16.12.70.0/24", "255.255.255.0", "Interface to Org 7"],
        ["16.12.71.0/24", "255.255.255.0", "Interface to Org 8"],
        ["16.12.72.0/21", "255.255.248.0", "Unallocated (drop or reserve)"],
    ],
)
sp(6)
br()

# ════════════════════════════════════════════════════════════════════════════
#  Q6 a
# ════════════════════════════════════════════════════════════════════════════
qbox("Q6a. Write a program for the Bellman-Ford algorithm.")
section("Answer")
definition(
    "<b>Bellman-Ford Algorithm:</b> A shortest-path algorithm that computes minimum-cost paths from a single source to all nodes in a weighted graph. Unlike Dijkstra's, it can handle <b>negative edge weights</b> and detects <b>negative weight cycles</b>. Time complexity: O(V * E)."
)
code_block(
    """
 // BELLMAN-FORD ALGORITHM — C Program
 #include <stdio.h>
 #include <limits.h>
 #define INF INT_MAX
 #define MAX_V 100
 #define MAX_E 1000

 typedef struct {
     int src, dest, weight;
 } Edge;

 Edge edges[MAX_E];
 int dist[MAX_V];
 int V, E; // number of vertices and edges

 void bellmanFord(int source) {
     // Step 1: Initialize distances
     for (int i = 0; i < V; i++)
         dist[i] = INF;
     dist[source] = 0;

     // Step 2: Relax all edges V-1 times
     for (int i = 1; i <= V - 1; i++) {
         for (int j = 0; j < E; j++) {
             int u = edges[j].src;
             int v = edges[j].dest;
             int w = edges[j].weight;
             if (dist[u] != INF && dist[u] + w < dist[v]) {
                 dist[v] = dist[u] + w;
             }
         }
     }

     // Step 3: Check for negative weight cycles
     for (int j = 0; j < E; j++) {
         int u = edges[j].src;
         int v = edges[j].dest;
         int w = edges[j].weight;
         if (dist[u] != INF && dist[u] + w < dist[v]) {
             printf("Negative weight cycle detected!\\n");
             return;
         }
     }

     // Print results
     printf("Shortest distances from source vertex %d:\\n", source);
     for (int i = 0; i < V; i++) {
         if (dist[i] == INF)
             printf("Vertex %d: INF (unreachable)\\n", i);
         else
             printf("Vertex %d: %d\\n", i, dist[i]);
     }
 }

 int main() {
     printf("Enter number of vertices and edges: ");
     scanf("%d %d", &V, &E);

     printf("Enter edges (src dest weight):\\n");
     for (int i = 0; i < E; i++)
         scanf("%d %d %d", &edges[i].src, &edges[i].dest, &edges[i].weight);

     int source;
     printf("Enter source vertex: ");
     scanf("%d", &source);

     bellmanFord(source);
     return 0;
 }

 /* SAMPLE OUTPUT for graph:
    Vertices: 5, Edges: 8
    0-1:6, 0-2:7, 1-2:8, 1-3:-4, 1-4:5, 2-4:-3, 3-0:2, 4-3:7
    Source: 0

    Shortest distances from source vertex 0:
    Vertex 0: 0
    Vertex 1: 6
    Vertex 2: 7
    Vertex 3: 2
    Vertex 4: 4
 */
"""
)
sp(6)

# ════════════════════════════════════════════════════════════════════════════
#  Q6 b
# ════════════════════════════════════════════════════════════════════════════
qbox("Q6b. Explain Open Shortest Path First (OSPF) Protocol with example.")
section("Answer")
definition(
    "<b>OSPF (Open Shortest Path First):</b> A link-state interior gateway routing protocol (IGP) standardized in RFC 2328. OSPF routers build a complete map of the network topology (LSDB — Link State Database) and independently run Dijkstra's algorithm to compute shortest paths. OSPF is classless (supports CIDR/VLSM) and supports fast convergence."
)
subsection("Key Features of OSPF")
bullet(
    [
        "<b>Link-State Protocol:</b> Each router floods its directly connected link information to ALL routers in the area. Every router builds an identical LSDB.",
        "<b>Dijkstra's SPF Algorithm:</b> Each router independently runs Dijkstra's algorithm on the LSDB to compute a Shortest Path Tree (SPT) rooted at itself.",
        "<b>Areas:</b> Large networks are divided into areas to reduce LSDB size and flooding overhead. Area 0 (backbone area) connects all other areas.",
        "<b>Hello Protocol:</b> OSPF routers send Hello packets every 10 seconds (default) to discover neighbors and confirm they are still alive.",
        "<b>Router Types:</b> DR (Designated Router) and BDR (Backup Designated Router) are elected on multi-access networks to reduce LSA flooding.",
        "<b>Metric:</b> OSPF uses <b>cost</b> = 100 Mbps / link bandwidth as the default metric.",
        "<b>Fast Convergence:</b> Link failures are detected quickly via Hello timeouts (Dead interval = 40 sec default). New LSAs are flooded immediately.",
        "<b>Authentication:</b> OSPF supports MD5 authentication to prevent malicious routing updates.",
    ]
)
web_image(
    "ospf_diagram.png",
    caption="Fig 8: OSPF areas — backbone area 0 connecting multiple areas",
    fallback_ascii="""
 OSPF NETWORK EXAMPLE:
 =================================================================
              [Area 0 — Backbone]
          R1 ---- R2 ---- R3
          |                 |
        Area 1           Area 2
        R4 -- R5         R6 -- R7

 Step 1: Each router sends Hello packets to discover neighbors.
          R1 discovers neighbors: R2, R4
          R2 discovers neighbors: R1, R3

 Step 2: Routers exchange LSAs (Link State Advertisements).
          R1 floods: "I have links to R2 (cost 1) and R4 (cost 5)"
          R2 floods: "I have links to R1 (cost 1) and R3 (cost 2)"
          ... and so on.

 Step 3: All routers build identical LSDB.

 Step 4: Each router runs Dijkstra's algorithm on the LSDB.
          R1 computes: shortest paths to R2, R3, R4, R5, R6, R7.

 Step 5: Routing table is populated with next-hop for each destination.
 =================================================================
""",
)
subsection("OSPF Packet Types")
info_table(
    ["Type", "Packet Name", "Purpose"],
    [
        ["1", "Hello", "Discover neighbors, elect DR/BDR, maintain adjacency."],
        [
            "2",
            "DBD (Database Description)",
            "Summary of LSDB — exchanged when forming adjacency to check if databases match.",
        ],
        [
            "3",
            "LSR (Link State Request)",
            "Request specific LSAs that are missing or outdated.",
        ],
        [
            "4",
            "LSU (Link State Update)",
            "Send the actual LSA data (one or more LSAs). The main data exchange packet.",
        ],
        [
            "5",
            "LSAck (LS Acknowledgment)",
            "Acknowledge receipt of LSAs. OSPF uses reliable flooding.",
        ],
    ],
)
sp(6)

# ════════════════════════════════════════════════════════════════════════════
#  Q6 c
# ════════════════════════════════════════════════════════════════════════════
qbox("Q6c. Explain DHCP and its importance.")
section("Answer")
definition(
    "<b>DHCP (Dynamic Host Configuration Protocol):</b> An application-layer protocol (RFC 2131) that automatically assigns IP addresses and other network configuration parameters to devices on a network. Without DHCP, every device would need to be manually configured with a static IP address, subnet mask, default gateway, and DNS server."
)
web_image(
    "dhcp_process.png",
    caption="Fig 9: DHCP 4-step process — DORA (Discover, Offer, Request, Acknowledge)",
    fallback_ascii="""
 DHCP PROCESS — DORA:
 =================================================================
  CLIENT                                          DHCP SERVER
    |                                                    |
    |--- DHCPDISCOVER (broadcast: 255.255.255.255) ----->|
    |    "I need an IP address!"                         |
    |                                                    |
    |<-- DHCPOFFER (unicast or broadcast) ---------------|
    |    "Here, use IP 192.168.1.10, mask /24, GW .1"   |
    |                                                    |
    |--- DHCPREQUEST (broadcast) ----------------------->|
    |    "I accept the offer from server 192.168.1.1"   |
    |                                                    |
    |<-- DHCPACK (acknowledgment) --------------------- |
    |    "Confirmed! IP 192.168.1.10 is yours for       |
    |     86400 seconds (lease time)"                   |
    |                                                    |
    [CLIENT configures its interface with received params]
 =================================================================
 At lease expiry: client sends DHCPREQUEST to renew, or
                  DHCPRELEASE to give up the address.
""",
)
subsection("DHCP Information Assigned to Client")
bullet(
    [
        "<b>IP Address:</b> A free IP from the server's address pool.",
        "<b>Subnet Mask:</b> Defines the network boundary.",
        "<b>Default Gateway:</b> Router address for packets going outside the subnet.",
        "<b>DNS Server Address:</b> For name-to-IP resolution.",
        "<b>Lease Time:</b> How long the client may use the IP before renewal.",
        "<b>Domain Name:</b> The network domain (e.g. local.example.com).",
    ]
)
subsection("Importance of DHCP")
info_table(
    ["Importance", "Explanation"],
    [
        [
            "Automated IP Management",
            "Eliminates manual configuration of every device. Crucial in large organizations with hundreds/thousands of devices.",
        ],
        [
            "Prevention of IP Conflicts",
            "DHCP server tracks assigned IPs, preventing duplicate address conflicts that cause network failures.",
        ],
        [
            "Efficient IP Reuse",
            "IP addresses are leased (not permanently assigned). When a device leaves the network, the IP is returned to the pool and reassigned.",
        ],
        [
            "Mobility Support",
            "Laptops, phones, and guest devices automatically get the right IP when connecting to any network — no manual setup needed.",
        ],
        [
            "Centralized Management",
            "Network administrators can change DNS servers, gateways, and subnets in one place (the DHCP server) and all clients pick up changes at renewal.",
        ],
        [
            "DHCP Relay",
            "A DHCP relay agent forwards DHCP broadcasts across routers, allowing a single DHCP server to serve multiple subnets.",
        ],
    ],
)
sp(6)
br()

# ════════════════════════════════════════════════════════════════════════════
#  Q7 a
# ════════════════════════════════════════════════════════════════════════════
qbox(
    "Q7a. Explain Transport-Layer Services: Process-to-Process Communication in detail."
)
section("Answer")
definition(
    "<b>Transport Layer (Layer 4 in TCP/IP):</b> Provides logical end-to-end (process-to-process) communication between applications running on different hosts. While the IP layer delivers packets from host to host, the Transport layer delivers data from the correct sending process to the correct receiving process."
)
subsection("Process-to-Process Communication")
body(
    "Multiple processes (applications) can run simultaneously on a single host (e.g., a web browser, email client, and video call app all running at the same time). The Transport layer uses <b>port numbers</b> to identify specific processes and deliver data to the right one."
)
code_block(
    """
 PROCESS-TO-PROCESS COMMUNICATION:
 =================================================================
  HOST A                                    HOST B
  +---------------------------+             +---------------------------+
  | Process 1 (HTTP)  :80    |             | Process 1 (HTTP)  :80    |
  | Process 2 (Email) :25    |             | Process 2 (Email) :25    |
  | Process 3 (FTP)   :21    |             | Process 3 (FTP)   :21    |
  |      |       |      |    |             |      |       |      |    |
  | TRANSPORT LAYER (TCP/UDP)|             | TRANSPORT LAYER (TCP/UDP)|
  |   Port numbers identify  |             |   Port numbers identify  |
  |   which process gets data|             |   which process gets data|
  +------------+-------------+             +-------------+------------+
               |      IP + Port = Socket                 |
               |                                         |
  +------------+-----------------------------------------+------------+
  |                    INTERNET LAYER (IP)                            |
  |              Host-to-host delivery via IP addresses               |
  +-------------------------------------------------------------------+

  Socket = IP Address : Port Number
  e.g. 192.168.1.5 : 80   (web server socket)
       10.0.0.1 : 54321   (client ephemeral port)
 =================================================================
"""
)
subsection("Port Numbers")
info_table(
    ["Port Range", "Category", "Examples"],
    [
        [
            "0 – 1023",
            "Well-Known Ports (IANA reserved)",
            "HTTP:80, HTTPS:443, FTP:21, SSH:22, SMTP:25, DNS:53, DHCP:67/68, Telnet:23",
        ],
        [
            "1024 – 49151",
            "Registered Ports",
            "MySQL:3306, PostgreSQL:5432, RDP:3389, HTTP alt:8080",
        ],
        [
            "49152 – 65535",
            "Dynamic/Ephemeral Ports",
            "Assigned temporarily by OS for client-side connections. Freed after connection closes.",
        ],
    ],
)
subsection("Transport Layer Services")
info_table(
    ["Service", "TCP Provides", "UDP Provides"],
    [
        [
            "Connection",
            "Connection-oriented: 3-way handshake (SYN-SYNACK-ACK) before data.",
            "Connectionless: no handshake. Data sent immediately.",
        ],
        [
            "Reliability",
            "Guaranteed delivery: retransmits lost segments using ACKs and timers.",
            "No reliability: lost packets are NOT retransmitted.",
        ],
        [
            "Ordering",
            "Sequence numbers ensure segments arrive in correct order.",
            "No ordering: packets may arrive out of order.",
        ],
        [
            "Flow Control",
            "Window-based flow control prevents sender from overwhelming receiver.",
            "No flow control.",
        ],
        [
            "Error Control",
            "Checksum + retransmission for error correction.",
            "Checksum only — error detection but no correction.",
        ],
        [
            "Congestion Ctrl",
            "Slow start, congestion avoidance, fast retransmit.",
            "No congestion control — sends at full rate.",
        ],
        [
            "Speed",
            "Slower due to overhead.",
            "Faster — minimal overhead. Good for real-time apps.",
        ],
        [
            "Use Cases",
            "HTTP/S, FTP, SMTP, SSH — where reliability matters.",
            "DNS, streaming, VoIP, gaming — where speed matters.",
        ],
    ],
)
subsection("Multiplexing and Demultiplexing")
body(
    "<b>Multiplexing (Sender):</b> The Transport layer collects data from multiple application processes, encapsulates each in a segment with the appropriate source and destination port numbers, and passes them down to the IP layer."
)
body(
    "<b>Demultiplexing (Receiver):</b> The Transport layer receives segments from the IP layer, reads the destination port number, and delivers the data to the correct application process."
)
sp(6)

# ════════════════════════════════════════════════════════════════════════════
#  Q7 b
# ════════════════════════════════════════════════════════════════════════════
qbox("Q7b. Calculate the shortest path by Bellman-Ford algorithm for the given graph.")
section("Answer")
body(
    "The graph from the assignment is referenced below. A general worked example is shown here, which matches the standard 5-node graph typically used in RGPV exams."
)
web_image(
    "bellman_ford.png",
    caption="Fig 10: Graph for Bellman-Ford algorithm (use the graph from your assignment sheet)",
    fallback_ascii="""
 GRAPH FOR BELLMAN-FORD (Standard RGPV Example):
 =================================================================
  Vertices: A(0), B(1), C(2), D(3), E(4)   Source = A

  Edges (directed, with weights):
    A -> B : 6       A -> D : 7
    B -> C : 5       B -> D : 8       B -> E : -4
    C -> B : -2
    D -> C : -3      D -> E : 9
    E -> A : 2       E -> C : 7

  Diagram:
       6       5
  A ------> B ----> C
  |       ^ |     ^ ^
  7|      | |8   /3  |7
  |    -2 | |   /-3  |
  v  <--- C  v /    v
  D -----> E     from E
      9
  A <-- E (weight 2)
 =================================================================
""",
)
code_block(
    """
 BELLMAN-FORD EXECUTION:
 =================================================================
 Graph: 5 vertices (A=0, B=1, C=2, D=3, E=4), Source = A

 Edges:
  A->B:6, A->D:7, B->C:5, B->D:8, B->E:-4,
  C->B:-2, D->C:-3, D->E:9, E->A:2, E->C:7

 INITIALIZATION:
   dist[A]=0, dist[B]=INF, dist[C]=INF, dist[D]=INF, dist[E]=INF
   prev[all] = none

 ---- ITERATION 1 (Relax all edges once) ----
 Process A->B:  dist[B] = min(INF, 0+6)  = 6    prev[B]=A
 Process A->D:  dist[D] = min(INF, 0+7)  = 7    prev[D]=A
 Process B->C:  dist[C] = min(INF, 6+5)  = 11   prev[C]=B
 Process B->D:  dist[D] = min(7,   6+8)  = 7    (no change)
 Process B->E:  dist[E] = min(INF, 6+-4) = 2    prev[E]=B
 Process C->B:  dist[B] = min(6, 11+-2)  = 6    (no change)
 Process D->C:  dist[C] = min(11, 7+-3)  = 4    prev[C]=D
 Process D->E:  dist[E] = min(2, 7+9)    = 2    (no change)
 Process E->A:  dist[A] = min(0, 2+2)    = 0    (no change)
 Process E->C:  dist[C] = min(4, 2+7)    = 4    (no change)

 After iter 1: dist={A:0, B:6, C:4, D:7, E:2}

 ---- ITERATION 2 (Relax all edges again) ----
 Process A->B:  dist[B] = min(6, 0+6)   = 6    (no change)
 Process A->D:  dist[D] = min(7, 0+7)   = 7    (no change)
 Process B->C:  dist[C] = min(4, 6+5)   = 4    (no change)
 Process B->D:  dist[D] = min(7, 6+8)   = 7    (no change)
 Process B->E:  dist[E] = min(2, 6+-4)  = 2    (no change)
 Process C->B:  dist[B] = min(6, 4+-2)  = 2    prev[B]=C   <-- UPDATED
 Process D->C:  dist[C] = min(4, 7+-3)  = 4    (no change)
 Process D->E:  dist[E] = min(2, 7+9)   = 2    (no change)
 Process E->A:  dist[A] = min(0, 2+2)   = 0    (no change)
 Process E->C:  dist[C] = min(4, 2+7)   = 4    (no change)

 After iter 2: dist={A:0, B:2, C:4, D:7, E:2}

 ---- ITERATION 3 ----
 Process C->B:  dist[B] = min(2, 4+-2)  = 2    (no change)
 Process B->E:  dist[E] = min(2, 2+-4)  = -2   prev[E]=B   <-- UPDATED

 After iter 3: dist={A:0, B:2, C:4, D:7, E:-2}

 ---- ITERATION 4 ----
 Process E->C:  dist[C] = min(4, -2+7)  = 4    (no change, 5>4)
 Process E->A:  dist[A] = min(0, -2+2)  = 0    (no change)

 No more updates. Algorithm converges.

 ---- NEGATIVE CYCLE CHECK ----
 Try one more relaxation of all edges:
   No distance decreases -> NO negative cycle.

 FINAL SHORTEST DISTANCES FROM A:
 +--------+----------+------------------------------+
 | Vertex | Distance | Shortest Path                |
 +--------+----------+------------------------------+
 | A      | 0        | A (source)                   |
 | B      | 2        | A -> B -> ... (via C->B)      |
 |        |          | A->B->C->B? No: A->D->C->B   |
 |        |          | 0+7-3-2 = 2. Path: A->D->C->B|
 | C      | 4        | A -> D -> C (0+7-3 = 4)      |
 | D      | 7        | A -> D (direct, weight 7)    |
 | E      | -2       | A -> D -> C -> B -> E        |
 |        |          | 0+7-3-2-4 = -2               |
 +--------+----------+------------------------------+
"""
)
tip(
    "Bellman-Ford runs V-1 iterations. For V=5, run exactly 4 iterations. Then do ONE more check for negative cycles. If any distance decreases in the 5th iteration -> negative cycle exists."
)
sp(6)
br()

# ════════════════════════════════════════════════════════════════════════════
#  QUICK REVISION TABLE
# ════════════════════════════════════════════════════════════════════════════
part_box("QUICK REVISION — KEY FORMULAS AND CONCEPTS", CARD_DARK, GREEN)
chap_box("Quick Reference Summary", CARD_MID, GREEN)
info_table(
    ["Topic", "Key Point / Formula"],
    [
        [
            "Packet Switching",
            "Connectionless (datagram): each packet routed independently. Connection-oriented (virtual circuit): path set up first.",
        ],
        [
            "TCP/IP Layers",
            "4 layers: Application | Transport | Internet | Network Access. (OSI has 7.)",
        ],
        [
            "Topologies",
            "Bus: shared cable. Star: central hub (SPOF). Ring: token passing. Mesh: n(n-1)/2 links.",
        ],
        [
            "Twisted Pair",
            "UTP cheaper, STP better noise immunity. Cat5e: 1Gbps, Cat6a: 10Gbps. Twisting cancels EMI.",
        ],
        [
            "CRC",
            "Append (degree-of-divisor) zeros. XOR divide. Remainder = FCS. Receiver divides: if 0, no error.",
        ],
        [
            "HDLC",
            "Flag(8)|Address(8)|Control(8/16)|Info(var)|FCS(16/32)|Flag(8). Bit stuffing: insert 0 after five 1s.",
        ],
        [
            "ALOHA",
            "Pure ALOHA: max 18.4% efficiency. Slotted ALOHA: max 36.8% (exactly double). S = G*e^(-aG).",
        ],
        [
            "CSMA/CD",
            "Sense -> Transmit -> Detect collision -> JAM -> Binary Exponential Backoff -> Retry. Max 16 attempts.",
        ],
        [
            "Classful IP",
            "A: /8, first bit=0. B: /16, first 2=10. C: /24, first 3=110. D: multicast. E: reserved.",
        ],
        [
            "CIDR/Subnetting",
            "Hosts = 2^(host bits) - 2. Block size = 2^(32-prefix). ISP /20 = 4096 addresses.",
        ],
        [
            "Dijkstra",
            "Greedy, non-negative weights only. O(V^2). Builds shortest path tree from source. No negative edges.",
        ],
        [
            "Bellman-Ford",
            "Dynamic programming. Handles negative weights. O(V*E). V-1 iterations + 1 cycle check.",
        ],
        [
            "OSPF",
            "Link-state IGP. Floods LSAs. All routers have same LSDB. Each runs Dijkstra. Area 0 = backbone.",
        ],
        [
            "DHCP",
            "DORA: Discover -> Offer -> Request -> Acknowledge. Assigns IP, mask, gateway, DNS, lease time.",
        ],
        [
            "Transport Layer",
            "Process-to-process via port numbers. Socket = IP:Port. Multiplexing/Demultiplexing. TCP vs UDP.",
        ],
        [
            "TCP vs UDP",
            "TCP: reliable, ordered, flow/congestion control, slow. UDP: fast, no reliability, connectionless.",
        ],
    ],
)
highlight(
    "<b>Exam Tips:</b> "
    "For CRC always show the XOR division step by step. "
    "For Dijkstra and Bellman-Ford always show a table with all iterations. "
    "For subnetting show binary breakdown. "
    "For HDLC draw the full frame format. "
    "Always define the protocol before explaining it.",
    YELLOW_CARD,
    YELLOW,
)

# ════════════════════════════════════════════════════════════════════════════
#  BUILD PDF
# ════════════════════════════════════════════════════════════════════════════
doc = SimpleDocTemplate(
    "CN_Assignment.pdf",
    pagesize=A4,
    leftMargin=PM,
    rightMargin=PM,
    topMargin=PM,
    bottomMargin=PM,
    title="Computer Networks IT-411 Assignment 1",
    author="UIT-RGPV",
)
doc.build(story, onFirstPage=page_decor, onLaterPages=page_decor)
print("PDF built successfully: CN_Assignment.pdf")
