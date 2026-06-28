"""
Computer Networks (IT-411) -- Unit V Notes
UIT-RGPV (Autonomous) Bhopal | Semester IV
Complete exam notes with vector diagrams.
Run: python cn_unit5_notes.py
Output: CN_Unit5_Notes.pdf
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
    data = [
        [Paragraph(f"<b>{name}</b>", th) for name, _ in fields],
        [Paragraph(size, td) for _, size in fields],
    ]
    total_w = sum(max(len(name), len(size)) for name, size in fields)
    col_widths = [
        max(28.0, CW * max(len(name), len(size)) / total_w) for name, size in fields
    ]
    scale = CW / sum(col_widths)
    col_widths = [w * scale for w in col_widths]
    t = Table(data, colWidths=col_widths)
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), CARD_DARK),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("GRID", (0, 0), (-1, -1), 1.0, TABLE_BDR),
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
                    textColor=WHITE_DIM,
                    fontName="Helvetica-Oblique",
                    alignment=TA_CENTER,
                    leading=12,
                ),
            )
        )
    sp(6)


def packet_format(
    caption: str, fields: list[tuple[str, int]], bit_ruler: bool = True
) -> None:
    """Render a 32-bit-aligned packet/header diagram (like Tanenbaum/RFC style)."""
    ruler_style = S(
        f"PF_RULER_{caption[:12]}",
        fontSize=6.5,
        textColor=colors.HexColor("#8b949e"),
        fontName="Helvetica-Bold",
        alignment=TA_CENTER,
        leading=8,
    )

    grid_rows: list[list[tuple[str, int]]] = []
    current_row: list[tuple[str, int]] = []
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
                f_sz, l_ing = (
                    (5.0, 6.0)
                    if width <= 2
                    else (
                        (6.0, 7.0)
                        if width <= 4
                        else (7.0, 8.0) if width <= 6 else (8.0, 10.0)
                    )
                )
                cell_th = S(
                    f"PF_H_{caption[:12]}_{r_idx}_{col_cursor}",
                    fontSize=f_sz,
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
    row_heights: list[float] = []
    if bit_ruler:
        row_heights.append(10)
    for _ in range(len(matrix) - (1 if bit_ruler else 0)):
        row_heights.append(26)

    t = Table(matrix, colWidths=col_widths, rowHeights=row_heights)
    style_cmds: list[Any] = [
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
        ("LEFTPADDING", (0, 0), (-1, -1), 1),
        ("RIGHTPADDING", (0, 0), (-1, -1), 1),
    ]
    start_grid_row = 1 if bit_ruler else 0
    style_cmds += [
        ("GRID", (0, start_grid_row), (-1, -1), 0.75, TABLE_BDR),
        ("BACKGROUND", (0, start_grid_row), (-1, -1), CARD_DARK),
    ]
    style_cmds.extend(spans)
    t.setStyle(TableStyle(style_cmds))
    add(t)
    if caption:
        add(Spacer(1, 4))
        add(
            Paragraph(
                f"<i>{caption}</i>",
                S(
                    f"PF_CAP_{caption[:12]}",
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
add(Paragraph("Unit V -- Complete Exam Notes", COVER_H2))
add(Paragraph("Subject Code: IT-411  |  UIT-RGPV (Autonomous) Bhopal", COVER_SUB))
add(Paragraph("Semester IV  |  Based on University Syllabus 2024-25", COVER_SUB))
sp(10)
rule(CYAN, 1.5)
sp(8)

info_table(
    ["Topic", "Coverage"],
    [
        [
            "5.1 Transport Layer Services",
            "Role, services, addressing, connection vs connectionless",
        ],
        [
            "5.2 Process-to-Process Delivery",
            "Port numbers, sockets, multiplexing, demultiplexing",
        ],
        [
            "5.3 UDP -- User Datagram Protocol",
            "Header format, checksum, use cases, advantages",
        ],
        [
            "5.4 TCP -- Transmission Control Protocol",
            "Header, 3-way handshake, teardown, state machine",
        ],
        ["5.5 TCP Flow Control", "Sliding window, receiver buffer, zero-window probe"],
        [
            "5.6 TCP Congestion Control",
            "Slow start, AIMD, fast retransmit, fast recovery, CUBIC",
        ],
        [
            "5.7 Quality of Service (QoS)",
            "Parameters, traffic classes, scheduling, policing",
        ],
        [
            "5.8 Integrated Services (IntServ)",
            "Resource reservation, RSVP, guaranteed service",
        ],
        [
            "5.9 Differentiated Services (DiffServ)",
            "Per-hop behavior, DSCP markings, traffic classes",
        ],
        [
            "5.10 LAN-WAN Design",
            "Hierarchical LAN design, structured cabling, WAN integration",
        ],
        [
            "5.11 TCP/IP Configuration",
            "Static and DHCP configuration, subnet mask, gateway, DNS",
        ],
        ["5.12 ipconfig and ping", "Commands, output interpretation, troubleshooting"],
        [
            "5.13 Structured LAN",
            "Three-tier model, access/distribution/core layers, STP, VLANs",
        ],
        [
            "5.14 Device Configuration",
            "Switch, hub, bridge, router, gateway -- configuration overview",
        ],
        ["5.15 Quick Revision Summary", "Key formulas, tables, and exam flashcards"],
    ],
)
br()


# =============================================================================
#  UNIT V DIVIDER
# =============================================================================
part_box("UNIT V -- TRANSPORT LAYER AND LAN-WAN DESIGN")


# -----------------------------------------------------------------------------
#  5.1  TRANSPORT LAYER SERVICES
# -----------------------------------------------------------------------------
chap_box("5.1  Transport Layer Services")
section("Role of the Transport Layer")
definition(
    "<b>Transport Layer (Layer 4 of OSI / Layer 3 of TCP/IP):</b> Provides "
    "<b>logical end-to-end (process-to-process) communication</b> between "
    "application processes running on different hosts. While the Network layer "
    "provides host-to-host delivery, the Transport layer delivers data to the "
    "correct <b>process</b> (application) on the destination host."
)
bullet(
    [
        "Sits between the Application layer (above) and the Network layer (below).",
        "Provides process-to-process communication using <b>port numbers</b>.",
        "The two main Transport layer protocols in TCP/IP are <b>TCP</b> and <b>UDP</b>.",
        "TCP provides: reliable, ordered, error-checked delivery with flow and congestion control.",
        "UDP provides: fast, lightweight, connectionless delivery with no guarantees.",
    ]
)

section("Transport Layer Services Summary")
info_table(
    ["Service", "TCP", "UDP"],
    [
        [
            "Connection",
            "Connection-oriented (3-way handshake)",
            "Connectionless (no setup)",
        ],
        [
            "Reliability",
            "Guaranteed delivery (ACK + retransmit)",
            "No guarantee -- best effort",
        ],
        ["Ordering", "In-order delivery (sequence numbers)", "No ordering guarantee"],
        [
            "Error detection",
            "Checksum + retransmit on error",
            "Checksum only (detect, not correct)",
        ],
        ["Flow control", "Sliding window (prevents buffer overflow)", "None"],
        [
            "Congestion control",
            "Slow start, AIMD, fast retransmit",
            "None -- app must handle",
        ],
        [
            "Speed/overhead",
            "Slower (header + handshake overhead)",
            "Faster (8-byte header, no handshake)",
        ],
        [
            "Use cases",
            "HTTP/S, FTP, SMTP, SSH -- where reliability matters",
            "DNS, VoIP, streaming, gaming, SNMP",
        ],
    ],
)

section("OSI Transport Layer vs TCP/IP Transport Layer")
info_table(
    ["Feature", "OSI Transport Layer", "TCP/IP Transport Layer"],
    [
        ["Protocols", "ISO TP0-TP4, TPDU", "TCP, UDP (plus SCTP, DCCP)"],
        ["Layer number", "Layer 4", "Layer 3 (in 4-layer model)"],
        [
            "Addressing",
            "TSAP (Transport Service Access Point)",
            "Port numbers (16-bit)",
        ],
        [
            "PDU name",
            "TPDU (Transport Protocol Data Unit) / Segment",
            "Segment (TCP) / Datagram (UDP)",
        ],
    ],
)
tip(
    "Transport layer = process-to-process (using port numbers). "
    "Network layer = host-to-host (using IP addresses). "
    "TCP: reliable, ordered, flow control, congestion control. "
    "UDP: fast, lightweight, no reliability -- application decides what to do with errors."
)
br()


# -----------------------------------------------------------------------------
#  5.2  PROCESS-TO-PROCESS DELIVERY
# -----------------------------------------------------------------------------
chap_box("5.2  Process-to-Process Delivery -- Ports and Sockets")
section("Port Numbers")
definition(
    "<b>Port Number:</b> A 16-bit unsigned integer (0-65535) that identifies a "
    "specific application process or service on a host. Used by the Transport "
    "layer to direct incoming data to the correct process. The combination of "
    "IP address and port number is called a <b>socket</b>."
)
code_block("""
 PORT NUMBER RANGES:
 =====================================================================
 Well-Known Ports (0-1023):
   Assigned by IANA to standard services. Require root/admin privileges.
   20/21 = FTP (Data/Control)    22  = SSH      23  = Telnet
   25    = SMTP (Email)          53  = DNS      67/68 = DHCP
   69    = TFTP                  80  = HTTP     110 = POP3
   119   = NNTP                  143 = IMAP     161 = SNMP
   443   = HTTPS                 465 = SMTPS    993 = IMAPS
   995   = POP3S                 3389 = RDP

 Registered Ports (1024-49151):
   Used by specific applications (not requiring root).
   1080  = SOCKS proxy    3306 = MySQL    5432 = PostgreSQL
   6379  = Redis          8080 = HTTP alt 27017 = MongoDB

 Dynamic/Ephemeral Ports (49152-65535):
   Temporarily assigned by the OS for client-side connections.
   Released when connection closes.
   Example: browser opens connection using ephemeral port 52341

 SOCKET = IP address + Port number
   Example: 192.168.1.10:80  (web server socket)
            10.0.0.5:52341   (client ephemeral socket)
""")

section("Multiplexing and Demultiplexing")
definition(
    "<b>Multiplexing (Sender):</b> The Transport layer at the sender collects "
    "data from multiple application processes, encapsulates each in a segment "
    "with the appropriate source and destination port numbers, and passes them "
    "to the Network layer. Multiple applications share the same IP/network."
)
definition(
    "<b>Demultiplexing (Receiver):</b> The Transport layer at the receiver "
    "receives segments from the Network layer, reads the destination port number, "
    "and delivers the data to the correct application process listening on that port."
)
code_block("""
 MULTIPLEXING / DEMULTIPLEXING:
 =====================================================================
 SENDER (multiplexing):
   App A (HTTP, port 80)  ]
   App B (FTP, port 21)   ] --> Transport Layer --> Network Layer --> ...
   App C (SSH, port 22)   ]
   Each gets its own port number in the segment header.

 RECEIVER (demultiplexing):
   Incoming segment with dst port 80 --> deliver to HTTP process
   Incoming segment with dst port 21 --> deliver to FTP process
   Incoming segment with dst port 22 --> deliver to SSH process

 TCP DEMULTIPLEXING (4-tuple):
   Unique connection identified by: (src IP, src port, dst IP, dst port)
   Two connections from the same client to the same server can coexist
   if they use different source ports.

 UDP DEMULTIPLEXING (2-tuple):
   Identified by: (dst IP, dst port) only.
   Multiple clients can send to the same UDP server socket.
   Server responds using the client's source IP and port.
""")

# Port/socket diagram
seq_mux = ed.SequenceDiagram(
    width=CW,
    height=200,
    caption="Fig 1: Multiplexing at sender and demultiplexing at receiver using port numbers",
)
seq_mux.actor("http", "HTTP App (80)")
seq_mux.actor("transp", "Transport Layer")
seq_mux.actor("net", "Network Layer")
seq_mux.actor("tdst", "Transport Layer")
seq_mux.actor("adst", "HTTP App (80)")
seq_mux.message("http", "transp", "Data + dest port 80", arrow="solid")
seq_mux.message("transp", "net", "TCP Segment (src:ephemeral, dst:80)", arrow="solid")
seq_mux.message("net", "tdst", "IP Packet + Segment", arrow="solid")
seq_mux.message("tdst", "adst", "Demux to port 80 process", arrow="dashed")
story.extend(seq_mux.as_flowable())
tip(
    "Socket = IP address + Port. Multiplexing = many apps share one network connection. "
    "Demultiplexing = directing incoming segments to the right app using port numbers. "
    "TCP uses 4-tuple for demux. UDP uses 2-tuple (dst IP + dst port) only."
)
br()


# -----------------------------------------------------------------------------
#  5.3  UDP
# -----------------------------------------------------------------------------
chap_box("5.3  UDP -- User Datagram Protocol")
section("Overview")
definition(
    "<b>UDP (User Datagram Protocol, RFC 768):</b> A simple, connectionless "
    "transport-layer protocol. UDP adds minimal overhead to IP -- just port "
    "numbers, length, and a checksum. It makes no attempt to provide reliability, "
    "ordering, or flow control. Applications that need speed over reliability, "
    "or that implement their own reliability, use UDP."
)

section("UDP Header Format")
packet_format(
    "UDP Header (fixed 8 bytes)",
    [
        ("Src Port", 16),
        ("Dst Port", 16),
        ("Length", 16),
        ("Checksum", 16),
    ],
    bit_ruler=True,
)
code_block("""
 UDP HEADER FIELDS:
 =====================================================================
 Source Port (16 bits):
   Port number of the sending process.
   Optional -- may be 0 if the sender doesn't need a reply.

 Destination Port (16 bits):
   Port number of the receiving process.
   Used for demultiplexing.

 Length (16 bits):
   Total length of the UDP datagram (header + data) in bytes.
   Minimum = 8 bytes (header only, no data).
   Maximum = 65,535 bytes (limited by 16-bit field).

 Checksum (16 bits):
   Computed over a pseudo-header (src IP, dst IP, protocol=17, UDP length)
   PLUS the UDP header and data.
   Optional in IPv4 (set to 0 if not used). MANDATORY in IPv6.
   If checksum fails at receiver: datagram silently discarded.

 UDP PSEUDO-HEADER (used for checksum calculation only):
 | Src IP (32 bits) | Dst IP (32 bits) | 0 | Proto=17 | UDP Length |
""")

section("UDP Use Cases")
info_table(
    ["Application", "Why UDP?", "Protocol"],
    [
        [
            "DNS",
            "Single request/response. Retransmit at app level if needed. Very fast.",
            "UDP port 53",
        ],
        [
            "DHCP",
            "Broadcast-based. No connection possible. Simple discover/offer.",
            "UDP port 67/68",
        ],
        [
            "SNMP",
            "Polling. Occasional loss acceptable. Simple and fast.",
            "UDP port 161",
        ],
        [
            "VoIP/Video",
            "Real-time. A retransmitted old packet is worse than no packet.",
            "RTP over UDP",
        ],
        ["Live streaming", "Throughput over reliability. Slight glitch ok.", "UDP/RTP"],
        [
            "Online gaming",
            "Low latency critical. Outdated position updates are useless.",
            "UDP",
        ],
        [
            "TFTP",
            "Simple file transfer. App implements its own stop-and-wait ARQ.",
            "UDP port 69",
        ],
        ["NTP", "Time sync. Single packet query. Simplicity required.", "UDP port 123"],
    ],
)
tip(
    "UDP header = only 8 bytes (Source Port + Dest Port + Length + Checksum). "
    "No handshake, no ACK, no sequence numbers. "
    "Use UDP when: speed > reliability, real-time data, or app handles reliability itself. "
    "DNS and DHCP always use UDP -- memorize these for exams."
)
br()


# -----------------------------------------------------------------------------
#  5.4  TCP
# -----------------------------------------------------------------------------
chap_box("5.4  TCP -- Transmission Control Protocol")
section("Overview")
definition(
    "<b>TCP (Transmission Control Protocol, RFC 793):</b> A connection-oriented, "
    "reliable, full-duplex, byte-stream transport protocol. TCP guarantees that all "
    "data arrives at the destination in order, without duplicates, without errors, "
    "and without loss. It uses sequence numbers, acknowledgements, retransmission, "
    "flow control, and congestion control to achieve this."
)
bullet(
    [
        "<b>Byte stream:</b> TCP treats data as a continuous stream of bytes, not messages.",
        "<b>Full-duplex:</b> Both sides can send and receive simultaneously on the same connection.",
        "<b>Connection-oriented:</b> Connection must be established before data transfer (3-way handshake) and released after (4-way teardown).",
        "<b>Reliable delivery:</b> Every byte acknowledged. Lost/corrupted segments retransmitted.",
        "<b>In-order delivery:</b> Sequence numbers ensure data delivered to application in the correct order.",
        "<b>Flow control:</b> Receiver advertises window size to prevent buffer overflow.",
        "<b>Congestion control:</b> Sender reduces rate when network is congested.",
    ]
)

section("TCP Header Format")
packet_format(
    "TCP Segment Header (min 20 bytes, max 60 bytes with options)",
    [
        # Row 1
        ("Src Port", 16),
        ("Dst Port", 16),
        # Row 2
        ("Sequence Number", 32),
        # Row 3
        ("Acknowledgement Number", 32),
        # Row 4 — 4 + 6 + 6 + 16 = 32
        ("DO", 4),
        ("Rsvd", 6),
        ("URG", 1),
        ("ACK", 1),
        ("PSH", 1),
        ("RST", 1),
        ("SYN", 1),
        ("FIN", 1),
        ("Window Size", 16),
        # Row 5
        ("Checksum", 16),
        ("Urgent Pointer", 16),
        # Row 6 (variable)
        ("Options + Padding (0–40 bytes)", 32),
    ],
    bit_ruler=True,
)
code_block("""
 TCP HEADER FIELD DESCRIPTIONS:
 =====================================================================
 Source Port (16 bits):      Sending process port number.
 Destination Port (16 bits): Receiving process port number.

 Sequence Number (32 bits):
   Position of the FIRST byte of data in this segment within the byte stream.
   If SYN flag is set: this is the ISN (Initial Sequence Number).

 Acknowledgement Number (32 bits):
   The next sequence number the sender of this segment EXPECTS to receive.
   Means "I have received all bytes up to (ACK-1) successfully."
   Only valid when ACK flag is set.

 Data Offset (4 bits):
   Length of the TCP header in 32-bit words. Minimum = 5 (20 bytes).
   Maximum = 15 (60 bytes). Points to the start of data.

 Control Flags (6 bits, each 1 bit):
   URG: Urgent pointer field is valid (rarely used).
   ACK: Acknowledgement number field is valid. Set in all segments except the first SYN.
   PSH: Push -- deliver data to application immediately without buffering.
   RST: Reset -- abruptly terminate the connection due to an error.
   SYN: Synchronize sequence numbers. Used only in connection setup.
   FIN: Finish -- sender has no more data to send. Used in connection teardown.

 Window Size (16 bits):
   Number of bytes the RECEIVER is willing to accept (receive buffer space).
   Used for flow control. The sender may not transmit more than this many
   unacknowledged bytes at a time.

 Checksum (16 bits):
   One's complement checksum over pseudo-header + TCP header + data.
   MANDATORY in both IPv4 and IPv6 (unlike UDP where it was optional in IPv4).

 Urgent Pointer (16 bits):
   Points to the last byte of urgent data when URG flag is set.
   Allows out-of-band data (e.g., Ctrl+C in Telnet session).

 Options (0-40 bytes):
   Common options: MSS (Maximum Segment Size), Window Scale (for large windows),
   SACK (Selective ACK), Timestamps.
""")

section("TCP 3-Way Handshake (Connection Establishment)")
definition(
    "<b>3-Way Handshake:</b> The procedure used to establish a TCP connection. "
    "It ensures both sides are ready to communicate and synchronises their "
    "Initial Sequence Numbers (ISN)."
)

# TCP 3-way handshake sequence diagram
seq_tcp = ed.SequenceDiagram(
    width=CW,
    height=320,
    caption="Fig 2: TCP 3-Way Handshake (connection setup) and 4-Way Teardown",
)
seq_tcp.actor("client", "Client")
seq_tcp.actor("server", "Server")
seq_tcp.message("client", "server", "SYN  (SEQ=x, SYN=1)", arrow="solid")
seq_tcp.message(
    "server", "client", "SYN-ACK  (SEQ=y, ACK=x+1, SYN=1, ACK=1)", arrow="dashed"
)
seq_tcp.message("client", "server", "ACK  (SEQ=x+1, ACK=y+1, ACK=1)", arrow="solid")
seq_tcp.divider("Connection ESTABLISHED -- Data Transfer")
seq_tcp.message("client", "server", "DATA segment(s)", arrow="solid")
seq_tcp.message("server", "client", "ACK", arrow="dashed")
seq_tcp.divider("4-Way Teardown (FIN/ACK)")
seq_tcp.message("client", "server", "FIN  (SEQ=u, FIN=1)", arrow="solid")
seq_tcp.message("server", "client", "ACK  (ACK=u+1)", arrow="dashed")
seq_tcp.message("server", "client", "FIN  (SEQ=v, FIN=1)", arrow="solid")
seq_tcp.message("client", "server", "ACK  (ACK=v+1)", arrow="dashed")
story.extend(seq_tcp.as_flowable())

code_block("""
 TCP 3-WAY HANDSHAKE STEPS:
 =====================================================================
 Step 1 -- SYN (Client -> Server):
   Client sends a TCP segment with SYN flag set and a random ISN (x).
   Client state: CLOSED -> SYN_SENT

 Step 2 -- SYN-ACK (Server -> Client):
   Server acknowledges client's SYN (ACK=x+1) and sends its own SYN
   with a random ISN (y). SYN + ACK flags both set.
   Server state: LISTEN -> SYN_RCVD

 Step 3 -- ACK (Client -> Server):
   Client acknowledges server's SYN (ACK=y+1). ACK flag set.
   Client state: SYN_SENT -> ESTABLISHED
   Server state: SYN_RCVD -> ESTABLISHED

 After these 3 steps, BOTH sides are ESTABLISHED.
 Data can now flow in BOTH directions (full-duplex).

 4-WAY TEARDOWN (FIN/ACK):
 Step 1: Client sends FIN (finished sending data). Client: FIN_WAIT_1
 Step 2: Server ACKs the FIN. Client: FIN_WAIT_2. Server: CLOSE_WAIT
         (Server can still send remaining data to client)
 Step 3: Server sends its own FIN when done. Server: LAST_ACK
 Step 4: Client ACKs server's FIN. Client: TIME_WAIT -> CLOSED (after 2*MSL)
         Server: CLOSED

 TIME_WAIT state (2*MSL = 60-120 seconds):
   Ensures the final ACK reaches the server even if it is lost (retransmitted).
   Prevents old duplicate segments from being mistaken for new connections.
""")

section("TCP State Machine")
sm_tcp = ed.StateMachine(
    width=CW,
    height=200,
    caption="Fig 3: Simplified TCP State Machine (client side)",
)
sm_tcp.state("closed", "CLOSED", initial=True)
sm_tcp.state("syn_sent", "SYN_SENT")
sm_tcp.state("established", "ESTABLISHED")
sm_tcp.state("fin_wait", "FIN_WAIT")
sm_tcp.state("time_wait", "TIME_WAIT", accepting=True)
sm_tcp.transition("closed", "syn_sent", label="connect / SYN")
sm_tcp.transition("syn_sent", "established", label="SYN-ACK / ACK")
sm_tcp.transition("established", "fin_wait", label="close / FIN")
sm_tcp.transition("fin_wait", "time_wait", label="FIN / ACK")
sm_tcp.transition("time_wait", "closed", label="2*MSL timeout")
story.extend(sm_tcp.as_flowable())
tip(
    "3-way handshake: SYN -> SYN-ACK -> ACK. Both sides send and ACK a SYN. "
    "ISN is random to prevent sequence number prediction attacks. "
    "Teardown: 4 steps (FIN/ACK/FIN/ACK). TIME_WAIT lasts 2*MSL. "
    "TCP flags: URG, ACK, PSH, RST, SYN, FIN -- remember with acronym 'Unskilled Attackers Pester Real Security Folks'."
)
br()


# -----------------------------------------------------------------------------
#  5.5  TCP FLOW CONTROL
# -----------------------------------------------------------------------------
chap_box("5.5  TCP Flow Control")
section("Purpose")
definition(
    "<b>Flow Control:</b> A TCP mechanism that prevents the sender from transmitting "
    "data faster than the receiver can process it. The receiver advertises its "
    "available buffer space (the <b>receive window</b>) in every ACK segment. "
    "The sender may not transmit more unacknowledged data than the receive window allows."
)
body(
    "The actual amount a sender can transmit at any time is: "
    "min(congestion window cwnd, receiver's advertised window rwnd). "
    "Flow control handles receiver buffer overflow; congestion control handles "
    "network congestion."
)
code_block("""
 TCP SLIDING WINDOW FLOW CONTROL:
 =====================================================================
 Sender maintains:
   SND.UNA  = oldest unacknowledged byte
   SND.NXT  = next byte to send
   SND.WND  = current send window (from receiver's ACK)

 Receiver maintains:
   RCV.NXT  = next byte expected
   RCV.WND  = available receive buffer space

 Rule: SND.NXT - SND.UNA <= SND.WND
   Sender may not have more than SND.WND bytes outstanding.

 EXAMPLE:
   Receiver buffer = 4096 bytes. Receiver has 2048 bytes buffered.
   Advertised window = 4096 - 2048 = 2048 bytes.
   Sender may send at most 2048 unacknowledged bytes.

 ZERO WINDOW:
   If rwnd = 0: sender must STOP transmitting.
   Sender sends a 1-byte WINDOW PROBE segment periodically to check
   if the receiver has freed buffer space.
   When receiver frees space: sends Window Update (ACK with rwnd > 0).

 SILLY WINDOW SYNDROME:
   Clark's solution: Receiver does not send small window updates.
   Nagle's algorithm: Sender does not send tiny segments.
   Wait until window >= MSS before advertising or sending.
""")

# TCP Sliding Window flowchart (explicit coords for clean layout)
fc_sw = ed.Flowchart(
    width=CW,
    height=260,
    caption="Fig 5: TCP Sliding Window Flow Control (sender side logic)",
)
fc_sw.terminal( "start",   "Segment to Send",           x=260, y=340)
fc_sw.decision( "chkwnd",  "Window space free?",         x=260, y=270)
fc_sw.process(  "wait",    "Wait for Window Update",     x=420, y=200)
fc_sw.process(  "send",    "Send Segment + Start Timer", x=110, y=200)
fc_sw.decision( "ack",     "ACK received?",              x=110, y=130)
fc_sw.process(  "slide",   "Slide Window (SND.UNA++)",   x=110, y=60)
fc_sw.decision( "timeout", "Timer expired?",             x=420, y=130)
fc_sw.process(  "retx",    "Retransmit Segment",         x=420, y=60)
# branch= auto-prepends "Yes"/"No" — do NOT also pass label= or it shows "Yes Yes"
fc_sw.edge("start",   "chkwnd")
fc_sw.edge("chkwnd",  "send",    branch="yes")
fc_sw.edge("chkwnd",  "wait",    branch="no")
# back-loop: use explicit path= waypoints so the arrow doesn't cross the main flow
fc_sw.edge("wait",    "chkwnd",  path=[(490, 200), (490, 330), (330, 330)])
fc_sw.edge("send",    "ack")
fc_sw.edge("ack",     "slide",   branch="yes")
fc_sw.edge("ack",     "timeout", branch="no")
fc_sw.edge("timeout", "retx",    branch="yes")
fc_sw.edge("timeout", "chkwnd",  branch="no",  path=[(490, 130), (490, 330), (330, 330)])
story.extend(fc_sw.as_flowable())

tip(
    "Flow control = receiver controls sender speed via rwnd (receive window). "
    "Congestion control = network controls sender speed via cwnd (congestion window). "
    "Effective window = min(cwnd, rwnd). Zero window probe sent when rwnd=0."
)
br()


# -----------------------------------------------------------------------------
#  5.6  TCP CONGESTION CONTROL
# -----------------------------------------------------------------------------
chap_box("5.6  TCP Congestion Control")
section("Overview")
definition(
    "<b>Congestion Control:</b> TCP's mechanism to prevent the sender from "
    "overwhelming the network (not just the receiver). TCP infers congestion "
    "from packet loss events -- a timeout or duplicate ACKs -- and reduces its "
    "sending rate. TCP uses a <b>congestion window (cwnd)</b> to limit the "
    "amount of data in flight."
)

section("TCP Reno Congestion Control Phases")
info_table(
    ["Phase", "cwnd Behaviour", "Trigger", "ssthresh Update"],
    [
        [
            "Slow Start (SS)",
            "Double per RTT: 1->2->4->8->...",
            "After timeout or start",
            "ssthresh set by timeout",
        ],
        [
            "Congestion Avoid.",
            "+1 MSS per RTT (linear AIMD)",
            "When cwnd >= ssthresh",
            "-",
        ],
        [
            "Timeout (loss)",
            "cwnd = 1 MSS, restart slow start",
            "ACK timer expires",
            "ssthresh = cwnd/2",
        ],
        [
            "3 Dup ACKs (loss)",
            "cwnd = ssthresh + 3 MSS (fast recovery)",
            "3 identical ACKs",
            "ssthresh = cwnd/2",
        ],
        [
            "Fast Retransmit",
            "Retransmit missing segment immediately",
            "3 dup ACKs",
            "-",
        ],
        [
            "Fast Recovery",
            "cwnd = ssthresh (+1 per dup ACK)",
            "After fast retransmit",
            "-",
        ],
    ],
)
code_block("""
 TCP CONGESTION CONTROL -- COMPLETE EXAMPLE:
 =====================================================================
 Initial: cwnd=1, ssthresh=8

 SLOW START phase (cwnd < ssthresh):
   RTT 1: cwnd=1 -> send 1 seg -> 1 ACK -> cwnd=2
   RTT 2: cwnd=2 -> send 2 segs -> 2 ACKs -> cwnd=4
   RTT 3: cwnd=4 -> send 4 segs -> 4 ACKs -> cwnd=8
   cwnd(8) >= ssthresh(8): switch to Congestion Avoidance

 CONGESTION AVOIDANCE (AIMD -- cwnd >= ssthresh):
   RTT 4: cwnd=8  -> +1 per RTT -> cwnd=9
   RTT 5: cwnd=9  -> cwnd=10
   RTT 6: cwnd=10 -> cwnd=11
   ...

 SCENARIO A -- TIMEOUT detected at cwnd=12:
   ssthresh = 12/2 = 6
   cwnd = 1
   Restart Slow Start from cwnd=1.

 SCENARIO B -- 3 DUPLICATE ACKs at cwnd=12 (mild congestion):
   ssthresh = 12/2 = 6
   cwnd = 6 + 3 = 9   (fast recovery -- skip slow start)
   Retransmit the lost segment.
   Each subsequent dup ACK: cwnd++
   On new ACK: cwnd = ssthresh = 6, enter Congestion Avoidance.

 KEY PRINCIPLE: AIMD (Additive Increase, Multiplicative Decrease)
   AI: +1 MSS per RTT during congestion avoidance
   MD: halve cwnd on packet loss signal
   This converges to fair sharing of bandwidth between competing flows.
""")
section("TCP CUBIC (Modern Default)")
body(
    "Most modern OS implementations use <b>TCP CUBIC</b> (default in Linux since 2006). "
    "Instead of purely halving on loss, CUBIC uses a cubic function of time since "
    "the last congestion event to grow cwnd. This achieves higher throughput on "
    "high-bandwidth-delay-product networks (long-distance fiber) while remaining "
    "compatible with legacy TCP Reno networks."
)

# TCP Congestion Control state machine
import engrapha_diagrams.shapes as _pds5


def _make_cc_drawer(lbl: str):
    def draw(sm: Any, x: float, y: float, fill: Any, stroke: Any) -> None:
        sm._add(_pds5.circle(x, y, sm.state_r, fill=fill, stroke=stroke))
        sm._add(
            _pds5.centered_wrapped_label(
                x,
                y,
                lbl,
                max_width=sm.state_r * 1.8,
                font=sm.theme.font_name_bold,
                size=8.5,
                color=sm.theme.state_text,
            )
        )

    return draw


sm_cc = ed.StateMachine(
    width=CW,
    height=200,
    caption="Fig 6: TCP Reno Congestion Control State Machine",
    state_r=35.0,
)
sm_cc.state(
    "SS", "Slow Start", initial=True, custom_draw=_make_cc_drawer("Slow\nStart")
)
sm_cc.state(
    "CA", "Congestion Avoidance", custom_draw=_make_cc_drawer("Congestion\nAvoidance")
)
sm_cc.state("FR", "Fast Recovery", custom_draw=_make_cc_drawer("Fast\nRecovery"))
sm_cc.transition("SS", "CA", label="cwnd >= ssthresh")
sm_cc.transition("SS", "FR", label="3 Dup ACKs")
sm_cc.transition("CA", "SS", label="Timeout")
sm_cc.transition("CA", "FR", label="3 Dup ACKs")
sm_cc.transition("FR", "SS", label="Timeout")
sm_cc.transition("FR", "CA", label="New ACK")
story.extend(sm_cc.as_flowable())

tip(
    "TCP Reno: slow start (exponential) -> CA (linear +1 MSS/RTT). Timeout -> cwnd=1. "
    "3 dup ACKs -> fast recovery (cwnd = ssthresh + 3). "
    "AIMD: additive increase, multiplicative decrease. "
    "TCP CUBIC is the default in modern Linux/Windows -- used in the Internet today."
)
br()


# -----------------------------------------------------------------------------
#  5.7  QUALITY OF SERVICE (QoS)
# -----------------------------------------------------------------------------
chap_box("5.7  Quality of Service (QoS)")
section("What is QoS?")
definition(
    "<b>QoS (Quality of Service):</b> A set of mechanisms and technologies that "
    "allow a network to provide different levels of service to different types of "
    "traffic. QoS ensures that critical or time-sensitive applications (VoIP, "
    "video conferencing) receive the bandwidth, low latency, and low jitter they "
    "need, even when the network is congested."
)

section("QoS Parameters")
info_table(
    ["Parameter", "Definition", "Affected By", "Matters For"],
    [
        [
            "Bandwidth",
            "Maximum data rate (bits per second) available for a flow.",
            "Link capacity, sharing",
            "Video streaming, file transfer",
        ],
        [
            "Delay",
            "Time for a packet to travel from source to destination.",
            "Distance, queuing, processing",
            "VoIP, online gaming",
        ],
        [
            "Jitter",
            "Variation in delay between consecutive packets.",
            "Queuing variability",
            "VoIP, live video -- buffered by jitter buffer",
        ],
        [
            "Packet loss",
            "Fraction of packets dropped in transit.",
            "Buffer overflow, errors",
            "All applications -- TCP retransmits; UDP does not",
        ],
        [
            "Availability",
            "Percentage of time the network is operational.",
            "Hardware reliability",
            "Mission-critical applications",
        ],
    ],
)

section("Traffic Classes")
info_table(
    ["Class", "Examples", "Requirements", "Treatment"],
    [
        [
            "Conversational",
            "VoIP, video calls",
            "Very low delay (<150ms), low jitter",
            "Highest priority, bandwidth guaranteed",
        ],
        [
            "Streaming",
            "YouTube, Netflix",
            "Low jitter (buffered), some loss ok",
            "High priority, rate guaranteed",
        ],
        [
            "Interactive",
            "Web browsing, SSH, gaming",
            "Moderate delay, low loss",
            "Medium priority",
        ],
        [
            "Background",
            "Email, FTP, software updates",
            "Best-effort, delay tolerant",
            "Lowest priority",
        ],
    ],
)

section("QoS Mechanisms")
subsection("Traffic Shaping and Policing")
bullet(
    [
        "<b>Traffic Shaping:</b> Delays packets to conform to a traffic profile (e.g., token bucket). Smooths bursts. Used at edge devices.",
        "<b>Traffic Policing:</b> Drops or marks non-conforming packets at the network ingress. Enforces contracts (SLA).",
    ]
)
subsection("Queuing Disciplines")
info_table(
    ["Algorithm", "Description", "Use Case"],
    [
        [
            "FIFO",
            "First In First Out. No differentiation. Simple.",
            "Best-effort networks",
        ],
        [
            "Priority Queuing",
            "Multiple queues. Higher-priority queues served first.",
            "VoIP + data on same link",
        ],
        [
            "Weighted Fair Queuing (WFQ)",
            "Each flow gets a weighted share of bandwidth.",
            "Fair multi-class sharing",
        ],
        [
            "Class-Based Queuing (CBQ)",
            "Traffic grouped into classes with guaranteed rates.",
            "Enterprise QoS",
        ],
        [
            "Low Latency Queuing (LLQ)",
            "Strict priority for voice + WFQ for data.",
            "VoIP deployments",
        ],
    ],
)
tip(
    "QoS parameters: bandwidth, delay, jitter, packet loss. "
    "VoIP needs: <150ms one-way delay, <30ms jitter, <1% packet loss. "
    "Priority Queuing: voice always goes first. WFQ: fair sharing by weight. "
    "Shaping delays; policing drops."
)
br()


# -----------------------------------------------------------------------------
#  5.8  INTEGRATED SERVICES (IntServ)
# -----------------------------------------------------------------------------
chap_box("5.8  Integrated Services (IntServ)")
section("Overview")
definition(
    "<b>Integrated Services (IntServ):</b> An IETF QoS architecture (RFC 1633) "
    "that provides per-flow resource reservation across the entire network path. "
    "Before sending data, the application requests a specific quality of service "
    "(bandwidth, delay guarantees) using the <b>RSVP</b> signalling protocol. "
    "Every router along the path reserves resources for the flow."
)
bullet(
    [
        "Provides <b>guaranteed service</b>: strict bandwidth and delay bounds.",
        "Each router maintains <b>per-flow state</b> -- resource reservation for every active flow.",
        "Uses <b>RSVP (Resource Reservation Protocol)</b> to signal resource reservations.",
        "Scales poorly: millions of flows on backbone routers = huge per-flow state tables.",
        "Best suited for small, controlled networks (not the global Internet).",
    ]
)

section("RSVP -- Resource Reservation Protocol")
definition(
    "<b>RSVP (RFC 2205):</b> A signalling protocol used by IntServ to reserve "
    "network resources along a path. Receivers (not senders) initiate reservations. "
    "RSVP messages travel hop-by-hop; each router can admit or reject the reservation."
)
bullet(
    [
        "<b>PATH message:</b> Sent by the sender downstream toward the receiver. Carries traffic specification (TSpec: peak rate, average rate, burst size).",
        "<b>RESV message:</b> Sent by the receiver upstream toward the sender. Requests actual resource reservation at each router along the path.",
        "<b>Soft state:</b> Reservations expire unless periodically refreshed. If no refresh: reservation removed automatically.",
        "<b>Admission control:</b> Each router decides whether it has enough resources to admit the new flow.",
    ]
)

# RSVP sequence diagram
seq_rsvp = ed.SequenceDiagram(
    width=CW,
    height=250,
    caption="Fig 4: RSVP signalling -- PATH message downstream, RESV message upstream",
)
seq_rsvp.actor("src", "Sender")
seq_rsvp.actor("r1", "Router 1")
seq_rsvp.actor("r2", "Router 2")
seq_rsvp.actor("dst", "Receiver")
seq_rsvp.message("src", "r1", "PATH (TSpec: 2 Mbps, 50ms)", arrow="solid")
seq_rsvp.message("r1", "r2", "PATH (forwarded)", arrow="solid")
seq_rsvp.message("r2", "dst", "PATH (forwarded)", arrow="solid")
seq_rsvp.message("dst", "r2", "RESV (reserve 2 Mbps)", arrow="dashed")
seq_rsvp.message("r2", "r1", "RESV (admitted, reserve 2 Mbps)", arrow="dashed")
seq_rsvp.message("r1", "src", "RESV (admitted -- path ready)", arrow="dashed")
seq_rsvp.divider("Sender now transmits data at guaranteed 2 Mbps with <50ms delay")
story.extend(seq_rsvp.as_flowable())

info_table(
    ["Feature", "IntServ", "DiffServ"],
    [
        ["Granularity", "Per-flow reservation", "Per-class (aggregate) treatment"],
        [
            "Signalling",
            "RSVP (explicit reservation per flow)",
            "None (just mark packets)",
        ],
        [
            "State in routers",
            "Per-flow state (large for backbone)",
            "Per-class state (small, scalable)",
        ],
        [
            "Guarantee",
            "Hard guarantee (bandwidth + delay)",
            "Relative priority (soft guarantee)",
        ],
        [
            "Scalability",
            "Poor (millions of flows = too much state)",
            "Excellent (few classes)",
        ],
        [
            "Deployment",
            "Small enterprise, lab networks",
            "ISPs, backbone, modern enterprise",
        ],
    ],
)
tip(
    "IntServ = per-flow reservation using RSVP. Strong guarantees. Does not scale to Internet. "
    "DiffServ = per-class marking using DSCP. Scales to Internet. Soft guarantees. "
    "Exam often asks for IntServ vs DiffServ comparison."
)
br()


# -----------------------------------------------------------------------------
#  5.9  DIFFERENTIATED SERVICES (DiffServ)
# -----------------------------------------------------------------------------
chap_box("5.9  Differentiated Services (DiffServ)")
section("Overview")
definition(
    "<b>Differentiated Services (DiffServ, RFC 2474/2475):</b> A scalable QoS "
    "architecture that provides different levels of service to different traffic "
    "classes by marking packets at the network edge and applying predefined "
    "<b>Per-Hop Behaviors (PHBs)</b> at each router. Unlike IntServ, DiffServ "
    "requires NO per-flow signalling and NO per-flow state in core routers."
)
bullet(
    [
        "Packets are <b>marked</b> at the ingress (edge) with a DSCP value in the IP header (6-bit field).",
        "Core routers apply forwarding behaviors based on the DSCP marking only -- no per-flow state.",
        "Scales to the Internet backbone -- only a few traffic classes per router interface.",
        "Provides <b>relative</b> (soft) QoS guarantees, not absolute end-to-end guarantees.",
    ]
)

section("DSCP -- Differentiated Services Code Point")
body(
    "The DSCP is a 6-bit field in the IPv4 ToS byte (or IPv6 Traffic Class). "
    "It defines the forwarding class for the packet."
)
info_table(
    ["DSCP Value", "Class Name", "PHB", "Use Case"],
    [
        [
            "000000 (0)",
            "Default Forwarding (DF)",
            "Best-effort",
            "Normal Internet traffic",
        ],
        [
            "101110 (46)",
            "Expedited Forwarding (EF)",
            "Low delay, low loss, low jitter -- like leased line",
            "VoIP, interactive video",
        ],
        [
            "001010 (10)",
            "AF11 (Assured Forwarding)",
            "Assured, 3 drop prefs",
            "Data class 1, low drop probability",
        ],
        ["010010 (18)", "AF21", "Assured Forwarding", "Data class 2"],
        ["011010 (26)", "AF31", "Assured Forwarding", "Data class 3"],
        ["100010 (34)", "AF41", "Assured Forwarding", "Streaming video"],
        [
            "110000 (48)",
            "CS6",
            "Class Selector",
            "Routing protocols (OSPF, BGP updates)",
        ],
    ],
)
subsection("Per-Hop Behaviors (PHBs)")
bullet(
    [
        "<b>EF (Expedited Forwarding):</b> Treated as highest priority. Departure rate >= arrival rate. Packet gets minimum delay and jitter. Equivalent to a dedicated leased line. Used for VoIP.",
        "<b>AF (Assured Forwarding):</b> Four AF classes (AF1-AF4), each with three drop precedences (low/medium/high). Higher drop precedence = more likely to be dropped under congestion.",
        "<b>BE (Best Effort / DF):</b> Default. No special treatment. Dropped first under congestion.",
        "<b>CS (Class Selector):</b> Backward compatible with older IP Precedence field (3 bits).",
    ]
)
tip(
    "DiffServ DSCP: 6-bit field in IP header. EF=46=101110 (VoIP). AF classes: 4 classes x 3 drop priorities. "
    "BE=0 (default). Core routers use DSCP to decide forwarding behaviour -- no signalling needed. "
    "DiffServ is what real ISPs deploy. IntServ is in labs."
)
br()


# -----------------------------------------------------------------------------
#  5.10  LAN-WAN DESIGN
# -----------------------------------------------------------------------------
chap_box("5.10  LAN-WAN Design and Implementation")
section("Enterprise Network Architecture")
body(
    "A well-designed enterprise network uses a hierarchical model that separates "
    "functions into distinct layers. The most widely adopted is the <b>Cisco "
    "Three-Tier Hierarchical Model</b> (also known as the Three-Layer Model): "
    "Core, Distribution, and Access."
)

section("Three-Tier Hierarchical LAN Design")
info_table(
    ["Layer", "Devices", "Function", "Design Principles"],
    [
        [
            "Core Layer",
            "High-speed Layer 3 switches, backbone routers",
            "High-speed backbone. Forwards traffic between distribution blocks. No policy enforcement.",
            "Redundancy, speed, minimal processing. No packet filtering or QoS marking.",
        ],
        [
            "Distribution Layer",
            "Layer 3 switches, routers",
            "Aggregates access-layer connections. Routing between VLANs. Implements QoS, ACLs, policies.",
            "80/20 rule (80% traffic local). Route summarization. Redundant uplinks to core.",
        ],
        [
            "Access Layer",
            "Layer 2 switches, wireless APs",
            "Directly connects end devices (PCs, phones, printers). VLAN assignment. Port security.",
            "High port density. PoE for IP phones and APs. Spanning Tree. QoS marking.",
        ],
    ],
)

# Three-tier network diagram
hier_net = ed.NetworkDiagram(
    width=CW,
    height=250,
    caption="Fig 5: Three-Tier Hierarchical Enterprise LAN Design",
)
hier_net.node("core1", "Core SW 1", x=180, y=200, kind="switch")
hier_net.node("core2", "Core SW 2", x=320, y=200, kind="switch")
hier_net.node("dist1", "Dist SW 1", x=100, y=130, kind="switch")
hier_net.node("dist2", "Dist SW 2", x=245, y=130, kind="switch")
hier_net.node("dist3", "Dist SW 3", x=400, y=130, kind="switch")
hier_net.node("acc1", "Access SW 1", x=55, y=60, kind="switch")
hier_net.node("acc2", "Access SW 2", x=150, y=60, kind="switch")
hier_net.node("acc3", "Access SW 3", x=245, y=60, kind="switch")
hier_net.node("acc4", "Access SW 4", x=350, y=60, kind="switch")
hier_net.node("acc5", "Access SW 5", x=445, y=60, kind="switch")
hier_net.node("wan", "WAN/Internet", x=500, y=200, kind="cloud")
hier_net.link("core1", "core2")
hier_net.link("core1", "dist1")
hier_net.link("core1", "dist2")
hier_net.link("core2", "dist2")
hier_net.link("core2", "dist3")
hier_net.link("dist1", "acc1")
hier_net.link("dist1", "acc2")
hier_net.link("dist2", "acc3")
hier_net.link("dist3", "acc4")
hier_net.link("dist3", "acc5")
hier_net.link("core2", "wan")
story.extend(hier_net.as_flowable())

section("Structured Cabling")
definition(
    "<b>Structured Cabling:</b> A standardised approach to cabling infrastructure "
    "that supports multiple hardware uses and is designed for long-term use. "
    "Defined by TIA/EIA-568 and ISO/IEC 11801 standards."
)
info_table(
    ["Subsystem", "Description", "Cable Type"],
    [
        [
            "Entrance Facility",
            "Where the building connects to the WAN/carrier.",
            "Fiber, coax from ISP",
        ],
        [
            "Main Distribution Frame (MDF)",
            "Central point of building cabling.",
            "Fiber backbone",
        ],
        [
            "Intermediate Distribution Frame (IDF)",
            "Floor or zone wiring closet.",
            "Fiber or Cat6 backbone",
        ],
        [
            "Horizontal Cabling",
            "From IDF to wall outlets (max 90m + 10m patch).",
            "Cat5e/Cat6/Cat6a UTP",
        ],
        [
            "Work Area",
            "Patch cable from wall outlet to end device.",
            "Cat5e/Cat6 patch cable",
        ],
    ],
)

section("WAN Integration")
bullet(
    [
        "<b>WAN Router:</b> Connects the LAN to the WAN/Internet. Typically at the core or distribution layer.",
        "<b>DMZ (Demilitarized Zone):</b> A separate network segment for publicly accessible servers (web, mail). Protected by firewalls on both sides.",
        "<b>Firewall:</b> Inspects and filters traffic between LAN and WAN based on rules.",
        "<b>NAT (Network Address Translation):</b> Router translates private IP addresses to a public IP for Internet access. Conserves public IPv4 addresses.",
        "<b>VPN (Virtual Private Network):</b> Secure encrypted tunnel over the public Internet connecting remote offices or users.",
    ]
)
tip(
    "Three-tier hierarchy: Access (end devices) -> Distribution (routing/VLAN) -> Core (fast backbone). "
    "Core: speed + redundancy. Distribution: policy + routing. Access: connectivity + VLAN. "
    "Structured cabling max horizontal run = 90m + 10m patch = 100m total."
)
br()


# -----------------------------------------------------------------------------
#  5.11  CONFIGURING TCP/IP
# -----------------------------------------------------------------------------
chap_box("5.11  Configuring TCP/IP")
section("TCP/IP Configuration Parameters")
body(
    "Every network interface that participates in TCP/IP communication must be "
    "configured with the following parameters:"
)
info_table(
    ["Parameter", "Description", "Example"],
    [
        [
            "IP Address",
            "The logical address uniquely identifying this host on the network.",
            "192.168.1.100",
        ],
        [
            "Subnet Mask",
            "Defines the boundary between Network ID and Host ID.",
            "255.255.255.0 (/24)",
        ],
        [
            "Default Gateway",
            "IP address of the router for packets destined outside the subnet.",
            "192.168.1.1",
        ],
        [
            "DNS Server",
            "IP address of the DNS server for hostname-to-IP resolution.",
            "8.8.8.8 (Google DNS)",
        ],
        [
            "DNS Suffix",
            "Default domain name appended when resolving short hostnames.",
            "example.local",
        ],
        [
            "DHCP Server",
            "IP address of the DHCP server if using dynamic assignment.",
            "192.168.1.1",
        ],
    ],
)

section("Static vs Dynamic (DHCP) Configuration")
info_table(
    ["Aspect", "Static IP Configuration", "Dynamic (DHCP) Configuration"],
    [
        [
            "Assignment",
            "Manually entered by administrator",
            "Automatically assigned by DHCP server",
        ],
        [
            "Changes",
            "Must be manually changed if needed",
            "Automatically renewed (lease)",
        ],
        [
            "Consistency",
            "Address is always the same -- predictable",
            "May change on lease expiry",
        ],
        ["Admin overhead", "High for large networks", "Low -- centralised management"],
        [
            "Use for",
            "Servers, printers, network devices, routers",
            "Workstations, laptops, guest devices",
        ],
        [
            "Risk",
            "Duplicate address possible if misconfigured",
            "DHCP server single point of failure",
        ],
    ],
)
code_block("""
 STATIC TCP/IP CONFIGURATION (Windows example):
 =====================================================================
 Via GUI: Control Panel -> Network Connections -> Properties
         -> Internet Protocol Version 4 (TCP/IPv4) -> Properties
         -> Select "Use the following IP address"

 Via Command Line (netsh):
   netsh interface ip set address "Local Area Connection"
         static 192.168.1.100 255.255.255.0 192.168.1.1

   netsh interface ip set dns "Local Area Connection"
         static 8.8.8.8

 STATIC CONFIGURATION ON LINUX:
   /etc/network/interfaces:
   iface eth0 inet static
     address 192.168.1.100
     netmask 255.255.255.0
     gateway 192.168.1.1
     dns-nameservers 8.8.8.8

   Or using ip command:
   ip addr add 192.168.1.100/24 dev eth0
   ip route add default via 192.168.1.1
""")
tip(
    "TCP/IP config: IP address + subnet mask (required) + default gateway (needed for Internet) + DNS server (needed for name resolution). "
    "Subnet mask determines what is local vs remote. "
    "Default gateway is the router's IP on the local subnet. Without it, can only reach local subnet."
)
br()


# -----------------------------------------------------------------------------
#  5.12  IPCONFIG AND PING
# -----------------------------------------------------------------------------
chap_box("5.12  ipconfig and ping -- Diagnostic Commands")
section("ipconfig -- IP Configuration Viewer (Windows)")
definition(
    "<b>ipconfig</b> is a Windows command-line tool that displays and manages the "
    "TCP/IP configuration of network interfaces. It can show current IP settings, "
    "release DHCP leases, renew DHCP leases, and flush the DNS resolver cache."
)
code_block("""
 ipconfig COMMAND REFERENCE:
 =====================================================================
 ipconfig
   Shows: IP Address, Subnet Mask, Default Gateway for each interface.
   Output example:
     Ethernet adapter Local Area Connection:
       Connection-specific DNS Suffix: example.local
       IPv4 Address    : 192.168.1.100
       Subnet Mask     : 255.255.255.0
       Default Gateway : 192.168.1.1

 ipconfig /all
   Shows ALL details including:
   - Physical (MAC) Address: 00-1A-2B-3C-4D-5E
   - DHCP Enabled: Yes/No
   - DHCP Server: 192.168.1.1
   - Lease Obtained: date/time
   - Lease Expires: date/time
   - DNS Servers: 8.8.8.8
   - IPv6 Address (if configured)

 ipconfig /release
   Releases the current DHCP-assigned IP address.
   Sends DHCPRELEASE to the server. Interface loses IP address.

 ipconfig /renew
   Requests a new IP address from the DHCP server (DORA process).
   Used after /release or when DHCP lease has expired.

 ipconfig /flushdns
   Clears the local DNS resolver cache.
   Useful when a DNS record has changed and old cached value is stale.
   Example: website moved to new IP, browser still uses old cached IP.

 ipconfig /displaydns
   Shows the current contents of the DNS resolver cache.

 Linux equivalent: ip addr show  OR  ifconfig  (older)
   ip addr show eth0
   ip route show
""")

section("ping -- Packet Internet Groper")
definition(
    "<b>ping</b> is a network diagnostic tool that tests connectivity between "
    "two hosts by sending ICMP Echo Request packets and waiting for ICMP Echo "
    "Reply packets. The round-trip time (RTT) for each packet is reported."
)
code_block("""
 ping COMMAND REFERENCE:
 =====================================================================
 Basic syntax: ping <destination>
 Destination can be: IP address (192.168.1.1) or hostname (www.google.com)

 WINDOWS EXAMPLE:
   C:\\> ping 192.168.1.1

   Pinging 192.168.1.1 with 32 bytes of data:
   Reply from 192.168.1.1: bytes=32 time=1ms TTL=64
   Reply from 192.168.1.1: bytes=32 time=1ms TTL=64
   Reply from 192.168.1.1: bytes=32 time<1ms TTL=64
   Reply from 192.168.1.1: bytes=32 time=2ms TTL=64

   Ping statistics for 192.168.1.1:
       Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
   Approximate round trip times in milli-seconds:
       Minimum = 0ms, Maximum = 2ms, Average = 1ms

 IMPORTANT FIELDS:
   bytes   = Size of ICMP payload (default 32 bytes on Windows, 56 on Linux)
   time    = Round-trip time (RTT). Higher = more delay. <1ms = excellent.
   TTL     = Time To Live remaining. Original TTL - hops traversed.
             Windows defaults: TTL=128. Linux: TTL=64. Cisco: TTL=255.
             If TTL received is 64: likely 0 hops (Linux direct reply).
             If TTL received is 127: likely 1 hop from a Windows host.

 COMMON ERROR MESSAGES:
   "Request timed out"    = No reply received within timeout.
                            Possible: host down, firewall blocks ICMP, packet lost.
   "Destination unreachable" = ICMP error from a router: no route to destination.
   "TTL expired in transit"  = TTL reached 0. Routing loop or too many hops.
   "General failure"      = Network adapter not ready or no valid configuration.

 USEFUL OPTIONS:
   ping -t 192.168.1.1    (ping continuously until Ctrl+C)
   ping -n 10 192.168.1.1 (send exactly 10 pings)
   ping -l 1472 192.168.1.1 (large payload -- test MTU)
   ping -i 2 192.168.1.1  (set TTL to 2 -- see which router responds)

 LINUX:
   ping -c 4 192.168.1.1     (4 pings then stop)
   ping -s 1472 192.168.1.1  (packet size 1472 bytes)

 TROUBLESHOOTING STEPS WITH PING:
   1. ping 127.0.0.1       -> Test local TCP/IP stack (loopback)
   2. ping <own IP>        -> Test local NIC and driver
   3. ping <default GW>    -> Test local LAN connectivity
   4. ping 8.8.8.8         -> Test Internet connectivity (bypasses DNS)
   5. ping www.google.com  -> Test DNS resolution + Internet
""")

section("tracert / traceroute")
body(
    "<b>tracert</b> (Windows) / <b>traceroute</b> (Linux/Unix) identifies the path "
    "(hop-by-hop) that packets take from source to destination. It uses ICMP with "
    "incrementally increasing TTL values. When TTL=1, the first router decrements "
    "to 0 and sends an ICMP 'Time Exceeded' reply, revealing its IP. TTL is then "
    "incremented to find the next hop, and so on until the destination is reached."
)
code_block("""
 TRACERT EXAMPLE (Windows):
 =====================================================================
 C:\\> tracert 8.8.8.8

 Tracing route to dns.google [8.8.8.8] over a maximum of 30 hops:
   1    <1 ms    <1 ms    <1 ms  192.168.1.1    <- Default gateway (home router)
   2     5 ms     4 ms     5 ms  10.0.0.1       <- ISP's first router
   3    12 ms    11 ms    12 ms  100.64.1.1     <- ISP core router
   4    18 ms    17 ms    18 ms  72.14.206.1    <- Google's edge router
   5    19 ms    18 ms    19 ms  8.8.8.8        <- Destination!

 Each row:
   Hop number | RTT 1 | RTT 2 | RTT 3 | Router's IP address
   3 RTTs because 3 ICMP probes are sent per TTL value.
   * * *  means the router does not respond to ICMP (firewall) -- not necessarily a problem.
""")
tip(
    "ping uses ICMP Echo Request/Reply. Steps: loopback -> own IP -> gateway -> Internet IP -> hostname. "
    "TTL in ping reply = sender's original TTL minus hops. Linux default TTL=64, Windows=128. "
    "tracert reveals each hop -- useful for identifying where delays or failures occur."
)
br()


# -----------------------------------------------------------------------------
#  5.13  STRUCTURED LAN
# -----------------------------------------------------------------------------
chap_box("5.13  Study of Structured LAN")
section("Structured LAN Design Principles")
body(
    "A structured LAN is designed using systematic, documented, and repeatable "
    "principles. It supports current needs and allows for future growth with "
    "minimal disruption."
)
bullet(
    [
        "<b>Hierarchical Design:</b> Core, Distribution, and Access layers with clear roles.",
        "<b>Redundancy:</b> Dual uplinks from access to distribution, dual distribution to core. STP/RSTP prevents loops.",
        "<b>Modularity:</b> Add new buildings or floors without redesigning the whole network.",
        "<b>Scalability:</b> Design accommodates 2-3x growth without major rework.",
        "<b>Security:</b> VLANs segregate traffic. ACLs at distribution layer. 802.1X authentication at access ports.",
        "<b>Manageability:</b> Consistent naming conventions, documented IP addressing, centralised management (SNMP, syslog).",
    ]
)

section("VLANs in Structured LAN")
definition(
    "<b>VLAN (Virtual LAN):</b> A logical subdivision of a physical switch "
    "network. Devices in the same VLAN communicate as if on the same physical "
    "segment, even across multiple switches. VLANs separate broadcast domains "
    "without requiring physical separation."
)
bullet(
    [
        "Each VLAN = separate broadcast domain. Traffic between VLANs requires a Layer 3 router or L3 switch.",
        "<b>Access port:</b> Switch port assigned to ONE VLAN. End devices (PCs, phones) connect here.",
        "<b>Trunk port:</b> Switch port carrying traffic for MULTIPLE VLANs. Uses 802.1Q tagging.",
        "<b>802.1Q VLAN tagging:</b> Adds a 4-byte tag (12-bit VLAN ID) to Ethernet frames on trunk links.",
        "Common VLAN design: VLAN 10=Data, VLAN 20=Voice (VoIP), VLAN 30=Management, VLAN 99=Native.",
    ]
)

section("STP -- Spanning Tree Protocol (IEEE 802.1D)")
definition(
    "<b>STP:</b> Prevents broadcast storms and MAC address table instability "
    "caused by Layer 2 loops in redundant switch topologies. STP blocks redundant "
    "links while keeping them as standby paths. Modern networks use <b>RSTP "
    "(Rapid Spanning Tree Protocol, 802.1W)</b> which converges in <2 seconds."
)
bullet(
    [
        "Elects a <b>Root Bridge</b> (switch with lowest Bridge ID = Priority + MAC).",
        "All ports on root bridge = <b>Designated Ports</b> (forwarding).",
        "Each non-root switch selects a <b>Root Port</b> (best path to root).",
        "Redundant paths are blocked (<b>Alternate Port</b> in RSTP).",
        "If active path fails: blocked port transitions to forwarding (takes 30-50 sec for STP, <2 sec for RSTP).",
    ]
)

section("Structured LAN Example Design")
code_block("""
 STRUCTURED LAN EXAMPLE -- 3-FLOOR OFFICE BUILDING:
 =====================================================================
 Building: 3 floors, ~80 users per floor, 1 data center

 PHYSICAL DESIGN:
   MDF (Main Distribution Frame):  Basement
     - 2x Core L3 switches (redundant pair)
     - WAN router + firewall + servers

   IDF Floor 1 (IDF-F1):
     - 2x Distribution L3 switches
     - Connected to both core switches (2 uplinks per dist. switch)

   IDF Floor 2 (IDF-F2):
     - 2x Distribution L3 switches (same pattern)

   IDF Floor 3 (IDF-F3):
     - 2x Distribution L3 switches

   Access layer per floor:
     - 4x Access L2 switches per floor (48-port each)
     - Connected to BOTH distribution switches (dual uplinks)
     - 802.11ac Wi-Fi APs (PoE-powered)

 VLAN DESIGN:
   VLAN 10:  Data (192.168.10.0/24)   - PCs and laptops
   VLAN 20:  Voice (192.168.20.0/24)  - IP phones (QoS priority)
   VLAN 30:  Guest (192.168.30.0/24)  - Guest Wi-Fi (Internet only)
   VLAN 40:  Servers (10.0.40.0/24)   - Data center servers
   VLAN 99:  Management (10.0.99.0/24)- Switch/AP management

 IP ADDRESSING:
   Core switch pair: 10.0.1.1/30 and 10.0.1.2/30 (point-to-point)
   WAN/firewall outside: 203.0.113.1/30 (public IP from ISP)
   NAT: all internal VLANs NAT to 203.0.113.1 for Internet

 REDUNDANCY:
   STP (RSTP) on all switch links. Core switches = Root Bridges.
   Dual uplinks from access->distribution, distribution->core.
   Active-active or active-standby routing at distribution layer.
""")
tip(
    "Structured LAN: Core -> Distribution -> Access hierarchy. "
    "VLANs separate broadcast domains. 802.1Q tags on trunk ports. "
    "STP prevents loops. RSTP converges in <2 seconds. "
    "Dual uplinks at each layer for redundancy."
)
br()


# -----------------------------------------------------------------------------
#  5.14  INTERNETWORKING DEVICE CONFIGURATION
# -----------------------------------------------------------------------------
chap_box("5.14  Internetworking Device Configuration")
section("Switch Configuration")
body(
    "A managed switch requires configuration for VLANs, trunk ports, STP, "
    "and management access. Cisco IOS command-line is the industry-standard "
    "reference for switch configuration."
)
code_block("""
 SWITCH CONFIGURATION -- KEY COMMANDS (Cisco IOS):
 =====================================================================
 -- Initial access
 Switch> enable                  ! Enter privileged mode
 Switch# configure terminal      ! Enter global config mode

 -- Hostname
 Switch(config)# hostname SW-Access-F1

 -- VLAN creation
 SW-Access-F1(config)# vlan 10
 SW-Access-F1(config-vlan)# name DATA
 SW-Access-F1(config)# vlan 20
 SW-Access-F1(config-vlan)# name VOICE

 -- Access port (end device)
 SW-Access-F1(config)# interface FastEthernet0/1
 SW-Access-F1(config-if)# switchport mode access
 SW-Access-F1(config-if)# switchport access vlan 10
 SW-Access-F1(config-if)# spanning-tree portfast  ! Instant up for PCs

 -- Trunk port (uplink to distribution switch)
 SW-Access-F1(config)# interface GigabitEthernet0/1
 SW-Access-F1(config-if)# switchport mode trunk
 SW-Access-F1(config-if)# switchport trunk allowed vlan 10,20,99

 -- Management IP (on VLAN 99)
 SW-Access-F1(config)# interface vlan 99
 SW-Access-F1(config-if)# ip address 10.0.99.11 255.255.255.0
 SW-Access-F1(config-if)# no shutdown
 SW-Access-F1(config)# ip default-gateway 10.0.99.1

 -- Save config
 SW-Access-F1# copy running-config startup-config
""")

section("Router Configuration")
code_block("""
 ROUTER CONFIGURATION -- KEY COMMANDS (Cisco IOS):
 =====================================================================
 Router> enable
 Router# configure terminal
 Router(config)# hostname R1-Core

 -- Configure LAN interface
 R1-Core(config)# interface GigabitEthernet0/0
 R1-Core(config-if)# ip address 192.168.1.1 255.255.255.0
 R1-Core(config-if)# no shutdown          ! Enable the interface
 R1-Core(config-if)# description LAN-Core-Link

 -- Configure WAN interface
 R1-Core(config)# interface Serial0/0/0
 R1-Core(config-if)# ip address 203.0.113.2 255.255.255.252
 R1-Core(config-if)# no shutdown

 -- Default route to ISP (0.0.0.0 = all destinations)
 R1-Core(config)# ip route 0.0.0.0 0.0.0.0 203.0.113.1

 -- Static route
 R1-Core(config)# ip route 10.0.0.0 255.255.0.0 192.168.1.2

 -- Enable RIP
 R1-Core(config)# router rip
 R1-Core(config-router)# version 2
 R1-Core(config-router)# network 192.168.1.0
 R1-Core(config-router)# no auto-summary

 -- Enable OSPF
 R1-Core(config)# router ospf 1
 R1-Core(config-router)# network 192.168.1.0 0.0.0.255 area 0
 R1-Core(config-router)# network 203.0.113.0 0.0.0.3 area 0

 -- NAT (overload = PAT -- many inside hosts share one outside IP)
 R1-Core(config)# ip nat inside source list 1 interface Serial0/0/0 overload
 R1-Core(config)# access-list 1 permit 192.168.0.0 0.0.255.255
 R1-Core(config)# interface GigabitEthernet0/0
 R1-Core(config-if)# ip nat inside
 R1-Core(config)# interface Serial0/0/0
 R1-Core(config-if)# ip nat outside
""")

section("Hub vs Switch vs Bridge vs Router vs Gateway -- Configuration Summary")
info_table(
    ["Device", "Configurable?", "Key Config Items", "Typical Config Method"],
    [
        ["Hub", "No", "None -- passive signal repeater", "Plug and play. No config."],
        [
            "Bridge",
            "Minimal",
            "None or basic filtering rules. STP auto-negotiated.",
            "Self-learning. Minimal setup.",
        ],
        [
            "Switch",
            "Yes",
            "VLANs, trunk/access ports, STP, port security, LACP, management IP.",
            "CLI (IOS), Web GUI, or SNMP",
        ],
        [
            "Router",
            "Yes",
            "Interface IPs, routing protocols or static routes, NAT, ACLs, DHCP, firewall rules.",
            "CLI (IOS), Web GUI (home), SNMP",
        ],
        [
            "Gateway",
            "Yes",
            "Protocol translation rules, application proxy config.",
            "Vendor-specific management UI",
        ],
    ],
)
tip(
    "Hub: no config -- just plug in. Bridge: auto-learns MAC, minimal config. "
    "Switch: configure VLANs, trunk ports, STP priority. "
    "Router: configure interface IPs, routing protocol, default route, NAT. "
    "All managed devices need management IP and default gateway for remote access."
)
br()


# =============================================================================
#  5.15  QUICK REVISION SUMMARY
# =============================================================================
part_box("UNIT V -- QUICK REVISION SUMMARY")
chap_box("Key Concepts at a Glance")

info_table(
    ["Topic", "Key Point to Remember"],
    [
        [
            "Transport Layer",
            "Process-to-process delivery using port numbers. TCP: reliable, ordered, flow/congestion ctrl. UDP: fast, lightweight, no guarantees.",
        ],
        [
            "Port Ranges",
            "Well-known: 0-1023 (HTTP:80, HTTPS:443, FTP:21, DNS:53, SMTP:25). Registered: 1024-49151. Ephemeral: 49152-65535.",
        ],
        [
            "Socket",
            "IP address + Port number uniquely identifies a process on the Internet. TCP uses 4-tuple (src IP, src port, dst IP, dst port).",
        ],
        [
            "UDP Header",
            "Only 8 bytes: Source Port + Dest Port + Length + Checksum. Connectionless. Use for DNS, DHCP, VoIP, streaming.",
        ],
        [
            "TCP Header",
            "Min 20 bytes. Key fields: Seq No, ACK No, Flags (SYN/ACK/FIN/RST), Window Size. SEQ/ACK track byte stream.",
        ],
        [
            "3-Way Handshake",
            "SYN -> SYN-ACK -> ACK. Establishes TCP connection. Both sides sync ISN. Client: CLOSED->SYN_SENT->ESTABLISHED.",
        ],
        [
            "4-Way Teardown",
            "FIN -> ACK -> FIN -> ACK. TIME_WAIT state lasts 2*MSL to handle late packets.",
        ],
        [
            "TCP Flow Control",
            "Receiver advertises rwnd (receive window). Sender cannot exceed rwnd. Zero window probe when rwnd=0.",
        ],
        [
            "TCP Slow Start",
            "cwnd doubles per RTT until ssthresh. Then congestion avoidance: +1 MSS per RTT (AIMD).",
        ],
        [
            "TCP Congestion",
            "Timeout: cwnd=1, restart slow start, ssthresh=cwnd/2. 3 dup ACKs: fast retransmit, fast recovery, ssthresh=cwnd/2.",
        ],
        [
            "QoS Parameters",
            "Bandwidth, delay, jitter, packet loss, availability. VoIP needs: <150ms delay, <30ms jitter, <1% loss.",
        ],
        [
            "IntServ",
            "Per-flow reservation. RSVP signalling. Hard guarantees. Does not scale to Internet backbone.",
        ],
        [
            "DiffServ",
            "Per-class DSCP marking. No signalling. PHBs: EF=VoIP (low delay), AF=Assured, BE=best-effort. Scalable.",
        ],
        [
            "DSCP EF",
            "DSCP=46 (101110). Expedited Forwarding. Highest priority. Minimum delay and jitter. Used for VoIP.",
        ],
        [
            "Three-Tier LAN",
            "Access (end devices, L2 switch) -> Distribution (VLAN routing, L3 switch) -> Core (high-speed backbone, L3 switch).",
        ],
        [
            "VLAN",
            "Logical broadcast domain within a switch. Access port = 1 VLAN. Trunk port = multiple VLANs (802.1Q tagging).",
        ],
        [
            "STP",
            "Prevents Layer 2 loops. Elects Root Bridge. Blocks redundant ports. STP: 30-50s convergence. RSTP: <2s.",
        ],
        [
            "ipconfig",
            "Windows tool. /all shows MAC, DHCP, DNS. /release releases IP. /renew gets new DHCP IP. /flushdns clears DNS cache.",
        ],
        [
            "ping",
            "ICMP Echo Request/Reply. Tests connectivity. TTL shows hops. Troubleshoot order: loopback->own IP->gateway->Internet IP->hostname.",
        ],
        [
            "tracert",
            "Reveals each router hop using TTL=1,2,3... ICMP Time Exceeded replies expose intermediate router IPs.",
        ],
        [
            "Structured Cabling",
            "MDF (building core) -> IDF (floor closet) -> horizontal (90m max) -> work area (10m max). Total max = 100m.",
        ],
        [
            "Router config",
            "interface ip + no shutdown + static/dynamic routes + NAT. Default route = ip route 0.0.0.0 0.0.0.0 <next-hop>.",
        ],
        [
            "Switch config",
            "vlan create + access port (switchport mode access) + trunk port (switchport mode trunk) + management IP on VLAN interface.",
        ],
    ],
)

highlight(
    "<b>UNIT V EXAM BLUEPRINT:</b>  "
    "2-mark: Define TCP vs UDP. State well-known port numbers. Define socket, VLAN, QoS, DiffServ.  "
    "5-mark: Explain TCP 3-way handshake with diagram. Compare IntServ vs DiffServ. "
    "Explain TCP slow start and congestion avoidance (cwnd graph). "
    "Explain ipconfig and ping with sample output.  "
    "10-mark: Explain TCP header with all fields and their functions. "
    "Explain QoS -- parameters, IntServ (RSVP), DiffServ (DSCP/PHB) comparison. "
    "Explain three-tier LAN design with diagram. "
    "Explain structured LAN with VLANs, STP, and cabling subsystems.",
    YELLOW_CARD,
    YELLOW,
)

# =============================================================================
#  COMBINED 5-UNIT REVISION TABLE
# =============================================================================
br()
part_box("COMPLETE COURSE -- CROSS-UNIT QUICK REFERENCE")
chap_box("All Five Units at a Glance")

info_table(
    ["Unit", "Core Topic", "Most Important Exam Points"],
    [
        [
            "I",
            "Network Fundamentals",
            "OSI 7 layers (PDUs: Bits/Frame/Packet/Segment/Data). TCP/IP 4 layers. "
            "LAN/MAN/WAN. Topologies: mesh links=n(n-1)/2. Service primitives: Request/Indication/Response/Confirm.",
        ],
        [
            "II",
            "Data Link Layer",
            "CRC: append r zeros, XOR divide, append remainder. Bit stuffing: insert 0 after 5 ones. "
            "GBN: Ws=2^n-1, Wr=1. SR: Ws=Wr=2^(n-1). Stop-and-Wait: eta=1/(1+2a). HDLC frame: FLAG|ADDR|CTRL|INFO|FCS|FLAG.",
        ],
        [
            "III",
            "MAC Protocols",
            "Pure ALOHA: S=G*e^(-2G), max 18.4% at G=0.5. Slotted ALOHA: S=G*e^(-G), max 36.8% at G=1.0. "
            "CSMA/CD: min frame 64B, BEB, jam signal. FDDI: 100Mbps dual ring, TTP, 4B/5B encoding.",
        ],
        [
            "IV",
            "Network Layer",
            "Classful: A=/8 (16M hosts), B=/16 (65K hosts), C=/24 (254 hosts). CIDR: block=2^(32-n). "
            "Dijkstra: greedy, non-negative weights. Bellman-Ford: V-1 iterations, handles negatives. "
            "IPv4 header: TTL/Protocol/Frag. IPv6: 128-bit, fixed 40B, no fragmentation by routers.",
        ],
        [
            "V",
            "Transport Layer + LAN Design",
            "TCP: 3-way handshake (SYN/SYN-ACK/ACK), flow ctrl (rwnd), congestion ctrl (cwnd, AIMD). "
            "UDP: 8-byte header, connectionless. DiffServ: DSCP marking, EF=VoIP (46). "
            "Three-tier LAN: Access/Distribution/Core. ipconfig/all. ping troubleshooting order.",
        ],
    ],
)

highlight(
    "<b>EXAM FORMULA SHEET -- ALL UNITS:</b>  "
    "Pure ALOHA: S=G*e^(-2G), max=18.4% at G=0.5.  "
    "Slotted ALOHA: S=G*e^(-G), max=36.8% at G=1.0.  "
    "Stop-and-Wait: eta=1/(1+2a) where a=Tp/Tt.  "
    "Pipelining: if W>=1+2a: eta=1, else eta=W/(1+2a).  "
    "GBN: Ws=2^n-1, Wr=1. SR: Ws=Wr=2^(n-1).  "
    "Hamming: 2^r >= m+r+1.  "
    "CIDR block size: 2^(32-prefix). Hosts=block-2.  "
    "Subnets=2^(borrowed bits). Hosts/subnet=2^(remaining bits)-2.  "
    "Dijkstra: O((V+E)log V), Bellman-Ford: O(V*E).  "
    "TCP cwnd: slow start doubles, CA +1 MSS/RTT, timeout->cwnd=1, 3dup->fast recovery.",
    CARD_DARK,
    CYAN,
)


# =============================================================================
#  BUILD PDF
# =============================================================================
doc = SimpleDocTemplate(
    "CN_Unit5_Notes.pdf",
    pagesize=A4,
    leftMargin=PM,
    rightMargin=PM,
    topMargin=PM,
    bottomMargin=PM,
    title="Computer Networks IT-411 Unit V Notes",
    author="UIT-RGPV (Autonomous) Bhopal",
)
doc.build(story, onFirstPage=page_decor, onLaterPages=page_decor)
print("Generated: CN_Unit5_Notes.pdf")
