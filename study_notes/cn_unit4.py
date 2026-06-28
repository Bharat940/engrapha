"""
Computer Networks (IT-411) -- Unit IV Notes
UIT-RGPV (Autonomous) Bhopal | Semester IV
Complete exam notes with vector diagrams.
Run: python cn_unit4_notes.py
Output: CN_Unit4_Notes.pdf
"""

from __future__ import annotations

from typing import Any, Callable

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
import engrapha_diagrams.shapes as pds

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


def packet_format(
    caption: str, fields: list[tuple[str, int]], bit_ruler: bool = True
) -> None:
    th = S(
        f"P_HDR_{caption[:10]}",
        fontSize=7.5,
        textColor=colors.HexColor("#79c0ff"),
        fontName="Helvetica-Bold",
        alignment=TA_CENTER,
        leading=9,
    )
    ruler_style = S(
        f"P_RULER_{caption[:10]}",
        fontSize=6.5,
        textColor=colors.HexColor("#8b949e"),
        fontName="Helvetica-Bold",
        alignment=TA_CENTER,
        leading=8,
    )

    grid_rows = []
    current_row = []
    current_width = 0

    for name, width in fields:
        if width >= 32 and current_width > 0:
            current_row.append(("", 32 - current_width))
            grid_rows.append(current_row)
            current_row = []
            current_width = 0

        if width >= 32:
            grid_rows.append([(name, width)])
        else:
            if current_width + width > 32:
                current_row.append(("", 32 - current_width))
                grid_rows.append(current_row)
                current_row = []
                current_width = 0
            current_row.append((name, width))
            current_width += width
            if current_width == 32:
                grid_rows.append(current_row)
                current_row = []
                current_width = 0

    if current_row:
        current_row.append(("", 32 - current_width))
        grid_rows.append(current_row)

    matrix: list[list[Any]] = []
    spans = []

    if bit_ruler:
        ruler_cells: list[Any] = [""] * 32
        for col_idx in [0, 4, 8, 16, 24, 31]:
            ruler_cells[col_idx] = Paragraph(str(col_idx), ruler_style)
        matrix.append(ruler_cells)
        ruler_offset = 1
    else:
        ruler_offset = 0

    current_rl_row = ruler_offset
    for r_idx, r_fields in enumerate(grid_rows):
        max_height = 1
        for name, width in r_fields:
            if width > 32:
                max_height = max(max_height, width // 32)

        for _ in range(max_height):
            row_cells: list[Any] = [""] * 32
            matrix.append(row_cells)

        col_cursor = 0
        for name, width in r_fields:
            if not name and width == 0:
                continue
            if name:
                f_size, l_ing = (5.0, 6.0) if width <= 2 else (6.0, 7.0) if width <= 4 else (7.0, 8.0) if width <= 6 else (8.0, 10.0)
                cell_th = S(
                    f"P_HDR_{caption[:10]}_{r_idx}_{col_cursor}",
                    fontSize=f_size,
                    textColor=colors.HexColor("#79c0ff"),
                    fontName="Helvetica-Bold",
                    alignment=TA_CENTER,
                    leading=l_ing,
                )
                if width >= 8:
                    text = f"<b>{name}</b><br/><font size=5.5 color='#9da7b3'>{width} bits</font>"
                else:
                    text = f"<b>{name}</b><br/><font size=5.0 color='#9da7b3'>{width}</font>"
                text_p = Paragraph(text, cell_th)
            else:
                text_p = ""

            matrix[current_rl_row][col_cursor] = text_p

            start_col = col_cursor
            end_col = col_cursor + min(width, 32) - 1
            start_row = current_rl_row
            end_row = current_rl_row + max_height - 1

            if start_col != end_col or start_row != end_row:
                spans.append(("SPAN", (start_col, start_row), (end_col, end_row)))

            col_cursor += min(width, 32)

        current_rl_row += max_height

    col_widths = [CW / 32.0] * 32
    row_heights = []
    if bit_ruler:
        row_heights.append(10)
    for _ in range(len(matrix) - (1 if bit_ruler else 0)):
        row_heights.append(26)

    t = Table(matrix, colWidths=col_widths, rowHeights=row_heights)

    style_commands: list[tuple[Any, ...]] = [
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
        ("LEFTPADDING", (0, 0), (-1, -1), 1),
        ("RIGHTPADDING", (0, 0), (-1, -1), 1),
    ]

    start_grid_row = 1 if bit_ruler else 0
    style_commands.extend(
        [
            ("GRID", (0, start_grid_row), (-1, -1), 0.75, TABLE_BDR),
            ("BACKGROUND", (0, start_grid_row), (-1, -1), CARD_DARK),
        ]
    )

    style_commands.extend(spans)
    t.setStyle(TableStyle(style_commands))
    add(t)

    if caption:
        add(Spacer(1, 4))
        add(
            Paragraph(
                f"<i>{caption}</i>",
                S(
                    f"P_CAP_{caption[:10]}",
                    fontSize=8.5,
                    textColor=WHITE_DIM,
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
add(Paragraph("Unit IV -- Complete Exam Notes", COVER_H2))
add(Paragraph("Subject Code: IT-411  |  UIT-RGPV (Autonomous) Bhopal", COVER_SUB))
add(Paragraph("Semester IV  |  Based on University Syllabus 2024-25", COVER_SUB))
sp(10)
rule(CYAN, 1.5)
sp(8)

info_table(
    ["Topic", "Coverage"],
    [
        [
            "4.1 Network Layer Overview",
            "Role, services, store-and-forward packet switching",
        ],
        [
            "4.2 Logical Addressing -- IPv4",
            "32-bit addresses, dotted decimal, address classes",
        ],
        [
            "4.3 Classful Addressing",
            "Classes A-E, default masks, host/network bits, limitations",
        ],
        [
            "4.4 Classless Addressing (CIDR)",
            "CIDR notation, subnetting, VLSM, supernetting",
        ],
        [
            "4.5 Address Mapping -- ARP and RARP",
            "IP to MAC, MAC to IP, proxy ARP, gratuitous ARP",
        ],
        [
            "4.6 Packet Delivery and Forwarding",
            "Direct/indirect delivery, forwarding table, routing",
        ],
        [
            "4.7 Unicast Routing Protocols",
            "RIP (distance vector), OSPF (link state), BGP (path vector)",
        ],
        ["4.8 Multicast Routing Protocols", "IGMP, DVMRP, PIM, multicast addresses"],
        [
            "4.9 Routing Algorithms",
            "Least cost, Dijkstra SPF (full worked example), Bellman-Ford",
        ],
        [
            "4.10 Congestion Control",
            "Causes, effects, open and closed loop algorithms, RED, TCP CC",
        ],
        [
            "4.11 Internetworking Devices",
            "Repeater, hub, bridge, switch, router, gateway -- comparison",
        ],
        [
            "4.12 IPv4 -- Internet Protocol",
            "IPv4 header format, fragmentation, TTL, checksum",
        ],
        [
            "4.13 IPv6 -- Next Generation IP",
            "Motivation, 128-bit addresses, header format, migration",
        ],
        ["4.14 Quick Revision Summary", "Key formulas, tables, and exam flashcards"],
    ],
)
br()


# =============================================================================
#  UNIT IV DIVIDER
# =============================================================================
part_box("UNIT IV -- THE NETWORK LAYER")


# -----------------------------------------------------------------------------
#  4.1  NETWORK LAYER OVERVIEW
# -----------------------------------------------------------------------------
chap_box("4.1  Network Layer -- Overview and Services")
section("Role of the Network Layer")
definition(
    "<b>Network Layer (Layer 3 of OSI):</b> Responsible for <b>host-to-host (end-to-end "
    "logical) delivery</b> of packets across multiple interconnected networks. While the "
    "Data Link layer handles delivery on a single link, the Network layer handles "
    "delivery across an internetwork -- a collection of networks connected by routers."
)
bullet(
    [
        "Provides <b>logical addressing</b> (IP addresses) to uniquely identify every host globally.",
        "Performs <b>routing</b>: determines the best path for a packet from source to destination.",
        "Performs <b>packet forwarding</b>: moves each packet from an input link to the correct output link at each router.",
        "Handles <b>fragmentation and reassembly</b>: splits large packets for smaller-MTU links.",
        "Provides <b>connectionless (datagram)</b> service in the Internet (IP is best-effort).",
    ]
)

section("Network Layer Services")
info_table(
    ["Service", "Description", "Example"],
    [
        [
            "Logical Addressing",
            "Globally unique addresses that identify source and destination across networks.",
            "IPv4 (32-bit), IPv6 (128-bit)",
        ],
        [
            "Routing",
            "Selection of the best path through the internetwork using routing algorithms.",
            "RIP, OSPF, BGP",
        ],
        [
            "Forwarding",
            "Moving packets from input interface to output interface at each router.",
            "Router forwarding table lookup",
        ],
        [
            "Fragmentation",
            "Splitting packets too large for a link's MTU. Reassembled at destination.",
            "IPv4 fragmentation; IPv6 uses Path MTU Discovery",
        ],
        [
            "Error Reporting",
            "Reporting errors and diagnostic information back to the source.",
            "ICMP (ping, traceroute)",
        ],
        [
            "Address Resolution",
            "Mapping logical IP addresses to physical MAC addresses.",
            "ARP (IP to MAC), RARP (MAC to IP)",
        ],
    ],
)
tip(
    "Network Layer = host-to-host delivery across multiple networks. "
    "Data Link Layer = node-to-node delivery on ONE link. "
    "Transport Layer = process-to-process delivery (end-to-end). "
    "These boundaries are a guaranteed exam question."
)
br()


# -----------------------------------------------------------------------------
#  4.2  LOGICAL ADDRESSING -- IPv4
# -----------------------------------------------------------------------------
chap_box("4.2  Logical Addressing -- IPv4 Address Structure")
section("IPv4 Address Basics")
definition(
    "<b>IPv4 Address:</b> A 32-bit binary number used to uniquely identify a network "
    "interface on an IP network. Written in <b>dotted-decimal notation</b>: four groups "
    "of 8 bits (octets), each expressed as a decimal number from 0 to 255, separated "
    "by dots. Example: 192.168.10.5"
)
bullet(
    [
        "32 bits = 4 bytes = 4 octets.",
        "Total address space: 2<super>32</super> = 4,294,967,296 (approximately 4.3 billion) unique addresses.",
        "Each octet ranges from 0 (00000000) to 255 (11111111).",
        "An IP address consists of two parts: <b>Network ID</b> (identifies the network) and <b>Host ID</b> (identifies the device within that network).",
        "The boundary between Network ID and Host ID is determined by the <b>subnet mask</b>.",
    ]
)
code_block("""
 IPv4 ADDRESS STRUCTURE:
 =====================================================================
 Example: 192.168.10.5

 In binary:
   192 = 1100 0000
   168 = 1010 1000
    10 = 0000 1010
     5 = 0000 0101

 Full 32-bit binary: 11000000.10101000.00001010.00000101

 With Class C subnet mask 255.255.255.0  (= /24 in CIDR):
   11111111.11111111.11111111.00000000  <- subnet mask
   11000000.10101000.00001010.00000101  <- IP address
   ------------------------------------ AND operation
   11000000.10101000.00001010.00000000  <- Network address = 192.168.10.0
                                 ^^^^^
                              Host ID = 5

 SPECIAL ADDRESSES in any subnet:
   Network address:   all host bits = 0  (e.g., 192.168.10.0)
   Broadcast address: all host bits = 1  (e.g., 192.168.10.255)
   Usable host range: 192.168.10.1 to 192.168.10.254  (254 hosts)
""")
sp(6)
br()


# -----------------------------------------------------------------------------
#  4.3  CLASSFUL ADDRESSING
# -----------------------------------------------------------------------------
chap_box("4.3  Classful Addressing")
section("Overview")
definition(
    "<b>Classful Addressing:</b> The original IPv4 addressing scheme (1981-1993) in which "
    "the 32-bit IP address space is divided into five fixed classes (A, B, C, D, E) "
    "based on the leading bits of the address. The class automatically determines the "
    "number of network bits and host bits -- no explicit subnet mask was needed."
)

section("The Five Classes")
code_block("""
 CLASSFUL IPv4 ADDRESS RANGES:
 =====================================================================
 CLASS A:   0xxxxxxx . -------- . -------- . --------
            First bit = 0.  Network bits: 8.  Host bits: 24.
            Range: 0.0.0.0  to  127.255.255.255
            Default mask: 255.0.0.0  (/8)
            Networks: 2^7 = 128    Hosts per network: 2^24 - 2 = 16,777,214

 CLASS B:   10xxxxxx . xxxxxxxx . -------- . --------
            First 2 bits = 10.  Network bits: 16.  Host bits: 16.
            Range: 128.0.0.0  to  191.255.255.255
            Default mask: 255.255.0.0  (/16)
            Networks: 2^14 = 16,384    Hosts per network: 2^16 - 2 = 65,534

 CLASS C:   110xxxxx . xxxxxxxx . xxxxxxxx . --------
            First 3 bits = 110.  Network bits: 24.  Host bits: 8.
            Range: 192.0.0.0  to  223.255.255.255
            Default mask: 255.255.255.0  (/24)
            Networks: 2^21 = 2,097,152    Hosts per network: 2^8 - 2 = 254

 CLASS D:   1110xxxx . xxxxxxxx . xxxxxxxx . xxxxxxxx
            First 4 bits = 1110.  No network/host split.
            Range: 224.0.0.0  to  239.255.255.255
            Purpose: MULTICAST groups. Assigned by IANA.

 CLASS E:   11110xxx . xxxxxxxx . xxxxxxxx . xxxxxxxx
            First 5 bits = 11110.
            Range: 240.0.0.0  to  255.255.255.255
            Purpose: Reserved / Experimental. Not used in the Internet.

 NOTE: 127.x.x.x is reserved for loopback testing (127.0.0.1 = localhost).
       0.x.x.x is reserved for "this network" (used in routing tables).
""")

info_table(
    [
        "Class",
        "First Bits",
        "Net Bits",
        "Host Bits",
        "Range",
        "Default Mask",
        "Max Hosts",
        "Purpose",
    ],
    [
        [
            "A",
            "0",
            "8",
            "24",
            "0.0.0.0 - 127.255.255.255",
            "255.0.0.0 (/8)",
            "16,777,214",
            "Large organisations, ISPs",
        ],
        [
            "B",
            "10",
            "16",
            "16",
            "128.0.0.0 - 191.255.255.255",
            "255.255.0.0 (/16)",
            "65,534",
            "Medium organisations",
        ],
        [
            "C",
            "110",
            "24",
            "8",
            "192.0.0.0 - 223.255.255.255",
            "255.255.255.0 (/24)",
            "254",
            "Small networks, offices",
        ],
        [
            "D",
            "1110",
            "-",
            "-",
            "224.0.0.0 - 239.255.255.255",
            "N/A",
            "N/A",
            "Multicast groups",
        ],
        [
            "E",
            "11110",
            "-",
            "-",
            "240.0.0.0 - 255.255.255.255",
            "N/A",
            "N/A",
            "Reserved/Experimental",
        ],
    ],
)

# Classful Address Division Diagrams (Class A, B, and C)
packet_format(
    "Classful Address Formats (Class A, B, and C)",
    [
        ("0", 1), ("Net ID", 7), ("Host ID", 24),
        ("10", 2), ("Net ID", 14), ("Host ID", 16),
        ("110", 3), ("Net ID", 21), ("Host ID", 8),
    ],
    bit_ruler=True,
)

section("Limitations of Classful Addressing")
bullet(
    [
        "<b>Address Waste:</b> A company needing 300 hosts must get a Class B block (65,534 hosts), wasting 65,000+ addresses.",
        "<b>Inflexibility:</b> Only three usable sizes (A, B, C). No way to get a block of exactly 500 addresses.",
        "<b>Exhaustion:</b> The 4.3 billion address space was being consumed rapidly by the mid-1990s.",
        "<b>Large Routing Tables:</b> Each classful network required a separate routing table entry.",
        "Solution: CIDR (Classless Inter-Domain Routing) introduced in 1993 to replace classful addressing.",
    ]
)
tip(
    "Hosts per network = 2^(host bits) - 2. Subtract 2 for: network address (all zeros) and broadcast (all ones). "
    "Class A: 3 octets for hosts. Class B: 2 octets. Class C: 1 octet. "
    "First octet determines class: 1-126 = A, 128-191 = B, 192-223 = C, 224-239 = D, 240-255 = E."
)
br()


# -----------------------------------------------------------------------------
#  4.4  CLASSLESS ADDRESSING (CIDR)
# -----------------------------------------------------------------------------
chap_box("4.4  Classless Addressing -- CIDR, Subnetting, and Supernetting")
section("CIDR -- Classless Inter-Domain Routing")
definition(
    "<b>CIDR (Classless Inter-Domain Routing):</b> An IPv4 addressing scheme introduced "
    "in 1993 (RFC 1519) that eliminates the rigid class boundaries of classful addressing. "
    "CIDR uses a <b>prefix length</b> (written as /n after the IP address) to specify "
    "exactly how many bits are the network part. This allows any block size that is a "
    "power of 2, not just the classful sizes of /8, /16, or /24."
)
body(
    "<b>CIDR Notation:</b> IP address / prefix length. Example: 192.168.5.0/26 means "
    "the first 26 bits are the network part and the last 6 bits are the host part."
)
code_block("""
 CIDR NOTATION AND BLOCK SIZE:
 =====================================================================
 /n notation means: first n bits = network, last (32-n) bits = host.

 Block size (number of addresses) = 2^(32 - n)
 Usable hosts = 2^(32 - n) - 2

 Common CIDR blocks:
 /24 -> 2^8  = 256 addresses, 254 usable hosts    (equiv. Class C)
 /25 -> 2^7  = 128 addresses,  126 usable hosts
 /26 -> 2^6  =  64 addresses,   62 usable hosts
 /27 -> 2^5  =  32 addresses,   30 usable hosts
 /28 -> 2^4  =  16 addresses,   14 usable hosts
 /29 -> 2^3  =   8 addresses,    6 usable hosts
 /30 -> 2^2  =   4 addresses,    2 usable hosts   (point-to-point links)
 /32 -> 1 address (single host route, loopback)

 EXAMPLE: 10.4.8.0/22
   Prefix = 22 bits, Host = 10 bits
   Block size = 2^10 = 1024 addresses
   Network address:   10.4.8.0
   Broadcast:         10.4.11.255  (10.4.8.0 + 1023)
   Usable range:      10.4.8.1 to 10.4.11.254
   Subnet mask:       255.255.252.0
""")

section("Subnetting")
definition(
    "<b>Subnetting:</b> Dividing a single large network block into multiple smaller "
    "subnetworks (subnets) by extending the prefix length (borrowing bits from the "
    "host part). Subnetting improves network management, reduces broadcast domains, "
    "and allows better utilization of address space."
)

# Subnetting Address Formats Comparison (Original Class C vs. Subnetted)
packet_format(
    "Subnetting Format Comparison (Original Class C vs. Subnetted)",
    [
        ("Original Class C", 24), ("Host ID", 8),
        ("Subnetted (/26)", 24), ("Sub", 2), ("Host ID", 6),
    ],
    bit_ruler=True,
)
code_block("""
 SUBNETTING EXAMPLE:
 =====================================================================
 Given network: 192.168.10.0/24  (254 usable hosts)
 Requirement:   4 subnets, each with at least 50 hosts

 Step 1: How many host bits needed for 50 hosts?
         2^n >= 50+2 = 52  =>  n=6 (2^6=64, enough for 62 hosts)

 Step 2: New prefix length = 32 - 6 = /26
         This gives: 2^(26-24) = 2^2 = 4 subnets

 Step 3: Subnet details:
         Subnet 1: 192.168.10.0/26    Hosts: .1 to .62    BC: .63
         Subnet 2: 192.168.10.64/26   Hosts: .65 to .126  BC: .127
         Subnet 3: 192.168.10.128/26  Hosts: .129 to .190 BC: .191
         Subnet 4: 192.168.10.192/26  Hosts: .193 to .254 BC: .255

 Subnet mask for /26: 255.255.255.192
   Binary: 11111111.11111111.11111111.11000000
   (6 host bits means 2 borrowed bits -> 192 = 11000000 in 4th octet)

 FORMULA SUMMARY:
   Number of subnets  = 2^(borrowed bits)
   Hosts per subnet   = 2^(remaining host bits) - 2
   Block size         = 2^(remaining host bits)
""")

section("VLSM -- Variable Length Subnet Masking")
definition(
    "<b>VLSM:</b> An extension of subnetting where different subnets of the same network "
    "can have different prefix lengths (different sizes). This allows efficient allocation -- "
    "large subnets for large segments and small subnets for small segments or point-to-point links."
)
code_block("""
 VLSM EXAMPLE:
 =====================================================================
 Allocated block: 192.168.1.0/24
 Requirements:
   Dept A: 100 hosts -> needs /25 (126 hosts)
   Dept B:  50 hosts -> needs /26 (62 hosts)
   Dept C:  25 hosts -> needs /27 (30 hosts)
   WAN link: 2 hosts -> needs /30 (2 hosts)

 Allocation:
   Dept A: 192.168.1.0/25   (.1 to .126)    <- 128 addresses
   Dept B: 192.168.1.128/26 (.129 to .190)  <- 64 addresses
   Dept C: 192.168.1.192/27 (.193 to .222)  <- 32 addresses
   WAN:    192.168.1.224/30 (.225 to .226)  <- 4 addresses
   Unused: 192.168.1.228/30 onwards         <- 28 addresses remain
""")

# VLSM Binary Splitting Trie Diagram
vlsm_fc = ed.Flowchart(
    width=540, 
    height=220, 
    caption="Fig 9: VLSM Address Space Binary Splitting Tree (Trie)",
)
vlsm_fc.process("root", "192.168.1.0/24\n(256 Hosts)", x=260, y=190)
vlsm_fc.process("left1", "192.168.1.0/25\nDept A (128 Hosts)", x=130, y=130)
vlsm_fc.process("right1", "192.168.1.128/25\n(Remaining 128)", x=390, y=130)
vlsm_fc.process("left2", "192.168.1.128/26\nDept B (64 Hosts)", x=310, y=70)
vlsm_fc.process("right2", "192.168.1.192/26\n(Remaining 64)", x=470, y=70)
vlsm_fc.process("left3", "192.168.1.192/27\nDept C (32 Hosts)", x=430, y=15)
vlsm_fc.process("right3", "192.168.1.224/27\n(WAN & Unused)", x=530, y=15)

vlsm_fc.edge("root", "left1", label="0")
vlsm_fc.edge("root", "right1", label="1")
vlsm_fc.edge("right1", "left2", label="0")
vlsm_fc.edge("right1", "right2", label="1")
vlsm_fc.edge("right2", "left3", label="0")
vlsm_fc.edge("right2", "right3", label="1")
story.extend(vlsm_fc.as_flowable())
br()

section("Supernetting (Route Aggregation)")
definition(
    "<b>Supernetting:</b> The opposite of subnetting. Multiple contiguous network blocks "
    "are combined into a single larger block by reducing the prefix length. Used by ISPs "
    "and backbone routers to reduce the size of routing tables (route aggregation / "
    "route summarization)."
)
code_block("""
 SUPERNETTING EXAMPLE:
 =====================================================================
 Four Class C networks to aggregate:
   200.1.0.0/24
   200.1.1.0/24
   200.1.2.0/24
   200.1.3.0/24

 In binary (third octet):
   00000000 = 0
   00000001 = 1
   00000010 = 2
   00000011 = 3
 Common prefix: 000000-- (first 6 bits of 3rd octet are common)

 Combined: 200.1.0.0/22  (prefix shortened from /24 to /22)
   This single route covers all four /24 networks.
   Block size = 2^10 = 1024 addresses
   Range: 200.1.0.0 to 200.1.3.255
""")
tip(
    "Subnetting: longer prefix (e.g., /24 to /26) = smaller subnets. "
    "Supernetting: shorter prefix (e.g., /24 to /22) = larger aggregate. "
    "VLSM = different subnet sizes within the same parent block. "
    "CIDR block size = 2^(32-prefix). Hosts = block size - 2."
)


# -----------------------------------------------------------------------------
#  4.5  ADDRESS MAPPING -- ARP AND RARP
# -----------------------------------------------------------------------------
chap_box("4.5  Address Mapping -- ARP and RARP")
section("Why Address Mapping?")
body(
    "A router or host knows the <b>IP address</b> (logical address, Layer 3) of the "
    "destination but needs the <b>MAC address</b> (physical address, Layer 2) to "
    "construct a frame for transmission on the local link. Address mapping bridges "
    "this gap between logical and physical addressing."
)

section("ARP -- Address Resolution Protocol (RFC 826)")
definition(
    "<b>ARP:</b> A protocol that maps a known IPv4 address to an unknown MAC address "
    "on the same local network. ARP broadcasts a request to all devices; only the "
    "device with the matching IP replies with its MAC address."
)
subsection("ARP Cache")
body(
    "Every device maintains an <b>ARP cache</b> (ARP table) -- a temporary mapping "
    "of IP addresses to MAC addresses. Entries expire after a few minutes "
    "(typically 2-20 minutes). The cache avoids broadcasting for every packet."
)
subsection("ARP Packet Format")
packet_format(
    "ARP Packet Format (32-bit aligned grid)",
    [
        ("Hardware Type", 16),
        ("Protocol Type", 16),
        ("Hardware Len (HLen)", 8),
        ("Protocol Len (PLen)", 8),
        ("Operation", 16),
        ("Sender MAC (Octets 0-3)", 32),
        ("Sender MAC (Octets 4-5)", 16),
        ("Sender IP (Octets 0-1)", 16),
        ("Sender IP (Octets 2-3)", 16),
        ("Target MAC (Octets 0-1)", 16),
        ("Target MAC (Octets 2-5)", 32),
        ("Target IP (Octets 0-3)", 32),
    ],
)
code_block("""
 ARP PACKET FIELDS:
 =====================================================================
 Hardware Type:  1 = Ethernet (IEEE 802 networks)
 Protocol Type:  0x0800 = IPv4
 HLen:           Hardware address length = 6 (MAC address = 6 bytes)
 PLen:           Protocol address length = 4 (IPv4 = 4 bytes)
 Operation:      1 = ARP Request  |  2 = ARP Reply
                 3 = RARP Request |  4 = RARP Reply

  ARP REQUEST (broadcast):
    Sender MAC = sender's own MAC
    Sender IP  = sender's own IP
    Target MAC = 00:00:00:00:00:00 (UNKNOWN -- what we're asking for)
    Target IP  = IP we want to resolve

  ARP REPLY (unicast back to requester):
    Sender MAC = RESPONDER's MAC (this is the answer!)
    Sender IP  = RESPONDER's IP
    Target MAC = REQUESTER's MAC
    Target IP  = REQUESTER's IP
""")

# ARP sequence diagram
seq_arp = ed.SequenceDiagram(
    width=CW,
    height=250,
    caption="Fig 1: ARP Operation -- broadcast request, unicast reply, cache update",
)
seq_arp.actor("a", "Host A")
seq_arp.actor("sw", "LAN Segment")
seq_arp.actor("b", "Host B")
seq_arp.actor("c", "Other Host")
seq_arp.message(
    "a", "sw", "ARP Request (broadcast): Who has 192.168.1.5?", arrow="solid"
)
seq_arp.message("sw", "b", "ARP Request (forwarded)", arrow="solid")
seq_arp.message("sw", "c", "ARP Request (forwarded -- ignored)", arrow="solid")
seq_arp.message(
    "b", "a", "ARP Reply (unicast): 192.168.1.5 is at AA:BB:CC:DD:EE:FF", arrow="dashed"
)
seq_arp.divider("Host A updates ARP cache. Sends IP packet directly to B's MAC.")
story.extend(seq_arp.as_flowable())

section("Proxy ARP and Gratuitous ARP")
subsection("Proxy ARP")
body(
    "A router responds to ARP requests on behalf of hosts in another subnet. "
    "Enables hosts without a default gateway to reach remote hosts -- the router "
    "replies with its own MAC address. Useful but can mask configuration errors."
)
subsection("Gratuitous ARP")
body(
    "A host broadcasts an ARP request for its own IP address at startup. Used to: "
    "(1) detect IP address conflicts -- if another host replies, there is a duplicate; "
    "(2) update ARP caches of all other devices after a MAC address change (NIC replacement)."
)

section("RARP -- Reverse ARP")
definition(
    "<b>RARP:</b> A host that knows only its own MAC address broadcasts a RARP request "
    "to find its IP address. A RARP server on the network replies with the assigned IP. "
    "Used by diskless workstations during boot. Replaced by BOOTP and then DHCP."
)
info_table(
    ["Protocol", "Maps", "Direction", "Method", "Status"],
    [
        [
            "ARP",
            "IP -> MAC",
            "Layer 3 to L2",
            "Broadcast request, unicast reply",
            "Active in all IPv4 networks",
        ],
        [
            "RARP",
            "MAC -> IP",
            "L2 to Layer 3",
            "Broadcast request, server reply",
            "Obsolete -- replaced by DHCP",
        ],
        [
            "DHCP",
            "Nothing -> full config",
            "None to L3",
            "Discover/Offer/Request/ACK",
            "Current standard",
        ],
        [
            "IPv6 NDP",
            "IP -> MAC (L2)",
            "L3 to L2",
            "Multicast (replaces ARP in IPv6)",
            "Used in IPv6",
        ],
    ],
)
tip(
    "ARP = IP address known, need MAC. Works only within the same subnet. "
    "To reach another subnet, the frame goes to the default gateway's MAC; the IP stays the same. "
    "ARP cache reduces broadcasts. RARP is obsolete -- replaced by DHCP."
)
br()


# -----------------------------------------------------------------------------
#  4.6  PACKET DELIVERY AND FORWARDING
# -----------------------------------------------------------------------------
chap_box("4.6  Packet Delivery and Forwarding")
section("Types of Delivery")
definition(
    "<b>Direct Delivery:</b> The destination host is on the same network (same subnet) "
    "as the sender. The sender can deliver the packet directly by resolving the "
    "destination's MAC address using ARP and creating a frame addressed to that MAC."
)
definition(
    "<b>Indirect Delivery:</b> The destination host is on a different network. "
    "The sender cannot reach it directly. The packet is sent to the <b>default "
    "gateway</b> (a router), which forwards it hop-by-hop toward the destination. "
    "The IP addresses (source and destination) remain unchanged; only the MAC "
    "addresses change at each hop."
)
code_block("""
 DIRECT vs INDIRECT DELIVERY:
 =====================================================================
 Sender: 192.168.1.10/24    Default GW: 192.168.1.1

 Case 1 -- DIRECT DELIVERY:
   Destination: 192.168.1.50 (same /24 subnet)
   192.168.1.10 AND 255.255.255.0 = 192.168.1.0  (sender's network)
   192.168.1.50 AND 255.255.255.0 = 192.168.1.0  (dest's network -- SAME)
   -> Direct delivery: ARP for 192.168.1.50's MAC, send frame directly.

 Case 2 -- INDIRECT DELIVERY:
   Destination: 10.0.0.5 (different network)
   10.0.0.5 AND 255.255.255.0 = 10.0.0.0  (DIFFERENT from 192.168.1.0)
   -> Indirect delivery:
      ARP for the Default Gateway (192.168.1.1) MAC
      Send frame to GW's MAC with IP dst = 10.0.0.5
      Router changes the frame (new src MAC, new dst MAC) at each hop
      IP addresses (192.168.1.10 -> 10.0.0.5) NEVER CHANGE end-to-end
""")

section("Router Forwarding Table")
body(
    "Each router maintains a <b>forwarding table</b> (also called a routing table). "
    "When a packet arrives, the router extracts the destination IP address, performs "
    "a <b>longest prefix match</b> against its forwarding table, and sends the packet "
    "out the matching interface."
)
code_block("""
 SAMPLE FORWARDING TABLE:
 =====================================================================
 Destination Network | Mask            | Next Hop      | Interface
 --------------------|-----------------|---------------|----------
 192.168.1.0         | 255.255.255.0   | Directly conn.| eth0
 10.0.0.0            | 255.0.0.0       | 192.168.1.1   | eth0
 172.16.0.0          | 255.255.0.0     | 192.168.1.2   | eth0
 0.0.0.0             | 0.0.0.0         | 192.168.1.1   | eth0  <- default route

 LONGEST PREFIX MATCH: When multiple entries match a destination,
 the entry with the LONGEST (most specific) prefix is chosen.
 Example: Destination = 10.5.3.1
   Matches 10.0.0.0/8 (8 bits)
   Matches 0.0.0.0/0  (0 bits -- default)
   -> Use 10.0.0.0/8 (longer match wins)
""")

# Packet forwarding network diagram -- dynamic layout, short labels
fwd_net = ed.NetworkDiagram(
    width=CW,
    height=200,
    caption="Fig 2: Packet forwarding across three hops -- IP addresses constant, MACs change at each router",
)
fwd_net.node("src", "Host A\n192.168.1.10", kind="host")
fwd_net.node("r1", "Router A\n192.168.1.1", kind="router")
fwd_net.node("r2", "Router B\n10.0.0.1", kind="router")
fwd_net.node("dst", "Host B\n10.0.0.50", kind="host")
fwd_net.link("src", "r1", label="Frame: A→R1_MAC | IP: same")
fwd_net.link("r1", "r2", label="Frame: R1→R2_MAC | IP: same")
fwd_net.link("r2", "dst", label="Frame: R2→B_MAC | IP: same")
story.extend(fwd_net.as_flowable())
tip(
    "IP addresses (src/dst) never change end-to-end. MAC addresses change at EVERY hop. "
    "Routers use longest prefix match in the forwarding table. Default route = 0.0.0.0/0."
)

section("Forwarding Decision Process")
body(
    "The following decision flow connects the concepts of direct delivery, ARP, "
    "longest prefix match, next-hop forwarding, and ICMP error reporting."
)
route_fc = ed.Flowchart(
    width=560,
    height=385,
    caption="Fig 3: Router forwarding decision -- local delivery, routed delivery, or error",
)
route_fc.terminal("receive", "Receive IP packet", x=280, y=360)
route_fc.process("inspect", "Extract destination IP address", x=280, y=310)
route_fc.decision("local", "Destination on a directly connected subnet?", x=280, y=248)
route_fc.process("arp_dest", "Resolve destination MAC using ARP", x=105, y=174)
route_fc.io_box("send_local", "Transmit directly on local LAN", x=105, y=96)
route_fc.process("lookup", "Run longest prefix match", x=438, y=174)
route_fc.decision("match", "Matching route found?", x=438, y=112)
route_fc.io_box("forward", "Forward to next-hop MAC", x=316, y=38)
route_fc.process("unreachable", "Send ICMP unreachable", x=505, y=38)
route_fc.edge("receive", "inspect")
route_fc.edge("inspect", "local")
route_fc.edge("local", "arp_dest", branch="yes")
route_fc.edge("arp_dest", "send_local")
route_fc.edge("local", "lookup", branch="no")
route_fc.edge("lookup", "match")
route_fc.edge("match", "forward", branch="yes")
route_fc.edge("match", "unreachable", branch="no")
story.extend(route_fc.as_flowable())
br()


# -----------------------------------------------------------------------------
#  4.7  UNICAST ROUTING PROTOCOLS
# -----------------------------------------------------------------------------
chap_box("4.7  Unicast Routing Protocols")
section("Overview")
definition(
    "<b>Routing Protocols:</b> Protocols that allow routers to <b>automatically</b> "
    "build and maintain their forwarding tables by exchanging routing information "
    "with other routers. They adapt to topology changes (link failures, new links) "
    "without manual intervention."
)
info_table(
    ["Category", "Protocol", "Algorithm", "Scope", "Metric"],
    [
        [
            "IGP (Interior)",
            "RIP",
            "Distance Vector",
            "Within one AS",
            "Hop count (max 15)",
        ],
        [
            "IGP (Interior)",
            "OSPF",
            "Link State (SPF)",
            "Within one AS",
            "Cost (100Mbps/link BW)",
        ],
        [
            "IGP (Interior)",
            "EIGRP",
            "Advanced DV (Cisco)",
            "Within one AS",
            "Bandwidth + delay (composite)",
        ],
        [
            "EGP (Exterior)",
            "BGP",
            "Path Vector",
            "Between ASes",
            "Policy-based AS path",
        ],
    ],
)
body(
    "An <b>Autonomous System (AS)</b> is a group of networks under a single administrative "
    "authority (e.g., a company, university, or ISP). Interior Gateway Protocols (IGPs) "
    "operate within an AS; Exterior Gateway Protocols (EGPs) operate between ASes."
)

section("RIP -- Routing Information Protocol")
definition(
    "<b>RIP (RFC 1058 / RFC 2453):</b> A distance-vector IGP where each router "
    "broadcasts its entire routing table to its directly connected neighbors every "
    "30 seconds. Routers use the Bellman-Ford algorithm to compute shortest paths. "
    "The metric is <b>hop count</b> -- the number of routers traversed."
)
bullet(
    [
        "<b>Maximum hop count: 15.</b> A hop count of 16 = infinity (unreachable). Limits RIP networks to 15 hops diameter.",
        "Sends complete routing table updates every <b>30 seconds</b> (convergence can be slow).",
        "<b>Count-to-infinity problem:</b> When a link fails, routers may slowly count up to 16 before declaring the route unreachable.",
        "<b>Split horizon:</b> A router does not advertise a route back on the interface it learned it from (prevents loops).",
        "<b>Poison reverse:</b> Advertise failed routes with metric 16 (infinity) to speed up convergence.",
        "RIPv1: classful (no subnet mask in updates). RIPv2: classless (includes subnet mask, supports VLSM and CIDR).",
        "<b>Best for:</b> Small, simple networks. Not suitable for large enterprise or ISP networks.",
    ]
)

section("OSPF -- Open Shortest Path First")
definition(
    "<b>OSPF (RFC 2328 / RFC 5340):</b> A link-state IGP where each router builds a "
    "complete map of the network topology (LSDB -- Link State Database) by flooding "
    "LSAs (Link State Advertisements) to all routers in the area. Each router then "
    "independently runs <b>Dijkstra's SPF algorithm</b> to compute shortest paths."
)
bullet(
    [
        "Fast convergence: LSAs flooded immediately when topology changes.",
        "Hierarchical design: backbone Area 0 connects all other areas.",
        "Metric: <b>cost</b> = 100 Mbps / link bandwidth. Lower cost = better path.",
        "No hop count limit (scales to very large networks).",
        "Classless: supports VLSM and CIDR.",
        "5 packet types: Hello, DBD, LSR, LSU, LSAck.",
        "Elects DR and BDR on multi-access networks to reduce flooding.",
        "<b>Best for:</b> Large enterprise networks, ISP interior routing.",
    ]
)

section("BGP -- Border Gateway Protocol")
definition(
    "<b>BGP (RFC 4271):</b> The only EGP in use today -- the routing protocol of the "
    "Internet. BGP is a <b>path-vector</b> protocol. Instead of advertising a metric, "
    "BGP advertises the full <b>AS path</b> (list of autonomous systems) to reach a "
    "destination. This allows routing policies (e.g., prefer certain ASes, avoid others)."
)
bullet(
    [
        "Operates over TCP port 179 (reliable, connection-oriented).",
        "Uses incremental updates (only changes, not full table) after initial exchange.",
        "AS path prevents routing loops (a router rejects a route containing its own AS number).",
        "<b>iBGP:</b> BGP between routers within the same AS. <b>eBGP:</b> BGP between different ASes.",
        "Policy-based: administrators control which routes are accepted, preferred, and advertised.",
        "<b>Best for:</b> Internet backbone, inter-AS routing between ISPs.",
    ]
)

info_table(
    ["Feature", "RIP", "OSPF", "BGP"],
    [
        [
            "Algorithm",
            "Bellman-Ford (Distance Vector)",
            "Dijkstra (Link State)",
            "Path Vector",
        ],
        [
            "Metric",
            "Hop count (max 15)",
            "Cost = 100Mbps / BW",
            "Policy (AS path, attributes)",
        ],
        [
            "Updates",
            "Full table every 30 seconds",
            "Incremental LSA flooding",
            "Incremental path updates",
        ],
        [
            "Convergence",
            "Slow (30-180 seconds)",
            "Fast (seconds)",
            "Slow (BGP designed for stability)",
        ],
        [
            "Scope",
            "IGP (small networks)",
            "IGP (large networks)",
            "EGP (Internet backbone)",
        ],
        [
            "Scalability",
            "Max 15 hops -- small only",
            "Hierarchical areas -- scales well",
            "Manages 900,000+ Internet routes",
        ],
        ["Protocol", "UDP port 520", "IP protocol 89 (no TCP/UDP)", "TCP port 179"],
        ["Admin distance", "120", "110", "20 (eBGP), 200 (iBGP)"],
    ],
)
tip(
    "RIP = hop count, max 15, every 30 sec, small networks. "
    "OSPF = cost, Dijkstra, link state, large networks, Area 0 backbone. "
    "BGP = AS path, policy-based, Internet routing. "
    "Admin distance: lower = more preferred. Direct=0, Static=1, OSPF=110, RIP=120."
)
br()


# -----------------------------------------------------------------------------
#  4.8  MULTICAST ROUTING PROTOCOLS
# -----------------------------------------------------------------------------
chap_box("4.8  Multicast Routing Protocols")
section("Multicast Overview")
definition(
    "<b>Multicast:</b> A transmission mode where a single packet is delivered to a "
    "<b>group</b> of interested receivers simultaneously. More efficient than unicast "
    "(one copy per receiver) and more controlled than broadcast (delivered to all). "
    "Used for: video streaming, IPTV, video conferencing, software distribution."
)
bullet(
    [
        "Multicast IP addresses: Class D range <b>224.0.0.0 to 239.255.255.255</b>.",
        "Receivers join a multicast group using IGMP (Internet Group Management Protocol).",
        "Routers build a multicast distribution tree to deliver packets efficiently.",
        "Well-known multicast addresses: 224.0.0.1 (all hosts), 224.0.0.2 (all routers), 224.0.0.5 (all OSPF routers).",
    ]
)

section("IGMP -- Internet Group Management Protocol")
definition(
    "<b>IGMP:</b> A protocol between a host and its directly connected router. "
    "Hosts use IGMP to <b>join</b> and <b>leave</b> multicast groups. Routers use "
    "IGMP to track which multicast groups have active members on each interface."
)
bullet(
    [
        "IGMP v1: Hosts send Join messages; router polls periodically.",
        "IGMP v2: Adds explicit Leave messages for faster group departure.",
        "IGMP v3: Allows hosts to specify which source addresses they want to receive from (Source-Specific Multicast).",
    ]
)

section("Multicast Routing Protocols")
info_table(
    ["Protocol", "Full Name", "Approach", "Notes"],
    [
        [
            "DVMRP",
            "Distance Vector Multicast Routing Protocol",
            "Dense mode -- flood and prune",
            "Floods multicast to all routers; prunes branches with no receivers. Legacy.",
        ],
        [
            "PIM-DM",
            "Protocol Independent Multicast -- Dense Mode",
            "Dense -- flood and prune",
            "Protocol-independent (works with any unicast routing). For dense receiver groups.",
        ],
        [
            "PIM-SM",
            "Protocol Independent Multicast -- Sparse Mode",
            "Sparse -- explicit join",
            "Receivers must explicitly join. Uses Rendezvous Point (RP). Most common today.",
        ],
        [
            "MOSPF",
            "Multicast Open Shortest Path First",
            "Link-state extension of OSPF",
            "Adds multicast to OSPF. Not widely deployed.",
        ],
        [
            "CBT",
            "Core Based Trees",
            "Shared tree from core node",
            "Single shared tree rooted at a core router. Low overhead. Rarely used.",
        ],
    ],
)
tip(
    "Multicast = Class D addresses (224.0.0.0 to 239.255.255.255). "
    "IGMP = host tells router it wants multicast group. "
    "PIM-SM = most common multicast routing protocol. "
    "Rendezvous Point (RP) is the meeting point for sources and receivers in PIM-SM."
)
br()


# -----------------------------------------------------------------------------
#  4.9  ROUTING ALGORITHMS
# -----------------------------------------------------------------------------
chap_box("4.9  Routing Algorithms -- Least Cost, Dijkstra, Bellman-Ford")
section("Least-Cost Routing")
definition(
    "<b>Least-Cost Routing:</b> Routing packets along the path that minimises "
    "some cost function. The cost may be measured in hop count, bandwidth, delay, "
    "reliability, or a composite metric. The network is modelled as a weighted "
    "directed graph where nodes are routers and edge weights are link costs."
)

section("Dijkstra's Shortest Path Algorithm")
definition(
    "<b>Dijkstra's Algorithm:</b> A greedy algorithm that finds the shortest (least-cost) "
    "paths from a single source node to ALL other nodes in a weighted graph with "
    "<b>non-negative</b> edge weights. Used by OSPF to build the Shortest Path Tree (SPT)."
)
subsection("Algorithm Steps")
bullet(
    [
        "<b>Initialize:</b> dist[source] = 0; dist[all others] = infinity. Mark all nodes unvisited.",
        "<b>Select:</b> Pick the unvisited node u with the smallest known distance.",
        "<b>Relax:</b> For each unvisited neighbour v of u: if dist[u] + cost(u,v) < dist[v], update dist[v].",
        "<b>Mark:</b> Mark u as visited (permanently settled). Never revisit u.",
        "<b>Repeat:</b> Go to step 2 until all nodes are visited.",
    ]
)
code_block("""
 DIJKSTRA'S ALGORITHM -- FULL WORKED EXAMPLE:
 =====================================================================
 GRAPH (undirected, weighted):
   Nodes: A, B, C, D, E, F
   Edges: A-B:2, A-C:4, B-C:1, B-D:5, C-E:3, D-E:1, D-F:4, E-F:2

   Adjacency:
     A: B(2), C(4)
     B: A(2), C(1), D(5)
     C: A(4), B(1), E(3)
     D: B(5), E(1), F(4)
     E: C(3), D(1), F(2)
     F: D(4), E(2)

 SOURCE: A

 INITIALIZATION:
   dist = {A:0, B:INF, C:INF, D:INF, E:INF, F:INF}
   prev = {all: None}
   Unvisited = {A, B, C, D, E, F}

 ITERATION 1 -- Visit A (dist=0, smallest unvisited):
   Neighbours: B(2), C(4)
   dist[B] = min(INF, 0+2) = 2  -> prev[B]=A
   dist[C] = min(INF, 0+4) = 4  -> prev[C]=A
   Mark A visited.
   dist = {A:0, B:2, C:4, D:INF, E:INF, F:INF}

 ITERATION 2 -- Visit B (dist=2, smallest unvisited):
   Neighbours: A(visited), C(1), D(5)
   dist[C] = min(4, 2+1) = 3    -> prev[C]=B  (UPDATED!)
   dist[D] = min(INF, 2+5) = 7  -> prev[D]=B
   Mark B visited.
   dist = {A:0, B:2, C:3, D:7, E:INF, F:INF}

 ITERATION 3 -- Visit C (dist=3, smallest unvisited):
   Neighbours: A(visited), B(visited), E(3)
   dist[E] = min(INF, 3+3) = 6  -> prev[E]=C
   Mark C visited.
   dist = {A:0, B:2, C:3, D:7, E:6, F:INF}

 ITERATION 4 -- Visit E (dist=6, smallest unvisited):
   Neighbours: C(visited), D(1), F(2)
   dist[D] = min(7, 6+1) = 7    -> (no change -- tie, keep B)
   dist[F] = min(INF, 6+2) = 8  -> prev[F]=E
   Mark E visited.
   dist = {A:0, B:2, C:3, D:7, E:6, F:8}

 ITERATION 5 -- Visit D (dist=7, smallest unvisited):
   Neighbours: B(visited), E(visited), F(4)
   dist[F] = min(8, 7+4) = 8    -> (no change)
   Mark D visited.

 ITERATION 6 -- Visit F (dist=8):
   All neighbours visited. Mark F visited. Done.

 FINAL SHORTEST DISTANCES FROM A:
   A -> A: 0   (trivial)
   A -> B: 2   path: A -> B
   A -> C: 3   path: A -> B -> C
   A -> D: 7   path: A -> B -> D
   A -> E: 6   path: A -> B -> C -> E
   A -> F: 8   path: A -> B -> C -> E -> F

 SHORTEST PATH TREE:
      A
      |2
      B
     /|
   3/ |5
   C  D
   |3 |1
   E  (already reached via C->E=6, D->E=7, so E's predecessor=C)
   |2
   F
""")

# Dijkstra state machine to show algorithm state
section("Dijkstra Iteration Summary Table")
info_table(
    [
        "Iter",
        "Visited Node",
        "dist[A]",
        "dist[B]",
        "dist[C]",
        "dist[D]",
        "dist[E]",
        "dist[F]",
    ],
    [
        ["Init", "-", "0", "INF", "INF", "INF", "INF", "INF"],
        ["1", "A", "0", "2", "4", "INF", "INF", "INF"],
        ["2", "B", "0", "2", "3", "7", "INF", "INF"],
        ["3", "C", "0", "2", "3", "7", "6", "INF"],
        ["4", "E", "0", "2", "3", "7", "6", "8"],
        ["5", "D", "0", "2", "3", "7", "6", "8"],
        ["6", "F", "0", "2", "3", "7", "6", "8"],
    ],
)

# Dijkstra example graph -- dynamic layout, nodes A-F with weighted edges
dijkstra_net = ed.NetworkDiagram(
    width=CW * 0.7,
    height=230,
    caption="Fig 4: Dijkstra example graph (A=source) -- shortest paths computed iteratively",
)
dijkstra_net.node("A", "A\n(src)", kind="router")
dijkstra_net.node("B", "B", kind="generic")
dijkstra_net.node("C", "C", kind="generic")
dijkstra_net.node("D", "D", kind="generic")
dijkstra_net.node("E", "E", kind="generic")
dijkstra_net.node("F", "F\n(dest)", kind="host")
dijkstra_net.link("A", "B", label="2")
dijkstra_net.link("A", "C", label="4")
dijkstra_net.link("B", "C", label="1")
dijkstra_net.link("B", "D", label="5")
dijkstra_net.link("C", "E", label="3")
dijkstra_net.link("D", "E", label="1")
dijkstra_net.link("D", "F", label="4")
dijkstra_net.link("E", "F", label="2")
story.extend(dijkstra_net.as_flowable())

section("Bellman-Ford Algorithm")
definition(
    "<b>Bellman-Ford Algorithm:</b> A dynamic-programming shortest-path algorithm "
    "that can handle <b>negative edge weights</b> and detects <b>negative weight "
    "cycles</b>. Unlike Dijkstra, it relaxes ALL edges in V-1 iterations. "
    "Used by RIP and other distance-vector protocols."
)
bullet(
    [
        "Time complexity: <b>O(V * E)</b> -- slower than Dijkstra for dense graphs.",
        "Requires V-1 iterations (V = number of vertices).",
        "After V-1 iterations, perform one more pass to detect negative cycles.",
        "If any distance decreases in the V-th iteration: negative weight cycle exists.",
        "Handles negative edge weights (Dijkstra cannot).",
    ]
)
code_block("""
 BELLMAN-FORD -- ALGORITHM PSEUDOCODE:
 =====================================================================
 Input: Graph G(V, E), source s, edge weights w(u,v)
 Output: Shortest distances from s to all vertices

 Initialize:
   dist[s] = 0
   dist[v] = INF for all v != s
   pred[v] = None for all v

 Main loop (V-1 iterations):
   for i = 1 to |V| - 1:
     for each edge (u, v) in E:
       if dist[u] != INF and dist[u] + w(u,v) < dist[v]:
         dist[v] = dist[u] + w(u,v)
         pred[v] = u

 Negative cycle detection:
   for each edge (u, v) in E:
     if dist[u] != INF and dist[u] + w(u,v) < dist[v]:
       print "Negative weight cycle detected!"

 WORKED EXAMPLE:
   Vertices: A B C D E  (5 nodes -> 4 iterations)
   Edges: A->B:6, A->D:7, B->C:5, B->D:8, B->E:-4,
          C->B:-2, D->C:-3, D->E:9, E->A:2, E->C:7
   Source: A

   Init:   A:0, B:INF, C:INF, D:INF, E:INF

   Iter 1: A->B: B=6, A->D: D=7, B->C: C=11, B->E: E=2,
           D->C: C=min(11,7-3)=4, D->E: E=min(2,7+9)=2
           Result: A:0, B:6, C:4, D:7, E:2

   Iter 2: C->B: B=min(6,4-2)=2, B->E: E=min(2,2-4)=-2
           Result: A:0, B:2, C:4, D:7, E:-2

   Iter 3: B->E: E=min(-2,2-4)=-2 (no change)
           Result: A:0, B:2, C:4, D:7, E:-2

   Final:  A->A:0, A->B:2, A->C:4, A->D:7, A->E:-2
""")

# Bellman-Ford example graph -- directed graph with negative weights
bf_net = ed.NetworkDiagram(
    width=CW * 0.7,
    height=230,
    caption="Fig 5: Bellman-Ford example graph (A=source) -- directed edges with negative weights",
)
bf_net.node("A", "A\n(src)", x=80, y=115, kind="router")
bf_net.node("B", "B", x=135, y=190, kind="generic")
bf_net.node("C", "C", x=225, y=160, kind="generic")
bf_net.node("D", "D", x=135, y=40, kind="generic")
bf_net.node("E", "E", x=225, y=70, kind="generic")

bf_net.link("A", "B", label="6", bidirectional=False)
bf_net.link("A", "D", label="7", bidirectional=False)
bf_net.link("B", "C", label="5 (B->C) | -2 (C->B)", bidirectional=True)
bf_net.link("B", "D", label="8", bidirectional=False)
bf_net.link("B", "E", label="-4", bidirectional=False)
bf_net.link("D", "C", label="-3", bidirectional=False)
bf_net.link("D", "E", label="9", bidirectional=False)
bf_net.link("E", "A", label="2", bidirectional=False)
bf_net.link("E", "C", label="7", bidirectional=False)
story.extend(bf_net.as_flowable())

info_table(
    ["Feature", "Dijkstra's Algorithm", "Bellman-Ford Algorithm"],
    [
        [
            "Approach",
            "Greedy -- visits nearest node first",
            "Dynamic programming -- relaxes all edges iteratively",
        ],
        [
            "Negative wt",
            "Cannot handle -- produces wrong results",
            "Handles negative weights correctly",
        ],
        ["Neg. cycles", "Cannot detect", "Detects negative weight cycles"],
        ["Complexity", "O((V+E) log V) with priority queue", "O(V * E) -- slower"],
        [
            "Iterations",
            "V iterations (one node settled per iter)",
            "V-1 iterations + 1 cycle detection pass",
        ],
        [
            "Usage",
            "OSPF, Dijkstra-based routing",
            "RIP (conceptually), distance-vector protocols",
        ],
        [
            "Best for",
            "Non-negative weights, faster computation",
            "Negative weights, cycle detection",
        ],
    ],
)
tip(
    "Dijkstra: greedy, non-negative weights, O(V log V + E), used in OSPF. "
    "Bellman-Ford: dynamic programming, handles negatives, O(VE), V-1 iterations. "
    "EXAM: always show the iteration table for both algorithms. "
    "Dijkstra permanently settles one node per iteration. BF relaxes ALL edges each iteration."
)
br()


# -----------------------------------------------------------------------------
#  4.10  CONGESTION CONTROL
# -----------------------------------------------------------------------------
chap_box("4.10  Congestion Control")
section("What is Congestion?")
definition(
    "<b>Congestion:</b> A state in which the demand for network resources (router "
    "buffers, link bandwidth) exceeds the supply. When too many packets arrive at "
    "a router faster than it can forward them, its buffer fills up. New packets are "
    "dropped. The network throughput decreases -- sometimes catastrophically "
    "(congestion collapse)."
)
bullet(
    [
        "Primary cause: too many sources sending too much data too fast.",
        "Router buffers overflow -> packet loss -> retransmissions -> more congestion.",
        "Congestion collapse: throughput approaches zero under extreme load.",
    ]
)

section("Causes of Congestion")
info_table(
    ["Cause", "Description"],
    [
        [
            "Insufficient buffer space",
            "Router has limited memory. When full, packets are dropped (tail drop or RED).",
        ],
        ["Slow processors", "Router CPU too slow to process packets at wire speed."],
        [
            "Bandwidth mismatch",
            "High-speed input link feeds into a low-speed output link -- bottleneck.",
        ],
        [
            "Bursty traffic",
            "Traffic arrives in bursts exceeding momentary link capacity.",
        ],
        [
            "Slow convergence",
            "Routing protocol takes time to adapt after a failure, causing temporary loops.",
        ],
    ],
)

section("Open-Loop vs Closed-Loop Congestion Control")
info_table(
    ["Type", "When Applied", "Mechanism", "Examples"],
    [
        [
            "Open-Loop (Preventive)",
            "Before congestion occurs",
            "Pre-planned admission control, traffic shaping, leaky bucket, token bucket.",
            "Leaky bucket, token bucket, traffic policing",
        ],
        [
            "Closed-Loop (Reactive)",
            "After congestion detected",
            "Feedback to source: reduce sending rate when congestion signals received.",
            "TCP congestion control, ICMP Source Quench, ECN",
        ],
    ],
)

section("Congestion Control Algorithms")
subsection("Leaky Bucket Algorithm")
body(
    "Incoming packets (of variable sizes and rates) are poured into a bucket with a "
    "constant-rate leak. The bucket acts as a queue. If the bucket is full, excess "
    "packets are discarded. The output is a smooth constant-rate stream -- bursty "
    "traffic is <b>shaped</b> into uniform flow."
)
code_block("""
 LEAKY BUCKET:
 =====================================================================
 Bucket capacity = B bytes/packets
 Leak rate       = R packets/second (constant output rate)
 
 Algorithm:
   When packet arrives:
     If bucket has space: add to bucket.
     Else: DISCARD packet (bucket full = congestion).
   Drain bucket at constant rate R.

 Effect: Output is always constant rate R, regardless of input burst.
 Use:    Traffic SHAPING -- smooth out bursty traffic for QoS compliance.
""")

# Leaky Bucket Flowchart
leaky_fc = ed.Flowchart(
    width=400,
    height=260,
    caption="Fig 6a: Leaky Bucket Traffic Shaper Flowchart",
)
leaky_fc.terminal("arrive", "Packet Arrives (Size S)", x=200, y=230)
leaky_fc.decision("check", "Bucket holds + S <= B?", x=200, y=160)
leaky_fc.process("add", "Add S to bucket\n(Enqueue packet)", x=90, y=90)
leaky_fc.process("drop", "Discard packet\n(Bucket full)", x=310, y=90)
leaky_fc.io_box("leak", "Drain at constant rate R", x=90, y=30)

leaky_fc.edge("arrive", "check")
leaky_fc.edge("check", "add", branch="yes")
leaky_fc.edge("check", "drop", branch="no")
leaky_fc.edge("add", "leak")
story.extend(leaky_fc.as_flowable())
br()

subsection("Token Bucket Algorithm")
body(
    "Tokens are added to a bucket at a constant rate (r tokens/second). The bucket "
    "holds at most B tokens. Each transmitted packet consumes one token. If no token "
    "is available, the packet must wait. Unlike leaky bucket, token bucket allows "
    "<b>bursts</b> -- if tokens have accumulated, the source can burst up to B packets."
)
code_block("""
 TOKEN BUCKET:
 =====================================================================
 Token arrival rate  = r tokens/second
 Bucket capacity     = B tokens (maximum burst size)
 
 Algorithm:
   Add r tokens/sec to bucket (up to max B).
   When packet arrives:
     If token available: consume 1 token, transmit packet.
     Else: wait for token (or drop, depending on policy).

 Maximum burst: B packets can be sent at once (if tokens accumulated).
 Long-term rate: cannot exceed r packets/second.
 
 Comparison:
   Leaky Bucket: enforces constant rate -- no bursts allowed.
   Token Bucket: allows controlled bursts up to B -- more flexible.
""")

# Token Bucket Flowchart
token_fc = ed.Flowchart(
    width=400,
    height=260,
    caption="Fig 6b: Token Bucket Traffic Shaper Flowchart",
)
token_fc.terminal("arrive", "Packet Arrives (Size S)", x=200, y=230)
token_fc.decision("check", "Bucket has >= S tokens?", x=200, y=160)
token_fc.process(
    "transmit", "Consume S tokens\nTransmit packet immediately", x=90, y=90
)
token_fc.process("queue_drop", "Wait for tokens / Drop\n(based on policy)", x=310, y=90)

token_fc.edge("arrive", "check")
token_fc.edge("check", "transmit", branch="yes")
token_fc.edge("check", "queue_drop", branch="no")
story.extend(token_fc.as_flowable())
br()

subsection("Random Early Detection (RED)")
body(
    "RED is an <b>active queue management</b> (AQM) algorithm used at routers. "
    "Instead of waiting for the buffer to be completely full (tail drop), RED "
    "randomly drops packets early when the average queue length exceeds a threshold. "
    "This signals congestion to TCP senders before the buffer fills completely."
)
bullet(
    [
        "Min threshold: below this, no dropping. Queue is building.",
        "Max threshold: above this, all packets dropped. Queue is full.",
        "Between min and max: each packet dropped with probability proportional to how full the queue is.",
        "Advantage: avoids global synchronisation (multiple TCP flows reducing at once).",
    ]
)

subsection("TCP Congestion Control")
body(
    "TCP implements end-to-end congestion control using a <b>congestion window (cwnd)</b>. "
    "The actual sending rate = min(cwnd, receiver's advertised window) / RTT."
)
info_table(
    ["Phase", "Algorithm", "cwnd Growth", "Trigger"],
    [
        [
            "Slow Start",
            "Exponential growth",
            "Double per RTT (1->2->4->8->...)",
            "Start / after timeout",
        ],
        [
            "Congestion Avoidance",
            "Linear (AIMD)",
            "+1 MSS per RTT",
            "After cwnd >= ssthresh",
        ],
        [
            "Fast Retransmit",
            "Detect loss early",
            "Retransmit on 3 duplicate ACKs",
            "3 dup ACKs (not timeout)",
        ],
        [
            "Fast Recovery",
            "Avoid slow start",
            "cwnd = ssthresh + 3 MSS",
            "After fast retransmit",
        ],
    ],
)
code_block("""
 TCP CONGESTION CONTROL -- RENO ALGORITHM:
 =====================================================================
 Initial: cwnd = 1 MSS, ssthresh = large value

 SLOW START phase:
   On each ACK: cwnd = cwnd + 1 MSS   (doubles each RTT)
   Until cwnd >= ssthresh OR loss detected

 CONGESTION AVOIDANCE phase (cwnd >= ssthresh):
   On each ACK: cwnd = cwnd + MSS * MSS / cwnd   (~+1 MSS per RTT)
   = ADDITIVE INCREASE

 ON TIMEOUT (severe congestion):
   ssthresh = cwnd / 2
   cwnd = 1 MSS
   Go back to SLOW START

 ON 3 DUPLICATE ACKs (mild congestion -- fast retransmit):
   ssthresh = cwnd / 2
   cwnd = ssthresh + 3 MSS     (fast recovery -- skip slow start)
   = MULTIPLICATIVE DECREASE
   Retransmit missing segment

 KEY PRINCIPLE: AIMD (Additive Increase, Multiplicative Decrease)
   Increase: +1 MSS per RTT during congestion avoidance
   Decrease: halve cwnd on congestion signal
""")


def make_state_drawer(label_text: str) -> Callable[..., None]:
    def draw(
        sm: ed.StateMachine,
        x: float,
        y: float,
        radius: float,
        fill: str,
        stroke: str,
    ) -> None:
        sm._add(pds.circle(x, y, radius, fill=fill, stroke=stroke))
        sm._add(
            pds.centered_wrapped_label(
                x,
                y,
                label_text,
                max_width=radius * 1.8,
                font=sm.theme.font_name_bold,
                size=8.5,
                color=sm.theme.state_text,
            )
        )

    return draw


tcp_cc_sm = ed.StateMachine(
    width=380,
    height=200,
    caption="Fig 7: TCP Congestion Control State Transition Diagram (Reno)",
    state_r=35.0,
)
tcp_cc_sm.state(
    "SS",
    "Slow Start",
    initial=True,
    custom_draw=make_state_drawer("Slow\nStart"),
)
tcp_cc_sm.state(
    "CA",
    "Congestion Avoidance",
    custom_draw=make_state_drawer("Congestion\nAvoidance"),
)
tcp_cc_sm.state(
    "FR", "Fast Recovery", custom_draw=make_state_drawer("Fast\nRecovery")
)

tcp_cc_sm.transition("SS", "CA", label="cwnd >= ssthresh")
tcp_cc_sm.transition("SS", "FR", label="3 Dup ACKs")
tcp_cc_sm.transition("CA", "SS", label="Timeout")
tcp_cc_sm.transition("CA", "FR", label="3 Dup ACKs")
tcp_cc_sm.transition("FR", "SS", label="Timeout")
tcp_cc_sm.transition("FR", "CA", label="New ACK")
story.extend(tcp_cc_sm.as_flowable())
tip(
    "Congestion control: open-loop (prevent) vs closed-loop (react). "
    "Leaky bucket: smooth constant output. Token bucket: allows bursts. "
    "TCP: slow start (exponential) -> congestion avoidance (linear AIMD). "
    "Timeout -> cwnd=1 (slow start). 3 dup ACKs -> fast recovery."
)
br()

# -----------------------------------------------------------------------------
#  4.11  INTERNETWORKING DEVICES
# -----------------------------------------------------------------------------
chap_box("4.11  Internetworking Devices")
section("Overview")
body(
    "Internetworking devices connect networks at different OSI layers. "
    "The OSI layer at which a device operates determines its capabilities -- "
    "higher-layer devices are more intelligent but also more expensive and slower."
)

section("Layer-by-Layer Device Summary")
info_table(
    [
        "Device",
        "OSI Layer",
        "Addresses Used",
        "Forwarding Basis",
        "Collision Domain",
        "Broadcast Domain",
        "Typical Use",
    ],
    [
        [
            "Repeater",
            "Layer 1",
            "None",
            "Regenerates electrical signal",
            "Extends it",
            "No change",
            "Extending cable length (legacy)",
        ],
        [
            "Hub",
            "Layer 1",
            "None",
            "Broadcasts bits to all ports",
            "Shared (all)",
            "No change",
            "Legacy Ethernet -- obsolete",
        ],
        [
            "Bridge",
            "Layer 2",
            "MAC address",
            "MAC forwarding table (learns)",
            "Separate per port",
            "No change",
            "Connecting two LAN segments",
        ],
        [
            "Switch",
            "Layer 2",
            "MAC address",
            "MAC table per port (fast ASIC)",
            "Separate per port",
            "No change",
            "Modern LAN -- dominant device",
        ],
        [
            "Router",
            "Layer 3",
            "IP address",
            "Routing/forwarding table",
            "Separate",
            "Separate",
            "Connecting networks, Internet",
        ],
        [
            "Gateway",
            "Layer 4-7",
            "IP + Port/other",
            "Protocol translation",
            "Separate",
            "Separate",
            "Translating between protocols",
        ],
        [
            "L3 Switch",
            "Layer 2+3",
            "MAC + IP",
            "Combined MAC table + routing",
            "Separate",
            "Separate (VLAN)",
            "Modern campus/data center",
        ],
    ],
)

section("Repeater")
definition(
    "<b>Repeater:</b> A Layer 1 device that receives a weakened or corrupted electrical "
    "signal, regenerates it to full strength, and retransmits it. Extends the physical "
    "reach of a LAN segment. Does NOT filter frames or separate collision domains. "
    "All segments connected via repeaters form ONE collision domain."
)

section("Hub")
definition(
    "<b>Hub:</b> A Layer 1 multi-port repeater. When a frame arrives on one port, "
    "the hub broadcasts it out ALL other ports simultaneously. All ports share one "
    "collision domain -- only one device can transmit at a time. Now obsolete."
)

section("Bridge")
definition(
    "<b>Bridge:</b> A Layer 2 device that connects two LAN segments and selectively "
    "forwards frames based on destination MAC addresses. Learns MAC addresses by "
    "observing which port frames arrive on. Separates collision domains. "
    "Software-based forwarding -- slower than switches."
)
bullet(
    [
        "Builds a MAC address table by learning: when frame arrives on port X from MAC A, record A->X.",
        "If destination MAC in table: forward only to that port (filtering).",
        "If destination MAC unknown or broadcast: flood to all ports except the source port.",
        "Transparent bridge: plug-and-play, no configuration needed.",
        "Spanning Tree Protocol (STP / IEEE 802.1D) prevents bridging loops in redundant topologies.",
    ]
)

section("Switch")
definition(
    "<b>Switch (Layer 2 Switch):</b> A high-speed, multi-port bridge implemented in "
    "dedicated ASIC hardware. Each port is its own collision domain -- full-duplex "
    "communication (no CSMA/CD needed). The switch builds and uses a MAC address "
    "table (CAM table) to forward frames only to the correct port."
)
bullet(
    [
        "Each port = separate collision domain. Entire switch = one broadcast domain.",
        "Full-duplex: no collisions, no CSMA/CD, simultaneous TX and RX.",
        "VLAN (Virtual LAN): logically divides a single physical switch into multiple broadcast domains.",
        "STP (802.1D) or RSTP (802.1W) prevents layer-2 loops in redundant switch topologies.",
        "Forwarding modes: store-and-forward (full error check), cut-through (fast, no error check), fragment-free.",
    ]
)

section("Router")
definition(
    "<b>Router:</b> A Layer 3 device that forwards packets between different IP networks "
    "based on destination IP addresses and the routing table. Separates both collision "
    "domains AND broadcast domains. The backbone of the Internet."
)
bullet(
    [
        "Each router interface = separate broadcast domain AND separate collision domain.",
        "Routers do NOT forward broadcasts between networks (unlike bridges/switches).",
        "Routing table built by static configuration or dynamic routing protocols (RIP, OSPF, BGP).",
        "NAT (Network Address Translation): commonly performed by routers to map private IPs to public IPs.",
        "Routers connect heterogeneous networks (Ethernet to WAN, IPv4 to IPv6).",
    ]
)

section("Gateway")
definition(
    "<b>Gateway:</b> A Layer 4-7 device that translates between different protocols, "
    "data formats, or architectures. The most intelligent and slowest of all "
    "internetworking devices. Required when connecting networks that use completely "
    "different communication models (e.g., email gateway between SMTP and X.400)."
)
bullet(
    [
        "Application gateway: translates between different application protocols (e.g., HTTP <-> SMTP).",
        "VoIP gateway: converts PSTN telephone signals to VoIP (SIP/H.323).",
        "Default gateway: in home networking, the term 'default gateway' refers to the router that connects the home LAN to the ISP -- this is actually a router, not a true protocol-translating gateway.",
        "Email gateway, firewall gateway, protocol converter.",
    ]
)

# Network diagram showing different devices
devices_net = ed.NetworkDiagram(
    width=CW,
    height=245,
    caption="Fig 5: Internetworking devices at different OSI layers connecting network segments",
)
devices_net.node("pc1", "PC-A", x=45, y=165, kind="host")
devices_net.node("pc2", "PC-B", x=45, y=90, kind="host")
devices_net.node("hub", "Hub (L1)", x=120, y=130, kind="hub")
devices_net.node("sw", "Switch (L2)", x=210, y=130, kind="switch")
devices_net.node("pc3", "PC-C", x=285, y=165, kind="host")
devices_net.node("pc4", "PC-D", x=285, y=90, kind="host")
devices_net.node("rtr", "Router (L3)", x=352, y=130, kind="router")
devices_net.node("wan", "WAN/Internet", x=432, y=160, kind="cloud")
devices_net.node("gw", "Gateway (L7)", x=395, y=55, kind="server")
devices_net.node("legacy", "Legacy Net", x=475, y=55, kind="generic")
devices_net.link("pc1", "hub")
devices_net.link("pc2", "hub")
devices_net.link("hub", "sw", label="Bridge boundary")
devices_net.link("sw", "pc3")
devices_net.link("sw", "pc4")
devices_net.link("sw", "rtr", label="Broadcast boundary")
devices_net.link("rtr", "wan")
devices_net.link("rtr", "gw", label="L7 path")
devices_net.link("gw", "legacy", label="Translate")
story.extend(devices_net.as_flowable())
tip(
    "Repeater/Hub: Layer 1, no filtering. Bridge/Switch: Layer 2, MAC filtering, separates collision domains. "
    "Router: Layer 3, IP filtering, separates broadcast domains. "
    "Gateway: Layer 4-7, protocol translation. "
    "Each router interface = separate broadcast domain -- key exam point."
)
br()


# -----------------------------------------------------------------------------
#  4.12  IPv4 -- INTERNET PROTOCOL
# -----------------------------------------------------------------------------
chap_box("4.12  IPv4 -- Internet Protocol Header")
section("Overview")
definition(
    "<b>IPv4 (Internet Protocol version 4):</b> The primary network-layer protocol "
    "of the Internet. IPv4 is a connectionless, best-effort, unreliable delivery "
    "service -- it makes no guarantees about delivery, ordering, or error correction. "
    "Reliability is provided by upper layers (TCP). Each IPv4 datagram is routed "
    "independently."
)

section("IPv4 Header Format")
packet_format(
    "IPv4 Header Format (minimum 20 bytes, maximum 60 bytes)",
    [
        ("Version", 4),
        ("IHL", 4),
        ("DSCP/ECN", 8),
        ("Total Length", 16),
        ("Identification", 16),
        ("Flags", 3),
        ("Fragment Offset", 13),
        ("TTL", 8),
        ("Protocol", 8),
        ("Header Checksum", 16),
        ("Source IP Address", 32),
        ("Destination IP Address", 32),
        ("Options + Padding", 32),
    ],
)

code_block("""
 IPv4 HEADER FIELD DESCRIPTIONS:
 =====================================================================
 Version (4 bits):         IP version number. Always 4 for IPv4.

 IHL -- Header Length (4 bits):
   Length of the IP header in 32-bit words.
   Minimum = 5 (20 bytes, no options).
   Maximum = 15 (60 bytes, with options).
   Payload data offset = IHL * 4 bytes.

 DSCP/ECN (8 bits, formerly TOS):
   DSCP (6 bits): Differentiated Services Code Point -- QoS marking.
   ECN (2 bits): Explicit Congestion Notification -- signals congestion
                 without dropping packets (requires router + endpoint support).

 Total Length (16 bits):
   Total size of the datagram (header + data) in bytes.
   Maximum = 65,535 bytes.
   Minimum = 20 bytes (header only, no data).

 Identification (16 bits):
   Unique ID assigned to each datagram by the sender.
   All fragments of the same original datagram share the same ID.

 Flags (3 bits):
   Bit 0: Reserved (must be 0).
   Bit 1: DF (Don't Fragment) -- if set, routers must NOT fragment this packet.
           If fragmentation needed and DF set, packet dropped + ICMP error sent.
   Bit 2: MF (More Fragments) -- 1 = more fragments follow, 0 = last fragment.

 Fragment Offset (13 bits):
   Position of this fragment's data relative to the start of the original datagram.
   Measured in units of 8 bytes (64-bit granularity).
   First fragment: offset = 0. MF=1 (unless only one fragment).

 TTL -- Time To Live (8 bits):
   Maximum number of router hops before the packet is discarded.
   Each router decrements TTL by 1. If TTL reaches 0: packet discarded +
   ICMP "Time Exceeded" message sent to source.
   Prevents infinite loops in routing.
   Typical initial values: 64 (Linux), 128 (Windows), 255 (Cisco routers).

 Protocol (8 bits):
   Identifies the upper-layer protocol in the data field.
   1 = ICMP,  6 = TCP,  17 = UDP,  89 = OSPF,  47 = GRE.

 Header Checksum (16 bits):
   One's complement checksum of the IP header ONLY (not data).
   Recalculated at every router (TTL changes each hop).
   If checksum fails: packet silently discarded.

 Source IP Address (32 bits):  IPv4 address of the sender.
 Destination IP Address (32 bits): IPv4 address of the intended receiver.

 Options (0-40 bytes):
   Optional fields: Record Route, Timestamp, Loose/Strict Source Routing.
   Rarely used in practice. Padding ensures header is multiple of 32 bits.
""")

section("IPv4 Fragmentation")
definition(
    "<b>Fragmentation:</b> When an IPv4 datagram is larger than the MTU "
    "(Maximum Transmission Unit) of an outgoing link, the router splits "
    "(fragments) the datagram into smaller pieces. The destination host "
    "reassembles the fragments into the original datagram."
)
code_block("""
 FRAGMENTATION EXAMPLE:
 =====================================================================
 Original datagram: 4000 bytes total (20 header + 3980 data)
 Link MTU: 1500 bytes

 Maximum data per fragment = MTU - header = 1500 - 20 = 1480 bytes
 But offset must be multiple of 8: 1480 / 8 = 185 -- OK.

 Fragment 1: 1500 bytes total
   Header: ID=777, MF=1, Offset=0
   Data:   bytes 0-1479 (1480 bytes)

 Fragment 2: 1500 bytes total
   Header: ID=777, MF=1, Offset=185 (185*8=1480)
   Data:   bytes 1480-2959 (1480 bytes)

 Fragment 3: 1040 bytes total (last fragment)
   Header: ID=777, MF=0, Offset=370 (370*8=2960)
   Data:   bytes 2960-3979 (1020 bytes)

 Reassembly at destination:
   1. Collect all fragments with same ID=777 from same source.
   2. Sort by Fragment Offset.
   3. Check: last fragment has MF=0.
   4. Reassemble data in offset order.
   5. Verify total size = expected.

 NOTE: If ANY fragment is lost, the entire datagram is discarded
 (IP has no partial reassembly). TCP must retransmit the whole segment.
""")

# IPv4 Fragmentation Diagram
frag_fc = ed.Flowchart(
    width=500,
    height=160,
    caption="Fig 11: IPv4 Fragmentation Example (MTU = 1500 bytes)",
)
frag_fc.process(
    "orig",
    "Original Datagram\nTotal: 4000 B (Header: 20 B, Data: 3980 B)\nID = 777",
    x=250,
    y=120,
)
frag_fc.process(
    "frag1", "Fragment 1\nTotal: 1500 B\nData: 1480 B\nOffset: 0, MF = 1", x=85, y=40
)
frag_fc.process(
    "frag2", "Fragment 2\nTotal: 1500 B\nData: 1480 B\nOffset: 185, MF = 1", x=250, y=40
)
frag_fc.process(
    "frag3", "Fragment 3\nTotal: 1040 B\nData: 1020 B\nOffset: 370, MF = 0", x=415, y=40
)

frag_fc.edge("orig", "frag1")
frag_fc.edge("orig", "frag2")
frag_fc.edge("orig", "frag3")
story.extend(frag_fc.as_flowable())
tip(
    "IPv4 header: 20 bytes minimum, 60 bytes maximum. TTL decremented at each hop. "
    "Protocol 6=TCP, 17=UDP, 1=ICMP. DF bit prevents fragmentation. "
    "Fragment offset in units of 8 bytes. All fragments share same Identification. "
    "MF=1 on all fragments except the last."
)
br()

# -----------------------------------------------------------------------------
#  4.13  IPv6 -- NEXT GENERATION IP
# -----------------------------------------------------------------------------
chap_box("4.13  IPv6 -- Next Generation Internet Protocol")
section("Why IPv6?")
definition(
    "<b>IPv6 (Internet Protocol version 6):</b> The successor to IPv4, standardised "
    "in RFC 2460 (1998). IPv6 was designed to solve the fundamental limitations of "
    "IPv4: address exhaustion, lack of built-in security, poor QoS support, and "
    "the overhead of fragmentation."
)
bullet(
    [
        "<b>Address Space:</b> 128-bit addresses = 2<super>128</super> = 3.4 * 10<super>38</super> addresses -- effectively unlimited.",
        "<b>Simplified Header:</b> Fixed 40-byte header (no options, no checksum, no fragmentation in header).",
        "<b>No Fragmentation by Routers:</b> Only the source host can fragment (using Path MTU Discovery). Routers no longer fragment.",
        "<b>No Header Checksum:</b> Removed since link-layer CRC and transport-layer checksums are sufficient. Speeds up router processing.",
        "<b>Built-in IPSec:</b> Mandatory support for authentication and encryption (IPSec).",
        "<b>Auto-configuration:</b> SLAAC (Stateless Address Auto-Configuration) -- hosts configure their own IP addresses without DHCP.",
        "<b>No Broadcast:</b> IPv6 uses multicast instead of broadcast. No more broadcast storms.",
        "<b>Flow Label:</b> New header field to identify traffic flows for QoS.",
    ]
)

section("IPv6 Address Notation")
code_block("""
 IPv6 ADDRESS FORMAT:
 =====================================================================
 128 bits written as 8 groups of 4 hex digits, separated by colons:
   2001:0db8:85a3:0000:0000:8a2e:0370:7334

 SIMPLIFICATION RULES:
 Rule 1: Leading zeros in each group may be omitted:
   2001:db8:85a3:0:0:8a2e:370:7334

 Rule 2: One (and only one) consecutive group of all-zeros may be
         replaced by :: (double colon):
   2001:db8:85a3::8a2e:370:7334

 Example compressions:
   Full:         2001:0db8:0000:0000:0000:0000:0000:0001
   Remove zeros: 2001:db8:0:0:0:0:0:1
   Use ::        2001:db8::1

   Full:         fe80:0000:0000:0000:0204:61ff:fe9d:f156
   Compressed:   fe80::204:61ff:fe9d:f156

 SPECIAL IPv6 ADDRESSES:
   ::1                   Loopback (equivalent to 127.0.0.1)
   ::                    Unspecified (0.0.0.0 equivalent)
   fe80::/10             Link-Local (auto-configured, not routed)
   fc00::/7              Unique Local (private, RFC 4193)
   ff00::/8              Multicast (all 1s in first byte)
   2000::/3              Global Unicast (public IPv6 addresses)
   ::ffff:0:0/96         IPv4-mapped IPv6 addresses

 PREFIX NOTATION (CIDR in IPv6):
   2001:db8::/32   <- 32-bit prefix (ISP allocation typical)
   2001:db8:1::/48 <- 48-bit prefix (site/organisation)
   2001:db8:1:1::/64 <- 64-bit prefix (subnet, most common)
""")

section("IPv6 Header Format")
packet_format(
    "IPv6 Base Header Format (fixed 40 bytes)",
    [
        ("Version", 4),
        ("Traffic Class", 8),
        ("Flow Label", 20),
        ("Payload Length", 16),
        ("Next Header", 8),
        ("Hop Limit", 8),
        ("Source Address", 128),
        ("Destination Address", 128),
    ],
)

code_block("""
 IPv6 HEADER FIELDS:
 =====================================================================
 Version (4 bits):       Always 6 for IPv6.

 Traffic Class (8 bits): Similar to IPv4 DSCP/TOS -- QoS marking.
                         DSCP (6 bits) + ECN (2 bits).

 Flow Label (20 bits):   NEW in IPv6. Identifies a flow (sequence of
                         packets from same source to same destination).
                         Routers can provide special handling to flows
                         without inspecting upper-layer headers.

 Payload Length (16 bits): Length of the data AFTER the IPv6 header.
                           (Unlike IPv4 Total Length which includes header.)

 Next Header (8 bits):  Identifies the protocol in the next header.
                         Same values as IPv4 Protocol field.
                         6=TCP, 17=UDP, 58=ICMPv6, 43=Routing header,
                         44=Fragment header, 0=Hop-by-Hop options.
                         IPv6 uses a chain of extension headers instead
                         of a single options field.

 Hop Limit (8 bits):    Replaces IPv4 TTL. Decremented by 1 at each hop.
                         Packet discarded when it reaches 0.

 Source Address (128 bits):      Sender's IPv6 address.
 Destination Address (128 bits): Receiver's IPv6 address.

 EXTENSION HEADERS (optional, chained via Next Header field):
   Hop-by-Hop Options  : processed by every router.
   Routing Header      : source routing (list of intermediate nodes).
   Fragment Header     : fragmentation info (only source can fragment).
   Authentication Header (AH): IPSec integrity and authentication.
   Encapsulating Security Payload (ESP): IPSec encryption.
   Destination Options : processed only by destination.
""")

section("IPv4 vs IPv6 Comparison")
info_table(
    ["Feature", "IPv4", "IPv6"],
    [
        ["Address size", "32 bits (4 bytes)", "128 bits (16 bytes)"],
        ["Address space", "~4.3 billion", "~3.4 * 10<super>38</super> (unlimited)"],
        ["Notation", "Dotted decimal (192.168.1.1)", "Colon-hex (2001:db8::1)"],
        ["Header size", "Variable 20-60 bytes", "Fixed 40 bytes"],
        [
            "Header checksum",
            "Yes (recalculated at each router)",
            "No (removed for speed)",
        ],
        [
            "Fragmentation",
            "By routers and hosts",
            "Only by source host (Path MTU Discovery)",
        ],
        [
            "Broadcast",
            "Yes (255.255.255.255)",
            "No broadcast -- uses multicast instead",
        ],
        ["Multicast", "Optional (Class D)", "Integral (ff00::/8)"],
        ["IPSec", "Optional", "Mandatory support"],
        ["Auto-config", "Manual or DHCP", "SLAAC (stateless), DHCPv6 (stateful)"],
        ["ARP", "ARP (broadcast)", "NDP (Neighbour Discovery Protocol -- multicast)"],
        ["QoS", "TOS/DSCP (8 bits)", "Traffic Class + Flow Label (28 bits)"],
        [
            "NAT",
            "Widely used (IPv4 exhaustion workaround)",
            "Not needed (huge address space)",
        ],
    ],
)

section("IPv4 to IPv6 Transition Mechanisms")
bullet(
    [
        "<b>Dual Stack:</b> Devices run both IPv4 and IPv6 simultaneously. Use IPv6 when possible, fall back to IPv4. Most widely deployed approach.",
        "<b>Tunneling:</b> IPv6 packets encapsulated inside IPv4 packets to traverse IPv4 infrastructure. 6to4, ISATAP, Teredo tunnels.",
        "<b>Translation (NAT64/DNS64):</b> IPv6-only clients communicate with IPv4-only servers via translation at a border device. The translator rewrites headers.",
    ]
)
tip(
    "IPv6: 128-bit, colon-hex, fixed 40-byte header, no broadcast, no fragmentation by routers, no checksum. "
    "Loopback = ::1. Link-local = fe80::/10. Multicast = ff00::/8. "
    "Next Header replaces IPv4 Protocol field. Hop Limit replaces TTL. "
    "Flow Label is NEW in IPv6 -- not present in IPv4."
)
br()


# =============================================================================
#  4.14  QUICK REVISION SUMMARY
# =============================================================================
part_box("UNIT IV -- QUICK REVISION SUMMARY")
chap_box("Key Concepts at a Glance")

info_table(
    ["Topic", "Key Point to Remember"],
    [
        [
            "Network Layer Role",
            "Host-to-host (logical) delivery across multiple networks. Services: addressing, routing, forwarding, fragmentation, error reporting (ICMP).",
        ],
        [
            "IPv4 Address",
            "32 bits, dotted decimal. Network ID + Host ID separated by subnet mask. 2^32 = ~4.3 billion total addresses.",
        ],
        [
            "Class A",
            "First bit=0. /8 mask. Range: 1.0.0.0-126.255.255.255. 16,777,214 hosts per network.",
        ],
        [
            "Class B",
            "First 2 bits=10. /16 mask. Range: 128.0.0.0-191.255.255.255. 65,534 hosts per network.",
        ],
        [
            "Class C",
            "First 3 bits=110. /24 mask. Range: 192.0.0.0-223.255.255.255. 254 hosts per network.",
        ],
        [
            "Class D",
            "Multicast 224.0.0.0-239.255.255.255. Class E: Reserved 240.0.0.0-255.255.255.255.",
        ],
        [
            "CIDR",
            "Block size = 2^(32-prefix). Hosts = block size - 2. /26 = 64 addresses, 62 hosts. /30 = 4 addresses, 2 hosts.",
        ],
        [
            "Subnetting",
            "Borrow bits from host part. Subnets = 2^(borrowed). Hosts/subnet = 2^(remaining) - 2. Extends prefix.",
        ],
        [
            "VLSM",
            "Different subnet sizes in same parent block. Allocate largest subnets first, then smaller.",
        ],
        [
            "Supernetting",
            "Combine contiguous blocks. Shortens prefix. Used for route aggregation to reduce routing table size.",
        ],
        [
            "ARP",
            "Maps IP -> MAC. Broadcast request on LAN. Unicast reply. ARP cache stores mappings. RARP = MAC->IP (obsolete).",
        ],
        [
            "Direct Delivery",
            "Source and destination on same subnet. ARP for dest MAC. Frame sent directly.",
        ],
        [
            "Indirect Delivery",
            "Different subnets. Packet sent to default gateway. IP unchanged; MAC changes each hop.",
        ],
        [
            "Longest Prefix Match",
            "Router picks most specific (longest) matching route for each packet. Default = 0.0.0.0/0.",
        ],
        [
            "RIP",
            "Distance vector. Bellman-Ford. Metric = hop count (max 15). Updates every 30 sec. Small networks only.",
        ],
        [
            "OSPF",
            "Link state. Dijkstra. Metric = cost (100Mbps/BW). Fast convergence. Hierarchical areas. Large networks.",
        ],
        [
            "BGP",
            "Path vector. TCP port 179. AS path prevents loops. Policy-based. Internet routing between ASes.",
        ],
        [
            "Dijkstra",
            "Greedy. Non-negative weights. O(V log V + E). Settles one node per iteration. Used in OSPF.",
        ],
        [
            "Bellman-Ford",
            "Dynamic programming. Handles negative weights. O(V*E). V-1 iterations. Detects negative cycles.",
        ],
        [
            "Leaky Bucket",
            "Constant output rate. Bursty input smoothed. Excess dropped. Enforces exact rate.",
        ],
        [
            "Token Bucket",
            "Tokens accumulate. Burst allowed (up to B tokens). Long-term rate = r tokens/sec.",
        ],
        [
            "TCP Congestion Ctrl",
            "Slow start (exponential) -> Congestion Avoidance (AIMD +1 MSS/RTT). Timeout: cwnd=1. 3 dup ACKs: fast recovery.",
        ],
        [
            "Repeater/Hub",
            "Layer 1. No filtering. Extends/broadcasts. All ports = one collision domain.",
        ],
        [
            "Bridge/Switch",
            "Layer 2. MAC filtering. Each port = separate collision domain. One broadcast domain (per VLAN for switch).",
        ],
        [
            "Router",
            "Layer 3. IP routing. Separates BOTH collision and broadcast domains. Connects different networks.",
        ],
        [
            "IPv4 Header",
            "Min 20 bytes. TTL decremented each hop. Protocol: 6=TCP,17=UDP,1=ICMP. Fragment offset in 8-byte units. MF+DF flags.",
        ],
        [
            "IPv4 Fragmentation",
            "When datagram > link MTU. Router fragments. Reassembled at destination. DF bit prevents. All fragments same ID.",
        ],
        [
            "IPv6",
            "128-bit, colon-hex. Fixed 40-byte header. No checksum. No router fragmentation. No broadcast. SLAAC. IPSec mandatory.",
        ],
        [
            "IPv6 Special Addresses",
            "::1 = loopback. fe80::/10 = link-local. fc00::/7 = unique local. ff00::/8 = multicast.",
        ],
        [
            "IPv4 vs IPv6",
            "IPv4: 32-bit, variable header, fragmentation by routers, ARP, optional IPSec. IPv6: 128-bit, fixed 40B, SLAAC, NDP, no broadcast.",
        ],
    ],
)

highlight(
    "<b>UNIT IV EXAM BLUEPRINT:</b>  "
    "2-mark: Define CIDR, ARP, TTL, classful addressing. State Dijkstra vs Bellman-Ford difference. "
    "Name internetworking devices with OSI layer.  "
    "5-mark: Compare RIP vs OSPF vs BGP. Explain subnetting with worked example. "
    "Explain ARP operation with diagram. Explain leaky vs token bucket.  "
    "10-mark: Dijkstra full worked example with iteration table (MOST common). "
    "Explain IPv4 header with all fields. Explain IPv6 features vs IPv4 comparison. "
    "Explain congestion control (TCP slow start, AIMD, fast recovery).",
    YELLOW_CARD,
    YELLOW,
)


# =============================================================================
#  BUILD PDF
# =============================================================================
doc = SimpleDocTemplate(
    "CN_Unit4_Notes.pdf",
    pagesize=A4,
    leftMargin=PM,
    rightMargin=PM,
    topMargin=PM,
    bottomMargin=PM,
    title="Computer Networks IT-411 Unit IV Notes",
    author="UIT-RGPV (Autonomous) Bhopal",
)
doc.build(story, onFirstPage=page_decor, onLaterPages=page_decor)
print("Generated: CN_Unit4_Notes.pdf")
