"""
DBMS Complete Exam Notes — Full Dark Theme
All text carefully chosen for contrast. No black boxes (no special Unicode glyphs).
All fonts: Helvetica / Courier (built-in ReportLab fonts — fully safe).
"""

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
from reportlab.platypus import Preformatted
import re

PAGE_W, PAGE_H = A4

PAGE_MARGIN = 1.8 * cm
CONTENT_WIDTH = PAGE_W - (PAGE_MARGIN * 2)

CARD_PADDING_V = 10
CARD_PADDING_H = 14

# ── Dark-theme palette ──────────────────────────────────────────────────────
BG = colors.HexColor("#0d1117")  # page background (not used directly)
CARD_DARK = colors.HexColor("#161b22")  # dark card / box
CARD_MID = colors.HexColor("#1c2333")  # medium card
CARD_LIGHT = colors.HexColor("#21262d")  # lighter card

CYAN = colors.HexColor("#79c0ff")
CYAN_BRIGHT = colors.HexColor("#79c0ff")
GREEN = colors.HexColor("#3fb950")
GREEN_CARD = colors.HexColor("#0d2119")
YELLOW = colors.HexColor("#d29922")
YELLOW_CARD = colors.HexColor("#1f1a0a")
ORANGE = colors.HexColor("#e3b341")
ORANGE_CARD = colors.HexColor("#1e1408")
RED = colors.HexColor("#f85149")
RED_CARD = colors.HexColor("#1e0d0d")
PURPLE = colors.HexColor("#bc8cff")
PURPLE_CARD = colors.HexColor("#180d2b")
TEAL = colors.HexColor("#39d353")
TEAL_CARD = colors.HexColor("#091d10")

WHITE = colors.HexColor("#f0f6fc")
WHITE_DIM = colors.HexColor("#9da7b3")
WHITE_BRIGHT = colors.HexColor("#f0f6fc")  # titles

CODE_BG = colors.HexColor("#161b22")
CODE_FG = colors.HexColor("#c9d1d9")
CODE_GREEN = colors.HexColor("#7ee787")
CODE_YELLOW = colors.HexColor("#e3b341")

TABLE_HEADER = colors.HexColor("#1f6feb")
TABLE_ROW1 = colors.HexColor("#161b22")
TABLE_ROW2 = colors.HexColor("#1b2230")
TABLE_BORDER = colors.HexColor("#30363d")


# ── Helpers ─────────────────────────────────────────────────────────────────
def S(name, **kw):
    return ParagraphStyle(name, **kw)


def draw_dark_page(canvas, doc):
    canvas.saveState()

    canvas.setFillColor(BG)
    canvas.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)

    canvas.restoreState()


def page_number(canvas, doc):
    canvas.saveState()

    canvas.setFillColor(WHITE_DIM)
    canvas.setFont("Helvetica", 9)

    page = str(doc.page)

    canvas.drawRightString(PAGE_W - PAGE_MARGIN, PAGE_MARGIN / 2, page)

    canvas.restoreState()


def escape_cell(s):
    s = str(s)
    tags = re.findall(r"</?(?:b|i|u|sub|super|font)(?:\s[^>]*)?>", s)
    ph = "ZPLACEHOLDERZ"
    clean = re.sub(r"</?(?:b|i|u|sub|super|font)(?:\s[^>]*)?>", ph, s)
    clean = clean.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    for tag in tags:
        clean = clean.replace(ph, tag, 1)
    return clean


# ── Style definitions ────────────────────────────────────────────────────────
COVER_H1 = S(
    "CoverH1",
    fontSize=34,
    textColor=WHITE_BRIGHT,
    fontName="Helvetica-Bold",
    alignment=TA_CENTER,
    leading=42,
    spaceAfter=6,
)
COVER_H2 = S(
    "CoverH2",
    fontSize=15,
    textColor=CYAN_BRIGHT,
    fontName="Helvetica",
    alignment=TA_CENTER,
    leading=22,
    spaceAfter=4,
)
COVER_INFO_ST = S(
    "CoverInfo",
    fontSize=10,
    textColor=WHITE_DIM,
    fontName="Helvetica",
    alignment=TA_CENTER,
    leading=16,
)

PART_ST = S(
    "Part",
    fontSize=26,
    textColor=WHITE_BRIGHT,
    fontName="Helvetica-Bold",
    alignment=TA_CENTER,
    leading=34,
)
CHAPTER_ST = S(
    "Chap",
    fontSize=18,
    textColor=WHITE_BRIGHT,
    fontName="Helvetica-Bold",
    alignment=TA_LEFT,
    leading=26,
)
SECTION_ST = S(
    "Sect",
    fontSize=13,
    textColor=CYAN,
    fontName="Helvetica-Bold",
    spaceBefore=12,
    spaceAfter=5,
    leading=20,
)
SUBSECT_ST = S(
    "Sub",
    fontSize=11,
    textColor=CYAN_BRIGHT,
    fontName="Helvetica-Bold",
    spaceBefore=8,
    spaceAfter=4,
    leading=17,
)
BODY_ST = S(
    "Bd",
    fontSize=10,
    textColor=WHITE,
    fontName="Helvetica",
    leading=17,
    spaceAfter=5,
    alignment=TA_JUSTIFY,
)
BODY_BOLD_ST = S(
    "BdB",
    fontSize=10,
    textColor=WHITE_BRIGHT,
    fontName="Helvetica-Bold",
    leading=17,
    spaceAfter=4,
)
BULLET_ST = S(
    "Bul",
    fontSize=10,
    textColor=WHITE,
    fontName="Helvetica",
    leading=16,
    leftIndent=16,
    spaceAfter=3,
)
DEF_ST = S(
    "Def",
    fontSize=10,
    textColor=WHITE,
    fontName="Helvetica",
    leading=16,
    leftIndent=10,
    spaceAfter=4,
    alignment=TA_JUSTIFY,
)
NOTE_ST = S(
    "Note",
    fontSize=9.5,
    textColor=YELLOW,
    fontName="Helvetica-Oblique",
    leading=15,
    leftIndent=6,
    spaceAfter=4,
)
TIP_ST = S(
    "Tip",
    fontSize=9.5,
    textColor=GREEN,
    fontName="Helvetica-Bold",
    leading=15,
    leftIndent=6,
    spaceAfter=5,
)
CODE_ST = S(
    "Code",
    fontSize=8,
    textColor=CODE_FG,
    fontName="Courier",
    leading=13,
    backColor=CODE_BG,
    leftIndent=10,
    rightIndent=10,
    spaceBefore=6,
    spaceAfter=10,
)
ASCII_ST = S(
    "Ascii",
    fontSize=8.5,
    fontName="Courier",
    textColor=CODE_GREEN,
    leading=13,
)

story = []


def add(x):
    story.append(x)


def sp(h=8):
    add(Spacer(1, h))


def rule(c=CYAN, t=0.6):
    add(HRFlowable(width="100%", thickness=t, color=c, spaceAfter=6, spaceBefore=2))


def br():
    add(PageBreak())


def cover_box(text_para, bg=CARD_DARK, pad_v=30, pad_h=18):
    t = Table([[text_para]], colWidths=[CONTENT_WIDTH])
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), bg),
                ("TOPPADDING", (0, 0), (-1, -1), pad_v),
                ("BOTTOMPADDING", (0, 0), (-1, -1), pad_v),
                ("LEFTPADDING", (0, 0), (-1, -1), pad_h),
                ("RIGHTPADDING", (0, 0), (-1, -1), pad_h),
                ("BOX", (0, 0), (-1, -1), 1.5, CYAN),
            ]
        )
    )
    add(t)
    sp(10)


def chap_box(text, bg=CARD_MID, border=CYAN):
    t = Table([[Paragraph(text, CHAPTER_ST)]], colWidths=[CONTENT_WIDTH])
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


def part_box(text, bg=CARD_DARK, border=CYAN):
    t = Table([[Paragraph(text, PART_ST)]], colWidths=[CONTENT_WIDTH])
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


def section(text):
    add(Paragraph(text, SECTION_ST))
    rule(CYAN, 0.5)


def subsection(text):
    add(Paragraph(text, SUBSECT_ST))


def body(text):
    add(Paragraph(text, BODY_ST))


def bold(text):
    add(Paragraph(text, BODY_BOLD_ST))


def bullet(items, color=CYAN):
    hex_color = color.hexval().replace("0x", "")

    for item in items:
        add(Paragraph(f'<font color="#{hex_color}">&#8226;</font> {item}', BULLET_ST))
    sp(4)


def code_block(c):

    style = ParagraphStyle(
        "AsciiBlock",
        parent=ASCII_ST,
        backColor=CARD_DARK,
        borderWidth=1,
        borderColor=CYAN,
        leftIndent=8,
        rightIndent=8,
        spaceBefore=6,
        spaceAfter=10,
    )

    pre = Preformatted(c.strip(), style)

    add(pre)


def note(text):
    add(Paragraph(f"<b>[NOTE]</b> {text}", NOTE_ST))


def tip(text):

    p = Paragraph(f"<b>[EXAM TIP]</b> {text}", TIP_ST)

    t = Table([[p]], colWidths=[CONTENT_WIDTH])

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


def definition(text, bg=CARD_MID, border=CYAN):
    t = Table([[Paragraph(text, DEF_ST)]], colWidths=[CONTENT_WIDTH])
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
        colWidths=[CONTENT_WIDTH],
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


def info_table(headers, rows, hdr_color=TABLE_HEADER):
    th_st = S(
        "TH2",
        fontSize=9,
        textColor=WHITE_BRIGHT,
        fontName="Helvetica-Bold",
        alignment=TA_CENTER,
        leading=14,
    )
    td_st = S("TD2", fontSize=9, textColor=WHITE, fontName="Helvetica", leading=14)
    data = [[Paragraph(escape_cell(h), th_st) for h in headers]]
    for i, row in enumerate(rows):
        data.append([Paragraph(escape_cell(c), td_st) for c in row])
    col_w = (CONTENT_WIDTH) / len(headers)
    t = Table(data, colWidths=[col_w] * len(headers), repeatRows=1)
    style = [
        ("BACKGROUND", (0, 0), (-1, 0), hdr_color),
        ("GRID", (0, 0), (-1, -1), 0.4, TABLE_BORDER),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]
    for i in range(1, len(rows) + 1):
        bg = TABLE_ROW1 if i % 2 == 1 else TABLE_ROW2
        style.append(("BACKGROUND", (0, i), (-1, i), bg))
    t.setStyle(TableStyle(style))
    add(t)
    sp(10)


# ════════════════════════════════════════════════════════════════════════
#  COVER PAGE
# ════════════════════════════════════════════════════════════════════════
sp(20)
cover_box(
    Paragraph("DATABASE MANAGEMENT<br/>SYSTEMS", COVER_H1),
    bg=CARD_DARK,
    pad_v=36,
    pad_h=24,
)
sp(10)
add(Paragraph("Complete Exam Notes with Full PYQ Model Answers", COVER_H2))
add(Paragraph("Unit I &amp; Unit II | 3 / 4 / 10 / 20 Mark Answers", COVER_INFO_ST))
sp(6)
rule(CYAN, 1.5)
sp(8)
add(
    Paragraph(
        "Based on NPTEL/IIT Kharagpur DBMS Course — Silberschatz, Korth &amp; Sudarshan (6th Ed.)",
        COVER_INFO_ST,
    )
)
sp(16)
info_table(
    ["Unit", "Topics Covered"],
    [
        [
            "UNIT I — Basic Concepts",
            "Introduction to DBMS, File System vs DBMS, Advantages, Three-Level Architecture, Data Models, Schemas & Instances, Data Independence, DBA & Designer Functions, Entities, Attributes, Keys, Relationships, ER Diagrams",
        ],
        [
            "UNIT II — Relational Model",
            "Structure of Relational Databases, Domains, Relations, Relational Algebra (all operators with examples), ER Model, Weak Entity Sets, Extended ER Features: Generalization, Specialization, Aggregation",
        ],
        [
            "PYQ Section",
            "Full model answers for all Q1 and Q2 questions — exact questions from your exam paper",
        ],
    ],
)
br()

# ════════════════════════════════════════════════════════════════════════
#  TABLE OF CONTENTS
# ════════════════════════════════════════════════════════════════════════
chap_box("TABLE OF CONTENTS", CARD_MID, PURPLE)
sp(6)
toc_items = [
    ("UNIT I — BASIC CONCEPTS", True),
    ("1.  Introduction to DBMS", False),
    ("2.  File System vs DBMS — Drawbacks & Comparison", False),
    ("3.  Advantages of Database Systems", False),
    ("4.  Three-Level DBMS Architecture", False),
    ("5.  Data Models", False),
    ("6.  Schemas, Instances & Data Independence", False),
    ("7.  Functions of DBA and Designer", False),
    ("8.  Entities, Attributes & Attribute Types", False),
    ("9.  Keys — Super, Candidate, Primary, Foreign", False),
    ("10. Relationships & Cardinality", False),
    ("11. ER Diagrams — Complete Guide", False),
    ("UNIT II — RELATIONAL MODEL", True),
    ("12. Structure of Relational Databases", False),
    ("13. Domains and Relations", False),
    ("14. Relational Algebra — All Operators with Examples", False),
    ("15. Relational Algebra Query Examples", False),
    ("16. ER Model — Constraints & Design Issues", False),
    ("17. Weak Entity Sets", False),
    ("18. Extended ER — Generalization, Specialization, Aggregation", False),
    ("PYQ MODEL ANSWERS — Q1 & Q2", True),
]
for title, is_header in toc_items:
    if is_header:
        add(
            Paragraph(
                f'<b><font color="#58a6ff">{title}</font></b>',
                S(
                    "TOC_H",
                    fontSize=11,
                    fontName="Helvetica-Bold",
                    leading=22,
                    spaceBefore=8,
                    textColor=CYAN,
                ),
            )
        )
    else:
        add(
            Paragraph(
                title,
                S(
                    "TOC_I",
                    fontSize=10,
                    fontName="Helvetica",
                    leading=18,
                    leftIndent=16,
                    textColor=WHITE,
                ),
            )
        )
br()

# ════════════════════════════════════════════════════════════════════════
#  UNIT I
# ════════════════════════════════════════════════════════════════════════
part_box("UNIT I — BASIC CONCEPTS", CARD_DARK, CYAN)

# ── 1. Introduction ─────────────────────────────────────────────────────
chap_box("1. Introduction to DBMS")
section("1.1 What is a Database?")
definition(
    "<b>Database:</b> An organised, shared collection of interrelated data that models some aspect of the real world. It stores facts about entities and the relationships among them in a structured, persistent manner."
)

body(
    "Databases are the backbone of virtually every modern application. Data is stored <i>once</i> and accessed by multiple users/applications simultaneously."
)
bullet(
    [
        "<b>Banking:</b> account transactions, loan records, customer details",
        "<b>Airlines:</b> seat reservations, flight schedules, crew management",
        "<b>Universities:</b> student registration, grades, course enrolment",
        "<b>E-Commerce:</b> product catalogue, orders, inventory, recommendations",
        "<b>Healthcare:</b> patient records, prescriptions, billing",
        "<b>HR Systems:</b> employee records, payroll, tax deductions",
    ]
)

section("1.2 What is a DBMS?")
definition(
    "<b>DBMS (Database Management System):</b> A software system that enables users to define, create, maintain, and control access to a database. It provides a convenient and efficient environment to store and retrieve database information, shielding users from low-level storage details."
)

code_block(
    """
 DBMS = Database + Set of programs to manage it

 Components of a DBMS:
 +-----------------------------------------+
 |           DBMS SOFTWARE                 |
 |  +-------------+  +------------------+  |
 |  | Query       |  | Storage Manager  |  |
 |  | Processor   |  | (File Org,Index) |  |
 |  +-------------+  +------------------+  |
 |  +-------------+  +------------------+  |
 |  | Transaction |  | Authorization &  |  |
 |  | Manager     |  | Integrity Mgr    |  |
 |  +-------------+  +------------------+  |
 +------------------+----------------------+
                    |
 +------------------v----------------------+
 |            DATABASE (Disk Storage)      |
 | [Data Files] [Index Files] [Log Files]  |
 +-----------------------------------------+
"""
)
tip(
    "Always state the full form + definition + list 3-4 real applications. For 3-mark questions this is enough. For 10-mark, add architecture diagram."
)
br()

# ── 2. File System vs DBMS ───────────────────────────────────────────────
chap_box("2. File System vs DBMS — Drawbacks & Comparison")
section("2.1 Drawbacks of File Processing Systems")
body(
    "Before DBMS, data was stored in traditional operating system files. This caused the following major problems:"
)

info_table(
    ["#", "Problem", "Description", "Impact"],
    [
        [
            "1",
            "Data Redundancy & Inconsistency",
            "Same data duplicated in multiple files. Updating one file does not update others.",
            "Wasted storage; data becomes inconsistent across files",
        ],
        [
            "2",
            "Difficulty Accessing Data",
            "A new program must be written for every new type of query. No ad-hoc querying.",
            "High development cost; inflexible system",
        ],
        [
            "3",
            "Data Isolation",
            "Data spread across multiple files with different formats; hard to retrieve together.",
            "Cannot easily join or correlate related data",
        ],
        [
            "4",
            "Integrity Problems",
            "Business rules (e.g., salary > 0) hardcoded in individual programs; easy to miss in new programs.",
            "Constraint violations; corrupt data",
        ],
        [
            "5",
            "Atomicity Problems",
            "System failures can leave the database in an inconsistent state with partial updates.",
            "Fund transfer: debit done, credit fails = money lost",
        ],
        [
            "6",
            "Concurrent Access Problems",
            "Uncontrolled simultaneous updates by multiple users cause lost updates (race condition).",
            "Two users both read balance=100, both deduct 50, final balance=50 not 0",
        ],
        [
            "7",
            "Security Problems",
            "Hard to grant selective access. Either a user sees ALL data or NONE.",
            "Cashier sees confidential salary data",
        ],
    ],
)
tip(
    "This table covers all 7 drawbacks. Each drawback = 1 mark in a 7-mark answer. Always give the fund-transfer example for atomicity."
)

section("2.2 File System vs DBMS — Comparison Table")
info_table(
    ["Feature", "File System", "DBMS"],
    [
        [
            "Data Redundancy",
            "High — data duplicated across files",
            "Low — centralised, single source of truth",
        ],
        [
            "Data Consistency",
            "Poor — no enforcement mechanism",
            "Enforced via integrity constraints",
        ],
        [
            "Data Sharing",
            "Difficult — file-level locking",
            "Controlled concurrent access via transactions",
        ],
        [
            "Data Independence",
            "None — apps tightly coupled to file structure",
            "Physical & Logical independence",
        ],
        [
            "Security",
            "OS-level only (read/write on whole file)",
            "Fine-grained: per-table, per-column, per-user",
        ],
        [
            "Query Language",
            "None — write custom C/Java programs for each query",
            "SQL — powerful, standard, ad-hoc queries",
        ],
        [
            "Recovery after Failure",
            "Manual — complex, error-prone",
            "Automatic via transaction logs and rollback",
        ],
        [
            "Integrity Constraints",
            "Hardcoded in every application program",
            "Declared once in schema; enforced by DBMS engine",
        ],
        [
            "Atomicity",
            "Not guaranteed — partial updates possible",
            "Guaranteed — ACID transactions",
        ],
        [
            "Cost",
            "Low initial setup",
            "Higher initial cost, much lower long-term maintenance",
        ],
    ],
)
br()

# ── 3. Advantages ────────────────────────────────────────────────────────
chap_box("3. Advantages of Database Systems")
section("3.1 Core Advantages")
highlight(
    "<b>Key point:</b> DBMS provides solutions to ALL seven problems of file systems. The advantages below map directly to those drawbacks.",
    YELLOW_CARD,
    YELLOW,
)

info_table(
    ["Advantage", "Explanation", "Example"],
    [
        [
            "Minimal Redundancy",
            "Single copy of data; no duplication across applications",
            "Customer address stored once; all apps use it",
        ],
        [
            "Data Consistency",
            "Integrity constraints prevent invalid states",
            "CHECK salary > 0 prevents negative salary",
        ],
        [
            "Data Sharing & Concurrency",
            "Multiple users access same DB simultaneously; locks prevent conflicts",
            "1000 users booking flights at the same time",
        ],
        [
            "Data Independence",
            "Change physical storage without changing apps (physical independence)",
            "Add B-tree index; no change to application code",
        ],
        [
            "Efficient Data Access",
            "B-tree indexes, hash indexes, query optimizer",
            "Find student by ID in O(log n) not O(n)",
        ],
        [
            "Backup & Recovery",
            "Transaction logs enable automatic roll-forward/rollback after crash",
            "Power failure: DB restored to last consistent state",
        ],
        [
            "Security & Authorization",
            "GRANT/REVOKE, roles, views — fine-grained access control",
            "Student sees own grades only; admin sees all",
        ],
        [
            "Data Integrity",
            "Primary key, foreign key, NOT NULL, CHECK constraints",
            "Cannot insert order for non-existent customer",
        ],
        [
            "Reduced Application Code",
            "No data management code in every app — DBMS handles it",
            "App just sends SQL; no file I/O code needed",
        ],
        [
            "Standard Interface",
            "SQL is an ISO standard — skills and code are portable",
            "MySQL query works on Oracle with minor changes",
        ],
    ],
)
br()

# ── 4. Architecture ──────────────────────────────────────────────────────
chap_box("4. Three-Level DBMS Architecture (ANSI/SPARC)")
section("4.1 Overview")
definition(
    "<b>Three-Level Architecture:</b> The ANSI/SPARC model proposed in 1975 separates a DBMS into three distinct abstraction levels — External, Conceptual, and Internal — to achieve data independence and hide complexity from users."
)

body(
    "The three levels ensure that changes at one level do not force changes at other levels. This separation is the foundation of data independence."
)

code_block(
    """
 THREE-LEVEL DBMS ARCHITECTURE
 =========================================================

  USERS / APPLICATIONS
  User A    User B    User C    User D    User E
    |         |         |         |         |
    v         v         v         v         v
 +--------+--------+--------+--------+--------+
 | View 1 | View 2 | View 2 | View 3 | View 3 |   <-- EXTERNAL LEVEL
 | (HR    | (Payroll| (Mgr  | (Cust  | (Admin |       (User views /
 |  View) |  View) | View) |  View) |  View) |        External Schemas)
 +--------+--------+--------+--------+--------+
                        |
              External/Conceptual Mapping
                        |
          +-------------v------------------+
          |    CONCEPTUAL SCHEMA           |   <-- CONCEPTUAL LEVEL
          |  (All tables, columns,         |       (Logical Schema)
          |   relationships, constraints,  |
          |   keys, foreign keys)          |
          +-------------+------------------+
                        |
              Conceptual/Internal Mapping
                        |
          +-------------v------------------+
          |    INTERNAL / PHYSICAL SCHEMA  |   <-- INTERNAL LEVEL
          |  (File organisation, indexes,  |       (Physical Schema)
          |   B-trees, hashing, block      |
          |   sizes, storage allocation)   |
          +-------------+------------------+
                        |
          +-------------v------------------+
          |     PHYSICAL DATABASE          |
          |     (Disk / SSD Storage)       |
          +--------------------------------+
 =========================================================
"""
)

section("4.2 Description of Each Level")
info_table(
    ["Level", "Also Called", "Description", "Who Works Here"],
    [
        [
            "Level 1 — Internal",
            "Physical Level / Internal Schema",
            "The lowest level. Describes HOW data is physically stored on disk. Covers file organisation, record formats, indexing structures (B-tree, hash), block sizes, access paths, and buffer management. Users and designers never see this level.",
            "System programmers, DBMS engine developers",
        ],
        [
            "Level 2 — Conceptual",
            "Logical Level / Conceptual Schema",
            "Describes WHAT data is stored and the relationships among data. Contains all entity types, their attributes, constraints (primary key, foreign key, NOT NULL, check), and the overall logical structure of the database. Independent of how or where data is stored.",
            "Database designers, DBAs",
        ],
        [
            "Level 3 — External",
            "View Level / External Schema",
            "The highest level, closest to users. Describes only the part of the database relevant to a particular user or user group. Multiple different views can be defined over the same conceptual schema. Sensitive data is hidden by not including it in the view.",
            "End users, application programmers",
        ],
    ],
)

section("4.3 Mappings Between Levels")
info_table(
    ["Mapping", "Direction", "Purpose"],
    [
        [
            "External/Conceptual Mapping",
            "Between view level and logical level",
            "Translates user queries on views into queries on the conceptual schema. Allows multiple different views over the same logical data.",
        ],
        [
            "Conceptual/Internal Mapping",
            "Between logical level and physical level",
            "Translates conceptual schema queries into physical storage access operations. Hides physical storage details from the logical level.",
        ],
    ],
)

section("4.4 Data Independence")
definition(
    "<b>Data Independence:</b> The ability to modify the schema at one level without requiring changes to the schema at the next higher level."
)
info_table(
    ["Type", "Definition", "Example", "Difficulty"],
    [
        [
            "Physical Data Independence",
            "Modify the physical schema (storage) without changing the logical schema or application code.",
            "Add a B-tree index to the instructor table for faster lookups. No change to SQL queries or app code.",
            "Easier to achieve — well-supported by most DBMS",
        ],
        [
            "Logical Data Independence",
            "Modify the logical schema (add/remove tables or columns) without changing external schemas or application programs.",
            "Add a new attribute 'email' to the Student table. Existing views/applications that don't use email continue to work.",
            "Harder to achieve — views and apps may be tightly coupled to schema structure",
        ],
    ],
)
highlight(
    "<b>Which is easier? Physical data independence is easier to achieve.</b><br/>Why? The mapping between conceptual and internal levels is well-defined and handled entirely by the DBMS. Logical data independence is harder because views and application programs may rely on specific table structure, making schema changes potentially breaking.",
    YELLOW_CARD,
    YELLOW,
)
tip(
    "This is directly asked in PYQ e). Always state: Physical is easier. Give the reason: conceptual/internal mapping is handled by DBMS automatically. Logical changes can break views/applications."
)
br()

# ── 5. Data Models ───────────────────────────────────────────────────────
chap_box("5. Data Models")
section("5.1 Definition")
definition(
    "<b>Data Model:</b> A collection of conceptual tools for describing data, data relationships, data semantics, and consistency constraints. It answers: How is data organised and represented in the database?"
)

info_table(
    ["Data Model", "Key Concept", "Representation", "Example Systems"],
    [
        [
            "Relational Model",
            "Data stored in 2D tables (relations). Rows=tuples, Columns=attributes.",
            "Tables with PKs and FKs",
            "MySQL, Oracle, PostgreSQL, SQL Server",
        ],
        [
            "Entity-Relationship Model",
            "Models enterprise as entities and relationships",
            "ER Diagram — rectangles, diamonds, ovals",
            "Design phase tool",
        ],
        [
            "Object-Oriented Model",
            "Data as objects with methods and inheritance",
            "Class hierarchy",
            "db4o, ObjectDB",
        ],
        [
            "Object-Relational Model",
            "Extends relational with OO features",
            "Extended SQL with user types",
            "PostgreSQL, Oracle",
        ],
        [
            "Hierarchical Model",
            "Tree structure — one parent, many children",
            "Inverted tree",
            "IBM IMS (1960s)",
        ],
        [
            "Network Model",
            "Graph structure — records connected by sets",
            "Directed graph",
            "CODASYL (1970s)",
        ],
        [
            "Semi-structured (XML/JSON)",
            "Flexible, self-describing schema",
            "XML/JSON documents",
            "MongoDB, CouchDB",
        ],
    ],
)
br()

# ── 6. Schemas and Instances ─────────────────────────────────────────────
chap_box("6. Schemas, Instances & Data Independence")
section("6.1 Schema vs Instance")
info_table(
    ["Concept", "Definition", "Analogy", "Example"],
    [
        [
            "Schema (Intension)",
            "The logical structure/blueprint of the database. Defined at design time. Rarely changes.",
            "Data type of a variable in a program",
            "instructor(ID char(5), name varchar(20), dept_name varchar(20), salary numeric(8,2))",
        ],
        [
            "Instance (Extension)",
            "The actual content of the database at a particular point in time. Changes with every INSERT/UPDATE/DELETE.",
            "Current value of a variable",
            "The specific rows of data stored in the instructor table right now",
        ],
    ],
)
code_block(
    """
 SCHEMA (Blueprint — stays fixed):
 instructor: | ID | name | dept_name | salary |

 INSTANCE (Data — changes constantly):
 | 10101 | Srinivasan | Comp. Sci. | 65000 |
 | 12121 | Wu         | Finance    | 90000 |
 | 15151 | Mozart     | Music      | 40000 |
 | 22222 | Einstein   | Physics    | 95000 |
   ^-- Added new row? Instance changes. Schema stays same.
"""
)
br()

# ── 7. DBA and Designer ──────────────────────────────────────────────────
chap_box("7. Functions of DBA and Database Designer")
section("7.1 Database Administrator (DBA)")
definition(
    "<b>DBA (Database Administrator):</b> A person or team with central control over the DBMS. Responsible for managing both the DBMS software and the data stored in it."
)

info_table(
    ["Function", "Description"],
    [
        [
            "Schema Definition",
            "Creates the original database schema using DDL (CREATE TABLE, ALTER TABLE)",
        ],
        [
            "Storage Structure & Access Method Definition",
            "Decides physical organisation — file structures, indexes, partitioning, clustering",
        ],
        [
            "Schema & Physical Modification",
            "Modifies schema as requirements evolve without disrupting existing applications",
        ],
        [
            "Granting User Authorization",
            "Manages GRANT and REVOKE privileges; creates roles and user accounts",
        ],
        [
            "Routine Maintenance",
            "Backup schedules, recovery testing, DBMS software updates",
        ],
        [
            "Performance Monitoring",
            "Analyses slow queries, identifies bottlenecks, tunes indexes and buffer pool",
        ],
        [
            "Integrity Constraint Management",
            "Defines and monitors constraints; handles constraint violations",
        ],
        [
            "Security Administration",
            "Manages authentication, encryption, audit trails, intrusion detection",
        ],
    ],
)

section("7.2 Database Designer")
definition(
    "<b>Database Designer:</b> Responsible for identifying the data to be stored in the database and choosing appropriate structures to represent and store this data. Works with users to understand requirements."
)

bullet(
    [
        "Gather requirements through interviews, studying existing documents, use case analysis",
        "Create conceptual design using Entity-Relationship diagrams",
        "Convert ER design to relational schema (logical design / ER-to-relational mapping)",
        "Normalize the relational schema to eliminate redundancy (1NF, 2NF, 3NF, BCNF)",
        "Define views for different user groups (external schemas)",
        "Collaborate with DBA to implement the physical design",
    ]
)
tip(
    "PYQ b) asks for the role of DBA — list 4-5 functions with brief explanations. This earns full 4 marks."
)
br()

# ── 8. Entities and Attributes ───────────────────────────────────────────
chap_box("8. Entities, Attributes & Attribute Types")
section("8.1 Entities")
definition(
    "<b>Entity:</b> A distinguishable real-world object or concept about which data is stored. Can be physical (student, car, book) or conceptual (course, loan, flight)."
)
definition(
    "<b>Entity Set:</b> A collection of entities of the same type sharing the same properties. Example: All students in a university form the STUDENT entity set."
)

section("8.2 Types of Attributes")
info_table(
    ["Type", "Definition", "ER Symbol", "Example"],
    [
        [
            "Simple (Atomic)",
            "Cannot be subdivided further. Single indivisible value.",
            "Single oval",
            "Age, Gender, Roll Number, Student ID",
        ],
        [
            "Composite",
            "Can be subdivided into smaller meaningful sub-attributes.",
            "Oval with child ovals",
            "Full Name = (First Name, Middle Name, Last Name); Address = (Street, City, State, PIN)",
        ],
        [
            "Single-Valued",
            "Holds exactly one value per entity instance.",
            "Single oval",
            "Date of Birth, Aadhaar Number, Employee ID",
        ],
        [
            "Multi-Valued",
            "Can hold multiple values for a single entity instance.",
            "Double oval",
            "Phone Numbers (home, office, mobile); Email Addresses; Degrees held",
        ],
        [
            "Derived",
            "Value can be computed from another stored attribute.",
            "Dashed oval",
            "Age (derived from Date of Birth); Number of Employees (derived by counting)",
        ],
        [
            "NULL",
            "Value is unknown, not applicable, or withheld for this entity.",
            "Not shown specially",
            "Passport Number for person without passport; Middle Name for people with no middle name",
        ],
        [
            "Key Attribute",
            "Uniquely identifies each entity in the entity set.",
            "Underlined text in oval",
            "Roll Number, Employee ID, ISBN",
        ],
    ],
)

code_block(
    """
 ATTRIBUTE TYPES IN ER DIAGRAM NOTATION:
 ============================================================

  Simple/Single-valued:   [ Entity ] ---- ( Attribute )
                                           ^ plain oval

  Composite:              [ Entity ] ---- ( Address )
                                         /    |     \\
                                    (City) (State) (PIN)
                                           ^ child ovals

  Multi-valued:           [ Entity ] ---- (( Phone ))
                                           ^ double oval

  Derived:                [ Entity ] - - -( Age )
                                           ^ dashed oval

  Key attribute:          [ Entity ] ---- ( Roll# )
                                           -----
                                           ^ underlined
 ============================================================
"""
)
tip(
    "PYQ 2a) asks for 4 types of attributes with examples — this section covers all 7 types. Pick any 4: Simple, Composite, Multi-valued, Derived. Draw the oval symbol for each."
)
br()

# ── 9. Keys ───────────────────────────────────────────────────────────────
chap_box("9. Keys — Super, Candidate, Primary, Foreign")
section("9.1 Types of Keys")
definition(
    "<b>Key:</b> An attribute or set of attributes that uniquely identifies a tuple within a relation."
)

info_table(
    [
        "Key Type",
        "Definition",
        "Example (Student table with: Roll#, Name, Aadhaar#, Passport#, Dept)",
    ],
    [
        [
            "Super Key",
            "Any set of attributes that uniquely identifies a tuple. May contain extra unnecessary attributes.",
            "{Roll#}, {Roll#, Name}, {Roll#, Dept}, {Aadhaar#, Name}, {Roll#, Aadhaar#, Passport#}",
        ],
        [
            "Candidate Key",
            "A MINIMAL super key — no proper subset is also a super key. There can be multiple candidate keys.",
            "{Roll#}, {Aadhaar#} — both uniquely identify a student without any extra attribute",
        ],
        [
            "Primary Key",
            "One candidate key CHOSEN by the designer to be the official identifier. Cannot be NULL. Underlined in schema.",
            "Roll# chosen as Primary Key (more stable than Aadhaar#)",
        ],
        [
            "Alternate Key",
            "Candidate keys that were NOT selected as primary key. Also called secondary keys.",
            "Aadhaar# (if Roll# is PK) — it can identify students but was not chosen as PK",
        ],
        [
            "Foreign Key",
            "Attribute(s) in relation R whose values must match the primary key of another relation S. Enforces referential integrity.",
            "dept_name in Student references dept_name (PK) in Department",
        ],
        [
            "Composite Key",
            "A key consisting of two or more attributes together. No single attribute alone is a key.",
            "{First_Name, Last_Name} — neither alone uniquely identifies, but together they might",
        ],
        [
            "Surrogate / Synthetic Key",
            "An artificial key (typically auto-increment integer) not derived from real-world data. Created purely for identification.",
            "student_id INT AUTO_INCREMENT — assigned by DBMS, has no real-world meaning",
        ],
    ],
)

section("9.2 Primary Key vs Super Key — Differentiation (PYQ c)")
highlight(
    "<b>PYQ Direct Answer:</b> Differentiate Primary Key and Super Key with examples",
    CARD_MID,
    CYAN,
)
info_table(
    ["Aspect", "Super Key", "Primary Key"],
    [
        [
            "Definition",
            "Any set of one or more attributes that can uniquely identify a tuple in a relation",
            "A minimal super key selected as the official identifier of tuples in a relation",
        ],
        [
            "Minimality",
            "NOT required to be minimal — can have extra unnecessary attributes",
            "MUST be minimal — removing any attribute loses the uniqueness property",
        ],
        ["Uniqueness", "Guarantees uniqueness", "Guarantees uniqueness"],
        [
            "NULL values",
            "May contain attributes with null values",
            "CANNOT contain null values (NOT NULL implicitly enforced)",
        ],
        [
            "Count per table",
            "Can be many (any superset of a candidate key is a super key)",
            "Exactly ONE primary key per table",
        ],
        [
            "Example table: Student(Roll#, Name, Aadhaar#, Dept)",
            "Super keys: {Roll#}, {Aadhaar#}, {Roll#, Name}, {Roll#, Dept}, {Roll#, Aadhaar#}, {Roll#, Name, Dept}, ...",
            "Primary key: Roll# (chosen from candidate keys; minimal; not null)",
        ],
    ],
)
code_block(
    """
 EXAMPLE: Student(Roll#, Name, Aadhaar#, Passport#, Department)

 Super Keys (ALL of these uniquely identify a student):
   {Roll#}
   {Aadhaar#}
   {Roll#, Name}            <- super key but NOT minimal (Name is extra)
   {Roll#, Department}      <- super key but NOT minimal
   {Roll#, Aadhaar#}        <- super key but NOT minimal
   {Roll#, Name, Aadhaar#}  <- super key but NOT minimal
   ... and many more supersets

 Candidate Keys (MINIMAL super keys):
   {Roll#}       <- minimal: removing Roll# loses uniqueness
   {Aadhaar#}    <- minimal: removing Aadhaar# loses uniqueness
   {Passport#}   <- minimal (but can be null -- problematic)

 Primary Key (ONE candidate key chosen):
   Roll#  <-- chosen because: always present (not null), stable, short

 Foreign Key:
   Department in Student references Department(dept_name) in Dept table
"""
)
br()

# ── 10. Relationships ─────────────────────────────────────────────────────
chap_box("10. Relationships & Cardinality Constraints")
section("10.1 Relationship Definition")
definition(
    "<b>Relationship:</b> An association among two or more entities. A <b>Relationship Set</b> is a set of relationships of the same type. Example: the association between a Student and a Course they are enrolled in."
)

info_table(
    ["Cardinality", "Meaning", "ER Notation", "Example"],
    [
        [
            "One-to-One (1:1)",
            "Each entity in A is associated with at most one entity in B, and vice versa.",
            "Arrow on both sides",
            "Person HAS one Passport; Passport belongs to one Person",
        ],
        [
            "One-to-Many (1:N)",
            "One entity in A is associated with many entities in B; each in B to at most one in A.",
            "Arrow toward N side",
            "One Department HAS many Instructors; each Instructor belongs to one Dept",
        ],
        [
            "Many-to-One (N:1)",
            "Many entities in A associated with one entity in B.",
            "Arrow toward 1 side",
            "Many Students belong to one Department",
        ],
        [
            "Many-to-Many (M:N)",
            "Many entities in A associated with many in B, and vice versa.",
            "No arrows (or arrows on both)",
            "Students ENROL in many Courses; Courses have many Students",
        ],
    ],
)

section("10.2 Participation Constraints")
info_table(
    ["Type", "Meaning", "ER Symbol", "Example"],
    [
        [
            "Total Participation",
            "Every entity in the entity set MUST participate in at least one relationship instance",
            "Double line (===)",
            "Every loan must be associated with at least one customer",
        ],
        [
            "Partial Participation",
            "Some entities may NOT participate in any relationship instance",
            "Single line (---)",
            "Not every customer needs to have a loan",
        ],
    ],
)
br()

# ── 11. ER Diagrams ───────────────────────────────────────────────────────
chap_box("11. ER Diagrams — Complete Guide")
section("11.1 ER Diagram Symbols")
info_table(
    ["Symbol", "Shape", "Represents"],
    [
        ["[ ENTITY ]", "Rectangle", "Strong entity set"],
        ["[[ ENTITY ]]", "Double rectangle", "Weak entity set (no own PK)"],
        ["< RELATION >", "Diamond", "Relationship set (strong)"],
        [
            "<< RELATION >>",
            "Double diamond",
            "Identifying relationship for weak entity",
        ],
        ["( attr )", "Single oval", "Simple or composite attribute"],
        ["(( attr ))", "Double oval", "Multi-valued attribute"],
        ["- - ( attr ) - -", "Dashed oval", "Derived attribute"],
        ["( Roll# )", "Oval with underline on text", "Key attribute (primary key)"],
        ["---", "Single line", "Partial participation or connects components"],
        ["===", "Double line", "Total participation (every entity must participate)"],
        ["-->", "Arrow on line", "Indicates 'one' side in cardinality (one-to-many)"],
    ],
)

section("11.2 University Database ER Diagram")
code_block(
    """
 UNIVERSITY DATABASE -- COMPLETE ER DIAGRAM
 =========================================================
  (dept_name)  (building)  (budget)      (course_id) (title) (credits)
       |            |          |               |         |        |
  +----+------------+----------+----+     +----+---------+--------+--+
  |          DEPARTMENT            |     |           COURSE          |
  +--------------------+-----------+     +------------+--------------+
                       ||                             |
                  <dept_member>                 <pre_req>---(course_id)
                       ||                             |   (self-join)
  (ID) (name) (salary)  |            (course_id)(sec_id)(semester)(year)
    |     |      |      |                 |       |        |        |
  +-+-----+------+------+-+     +---------+-------+--------+--------+-+
  |       INSTRUCTOR       |    |              SECTION               |
  +-----------+------------+    +---+--------------------+-----------+
              |                     |                    |
          <teaches>             <section_of>         <takes>--(grade)
         (semester,yr)              |                    |
              +--------------------+                     |
                                                (ID)(name)(tot_cred)
                                                  |    |       |
                                              +---+----+-------+---+
                                              |       STUDENT      |
                                              +--------------------+

 Legend: +--+ = Entity, <> = Relationship, () = Attribute
         || = Total participation, -- = Partial participation
         -> = One side of cardinality
 =========================================================
"""
)
br()

# ════════════════════════════════════════════════════════════════════════
#  UNIT II
# ════════════════════════════════════════════════════════════════════════
part_box("UNIT II — RELATIONAL MODEL & EXTENDED ER", CARD_DARK, PURPLE)

# ── 12. Structure of Relational Databases ────────────────────────────────
chap_box("12. Structure of Relational Databases", CARD_MID, PURPLE)
section("12.1 Basic Terminology")
definition(
    "<b>Relational Database:</b> A database organised as a collection of relations (tables). The relational model was proposed by E.F. Codd in 1970 and is the most widely used database model today."
)

info_table(
    ["Term", "Mathematical Equivalent", "Definition"],
    [
        [
            "Relation",
            "Set of tuples",
            "A table with rows and columns. The primary data structure in the relational model.",
        ],
        [
            "Tuple",
            "n-tuple (a1, a2, ..., an)",
            "A single row in a table. Represents one entity instance.",
        ],
        [
            "Attribute",
            "Column component Ai",
            "A named column in a table with an associated domain (set of allowed values).",
        ],
        [
            "Domain",
            "Set Di",
            "The set of atomic (indivisible) permitted values for an attribute. E.g., grade domain = {A, B, C, D, F}",
        ],
        [
            "Relation Schema",
            "R = (A1, A2, ..., An)",
            "The structure of a relation: its name and attribute list with types.",
        ],
        [
            "Relation Instance",
            "r(R) at time t",
            "The set of tuples currently stored in the relation at a given moment.",
        ],
        [
            "Degree / Arity",
            "Number of attributes",
            "The number of columns in a relation.",
        ],
        [
            "Cardinality",
            "Number of tuples",
            "The number of rows currently in a relation.",
        ],
    ],
)

code_block(
    """
 ANATOMY OF A RELATION:
 =========================================================
             Attributes (Columns) --> Degree = 4
          +--------+-------------+----------+---------+
          |   ID   |    name     | dept_name|  salary | <-- Schema
          +--------+-------------+----------+---------+
          | 10101  | Srinivasan  | Comp.Sci | 65000   | <--+
          | 12121  | Wu          | Finance  | 90000   |    | Tuples
          | 15151  | Mozart      | Music    | 40000   |    | (Rows)
          | 22222  | Einstein    | Physics  | 95000   | <--+
          | 32343  | El Said     | History  | 60000   |
          +--------+-------------+----------+---------+
          |<---------- Cardinality = 5 rows ---------->|
          Relation name: instructor
 =========================================================

 Properties:
  - All tuples are DISTINCT (no duplicate rows -- it's a set)
  - Tuples are UNORDERED (no top-to-bottom ordering)
  - Attributes are UNORDERED (no left-to-right ordering)
  - All attribute values are ATOMIC (1st Normal Form)
  - NULL = unknown / not applicable / withheld
"""
)
tip(
    "PYQ 2c) asks to explain relational databases with an example. Use the instructor table above. Explain schema vs instance, degree, cardinality, and properties."
)
br()

# ── 13. Domains ───────────────────────────────────────────────────────────
chap_box("13. Domains and Relations")
section("13.1 Formal Definition")
definition(
    "<b>Domain:</b> A domain D is a set of atomic values. Each attribute Ai of a relation schema is associated with a domain dom(Ai), specifying the type and range of valid values for that attribute."
)

code_block(
    """
 FORMAL DEFINITION:
 A relation schema R is defined as R = (A1, A2, ..., An)
 where A1...An are attributes each with a domain dom(Ai).

 Formally: Given domains D1, D2, ..., Dn,
 a relation r is a subset of D1 x D2 x ... x Dn
 (a subset of the Cartesian product of the domains)

 EXAMPLE DOMAINS:
 +---------------------+----------------------------------------+
 | Attribute           | Domain                                 |
 +---------------------+----------------------------------------+
 | Roll#               | Alphanumeric strings of length 10      |
 | salary              | Real numbers > 0 and < 10,000,000      |
 | semester            | {'Fall', 'Spring', 'Winter', 'Summer'} |
 | grade               | {'A+','A','B','C','D','F', NULL}        |
 | year                | Integers in range 1900 to 2100         |
 | dept_name           | Alphabetic strings up to 20 chars      |
 +---------------------+----------------------------------------+

 Referential Integrity:
 Value of foreign key dept_name in instructor
 MUST match some value of dept_name (PK) in department
 OR be NULL (if dept_name allows NULL in instructor)
"""
)

section("13.2 Domain Constraints & Referential Integrity (PYQ 2b)")
highlight(
    "<b>PYQ Direct Answer:</b> Discuss Domain Constraints and Referential Integrity",
    CARD_MID,
    CYAN,
)

bold("i) Referential Integrity:")
definition(
    "<b>Referential Integrity:</b> A constraint that ensures a value appearing in one relation for a given set of attributes ALSO appears in another relation for a certain set of attributes (typically the primary key). It prevents 'dangling references' — foreign key values that point to non-existent entities."
)
code_block(
    """
 EXAMPLE:
 instructor(ID, name, dept_name, salary)
 department(dept_name, building, budget)

 Referential Integrity: dept_name in instructor
 references dept_name (PK) in department.

 VALID:   INSERT INTO instructor VALUES ('99', 'Ali', 'Physics', 70000)
          (because 'Physics' exists in department table)

 INVALID: INSERT INTO instructor VALUES ('100', 'Bob', 'XYZ', 80000)
          (because 'XYZ' does NOT exist in department)
          --> DBMS will REJECT this insert.

 ON DELETE of a department:
   CASCADE:    Delete all instructors in that department
   SET NULL:   Set dept_name to NULL in instructor
   RESTRICT:   Reject the delete if any instructor references it
"""
)

bold("ii) Domain Constraints:")
definition(
    "<b>Domain Constraints:</b> The most basic type of integrity constraint. They specify that the value of each attribute A must be an atomic value from the domain dom(A). They restrict the type of data that can be stored in a column."
)
code_block(
    """
 EXAMPLES OF DOMAIN CONSTRAINTS:

 1. Data type constraint:
    salary NUMERIC(8,2)  -- must be a number with 2 decimal places
    name VARCHAR(20)     -- must be a string up to 20 characters
    dob DATE             -- must be a valid date

 2. NOT NULL constraint:
    name VARCHAR(20) NOT NULL  -- cannot be NULL

 3. CHECK constraint (domain restriction):
    salary NUMERIC(8,2) CHECK (salary > 0)
    semester VARCHAR(6) CHECK (semester IN ('Fall','Spring','Winter','Summer'))
    year NUMERIC(4,0)   CHECK (year >= 1900 AND year <= 2100)

 4. UNIQUE constraint:
    UNIQUE(aadhaar_number)  -- no two students can have the same Aadhaar#

 Domain violations are caught by DBMS at INSERT/UPDATE time.
"""
)
br()

# ── 14. Relational Algebra ────────────────────────────────────────────────
chap_box("14. Relational Algebra — All Operators with Examples", CARD_MID, TEAL)
section("14.1 Overview")
definition(
    "<b>Relational Algebra (RA):</b> A formal, procedural query language for the relational model. Operations take relations as input and return relations as output. It provides the theoretical foundation for SQL."
)
bullet(
    [
        "Six fundamental operators: Select (sigma), Project (pi), Union, Set Difference, Cartesian Product, Rename",
        "Derived operators: Intersection, Natural Join, Theta Join, Division",
        "NOT Turing-machine equivalent — cannot solve all computational problems",
        "Each query input is one or more tables; output is always a table",
    ]
)

section("14.2 Select Operation (sigma)")
definition(
    "<b>Select sigma:</b> Returns only the tuples (rows) that satisfy a given predicate. Works horizontally — filters rows. Equivalent to SQL WHERE clause."
)
highlight(
    "Syntax: sigma predicate(R)   |   Predicate uses: =, !=, <, >, <=, >= and AND, OR, NOT",
    TEAL_CARD,
    TEAL,
)
code_block(
    """
 EXAMPLE 1: sigma dept_name = 'Comp. Sci.' (instructor)
 Returns all tuples from instructor where dept_name = 'Comp. Sci.'

 Input instructor:                   Result:
 | ID    | name      | dept  | sal  | | ID    | name      | dept    | sal  |
 | 10101 | Srinivasan| Comp  | 65000| | 10101 | Srinivasan| Comp.Sci| 65000|
 | 12121 | Wu        | Fin   | 90000| <-- filtered out (Finance)
 | 45565 | Katz      | Comp  | 75000| | 45565 | Katz      | Comp.Sci| 75000|
 | 83821 | Brandt    | Comp  | 92000| | 83821 | Brandt    | Comp.Sci| 92000|

 EXAMPLE 2: sigma salary > 90000 AND dept_name = 'Comp. Sci.' (instructor)
 Result: only Brandt (Comp.Sci. AND salary 92000 > 90000)
"""
)

section("14.3 Project Operation (pi)")
definition(
    "<b>Project pi:</b> Returns only specified columns. Works vertically — selects columns and removes duplicate rows. Equivalent to SQL SELECT with DISTINCT."
)
highlight("Syntax: pi A1, A2, ..., An(R)", TEAL_CARD, TEAL)
code_block(
    """
 EXAMPLE: pi ID, name (instructor)
 Returns only the ID and name columns; drops dept_name and salary.

 Input:                           Result:
 | ID    | name      | dept | sal | | ID    | name      |
 | 10101 | Srinivasan| Comp | 65k | | 10101 | Srinivasan|
 | 12121 | Wu        | Fin  | 90k | | 12121 | Wu        |
 | 45565 | Katz      | Comp | 75k | | 45565 | Katz      |

 NOTE: If two rows have identical values after projection,
       duplicates are automatically REMOVED (set semantics).
"""
)

section("14.4 Union, Set Difference, Intersection")
info_table(
    ["Operation", "Symbol", "Prerequisite", "Result", "SQL"],
    [
        [
            "Union",
            "r UNION s",
            "r and s must be union-compatible (same arity, compatible domains)",
            "All tuples in r OR s, duplicates removed",
            "UNION",
        ],
        [
            "Set Difference",
            "r MINUS s",
            "Union-compatible",
            "Tuples in r but NOT in s",
            "EXCEPT",
        ],
        [
            "Intersection",
            "r INTERSECT s",
            "Union-compatible",
            "Tuples in BOTH r AND s (= r - (r - s))",
            "INTERSECT",
        ],
    ],
)
code_block(
    """
 r = {(CS-101), (CS-315), (CS-319)}   (Fall 2009 courses)
 s = {(CS-101), (CS-347)}              (Spring 2010 courses)

 r UNION s     = {(CS-101), (CS-315), (CS-319), (CS-347)}  -- all unique
 r INTERSECT s = {(CS-101)}                                  -- only common
 r MINUS s     = {(CS-315), (CS-319)}                        -- in r, not s
 s MINUS r     = {(CS-347)}                                   -- in s, not r
"""
)

section("14.5 Cartesian Product (x)")
definition(
    "<b>Cartesian Product:</b> Combines EVERY tuple of r with EVERY tuple of s. If r has n tuples and s has m tuples, the result has n x m tuples. Rarely useful alone; combined with Select to form joins."
)
code_block(
    """
 r x s where r has 12 tuples, s has 50 tuples --> 600 tuples (most meaningless)

 Useful combined with Select:
 sigma instructor.ID = teaches.ID (instructor x teaches)
 This is equivalent to the Natural Join: instructor JOIN teaches
"""
)

section("14.6 Natural Join (JOIN)")
definition(
    "<b>Natural Join:</b> Joins two relations on ALL attributes with the same name. Keeps exactly one copy of the common attributes. Most frequently used join type."
)
code_block(
    """
 EXAMPLE: instructor JOIN department
 (joins on dept_name since it appears in both relations)

 instructor:                 department:
 | ID   | name  | dept |    | dept   | building | budget |
 | 10101| Srini | Comp |    | Comp   | Taylor   | 100000 |
 | 12121| Wu    | Fin  |    | Finance| Painter  | 120000 |

 Result (instructor JOIN department):
 | ID   | name  | dept | building | budget  |
 | 10101| Srini | Comp | Taylor   | 100000  |
 | 12121| Wu    | Fin  | Painter  | 120000  |
 (dept_name appears only once in result)
"""
)

section("14.7 Rename (rho)")
definition(
    "<b>Rename rho:</b> Renames a relation or its attributes. Essential for self-joins where we need two different names for the same table."
)
code_block(
    """
 SYNTAX:
  rho X (E)           -- rename expression E to X
  rho X(A1,A2,...)(E) -- rename E to X with new attribute names

 EXAMPLE -- Find instructors earning more than some Comp.Sci. instructor:
  pi T.name (
    sigma T.salary > S.salary AND S.dept_name = 'Comp. Sci.' (
      rho T (instructor) x rho S (instructor)
    )
  )
  Here T and S are two different aliases for the same instructor table.
"""
)

section("14.8 Summary Table of All RA Operators")
info_table(
    ["Symbol", "Name", "Input", "Example", "SQL Equivalent"],
    [
        [
            "sigma p(r)",
            "Select",
            "1 relation",
            "sigma salary>90000 (instructor)",
            "WHERE salary > 90000",
        ],
        [
            "pi A,B(r)",
            "Project",
            "1 relation",
            "pi name, dept_name (instructor)",
            "SELECT DISTINCT name, dept",
        ],
        [
            "r UNION s",
            "Union",
            "2 compatible",
            "pi name(instructor) UNION pi name(student)",
            "UNION",
        ],
        [
            "r MINUS s",
            "Set Difference",
            "2 compatible",
            "F2009 MINUS S2010",
            "EXCEPT / MINUS",
        ],
        [
            "r x s",
            "Cartesian Product",
            "2 relations",
            "instructor x department",
            "CROSS JOIN",
        ],
        ["rho X(r)", "Rename", "1 relation", "rho T (instructor)", "AS T (alias)"],
        [
            "r INTERSECT s",
            "Intersection",
            "2 compatible",
            "F2009 INTERSECT S2010",
            "INTERSECT",
        ],
        [
            "r JOIN s",
            "Natural Join",
            "2 relations",
            "instructor JOIN department",
            "NATURAL JOIN",
        ],
        [
            "r JOIN-theta s",
            "Theta Join",
            "2 relations",
            "r JOIN r.A < s.B s",
            "JOIN r ON condition",
        ],
        [
            "G F(r)",
            "Aggregation",
            "1 relation",
            "dept G avg(salary)(instructor)",
            "GROUP BY + aggregate",
        ],
    ],
)
br()

# ── 15. RA Queries ────────────────────────────────────────────────────────
chap_box("15. Relational Algebra Query Examples", CARD_MID, TEAL)
section("15.1 Single-Relation Queries")
code_block(
    """
 Schema: Employee(employee_id, first_name, last_name, salary,
                  joining_date, department)
         Incentives(employee_ref_id, incentive_date, incentive_amount)

 ---------------------------------------------------------------
 i) Get employee details whose name is "John":
    sigma first_name = 'John' (Employee)

 ii) Get employee details whose salary > 800000:
    sigma salary > 800000 (Employee)

 iii) Get employee with maximum salary:
    Step 1: Find all salaries LESS THAN the max (not-max salaries):
    Not_Max <- pi T.salary (sigma T.salary < S.salary
                            (rho T(Employee) x rho S(Employee)))

    Step 2: Subtract from all salaries to get only the maximum:
    Max_Salary <- pi salary(Employee) MINUS Not_Max

    Step 3: Get the employee(s) with that salary:
    pi employee_id, first_name, last_name, salary (
        Employee JOIN Max_Salary
    )
    (join on salary attribute)

 iv) Find the average salary of each employee:
    Note: Relational Algebra uses the aggregation operator G
    department G avg(salary) -> avg_salary (Employee)
    This groups by department and computes avg salary per group.

    For per-employee (each employee has one salary, so avg = salary):
    employee_id G avg(salary) -> avg_salary (Employee)
    Result: (employee_id, avg_salary)
"""
)

section("15.2 Multi-Relation Queries")
code_block(
    """
 MORE EXAMPLE QUERIES (University DB):

 1) Names of instructors who teach at least one course:
    pi name (instructor JOIN teaches)

 2) Names of instructors in Physics dept who teach CS-101:
    pi name (sigma dept_name='Physics' AND course_id='CS-101'
                   (instructor JOIN teaches))

 3) Courses offered in BOTH Fall 2009 and Spring 2010:
    pi course_id (sigma semester='Fall' AND year=2009 (section))
    INTERSECT
    pi course_id (sigma semester='Spring' AND year=2010 (section))

 4) Courses offered in Fall 2009 but NOT Spring 2010:
    pi course_id (sigma semester='Fall' AND year=2009 (section))
    MINUS
    pi course_id (sigma semester='Spring' AND year=2010 (section))

 5) Names of students who have taken ALL courses in Comp.Sci.:
    Uses DIVISION operator (advanced):
    pi ID, course_id (takes)
    DIVIDE BY
    pi course_id (sigma dept_name='Comp.Sci.' (course))
"""
)
br()

# ── 16. ER Model — Design Issues ─────────────────────────────────────────
chap_box("16. ER Model — Constraints & Design Issues", CARD_MID, PURPLE)
section("16.1 ER Design Process")
code_block(
    """
 COMPLETE DATABASE DESIGN PROCESS:
 =========================================================
  Real World Requirements
         |
         v
  [1. Requirements Analysis] -- data requirements, functional requirements
         |
         v
  [2. Conceptual Design]     -- ER Diagram (entities, attributes, relationships)
         |
         v
  [3. Logical Design]        -- Map ER to Relational Schema (tables)
         |
         v
  [4. Schema Refinement]     -- Normalize: 1NF -> 2NF -> 3NF -> BCNF
         |
         v
  [5. Physical Design]       -- Indexes, partitioning, storage structures
         |
         v
  [6. Application & Security]-- Views, GRANT/REVOKE, application code
 =========================================================
"""
)

section("16.2 ER to Relational Schema Mapping Rules")
info_table(
    ["ER Construct", "Conversion Rule", "Resulting Schema"],
    [
        [
            "Strong Entity Set E (attrs: a1...an, PK: k)",
            "Create table E. Columns = all attributes. Primary key = k.",
            "E(a1, a2, ..., an) with PK k",
        ],
        [
            "Weak Entity Set W (partial key: d, owner: E with PK k)",
            "Table W has all W attributes PLUS the PK of owner E. PK = (k, d) composite.",
            "W(k, d, w_attrs) with PK (k, d)",
        ],
        [
            "1:1 Relationship R",
            "Add FK of one side into the other table (prefer total participation side).",
            "FK added to one of the two entity tables",
        ],
        [
            "1:N Relationship R",
            "Add FK (primary key of 1-side) into the N-side table. Include relationship attributes.",
            "FK added to N-side table",
        ],
        [
            "M:N Relationship R",
            "Create NEW junction table R with FKs to both PKs. PK = (FK1, FK2). Include relationship attrs.",
            "New table R(pk1, pk2, rel_attrs)",
        ],
        [
            "Multi-valued attribute A of entity E with PK k",
            "Create new table with (k, A) as PK.",
            "New table(k, A)",
        ],
        [
            "Composite attribute",
            "Each component becomes a separate column. The composite itself is NOT stored.",
            "Flattened into individual columns",
        ],
    ],
)
br()

# ── 17. Weak Entity Sets ──────────────────────────────────────────────────
chap_box("17. Weak Entity Sets", CARD_MID, PURPLE)
section("17.1 Definition and Properties")
definition(
    "<b>Weak Entity Set:</b> An entity set that does NOT have sufficient attributes to form a primary key on its own. It depends on an 'owner' (identifying) entity set for its unique identification."
)

info_table(
    ["Feature", "Strong Entity", "Weak Entity"],
    [
        [
            "Primary Key",
            "Complete primary key from own attributes",
            "No complete PK; uses partial key + owner's PK",
        ],
        ["ER Symbol", "Single rectangle", "Double rectangle"],
        ["Existence", "Exists independently", "Cannot exist without its owner entity"],
        [
            "Identifying Relationship",
            "Not needed",
            "Must be in an identifying relationship with owner (double diamond)",
        ],
        [
            "Discriminator",
            "Not applicable",
            "Partial key (dashed underline) distinguishes instances with same owner",
        ],
        [
            "Participation",
            "Can be partial",
            "ALWAYS total participation in identifying relationship",
        ],
        [
            "Example 1",
            "EMPLOYEE (employee_id)",
            "DEPENDENT (employee_ref_id + dependent_name = full key)",
        ],
        [
            "Example 2",
            "LOAN (loan_number)",
            "PAYMENT (loan_number + payment_number = full key)",
        ],
    ],
)

code_block(
    """
 WEAK ENTITY SET ER NOTATION:
 =========================================================

 (loan_number)(amount)   (payment_number)(amount)(date)
      |           |            |        |         |
 +----+-----------+----+  +====+========+=========+====+
 |         LOAN        |  ||         PAYMENT           ||
 |   ____________      |  ||   - - - - - - -           ||
 |   loan_number       +==++   payment_number           ||
 +--------------------+   <<  loan_payment  >>  (double diamond)
 Strong entity             +==========================++
                            (double rectangle)
                            Full PK = (loan_number, payment_number)
 =========================================================

 SQL Schema:
 loan(loan_number, amount)               -- strong entity
 payment(loan_number, payment_number,    -- weak entity
         payment_amount, payment_date,
         PRIMARY KEY (loan_number, payment_number),
         FOREIGN KEY (loan_number) REFERENCES loan)
"""
)
br()

# ── 18. Extended ER ───────────────────────────────────────────────────────
chap_box(
    "18. Extended ER — Generalization, Specialization & Aggregation", CARD_MID, PURPLE
)
section("18.1 Specialization")
definition(
    "<b>Specialization:</b> A TOP-DOWN design process. A higher-level (general) entity set is divided into lower-level (specific) entity sets called subclasses. Each subclass inherits ALL attributes and relationships of the superclass and adds its own distinguishing attributes."
)

code_block(
    """
 SPECIALIZATION EXAMPLE -- EMPLOYEE:

              (ID) (name) (address) (salary)
                |     |      |        |
         +------+-----+------+--------+------+
         |             EMPLOYEE              |
         +--------------------+--------------+
                              |
                           [ISA] <-- triangle
                              |
            +-----------------+-----------------+
            |                                   |
   +--------+--------+              +----------+----------+
   |     OFFICER     |              |       TELLER        |
   | (office_no,     |              | (station_no,        |
   |  office_duties) |              |  hours_per_week)    |
   +-----------------+              +---------------------+

 Each OFFICER and TELLER inherits: ID, name, address, salary
 OFFICER adds: office_no, office_duties
 TELLER adds: station_no, hours_per_week
"""
)

info_table(
    ["Concept", "Definition"],
    [
        [
            "ISA Relationship",
            "The relationship between superclass and subclass. Denoted by triangle labelled ISA. Means 'IS A' -- an Officer IS A Employee.",
        ],
        [
            "Attribute Inheritance",
            "Every attribute and relationship of the superclass is automatically available in all subclasses.",
        ],
        [
            "Disjoint Specialization",
            "An entity can belong to AT MOST ONE subclass (labelled 'd' in triangle). A person is either officer or teller but not both.",
        ],
        [
            "Overlapping Specialization",
            "An entity can belong to MULTIPLE subclasses simultaneously (labelled 'o'). A person can be both a part-time student and part-time employee.",
        ],
        [
            "Total Specialization",
            "EVERY superclass entity must be a member of at least one subclass (double line to ISA). Every vehicle must be a car or truck.",
        ],
        [
            "Partial Specialization",
            "Some superclass entities may not belong to any subclass (single line). Some employees may not be officers or tellers.",
        ],
    ],
)

section("18.2 Generalization")
definition(
    "<b>Generalization:</b> A BOTTOM-UP design process. Multiple specific entity sets that share common features are combined into a single higher-level (generalised) entity set. The common attributes are lifted to the superclass."
)

highlight(
    "<b>Key difference from Specialization:</b> Same final ER diagram structure, but different design direction. Specialization = start general, divide down. Generalization = start specific, merge up. In exams, always state the direction.",
    YELLOW_CARD,
    YELLOW,
)

code_block(
    """
 GENERALIZATION EXAMPLE -- ACCOUNT types:

 BEFORE (two separate, redundant entity sets):
 SAVINGS_ACCOUNT(acc_no, balance, interest_rate)
 CURRENT_ACCOUNT(acc_no, balance, overdraft_limit)
 Common attributes: acc_no, balance --> generalize!

 AFTER (generalized into superclass):
            (acc_no)(balance)
                |       |
         +------+-------+------+
         |         ACCOUNT     |  <-- superclass (generalized)
         +----------+----------+
                    |
                 [ISA]
                    |
       +------------+---------------+
       |                            |
 +-----+--------+           +-------+--------+
 |   SAVINGS    |           |    CURRENT     |
 |(interest_rate)|          |(overdraft_lmt) |
 +--------------+           +----------------+
"""
)

section("18.3 Aggregation")
definition(
    "<b>Aggregation:</b> An abstraction that allows a relationship to be treated as a higher-level entity so that it can participate in another relationship. Solves the problem: ER cannot directly have relationships between relationships."
)

code_block(
    """
 PROBLEM: We need to record that an employee 'works_on' a project
 AND this work assignment 'uses' a particular machine.
 (The machine is associated with the work assignment, not just
  the employee or the project alone.)

 WRONG -- Cannot have relationships between relationships in ER:
 EMPLOYEE --<works_on>-- PROJECT --<uses>-- MACHINE (WRONG!)

 CORRECT -- Use Aggregation:
 +===========================================+  <-- dashed box
 ||                                         ||     (aggregation)
 ||  [EMPLOYEE] ---<works_on>--- [PROJECT]  ||
 ||             (hours, from_date)          ||
 +===========================================+
                     |
                  <uses>
                  (start_date, hours_allocated)
                     |
               [MACHINE]
               (machine_id, machine_type)

 The entire (EMPLOYEE, works_on, PROJECT) relationship is
 treated as a conceptual entity that participates in 'uses'.
"""
)

info_table(
    ["Feature", "Generalization", "Specialization", "Aggregation"],
    [
        [
            "Direction",
            "Bottom-up (merge specific into general)",
            "Top-down (divide general into specific)",
            "Wrapping a relationship as entity",
        ],
        [
            "Purpose",
            "Find and represent common features of multiple entity sets",
            "Distinguish subsets of an entity set with unique features",
            "Allow a relationship to participate in another relationship",
        ],
        [
            "Result",
            "Creates a superclass; subclasses retain unique attrs",
            "Creates subclasses; they inherit superclass attrs",
            "Relationship treated as entity; participates in new relationship",
        ],
        [
            "ER Symbol",
            "ISA triangle (upward arrows)",
            "ISA triangle (downward arrows)",
            "Dashed rectangle around relationship",
        ],
    ],
)
br()

# ════════════════════════════════════════════════════════════════════════
#  PYQ MODEL ANSWERS
# ════════════════════════════════════════════════════════════════════════
part_box("PYQ — FULL MODEL ANSWERS", CARD_DARK, RED)
chap_box("QUESTION 1 — Complete Model Answers", CARD_MID, RED)

section("Q1a) Enlist any four applications of DBMS. [3 Marks]")
highlight(
    "<b>Model Answer (3 marks = 4 applications x brief explanation):</b>",
    CARD_MID,
    CYAN,
)
info_table(
    ["Application Domain", "How DBMS is Used", "Example System"],
    [
        [
            "Banking",
            "Stores customer accounts, processes transactions, maintains loan records, generates statements. Ensures ACID compliance for fund transfers.",
            "Core banking systems like Finacle, Temenos",
        ],
        [
            "Airlines",
            "Manages seat reservations, flight schedules, crew assignments, baggage tracking, ticket sales across multiple channels simultaneously.",
            "Amadeus, Sabre reservation systems",
        ],
        [
            "Universities",
            "Handles student registration, course scheduling, grade recording, transcript generation, fee management, library catalogues.",
            "University ERP systems, Moodle LMS",
        ],
        [
            "E-Commerce / Online Retail",
            "Manages product catalogue, customer orders, inventory levels, payment processing, order tracking, personalised recommendations.",
            "Amazon, Flipkart backend databases",
        ],
        [
            "Healthcare / Hospitals",
            "Stores patient medical records, prescription histories, doctor schedules, billing, insurance claims, diagnostic reports.",
            "Hospital Management Systems (HMS)",
        ],
        [
            "Manufacturing",
            "Tracks production planning, raw material inventory, supply chain, quality control, finished goods, supplier management.",
            "SAP, Oracle ERP manufacturing modules",
        ],
    ],
)
note(
    "Pick any 4 from the table above. Write: Application name + 1-2 lines of explanation. That earns full 3 marks."
)

section("Q1b) What is the role of Database Administrator? [4 Marks]")
highlight("<b>Model Answer:</b>", CARD_MID, CYAN)
body(
    "A <b>Database Administrator (DBA)</b> is a person (or team) with central control and overall authority over the database management system. The DBA's primary role is to manage both the DBMS software and the data stored within it."
)
body("<b>Key Roles and Responsibilities of a DBA:</b>")
info_table(
    ["Role", "Description"],
    [
        [
            "Schema Definition",
            "Creates the original database schema (table structures) using DDL statements. Defines entity types, attribute types, and integrity constraints.",
        ],
        [
            "Storage & Access Method Definition",
            "Decides physical storage structures — which file organisation to use, which attributes to index, and how indexes are structured (B-tree, hash). Aims to optimise query performance.",
        ],
        [
            "Schema Modification",
            "Alters the database schema as business requirements change (e.g., adding new attributes, tables, or constraints) while minimising disruption to existing applications.",
        ],
        [
            "Authorization & Security",
            "Creates user accounts, assigns roles, and manages GRANT/REVOKE privileges. Ensures each user can access only the data they are authorised to see.",
        ],
        [
            "Backup & Recovery",
            "Designs and schedules backup strategies. Tests and executes recovery procedures after system failures to restore data to a consistent state.",
        ],
        [
            "Performance Monitoring & Tuning",
            "Monitors query execution plans, identifies slow queries, adds/removes indexes, adjusts buffer pool sizes and I/O scheduling for optimal performance.",
        ],
        [
            "Integrity Enforcement",
            "Defines domain, entity, and referential integrity constraints. Monitors for violations and resolves constraint issues.",
        ],
        [
            "Routine Maintenance",
            "Applies DBMS software patches and updates. Monitors disk space usage and manages data archiving and purging of obsolete data.",
        ],
    ],
)
tip(
    "4 marks = name 4 specific roles + 1 sentence each. Never just write 'manages database' without specifics."
)

section(
    "Q1c) Differentiate Primary Key and Super Key with appropriate examples. [4 Marks]"
)
highlight("<b>Model Answer:</b>", CARD_MID, CYAN)
info_table(
    ["Aspect", "Super Key", "Primary Key"],
    [
        [
            "Definition",
            "Any attribute or set of attributes that can UNIQUELY IDENTIFY every tuple in a relation. May have redundant attributes.",
            "A MINIMAL super key chosen by the designer as the official identifier of tuples. No redundant attributes.",
        ],
        [
            "Minimality",
            "NOT required to be minimal. May contain extra attributes that are not needed for uniqueness.",
            "MUST be minimal. Removing any attribute from the primary key would lose the uniqueness property.",
        ],
        [
            "NULL Values",
            "Attributes in a super key may be null (if uniqueness is still guaranteed by other attributes in the set)",
            "Primary key attributes CANNOT be null. NOT NULL is automatically enforced.",
        ],
        [
            "Number per table",
            "A table can have many super keys (every superset of a candidate key is a super key)",
            "Exactly ONE primary key per table",
        ],
        [
            "Relationship",
            "Every primary key is a super key. But not every super key is a primary key.",
            "A primary key is always a candidate key (which is itself a minimal super key).",
        ],
    ],
)
body(
    "<b>Example:</b> Consider the Student relation with attributes: Roll#, Name, Aadhaar#, Passport#, Department"
)
code_block(
    """
 Student(Roll#, Name, Aadhaar#, Passport#, Department)

 SUPER KEYS (all sets that guarantee uniqueness):
   {Roll#}                   <- uniquely identifies students
   {Aadhaar#}                <- uniquely identifies students
   {Roll#, Name}             <- still unique (but Name is extra!)
   {Roll#, Department}       <- still unique (but Dept is extra!)
   {Roll#, Name, Aadhaar#}   <- unique but has 2 extra attributes
   {Roll#, Aadhaar#, Passport#, Name, Department}  <- all attributes

 CANDIDATE KEYS (MINIMAL super keys -- cannot remove any attribute):
   {Roll#}     <- remove Roll#? Not unique anymore. So it IS minimal.
   {Aadhaar#}  <- remove Aadhaar#? Not unique anymore. So it IS minimal.
   Note: {Passport#} would be a candidate key too but can be null.

 PRIMARY KEY (one candidate key chosen by designer):
   PRIMARY KEY: Roll#
   Reason: always assigned (not null), stable, short, numeric

 CONCLUSION:
   {Roll#} is both a super key AND a primary key (minimal super key).
   {Roll#, Name} is a super key but NOT a primary key (not minimal).
   All primary keys are super keys. Not all super keys are primary keys.
"""
)

section(
    "Q1d) With a neat sketch, discuss the overall architecture of a DBMS. [10 Marks]"
)
highlight("<b>Model Answer:</b>", CARD_MID, CYAN)
body(
    "A DBMS has a well-defined internal architecture consisting of several interacting components. The overall architecture can be described in terms of how SQL queries are processed from user to disk and back."
)
code_block(
    """
 OVERALL DBMS ARCHITECTURE
 =========================================================

      USERS / APPLICATION PROGRAMS
           |              |
  +--------+-----+  +-----+--------+
  | Naive Users  |  | App Programs |  (forms, web apps)
  | (Forms-based)|  | (SQL embed'd)|
  +--------+-----+  +-----+--------+
           |              |
           +------+-------+
                  |
         +--------v---------+
         | Query Processor  |
         |  +-------------+ |
         |  | DDL Compiler| |  <-- processes CREATE TABLE etc.
         |  +-------------+ |
         |  | DML Compiler| |  <-- processes SELECT/INSERT etc.
         |  | + Query     | |
         |  |  Optimizer  | |  <-- chooses best execution plan
         |  +-------------+ |
         |  | Query       | |
         |  | Evaluation  | |  <-- executes the plan
         |  | Engine      | |
         +--------+--------+
                  |
         +--------v---------+
         | Storage Manager  |
         |  +-----------+   |
         |  |Authorisati|   |  <-- checks GRANT/REVOKE
         |  |on Manager |   |
         |  +-----------+   |
         |  |Integrity  |   |  <-- checks constraints
         |  |Manager    |   |
         |  +-----------+   |
         |  |Transaction|   |  <-- ACID properties
         |  |Manager    |   |
         |  +-----------+   |
         |  |File Manager|  |  <-- disk space allocation
         |  +-----------+   |
         |  |Buffer Mgr |   |  <-- RAM buffer management
         |  +-----------+   |
         +--------+---------+
                  |
     +------------+--------------+
     |                           |
 +---v------+  +-----------+  +--v-------+
 | Data     |  | Index /   |  | Log /    |
 | Files    |  | Hash Files|  | Stats    |
 |(on disk) |  | (on disk) |  | Files    |
 +----------+  +-----------+  +----------+
 =========================================================

 QUERY PROCESSING STEPS:
 1. SQL query arrives at Query Processor
 2. Parser checks syntax; Translator converts to relational algebra
 3. Query Optimizer: generates multiple execution plans, estimates
    cost of each, selects the lowest-cost plan
 4. Execution Engine calls Storage Manager
 5. Storage Manager checks authorization and integrity constraints
 6. Buffer Manager loads required pages from disk into RAM buffer
 7. Results returned up through all layers to the user
"""
)

body("<b>Three Main Components of DBMS:</b>")
info_table(
    ["Component", "Sub-Components", "Responsibility"],
    [
        [
            "Query Processor",
            "DDL Compiler, DML Compiler, Query Optimizer, Query Evaluation Engine",
            "Translates SQL queries to executable operations, optimises query plans for efficiency",
        ],
        [
            "Storage Manager",
            "Authorization Manager, Integrity Manager, Transaction Manager, File Manager, Buffer Manager",
            "Interfaces between high-level queries and physical disk storage; ensures correctness, security, and ACID compliance",
        ],
        [
            "Database on Disk",
            "Data files, Index files, Log files, Statistics files, Data dictionary",
            "Physical persistent storage of all data, metadata, and recovery information",
        ],
    ],
)

section(
    "Q1e) Differentiate between Logical Data Independence and Physical Data Independence. Which is easier to accomplish? Why? [10 Marks]"
)
highlight("<b>Model Answer:</b>", CARD_MID, CYAN)
definition(
    "<b>Data Independence:</b> The ability to modify the schema definition at one level of the three-level architecture without affecting the schema definition at the next higher level."
)

info_table(
    ["Aspect", "Physical Data Independence", "Logical Data Independence"],
    [
        [
            "Definition",
            "Ability to modify the PHYSICAL (internal) schema without requiring changes to the LOGICAL (conceptual) schema or application programs.",
            "Ability to modify the LOGICAL (conceptual) schema without requiring changes to the EXTERNAL (view) schemas or application programs.",
        ],
        [
            "Schema Levels Involved",
            "Physical level to Conceptual level mapping",
            "Conceptual level to External (view) level mapping",
        ],
        [
            "What can be changed",
            "Storage structure, file organisation, indexes, record placement, block sizes, access methods, hashing schemes",
            "Adding/removing tables, adding/removing columns, changing column data types, adding new constraints, splitting or merging tables",
        ],
        [
            "Effect on users",
            "Users are completely unaffected — they never see the internal level",
            "Users may be affected if their views rely on modified parts of the schema",
        ],
        [
            "Example",
            "Change from sequential file to B-tree index for instructor table. All SQL queries still work — no application change needed.",
            "Add new column 'email' to Student table. Existing views that do not include email continue to work (partial logical independence).",
        ],
        [
            "SQL equivalent",
            "Creating/dropping indexes, changing tablespace, partitioning",
            "ALTER TABLE ADD COLUMN; creating new views to present old interface",
        ],
        ["Which is easier?", "EASIER to achieve", "HARDER to achieve"],
    ],
)

bold("Which is easier to accomplish and why?")
highlight(
    """<b>Physical Data Independence is EASIER to achieve.</b>

Reason 1 — Well-defined mapping: The mapping between the conceptual schema and the internal (physical) schema is well-defined and fully managed by the DBMS engine. The application programmer and user never interact with this mapping.

Reason 2 — Transparent to users: Physical changes (adding an index, changing file organisation) are completely transparent to all users. A query executed before and after adding an index returns exactly the same result — only the speed changes.

Reason 3 — DBMS handles it automatically: Modern DBMS systems are specifically designed to handle physical changes without application impact. Adding an index is a routine DBA task that requires zero application changes.

Logical Data Independence is HARDER because:
- Views and application programs may be written to depend on specific table structures.
- If you rename or remove a column, every view and program referencing that column breaks.
- While views can be redefined to mask changes, complex structural changes (e.g., splitting one table into two) require carefully rewriting views and stored procedures.
- The mapping between conceptual and external schema is much more complex and application-specific.""",
    CARD_DARK,
    YELLOW,
)

tip(
    "10 marks: Definition of both types + comparison table (at least 5 rows) + clear answer for 'which is easier' with 3 specific reasons. Never just say 'physical is easier' without explaining WHY."
)
br()

chap_box("QUESTION 2 — Complete Model Answers", CARD_MID, RED)

section(
    "Q2a) List any 4 types of attributes in ER model with an example of each. [3 Marks]"
)
highlight("<b>Model Answer:</b>", CARD_MID, CYAN)
info_table(
    ["Attribute Type", "Definition", "ER Symbol", "Example"],
    [
        [
            "Simple (Atomic)",
            "Cannot be subdivided further. A single, indivisible value.",
            "Single oval (plain)",
            "Age of a student; Gender; Roll Number; Employee ID",
        ],
        [
            "Composite",
            "Can be divided into smaller meaningful sub-attributes that independently have meaning.",
            "Oval with child ovals connected below it",
            "Full Name = (First Name, Middle Name, Last Name); Address = (Street, City, State, PIN Code)",
        ],
        [
            "Multi-Valued",
            "Can hold multiple values simultaneously for a single entity instance.",
            "Double oval (two concentric ovals)",
            "Phone Numbers of an employee (home: 9800000001, mobile: 9800000002); Email Addresses; Degrees held by a person (B.Tech, M.Tech, PhD)",
        ],
        [
            "Derived",
            "The value can be computed or derived from another stored attribute. Not physically stored.",
            "Dashed oval",
            "Age (derived from Date of Birth and current date); Number_of_employees (derived by counting tuples in the Employee table); Experience (derived from joining date)",
        ],
        [
            "NULL",
            "Represents an unknown value or a value that is not applicable for a particular entity.",
            "No special symbol",
            "Passport_Number for students who do not have a passport; Middle_Name for persons without a middle name",
        ],
    ],
)
code_block(
    """
 ER DIAGRAM SHOWING ALL ATTRIBUTE TYPES:
 ================================================
          (emp_id)  (name)   (( phone ))  (- age -)
            |         |           |           |
      +-----+---------+-----------+-----------+----+
      |                  EMPLOYEE                   |
      +----------------------------------------------+
                    |
              (address)  <-- composite
              /    |    \\
         (street)(city)(PIN)
 ================================================
 emp_id    = Simple attribute (atomic, single-valued)
 name      = Simple attribute
 (( phone )) = Multi-valued (double oval) -- can have many phones
 (- age -) = Derived attribute (dashed oval) -- from dob
 address   = Composite attribute -- has sub-parts
"""
)

section("Q2b) Discuss: i) Referential Integrity  ii) Domain Constraints [4 Marks]")
highlight("<b>Model Answer (2 + 2 marks):</b>", CARD_MID, CYAN)

bold("i) Referential Integrity [2 marks]:")
definition(
    "<b>Referential Integrity:</b> An integrity constraint that ensures that a value appearing as a foreign key in one relation MUST also appear as the primary key value in the referenced relation (or be NULL). It prevents orphan references — tuples that reference non-existent data."
)
code_block(
    """
 REFERENTIAL INTEGRITY EXAMPLE:
 ================================================
 student(ID, name, dept_name, tot_cred)
 department(dept_name, building, budget)

 Constraint: dept_name in student REFERENCES dept_name in department

 VALID INSERT:
 INSERT INTO student VALUES ('S001','Rahul','CS',120)
 -> 'CS' exists in department table -> ACCEPTED

 INVALID INSERT:
 INSERT INTO student VALUES ('S002','Priya','XYZ',90)
 -> 'XYZ' does NOT exist in department table -> REJECTED
    Error: Referential integrity violation

 Actions when referenced row is deleted:
 ON DELETE CASCADE  -> delete all referencing rows automatically
 ON DELETE SET NULL -> set FK to NULL in referencing rows
 ON DELETE RESTRICT -> reject the delete operation
 ================================================
"""
)

bold("ii) Domain Constraints [2 marks]:")
definition(
    "<b>Domain Constraints:</b> The simplest form of integrity constraints. They specify that each attribute value must be drawn from a specific domain (set of valid values) — the correct data type, range, or enumerated set."
)
code_block(
    """
 DOMAIN CONSTRAINT EXAMPLES:
 ================================================
 -- Data type constraint:
 salary NUMERIC(8,2)          -- must be numeric
 joining_date DATE            -- must be a valid date
 name VARCHAR(20)             -- must be string, max 20 chars

 -- NOT NULL constraint:
 name VARCHAR(20) NOT NULL    -- cannot be empty/null

 -- CHECK constraint (value range):
 CHECK (salary > 0)           -- salary must be positive
 CHECK (year BETWEEN 1900 AND 2100)
 CHECK (semester IN ('Fall','Spring','Winter','Summer'))
 CHECK (grade IN ('O','A+','A','B+','B','C','F'))

 -- UNIQUE constraint:
 UNIQUE (aadhaar_number)      -- no two rows have same value

 Domain violations are automatically detected by the DBMS
 at INSERT or UPDATE time, before data is written to disk.
 ================================================
"""
)

section("Q2c) Explain about Relational Databases with example. [4 Marks]")
highlight("<b>Model Answer:</b>", CARD_MID, CYAN)
definition(
    "<b>Relational Database:</b> A database that organises data as a collection of relations (tables). Based on the relational model proposed by E.F. Codd in 1970. Each relation has a schema (structure) and an instance (current data). Data is queried using relational algebra or SQL."
)

body("<b>Key concepts:</b>")
code_block(
    """
 RELATIONAL DATABASE EXAMPLE: University Database

 Schema (structure):
 instructor(ID, name, dept_name, salary)
 department(dept_name, building, budget)

 Instance (current data in instructor):
 +-------+-------------+-----------+--------+
 |  ID   |    name     | dept_name | salary |
 +-------+-------------+-----------+--------+
 | 10101 | Srinivasan  | Comp. Sci.| 65000  |
 | 12121 | Wu          | Finance   | 90000  |
 | 15151 | Mozart      | Music     | 40000  |
 | 22222 | Einstein    | Physics   | 95000  |
 | 32343 | El Said     | History   | 60000  |
 +-------+-------------+-----------+--------+
 Degree = 4 attributes, Cardinality = 5 tuples

 Instance (current data in department):
 +-----------+----------+--------+
 | dept_name | building | budget |
 +-----------+----------+--------+
 | Comp. Sci.| Taylor   | 100000 |
 | Finance   | Painter  | 120000 |
 | Physics   | Watson   | 70000  |
 | Music     | Packard  | 80000  |
 | History   | Painter  | 50000  |
 +-----------+----------+--------+
"""
)

info_table(
    ["Property", "Description"],
    [
        [
            "All tuples distinct",
            "No two rows are identical (relational model uses set semantics, not multiset by default)",
        ],
        [
            "Tuples unordered",
            "There is no 'first' or 'last' row -- order has no meaning",
        ],
        [
            "Attributes unordered",
            "Column order has no significance in the relational model",
        ],
        [
            "Atomic values (1NF)",
            "Every attribute value must be indivisible -- no sets or lists within a cell",
        ],
        [
            "Null values allowed",
            "NULL can appear in any attribute (unless NOT NULL is specified) representing unknown/N.A. values",
        ],
        [
            "Primary key uniquely identifies",
            "One attribute (or combination) is chosen as primary key; no two tuples can have same PK value",
        ],
        [
            "Foreign keys link tables",
            "dept_name in instructor references dept_name PK in department -- enforcing referential integrity",
        ],
    ],
)

section("Q2d) Construct an ER Diagram for a Car Insurance Company. [10 Marks]")
highlight(
    "<b>Problem:</b> Customers own one or more cars. Each car has zero or more recorded accidents.",
    CARD_MID,
    CYAN,
)

body("<b>Entities identified:</b>")
bullet(
    [
        "<b>CUSTOMER</b> — people who hold insurance policies",
        "<b>CAR</b> — vehicles owned by customers",
        "<b>ACCIDENT</b> — recorded accidents associated with cars",
    ]
)
body("<b>Relationships identified:</b>")
bullet(
    [
        "<b>OWNS</b> — between CUSTOMER and CAR (1 customer owns 1 or more cars; each car owned by 1 customer)",
        "<b>INVOLVED_IN</b> — between CAR and ACCIDENT (each car has 0 to many accidents; each accident involves at least 1 car)",
    ]
)

code_block(
    """
 CAR INSURANCE COMPANY -- ER DIAGRAM
 =========================================================

  (customer_id)(name)  (address)   (phone) (dob)
       |          |        |          |      |
  +====+==========+========+==========+======+====+
  ||                    CUSTOMER                  ||  <- double line
  ||              ________________________        ||     (total part.
  ||              customer_id             ||      ||      in OWNS)
  +==========================+============+====+==+
                             ||  (total -- every customer
                         <OWNS>   owns at least 1 car)
                             ||
  (license_plate)(year)(model)(make)(colour)
       |            |     |      |      |
  +====+============+=====+======+======+====+
  ||                    CAR                  ||  <- strong entity
  ||              ________________________  ||
  ||              license_plate            ||
  +============+============================+
               |   (partial -- a car may have 0 accidents)
         <INVOLVED_IN>
               |
  (report_no)(date)(location)(damage_amount)(description)
       |        |      |           |             |
  +=====+=======+======+===========+=============+=====+
  ||                   ACCIDENT                        ||
  ||               _______________                     ||
  ||               report_number                       ||
  +=====================================================+

 CARDINALITY:
   CUSTOMER to CAR (via OWNS): 1 customer -- OWNS --> N cars
   CAR to ACCIDENT (via INVOLVED_IN): 1 car -- INVOLVED_IN --> N accidents

 PARTICIPATION:
   CUSTOMER in OWNS: TOTAL (every customer must own at least 1 car)
   CAR in OWNS: TOTAL (every car must be owned by exactly 1 customer)
   CAR in INVOLVED_IN: PARTIAL (a car may have 0 accidents)
   ACCIDENT in INVOLVED_IN: TOTAL (every accident involves at least 1 car)

 KEY ATTRIBUTES:
   CUSTOMER: customer_id (Primary Key)
   CAR: license_plate (Primary Key)
   ACCIDENT: report_number (Primary Key)

 =========================================================

 RELATIONAL SCHEMA (ER to Tables):
   customer(customer_id, name, address, phone, dob)
   car(license_plate, year, model, make, colour, customer_id)
     -- customer_id FK references customer
   accident(report_number, date, location, damage_amount, description)
   involved_in(license_plate, report_number)
     -- M:N relationship table
     -- FK license_plate references car
     -- FK report_number references accident
"""
)
tip(
    "10 marks for ER diagram: Draw entities (rectangles) + attributes (ovals) + relationships (diamonds) + cardinality labels (1, N, M) + participation (single/double lines) + underline primary keys. Always provide the relational schema mapping too."
)

section(
    "Q2e) Relational Algebra Queries on Employee and Incentives schemas. [10 Marks]"
)
highlight(
    "<b>Schema:</b> Employee(employee_id, first_name, last_name, salary, joining_date, department) | Incentives(employee_ref_id, incentive_date, incentive_amount)",
    CARD_MID,
    CYAN,
)

code_block(
    """
 RELATIONAL ALGEBRA QUERIES:
 =========================================================

 i) Get employee details whose name is "John":
 -------------------------------------------------------
 sigma first_name = 'John' (Employee)

 This uses the SELECT operator (sigma) to filter rows.
 Returns: All columns (employee_id, first_name, last_name,
          salary, joining_date, department)
 where first_name = 'John'

 SQL equivalent: SELECT * FROM Employee WHERE first_name = 'John';

 =========================================================
 ii) Get employee details whose Salary > 800000:
 -------------------------------------------------------
 sigma salary > 800000 (Employee)

 Returns all columns of employees whose salary exceeds 800000.

 SQL equivalent: SELECT * FROM Employee WHERE salary > 800000;

 =========================================================
 iii) Get employee details whose salary is maximum:
 -------------------------------------------------------
 Step 1: Find all salaries that are NOT maximum.
         A salary is not the maximum if there EXISTS
         another salary that is greater than it.

  Not_Maximum_Salary <- pi T.salary (
      sigma T.salary < S.salary (
          rho T(Employee) x rho S(Employee)
      )
  )
  (T and S are two aliases for the same Employee table.
   For each pair (T, S) where T.salary < S.salary,
   T.salary is NOT the maximum.)

 Step 2: Maximum salary = All salaries MINUS Not_Maximum_Salary

  Max_Salary <- pi salary (Employee) MINUS Not_Maximum_Salary

 Step 3: Get full employee record(s) with that maximum salary.

  Result <- Employee JOIN Max_Salary
  (natural join on salary attribute)

 SQL equivalent:
  SELECT * FROM Employee WHERE salary = (SELECT MAX(salary) FROM Employee);

 =========================================================
 iv) Find the average salary of each employee:
 -------------------------------------------------------
 Note: Since each employee has ONE salary value, the
 "average salary of each employee" equals their own salary.
 If the question means "average salary grouped by department":

 A) Average salary per employee:
    employee_id G avg(salary) -> avg_salary (Employee)
    (G is aggregation operator: GROUP BY employee_id)
    Result: (employee_id, avg_salary) -- same as their salary

 B) Average salary per department (more meaningful):
    department G avg(salary) -> avg_salary (Employee)
    Result: (department, avg_salary)

 C) Overall average salary:
    G avg(salary) -> overall_avg (Employee)
    (No grouping -- computes single avg over all tuples)

 SQL equivalents:
 A) SELECT employee_id, AVG(salary) FROM Employee GROUP BY employee_id;
 B) SELECT department, AVG(salary) FROM Employee GROUP BY department;
 C) SELECT AVG(salary) AS overall_avg FROM Employee;
 =========================================================
"""
)
tip(
    "10 marks: Write each RA expression clearly. For maximum salary (iii), you MUST show the 3-step approach using self-join + set difference. For average (iv), use the G (aggregation) operator. Always write the SQL equivalent for extra clarity."
)
br()

# ── Quick Revision ─────────────────────────────────────────────────────────
part_box("QUICK REVISION — KEY CONCEPTS AT A GLANCE", CARD_DARK, GREEN)
chap_box("Quick Revision Summary", CARD_MID, GREEN)
info_table(
    ["Concept", "One-Line Definition", "Key Points to Remember"],
    [
        [
            "DBMS",
            "Software managing creation, retrieval, update, deletion of DB data",
            "Solves 7 file system problems; provides ACID, SQL, security",
        ],
        [
            "Three-Level Architecture",
            "External / Conceptual / Internal levels of abstraction",
            "Physical indep. = easier; Logical indep. = harder",
        ],
        [
            "Data Independence",
            "Change schema at one level without affecting higher levels",
            "Physical: storage changes; Logical: table structure changes",
        ],
        [
            "Schema vs Instance",
            "Schema = blueprint (stable); Instance = actual data (changes)",
            "Like data type vs current value of a variable",
        ],
        [
            "Super Key",
            "Any set of attributes uniquely identifying a tuple",
            "Not necessarily minimal; includes all candidate keys and their supersets",
        ],
        [
            "Primary Key",
            "Minimal super key chosen as official identifier",
            "One per table; cannot be NULL; underlined in schema",
        ],
        [
            "Foreign Key",
            "Attribute referencing PK of another table",
            "Enforces referential integrity; prevents orphan references",
        ],
        [
            "ER Model",
            "Conceptual design using entities, attributes, relationships",
            "Rectangle=entity, Diamond=relationship, Oval=attribute",
        ],
        [
            "Weak Entity",
            "No own PK; depends on owner entity",
            "Double rectangle; double diamond; partial key + owner PK",
        ],
        [
            "Specialization",
            "Top-down: divide general entity into subclasses",
            "ISA triangle; subclasses inherit all superclass attributes",
        ],
        [
            "Generalization",
            "Bottom-up: merge specific entities into superclass",
            "Same ER structure as specialization; different design direction",
        ],
        [
            "Aggregation",
            "Treat a relationship as entity for another relationship",
            "Dashed box around relationship; solves relationship-in-relationship problem",
        ],
        ["RA Select (sigma)", "Filter rows by predicate", "SQL WHERE clause"],
        ["RA Project (pi)", "Select specific columns", "SQL SELECT DISTINCT"],
        [
            "RA Natural Join",
            "Join on common attributes; one copy of common cols",
            "Most efficient common join; SQL NATURAL JOIN",
        ],
        [
            "Domain Constraints",
            "Values must be from valid domain/type/range",
            "CHECK, NOT NULL, data type enforcement",
        ],
        [
            "Referential Integrity",
            "FK values must match PK in referenced table",
            "ON DELETE CASCADE / SET NULL / RESTRICT",
        ],
    ],
)

highlight(
    """<b>EXAM WRITING STRATEGY:</b>
  3-mark questions:  Definition (1 line) + 2 key points + 1 example = full marks
  4-mark questions:  Definition + table/list of 4 points + brief example
  10-mark questions: Definition + Theory + ASCII diagram + comparison table + worked examples
  20-mark questions: All of the above + multiple examples + advantages/disadvantages + design trade-offs

  ALWAYS: Draw diagrams. Label everything. Write SQL equivalents next to RA. Show output of example queries.
  NEVER: Just copy-paste definitions without context. Diagrams without labels. RA without explaining steps.""",
    YELLOW_CARD,
    YELLOW,
)

# ── Build PDF ────────────────────────────────────────────────────────────────
doc = SimpleDocTemplate(
    "DBMS_Complete_Dark_ExamNotes.pdf",
    pagesize=A4,
    leftMargin=PAGE_MARGIN,
    rightMargin=PAGE_MARGIN,
    topMargin=PAGE_MARGIN,
    bottomMargin=PAGE_MARGIN,
    title="DBMS Complete Exam Notes — Dark Theme",
    author="Based on NPTEL IIT Kharagpur",
)


def page_decor(canvas, doc):
    draw_dark_page(canvas, doc)
    page_number(canvas, doc)


doc.build(story, onFirstPage=page_decor, onLaterPages=page_decor)
print("PDF built successfully!")
