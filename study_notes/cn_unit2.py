"""
Computer Networks (IT-411) -- Unit II Notes
UIT-RGPV (Autonomous) Bhopal | Semester IV
Complete exam notes with vector diagrams.
Run: python cn_unit2_notes.py
Output: CN_Unit2_Notes.pdf
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

PAGE_W, PAGE_H = A4
PM = 1.8 * cm
CW = PAGE_W - 2 * PM

# -- Colour palette -----------------------------------------------------------
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


# -- Style definitions --------------------------------------------------------
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


# -- Core helpers -------------------------------------------------------------
def add(x: Flowable) -> None:
    story.append(x)


def sp(h: float = 8) -> None:
    add(Spacer(1, h))


def rule(c: Color = CYAN, t: float = 0.6) -> None:
    add(HRFlowable(width="100%", thickness=t, color=c, spaceAfter=6, spaceBefore=2))


def br() -> None:
    add(PageBreak())


# -- Layout blocks ------------------------------------------------------------
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


def frame_format(caption: str, fields: list[tuple[str, str]]) -> None:
    headers = [f"<b>{name}</b>" for name, _ in fields]
    sizes = [size for _, size in fields]

    # Text styles
    th = S("F_HDR", fontSize=8.5, textColor=colors.HexColor("#79c0ff"), fontName="Helvetica-Bold", alignment=TA_CENTER, leading=11)
    td = S("F_SZ", fontSize=7.5, textColor=colors.HexColor("#9da7b3"), fontName="Helvetica-Oblique", alignment=TA_CENTER, leading=10)

    data = [
        [Paragraph(h, th) for h in headers],
        [Paragraph(s, td) for s in sizes]
    ]

    col_widths = []
    total_w = sum(max(len(name), len(size)) for name, size in fields)
    for name, size in fields:
        w = max(len(name), len(size))
        col_widths.append(max(30.0, CW * (w / total_w)))

    scale = CW / sum(col_widths)
    col_widths = [w * scale for w in col_widths]

    t = Table(data, colWidths=col_widths)
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#161b22")),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("GRID", (0, 0), (-1, -1), 1.0, colors.HexColor("#30363d")),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                ("LEFTPADDING", (0, 0), (-1, -1), 2),
                ("RIGHTPADDING", (0, 0), (-1, -1), 2),
            ]
        )
    )

    add(t)
    if caption:
        add(Spacer(1, 4))
        add(Paragraph(f"<i>{caption}</i>", S("F_CAP", fontSize=8.5, textColor=colors.HexColor("#9da7b3"), fontName="Helvetica-Oblique", alignment=TA_CENTER, leading=12)))
    sp(6)


# -- Page decoration ----------------------------------------------------------
def page_decor(canvas: Canvas, doc: BaseDocTemplate) -> None:
    canvas.saveState()
    canvas.setFillColor(BG)
    canvas.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
    canvas.setFillColor(WHITE_DIM)
    canvas.setFont("Helvetica", 9)
    canvas.drawRightString(PAGE_W - PM, PM / 2, str(doc.page))
    canvas.restoreState()


# =============================================================================
#  COVER PAGE
# =============================================================================
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
add(Paragraph("Unit II -- Complete Exam Notes", COVER_H2))
add(Paragraph("Subject Code: IT-411  |  UIT-RGPV (Autonomous) Bhopal", COVER_SUB))
add(Paragraph("Semester IV  |  Based on University Syllabus 2024-25", COVER_SUB))
sp(10)
rule(CYAN, 1.5)
sp(8)

info_table(
    ["Topic", "Coverage"],
    [
        [
            "2.1 Switching Techniques",
            "Circuit switching, Packet switching, Hybrid switching -- comparison and diagrams",
        ],
        [
            "2.2 Data Link Layer Design Issues",
            "Services, framing methods, error and flow control overview",
        ],
        [
            "2.3 Framing",
            "Character count, byte stuffing, bit stuffing, physical layer coding violations",
        ],
        [
            "2.4 Error Detection and Correction",
            "Parity, CRC, Hamming code, checksum -- worked examples",
        ],
        ["2.5 Flow Control", "Stop-and-Wait protocol with timing diagram"],
        [
            "2.6 ARQ Protocols",
            "Go-Back-N ARQ, Selective Repeat ARQ, window sizes, comparison",
        ],
        [
            "2.7 Piggybacking and Pipelining",
            "Concepts, efficiency formulas, worked examples",
        ],
        ["2.8 Link Layer Addressing", "MAC address structure, ARP, RARP"],
        ["2.9 HDLC", "Frame format, frame types, bit stuffing -- exam favourite"],
        [
            "2.10 LAN Protocol Stack",
            "LLC and MAC sublayers, IEEE 802.2 LLC frame format",
        ],
        ["2.11 Quick Revision Summary", "Key formulas, mnemonics, and exam flashcards"],
    ],
)
br()


# =============================================================================
#  UNIT II DIVIDER
# =============================================================================
part_box("UNIT II -- DATA LINK LAYER AND SWITCHING TECHNIQUES")


# -----------------------------------------------------------------------------
#  2.1  SWITCHING TECHNIQUES
# -----------------------------------------------------------------------------
chap_box("2.1  Switching Techniques")
section("Introduction")
definition(
    "<b>Switching:</b> The mechanism by which a network establishes a path (or routes "
    "data) between a sender and a receiver. Three fundamental switching techniques are "
    "used in communication networks: Circuit Switching, Packet Switching, and "
    "Hybrid (Message) Switching. The choice of technique affects delay, efficiency, "
    "and reliability."
)

section("Circuit Switching")
definition(
    "<b>Circuit Switching:</b> A switching technique in which a dedicated communication "
    "path (circuit) is established between the source and destination before data "
    "transfer begins. The path is reserved for the entire duration of the call and "
    "is released only after the communication is complete. The traditional Public "
    "Switched Telephone Network (PSTN) uses circuit switching."
)
subsection("Three Phases of Circuit Switching")
bullet(
    [
        "<b>Phase 1 -- Circuit Establishment:</b> A dedicated end-to-end path is set up "
        "through the network by reserving resources (bandwidth, switch capacity) at each "
        "intermediate node. This is a signalling phase and introduces setup delay.",
        "<b>Phase 2 -- Data Transfer:</b> Data flows continuously over the reserved circuit "
        "at the full reserved bandwidth. Delay is constant and predictable -- ideal for "
        "voice. Bandwidth is wasted if the channel is silent.",
        "<b>Phase 3 -- Circuit Teardown:</b> After communication ends, a teardown signal "
        "is sent to release all reserved resources along the path.",
    ]
)
subsection("Characteristics")
bullet(
    [
        "Guaranteed bandwidth and constant delay -- suitable for real-time voice/video.",
        "Inefficient for bursty data (resources wasted during silence).",
        "Blocking: if all circuits are busy, new connections are rejected.",
        "Examples: PSTN telephone network, ISDN, early mobile networks (GSM voice calls).",
    ]
)

# Circuit switching sequence diagram
seq_cs = pd.SequenceDiagram(
    width=CW,
    height=230,
    caption="Fig 1: Circuit Switching -- three phases (setup, transfer, teardown)",
)
seq_cs.actor("src", "Source (A)")
seq_cs.actor("sw1", "Switch 1")
seq_cs.actor("sw2", "Switch 2")
seq_cs.actor("dst", "Destination (B)")
seq_cs.message("src", "sw1", "Circuit request", arrow="solid")
seq_cs.message("sw1", "sw2", "Circuit request", arrow="solid")
seq_cs.message("sw2", "dst", "Circuit request", arrow="solid")
seq_cs.message("dst", "sw2", "Circuit accept", arrow="dashed")
seq_cs.message("sw2", "sw1", "Circuit accept", arrow="dashed")
seq_cs.message("sw1", "src", "Circuit ready", arrow="dashed")
seq_cs.divider("Data Transfer Phase -- reserved circuit in use")
seq_cs.message("src", "dst", "Continuous data stream", arrow="solid")
seq_cs.divider("Teardown Phase")
seq_cs.message("src", "sw1", "Disconnect signal", arrow="solid")
seq_cs.message("sw1", "sw2", "Disconnect signal", arrow="solid")
seq_cs.message("sw2", "dst", "Disconnect signal", arrow="solid")
story.extend(seq_cs.as_flowable())

section("Packet Switching")
definition(
    "<b>Packet Switching:</b> A switching technique in which data is broken into small "
    "units called <b>packets</b>. Each packet carries the full source and destination "
    "address and is forwarded independently through the network. No dedicated path is "
    "established in advance. The Internet is built on packet switching."
)
subsection("Two Approaches to Packet Switching")
bullet(
    [
        "<b>Datagram (Connectionless):</b> Each packet is treated as an independent entity. "
        "Routers make a forwarding decision for every packet individually. Packets may "
        "arrive out of order. Example: IP (Internet Protocol).",
        "<b>Virtual Circuit (Connection-Oriented):</b> A logical path (virtual circuit) is "
        "established before data transfer. All packets follow the same path in order. "
        "Resources are NOT fully reserved (unlike circuit switching). Example: ATM, X.25.",
    ]
)
subsection("Store-and-Forward Operation")
body(
    "Each intermediate node (router) receives the entire packet, stores it in a buffer, "
    "checks it for errors, and then forwards it to the next node. This introduces "
    "<b>store-and-forward delay</b> at each hop."
)
code_block("""
 STORE-AND-FORWARD DELAY CALCULATION:
 ======================================================
 Transmission delay per link = L / R
   L = packet size in bits
   R = link rate in bps

 For a 3-link path (2 intermediate routers):
   Total delay = 3 * (L / R)    [ignoring propagation delay]

 Example: L = 10,000 bits, R = 1 Mbps, 3 links
   Delay = 3 * (10,000 / 1,000,000) = 0.03 seconds = 30 ms
""")

# Packet switching network diagram
ps_net = pd.NetworkDiagram(
    width=CW,
    height=180,
    caption="Fig 2: Packet Switching -- packets routed independently through the network",
)
ps_net.node("src", "Source", kind="host")
ps_net.node("r1", "Router A", kind="router")
ps_net.node("r2", "Router B", kind="router")
ps_net.node("r4", "Router D", kind="router")
ps_net.node("r3", "Router C", kind="router")
ps_net.node("dst", "Destination", kind="host")
ps_net.link("src", "r1")
ps_net.link("r1", "r2", label="Pkt 1")
ps_net.link("r1", "r4", label="Pkt 2")
ps_net.link("r2", "r3")
ps_net.link("r4", "r3")
ps_net.link("r3", "dst")
story.extend(ps_net.as_flowable())

section("Hybrid (Message) Switching")
definition(
    "<b>Message Switching:</b> An intermediate technique (precursor to packet switching) "
    "in which the entire message (not broken into packets) is stored at each intermediate "
    "node and then forwarded when the outgoing link is available. Also called "
    "<b>store-and-forward switching</b> at the message level. No dedicated path is needed."
)
bullet(
    [
        "The entire message is stored at each hop -- large buffer requirements.",
        "No blocking: messages are queued if the link is busy.",
        "Not suitable for interactive or real-time communication due to high delay.",
        "Used in early telegraph networks and email systems.",
        "Packet switching is superior: packets are smaller, so delay is less and buffers are smaller.",
    ]
)

section("Switching Techniques Comparison")
info_table(
    ["Feature", "Circuit Switching", "Message Switching", "Packet Switching"],
    [
        [
            "Path",
            "Dedicated end-to-end circuit",
            "No fixed path -- hop-by-hop",
            "No fixed path (datagram) or virtual circuit",
        ],
        [
            "Setup",
            "Required before transfer",
            "Not required",
            "Not required (datagram)",
        ],
        [
            "Delay",
            "Low and constant after setup",
            "Very high (whole message stored)",
            "Low -- only packet-size delay per hop",
        ],
        [
            "Bandwidth Use",
            "Inefficient -- reserved even when idle",
            "Efficient -- shared",
            "Efficient -- shared dynamically",
        ],
        [
            "Ordering",
            "In order (constant path)",
            "In order",
            "Out of order possible (datagram)",
        ],
        [
            "Blocking",
            "Yes -- if circuit unavailable",
            "No -- message queued",
            "No -- packets queued",
        ],
        [
            "Buffering",
            "None needed at switches",
            "Large (entire message)",
            "Small (one packet at a time)",
        ],
        ["Error Control", "None at network level", "Per hop", "Per hop or end-to-end"],
        ["Examples", "PSTN telephone, ISDN", "Email, telegraph", "Internet (IP), ATM"],
    ],
)
tip(
    "Circuit switching guarantees bandwidth but wastes it during silence. "
    "Packet switching is efficient for bursty data. Message switching is obsolete -- "
    "replaced by packet switching. Exam often asks for a 3-way comparison table."
)
br()


# -----------------------------------------------------------------------------
#  2.2  DATA LINK LAYER DESIGN ISSUES
# -----------------------------------------------------------------------------
chap_box("2.2  Data Link Layer -- Design Issues")
section("Role of the Data Link Layer")
definition(
    "<b>Data Link Layer (Layer 2 of OSI):</b> Responsible for reliable node-to-node "
    "(hop-by-hop) delivery of frames over a single communication link. It takes raw "
    "bits from the Physical layer and packages them into meaningful units called "
    "<b>frames</b>, detects errors, controls the flow of data, and manages access to "
    "the shared medium."
)

section("Services Provided by the Data Link Layer")
subsection("1. Unacknowledged Connectionless Service")
body(
    "Frames are sent without any connection setup and without expecting acknowledgements. "
    "No error recovery -- lost frames are simply lost. Suitable for low-error links "
    "(Ethernet LAN) or real-time applications where retransmission is useless (VoIP). "
    "Example: Ethernet."
)
subsection("2. Acknowledged Connectionless Service")
body(
    "Frames are sent without connection setup, but each frame is individually "
    "acknowledged. If an ACK is not received within a timeout, the frame is retransmitted. "
    "Useful for unreliable channels (Wi-Fi 802.11 uses this at the link layer)."
)
subsection("3. Acknowledged Connection-Oriented Service")
body(
    "A connection is first established, frames are numbered and acknowledged, and "
    "the connection is explicitly released afterwards. Guarantees exactly-once delivery "
    "in the correct order. Used in some WAN protocols such as HDLC and X.25."
)

section("Key Design Issues at the Data Link Layer")
info_table(
    ["Design Issue", "Description", "Solution / Mechanism"],
    [
        [
            "Framing",
            "How to delimit the start and end of a frame from a raw bit stream.",
            "Character count, byte stuffing, bit stuffing, physical layer violations.",
        ],
        [
            "Error Detection",
            "Detect bits that were flipped during transmission.",
            "Parity bits, CRC (Cyclic Redundancy Check), checksum.",
        ],
        [
            "Error Correction",
            "Recover the original data without retransmission.",
            "Hamming code, Reed-Solomon code (forward error correction -- FEC).",
        ],
        [
            "Flow Control",
            "Prevent a fast sender from overwhelming a slow receiver.",
            "Stop-and-Wait, sliding window (Go-Back-N, Selective Repeat).",
        ],
        [
            "ARQ (Error Control)",
            "Handle lost or corrupted frames via retransmission.",
            "Stop-and-Wait ARQ, Go-Back-N ARQ, Selective Repeat ARQ.",
        ],
        [
            "Link Layer Addressing",
            "Identify the sender and receiver on a shared medium.",
            "MAC (Media Access Control) addresses -- 48-bit hardware address.",
        ],
        [
            "Medium Access",
            "Decide which station transmits on a shared channel.",
            "CSMA/CD (Ethernet), token passing, TDMA, ALOHA (covered in Unit III).",
        ],
    ],
)
br()


# -----------------------------------------------------------------------------
#  2.3  FRAMING
# -----------------------------------------------------------------------------
chap_box("2.3  Framing")
section("What is Framing?")
definition(
    "<b>Framing:</b> The process of dividing the continuous bit stream received from "
    "the Physical layer into discrete units called <b>frames</b>, each with a clear "
    "start and end boundary. Without framing, the receiver cannot determine where one "
    "frame ends and the next begins."
)

section("Method 1: Character Count")
body(
    "The first field in the frame header contains a count of the total number of "
    "characters (bytes) in the frame, including the count field itself. The receiver "
    "reads the count, accepts that many bytes, then starts reading the next frame."
)
code_block("""
 CHARACTER COUNT FRAMING:
 =====================================================
 | 5 | D | A | T | A |  5  | M | O | R | E |  ...
   ^                    ^
   Count = 5 bytes      Count = 5 bytes (next frame)

 PROBLEM: If the count field is corrupted (e.g., 5 -> 7),
 the receiver will misalign and all subsequent frames are lost.
 This method is rarely used alone for this reason.
""")

section("Method 2: Byte Stuffing (Character Stuffing)")
body(
    "Special byte sequences mark the start (FLAG = 01111110 or a specific byte like "
    "DLE STX) and end (DLE ETX) of a frame. If the flag sequence appears in the data, "
    "an escape byte (DLE) is inserted before it."
)
code_block("""
 BYTE STUFFING (PPP-style using FLAG = 0x7E, ESC = 0x7D):
 =============================================================
 Rule:  If 0x7E appears in data -> replace with 0x7D 0x5E
        If 0x7D appears in data -> replace with 0x7D 0x5D

 Original data:  48 7E 45 7D 23
 After stuffing: 48 7D 5E 45 7D 5D 23
                     ^^^         ^^^
                  7E escaped    7D escaped

 Frame on wire: | FLAG | 48 7D 5E 45 7D 5D 23 | FLAG |
                | 0x7E |                       | 0x7E |

 UNSTUFFING (receiver):
   Read byte: if 0x7D, read next byte and XOR with 0x20 to recover original.
   0x7D 0x5E -> 0x5E XOR 0x20 = 0x7E (original)
   0x7D 0x5D -> 0x5D XOR 0x20 = 0x7D (original)
""")

section("Method 3: Bit Stuffing (HDLC / Zero-Bit Insertion)")
body(
    "Used in bit-oriented protocols like HDLC. The frame delimiter is the flag "
    "01111110. To prevent this pattern from appearing in data, the sender inserts "
    "a 0 after every five consecutive 1-bits in the data. The receiver removes any "
    "0 that follows five consecutive 1s."
)
code_block("""
 BIT STUFFING (HDLC):
 =============================================================
 Flag:  01111110  (marks start and end of every frame)

 SENDER RULE: After 5 consecutive 1s in data, insert a 0.

 Original data:   0 1 1 1 1 1 0 1 1 1 1 1 1 0
                        ^^^^^               ^^^^^^
 After stuffing:  0 1 1 1 1 1[0]0 1 1 1 1 1[0]1 0
                  (a 0 inserted after each run of 5 ones)

 RECEIVER RULE: After 5 consecutive 1s, delete the next bit (must be 0).
   If the next bit is 1, and the bit after is 0 -> flag 01111110 detected.

 WHY: Ensures the flag pattern can NEVER appear inside the data field.
""")

section("Method 4: Physical Layer Coding Violations")
body(
    "Some physical encoding schemes (e.g., Manchester encoding used in 802.3) "
    "have reserved signal patterns that never appear in normal data. These invalid "
    "patterns are used as frame delimiters. For example, in 4B/5B encoding, "
    "certain 5-bit codes are reserved for control purposes (start-of-frame, "
    "end-of-frame). This requires no overhead in the data field."
)
info_table(
    ["Framing Method", "Mechanism", "Drawback", "Used In"],
    [
        [
            "Character Count",
            "First field = byte count of frame",
            "One corrupted count loses sync for all frames",
            "Rarely used alone",
        ],
        [
            "Byte Stuffing",
            "FLAG byte + ESC byte; stuff ESC before FLAG in data",
            "Extra bytes added; only works for byte-aligned data",
            "PPP, BSC, SLIP",
        ],
        [
            "Bit Stuffing",
            "Insert 0 after every five consecutive 1s in data",
            "Slight overhead; clock sync needed",
            "HDLC, SDLC, X.25",
        ],
        [
            "Coding Violations",
            "Reserved physical signals used as delimiters",
            "Depends on specific physical encoding; not universal",
            "802.3 (Ethernet), FDDI",
        ],
    ],
)
tip(
    "Bit stuffing is the most important framing method for exams. Know the rule: "
    "insert 0 after 5 ones (sender), remove 0 after 5 ones (receiver). "
    "HDLC flag = 01111110."
)
br()


# -----------------------------------------------------------------------------
#  2.4  ERROR DETECTION AND CORRECTION
# -----------------------------------------------------------------------------
chap_box("2.4  Error Detection and Correction")
section("Types of Errors")
bullet(
    [
        "<b>Single-Bit Error:</b> Only one bit in the data unit changes from 0 to 1 or "
        "1 to 0. Rare in serial communication but common in parallel.",
        "<b>Burst Error:</b> Two or more consecutive bits are corrupted. More common in "
        "real networks -- caused by noise, interference, or fading. Burst length = "
        "distance from first corrupted bit to last.",
    ]
)

section("Error Detection Techniques")
subsection("1. Simple Parity Check (VRC -- Vertical Redundancy Check)")
body(
    "A single parity bit is appended to each data unit. For <b>even parity</b>, the "
    "total number of 1s (including parity bit) must be even. For <b>odd parity</b>, "
    "total 1s must be odd. Detects all single-bit errors and all odd-number-of-bit "
    "errors. Does NOT detect even-number-of-bit errors."
)
code_block("""
 EVEN PARITY EXAMPLE:
 =====================================================
 Data:        1 0 1 1 0 1 1     (five 1s -- odd count)
 Parity bit:  1                 (add 1 to make count even = 6)
 Transmitted: 1 0 1 1 0 1 1 1

 If receiver gets 1 0 0 1 0 1 1 1  (1 bit flipped)
   Count of 1s = 5 (odd) -> ERROR DETECTED

 If receiver gets 1 0 0 1 0 0 1 1  (2 bits flipped)
   Count of 1s = 4 (even) -> ERROR NOT DETECTED (parity passes)
""")

subsection("2. Two-Dimensional Parity (LRC -- Longitudinal Redundancy Check)")
body(
    "Data is organized in a 2D matrix (rows and columns). A parity bit is added "
    "for each row AND each column. Detects all single-bit errors, all odd-number "
    "burst errors, and can correct single-bit errors (by pinpointing the row and "
    "column intersection)."
)

subsection("3. CRC -- Cyclic Redundancy Check")
definition(
    "<b>CRC:</b> The most powerful and widely used error detection technique. Based "
    "on binary polynomial division (modulo-2 arithmetic -- XOR instead of subtraction). "
    "The sender appends a remainder (FCS -- Frame Check Sequence) to the data. "
    "The receiver divides the received frame by the same generator polynomial; if the "
    "remainder is 0, no error is detected."
)
body("<b>CRC Algorithm -- Sender Side:</b>")
bullet(
    [
        "Step 1: Agree on a generator polynomial G(x) of degree r (r+1 bits).",
        "Step 2: Append r zeros to the end of the dataword (multiply by x<super>r</super>).",
        "Step 3: Divide the augmented dataword by G(x) using modulo-2 (XOR) division.",
        "Step 4: The remainder R (r bits) is the CRC. Append it to the original dataword.",
        "Step 5: Transmit Dataword + CRC (the transmitted frame is exactly divisible by G(x)).",
    ]
)
code_block("""
 CRC WORKED EXAMPLE:
 =====================================================
 Dataword:  1 1 0 1 0 1 1
 Generator: 1 0 1 1  (degree 3, so r=3, append 3 zeros)

 Augmented: 1 1 0 1 0 1 1 0 0 0

 Modulo-2 division (XOR at each step):

   1101011000  divided by  1011:

   Take 4 bits: 1101
   1101 XOR 1011 = 0110  -> bring down next bit -> 1100

   Take 4 bits: 1100
   1100 XOR 1011 = 0111  -> bring down next bit -> 1110

   Take 4 bits: 1110
   1110 XOR 1011 = 0101  -> bring down next bit -> 1011

   Take 4 bits: 1011
   1011 XOR 1011 = 0000  -> bring down next bit -> 0001

   Take 4 bits: 0001 (leading 0, MSB < divisor)
   XOR with 0000 = 0001  -> bring down next bit -> 0010

   Remaining 3 bits: 010

 CRC REMAINDER = 010

 Transmitted Frame = 1101011 + 010 = 1101011010

 RECEIVER VERIFICATION:
   Divide 1101011010 by 1011:
   Remainder = 000 -> NO ERROR

 CRC detects: all single-bit, double-bit, all odd-count errors,
 and all burst errors of length <= degree of generator.
""")

subsection("4. Checksum")
body(
    "Used in TCP, UDP, and IP headers. The sender divides the data into 16-bit "
    "segments, adds them using ones-complement addition, and takes the complement "
    "of the sum. The result is the checksum. The receiver adds all segments including "
    "the checksum -- if the result is all 1s (0xFFFF in ones-complement), no error."
)
code_block("""
 ONES-COMPLEMENT CHECKSUM EXAMPLE:
 =====================================================
 Segment 1: 1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0
 Segment 2: 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0
 Sum (ones-complement):
   1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0
 + 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0
 = 0 1 1 1 0 1 1 1 0 1 1 1 0 1 1 0  (with carry-around if needed)
 Checksum = ones-complement of sum = 1 0 0 0 1 0 0 0 1 0 0 0 1 0 0 1

 Receiver: adds all segments + checksum -> result = 1111...1111 -> OK
""")

section("Error Correction -- Hamming Code")
definition(
    "<b>Hamming Code:</b> A Forward Error Correction (FEC) technique that adds "
    "redundant bits at specific positions (powers of 2: 1, 2, 4, 8, ...) so that "
    "the receiver can not only detect but also <b>correct</b> single-bit errors "
    "without retransmission."
)
body(
    "<b>Formula:</b> For m data bits, the number of parity bits r must satisfy: "
    "2<super>r</super> >= m + r + 1"
)
code_block("""
 HAMMING CODE EXAMPLE (even parity):
 =====================================================
 Data bits: d1=1, d2=0, d3=1, d4=1  (m=4 data bits)

 Parity bits needed: 2^r >= 4+r+1
   r=3: 2^3=8 >= 4+3+1=8  YES -> r=3 parity bits

 Positions: p1(1), p2(2), d1(3), p4(4), d2(5), d3(6), d4(7)
             1      0      1      ?      0      1      1

 Calculate each parity bit (even parity):
   p1 (pos 1): covers positions 1,3,5,7 -> values: p1,1,0,1
               p1 + 1 + 0 + 1 = even -> p1 = 0
   p2 (pos 2): covers positions 2,3,6,7 -> values: p2,1,1,1
               p2 + 1 + 1 + 1 = even -> p2 = 1
   p4 (pos 4): covers positions 4,5,6,7 -> values: p4,0,1,1
               p4 + 0 + 1 + 1 = even -> p4 = 0

 Transmitted Hamming codeword: 0 1 1 0 0 1 1
 Positions:                     1 2 3 4 5 6 7

 ERROR DETECTION AND CORRECTION:
   Suppose bit at position 5 is flipped: 0 1 1 0 1 1 1
   Receiver recalculates parity:
     p1 (1,3,5,7): 0+1+1+1 = 3 (odd) -> ERROR in p1 group
     p2 (2,3,6,7): 1+1+1+1 = 4 (even) -> OK
     p4 (4,5,6,7): 0+1+1+1 = 3 (odd) -> ERROR in p4 group
   Error position = p1 + p4 = 1 + 4 = 5 -> Flip bit 5 -> CORRECTED
""")

info_table(
    ["Technique", "Detects", "Corrects", "Overhead", "Used In"],
    [
        [
            "Parity bit",
            "Single-bit, odd-count errors",
            "No",
            "1 bit per unit",
            "Serial comms, RAM (basic)",
        ],
        [
            "2D Parity",
            "All single-bit, burst < 1 row",
            "Single-bit only",
            "Row + column parity bits",
            "Older protocols",
        ],
        [
            "CRC-16",
            "All burst errors <= 16 bits",
            "No",
            "16-bit FCS",
            "Ethernet, PPP, USB",
        ],
        [
            "CRC-32",
            "All burst errors <= 32 bits",
            "No",
            "32-bit FCS",
            "Ethernet 802.3, ZIP, PNG",
        ],
        [
            "Hamming Code",
            "Double-bit errors (if extended)",
            "Single-bit errors",
            "r bits where 2<super>r</super> >= m+r+1",
            "RAM ECC, satellite links",
        ],
        ["Checksum", "Some burst errors", "No", "16-bit sum", "TCP, UDP, IP headers"],
    ],
)
tip(
    "CRC is the most exam-important error detection technique. Know the XOR division "
    "steps. For Hamming code, remember: parity positions are powers of 2 (1,2,4,8...). "
    "Error position = sum of failing parity bit positions."
)
br()


# -----------------------------------------------------------------------------
#  2.5  FLOW CONTROL -- STOP-AND-WAIT
# -----------------------------------------------------------------------------
chap_box("2.5  Flow Control and Stop-and-Wait Protocol")
section("Why Flow Control?")
definition(
    "<b>Flow Control:</b> A mechanism that prevents a fast sender from overwhelming "
    "a slow receiver by regulating the rate at which data is sent. Without flow "
    "control, the receiver's buffer would overflow, causing frame loss."
)

section("Stop-and-Wait Protocol")
definition(
    "<b>Stop-and-Wait:</b> The simplest ARQ (Automatic Repeat reQuest) protocol. "
    "The sender transmits ONE frame, then STOPS and WAITS for an acknowledgement (ACK) "
    "from the receiver before sending the next frame. If no ACK arrives within a "
    "timeout period, the sender retransmits the same frame."
)
subsection("Operation")
bullet(
    [
        "Sender transmits Frame 0 and starts a timer.",
        "Receiver gets Frame 0, checks for errors. If OK, sends ACK 0.",
        "Sender receives ACK 0, stops timer, and sends Frame 1.",
        "If sender's timer expires before ACK arrives -> retransmit Frame 0.",
        "1-bit sequence numbers (0 and 1) are sufficient to distinguish consecutive frames.",
    ]
)

# Stop-and-Wait timing diagram
seq_sw = pd.SequenceDiagram(
    width=CW,
    height=290,
    caption="Fig 3: Stop-and-Wait -- normal operation and timeout-retransmit",
)
seq_sw.actor("tx", "Sender")
seq_sw.actor("rx", "Receiver")
seq_sw.message("tx", "rx", "Frame 0", arrow="solid")
seq_sw.message("rx", "tx", "ACK 0", arrow="dashed")
seq_sw.message("tx", "rx", "Frame 1", arrow="solid")
seq_sw.message("rx", "tx", "ACK 1", arrow="dashed")
seq_sw.divider("Frame lost -- timeout scenario")
seq_sw.message("tx", "rx", "Frame 0 (lost)", arrow="solid")
seq_sw.message("tx", "rx", "Frame 0 (retransmit after timeout)", arrow="solid")
seq_sw.message("rx", "tx", "ACK 0", arrow="dashed")
story.extend(seq_sw.as_flowable())

section("Efficiency of Stop-and-Wait")
body(
    "Stop-and-Wait is highly inefficient over high-bandwidth-delay-product links "
    "(satellite or long-distance fiber) because the sender is idle while waiting "
    "for the ACK."
)
code_block("""
 EFFICIENCY FORMULA FOR STOP-AND-WAIT:
 =====================================================
 Let:
   T_t = Transmission time = L / R  (L = frame size, R = link rate)
   T_p = Propagation delay (one-way)
   a   = T_p / T_t  (normalised propagation delay)

 Efficiency (eta) = 1 / (1 + 2a)

 Example: L=1000 bits, R=1Mbps, T_p=250ms
   T_t = 1000/1,000,000 = 1 ms
   a   = 250/1 = 250
   Efficiency = 1/(1+500) = 0.2% !!

 -> Stop-and-Wait is almost useless on long high-speed links.
 -> Solution: Pipelining -- send multiple frames before receiving ACK.
""")
tip(
    "Efficiency of Stop-and-Wait = 1/(1+2a). As propagation delay increases "
    "(a increases), efficiency collapses. Sliding window protocols solve this."
)
br()


# -----------------------------------------------------------------------------
#  2.6  ARQ PROTOCOLS
# -----------------------------------------------------------------------------
chap_box("2.6  ARQ Protocols -- Go-Back-N and Selective Repeat")
section("Sliding Window Concept")
definition(
    "<b>Sliding Window:</b> A flow and error control mechanism that allows the sender "
    "to have multiple unacknowledged frames outstanding at any time (up to the window "
    "size W). As ACKs arrive, the window slides forward, allowing new frames to be "
    "sent. This keeps the channel busy even over long-delay links."
)
body(
    "Window size W must satisfy: W >= 1 + 2a to fully utilise the channel bandwidth, "
    "where a = T<sub>p</sub> / T<sub>t</sub>."
)
code_block("""
 SLIDING WINDOW EFFICIENCY:
 =====================================================
 If W >= 1 + 2a:   Efficiency = 1  (100% channel utilisation)
 If W <  1 + 2a:   Efficiency = W / (1 + 2a)

 Example: a = 10, W = 7
   1 + 2*10 = 21
   W < 21  -> Efficiency = 7/21 = 33%
   Need W >= 21 for 100% efficiency.
""")

section("Go-Back-N ARQ (GBN)")
definition(
    "<b>Go-Back-N ARQ:</b> A sliding window protocol in which the sender may have "
    "up to <b>W = 2<super>n</super> - 1</b> unacknowledged frames outstanding (where n = number of "
    "sequence number bits). If a frame error is detected (or a timeout occurs), the "
    "receiver DISCARDS that frame and all subsequent frames already received, and the "
    "sender RETRANSMITS from the erroneous frame onwards -- it 'goes back N' frames."
)
subsection("Key Rules")
bullet(
    [
        "<b>Sender window size:</b> W<sub>s</sub> = 2<super>n</super> - 1 (for n-bit sequence numbers).",
        "<b>Receiver window size:</b> W<sub>r</sub> = 1 (receiver only buffers one frame at a time).",
        "Receiver uses <b>cumulative ACK</b>: ACK k means all frames up to k-1 received OK.",
        "If frame i is lost or corrupted, the receiver discards frames i+1, i+2, ... and "
        "sends REJ i (Reject/NAK). Sender retransmits frame i, i+1, i+2, ...",
        "Receiver window size is 1 -- no out-of-order buffering at the receiver.",
    ]
)
code_block("""
 GO-BACK-N EXAMPLE (n=3 bits, W=7):
 =====================================================
 Sequence numbers: 0 1 2 3 4 5 6 7 0 1 2 3 ...

 Sender sends: 0 1 2 3 4 5 6
 Frame 3 is corrupted (error detected by CRC)

 Receiver:
   Accepts 0, 1, 2 (sends ACK 1, ACK 2, ACK 3 cumulatively)
   Rejects frame 3 -> sends REJ 3
   Discards frames 4, 5, 6 (already received but cannot buffer out-of-order)

 Sender receives REJ 3:
   Goes back and retransmits: 3, 4, 5, 6, ...

 WASTED TRANSMISSION: frames 4, 5, 6 retransmitted even though correct!
 This is the inefficiency of Go-Back-N.
""")

# Go-Back-N sequence diagram
seq_gbn = pd.SequenceDiagram(
    width=CW,
    height=310,
    caption="Fig 4: Go-Back-N ARQ -- frame 3 lost, sender goes back and retransmits 3,4,5,6",
)
seq_gbn.actor("tx", "Sender")
seq_gbn.actor("rx", "Receiver")
seq_gbn.message("tx", "rx", "Frame 0", arrow="solid")
seq_gbn.message("tx", "rx", "Frame 1", arrow="solid")
seq_gbn.message("tx", "rx", "Frame 2", arrow="solid")
seq_gbn.message("tx", "rx", "Frame 3 (LOST)", arrow="solid")
seq_gbn.message("rx", "tx", "ACK 1", arrow="dashed")
seq_gbn.message("rx", "tx", "ACK 2", arrow="dashed")
seq_gbn.message("rx", "tx", "ACK 3", arrow="dashed")
seq_gbn.message("tx", "rx", "Frame 4 (discarded by RX)", arrow="solid")
seq_gbn.message("tx", "rx", "Frame 5 (discarded by RX)", arrow="solid")
seq_gbn.message("rx", "tx", "REJ 4 (go back!)", arrow="dashed")
seq_gbn.divider("Sender retransmits from frame 4 onwards")
seq_gbn.message("tx", "rx", "Frame 4 (retransmit)", arrow="solid")
seq_gbn.message("tx", "rx", "Frame 5 (retransmit)", arrow="solid")
seq_gbn.message("rx", "tx", "ACK 5", arrow="dashed")
seq_gbn.message("rx", "tx", "ACK 6", arrow="dashed")
story.extend(seq_gbn.as_flowable())

section("Selective Repeat ARQ (SR)")
definition(
    "<b>Selective Repeat ARQ:</b> A sliding window protocol that retransmits ONLY "
    "the specific frame(s) that were lost or corrupted -- not all subsequent frames. "
    "The receiver buffers out-of-order frames until the missing frame arrives and "
    "is correctly inserted."
)
subsection("Key Rules")
bullet(
    [
        "<b>Sender window size:</b> W<sub>s</sub> = 2<super>n-1</super> (half the sequence number space).",
        "<b>Receiver window size:</b> W<sub>r</sub> = 2<super>n-1</super> (same as sender -- receiver can buffer).",
        "Receiver sends NAK (negative ACK) for the specific missing frame.",
        "Sender retransmits ONLY the NAK'd frame.",
        "Receiver buffers correctly received out-of-order frames and delivers them "
        "in order to the upper layer once the gap is filled.",
    ]
)
code_block("""
 SELECTIVE REPEAT EXAMPLE (n=3 bits, W=4):
 =====================================================
 Sender sends: 0 1 2 3 4 5 6 7
 Frame 2 is lost.

 Receiver:
   Accepts 0 -> ACK 1
   Accepts 1 -> ACK 2
   Frame 2 lost -> sends NAK 2
   Accepts 3 -> buffers (out of order, waiting for 2)
   Accepts 4 -> buffers
   ...

 Sender receives NAK 2:
   Retransmits ONLY Frame 2.

 Receiver receives Frame 2:
   Delivers 2, 3, 4 in order to upper layer.
   Sends ACK 3, ACK 4, ACK 5 (cumulative).

 ADVANTAGE over GBN: Only one frame retransmitted, not all subsequent ones.
 COST: Receiver needs larger buffer (W_r = 2^(n-1)).
""")

# Selective Repeat is shown separately to contrast its single retransmission with GBN.
seq_sr = pd.SequenceDiagram(
    width=CW,
    height=300,
    caption="Fig 5: Selective Repeat ARQ -- only the missing frame is retransmitted",
)
seq_sr.actor("tx", "Sender")
seq_sr.actor("rx", "Receiver")
seq_sr.message("tx", "rx", "Frame 0", arrow="solid")
seq_sr.message("tx", "rx", "Frame 1", arrow="solid")
seq_sr.message("tx", "rx", "Frame 2 (LOST)", arrow="solid")
seq_sr.message("tx", "rx", "Frame 3 (buffered)", arrow="solid")
seq_sr.message("tx", "rx", "Frame 4 (buffered)", arrow="solid")
seq_sr.message("rx", "tx", "NAK 2 only", arrow="dashed")
seq_sr.divider("Receiver retains frames 3 and 4 while the gap is filled")
seq_sr.message("tx", "rx", "Frame 2 (retransmit only)", arrow="solid")
seq_sr.message("rx", "tx", "ACK 5 -- deliver 2,3,4 in order", arrow="dashed")
story.extend(seq_sr.as_flowable())

section("Go-Back-N vs Selective Repeat Comparison")
info_table(
    ["Feature", "Go-Back-N ARQ", "Selective Repeat ARQ"],
    [
        [
            "Sender window (W<sub>s</sub>)",
            "2<super>n</super> - 1 (almost full seq space)",
            "2<super>n-1</super> (half of seq space)",
        ],
        [
            "Receiver window (W<sub>r</sub>)",
            "1 (no out-of-order buffering)",
            "2<super>n-1</super> (buffering required)",
        ],
        [
            "Retransmission",
            "Erroneous frame AND all subsequent frames",
            "ONLY the erroneous frame",
        ],
        ["Receiver buffer", "None needed", "Buffer of size W<sub>r</sub> needed"],
        [
            "ACK type",
            "Cumulative ACK (ACK k = frames 0..k-1 received)",
            "Individual ACK or NAK for specific frame",
        ],
        [
            "Efficiency",
            "Lower on error-prone links (retransmits many frames)",
            "Higher -- only bad frames retransmitted",
        ],
        [
            "Complexity",
            "Simpler -- receiver logic is trivial",
            "More complex -- receiver must reorder frames",
        ],
        ["Seq numbers (3-bit example)", "W<sub>s</sub> = 7 (0..6), W<sub>r</sub> = 1", "W<sub>s</sub> = 4, W<sub>r</sub> = 4"],
    ],
)
highlight(
    "<b>Window Size Rule (CRITICAL for exams):</b>  "
    "Go-Back-N: W<sub>s</sub> = 2<super>n</super> - 1, W<sub>r</sub> = 1.  "
    "Selective Repeat: W<sub>s</sub> = W<sub>r</sub> = 2<super>n-1</super>.  "
    "For n=3 bits: GBN window = 7, SR window = 4.  "
    "For n=4 bits: GBN window = 15, SR window = 8.",
    CARD_DARK,
    CYAN,
)
tip(
    "If sequence numbers are 3 bits (0-7), GBN uses window=7, SR uses window=4. "
    "SR window = half of sequence space to avoid ambiguity when ACKs are lost."
)
br()


# -----------------------------------------------------------------------------
#  2.7  PIGGYBACKING AND PIPELINING
# -----------------------------------------------------------------------------
chap_box("2.7  Piggybacking and Pipelining")
section("Piggybacking")
definition(
    "<b>Piggybacking:</b> The technique of attaching an acknowledgement (ACK) for "
    "the last received data frame to an outgoing data frame travelling in the opposite "
    "direction. Instead of sending a separate ACK frame, the ACK is 'piggybacked' onto "
    "the next data frame, saving bandwidth."
)
body(
    "Piggybacking is used in full-duplex protocols like TCP and HDLC. The ACK field "
    "in a data frame serves as confirmation of frames received in the reverse direction."
)
code_block("""
 PIGGYBACKING EXAMPLE:
 =====================================================
 Without piggybacking (separate ACK):
   A -> B: [Data Frame 0]
   B -> A: [ACK 0]             <- separate ACK frame overhead
   A -> B: [Data Frame 1]
   B -> A: [ACK 1]

 With piggybacking (ACK embedded in data frame):
   A -> B: [Data Frame 0]
   B -> A: [Data Frame 0 | ACK(A's frame 0)]   <- combined!
   A -> B: [Data Frame 1 | ACK(B's frame 0)]   <- combined!

 BENEFIT: Halves the number of frames on the channel.
 COST:    A slight delay -- the receiver must wait a moment for an
          outgoing data frame to attach the ACK to. If no data comes
          soon, a separate ACK must be sent anyway (timer-based).
""")
tip(
    "TCP uses piggybacking extensively. The ACK number in a TCP segment "
    "acknowledges data received from the other side while carrying new data. "
    "This is why TCP is called a full-duplex protocol."
)

section("Pipelining")
definition(
    "<b>Pipelining:</b> The technique of sending multiple frames without waiting "
    "for an acknowledgement for each one. The sender keeps the link busy by "
    "maintaining a window of outstanding unacknowledged frames. Both Go-Back-N "
    "and Selective Repeat are pipelined protocols."
)
code_block("""
 PIPELINING EFFICIENCY:
 =====================================================
 Parameters:
   T_t = Frame transmission time = L / R
   T_p = One-way propagation delay
   a   = T_p / T_t

 Without pipelining (Stop-and-Wait):
   Efficiency = 1 / (1 + 2a)
   (sender idle for 2*T_p per frame)

 With pipelining (window size W):
   If W >= 1 + 2a: Efficiency = 1 (100%)
   If W <  1 + 2a: Efficiency = W / (1 + 2a)

 EXAMPLE:
   L = 1000 bits, R = 1 Mbps, T_p = 20 ms
   T_t = 1 ms, a = 20
   1 + 2a = 41

   Stop-and-Wait: Efficiency = 1/41 = 2.44%
   GBN (W=7):     Efficiency = 7/41 = 17.1%
   GBN (W=41):    Efficiency = 41/41 = 100%
   SR  (W=21):    Efficiency = 21/41 = 51.2%  (W_s = 21 for n=5 bits)
""")
br()


# -----------------------------------------------------------------------------
#  2.8  LINK LAYER ADDRESSING
# -----------------------------------------------------------------------------
chap_box("2.8  Link Layer Addressing -- MAC Addresses, ARP, RARP")
section("MAC Address (Physical Address)")
definition(
    "<b>MAC Address (Media Access Control Address):</b> A 48-bit hardware address "
    "permanently assigned to a Network Interface Card (NIC) by the manufacturer. "
    "Used at the Data Link layer to identify devices on the same local network segment. "
    "Every Ethernet and Wi-Fi frame contains source and destination MAC addresses."
)
bullet(
    [
        "48 bits = 6 bytes, written as 6 hexadecimal pairs: e.g. 00:1A:2B:3C:4D:5E",
        "<b>First 3 bytes (OUI):</b> Organizationally Unique Identifier -- identifies "
        "the manufacturer (assigned by IEEE). e.g. 00:1A:2B = a specific vendor.",
        "<b>Last 3 bytes:</b> Device serial number assigned by the manufacturer.",
        "Broadcast MAC address: FF:FF:FF:FF:FF:FF -- all devices on the LAN accept this.",
        "Multicast MAC addresses start with 01 in the first byte.",
        "MAC addresses operate at Layer 2; IP addresses operate at Layer 3.",
        "Routers replace the source and destination MAC address at every hop; "
        "IP addresses remain unchanged end-to-end.",
    ]
)

section("ARP -- Address Resolution Protocol")
definition(
    "<b>ARP (Address Resolution Protocol):</b> A protocol used to discover the "
    "MAC address of a device on the same local network when only its IP address "
    "is known. ARP maps Layer 3 (IP) addresses to Layer 2 (MAC) addresses."
)
subsection("ARP Operation")
bullet(
    [
        "Host A wants to send a packet to IP 192.168.1.5 but does not know its MAC.",
        "A broadcasts an ARP Request: 'Who has IP 192.168.1.5? Tell 192.168.1.1 (my IP).'",
        "All hosts on the LAN receive the broadcast.",
        "Host B (which has IP 192.168.1.5) sends a unicast ARP Reply with its MAC address.",
        "Host A receives the reply, stores the mapping in its ARP cache (table), "
        "and now frames can be sent directly to B's MAC address.",
        "ARP cache entries expire after a few minutes to handle IP address changes.",
    ]
)

# ARP sequence diagram
seq_arp = pd.SequenceDiagram(
    width=CW,
    height=230,
    caption="Fig 6: ARP operation -- broadcast request, unicast reply",
)
seq_arp.actor("a", "Host A")
seq_arp.actor("sw", "LAN Switch")
seq_arp.actor("b", "Host B")
seq_arp.actor("c", "Host C")
seq_arp.message("a", "sw", "ARP Request (broadcast): Who has .1.5?", arrow="solid")
seq_arp.message("sw", "b", "ARP Request (forwarded to all ports)", arrow="solid")
seq_arp.message("sw", "c", "ARP Request (forwarded to all ports)", arrow="solid")
seq_arp.message(
    "b", "a", "ARP Reply (unicast): .1.5 is at 00:1A:2B:3C:4D:5E", arrow="dashed"
)
seq_arp.divider("Host A caches the mapping and sends data directly to B's MAC")
story.extend(seq_arp.as_flowable())

section("RARP -- Reverse ARP")
definition(
    "<b>RARP (Reverse Address Resolution Protocol):</b> The reverse of ARP. "
    "A diskless workstation knows its own MAC address (from the NIC) but does not "
    "know its IP address. RARP broadcasts a request containing its MAC, and a "
    "RARP server responds with the assigned IP address. Largely replaced by DHCP."
)
info_table(
    ["Protocol", "Known", "Wants to Find", "Method", "Status"],
    [
        [
            "ARP",
            "IP address",
            "MAC address",
            "Broadcast on LAN, unicast reply",
            "Still used in all IPv4 networks",
        ],
        [
            "RARP",
            "MAC address",
            "IP address",
            "Broadcast on LAN, server replies",
            "Obsolete -- replaced by DHCP",
        ],
        [
            "DHCP",
            "Nothing (new device)",
            "IP + mask + gateway + DNS",
            "Broadcast Discover, server offers",
            "Current standard",
        ],
    ],
)
tip(
    "ARP = IP -> MAC (need to send a frame). RARP = MAC -> IP (diskless boot). "
    "ARP works within one subnet only. To reach another subnet, the frame goes "
    "to the default gateway's MAC -- the IP stays the same."
)
br()


# -----------------------------------------------------------------------------
#  2.9  HDLC
# -----------------------------------------------------------------------------
chap_box("2.9  HDLC -- High-Level Data Link Control")
section("Overview")
definition(
    "<b>HDLC (High-Level Data Link Control):</b> A bit-oriented, synchronous Data "
    "Link layer protocol standardized by ISO. HDLC uses a frame structure with a "
    "flag delimiter (01111110), supports sliding window flow control, and provides "
    "error control via CRC. It is the basis for many modern protocols including PPP, "
    "Frame Relay, and SDLC."
)
bullet(
    [
        "Bit-oriented: treats data as a stream of bits, not characters.",
        "Synchronous: requires a clock signal (no start/stop bits like asynchronous protocols).",
        "Full-duplex: supports simultaneous bidirectional communication.",
        "Supports both point-to-point and multipoint links.",
        "Three frame types: I-frame, S-frame, U-frame.",
    ]
)

section("HDLC Frame Format")
frame_format(
    "HDLC Frame Format",
    [
        ("FLAG", "8 bits\n01111110"),
        ("ADDRESS", "8 bits"),
        ("CONTROL", "8 or 16 bits"),
        ("INFORMATION", "Variable"),
        ("FCS", "16 or 32 bits"),
        ("FLAG", "8 bits\n01111110"),
    ],
)
bullet(
    [
        "<b>FLAG:</b> 01111110 (hex 0x7E) -- marks start and end of frame. Bit stuffing ensures this pattern cannot appear in data.",
        "<b>ADDRESS:</b> Identifies the secondary station in multipoint configuration. Can be extended to multiple bytes (leftmost bit = 1 if last byte).",
        "<b>CONTROL:</b> Identifies frame type and carries sequence numbers (N(S), N(R)). 8 bits (modulo 8 windows) or 16 bits (modulo 128 windows).",
        "<b>INFORMATION:</b> User data payload. Present only in I-frames. Variable length.",
        "<b>FCS:</b> Frame Check Sequence. CRC-16 (CCITT) or CRC-32 calculated over ADDRESS + CONTROL + INFORMATION fields.",
        "<b>FLAG:</b> Closing 01111110 delimiter.",
    ]
)

section("HDLC Frame Types")
info_table(
    ["Frame Type", "Control Field MSBs", "Sequence Numbers", "Purpose"],
    [
        [
            "I-frame (Information)",
            "Bit 0 = 0",
            "N(S): send sequence, N(R): receive sequence (piggybacked ACK)",
            "Carries user data. Most common frame type. Implements sliding window ARQ.",
        ],
        [
            "S-frame (Supervisory)",
            "Bits 1,0 = 1,0",
            "N(R) only (no N(S))",
            "Flow and error control only. Subtypes: RR (ACK), RNR (hold), REJ (NAK for GBN), SREJ (NAK for SR).",
        ],
        [
            "U-frame (Unnumbered)",
            "Bits 1,0 = 1,1",
            "None",
            "Link management: setup (SABM), disconnect (DISC), mode setting, error reporting (FRMR).",
        ],
    ],
)
subsection("S-frame Subtypes")
info_table(
    ["Subtype", "Code", "Meaning"],
    [
        [
            "RR  (Receive Ready)",
            "00",
            "ACK -- ready to receive next frame. N(R) = next expected frame.",
        ],
        [
            "RNR (Receive Not Ready)",
            "10",
            "Pause -- receiver busy (buffer full). Stop sending until RR received.",
        ],
        [
            "REJ (Reject)",
            "01",
            "NAK for Go-Back-N. Retransmit frame N(R) and all subsequent.",
        ],
        [
            "SREJ (Selective Reject)",
            "11",
            "NAK for Selective Repeat. Retransmit ONLY frame N(R).",
        ],
    ],
)

section("HDLC Configurations")
info_table(
    ["Configuration", "Abbreviation", "Description"],
    [
        [
            "Normal Response Mode",
            "NRM",
            "Primary station controls the link. Secondary transmits only when polled by primary. "
            "Used on multipoint (multidrop) links.",
        ],
        [
            "Asynchronous Balanced Mode",
            "ABM",
            "Both stations are peers (combined stations). Either can initiate transmission. "
            "Used on point-to-point links. Most common mode (PPP uses this).",
        ],
        [
            "Asynchronous Response Mode",
            "ARM",
            "Secondary can initiate without waiting for poll. Rarely used.",
        ],
    ],
)
tip(
    "HDLC control field: I-frame starts with 0, S-frame with 10, U-frame with 11. "
    "N(S) = sequence number of frame being sent. N(R) = sequence number of next "
    "frame expected (acknowledges all frames up to N(R)-1). Exam loves this."
)
br()


# -----------------------------------------------------------------------------
#  2.10  LAN PROTOCOL STACK -- LLC AND MAC
# -----------------------------------------------------------------------------
chap_box("2.10  LAN Protocol Stack -- LLC, MAC, and IEEE 802.2 LLC Frame Format")
section("IEEE 802 LAN Architecture")
definition(
    "<b>IEEE 802 Standard:</b> A family of standards for local area networks defined "
    "by the IEEE (Institute of Electrical and Electronics Engineers). The 802 standard "
    "divides the OSI Data Link layer into two sublayers to separate common LLC functions "
    "from medium-specific MAC functions."
)

# LAN stack layered diagram
lan_stack = pd.LayeredStack(
    width=CW * 0.6, height=280, caption="Fig 7: IEEE 802 LAN Protocol Stack"
)
lan_stack.layer(
    "Network Layer (IP)", sublabel="OSI Layer 3 -- logical addressing and routing"
)
lan_stack.divider()
lan_stack.layer(
    "LLC Sublayer (IEEE 802.2)",
    sublabel="Logical Link Control -- framing, flow control, error control",
)
lan_stack.layer(
    "MAC Sublayer (IEEE 802.3 / 802.11 etc.)",
    sublabel="Medium Access Control -- CSMA/CD, token, addressing",
)
lan_stack.divider()
lan_stack.layer(
    "Physical Layer", sublabel="Bit encoding, signalling, cables, connectors"
)
story.extend(lan_stack.as_flowable())

section("LLC -- Logical Link Control Sublayer (IEEE 802.2)")
definition(
    "<b>LLC (Logical Link Control):</b> The upper sublayer of the Data Link layer, "
    "defined by IEEE 802.2. It provides a uniform interface to the Network layer "
    "regardless of the underlying physical medium (Ethernet, Token Ring, Wi-Fi). "
    "LLC handles multiplexing (identifying which network-layer protocol the frame "
    "carries), flow control, and error control for connection-oriented services."
)
subsection("LLC Services")
bullet(
    [
        "<b>LLC Type 1 (Unacknowledged Connectionless):</b> No connection setup, no ACK. "
        "Simple datagram service. Used in modern Ethernet where upper layers (TCP) handle "
        "reliability. Equivalent to OSI unacknowledged connectionless service.",
        "<b>LLC Type 2 (Connection-Oriented):</b> Connection established before data "
        "transfer, frames acknowledged, retransmitted if lost. Supports sliding window. "
        "Used in older IBM networks (Token Ring). Rarely used today.",
        "<b>LLC Type 3 (Acknowledged Connectionless):</b> No connection setup but each "
        "frame is individually acknowledged. Compromise between Type 1 and Type 2.",
    ]
)

section("IEEE 802.2 LLC Frame Format")
frame_format(
    "IEEE 802.2 LLC Frame Format (within the Ethernet frame payload)",
    [
        ("DSAP", "8 bits"),
        ("SSAP", "8 bits"),
        ("CONTROL", "8 or 16 bits"),
        ("DATA (upper-layer PDU)", "Variable"),
    ],
)
bullet(
    [
        "<b>DSAP (Destination Service Access Point):</b> 7-bit identifier indicating the upper-layer protocol receiving the frame. Bit 0 (I/G bit) indicates individual (0) or group (1) address. Examples: 0x06 = IP, 0x42 = STP (Spanning Tree), 0xFF = broadcast.",
        "<b>SSAP (Source Service Access Point):</b> 7-bit identifier indicating the upper-layer protocol that sent the frame. Bit 0 (C/R bit) indicates command (0) or response (1) frame.",
        "<b>CONTROL FIELD:</b> 8 bits for Type 1 (unnumbered frames) or 16 bits for Type 2 (numbered frames). Same structure as HDLC control field.",
        "<b>DATA:</b> Upper-layer protocol data unit encapsulated in this LLC frame.",
        "<b>Example LLC Frame (IP datagram):</b> DSAP = 0x06 (IP), SSAP = 0x06 (IP), CONTROL = 0x03 (UI -- Unnumbered Information, Type 1 service), DATA = IP Packet.",
    ]
)

section("MAC -- Media Access Control Sublayer")
definition(
    "<b>MAC (Media Access Control) Sublayer:</b> The lower sublayer of the Data Link "
    "layer. It handles medium-specific functions: determining which device may "
    "transmit at a given time (access control), constructing and processing MAC frames, "
    "and implementing MAC addressing (48-bit hardware addresses)."
)
bullet(
    [
        "MAC protocols differ depending on the medium: CSMA/CD for Ethernet, "
        "CSMA/CA for Wi-Fi, token passing for Token Ring.",
        "The MAC sublayer adds the preamble, source MAC, destination MAC, and FCS "
        "to form a complete Ethernet frame.",
        "MAC is medium-specific; LLC is medium-independent.",
    ]
)

section("IEEE 802.3 Ethernet MAC Frame Format")
frame_format(
    "IEEE 802.3 Ethernet Frame Format",
    [
        ("PRE", "7 bytes"),
        ("SFD", "1 byte"),
        ("DST MAC", "6 bytes"),
        ("SRC MAC", "6 bytes"),
        ("LENGTH/TYPE", "2 bytes"),
        ("DATA", "46-1500 bytes"),
        ("FCS", "4 bytes"),
    ],
)
bullet(
    [
        "<b>PREAMBLE (7 bytes):</b> 10101010 repeated 7 times. Allows receiver to synchronise its clock with the sender.",
        "<b>SFD -- Start Frame Delimiter (1 byte):</b> 10101011. Signals that the next byte is the destination MAC address.",
        "<b>DESTINATION MAC (6 bytes):</b> 48-bit MAC address of intended receiver. FF:FF:FF:FF:FF:FF = broadcast.",
        "<b>SOURCE MAC (6 bytes):</b> 48-bit MAC address of the sender.",
        "<b>LENGTH/TYPE (2 bytes):</b> If value <= 1500: Length field (802.3). If value >= 1536 (0x0600): Type field (Ethernet II). Common EtherType values: 0x0800=IPv4, 0x0806=ARP, 0x86DD=IPv6.",
        "<b>DATA (46 to 1500 bytes):</b> Payload from upper layer. Minimum 46 bytes -- padded with zeros if shorter (to ensure minimum frame size of 64 bytes for CSMA/CD collision detection).",
        "<b>FCS (4 bytes):</b> CRC-32 over DST+SRC+LEN/TYPE+DATA for error detection.",
        "<b>Frame Sizes:</b> Minimum Ethernet frame is 64 bytes (excluding preamble/SFD); maximum is 1518 bytes.",
    ]
)

info_table(
    ["IEEE Standard", "Technology", "Speed", "Medium", "Key Feature"],
    [
        [
            "802.2",
            "LLC",
            "-",
            "All media",
            "Common LLC for all 802 LANs -- medium independence",
        ],
        [
            "802.3",
            "Ethernet",
            "10M-10G",
            "UTP, Fiber, Coax",
            "CSMA/CD, most dominant wired LAN standard",
        ],
        [
            "802.4",
            "Token Bus",
            "1-20 Mbps",
            "Coax bus",
            "Token passing on bus -- used in factory automation (obsolete)",
        ],
        [
            "802.5",
            "Token Ring",
            "4-16 Mbps",
            "STP cable ring",
            "Token passing on ring -- IBM network (obsolete)",
        ],
        [
            "802.11",
            "Wi-Fi (WLAN)",
            "11M-9.6G",
            "Radio (2.4/5/6 GHz)",
            "CSMA/CA -- most dominant wireless LAN standard",
        ],
        [
            "802.16",
            "WiMAX",
            "Up to 1G",
            "Radio (licensed)",
            "Broadband wireless MAN (metropolitan area)",
        ],
    ],
)
tip(
    "LLC provides the same interface to the network layer regardless of whether "
    "the LAN is Ethernet, Wi-Fi, or Token Ring. MAC is what changes between them. "
    "IEEE 802.2 LLC frame contains DSAP, SSAP, and Control fields."
)
br()


# =============================================================================
#  2.11  QUICK REVISION SUMMARY
# =============================================================================
part_box("UNIT II -- QUICK REVISION SUMMARY")
chap_box("Key Concepts at a Glance")

info_table(
    ["Topic", "Key Point to Remember"],
    [
        [
            "Circuit Switching",
            "Dedicated end-to-end path. 3 phases: setup, transfer, teardown. "
            "Wastes bandwidth when idle. PSTN telephone network.",
        ],
        [
            "Packet Switching (Datagram)",
            "No dedicated path. Each packet routed independently. May arrive out "
            "of order. Example: IP, UDP.",
        ],
        [
            "Packet Switching (Virtual Circuit)",
            "Logical path established first. Packets follow same route in order. "
            "Resources NOT fully reserved. Example: ATM, X.25.",
        ],
        [
            "Message Switching",
            "Entire message stored at each hop. No blocking. Very high delay. "
            "Precursor to packet switching. Largely obsolete.",
        ],
        [
            "Data Link Layer Services",
            "3 types: Unacknowledged connectionless (Ethernet), "
            "Acknowledged connectionless (Wi-Fi), Connection-oriented (HDLC X.25).",
        ],
        [
            "Framing Methods",
            "Character count, byte stuffing (PPP: 0x7E/0x7D), bit stuffing (HDLC: "
            "insert 0 after 5 ones), physical layer violations.",
        ],
        [
            "Bit Stuffing Rule",
            "Sender: insert 0 after five consecutive 1s. "
            "Receiver: delete 0 that follows five consecutive 1s. Flag = 01111110.",
        ],
        [
            "CRC",
            "Append r zeros (r = degree of generator). XOR divide. "
            "Remainder = FCS appended to frame. Receiver divides: remainder 0 = no error.",
        ],
        [
            "Hamming Code",
            "Parity at positions 2<super>k</super> (1,2,4,8,...). Formula: 2<super>r</super> >= m+r+1. "
            "Error position = sum of failing parity bit positions.",
        ],
        [
            "Stop-and-Wait Efficiency",
            "eta = 1/(1+2a) where a = T<sub>propagation</sub> / T<sub>transmission</sub>. "
            "Very inefficient for high-delay links.",
        ],
        [
            "Go-Back-N Window",
            "Sender window W<sub>s</sub> = 2<super>n</super> - 1. Receiver window W<sub>r</sub> = 1. "
            "Retransmits error frame + all subsequent frames.",
        ],
        [
            "Selective Repeat Window",
            "Sender window W<sub>s</sub> = 2<super>n-1</super>. Receiver window W<sub>r</sub> = 2<super>n-1</super>. "
            "Retransmits ONLY the error frame. Receiver buffers out-of-order.",
        ],
        [
            "Pipelining Efficiency",
            "If W >= 1+2a: efficiency = 1. Else: efficiency = W/(1+2a). "
            "Send multiple frames without waiting for ACK.",
        ],
        [
            "Piggybacking",
            "ACK embedded in outgoing data frame in opposite direction. "
            "Saves bandwidth. Used in TCP, HDLC.",
        ],
        [
            "MAC Address",
            "48-bit hardware address. OUI (3 bytes, manufacturer) + device ID (3 bytes). "
            "Broadcast: FF:FF:FF:FF:FF:FF. Written in hex pairs.",
        ],
        [
            "ARP",
            "IP address -> MAC address. Broadcast request on LAN. "
            "Unicast reply. ARP cache stores mappings temporarily.",
        ],
        [
            "RARP",
            "MAC address -> IP address. Used by diskless workstations. "
            "Replaced by DHCP. Now obsolete.",
        ],
        [
            "HDLC Frame",
            "FLAG(8)|ADDRESS(8)|CONTROL(8/16)|INFO(var)|FCS(16/32)|FLAG(8). "
            "I-frame(data), S-frame(flow/error ctrl), U-frame(link mgmt).",
        ],
        [
            "HDLC S-Frame Subtypes",
            "RR=ACK, RNR=pause/busy, REJ=NAK(Go-Back-N), SREJ=NAK(Selective Repeat).",
        ],
        [
            "IEEE 802.2 LLC",
            "DSAP + SSAP + Control + Data. Medium-independent. "
            "Type1=connectionless, Type2=connection-oriented, Type3=ack-connectionless.",
        ],
        [
            "IEEE 802.3 Ethernet Frame",
            "Preamble(7B)+SFD(1B)+DST MAC(6B)+SRC MAC(6B)+Length/Type(2B)"
            "+Data(46-1500B)+FCS(4B). Min frame=64B, Max=1518B.",
        ],
        [
            "LLC vs MAC",
            "LLC is medium-independent (same for Ethernet, Wi-Fi, Token Ring). "
            "MAC is medium-specific (CSMA/CD for Ethernet, CSMA/CA for Wi-Fi).",
        ],
    ],
)

highlight(
    "<b>UNIT II EXAM BLUEPRINT:</b>  "
    "2-mark: Define circuit/packet/message switching. Name 4 DLL design issues. "
    "State HDLC frame fields. Give window size formula.  "
    "5-mark: Compare GBN vs SR ARQ. Explain bit stuffing with example. "
    "Explain ARP operation. Draw HDLC frame format.  "
    "10-mark: Explain all switching techniques with diagrams. "
    "Explain error detection (CRC with worked example). "
    "Explain sliding window ARQ protocols (GBN + SR) with diagrams and efficiency.",
    YELLOW_CARD,
    YELLOW,
)

# =============================================================================
#  BUILD PDF
# =============================================================================
doc = SimpleDocTemplate(
    "CN_Unit2_Notes.pdf",
    pagesize=A4,
    leftMargin=PM,
    rightMargin=PM,
    topMargin=PM,
    bottomMargin=PM,
    title="Computer Networks IT-411 Unit II Notes",
    author="UIT-RGPV (Autonomous) Bhopal",
)
doc.build(story, onFirstPage=page_decor, onLaterPages=page_decor)
print("Generated: CN_Unit2_Notes.pdf")
