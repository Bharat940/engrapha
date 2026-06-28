"""
Computer Networks (IT-411) -- Unit III Notes
UIT-RGPV (Autonomous) Bhopal | Semester IV
Complete exam notes with vector diagrams.
Run: python cn_unit3_notes.py
Output: CN_Unit3_Notes.pdf
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

import engrapha_diagrams as ed

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
    th = S(
        "F_HDR",
        fontSize=8.5,
        textColor=colors.HexColor("#79c0ff"),
        fontName="Helvetica-Bold",
        alignment=TA_CENTER,
        leading=11,
    )
    td = S(
        "F_SZ",
        fontSize=7.5,
        textColor=colors.HexColor("#9da7b3"),
        fontName="Helvetica-Oblique",
        alignment=TA_CENTER,
        leading=10,
    )

    data = [[Paragraph(h, th) for h in headers], [Paragraph(s, td) for s in sizes]]

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
        add(
            Paragraph(
                f"<i>{caption}</i>",
                S(
                    "F_CAP",
                    fontSize=8.5,
                    textColor=colors.HexColor("#9da7b3"),
                    fontName="Helvetica-Oblique",
                    alignment=TA_CENTER,
                    leading=12,
                ),
            )
        )
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
add(Paragraph("Unit III -- Complete Exam Notes", COVER_H2))
add(Paragraph("Subject Code: IT-411  |  UIT-RGPV (Autonomous) Bhopal", COVER_SUB))
add(Paragraph("Semester IV  |  Based on University Syllabus 2024-25", COVER_SUB))
sp(10)
rule(CYAN, 1.5)
sp(8)

info_table(
    ["Topic", "Coverage"],
    [
        [
            "3.1 MAC Sub-layer Overview",
            "Role, channel allocation problem, taxonomy of protocols",
        ],
        [
            "3.2 Static Channel Allocation",
            "TDMA, FDMA -- fixed division, advantages and limitations",
        ],
        ["3.3 Dynamic Channel Allocation", "Assumptions, need for dynamic allocation"],
        ["3.4 Pure ALOHA", "Operation, throughput analysis, efficiency 18.4%"],
        ["3.5 Slotted ALOHA", "Operation, throughput analysis, efficiency 36.8%"],
        ["3.6 CSMA Protocols", "1-persistent, non-persistent, p-persistent CSMA"],
        ["3.7 CSMA/CD", "Ethernet collision detection, binary exponential backoff"],
        ["3.8 CSMA/CA", "Wireless collision avoidance, RTS/CTS, Wi-Fi"],
        [
            "3.9 IEEE 802.3 and Ethernet",
            "Frame format, cabling variants, CSMA/CD details",
        ],
        ["3.10 IEEE 802.4 -- Token Bus", "Operation, frame format, advantages"],
        ["3.11 IEEE 802.5 -- Token Ring", "Operation, frame format, token passing"],
        ["3.12 FDDI", "Dual ring, timed token protocol, fault tolerance"],
        [
            "3.13 Quick Revision Summary",
            "Key formulas, comparisons, and exam flashcards",
        ],
    ],
)
br()


# =============================================================================
#  UNIT III DIVIDER
# =============================================================================
part_box("UNIT III -- MAC LAYER PROTOCOLS")


# -----------------------------------------------------------------------------
#  3.1  MAC SUB-LAYER OVERVIEW
# -----------------------------------------------------------------------------
chap_box("3.1  MAC Sub-layer -- Overview and Channel Allocation Problem")
section("Role of the MAC Sub-layer")
definition(
    "<b>MAC (Medium Access Control) Sub-layer:</b> The lower half of the Data Link "
    "layer (IEEE 802 architecture). Its primary role is to determine <b>which station "
    "gets to use the shared communication channel at any given time</b>. Without MAC "
    "protocols, multiple stations transmitting simultaneously would cause signal "
    "collisions, rendering all transmissions useless."
)
body(
    "The MAC sub-layer sits between the LLC (Logical Link Control) sub-layer above "
    "and the Physical layer below. It handles frame delimiting, addressing (MAC "
    "addresses), and -- most importantly -- medium access control."
)

section("The Channel Allocation Problem")
definition(
    "<b>Channel Allocation Problem:</b> When multiple independent stations share a "
    "single broadcast channel (like an Ethernet bus or a Wi-Fi radio channel), a "
    "mechanism is needed to decide which station transmits when. If two stations "
    "transmit at the same time, their signals interfere -- a <b>collision</b> occurs "
    "and both frames are destroyed."
)
bullet(
    [
        "A shared channel is called a <b>multi-access channel</b> or <b>broadcast channel</b>.",
        "The problem is solved by channel allocation protocols, collectively called MAC protocols.",
        "Design goals: maximize throughput, minimize delay, be fair to all stations, be simple.",
    ]
)

section("Taxonomy of MAC Protocols")
info_table(
    ["Category", "Sub-category", "Examples"],
    [
        [
            "Static Allocation",
            "TDMA (Time Division)",
            "GSM voice calls, satellite links",
        ],
        [
            "Static Allocation",
            "FDMA (Frequency Division)",
            "FM radio, cable TV, 1G cellular",
        ],
        [
            "Dynamic -- Random Access",
            "ALOHA (Pure)",
            "Early satellite networks, LoRa IoT",
        ],
        [
            "Dynamic -- Random Access",
            "Slotted ALOHA",
            "Satellite return channels, LTE RACH",
        ],
        ["Dynamic -- Random Access", "CSMA (1-persistent)", "Early Ethernet"],
        ["Dynamic -- Random Access", "CSMA/CD", "IEEE 802.3 Ethernet (wired)"],
        ["Dynamic -- Random Access", "CSMA/CA", "IEEE 802.11 Wi-Fi (wireless)"],
        [
            "Controlled Access",
            "Token Passing",
            "IEEE 802.4 Token Bus, IEEE 802.5 Token Ring",
        ],
        ["Controlled Access", "Polling", "Bluetooth piconet (master polls slaves)"],
        ["Limited Contention", "Adaptive Tree Walk", "Research protocols"],
    ],
)
tip(
    "MAC protocols fall into 3 broad families: Static (fixed assignment), "
    "Dynamic Random Access (contention-based), and Controlled Access (collision-free). "
    "Know at least 2 examples from each family."
)
br()


# -----------------------------------------------------------------------------
#  3.2  STATIC CHANNEL ALLOCATION
# -----------------------------------------------------------------------------
chap_box("3.2  Static Channel Allocation -- TDMA and FDMA")
section("Overview")
body(
    "Static allocation divides the channel's capacity into fixed slots and assigns "
    "each station a permanent slot. Stations only transmit in their assigned slot; "
    "no contention ever occurs. However, if a station has nothing to send, its "
    "slot goes to waste -- making static allocation inefficient for bursty data traffic."
)

section("TDMA -- Time Division Multiple Access")
definition(
    "<b>TDMA:</b> The channel's time is divided into fixed-length frames. Each frame "
    "is divided into N time slots (one per station). Station i always transmits "
    "in slot i of every frame. Each station gets 1/N of the total channel capacity."
)
bullet(
    [
        "Bandwidth per station = Total bandwidth / N (always, whether or not station has data).",
        "No collisions ever -- completely deterministic.",
        "Wasted slots when a station is idle -- poor efficiency for bursty data.",
        "Used in: GSM (2G cellular voice), satellite systems, TDM multiplexing on leased lines.",
        "Guard time between slots prevents overlap due to timing imperfections.",
    ]
)
code_block("""
 TDMA FRAME STRUCTURE (N=4 stations):
 =====================================================================
 | Slot 1  | Slot 2  | Slot 3  | Slot 4  | Slot 1  | Slot 2  | ...
 | Sta. A  | Sta. B  | Sta. C  | Sta. D  | Sta. A  | Sta. B  | ...
 |---------|---------|---------|---------|---------|---------|
 <------------- One TDMA Frame ----------->

 If Station B has no data to send:
 | Slot 1  | [IDLE]  | Slot 3  | Slot 4  | Slot 1  | [IDLE]  | ...
   Slot 2 is wasted -- bandwidth lost forever.
""")

section("FDMA -- Frequency Division Multiple Access")
definition(
    "<b>FDMA:</b> The total available frequency spectrum is permanently divided into "
    "N sub-bands. Each station is assigned one sub-band and can transmit at any "
    "time within its sub-band. Stations transmit simultaneously but on different "
    "frequencies -- no interference."
)
bullet(
    [
        "Each station gets a fixed sub-band of width B/N (B = total bandwidth).",
        "No collisions -- stations transmit on different frequencies.",
        "Guard bands between sub-bands prevent inter-channel interference.",
        "Wasted spectrum when a station is idle -- rigid allocation.",
        "Used in: FM radio, 1G AMPS cellular, cable TV, first-generation satellite.",
    ]
)

section("Static Allocation -- Limitations")
info_table(
    ["Feature", "Static Allocation (TDMA / FDMA)", "Dynamic Allocation"],
    [
        [
            "Collisions",
            "None -- deterministic assignment",
            "Possible -- managed by protocol",
        ],
        [
            "Efficiency",
            "Low for bursty traffic -- slots wasted",
            "High -- channel only used when needed",
        ],
        [
            "Delay",
            "Bounded -- worst case = 1 frame wait",
            "Variable -- depends on load",
        ],
        ["Overhead", "No protocol overhead at runtime", "Protocol signalling overhead"],
        [
            "Scalability",
            "Fixed N -- must reassign if stations join/leave",
            "Adapts automatically",
        ],
        [
            "Best for",
            "Continuous, constant-rate traffic (voice, video)",
            "Bursty data traffic (LAN, Internet)",
        ],
    ],
)
tip(
    "TDMA wastes time slots; FDMA wastes frequency sub-bands. Both are inefficient "
    "for data networks where traffic is bursty. That is why Ethernet uses CSMA/CD "
    "instead of TDMA or FDMA."
)
br()


# -----------------------------------------------------------------------------
#  3.3  DYNAMIC CHANNEL ALLOCATION -- ASSUMPTIONS
# -----------------------------------------------------------------------------
chap_box("3.3  Dynamic Channel Allocation -- Assumptions and Models")
section("Five Key Assumptions")
body(
    "All dynamic MAC protocols are analyzed under a set of standard assumptions "
    "that define the model of the shared channel:"
)
info_table(
    ["Assumption", "Description"],
    [
        [
            "1. Station Model",
            "There are N independent stations. Each station generates frames at a Poisson rate of lambda frames/sec. "
            "Once a frame is generated, the station is blocked until it is successfully transmitted.",
        ],
        [
            "2. Single Channel",
            "A single shared broadcast channel is available for all transmissions. "
            "All stations can transmit on -- and receive from -- this single channel.",
        ],
        [
            "3. Collision Assumption",
            "If two or more frames overlap in time, they collide. All colliding frames "
            "are destroyed (garbled). The channel can carry at most ONE frame at a time.",
        ],
        [
            "4. Continuous or Slotted Time",
            "Continuous time: frames can begin at any instant. "
            "Slotted time: time is divided into discrete slots; frames can only begin at a slot boundary.",
        ],
        [
            "5. Carrier Sense or No Carrier Sense",
            "Carrier sense: stations can detect if the channel is busy before transmitting. "
            "No carrier sense (ALOHA): stations transmit without checking -- they learn about collisions only after they occur.",
        ],
    ],
)
body(
    "The <b>offered load G</b> is the total number of frame transmission attempts "
    "(including retransmissions) per frame-time. The <b>throughput S</b> is the "
    "fraction of slots carrying successfully delivered frames. S = G * P(success)."
)
sp(6)
br()


# -----------------------------------------------------------------------------
#  3.4  PURE ALOHA
# -----------------------------------------------------------------------------
chap_box("3.4  Pure ALOHA")
section("Overview")
definition(
    "<b>Pure ALOHA:</b> The simplest random access protocol, developed at the University "
    "of Hawaii in 1970 for satellite communication. Stations transmit frames whenever "
    "they have data ready -- completely at random, with no coordination. After "
    "transmitting, a station listens for an ACK. If no ACK arrives within a timeout "
    "(collision occurred), it waits a random time and retransmits."
)

section("Operation")
bullet(
    [
        "A station generates a frame and <b>immediately transmits</b> it.",
        "The station waits for an ACK from the receiver.",
        "If ACK arrives within timeout: success. Move to next frame.",
        "If no ACK (collision detected): wait a <b>random backoff time</b> and retransmit.",
        "Backoff time is chosen uniformly at random from {0, 1, ..., 2<super>k</super> - 1} frame times after k collisions.",
        "No synchronization required -- simplest possible protocol.",
    ]
)

# Pure ALOHA timeline sequence diagram
seq_aloha = ed.SequenceDiagram(
    width=CW,
    height=240,
    caption="Fig 1: Pure ALOHA -- Station A collides with Station B, both retransmit after random backoff",
)
seq_aloha.actor("a", "Station A")
seq_aloha.actor("ch", "Channel")
seq_aloha.actor("b", "Station B")
seq_aloha.message("a", "ch", "Frame A1 (transmit)", arrow="solid")
seq_aloha.message("b", "ch", "Frame B1 (transmit -- COLLISION)", arrow="solid")
seq_aloha.message("ch", "a", "Collision -- no ACK received", arrow="dashed")
seq_aloha.message("ch", "b", "Collision -- no ACK received", arrow="dashed")
seq_aloha.divider("Both wait random backoff -- B waits less")
seq_aloha.message("b", "ch", "Frame B1 (retransmit -- success)", arrow="solid")
seq_aloha.message("a", "ch", "Frame A1 (retransmit -- success)", arrow="solid")
story.extend(seq_aloha.as_flowable())

section("Throughput Analysis")
body(
    "The <b>vulnerable period</b> for a frame of duration T is <b>2T</b>. A collision "
    "occurs if any other station starts transmitting in the interval [t-T, t+T]. "
    "With offered load G (frames per frame-time):"
)
code_block("""
 PURE ALOHA THROUGHPUT FORMULA:
 =====================================================================
 S = G * e^(-2G)

 Where:
   G = offered load (total attempts per frame time, including retransmits)
   S = throughput (successfully delivered frames per frame time)
   e = Euler's number (2.718...)

 Maximum throughput:
   dS/dG = 0  =>  G = 0.5
   S_max = 0.5 * e^(-1) = 0.5 / 2.718 = 0.184 = 18.4%

 Interpretation:
   Even under optimal load (G=0.5), only 18.4% of channel capacity
   is used for successful transmissions.
   81.6% of the channel is wasted on collisions and idle time.

 EXAMPLE CALCULATIONS:
   G=0.1: S = 0.1 * e^(-0.2) = 0.1 * 0.819 = 0.082  (8.2%)
   G=0.5: S = 0.5 * e^(-1.0) = 0.5 * 0.368 = 0.184  (18.4%) <- MAX
   G=1.0: S = 1.0 * e^(-2.0) = 1.0 * 0.135 = 0.135  (13.5%)
   G=2.0: S = 2.0 * e^(-4.0) = 2.0 * 0.018 = 0.037  (3.7%)
   As G increases beyond 0.5, throughput DECREASES -- channel collapses.
""")
tip(
    "Pure ALOHA: S = G * e<super>-2G</super>. Maximum = 18.4% at G = 0.5. "
    "Vulnerable period = 2T. No synchronization needed. "
    "These numbers are guaranteed exam questions."
)
br()


# -----------------------------------------------------------------------------
#  3.5  SLOTTED ALOHA
# -----------------------------------------------------------------------------
chap_box("3.5  Slotted ALOHA")
section("Overview")
definition(
    "<b>Slotted ALOHA:</b> An improvement over Pure ALOHA proposed by Roberts (1972). "
    "Time is divided into discrete slots, each exactly equal to one frame transmission "
    "time T. Stations are synchronized and may only begin transmission at the start "
    "of a slot. This halves the vulnerable period compared to Pure ALOHA."
)

section("Operation")
bullet(
    [
        "Time is divided into fixed slots of length T (one frame-time each).",
        "All stations are synchronized to the same global clock.",
        "A station with a frame to send <b>waits for the next slot boundary</b> before transmitting.",
        "If two stations transmit in the same slot: collision -- both retransmit in a future slot (random backoff).",
        "If only one station transmits in a slot: success.",
        "Vulnerable period is T (only stations that begin in the SAME slot can collide).",
    ]
)
code_block("""
 PURE ALOHA vs SLOTTED ALOHA -- VULNERABLE PERIOD:
 =====================================================================

 PURE ALOHA (unslotted):
 Frame A starts at time t. It occupies [t, t+T].
 A collision occurs if any other frame starts in [t-T, t+T] -- period = 2T.

   |--- T ---|--- T ---|
   [----A----]
   [--B--]        <- B starts T before A -> collision
            [--C--]  <- C starts just after A starts -> collision

 SLOTTED ALOHA:
 Frames can only start at slot boundaries: 0, T, 2T, 3T, ...
 A collision occurs only if another frame starts at the SAME slot boundary.
 Vulnerable period = T (only ONE slot, not two).

   | Slot 1  | Slot 2  | Slot 3  |
   [----A----][----B----][----C----]
   A and B in same slot -> collision. C in slot 2 -> safe.
""")

section("Throughput Analysis")
code_block("""
 SLOTTED ALOHA THROUGHPUT FORMULA:
 =====================================================================
 S = G * e^(-G)

 Where:
   G = offered load (attempts per slot)
   S = throughput (successful transmissions per slot)

 Maximum throughput:
   dS/dG = 0  =>  G = 1.0
   S_max = 1.0 * e^(-1) = 1/e = 0.368 = 36.8%

 This is EXACTLY DOUBLE Pure ALOHA's maximum of 18.4%.

 EXAMPLE CALCULATIONS:
   G=0.5: S = 0.5 * e^(-0.5) = 0.5 * 0.607 = 0.303  (30.3%)
   G=1.0: S = 1.0 * e^(-1.0) = 1.0 * 0.368 = 0.368  (36.8%) <- MAX
   G=2.0: S = 2.0 * e^(-2.0) = 2.0 * 0.135 = 0.271  (27.1%)
   G=3.0: S = 3.0 * e^(-3.0) = 3.0 * 0.050 = 0.149  (14.9%)

 KEY INSIGHT:
   Slotted ALOHA doubles throughput by halving the collision window.
   Requires global time synchronization (extra overhead).
""")

section("Pure ALOHA vs Slotted ALOHA -- Comparison")
info_table(
    ["Feature", "Pure ALOHA", "Slotted ALOHA"],
    [
        [
            "Time model",
            "Continuous -- transmit at any instant",
            "Slotted -- transmit only at slot boundaries",
        ],
        ["Synchronization", "None required", "All stations must be time-synchronized"],
        ["Vulnerable period", "2T (two frame times)", "T (one frame time -- one slot)"],
        [
            "Throughput formula",
            "S = G * e<super>-2G</super>",
            "S = G * e<super>-G</super>",
        ],
        ["Max throughput", "18.4%  (at G = 0.5)", "36.8%  (at G = 1.0)"],
        [
            "Implementation",
            "Simpler -- no clock sync needed",
            "More complex -- requires global clock",
        ],
        [
            "Collision window",
            "Frame can collide with frames in [t-T, t+T]",
            "Frame can only collide with frames in same slot",
        ],
        [
            "Used in",
            "LoRa IoT, early satellite",
            "LTE Random Access Channel (RACH), satellite",
        ],
    ],
)
highlight(
    "<b>Key Formula Summary:</b>  "
    "Pure ALOHA: S = G * e<super>-2G</super>,  max = 18.4% at G=0.5.  "
    "Slotted ALOHA: S = G * e<super>-G</super>,  max = 36.8% at G=1.0.  "
    "General form: S = G * e<super>-aG</super> where a=2 (Pure) or a=1 (Slotted).  "
    "Slotted ALOHA throughput = exactly 2x Pure ALOHA.",
    CARD_DARK,
    CYAN,
)
tip(
    "The formula S = G * e<super>-2G</super> for Pure ALOHA comes from the Poisson probability that "
    "NO other transmission starts during the 2T vulnerable window: P = e<super>-2G</super>. "
    "Slotted halves the window to T, so P = e<super>-G</super>."
)
br()


# -----------------------------------------------------------------------------
#  3.6  CSMA PROTOCOLS
# -----------------------------------------------------------------------------
chap_box("3.6  CSMA -- Carrier Sense Multiple Access Protocols")
section("Overview")
definition(
    "<b>CSMA (Carrier Sense Multiple Access):</b> A family of MAC protocols in which "
    "stations <b>listen to the channel before transmitting</b> (carrier sense). If the "
    "channel is busy, the station waits before attempting transmission. This dramatically "
    "reduces the collision rate compared to ALOHA, because a station would never "
    "transmit on top of an ongoing frame (in the ideal case)."
)
body(
    "CSMA does NOT eliminate collisions entirely. Two stations may simultaneously "
    "sense the channel as idle (because the signal from one has not yet reached the "
    "other -- propagation delay) and both start transmitting, causing a collision. "
    "This time window is called the <b>vulnerable period = propagation delay (tau)</b>."
)

section("3.6.1  1-Persistent CSMA")
definition(
    "<b>1-Persistent CSMA:</b> A station that wants to transmit continuously monitors "
    "the channel. As soon as the channel becomes idle, the station transmits <b>immediately "
    "with probability 1</b>. If a collision occurs, it waits a random backoff time and "
    "resumes monitoring."
)
bullet(
    [
        "If channel is IDLE: transmit immediately (probability = 1).",
        "If channel is BUSY: wait and keep sensing; transmit as soon as idle.",
        "After collision: wait random time, then sense again.",
        "Greedy -- transmits immediately when idle.",
        "HIGH collision probability when multiple stations are waiting for a busy channel "
        "(all will transmit simultaneously when the channel clears).",
        "Used in: Classic Ethernet (with CSMA/CD added for detection).",
    ]
)

section("3.6.2  Non-Persistent CSMA")
definition(
    "<b>Non-Persistent CSMA:</b> If the channel is busy, the station does NOT "
    "continuously monitor it. Instead, it waits a <b>random amount of time</b> and "
    "then senses the channel again. This reduces the chance of multiple stations "
    "rushing in simultaneously when a busy channel becomes free."
)
bullet(
    [
        "If channel is IDLE: transmit immediately.",
        "If channel is BUSY: wait a RANDOM time, then sense again (do NOT keep watching).",
        "After collision: wait random time, then sense again.",
        "Less greedy -- reduced collision probability.",
        "Higher channel efficiency under heavy load than 1-persistent.",
        "Slightly higher delay -- even if channel becomes idle, station may not notice immediately.",
    ]
)

section("3.6.3  p-Persistent CSMA (Slotted Channels)")
definition(
    "<b>p-Persistent CSMA:</b> Used with slotted channels. When the channel is idle, "
    "a station transmits with probability <b>p</b> in the current slot, or defers to "
    "the next slot with probability <b>1-p</b>. This balances the aggressiveness of "
    "1-persistent with the conservatism of non-persistent."
)
bullet(
    [
        "If channel is IDLE: transmit with probability p; with probability (1-p), defer one slot.",
        "If channel is BUSY: wait until idle, then apply p-persistent rule.",
        "After collision: wait random time, then apply p-persistent rule.",
        "p=1: degenerates to 1-persistent CSMA.",
        "Smaller p = less aggressive = fewer collisions but more delay.",
        "The optimal p depends on traffic load N: p = 1/N (if N stations active).",
    ]
)

section("CSMA Variants Comparison")
info_table(
    ["Feature", "1-Persistent", "Non-Persistent", "p-Persistent"],
    [
        [
            "Channel IDLE action",
            "Transmit immediately (p=1)",
            "Transmit immediately",
            "Transmit with prob p; defer with 1-p",
        ],
        [
            "Channel BUSY action",
            "Keep sensing -- pounce when free",
            "Wait RANDOM time, then sense again",
            "Wait until idle, apply p rule",
        ],
        [
            "Collision rate",
            "High -- all waiting stations jump in",
            "Low -- random delays spread traffic",
            "Medium -- controlled by p",
        ],
        [
            "Channel efficiency",
            "Lower under heavy load",
            "Better under heavy load",
            "Best if p chosen well",
        ],
        [
            "Delay",
            "Low -- transmits instantly when free",
            "Higher -- random waits add delay",
            "Medium",
        ],
        ["Complexity", "Simple", "Simple", "Moderate"],
    ],
)

# CSMA flowchart
fc_csma = ed.Flowchart(
    width=CW,
    height=400,
    caption="Fig 2: p-Persistent CSMA Protocol Flowchart (generalises all three variants)",
)
fc_csma.terminal("start", "Frame ready to send")
fc_csma.decision("sense", "Is channel idle?")
fc_csma.decision("transmit", "Transmit with prob p?")
fc_csma.process("send", "Transmit frame")
fc_csma.decision("success", "Collision detected?")
fc_csma.terminal("done", "Transmission complete")
fc_csma.process("wait_busy", "Wait random time")
fc_csma.process("defer", "Defer one slot (wait 1-p)")
fc_csma.process("backoff", "Backoff and retry")
fc_csma.edge("start", "sense")
fc_csma.edge("sense", "transmit", branch="yes")
fc_csma.edge("sense", "wait_busy", branch="no")
fc_csma.edge("wait_busy", "sense", orthogonal=True)
fc_csma.edge("transmit", "send", branch="yes")
fc_csma.edge("transmit", "defer", branch="no")
fc_csma.edge("defer", "sense", orthogonal=True)
fc_csma.edge("send", "success")
fc_csma.edge("success", "done", branch="no")
fc_csma.edge("success", "backoff", branch="yes")
fc_csma.edge("backoff", "sense", orthogonal=True)
story.extend(fc_csma.as_flowable())
tip(
    "1-persistent: always transmit when idle (p=1). "
    "Non-persistent: sense randomly (wait random time when busy). "
    "p-persistent: transmit with probability p when idle. "
    "All three detect collisions only AFTER they happen -- CSMA/CD adds during-transmission detection."
)
br()


# -----------------------------------------------------------------------------
#  3.7  CSMA/CD
# -----------------------------------------------------------------------------
chap_box("3.7  CSMA/CD -- Carrier Sense Multiple Access with Collision Detection")
section("Overview")
definition(
    "<b>CSMA/CD:</b> An enhancement of CSMA used in wired Ethernet (IEEE 802.3). "
    "While transmitting, the station <b>simultaneously monitors the channel</b>. "
    "If the transmitted signal and the received signal differ (collision), the "
    "station immediately aborts the frame, sends a 48-bit <b>jam signal</b> to ensure "
    "all other stations detect the collision, then backs off and retransmits."
)
body(
    "CSMA/CD dramatically improves efficiency over plain CSMA because collisions "
    "are detected early -- the station stops wasting bandwidth transmitting a "
    "garbled frame."
)

section("Why a Minimum Frame Size?")
body(
    "For CSMA/CD to work, a station must still be transmitting when the collision "
    "signal propagates back to it. The worst case is when two stations at opposite "
    "ends of the cable transmit simultaneously. The round-trip propagation time is "
    "2 * tau (tau = one-way propagation delay). Therefore:"
)
definition(
    "<b>Minimum Frame Size Condition:</b><br/>"
    "The frame transmission time (T<sub>tx</sub>) must be at least twice the one-way "
    "propagation delay (tau):<br/>"
    "&nbsp;&nbsp;&nbsp;&nbsp;<b>T<sub>tx</sub> &gt;= 2 * tau</b><br/>"
    "Since T<sub>tx</sub> = L / R (where L is frame size in bits and R is transmission rate in bps):<br/>"
    "&nbsp;&nbsp;&nbsp;&nbsp;<b>L / R &gt;= 2 * tau</b>  =&gt;  <b>L<sub>min</sub> = 2 * tau * R</b>"
)
body("<b>Worked Example for IEEE 802.3 (10 Mbps Ethernet):</b>")
bullet(
    [
        "Maximum cable length: <b>2500 m</b> (with repeaters)",
        "Signal speed in copper: <b>2 * 10<super>8</super> m/s</b>",
        "One-way propagation delay: <b>tau = 2500 / (2 * 10<super>8</super>) = 12.5 microseconds</b>",
        "Worst-case round-trip time (collision slot time): <b>2 * tau = 25 microseconds</b>",
        "Minimum frame size in bits: <b>L<sub>min</sub> = 25 * 10<super>-6</super> s * 10 * 10<super>6</super> bps = 250 bits</b>",
        "IEEE 802.3 standard round-up: <b>512 bits (64 bytes)</b>. This provides a safety margin. Any frame shorter than 64 bytes is classified as a <b>RUNT frame</b> and automatically discarded.",
    ]
)

section("Binary Exponential Backoff (BEB)")
definition(
    "<b>Binary Exponential Backoff:</b> After the k-th collision, a station waits "
    "a random number of slot times r, where r is chosen uniformly from "
    "{0, 1, 2, ..., 2<super>min(k,10)</super> - 1}. After 16 failed attempts, the transmission "
    "is aborted and an error is reported to the upper layer."
)
code_block("""
 BINARY EXPONENTIAL BACKOFF TABLE:
 =====================================================================
 Collision   | Backoff Range         | Max Slots | Avg Wait
 ------------|----------------------|-----------|----------
 1st         | {0, 1}               | 1         | 0.5 slots
 2nd         | {0, 1, 2, 3}         | 3         | 1.5 slots
 3rd         | {0 ... 7}            | 7         | 3.5 slots
 4th         | {0 ... 15}           | 15        | 7.5 slots
 5th         | {0 ... 31}           | 31        | 15.5 slots
 10th        | {0 ... 1023}         | 1023      | 511.5 slots
 11th-16th   | {0 ... 1023}         | 1023      | (capped at 10)
 17th        | ABORT -- report error |           |

 Slot time in 10 Mbps Ethernet = 51.2 microseconds (512 bits / 10 Mbps)

 KEY INSIGHT: The exponentially growing backoff window adapts to the
 number of competing stations. If many collide -> wider window -> fewer
 future collisions. Self-regulating mechanism.
""")

section("CSMA/CA Flowchart")

fc = ed.Flowchart(
    width=CW, height=650, caption="Fig 4: IEEE 802.11 CSMA/CA (DCF) Working Procedure"
)

# ------------------------------------------------------------------
# Nodes
# ------------------------------------------------------------------

fc.terminal("start", "Frame Ready\nfor Transmission")

fc.process("sense", "Sense Wireless\nChannel")

fc.decision("idle", "Is Channel\nIdle?")

fc.process("wait_busy", "Wait Until Channel\nBecomes Idle")

fc.process("difs", "Wait for DIFS")

fc.process("backoff", "Select Random\nBackoff Value")

fc.decision("counter_zero", "Backoff Counter\nReached 0?")

fc.process("continue_backoff", "Continue Backoff\nCountdown")

fc.process("freeze", "Freeze Backoff if\nChannel Becomes Busy")

fc.process("transmit", "Transmit\nRTS/DATA")

fc.process("receive", "Receive CTS/ACK")

fc.decision("ack", "ACK\nReceived?")

fc.process("increase_cw", "Increase Contention Window")

fc.process("retry", "Increment Retry Counter\nPrepare Retransmission")

fc.decision("retry_limit", "Retry Limit\nExceeded?")

fc.terminal("success", "Transmission\nSuccessful")

fc.terminal("drop", "Drop Frame")

# ------------------------------------------------------------------
# Edges
# ------------------------------------------------------------------

fc.edge("start", "sense")

fc.edge("sense", "idle")

fc.edge("idle", "difs", branch="yes")

fc.edge("idle", "wait_busy", branch="no")

fc.edge("wait_busy", "sense", orthogonal=True)

fc.edge("difs", "backoff")

fc.edge("backoff", "counter_zero")

fc.edge("counter_zero", "transmit", branch="yes")

fc.edge("counter_zero", "continue_backoff", branch="no")

fc.edge("continue_backoff", "freeze")

fc.edge("freeze", "backoff", orthogonal=True)

fc.edge("transmit", "receive")

fc.edge("receive", "ack")

fc.edge("ack", "success", branch="yes")

fc.edge("ack", "increase_cw", branch="no")

fc.edge("increase_cw", "retry")

fc.edge("retry", "retry_limit")

fc.edge("retry_limit", "drop", branch="yes")

fc.edge("retry_limit", "sense", branch="no", orthogonal=True)

story.extend(fc.as_flowable())

sp(8)


# -----------------------------------------------------------------------------
#  3.8  CSMA/CA (WIRELESS)
# -----------------------------------------------------------------------------
chap_box("3.8  CSMA/CA -- Collision Avoidance (IEEE 802.11 Wi-Fi)")
section("Why CSMA/CA Instead of CSMA/CD?")
body(
    "Wireless stations cannot detect their own collisions. When a station transmits, "
    "its signal is so strong locally that it completely drowns out any incoming "
    "collision signal -- the transmitted signal is thousands of times stronger than "
    "anything received. Therefore collision detection is impossible, and 802.11 "
    "uses collision avoidance instead."
)
bullet(
    [
        "<b>Hidden Node Problem:</b> Station A and Station C cannot hear each other (range) "
        "but both can hear the access point B. A transmits to B; C cannot hear A so C "
        "also transmits to B -- collision at B, neither A nor C knows.",
        "<b>Exposed Node Problem:</b> Station B is transmitting to A. Station C can hear B "
        "so C wrongly stays silent, even though C could transmit to D without interfering.",
    ]
)

section("IEEE 802.11 MAC -- DCF Operation")

definition(
    "<b>DCF (Distributed Coordination Function):</b> "
    "The fundamental medium access mechanism used in IEEE 802.11 Wi-Fi. "
    "DCF uses <b>CSMA/CA (Carrier Sense Multiple Access with Collision Avoidance)</b> "
    "to reduce the probability of collisions in wireless networks. "
    "Unlike Ethernet CSMA/CD, wireless stations cannot detect collisions while "
    "transmitting, so collisions are avoided using carrier sensing, inter-frame "
    "spacing, random backoff timers, RTS/CTS exchange, and acknowledgements."
)

bullet(
    [
        "<b>Carrier Sensing:</b> A station listens to the wireless medium before transmission.",
        "<b>DIFS Waiting:</b> The channel must remain idle for a Distributed Inter Frame Space (DIFS) interval before transmission can begin.",
        "<b>Random Backoff:</b> Each station selects a random backoff counter to reduce the probability of simultaneous transmissions.",
        "<b>Backoff Freezing:</b> If the channel becomes busy during countdown, the timer is frozen and resumed later.",
        "<b>RTS/CTS Mechanism:</b> Optional RTS and CTS control frames help solve the hidden node problem.",
        "<b>Positive Acknowledgement:</b> Successful reception is confirmed using ACK frames.",
        "<b>Collision Assumption:</b> If ACK is not received within timeout, the sender assumes collision or frame loss.",
        "<b>Binary Exponential Backoff:</b> After each failed attempt, the contention window size increases exponentially.",
    ]
)
subsection("Key Time Intervals")
info_table(
    ["Interval", "Duration (approx)", "Purpose"],
    [
        [
            "SIFS (Short IFS)",
            "16 us (802.11a)",
            "Highest priority. Used before ACK, CTS. Immediately after frame.",
        ],
        [
            "DIFS (DCF IFS)",
            "34 us (802.11a)",
            "Used before DATA and RTS frames. Station must sense idle for DIFS before backoff.",
        ],
        [
            "EIFS (Extended IFS)",
            "Longest",
            "Used after a received frame had errors. Lowest priority.",
        ],
        ["Slot time", "9 us (802.11a)", "Unit of the random backoff counter."],
    ],
)

subsection("CSMA/CA with RTS/CTS Operation")
bullet(
    [
        "<b>Step 1:</b> Station senses channel. Must be idle for at least DIFS.",
        "<b>Step 2:</b> Station waits a random number of slot times (backoff countdown).",
        "<b>Step 3:</b> Station sends an RTS (Request To Send) frame to the AP with the intended duration.",
        "<b>Step 4:</b> AP replies with CTS (Clear To Send) -- all nearby stations hearing CTS set their "
        "NAV (Network Allocation Vector) timer and stay silent for the declared duration.",
        "<b>Step 5:</b> Station sends the DATA frame.",
        "<b>Step 6:</b> AP sends ACK after SIFS. If no ACK: collision assumed, retry with doubled backoff.",
    ]
)

# Wi-Fi RTS/CTS sequence diagram
seq_wifi = ed.SequenceDiagram(
    width=CW,
    height=270,
    caption="Fig 4: CSMA/CA with RTS/CTS -- resolves hidden node problem",
)
seq_wifi.actor("sta", "Station A")
seq_wifi.actor("ap", "Access Point")
seq_wifi.actor("other", "Other Stations")
seq_wifi.message("sta", "ap", "DIFS + Backoff -- then RTS (duration=D)", arrow="solid")
seq_wifi.message("ap", "sta", "SIFS + CTS (duration=D)", arrow="dashed")
seq_wifi.message(
    "ap", "other", "CTS heard -- set NAV timer (silent for D)", arrow="dashed"
)
seq_wifi.divider("Station A transmits DATA (others stay silent due to NAV)")
seq_wifi.message("sta", "ap", "DATA frame", arrow="solid")
seq_wifi.message("ap", "sta", "SIFS + ACK", arrow="dashed")
seq_wifi.divider("Transmission complete -- NAV expires -- others compete again")
story.extend(seq_wifi.as_flowable())

# -----------------------------------------------------------------------------
#  3.8  CSMA/CA FLOWCHART (FINAL CLEANEST VERSION)
# -----------------------------------------------------------------------------

section("CSMA/CA Flowchart")

fc = ed.Flowchart(
    width=CW, height=800, caption="Fig 4: IEEE 802.11 CSMA/CA (DCF) Working Procedure"
)

# ------------------------------------------------------------------
# Nodes
# ------------------------------------------------------------------

fc.terminal("start", "Frame Ready\nfor Transmission")

fc.process("sense", "Sense Wireless\nChannel")

fc.decision("idle", "Is Channel\nIdle?")

fc.process("wait_busy", "Wait Until Channel\nBecomes Idle")

fc.process("difs", "Wait for DIFS")

fc.process("backoff", "Select Random\nBackoff Value")

fc.decision("counter_zero", "Backoff Counter\nReached 0?")

fc.process("continue_backoff", "Continue Backoff\nCountdown")

fc.process("freeze", "Freeze Backoff if\nChannel Becomes Busy")

fc.process("transmit", "Transmit\nRTS/DATA")

fc.process("receive", "Receive CTS/ACK")

fc.decision("ack", "ACK\nReceived?")

fc.process("increase_cw", "Increase Contention\nWindow")

fc.process("retry", "Increment Retry Counter\nPrepare Retransmission")

fc.decision("retry_limit", "Retry Limit\nExceeded?")

fc.terminal("success", "Transmission\nSuccessful")

fc.terminal("drop", "Drop Frame")

# ------------------------------------------------------------------
# Edges
# ------------------------------------------------------------------

fc.edge("start", "sense")

fc.edge("sense", "idle")

fc.edge("idle", "difs", branch="yes")

fc.edge("idle", "wait_busy", branch="no")

fc.edge("wait_busy", "sense", orthogonal=True)

fc.edge("difs", "backoff")

fc.edge("backoff", "counter_zero")

# IMPORTANT:
# No branch labels here to avoid duplicate "No" rendering

fc.edge("counter_zero", "transmit")

fc.edge("counter_zero", "continue_backoff", orthogonal=True)

fc.edge("continue_backoff", "freeze")

fc.edge("freeze", "backoff", orthogonal=True)

fc.edge("transmit", "receive")

fc.edge("receive", "ack")

fc.edge("ack", "success", branch="yes")

fc.edge("ack", "increase_cw", branch="no")

fc.edge("increase_cw", "retry")

fc.edge("retry", "retry_limit")

fc.edge("retry_limit", "drop", branch="yes")

fc.edge("retry_limit", "sense", branch="no", orthogonal=True)

story.extend(fc.as_flowable())

sp(8)
tip(
    "RTS/CTS is optional in 802.11 -- used only for large frames where collision cost is high. "
    "Small frames skip RTS/CTS and transmit directly after DIFS + backoff. "
    "ACK is always required in 802.11 (unlike Ethernet)."
)
br()


# -----------------------------------------------------------------------------
#  3.9  IEEE 802.3 AND ETHERNET
# -----------------------------------------------------------------------------
chap_box("3.9  IEEE 802.3 and Ethernet")
section("Overview")
definition(
    "<b>Ethernet (IEEE 802.3):</b> The dominant wired LAN technology, first developed "
    "by Xerox, DEC, and Intel in 1976 (DIX Ethernet), then standardized as IEEE 802.3 "
    "in 1980. Ethernet uses CSMA/CD for medium access. Modern Ethernet switches have "
    "eliminated collisions by giving each port a dedicated full-duplex link, making "
    "CSMA/CD largely irrelevant in modern networks -- but still required for exam study."
)

section("IEEE 802.3 Ethernet Frame Format")
frame_format(
    "IEEE 802.3 Ethernet Frame Format",
    [
        ("PREAMBLE", "7 bytes"),
        ("SFD", "1 byte"),
        ("DEST MAC", "6 bytes"),
        ("SRC MAC", "6 bytes"),
        ("LEN/TYPE", "2 bytes"),
        ("DATA (Payload)", "46-1500 bytes"),
        ("FCS", "4 bytes"),
    ],
)

code_block("""
 PREAMBLE (7 bytes = 56 bits):
   10101010 repeated 7 times.
   Allows receiver NIC to synchronize its clock (phase-lock).

 SFD -- Start Frame Delimiter (1 byte = 10101011):
   The 7th byte of the preamble ends with 11 instead of 10.
   Signals: "next byte is the Destination MAC address."

 DESTINATION MAC (6 bytes = 48 bits):
   MAC address of the intended recipient.
   FF:FF:FF:FF:FF:FF = broadcast (all stations on segment receive).
   Multicast if first bit of first byte = 1.

 SOURCE MAC (6 bytes = 48 bits):
   MAC address of the sender NIC. Always a unicast address.

 LENGTH / TYPE (2 bytes):
   Value <= 1500 (0x05DC): IEEE 802.3 format -- field = payload length.
   Value >= 1536 (0x0600): Ethernet II format -- field = EtherType.
   EtherType 0x0800 = IPv4, 0x0806 = ARP, 0x86DD = IPv6, 0x8100 = VLAN.

 DATA (46 to 1500 bytes):
   Upper-layer payload (usually IP packet, encapsulated via LLC or directly).
   Minimum 46 bytes -- padded with zeros if shorter.
   Minimum total frame size = 64 bytes (for CSMA/CD to work at 10 Mbps).

 FCS (4 bytes = 32 bits):
   CRC-32 computed over DST+SRC+LEN/TYPE+DATA.
   Receiver recomputes CRC; mismatch = frame discarded silently.

 Frame sizes:
   Minimum: 64 bytes (512 bits) -- anything shorter is a runt (error).
   Maximum: 1518 bytes (MTU = 1500 bytes data).
   Jumbo frames (non-standard): up to 9000 bytes payload.
""")

section("Ethernet Cabling Standards (802.3 Variants)")
info_table(
    ["Standard", "Speed", "Medium", "Max Segment", "Topology", "Notes"],
    [
        [
            "10BASE5",
            "10 Mbps",
            "Thick coax (RG-8)",
            "500 m",
            "Bus",
            "Thicknet -- vampire tap connectors. Original Ethernet. Obsolete.",
        ],
        [
            "10BASE2",
            "10 Mbps",
            "Thin coax (RG-58)",
            "185 m",
            "Bus",
            "Thinnet -- BNC T-connectors. Cheaper than 10BASE5. Obsolete.",
        ],
        [
            "10BASE-T",
            "10 Mbps",
            "UTP Cat3",
            "100 m",
            "Star (hub)",
            "First twisted-pair Ethernet. Hub-based. RJ-45 connectors.",
        ],
        [
            "100BASE-TX",
            "100 Mbps",
            "UTP Cat5",
            "100 m",
            "Star",
            "Fast Ethernet. Most common in 1990s offices.",
        ],
        [
            "100BASE-FX",
            "100 Mbps",
            "Multimode fiber",
            "412 m",
            "Star",
            "Fast Ethernet over fiber. Longer runs.",
        ],
        [
            "1000BASE-T",
            "1 Gbps",
            "UTP Cat5e/6",
            "100 m",
            "Star",
            "Gigabit Ethernet. Dominant in modern LANs. Uses all 4 pairs.",
        ],
        [
            "1000BASE-SX",
            "1 Gbps",
            "Multimode fiber",
            "550 m",
            "Star",
            "Gigabit over short-wavelength fiber. Data centers.",
        ],
        [
            "10GBASE-T",
            "10 Gbps",
            "UTP Cat6a/7",
            "100 m",
            "Star",
            "10 Gigabit Ethernet. Data centers, server rooms.",
        ],
        [
            "10GBASE-SR",
            "10 Gbps",
            "Multimode fiber",
            "400 m",
            "Star",
            "10GbE over fiber. Short reach.",
        ],
    ],
)
body(
    "The naming convention <b>XBASEy</b> means: X = speed in Mbps, BASE = baseband signalling, "
    "y = cable type/length (T = twisted pair, F = fiber, number = max length in hundreds of metres)."
)

section("Ethernet Switch vs Hub")
info_table(
    ["Feature", "Hub (Layer 1)", "Switch (Layer 2)"],
    [
        [
            "Operation",
            "Broadcasts all traffic to all ports",
            "Forwards frames only to the correct port (MAC table)",
        ],
        [
            "Collisions",
            "All ports in one collision domain",
            "Each port = separate collision domain (no collisions with full-duplex)",
        ],
        [
            "Bandwidth",
            "Shared among all ports",
            "Dedicated per port (full-duplex = 2x line rate)",
        ],
        [
            "Intelligence",
            "None -- pure signal repeater",
            "MAC address table, VLAN support, QoS",
        ],
        ["Mode", "Half-duplex only", "Full-duplex supported"],
        ["Status", "Obsolete -- replaced by switches", "Standard in all modern LANs"],
    ],
)
tip(
    "Name decoding: 100BASE-TX = 100 Mbps, baseband, twisted pair. "
    "1000BASE-T = Gigabit Ethernet on Cat5e/6. "
    "Minimum Ethernet frame = 64 bytes. Maximum = 1518 bytes (1500 payload + 18 header). "
    "EtherType 0x0800 = IPv4 -- exam frequently tests this."
)
br()


# -----------------------------------------------------------------------------
#  3.10  IEEE 802.4 -- TOKEN BUS
# -----------------------------------------------------------------------------
chap_box("3.10  IEEE 802.4 -- Token Bus")
section("Overview")
definition(
    "<b>IEEE 802.4 Token Bus:</b> A LAN standard that combines bus topology (physical) "
    "with token passing (logical ring). Stations on a coaxial bus form a <b>logical "
    "ring</b> -- each station knows the address of its predecessor and successor in "
    "the logical ring. A token is passed in decreasing address order around this "
    "logical ring. Only the station holding the token may transmit."
)
bullet(
    [
        "Physical topology: Bus (coaxial cable) -- all stations share one cable.",
        "Logical topology: Ring -- token passes from station to station in address order.",
        "Deterministic access -- guaranteed maximum wait time for the token.",
        "No collisions -- only one station transmits at a time (the token holder).",
        "Designed for industrial automation (factory networks) where determinism matters.",
        "Used by: General Motors Manufacturing Automation Protocol (MAP).",
        "Now largely obsolete -- replaced by Industrial Ethernet and PROFIBUS.",
    ]
)

section("Token Bus Operation")
bullet(
    [
        "<b>Initialization:</b> The station with the highest address claims the token and starts the logical ring.",
        "<b>Token passing:</b> After transmitting (or having nothing to send), the station sends a token frame to the next station in the logical ring (next-lower address).",
        "<b>Ring maintenance:</b> If a station fails, the predecessor detects the missing ACK for the token and skips that station (removes it from the ring).",
        "<b>Adding a station:</b> Existing stations periodically invite new stations to join the ring during a ring-maintenance window.",
        "<b>Token recovery:</b> If the token is lost (station fails while holding it), a recovery procedure re-establishes the token.",
    ]
)

section("IEEE 802.4 Frame Format")
frame_format(
    "IEEE 802.4 Token Bus Frame Format",
    [
        ("PREAMBLE", "1+ bytes"),
        ("SD", "1 byte"),
        ("FC", "1 byte"),
        ("DEST", "2 or 6 bytes"),
        ("SRC", "2 or 6 bytes"),
        ("DATA (Payload)", "0-8182 bytes"),
        ("FCS", "4 bytes"),
        ("ED", "1 byte"),
    ],
)

code_block("""
 PREAMBLE: Synchronization pattern.
 SD (Start Delimiter): Marks start of frame.
 FC (Frame Control): Identifies frame type.
   - LLC data frame, token frame, claim_token, who_follows, resolve_contention.
 DST (Destination Address): 2 or 6 byte MAC address.
 SRC (Source Address): 2 or 6 byte MAC address.
 DATA: User data payload (0 to 8182 bytes).
 FCS (Frame Check Sequence): 32-bit CRC over FC+DST+SRC+DATA.
 ED (End Delimiter): Marks end of frame.

 SPECIAL FRAMES:
   Token Frame: FC=token, DST=next station's address. Contains no data.
   Claim Token:  Used during initialization to establish who holds the token first.
""")
tip(
    "802.4 Token Bus = bus topology + token passing. "
    "Deterministic -- bounded delay. Used in factory automation. "
    "Contrast with 802.5 Token Ring (physical ring, not bus). Now obsolete."
)
br()


# -----------------------------------------------------------------------------
#  3.11  IEEE 802.5 -- TOKEN RING
# -----------------------------------------------------------------------------
chap_box("3.11  IEEE 802.5 -- Token Ring")
section("Overview")
definition(
    "<b>IEEE 802.5 Token Ring:</b> A LAN standard using a physical ring topology. "
    "A special 3-byte pattern called a <b>token</b> circulates continuously around "
    "the ring. Only the station holding the token may transmit. After transmitting, "
    "the station removes its own frame from the ring and releases the token "
    "for the next station. IBM introduced Token Ring commercially in 1985."
)
bullet(
    [
        "Physical topology: Ring (each station connected to exactly two others).",
        "Token: a special 3-byte pattern (SD + AC + ED) that grants transmission rights.",
        "Speeds: 4 Mbps (original) and 16 Mbps.",
        "Deterministic -- bounded maximum wait time (all stations get a turn).",
        "No collisions -- only the token holder transmits.",
        "More complex and expensive than Ethernet. Largely replaced by Ethernet by the 2000s.",
    ]
)

section("Token Ring Operation -- Step by Step")
bullet(
    [
        "<b>Step 1 -- Idle:</b> The free token circulates around the ring. All stations pass it along.",
        "<b>Step 2 -- Capture:</b> A station with data to send captures the free token by changing one bit (the T bit in the AC byte) to 1, making it a busy token.",
        "<b>Step 3 -- Transmit:</b> The station immediately appends its data frame after the token and transmits both around the ring.",
        "<b>Step 4 -- Propagation:</b> The frame travels the entire ring. Each intermediate station amplifies and retransmits it (ring is an active device).",
        "<b>Step 5 -- Destination copy:</b> The destination station copies the frame from the ring, sets the A (Address Recognized) and C (Frame Copied) bits in the frame trailer.",
        "<b>Step 6 -- Frame removal:</b> When the frame travels back to the originating station, it removes the frame from the ring (absorbs it).",
        "<b>Step 7 -- Token release:</b> The originating station releases a new free token for the next station.",
    ]
)

section("IEEE 802.5 Frame Format")
body("<b>Token Frame (3 bytes):</b>")
frame_format(
    "IEEE 802.5 Token Frame Format",
    [
        ("SD (Start Delimiter)", "1 byte"),
        ("AC (Access Control)", "1 byte"),
        ("ED (End Delimiter)", "1 byte"),
    ],
)
body("<b>Data Frame:</b>")
frame_format(
    "IEEE 802.5 Data Frame Format",
    [
        ("SD (Start Delimiter)", "1 byte"),
        ("AC (Access Control)", "1 byte"),
        ("FC (Frame Control)", "1 byte"),
        ("DEST", "2 or 6 bytes"),
        ("SRC", "2 or 6 bytes"),
        ("DATA (Payload)", "0-17800 bytes"),
        ("FCS", "4 bytes"),
        ("ED (End Delimiter)", "1 byte"),
        ("FS (Frame Status)", "1 byte"),
    ],
)

code_block("""
 SD (Start Delimiter): Uses non-data symbols to mark frame start.
 AC (Access Control): Contains P (priority), T (token bit), M (monitor).
    T bit = 0: free token.   T bit = 1: busy token (station is transmitting).
 FC (Frame Control): LLC data (00) or MAC control frame (01).
 DST: Destination MAC address.
 SRC: Source MAC address.
 DATA: Upper-layer payload.
 FCS: CRC-32 error check.
 ED (End Delimiter): Marks end of frame. Contains E (error) and I (intermediate) bits.
 FS (Frame Status): Contains A (address recognized) and C (frame copied) bits.
    Set by the DESTINATION station after it reads the frame.
    The SOURCE station checks these bits to know if delivery was successful.
 
 FREE TOKEN = SD + AC(T=0) + ED  (3 bytes, no data)
""")

section("Active Monitor")
body(
    "One station is elected as the <b>Active Monitor (AM)</b>. The AM is responsible "
    "for ring maintenance: it generates a new token if the token is lost, removes "
    "continuously circulating frames (a transmitting station that failed to remove "
    "its own frame), and monitors timing. Other stations are <b>Standby Monitors</b> "
    "ready to take over if the AM fails."
)

section("Token Ring vs Ethernet")
info_table(
    ["Feature", "Token Ring (802.5)", "Ethernet (802.3)"],
    [
        ["Topology", "Physical ring", "Star (switch-based) or Bus (legacy)"],
        [
            "Access method",
            "Token passing (collision-free)",
            "CSMA/CD (contention-based)",
        ],
        [
            "Determinism",
            "Yes -- bounded max wait time",
            "No -- unbounded delay under heavy load",
        ],
        ["Speed", "4 or 16 Mbps", "10M / 100M / 1G / 10G / 100G bps"],
        ["Complexity", "High -- token management, AM", "Low -- simple protocol"],
        [
            "Cost",
            "More expensive (MAU, ring wiring)",
            "Cheaper (straight cable, commodity NICs)",
        ],
        [
            "Performance",
            "Degrades gracefully under heavy load",
            "Collapses under heavy load (legacy bus)",
        ],
        ["Status", "Obsolete -- withdrawn from market", "Dominant -- used everywhere"],
    ],
)
tip(
    "Token Ring: Physical ring, token passes around, no collisions, deterministic. "
    "Frame travels full ring; source removes it. Active Monitor manages ring health. "
    "Speeds: 4 Mbps / 16 Mbps. Now replaced by Ethernet."
)

# Token Ring state machine diagram
sm_tr = ed.StateMachine(
    width=CW,
    height=200,
    caption="Fig 5: Token Ring station state machine -- idle, transmitting, draining",
)
sm_tr.state("idle", "Idle (repeating)", initial=True)
sm_tr.state("tx", "Transmitting")
sm_tr.state("drain", "Draining frame")
sm_tr.state("release", "Release token", accepting=True)
sm_tr.transition("idle", "tx", label="token captured")
sm_tr.transition("tx", "drain", label="frame sent")
sm_tr.transition("drain", "release", label="own frame absorbed")
sm_tr.transition("release", "idle", label="new token released")
story.extend(sm_tr.as_flowable())
br()


# -----------------------------------------------------------------------------
#  3.12  FDDI
# -----------------------------------------------------------------------------
chap_box("3.12  FDDI -- Fiber Distributed Data Interface")
section("Overview")
definition(
    "<b>FDDI (Fiber Distributed Data Interface):</b> A high-speed LAN/MAN standard "
    "developed by ANSI (X3T9.5) in the late 1980s. FDDI uses a dual counter-rotating "
    "fiber optic ring running at <b>100 Mbps</b> and can span distances up to "
    "<b>200 km</b> with up to <b>500 stations</b>. It uses the Timed Token Protocol "
    "(TTP) for MAC, providing both synchronous (real-time) and asynchronous "
    "(data) bandwidth."
)
bullet(
    [
        "Speed: 100 Mbps (very fast for its era -- 1988-2000s).",
        "Medium: Multimode fiber (primary), single-mode fiber (extended distance), or STP copper (CDDI variant).",
        "Ring length: up to 200 km (dual ring).",
        "Stations: up to 500 nodes.",
        "Token-based MAC: Timed Token Protocol (TTP).",
        "Fault tolerant: dual ring can automatically heal a single cable or station failure.",
        "Used as: campus backbone, connecting buildings, MAN rings, connecting Ethernet LANs.",
        "Now largely replaced by Gigabit Ethernet and MPLS.",
    ]
)

section("Dual Ring Architecture")
definition(
    "<b>Dual Ring:</b> FDDI uses two counter-rotating fiber rings -- a <b>Primary Ring</b> "
    "(data flows clockwise) and a <b>Secondary Ring</b> (data flows counter-clockwise). "
    "Normally only the primary ring carries data; the secondary ring is on standby. "
    "If the primary ring breaks (cable cut or station failure), the two rings are "
    "automatically joined at the point of failure to form a single large ring, "
    "called <b>ring wrapping</b> -- maintaining connectivity."
)

# FDDI dual ring network diagram
fddi_net = ed.NetworkDiagram(
    width=CW,
    height=200,
    caption="Fig 6: FDDI Dual Counter-Rotating Ring -- Primary (solid) and Secondary (dashed backup)",
)
fddi_net.ring_topology(["DAS A", "DAS B", "DAS C", "DAS D"])
story.extend(fddi_net.as_flowable())

section("Station Types")
info_table(
    ["Station Type", "Abbreviation", "Connection", "Description"],
    [
        [
            "Dual Attachment Station",
            "DAS",
            "Both rings",
            "Connected to both primary and secondary ring. Full fault tolerance. Expensive.",
        ],
        [
            "Single Attachment Station",
            "SAS",
            "Primary ring only",
            "Connected to only the primary ring via a concentrator. Cheaper. Failure does not break the ring.",
        ],
        [
            "Dual Attachment Concentrator",
            "DAC",
            "Both rings + SAS ports",
            "Hub for SAS devices. Connected to both rings. SAS devices attach here.",
        ],
        [
            "Single Attachment Concentrator",
            "SAC",
            "Primary ring + SAS ports",
            "Attaches to ring via a DAC. For extending the network.",
        ],
    ],
)

section("Timed Token Protocol (TTP)")
definition(
    "<b>TTP (Timed Token Protocol):</b> FDDI's MAC mechanism, more sophisticated than "
    "simple token ring. TTP allocates bandwidth in two categories: synchronous "
    "(guaranteed, for real-time traffic) and asynchronous (best-effort, for data)."
)
bullet(
    [
        "<b>TTRT (Target Token Rotation Time):</b> Negotiated during ring initialization. All stations agree on a target time T_TTRT for the token to complete one full ring rotation.",
        "<b>Synchronous allocation:</b> Each station reserves a fixed portion of TTRT for synchronous (guaranteed) data. Station always transmits synchronous data when it gets the token.",
        "<b>Asynchronous allocation:</b> If the token arrives EARLY (before TTRT expires), the station may also transmit asynchronous (non-time-critical) data.",
        "<b>Token monitoring:</b> If the token is late (rotation time > 2*TTRT), all asynchronous transmissions are suspended to let the ring recover.",
        "This dual-queue mechanism provides QoS -- real-time traffic gets guaranteed bandwidth, data traffic gets whatever is left.",
    ]
)
code_block("""
 FDDI TIMED TOKEN PROTOCOL:
 =====================================================================
 Variables per station:
   T_TTRT = Target Token Rotation Time (negotiated, e.g. 8 ms)
   T_Req  = Each station's synchronous allocation request
   TRT    = Token Rotation Timer (measures actual rotation)

 On receiving the token:
   1. Transmit all queued SYNCHRONOUS frames (guaranteed bandwidth).
   2. Check if token arrived EARLY: TRT < T_TTRT
      - If early: also transmit ASYNCHRONOUS frames until TRT >= T_TTRT.
      - If late:  no asynchronous frames -- ring is overloaded.
   3. Release the token to the next station.

 EFFICIENCY:
   FDDI can sustain close to 100 Mbps on the ring because multiple
   frames can be on the ring simultaneously (unlike basic Token Ring
   where the source absorbs its frame before releasing the token).
   FDDI releases the token IMMEDIATELY after transmitting (early token
   release), allowing the next station to begin transmitting even
   before the first station's frame completes the ring.
""")

section("FDDI Frame Format")
frame_format(
    "FDDI Frame Format",
    [
        ("PA (Preamble)", "16 bytes"),
        ("SD", "1 byte"),
        ("FC", "1 byte"),
        ("DEST", "6 bytes"),
        ("SRC", "6 bytes"),
        ("DATA (Payload)", "0-4478 bytes"),
        ("FCS", "4 bytes"),
        ("ED", "1 byte"),
        ("FS", "1 byte"),
    ],
)

code_block("""
 PA  (Preamble): 16 idle symbols -- synchronization.
 SD  (Start Delimiter): JK symbol pair (non-data symbols in 4B/5B encoding).
 FC  (Frame Control): Synchronous vs asynchronous, LLC vs MAC frame.
 DST: 6-byte destination MAC address.
 SRC: 6-byte source MAC address.
 DATA: Payload -- maximum 4478 bytes (larger than Ethernet's 1500 bytes).
 FCS: CRC-32 error detection.
 ED  (End Delimiter): T symbol.
 FS  (Frame Status): Error, Address-recognized, Frame-copied bits.

 TOKEN FORMAT:
 | PA  | SD | FC | ED |
 | 16B | 1B | 1B | 1B |

 ENCODING: FDDI uses 4B/5B encoding (every 4 data bits encoded as
 5 wire bits) with NRZI physical signalling. Provides built-in
 synchronization and allows special non-data symbols (J, K, T, R, S)
 to be used as frame delimiters without bit stuffing.
""")

section("FDDI vs Token Ring vs Ethernet")
info_table(
    ["Feature", "FDDI", "Token Ring (802.5)", "Ethernet (802.3)"],
    [
        ["Speed", "100 Mbps", "4 / 16 Mbps", "10M -- 100G Mbps"],
        ["Medium", "Fiber (primary)", "STP copper", "UTP / Fiber"],
        [
            "Topology",
            "Dual counter-rotating ring",
            "Single physical ring",
            "Star (switch)",
        ],
        ["MAC", "Timed Token Protocol", "Token passing", "CSMA/CD"],
        ["Max span", "200 km", "~300 m (MAU limit)", "100 m (copper)"],
        ["Stations", "Up to 500", "Up to 250", "Virtually unlimited (switched)"],
        [
            "Fault tolerance",
            "Dual ring -- self-healing",
            "Active Monitor",
            "Switch redundancy (STP)",
        ],
        ["Bandwidth", "Synchronous + Asynchronous", "Priority levels", "Best-effort"],
        [
            "Status",
            "Obsolete -- Gigabit Ethernet replaced it",
            "Obsolete",
            "Current standard",
        ],
    ],
)
tip(
    "FDDI: 100 Mbps, dual fiber ring, 200 km, 500 nodes, Timed Token Protocol, "
    "4B/5B encoding, synchronous+asynchronous bandwidth. "
    "Fault tolerance via ring wrapping when cable fails. "
    "DAS connects to both rings; SAS connects to only primary via concentrator."
)
br()


# =============================================================================
#  3.13  QUICK REVISION SUMMARY
# =============================================================================
part_box("UNIT III -- QUICK REVISION SUMMARY")
chap_box("Key Concepts at a Glance")

info_table(
    ["Topic", "Key Point to Remember"],
    [
        [
            "MAC Sub-layer",
            "Determines who uses the shared channel. Part of Data Link layer. "
            "3 protocol families: static, random access, controlled access.",
        ],
        [
            "TDMA (Static)",
            "Time divided into N fixed slots. Each station gets 1 slot per frame. "
            "Efficient for voice (constant rate). Wastes bandwidth for bursty data.",
        ],
        [
            "FDMA (Static)",
            "Frequency spectrum divided into N sub-bands. Simultaneous transmission. "
            "Guard bands prevent interference. Used in FM radio, 1G cellular.",
        ],
        [
            "Pure ALOHA",
            "Transmit anytime. Vulnerable period = 2T. "
            "S = G * e<super>-2G</super>. Max throughput = 18.4% at G=0.5.",
        ],
        [
            "Slotted ALOHA",
            "Transmit only at slot boundaries. Vulnerable period = T. "
            "S = G * e<super>-G</super>. Max throughput = 36.8% at G=1.0. Exactly 2x Pure ALOHA.",
        ],
        [
            "General ALOHA",
            "S = G * e<super>-aG</super>. a=2 for Pure, a=1 for Slotted. "
            "Max = 1/(2e) = 18.4% and 1/e = 36.8% respectively.",
        ],
        [
            "1-Persistent CSMA",
            "If idle: transmit immediately (p=1). If busy: wait and keep sensing. "
            "High collision rate when multiple stations wait for busy channel.",
        ],
        [
            "Non-Persistent CSMA",
            "If idle: transmit. If busy: wait RANDOM time then sense again. "
            "Less aggressive. Better efficiency under heavy load.",
        ],
        [
            "p-Persistent CSMA",
            "If idle: transmit with prob p; defer 1 slot with prob (1-p). "
            "Generalises both: p=1 gives 1-persistent.",
        ],
        [
            "CSMA/CD",
            "IEEE 802.3 Ethernet. Detect collision DURING transmission. "
            "Send JAM (48 bits), Binary Exponential Backoff, abort after 16 attempts. "
            "Min frame = 64 bytes. Slot = 51.2 us (10 Mbps).",
        ],
        [
            "CSMA/CA",
            "IEEE 802.11 Wi-Fi. Cannot detect collision (wireless). "
            "Avoid BEFORE transmitting: DIFS + backoff + RTS/CTS + DATA + ACK.",
        ],
        [
            "Ethernet Frame",
            "Preamble(7B)+SFD(1B)+DstMAC(6B)+SrcMAC(6B)+Type/Len(2B)+Data(46-1500B)+FCS(4B). "
            "Min=64B, Max=1518B. EtherType 0x0800=IPv4, 0x0806=ARP, 0x86DD=IPv6.",
        ],
        [
            "802.3 Cabling",
            "10BASE5: thick coax 500m. 10BASE2: thin coax 185m. "
            "10BASE-T: UTP Cat3. 100BASE-TX: UTP Cat5. 1000BASE-T: Cat5e/6.",
        ],
        [
            "IEEE 802.4 Token Bus",
            "Bus topology + logical ring. Token passes in address order. "
            "Deterministic. Used in factory automation (MAP). Now obsolete.",
        ],
        [
            "IEEE 802.5 Token Ring",
            "Physical ring. Token (3-byte) circulates. Only token holder transmits. "
            "Source removes its own frame. 4/16 Mbps. Active Monitor manages ring.",
        ],
        [
            "Token Ring Frame",
            "SD+AC+FC+DST+SRC+DATA+FCS+ED+FS. "
            "T bit in AC: 0=free token, 1=busy. A+C bits in FS set by destination.",
        ],
        [
            "FDDI",
            "100 Mbps, dual fiber ring (primary+secondary), 200km, 500 nodes. "
            "Timed Token Protocol. Synchronous+asynchronous bandwidth. 4B/5B encoding.",
        ],
        [
            "FDDI Fault Tolerance",
            "Single cable break: ring wrapping joins primary and secondary into one ring. "
            "DAS: dual attachment (both rings). SAS: single attachment (via concentrator).",
        ],
        [
            "FDDI TTP",
            "TTRT = target rotation time. Token early = can send async data. "
            "Token late = sync only. Early token release for high efficiency.",
        ],
        [
            "Throughput Summary",
            "Pure ALOHA: 18.4%. Slotted ALOHA: 36.8%. CSMA: up to ~80-90%. "
            "Token Ring/Bus: nearly 100% under heavy load (no collisions).",
        ],
    ],
)

highlight(
    "<b>UNIT III EXAM BLUEPRINT:</b>  "
    "2-mark: Define MAC, ALOHA, FDDI, CSMA/CD. Give Pure/Slotted ALOHA throughput formula.  "
    "5-mark: Compare Pure vs Slotted ALOHA (table + formulas). "
    "Explain CSMA variants (1-persistent, non-persistent, p-persistent). "
    "Draw IEEE 802.3 Ethernet frame. Compare Token Ring vs Ethernet.  "
    "10-mark: Explain CSMA/CD with flowchart and minimum frame size calculation. "
    "Explain IEEE 802.5 Token Ring operation with frame format. "
    "Explain FDDI with dual ring, TTP, station types, and fault tolerance.",
    YELLOW_CARD,
    YELLOW,
)


# =============================================================================
#  BUILD PDF
# =============================================================================
doc = SimpleDocTemplate(
    "CN_Unit3_Notes.pdf",
    pagesize=A4,
    leftMargin=PM,
    rightMargin=PM,
    topMargin=PM,
    bottomMargin=PM,
    title="Computer Networks IT-411 Unit III Notes",
    author="UIT-RGPV (Autonomous) Bhopal",
)
doc.build(story, onFirstPage=page_decor, onLaterPages=page_decor)
print("Generated: CN_Unit3_Notes.pdf")
