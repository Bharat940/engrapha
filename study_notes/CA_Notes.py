"""
Computer Architecture — Unit I & II Complete Exam Notes (Dark Theme)
UIT-RGPV Subject IT404 | Full PYQ Model Answers
Safe fonts: Helvetica / Courier only. No Unicode glyphs.
Web images with ASCII fallbacks.
Run: python ca_unit12.py
Output: CA_Unit1_2_ExamNotes.pdf
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
from reportlab.platypus import Preformatted, Image
from io import BytesIO
import re
import requests
import os

PAGE_W, PAGE_H = A4
PM = 1.8 * cm
CW = PAGE_W - 2 * PM

ASSET_DIR = "asset_images"

IMAGES = {
    "von_neumann.png": "https://upload.wikimedia.org/wikipedia/commons/3/3a/VonNeumann-01.png",

    "harvard_architecture.webp": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Harvard_architecture.svg/800px-Harvard_architecture.svg.png",

    "cpu_block.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/CPU_block_diagram.svg/800px-CPU_block_diagram.svg.png",

    "ripple_adder.jpeg": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/4-bit_ripple_carry_adder.svg/800px-4-bit_ripple_carry_adder.svg.png",

    "alu_block.png": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/ALU_block.gif/800px-ALU_block.gif",

    "ieee754.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/Float_example.svg/800px-Float_example.svg.png",

    "hardwired_cu.png": "https://upload.wikimedia.org/wikipedia/commons/8/8f/Hardwired_control_unit.png",

    "microprogrammed_cu.png": "https://upload.wikimedia.org/wikipedia/commons/3/3c/Microprogrammed_control_unit.png",
}

# ── HTTP session (reuse connections + proper identity) ─────────
SESSION = requests.Session()
SESSION.headers.update(
    {"User-Agent": "CA-Notes-Bot/1.0 (student project, contact: example@email.com)"}
)

# ── Colour palette ──────────────────────────────────────────────────────────
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
TEAL = colors.HexColor("#39d353")
TEAL_CARD = colors.HexColor("#091d10")
WHITE = colors.HexColor("#f0f6fc")
WHITE_DIM = colors.HexColor("#9da7b3")
TABLE_HDR = colors.HexColor("#1f6feb")
TABLE_R1 = colors.HexColor("#161b22")
TABLE_R2 = colors.HexColor("#1b2230")
TABLE_BDR = colors.HexColor("#30363d")
CODE_BG = colors.HexColor("#161b22")
CODE_GREEN = colors.HexColor("#7ee787")


# ── Style factory ────────────────────────────────────────────────────────────
def S(name, **kw):
    return ParagraphStyle(name, **kw)


COVER_H1 = S(
    "CH1",
    fontSize=34,
    textColor=WHITE,
    fontName="Helvetica-Bold",
    alignment=TA_CENTER,
    leading=42,
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
    fontSize=26,
    textColor=WHITE,
    fontName="Helvetica-Bold",
    alignment=TA_CENTER,
    leading=34,
)
CHAP_ST = S(
    "CP",
    fontSize=18,
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
TOC_H_ST = S(
    "TH",
    fontSize=11,
    fontName="Helvetica-Bold",
    leading=22,
    spaceBefore=8,
    textColor=CYAN,
)
TOC_I_ST = S(
    "TI", fontSize=10, fontName="Helvetica", leading=18, leftIndent=16, textColor=WHITE
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


def escape_cell(s):
    s = str(s)
    tags = re.findall(r"</?(?:b|i|u|sub|super|font)(?:\s[^>]*)?>", s)
    ph = "ZZZPH"
    clean = re.sub(r"</?(?:b|i|u|sub|super|font)(?:\s[^>]*)?>", ph, s)
    clean = clean.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    for tag in tags:
        clean = clean.replace(ph, tag, 1)
    return clean


# ── Layout widgets ───────────────────────────────────────────────────────────
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


def note(text):
    add(Paragraph(f"<b>[NOTE]</b> {text}", NOTE_ST))


def tip(text):
    p = Paragraph(f"<b>[EXAM TIP]</b> {text}", TIP_ST)
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


# ───────────────── IMAGE SETTINGS (GLOBAL CONTROL) ─────────────────
ENABLE_IMAGES = True  # Turn OFF to make PDF instant
MAX_IMAGES = 6  # Limit total images
REQUEST_TIMEOUT = 3  # seconds per request
MAX_RETRIES = 2  # retries per image
SLEEP_BETWEEN_RETRIES = 0.5  # seconds

image_counter = 0


def get_wikimedia_urls(url):
    if not url.endswith(".svg"):
        return [url]

    filename = url.split("/")[-1]
    base = "/".join(url.split("/")[:-1])
    png_name = filename.replace(".svg", ".png")

    return [
        f"{base}/thumb/{filename}/800px-{png_name}",
        f"{base}/thumb/{filename}/600px-{png_name}",
        url,
    ]


def web_image(url, width=None, height=None, caption=None, fallback_ascii=None, local_name=None):
    """FAST + SAFE image loader (no hanging, prefers local, minimal network)"""

    global image_counter

    # ── 0. HARD STOP (instant mode) ─────────────────
    if not ENABLE_IMAGES:
        return False

    # ── 1. LOCAL IMAGE FIRST (MOST IMPORTANT) ───────
    if local_name:
        local_path = os.path.join(ASSET_DIR, local_name)

        if os.path.exists(local_path):
            try:
                from reportlab.lib.utils import ImageReader

                img_reader = ImageReader(local_path)
                orig_w, orig_h = img_reader.getSize()

                w = width or (CW * 0.88)
                h = height or (w * 0.55)

                scale = min(w / orig_w, h / orig_h)

                img = Image(
                    local_path,
                    width=orig_w * scale,
                    height=orig_h * scale,
                )

                t = Table([[img]], colWidths=[CW])
                t.setStyle(TableStyle([
                    ("BACKGROUND", (0, 0), (-1, -1), CARD_DARK),
                    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                    ("BOX", (0, 0), (-1, -1), 1, CYAN),
                ]))

                add(t)

                if caption:
                    add(Paragraph(f"<i>{caption}</i>", CAP_ST))

                sp(8)
                print("[IMG] Loaded LOCAL:", local_name)
                return True

            except Exception as e:
                print("[IMG] Local load failed:", e)

    # ── 2. LIMIT IMAGES ─────────────────────────────
    if image_counter >= MAX_IMAGES:
        print("[IMG] Skipped (limit reached)")
        return False

    image_counter += 1

    # ── 3. FAST NETWORK (fallback only) ─────────────
    try:
        print("[IMG] Download:", url)
        resp = SESSION.get(url, timeout=2)

        if resp.status_code == 200 and "image" in resp.headers.get("Content-Type", ""):
            from reportlab.lib.utils import ImageReader

            img_reader = ImageReader(BytesIO(resp.content))
            orig_w, orig_h = img_reader.getSize()

            w = width or (CW * 0.88)
            h = height or (w * 0.55)

            scale = min(w / orig_w, h / orig_h)

            img = Image(
                BytesIO(resp.content),
                width=orig_w * scale,
                height=orig_h * scale,
            )

            t = Table([[img]], colWidths=[CW])
            t.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, -1), CARD_DARK),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("BOX", (0, 0), (-1, -1), 1, CYAN),
            ]))

            add(t)

            if caption:
                add(Paragraph(f"<i>{caption}</i>", CAP_ST))

            sp(8)
            return True

    except Exception as e:
        print("[IMG] Network failed:", e)

    # ── 4. FALLBACK ASCII ───────────────────────────
    print("[IMG] Using ASCII fallback")

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
cover_box(Paragraph("COMPUTER ARCHITECTURE", COVER_H1))
sp(6)
add(Paragraph("Unit I & Unit II — Complete Exam Notes with Full PYQ Answers", COVER_H2))
add(Paragraph("Subject Code: IT404 | UIT-RGPV (Autonomous) Bhopal", COVER_INFO))
sp(4)
rule(CYAN, 1.5)
sp(6)
add(
    Paragraph(
        "Reference: M. Morris Mano — Computer System Architecture (Pearson)", COVER_INFO
    )
)
sp(14)
info_table(
    ["Unit", "Topics Covered"],
    [
        [
            "Unit I",
            "Architecture vs Organization, Computer Generations, Von Neumann Model, "
            "CPU & Register Organization, Register Transfer Language (RTL), "
            "Bus & Memory Transfers, Arithmetic / Logic / Shift Micro-operations, ALSU",
        ],
        [
            "Unit II",
            "Fixed-Point Representation (Sign-Magnitude, 1's Complement, 2's Complement), "
            "Integer Arithmetic (Add, Subtract, Multiply with Booth's, Divide), "
            "Floating-Point IEEE 754 (Single & Double Precision), "
            "Hardwired vs Microprogrammed Control Unit, Control Memory, Microprogram Sequence",
        ],
        [
            "PYQ Answers",
            "Von Neumann diagram, Register classification, RTL block diagram, "
            "4-bit Arithmetic Circuit, Shift sequence, IEEE 754 conversion, "
            "Hardwired vs Microprogrammed, 2's Complement arithmetic, "
            "Booth's Multiplication, Negative Number Representations",
        ],
    ],
)
br()

# ── Table of Contents ────────────────────────────────────────────────────────
chap_box("TABLE OF CONTENTS", CARD_MID, PURPLE)
sp(6)
toc = [
    ("UNIT I — BASIC CONCEPTS & CPU ORGANIZATION", True),
    ("1.  Computer Architecture vs Organization", False),
    ("2.  Computer Generations", False),
    ("3.  Von Neumann Model", False),
    ("4.  Harvard Architecture", False),
    ("5.  CPU Organization", False),
    ("6.  CPU Registers", False),
    ("7.  Register Transfer Language (RTL)", False),
    ("8.  Bus and Memory Transfers", False),
    ("9.  Arithmetic Micro-operations", False),
    ("10. Logic Micro-operations", False),
    ("11. Shift Micro-operations", False),
    ("12. Arithmetic Logic Shift Unit (ALSU)", False),
    ("UNIT II — ALU, NUMBER REPRESENTATIONS & CONTROL", True),
    ("13. Fixed-Point Representation", False),
    ("14. Integer Arithmetic", False),
    ("15. Floating-Point Representation — IEEE 754", False),
    ("16. Floating-Point Arithmetic", False),
    ("17. Hardwired vs Microprogrammed Control Unit", False),
    ("18. Control Memory & Microprogram Sequencer", False),
    ("PYQ MODEL ANSWERS — Q1 & Q2", True),
]
for title, is_hdr in toc:
    if is_hdr:
        add(Paragraph(f'<b><font color="#79c0ff">{title}</font></b>', TOC_H_ST))
    else:
        add(Paragraph(title, TOC_I_ST))
br()

# ════════════════════════════════════════════════════════════════════════════
#  UNIT I
# ════════════════════════════════════════════════════════════════════════════
part_box("UNIT I — BASIC CONCEPTS & CPU ORGANIZATION", CARD_DARK, CYAN)

# ── 1. Architecture vs Organization ─────────────────────────────────────────
chap_box("1. Computer Architecture vs Organization")
section("1.1 Definitions")
info_table(
    ["Aspect", "Computer Architecture", "Computer Organization"],
    [
        [
            "Definition",
            "Attributes of the system visible to the programmer. Deals with the logical design.",
            "How the architectural attributes are implemented. Deals with physical components.",
        ],
        [
            "Focus",
            "Logic — instruction sets, addressing modes, data types, cache optimisation",
            "Physical — circuit design, adders, control signals, peripherals, buses",
        ],
        [
            "Examples",
            "Instruction Set Architecture (ISA), register bit width, I/O mechanisms",
            "Control signals, memory technology, buffer/timing circuits",
        ],
        ["Analogy", "'What the computer does'", "'How the computer does it'"],
        [
            "Change independence",
            "Does not change when organisation changes (e.g. ISA stays same across Intel generations)",
            "Can change while keeping the same architecture",
        ],
    ],
)
tip(
    "Architecture = Logic (visible to programmer). Organization = Physical implementation (hidden from programmer). This 1-liner earns easy marks."
)
br()

# ── 2. Computer Generations ─────────────────────────────────────────────────
chap_box("2. Computer Generations")
info_table(
    ["Generation", "Period", "Technology", "Key Features", "Examples"],
    [
        [
            "1st",
            "1940–1956",
            "Vacuum Tubes",
            "Machine language only; huge, slow, very power hungry; room-sized",
            "ENIAC, UNIVAC, IBM 701",
        ],
        [
            "2nd",
            "1956–1963",
            "Transistors",
            "Assembly & high-level languages (FORTRAN, COBOL); smaller, faster, cheaper",
            "IBM 7094, CDC 1604",
        ],
        [
            "3rd",
            "1964–1971",
            "Integrated Circuits (ICs)",
            "Multiple transistors on single chip; OS; time-sharing; miniaturisation",
            "IBM 360, DEC PDP-8",
        ],
        [
            "4th",
            "1971–present",
            "VLSI Microprocessors",
            "Entire CPU on one chip; personal computers; GUI; networking",
            "Intel 4004, x86, ARM",
        ],
        [
            "5th",
            "Present–future",
            "AI / Parallel / Quantum",
            "Artificial intelligence, parallel processing, voice recognition, quantum computing",
            "IBM Watson, Google TPU",
        ],
    ],
)
br()

# ── 3. Von Neumann Model ─────────────────────────────────────────────────────
chap_box("3. Von Neumann Model")
section("3.1 Overview")
definition(
    "<b>Von Neumann Architecture</b> (1945, John von Neumann): A computer design in which program instructions and data are stored in the <b>same memory</b>. The CPU fetches and executes instructions sequentially from this shared memory via a single shared bus."
)
body(
    "This concept — the <b>stored-program computer</b> — is still the basis of most computers today."
)

# Web image — Von Neumann Architecture
web_image(
    IMAGES["von_neumann.png"],
    local_name="von_neumann.png",
    width=CW * 0.90,
    height=CW * 0.48,
    caption="Fig 1: Von Neumann Architecture — single shared bus between CPU and Memory",
    fallback_ascii="""
 VON NEUMANN ARCHITECTURE
 =================================================================
                    +---------------------------+
                    |        MEMORY UNIT        |
                    |  (Stores BOTH Program     |
                    |   Instructions AND Data)  |
                    +-------------+-------------+
                                  |
                         Single Shared Bus
                    ______________|______________
                   |                             |
        +----------v----------+    +-------------v----------+
        |    CONTROL UNIT     |    |   ARITHMETIC & LOGIC   |
        |  (CU)               |    |   UNIT  (ALU)          |
        |  - Fetch            |    |  - Addition            |
        |  - Decode           |    |  - Subtraction         |
        |  - Execute          |    |  - Logic operations    |
        +----------+----------+    +-------------+----------+
                   |                             |
                   +------------+----------------+
                                |
                    +-----------v-----------+
                    |     REGISTERS         |
                    |  PC  IR  MAR  MDR  AC |
                    +-----------+-----------+
                                |
                   +------------+---------------+
                   |                            |
        +----------v----------+   +------------v-----------+
        |    INPUT DEVICES    |   |    OUTPUT DEVICES      |
        | (Keyboard, Mouse,   |   | (Monitor, Printer,     |
        |  Scanner, Disk)     |   |  Speaker, Disk)        |
        +---------------------+   +------------------------+
 =================================================================
 KEY PRINCIPLE: Instructions and Data share the SAME memory and bus.
""",
)

section("3.2 Five Key Components")
info_table(
    ["Component", "Full Name", "Function"],
    [
        [
            "CPU",
            "Central Processing Unit",
            "Executes instructions. Consists of the CU and ALU. The 'brain' of the computer.",
        ],
        [
            "Memory Unit",
            "RAM (Primary/Main Memory)",
            "Stores both program instructions and data. Fast, directly accessible by CPU. Volatile.",
        ],
        [
            "ALU",
            "Arithmetic Logic Unit",
            "Performs arithmetic (add, sub, mul, div) and logic (AND, OR, NOT, XOR, compare) operations.",
        ],
        [
            "Control Unit",
            "Control Unit (CU)",
            "Fetches instructions from memory, decodes them, and generates control signals to execute them. Coordinates all components.",
        ],
        [
            "Buses",
            "Data / Address / Control Bus",
            "Pathways for data and instructions. In Von Neumann, a single shared bus connects CPU and Memory — the source of the bottleneck.",
        ],
    ],
)

section("3.3 Von Neumann Bottleneck")
definition(
    "<b>Von Neumann Bottleneck:</b> Since both instructions and data share the same single memory and bus, the CPU is often idle waiting for one or the other. This limits throughput and execution speed. It is the fundamental performance limitation of the Von Neumann model."
)
highlight(
    "<b>Solution:</b> Harvard Architecture — uses <b>separate buses and memories</b> for instructions and data, allowing the CPU to fetch an instruction and read/write data simultaneously.",
    YELLOW_CARD,
    YELLOW,
)
tip(
    "PYQ Q1a): Draw Von Neumann model + describe all 5 subsystems. Always label: Memory (stores both instructions and data), CU, ALU, Registers, I/O, and the single shared bus. Mention the Von Neumann bottleneck for full marks."
)
br()

# ── 4. Harvard Architecture ──────────────────────────────────────────────────
chap_box("4. Harvard Architecture")
section("4.1 Overview")
definition(
    "<b>Harvard Architecture:</b> A computer design that uses <b>separate memories and buses</b> for program instructions and data. This eliminates the Von Neumann bottleneck by allowing simultaneous instruction fetch and data access."
)

web_image(
    IMAGES["harvard_architecture.webp"],
    local_name="harvard_architecture.webp",
    width=CW * 0.88,
    height=CW * 0.46,
    caption="Fig 2: Harvard Architecture — separate instruction and data memories",
    fallback_ascii="""
 HARVARD ARCHITECTURE
 =================================================================
  +--------------------+        +--------------------+
  |  INSTRUCTION       |        |   DATA             |
  |  MEMORY            |        |   MEMORY           |
  |  (Program store)   |        |   (Data store)     |
  +--------+-----------+        +----------+---------+
           |  Instruction Bus              |  Data Bus
           |                               |
  +--------v-------------------------------v---------+
  |                  CPU                             |
  |   +-------------------+  +-------------------+  |
  |   |  CONTROL UNIT     |  |  ALU              |  |
  |   |  (Fetch, Decode,  |  |  (Arithmetic &    |  |
  |   |   Execute)        |  |   Logic ops)      |  |
  |   +-------------------+  +-------------------+  |
  |   +-------------------------------------------+  |
  |   |           REGISTERS                       |  |
  |   |   PC   IR   MAR   MDR   AC                |  |
  |   +-------------------------------------------+  |
  +--------------------------------------------------+
           |                               |
  +--------v-----------+        +----------v---------+
  |  INPUT DEVICES     |        |  OUTPUT DEVICES    |
  +--------------------+        +--------------------+
 =================================================================
 KEY ADVANTAGE: CPU can fetch next instruction AND access data
 at the SAME TIME -> higher throughput, faster execution.
""",
)

info_table(
    ["Feature", "Von Neumann", "Harvard"],
    [
        [
            "Memory",
            "Single memory for both instructions and data",
            "Separate memories for instructions and data",
        ],
        [
            "Bus",
            "Single shared bus for instructions and data",
            "Separate buses for instruction fetch and data access",
        ],
        [
            "Speed",
            "Slower — one operation at a time on the bus",
            "Faster — simultaneous instruction fetch and data access",
        ],
        [
            "Bottleneck",
            "Yes — Von Neumann bottleneck exists",
            "No — bottleneck eliminated",
        ],
        ["Complexity", "Simpler, less hardware", "More complex, more hardware"],
        [
            "Use Today",
            "General-purpose computers (PCs, servers)",
            "Microcontrollers, DSPs, ARM Cortex-M, AVR, PIC",
        ],
    ],
)
br()

# ── 5. CPU Organization ──────────────────────────────────────────────────────
chap_box("5. CPU Organization")
section("5.1 Internal CPU Structure")
body(
    "The CPU is organised around an internal bus (ALU bus or CPU internal bus) that connects registers, the ALU, and the control unit. All data movement between registers and the ALU passes through this internal bus."
)

web_image(
    IMAGES["cpu_block.jpg"],
    local_name="cpu_block.jpg",
    width=CW * 0.85,
    height=CW * 0.50,
    caption="Fig 3: Internal CPU organisation showing registers, ALU, and control unit",
    fallback_ascii="""
 CPU INTERNAL ORGANIZATION
 =================================================================
  +---------------------------------------------------------------+
  |                        CPU                                    |
  |                                                               |
  |  +----------+  +----------+  +----------+  +----------+      |
  |  |    PC    |  |    IR    |  |   MAR    |  |   MDR    |      |
  |  | (Program |  |(Instruc- |  | (Memory  |  | (Memory  |      |
  |  | Counter) |  | tion Reg)|  | Address) |  |  Data)   |      |
  |  +----+-----+  +----+-----+  +----+-----+  +----+-----+      |
  |       |             |             |              |            |
  |  +----+---------------------------------------------+------+ |
  |  |              INTERNAL CPU BUS (ALU Bus)           |      | |
  |  +---------+----------------------------------+------+------+ |
  |            |                                  |               |
  |  +---------v---------+            +-----------v-----------+  |
  |  |        ALU        |            |    CONTROL UNIT (CU)  |  |
  |  | (Arithmetic &     |            | - Fetch               |  |
  |  |  Logic ops)       |            | - Decode              |  |
  |  |                   |            | - Execute             |  |
  |  +--------+----------+            +-----------+-----------+  |
  |           |                                   |               |
  |  +--------v------------------------------------------+------+ |
  |  |     ACCUMULATOR (AC) / General Purpose Registers  |      | |
  |  +---------------------------------------------------+------+ |
  +---------------------------------------------------------------+
           |                                  |
  +--------v-----------+         +------------v-------+
  | ADDRESS BUS        |         | DATA BUS           |
  +--------------------+         +--------------------+
           |                                  |
           +----------------------------------+
                         |
              +----------v----------+
              |   MAIN MEMORY       |
              +---------------------+
 =================================================================
""",
)
br()

# ── 6. CPU Registers ─────────────────────────────────────────────────────────
chap_box("6. CPU Registers")
section("6.1 What is a Register?")
definition(
    "<b>Register:</b> A small, extremely fast storage location inside the CPU. Registers temporarily hold data, instructions, and addresses that are currently being processed. They are the fastest memory in the memory hierarchy — faster than cache or RAM."
)

section("6.2 Classification of Registers")
body("CPU registers fall into two broad classes:")
highlight(
    "<b>Class 1 — User-Visible Registers:</b> Can be referenced by the programmer via machine-language instructions. Include general-purpose registers, data registers, address registers, and condition codes (flags).",
    CARD_DARK,
    CYAN,
)
highlight(
    "<b>Class 2 — Control & Status Registers (not user-visible):</b> Used by the processor to control operations. Cannot be directly accessed by user programs. Include PC, IR, MAR, MDR, and PSW.",
    CARD_DARK,
    PURPLE,
)

section("6.3 Key CPU Registers")

web_image(
    IMAGES["ripple_adder.jpeg"],
    local_name="ripple_adder.jpeg",
    width=CW * 0.82,
    height=CW * 0.45,
    caption="Fig 4: CPU registers and their role in instruction execution",
    fallback_ascii="""
 CPU REGISTERS OVERVIEW
 =================================================================
  REGISTER    | SIZE  | FUNCTION
  ------------|-------|------------------------------------------
  PC          | 16/32 | Program Counter: holds address of NEXT
              |  bit  | instruction to be fetched.
  ------------|-------|------------------------------------------
  IR          | 16/32 | Instruction Register: holds the CURRENT
              |  bit  | instruction being decoded/executed.
  ------------|-------|------------------------------------------
  MAR         | 16/32 | Memory Address Register: holds the address
              |  bit  | of the memory location to be accessed.
  ------------|-------|------------------------------------------
  MDR / MBR   | 16/32 | Memory Data Register: holds the data
              |  bit  | being transferred to/from memory.
  ------------|-------|------------------------------------------
  AC          | 16/32 | Accumulator: holds intermediate and final
              |  bit  | results of ALU operations.
  ------------|-------|------------------------------------------
  SP          | 16/32 | Stack Pointer: points to top of stack in
              |  bit  | memory. Used for subroutine calls.
  ------------|-------|------------------------------------------
  FLAGS / PSW | 8 bit | Program Status Word / Condition Codes:
              |       | C (Carry), Z (Zero), S (Sign), V (Overflow)
  =================================================================
""",
)

info_table(
    ["Register", "Full Name", "Class", "Function"],
    [
        [
            "PC",
            "Program Counter",
            "Control (not user-visible)",
            "Holds address of the NEXT instruction to fetch. Incremented after each fetch.",
        ],
        [
            "IR",
            "Instruction Register",
            "Control (not user-visible)",
            "Holds the CURRENT instruction being decoded and executed by the CU.",
        ],
        [
            "MAR",
            "Memory Address Register",
            "Control (not user-visible)",
            "Holds the memory address to be read from or written to. Connected to address bus.",
        ],
        [
            "MDR",
            "Memory Data Register",
            "Control (not user-visible)",
            "Holds the data being transferred to or from memory. Connected to data bus.",
        ],
        [
            "AC",
            "Accumulator",
            "User-visible",
            "Holds operands and intermediate/final results of ALU operations.",
        ],
        [
            "SP",
            "Stack Pointer",
            "User-visible",
            "Points to the top of the stack in memory. Used for PUSH/POP and subroutine calls.",
        ],
        [
            "Flags/PSW",
            "Program Status Word",
            "Control",
            "Status bits: C=Carry, Z=Zero, S=Sign/Negative, V=Overflow. Set by ALU after operations.",
        ],
    ],
)
tip(
    "PYQ Q1b): Classify registers into TWO broad classes: (1) User-Visible Registers (programmer can access: AC, SP, general-purpose, flags) and (2) Control/Status Registers (CPU-internal, not accessible by programmer: PC, IR, MAR, MDR). Give 2 examples each."
)
br()

# ── 7. Register Transfer Language ────────────────────────────────────────────
chap_box("7. Register Transfer Language (RTL)")
section("7.1 What is RTL?")
definition(
    "<b>Register Transfer Language (RTL):</b> A symbolic notation used to describe the micro-operations performed on data stored in registers. It specifies how data flows between registers and what operations are performed on that data at the micro level."
)

section("7.2 RTL Notation Basics")
info_table(
    ["Symbol", "Meaning", "Example"],
    [
        ["R1, R2, R3 ...", "Denote registers", "R1 holds value 0101"],
        [
            "R1 <- R2",
            "Transfer contents of R2 into R1",
            "R1 gets the value stored in R2",
        ],
        [
            "R1 <- R2 + R3",
            "Add R2 and R3, store result in R1",
            "Arithmetic micro-operation",
        ],
        [
            "R1 <- R2 AND R3",
            "Bitwise AND of R2 and R3 into R1",
            "Logic micro-operation",
        ],
        [
            "M[MAR]",
            "Memory location addressed by MAR",
            "M[MAR] <- MDR means write MDR to memory",
        ],
        [
            "MDR <- M[MAR]",
            "Read from memory address in MAR into MDR",
            "Read (load) operation",
        ],
        [
            "M[MAR] <- MDR",
            "Write MDR contents to memory address in MAR",
            "Write (store) operation",
        ],
        [
            "If (P=1) then R1 <- R2",
            "Conditional transfer; only if control variable P is 1",
            "Conditional micro-operation",
        ],
        [
            "P: R1 <- R2",
            "Shorthand: R1 <- R2 happens when P=1",
            "Same as If(P=1) then R1<-R2",
        ],
    ],
)

section("7.3 Categories of Micro-operations")
bullet(
    [
        "<b>Register Transfer Micro-operations:</b> Transfer data between registers (e.g. R1 <- R2)",
        "<b>Arithmetic Micro-operations:</b> Arithmetic on numeric data in registers (e.g. R3 <- R1 + R2)",
        "<b>Logic Micro-operations:</b> Bitwise logic on register contents (e.g. R1 <- R1 AND R2)",
        "<b>Shift Micro-operations:</b> Shift or rotate bits in a register (e.g. R1 <- shl R1)",
    ]
)

section("7.4 RTL — Bus Transfers")
body(
    "A common bus connects multiple registers. The bus allows one source register to transfer data to one destination register at a time using multiplexers and control signals."
)
code_block(
    """
 SINGLE BUS REGISTER TRANSFER:

 Transfer R1 to R2 using a bus with MUX select:
   R2 <- R1       (S = select line choosing R1 as input to bus)

 Three-Register Bus Example:
   Instruction: R3 <- R1 + R2
   Step 1: BUS <- R1      (select R1 onto bus, load into temp A of ALU)
   Step 2: BUS <- R2      (select R2 onto bus, load into temp B of ALU)
   Step 3: ALU performs ADD, result placed on bus
   Step 4: R3 <- BUS      (load result from bus into R3)

 RTL Notation for conditional transfer:
   If (T = 1): R2 <- R1     written as    T: R2 <- R1

 Multiple simultaneous transfers (if separate buses exist):
   R1 <- R2, R3 <- R4      (both happen in the same clock cycle)
"""
)
br()

# ── 8. Bus and Memory Transfers ──────────────────────────────────────────────
chap_box("8. Bus and Memory Transfers")
section("8.1 Types of Buses")
info_table(
    ["Bus", "Width", "Direction", "Function"],
    [
        [
            "Data Bus",
            "8/16/32/64 bits",
            "Bidirectional",
            "Carries actual data between CPU, memory, and I/O",
        ],
        [
            "Address Bus",
            "16/32/64 bits",
            "Unidirectional (CPU out)",
            "Carries memory/I/O address from CPU",
        ],
        [
            "Control Bus",
            "Variable",
            "Bidirectional",
            "Carries control signals: Read, Write, Clock, Interrupt, Reset",
        ],
    ],
)

section("8.2 Memory Read and Write Operations")
code_block(
    """
 MEMORY READ (Load from memory into MDR):
 ==========================================
 Step 1:  MAR <- Address           (put address into MAR)
 Step 2:  MDR <- M[MAR]            (memory places data on MDR)
 Step 3:  R <- MDR                 (transfer MDR to destination register)

 RTL in one step:  R <- M[Address]

 MEMORY WRITE (Store from MDR to memory):
 ==========================================
 Step 1:  MAR <- Address           (put address into MAR)
 Step 2:  MDR <- R                 (put data to write into MDR)
 Step 3:  M[MAR] <- MDR            (write MDR contents to memory)

 RTL in one step:  M[Address] <- R

 FETCH-DECODE-EXECUTE CYCLE (RTL):
 ==========================================
 T0:  MAR <- PC              (copy PC to MAR)
 T1:  MDR <- M[MAR], PC <- PC + 1  (fetch instruction, increment PC)
 T2:  IR <- MDR              (load instruction into IR)
 T3:  Decode IR, MAR <- IR(address field)  (decode and get operand address)
 T4:  MDR <- M[MAR]          (fetch operand from memory)
 T5:  Execute (ALU operation using AC and MDR)
"""
)
br()

# ── 9. Arithmetic Micro-operations ──────────────────────────────────────────
chap_box("9. Arithmetic Micro-operations")
section("9.1 Summary Table")
info_table(
    ["RTL Statement", "Operation", "Description"],
    [
        ["R3 <- R1 + R2", "Addition", "Add contents of R1 and R2; store in R3"],
        ["R3 <- R1 - R2", "Subtraction", "Subtract R2 from R1; store in R3"],
        ["R1 <- R1 + 1", "Increment", "Add 1 to R1 (increment)"],
        ["R1 <- R1 - 1", "Decrement", "Subtract 1 from R1"],
        ["R2 <- ~R2", "1's Complement", "Complement each bit of R2"],
        [
            "R2 <- ~R2 + 1",
            "2's Complement",
            "Negate R2 (1's complement + 1 = subtraction)",
        ],
        ["R3 <- R1 + R2 + Cin", "Add with Carry", "Add R1, R2, and carry-in bit"],
    ],
)

section("9.2 Binary Adder (Full Adder)")
code_block(
    """
 FULL ADDER TRUTH TABLE:
 A  B  Cin | Sum  Cout
 ----------|----------
 0  0   0  |  0    0
 0  0   1  |  1    0
 0  1   0  |  1    0
 0  1   1  |  0    1
 1  0   0  |  1    0
 1  0   1  |  0    1
 1  1   0  |  0    1
 1  1   1  |  1    1

 Sum  = A XOR B XOR Cin
 Cout = (A AND B) OR (B AND Cin) OR (A AND Cin)

 4-BIT RIPPLE CARRY ADDER:
 A3 A2 A1 A0
 B3 B2 B1 B0
  |  |  |  |
 FA  FA FA FA   (Full Adder for each bit position)
  |  |  |  |
 S3 S2 S1 S0    (Sum bits)
  C3 C2 C1 C0   (Carry bits ripple left to right)
"""
)

web_image(
    IMAGES["alu_block.png"],
    local_name="alu_block.png",
    width=CW * 0.85,
    height=CW * 0.35,
    caption="Fig 5: 4-bit Ripple Carry Adder — four full adders cascaded",
    fallback_ascii="""
 4-BIT RIPPLE CARRY ADDER:
 =================================================================
  A3 B3   A2 B2   A1 B1   A0 B0
   | |     | |     | |     | |
 +-v-v-+ +-v-v-+ +-v-v-+ +-v-v-+
 | FA3 | | FA2 | | FA1 | | FA0 |<-- C0=0 (no initial carry)
 +--+--+ +--+--+ +--+--+ +--+--+
    |  C3    |  C2    |  C1    |
    S3       S2       S1       S0
 =================================================================
 Carry RIPPLES from LSB (FA0) to MSB (FA3) - hence "Ripple Carry"
""",
)
br()

# ── 10. Logic Micro-operations ───────────────────────────────────────────────
chap_box("10. Logic Micro-operations")
section("10.1 Overview")
definition(
    "<b>Logic Micro-operations:</b> Perform bit-level (Boolean) operations on data in registers. They operate on individual bits independently. Used for masking, setting, clearing, or complementing specific bits."
)

section("10.2 The 16 Possible Logic Operations")
body(
    "For two 1-bit inputs, there are 2^2 = 4 possible input combinations, giving 2^4 = 16 possible logic functions. The commonly used ones are:"
)
info_table(
    ["RTL", "Operation", "Symbol", "Effect on each bit pair (A, B)"],
    [
        [
            "F <- A AND B",
            "AND",
            "&",
            "1 only if BOTH A=1 and B=1. Used for MASKING (clearing specific bits).",
        ],
        [
            "F <- A OR B",
            "OR",
            "|",
            "1 if EITHER A=1 or B=1. Used for SETTING specific bits.",
        ],
        [
            "F <- A XOR B",
            "Exclusive OR",
            "^",
            "1 if inputs are DIFFERENT. Used for COMPLEMENTING specific bits.",
        ],
        [
            "F <- NOT A",
            "Complement",
            "~",
            "Inverts every bit of A. Used for 1's complement.",
        ],
        ["F <- NAND", "NOT AND", "", "Complement of AND. Universal gate."],
        ["F <- NOR", "NOT OR", "", "Complement of OR. Universal gate."],
    ],
)

section("10.3 Selective Operations using Logic Micro-ops")
code_block(
    """
 SELECTIVE CLEAR (using AND with a MASK):
   To clear bits 0 and 1 of R1 (set them to 0):
   Mask = 1111 1100
   R1 <- R1 AND Mask
   Example: R1 = 1010 1011
             AND  1111 1100
             R1 = 1010 1000  (bits 0 and 1 cleared)

 SELECTIVE SET (using OR with a MASK):
   To set bits 0 and 1 of R1 to 1:
   Mask = 0000 0011
   R1 <- R1 OR Mask
   Example: R1 = 1010 1000
              OR  0000 0011
             R1 = 1010 1011  (bits 0 and 1 set to 1)

 SELECTIVE COMPLEMENT (using XOR with a MASK):
   To complement bits 0 and 1 of R1:
   Mask = 0000 0011
   R1 <- R1 XOR Mask
   Example: R1 = 1010 1010
             XOR  0000 0011
             R1 = 1010 1001  (bits 0 and 1 flipped)
"""
)
br()

# ── 11. Shift Micro-operations ───────────────────────────────────────────────
chap_box("11. Shift Micro-operations")
section("11.1 Types of Shifts")
info_table(
    ["Shift Type", "RTL Symbol", "Description", "Serial Input", "Bit Loss?"],
    [
        [
            "Logical Shift Left",
            "shl R",
            "All bits shift left by 1 position. 0 inserted at LSB.",
            "0 at LSB",
            "MSB lost",
        ],
        [
            "Logical Shift Right",
            "shr R",
            "All bits shift right by 1 position. 0 inserted at MSB.",
            "0 at MSB",
            "LSB lost",
        ],
        [
            "Circular Shift Left",
            "cil R",
            "All bits rotate left. MSB wraps around to LSB.",
            "MSB -> LSB",
            "No loss",
        ],
        [
            "Circular Shift Right",
            "cir R",
            "All bits rotate right. LSB wraps around to MSB.",
            "LSB -> MSB",
            "No loss",
        ],
        [
            "Arithmetic Shift Left",
            "ashl R",
            "Shift left; 0 inserted at LSB. Sign bit may change (overflow!).",
            "0 at LSB",
            "MSB lost; overflow possible",
        ],
        [
            "Arithmetic Shift Right",
            "ashr R",
            "Shift right; SIGN BIT preserved at MSB. Equivalent to divide by 2.",
            "Sign bit repeated",
            "LSB lost",
        ],
    ],
)

section("11.2 Worked Examples")
code_block(
    """
 INITIAL VALUE: R = 1 0 1 0 1 0 1 0  (binary, MSB on left)

 LOGICAL SHIFT LEFT  (shl R):
   1 0 1 0 1 0 1 0  -->  0 1 0 1 0 1 0 0
   (0 inserted at LSB, MSB = 1 is lost)

 LOGICAL SHIFT RIGHT (shr R):
   1 0 1 0 1 0 1 0  -->  0 1 0 1 0 1 0 1
   (0 inserted at MSB, LSB = 0 is lost)

 CIRCULAR SHIFT LEFT (cil R):
   1 0 1 0 1 0 1 0  -->  0 1 0 1 0 1 0 1
   (MSB = 1 wraps around to LSB position)

 CIRCULAR SHIFT RIGHT (cir R):
   1 0 1 0 1 0 1 0  -->  0 1 0 1 0 1 0 1
   (LSB = 0 wraps around to MSB position)

 ARITHMETIC SHIFT LEFT (ashl R):
   1 0 1 0 1 0 1 0  -->  0 1 0 1 0 1 0 0
   (Same as logical shift left; equivalent to multiply by 2)
   WARNING: If sign bit changes -> OVERFLOW occurred!

 ARITHMETIC SHIFT RIGHT (ashr R):
   1 0 1 0 1 0 1 0  -->  1 1 0 1 0 1 0 1
   (Sign bit = 1 is REPLICATED at MSB; equivalent to divide by 2)
   NOTE: Sign is PRESERVED. This is the key difference from shr.

 PYQ SEQUENCE: Start R = 1 1 0 1 1 1 0 1
   Step 1 (shl):  1 0 1 1 1 0 1 0   (0 in LSB, MSB dropped)
   Step 2 (cir):  0 1 0 1 1 1 0 1   (LSB=0 wraps to MSB)
   Step 3 (shr):  0 0 1 0 1 1 1 0   (0 in MSB, LSB dropped)
   Step 4 (cil):  0 1 0 1 1 1 0 0   (MSB=0 wraps to LSB)
"""
)
tip(
    "PYQ Q1e) asks to trace a shift sequence. Always show the full 8-bit register value after EACH shift. Draw arrows showing which bit moves where. Logical shift: 0 enters. Circular: bits wrap. Arithmetic right: sign bit replicated."
)
br()

# ── 12. Arithmetic Logic Shift Unit (ALSU) ───────────────────────────────────
chap_box("12. Arithmetic Logic Shift Unit (ALSU)")
section("12.1 Overview")
definition(
    "<b>ALSU:</b> A combined unit that can perform all arithmetic, logic, and shift operations depending on selection signals S0–S3 and mode bit M. Each bit-slice of the ALSU takes inputs Ai and Bi and produces output Fi based on the selection."
)

web_image(
    IMAGES["alu_block.png"],
    local_name="alu_block.png",
    width=CW * 0.80,
    height=CW * 0.50,
    caption="Fig 6: One stage of the Arithmetic Logic Shift Unit",
    fallback_ascii="""
 ONE STAGE OF THE ALSU (for bit position i):
 =================================================================
               S3  S2  S1  S0   M (mode)
                |   |   |   |   |
            +---v---v---v---v---v---+
            |   OPERATION SELECT    |
            |   (MUX + Logic)       |
 Ai ------->|                       |---------> Fi (output bit)
 Bi ------->|   +-----------+       |
            |   | FULL      +------>|---------> Ci+1 (carry out)
 Ci ------->|   | ADDER     |       |
            +---+-----------+-------+
                      |
                  (arithmetic path when M=0)

 FUNCTION TABLE (S3 S2 S1 S0 | Cin | M | Operation):
 +---------+-----+---+---------------------------+
 | S3 S2 S1 S0  | M | Cin | Operation           |
 +---------+-----+---+-----+---------------------+
 | 0  0  0  0   | 0 |  0  | F = A               |
 | 0  0  0  0   | 0 |  1  | F = A + 1 (incr)    |
 | 0  0  0  1   | 0 |  0  | F = A + B           |
 | 0  0  1  1   | 0 |  1  | F = A - B (via 2's) |
 | 0  1  0  0   | 0 |  0  | F = A - 1 (decr)    |
 | 0  0  0  0   | 1 |  0  | F = A AND B         |
 | 0  1  0  1   | 1 |  0  | F = A OR B          |
 | 0  1  1  0   | 1 |  0  | F = A XOR B         |
 | 1  0  1  1   | 1 |  0  | F = NOT A           |
 | 1  0  0  0   | 1 |  0  | F = shl A           |
 | 1  0  0  1   | 1 |  0  | F = shr A           |
 +---------+-----+---+-----+---------------------+
 M = 0: Arithmetic mode    M = 1: Logic mode
 =================================================================
""",
)

section("12.2 Full 4-bit Arithmetic Circuit (PYQ Q1d)")
highlight(
    "<b>PYQ Direct Answer:</b> Build a 4-bit arithmetic circuit that performs all arithmetic operations.",
    CARD_MID,
    CYAN,
)
code_block(
    """
 4-BIT ARITHMETIC CIRCUIT DESIGN:
 =================================================================
 The circuit uses 4 Full Adders (FA0..FA3) connected in cascade.
 Input to each FA: Ai, Xi (function of Bi and S), Ci

 Xi is generated by a MUX controlled by selection bits S1 S0:
   S1=0, S0=0 : Xi = 0            -> F = A
   S1=0, S0=1 : Xi = Bi           -> F = A + B
   S1=1, S0=0 : Xi = NOT Bi       -> F = A + NOT B (with Cin=1 gives A-B)
   S1=1, S0=1 : Xi = 1            -> F = A + 1 (increment)

 Block diagram (1-bit slice):
         S1  S0
          |   |
     +----|---|----+
 Bi -|  4:1 MUX   |--Xi
     |  Xi select  |
     +-------------+
          |
 Ai ------|---> [ FULL ADDER ] ---> Fi (sum bit)
 Ci ------|---> [           ] ---> Ci+1 (carry out)

 FUNCTION TABLE (4-bit Arithmetic Unit):
 +-------+-----+---------+---------------------------+
 | S1 S0 | Cin | Function| Operation                 |
 +-------+-----+---------+---------------------------+
 | 0   0 |  0  | F=A     | Transfer A                |
 | 0   0 |  1  | F=A+1   | Increment A               |
 | 0   1 |  0  | F=A+B   | Addition                  |
 | 0   1 |  1  | F=A+B+1 | Add with carry            |
 | 1   0 |  0  | F=A+B'  | Subtract with borrow      |
 | 1   0 |  1  | F=A-B   | Subtraction (2's compl.)  |
 | 1   1 |  0  | F=A-1   | Decrement A               |
 | 1   1 |  1  | F=A     | Transfer A                |
 +-------+-----+---------+---------------------------+
 NOTE: For subtraction (A-B): use F=A+B'+1 (2's complement method)
       B' = 1's complement of B; +1 comes from Cin=1
 =================================================================
"""
)

section("12.3 RTL Block Diagram for Conditional Transfer (PYQ Q1c)")
highlight(
    "<b>PYQ Q1c:</b> Draw hardware block diagram for: if x + yz: AR <- AR + BR",
    CARD_MID,
    CYAN,
)
code_block(
    """
 STATEMENT: x + yz : AR <- AR + BR
 (Transfer AR + BR into AR when control condition x+yz is TRUE)

 CONTROL FUNCTION: F = x + yz
   This is a Boolean expression. When F=1, the transfer AR <- AR+BR occurs.

 STEP 1: Implement control function F = x + yz using logic gates:
   - AND gate: yz = y AND z
   - OR gate:  F = x OR (y AND z)

 STEP 2: Connect F to the load enable of AR register.

 BLOCK DIAGRAM:
 ================================================================
    x --------+
              |
    y ---[AND]---> yz
    z ---|        |
              +--[OR]---> F (Load Enable for AR)
                              |
                              |
    AR ----+                  |
           |                  v
    BR ----|--> [n-bit ADDER]--> SUM
           |         |            |
           |         v            |
           +---->[REGISTER AR]<---+  (AR loaded when F=1)
                (Load when F=1)

 RTL:
   F = x + yz               (control function using gates)
   If (F = 1): AR <- AR + BR (conditional register transfer)

 ================================================================
"""
)
tip(
    "PYQ Q1c): Always draw: (1) The logic gates for the control function (x+yz uses AND gate for yz, then OR gate), (2) The n-bit adder, (3) The register AR with a load enable input connected to F. Label everything."
)
br()

# ════════════════════════════════════════════════════════════════════════════
#  UNIT II
# ════════════════════════════════════════════════════════════════════════════
part_box("UNIT II — ALU, NUMBER REPRESENTATIONS & CONTROL", CARD_DARK, PURPLE)

# ── 13. Fixed-Point Representation ───────────────────────────────────────────
chap_box("13. Fixed-Point Representation", CARD_MID, PURPLE)
section("13.1 Unsigned vs Signed Numbers")
definition(
    "<b>Fixed-Point Representation:</b> Numbers are represented with the binary point fixed at a specific position — either at the far right (integer) or far left (fraction). Negative numbers use the MSB as the sign bit."
)

section("13.2 Three Forms of Signed Integer Representation")
info_table(
    ["Format", "Positive Number", "Negative Number", "Range (n-bit)", "Special Cases"],
    [
        [
            "Sign-Magnitude",
            "MSB = 0, remaining n-1 bits = magnitude",
            "MSB = 1, remaining n-1 bits = magnitude",
            "-(2^(n-1) - 1) to +(2^(n-1) - 1)",
            "Two representations of zero: +0 (0 000...0) and -0 (1 000...0)",
        ],
        [
            "1's Complement",
            "MSB = 0, same as sign-magnitude",
            "MSB = 1, invert ALL bits of positive",
            "-(2^(n-1) - 1) to +(2^(n-1) - 1)",
            "Two representations of zero: +0 (0000) and -0 (1111)",
        ],
        [
            "2's Complement",
            "MSB = 0, same as sign-magnitude",
            "MSB = 1, invert all bits then add 1",
            "-2^(n-1) to +(2^(n-1) - 1)",
            "Single zero (0000). One extra negative number (-128 for 8-bit).",
        ],
    ],
)

section("13.3 Range Table")
info_table(
    ["Representation", "Smallest (most negative)", "Largest (most positive)"],
    [
        [
            "Sign-Magnitude",
            "-(2^(n-1) - 1)  e.g. -127 for 8-bit",
            "+(2^(n-1) - 1)  e.g. +127 for 8-bit",
        ],
        [
            "1's Complement",
            "-(2^(n-1) - 1)  e.g. -127 for 8-bit",
            "+(2^(n-1) - 1)  e.g. +127 for 8-bit",
        ],
        [
            "2's Complement",
            " -2^(n-1)        e.g. -128 for 8-bit",
            "+(2^(n-1) - 1)  e.g. +127 for 8-bit",
        ],
    ],
)

section("13.4 Conversion Examples (4-bit register)")
code_block(
    """
 NUMBER: +5 and -5 in 4-bit register

 SIGN-MAGNITUDE:
   +5 = 0 101    (MSB=0 for positive, 101 = 5)
   -5 = 1 101    (MSB=1 for negative, 101 = magnitude 5)

 1'S COMPLEMENT:
   +5 = 0 101    (same as sign-magnitude)
   -5 = 1 010    (invert ALL bits of +5: 0101 -> 1010)

 2'S COMPLEMENT:
   +5 = 0 101    (same as sign-magnitude)
   -5 = 1 011    (invert all bits of +5: 0101 -> 1010, then add 1: 1010+1 = 1011)

 QUICK 2'S COMPLEMENT METHOD:
   Starting from LSB, copy bits up to and including the first 1,
   then invert all remaining bits.
   +5 = 0 1 0 1
   Copy from right up to first 1: _ _ _ 1  (LSB stays 1)
   Next bit (0): copy it:          _ _ 1 1  (stays 1? No -- next 0 stays 0)
   Let me redo: 0101
   From right: first 1 is at position 0.
   Copy bit 0: 1 stays 1
   Invert remaining: 010 -> 101
   Result: 1011 = -5 in 2's complement. Correct!

 NEGATION IN 2'S COMPLEMENT:
   Take 2's complement again to get the positive version.
   -5 = 1011  -->  complement: 0100  --> add 1: 0101 = +5. Correct!
"""
)
tip(
    "PYQ Q2e): Three ways to represent negative numbers. For EACH: define it, show how to convert, give range for n-bit register, and show an 8-bit example. Always state: 2's complement has ONE zero and a larger negative range."
)
br()

# ── 14. Integer Arithmetic ───────────────────────────────────────────────────
chap_box("14. Integer Arithmetic")
section("14.1 Addition and Subtraction using 2's Complement")
definition(
    "In 2's complement arithmetic, subtraction A - B is performed as A + (-B) where -B is the 2's complement of B. This allows a single adder circuit to perform both addition and subtraction."
)
code_block(
    """
 RULES FOR 2'S COMPLEMENT ADDITION:
 1. Add the two numbers normally (including sign bits).
 2. Ignore any carry out of the sign bit (MSB).
 3. If both operands have the SAME sign but the result has a
    DIFFERENT sign -> OVERFLOW occurred.

 OVERFLOW DETECTION: V = Cn XOR Cn-1
   (XOR of carry into sign bit and carry out of sign bit)
   V = 1 means overflow.

 EXAMPLES (4-bit 2's complement):

 Example 1: +5 + (-4)
   +5 = 0101
   -4 = 1100   (2's complement of 0100)
   Sum= 0101 + 1100 = 1 0001
        Carry out = 1 (ignore)
        Result = 0001 = +1   CORRECT

 Example 2: +5 + (-4) with overflow check
   Cn (carry into sign) = 1
   Cn-1 (carry out of sign) = 1
   V = 1 XOR 1 = 0  -> NO OVERFLOW. Correct.

 Example 3: +7 + +7 (overflow case)
   +7 = 0111
   +7 = 0111
   Sum= 0111 + 0111 = 1110
   Result MSB = 1 (looks negative!) but both inputs were positive.
   Cn-1 (carry out of sign) = 0
   Cn   (carry into sign)   = 1
   V = 1 XOR 0 = 1  -> OVERFLOW detected!
"""
)

section("14.2 Multiplication — Booth's Algorithm (PYQ Q2d)")
definition(
    "<b>Booth's Algorithm:</b> An efficient method to multiply two signed binary numbers in 2's complement. It examines pairs of bits in the multiplier and adds/subtracts the multiplicand based on transitions between 0s and 1s."
)

highlight(
    """<b>Booth's Rules:</b>
  Examine current bit Qn and previous bit Qn-1 (start with Qn-1 = 0):
  - 0 0 : No operation (middle of a string of 0s)  -> A unchanged
  - 0 1 : End of a string of 1s -> A = A + M  (ADD multiplicand)
  - 1 0 : Start of a string of 1s -> A = A - M  (SUBTRACT multiplicand, i.e. A = A + 2's complement of M)
  - 1 1 : No operation (middle of a string of 1s) -> A unchanged
  After each step: Arithmetic Right Shift (AQn Qn-1) by 1 position.""",
    CARD_DARK,
    CYAN,
)

code_block(
    """
 BOOTH'S ALGORITHM EXAMPLE: +7 x +3
 =================================================================
 Multiplicand M = +7 = 0111  (4-bit)
 -M (2's complement)  = 1001
 Multiplier Q  = +3 = 0011  (4-bit)
 n = 4 bits
 Registers: A (accumulator, 4-bit, init=0), Q (multiplier), Qn-1 (1-bit, init=0)

 Initial state: A=0000, Q=0011, Qn-1=0

 Step 1: Qn=Q[0]=1, Qn-1=0 -> case 1,0 -> A = A - M = 0000 + 1001 = 1001
   A=1001, Q=0011, Qn-1=0
   Arithmetic Right Shift: A=1100, Q=1001, Qn-1=1
   (shift: 1 | 1001 | 0011 -> 11 | 1001 | 001 -> 1100 | 1001 | 1)

 Step 2: Qn=Q[0]=1, Qn-1=1 -> case 1,1 -> No operation
   Arithmetic Right Shift: A=1110, Q=0100, Qn-1=1

 Step 3: Qn=Q[0]=0, Qn-1=1 -> case 0,1 -> A = A + M = 1110 + 0111 = 10101 -> 0101 (ignore overflow carry)
   A=0101, Q=0100, Qn-1=0
   Arithmetic Right Shift: A=0010, Q=1010, Qn-1=0

 Step 4: Qn=Q[0]=0, Qn-1=0 -> case 0,0 -> No operation
   Arithmetic Right Shift: A=0001, Q=0101, Qn-1=0

 Final Result: AQ = 0001 0101 = 0001 0101 binary = 21 decimal

 VERIFICATION: +7 x +3 = +21. Correct!
 =================================================================

 SIMPLER EXAMPLE FOR EXAM: +7 x +3 using BOOTH'S METHOD
 (showing just the addition/subtraction steps more clearly)

 M  = 0111 (+7)
 -M = 1001 (-7 in 2's complement)
 Q  = 0011 (+3 = multiplier)

 Initialize: A = 0000, Q = 0011, Q-1 = 0 (extra bit)

 | Step | Q0 | Q-1 | Operation      | A      | Q    | Q-1 |
 |------|-----|-----|----------------|--------|------|-----|
 | Init |  -  |  0  | -              | 0000   | 0011 |  0  |
 |  1   |  1  |  0  | A = A - M      | 1001   | 0011 |  0  |
 |      |     |     | Arith shr      | 1100   | 1001 |  1  |
 |  2   |  1  |  1  | No op          | 1100   | 1001 |  1  |
 |      |     |     | Arith shr      | 1110   | 0100 |  1  |
 |  3   |  0  |  1  | A = A + M      | 0101   | 0100 |  1  |
 |      |     |     | Arith shr      | 0010   | 1010 |  0  |
 |  4   |  0  |  0  | No op          | 0010   | 1010 |  0  |
 |      |     |     | Arith shr      | 0001   | 0101 |  0  |

 Result = A | Q = 0001 0101 = 21. Correct! (+7 x +3 = +21)
"""
)

section("14.3 Division (Non-Restoring)")
code_block(
    """
 BINARY DIVISION: 7 / 2

 Dividend = 0111 (+7), Divisor = 0010 (+2)

 Using repeated subtraction / shift method:
   7 / 2 = Quotient 3, Remainder 1

 In binary: 0111 / 0010
   Step 1: Shift dividend left, subtract divisor
   Step 2: If result >= 0: quotient bit = 1, keep result
           If result < 0:  quotient bit = 0, restore
   ...
   Quotient = 0011 (3), Remainder = 0001 (1)
   VERIFY: 2 * 3 + 1 = 7. Correct.
"""
)
br()

# ── 15. IEEE 754 Floating-Point ───────────────────────────────────────────────
chap_box("15. Floating-Point Representation — IEEE 754", CARD_MID, PURPLE)
section("15.1 What is Floating-Point?")
definition(
    "<b>Floating-Point Representation:</b> A method to represent very large or very small numbers by storing a mantissa (significant digits) and an exponent (position of the binary point). A number is stored as: ±1.mantissa × 2^exponent"
)

web_image(
    IMAGES["ieee754.jpg"],
    local_name="ieee754.jpg",
    width=CW * 0.88,
    height=CW * 0.30,
    caption="Fig 7: IEEE 754 Single Precision 32-bit floating-point format",
    fallback_ascii="""
 IEEE 754 SINGLE PRECISION (32-bit) FORMAT:
 =================================================================
 Bit 31  | Bits 30-23   | Bits 22-0
 --------+--------------+-----------------------------------------
  1 bit  |   8 bits     |        23 bits
  SIGN   |  EXPONENT    |        MANTISSA (fraction)
  (S)    |  (biased-127)|        (stored without leading 1)
 =================================================================
 VALUE = (-1)^S  x  1.Mantissa  x  2^(Exponent - 127)
         ^sign      ^implicit 1    ^remove bias of 127
 =================================================================

 IEEE 754 DOUBLE PRECISION (64-bit) FORMAT:
 =================================================================
  1 bit  |  11 bits     |        52 bits
  SIGN   |  EXPONENT    |        MANTISSA
         |  (biased-1023)|
 =================================================================
 VALUE = (-1)^S  x  1.Mantissa  x  2^(Exponent - 1023)
""",
)

section("15.2 Single Precision (32-bit) Details")
info_table(
    ["Field", "Bits", "Value", "Notes"],
    [
        [
            "Sign (S)",
            "1 bit (bit 31)",
            "0 = positive, 1 = negative",
            "MSB of the 32-bit pattern",
        ],
        [
            "Exponent (e')",
            "8 bits (bits 30-23)",
            "Stored in excess-127 (biased) format",
            "e' = actual exponent + 127; range 0-255",
        ],
        [
            "Mantissa (m)",
            "23 bits (bits 22-0)",
            "Fractional part after the implicit leading 1",
            "Leading 1 is NOT stored (hidden bit)",
        ],
    ],
)
body("The actual stored value is: <b>(-1)^S  x  1.m  x  2^(e' - 127)</b>")
body(
    "The bias (127) is added to the exponent so it can be stored as an unsigned number. To get the actual exponent: e = e' - 127."
)

section("15.3 Converting Decimal to IEEE 754 Single Precision")
code_block(
    """
 EXAMPLE: Convert (-208.1025) to IEEE 754 Single Precision

 Step 1: Convert to binary
   208 in binary = 1101 0000
   0.1025 in binary = 0.0001 (approximately: 0.0625+... ~ 0.0001101...)
   Result: -11010000.0001...

 Step 2: Normalize (move binary point so only 1 bit before it)
   -11010000.0001 x 2^0 = -1.10100000001 x 2^7
   (moved point 7 places left, exponent = +7)

 Step 3: Identify fields
   Sign     = 1   (negative)
   Mantissa = 10100000001 (bits after the "1.")
   Actual exponent e = 7

 Step 4: Calculate biased exponent
   e' = e + 127 = 7 + 127 = 134 = (10000110) in binary

 Step 5: Assemble 32 bits
   [S=1] [e'=10000110] [m=10100000001000000000000]
    1   | 1 0 0 0 0 1 1 0 | 1 0 1 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0
"""
)

section("15.4 Converting IEEE 754 Single Precision to Decimal (PYQ Q2a)")
highlight(
    "<b>PYQ Q2a:</b> Find the decimal value of the exponent in excess-127 form for IEEE 754 representation of (1101 0000 .0001) base 2",
    CARD_MID,
    CYAN,
)
code_block(
    """
 PYQ SOLUTION: Find IEEE 754 single precision for (11010000.0001)_2

 Step 1: Normalize the binary number
   11010000.0001 x 2^0 = 1.1010000 0001 x 2^7
   (binary point moved 7 places to the left)
   Actual exponent e = 7

 Step 2: Calculate e' (biased exponent in excess-127 form)
   e' = e + 127 = 7 + 127 = 134
   134 in binary = 10000110

 ANSWER: The exponent in excess-127 form = (10000110)_2 = 134 in decimal.

 FULL IEEE 754 REPRESENTATION:
   Sign = 0 (positive)
   e'   = 10000110
   m    = 1010000 0001 (after the implicit 1.)
   32-bit: 0 | 10000110 | 10100000001000000000000

 ADDITIONAL EXAMPLE (from notes):
 Given: 0 | 10001001 | 01101101000001000000000

 Step 1: S = 0 (positive)
 Step 2: e' = 10001001 = 137 (decimal)
         e  = 137 - 127 = 10 (actual exponent)
 Step 3: Mantissa = .01101101000001 (append 1. in front)
         Number = 1.01101101000001 x 2^10
 Step 4: De-normalize: move point 10 places right
         = 10110110100.0001
 Step 5: Convert to decimal = 1460.125
"""
)

section("15.5 Double Precision (64-bit)")
info_table(
    ["Field", "Bits", "Bias", "Exponent Range"],
    [
        ["Sign", "1 bit", "-", "0=positive, 1=negative"],
        ["Exponent", "11 bits", "1023", "e' = e + 1023; actual e = e' - 1023"],
        [
            "Mantissa",
            "52 bits",
            "-",
            "52 bits of fractional part; implicit leading 1 not stored",
        ],
    ],
)
code_block(
    """
 DOUBLE PRECISION EXAMPLE: -128.1025 in 64-bit IEEE 754

 Step 1: 128 in binary = 1000 0000; 0.1025 ~ 0.0001
   -128.1025 ~ -1000 0000.0001

 Step 2: Normalize: -1.000 0000 0001 x 2^7
   e = 7

 Step 3: e' = 1023 + 7 = 1030 = (1000 0000 110) in binary (11 bits)

 Step 4: Assemble:
   S=1, e'=10000000110, m=0000000000010000... (52 bits)
   1 | 10000000110 | 0000000000010000000000000000000000000000000000000000
"""
)
br()

# ── 16. Floating-Point Arithmetic ────────────────────────────────────────────
chap_box("16. Floating-Point Arithmetic")
section("16.1 Addition and Subtraction")
code_block(
    """
 FP ADDITION/SUBTRACTION ALGORITHM:
 Step 1: Compare exponents. Shift the mantissa of the number with
         the SMALLER exponent right until both exponents match.
         (De-normalize the smaller number)
 Step 2: Add (or subtract) the mantissas.
 Step 3: Normalize the result if needed (shift mantissa, adjust exponent).
 Step 4: Check for overflow/underflow in the exponent.
 Step 5: Round the mantissa to fit the available bits.

 EXAMPLE: (1.010 x 2^3) + (1.100 x 2^1)
   Step 1: Align exponents (both to 2^3):
           1.010 x 2^3
           0.01100 x 2^3  (shifted right 2 places)
   Step 2: Add mantissas:
           1.010 00
         + 0.011 00
         = 1.101 00
   Step 3: Already normalized: 1.101 x 2^3
   Result = 1.101 x 2^3 = 1101.0 = 13.0
"""
)
br()

# ── 17. Hardwired vs Microprogrammed Control Unit ────────────────────────────
chap_box("17. Hardwired vs Microprogrammed Control Unit")
section("17.1 Control Unit Overview")
definition(
    "<b>Control Unit (CU):</b> Generates the sequence of control signals needed to execute machine instructions. It interprets the opcode in the instruction register (IR) and produces timing signals and control signals for data paths."
)

section("17.2 Hardwired Control Unit")
definition(
    "<b>Hardwired Control Unit:</b> The control logic is implemented directly as combinational and sequential logic circuits (gates, flip-flops, decoders, sequence counters). Control signals are physically 'wired' into the hardware."
)

web_image(
    IMAGES["hardwired_cu.png"],
    local_name="hardwired_cu.png",
    width=CW * 0.85,
    height=CW * 0.45,
    caption="Fig 8: Hardwired Control Unit block diagram",
    fallback_ascii="""
 HARDWIRED CONTROL UNIT BLOCK DIAGRAM:
 =================================================================
  +-----------+      +-----------+
  |    IR     |----->| Instruction|
  | (Opcode)  |      | Decoder   |----+
  +-----------+      +-----------+    |
                                      |     Control
  +-----------+      +-----------+    +---> Signal
  |  Timing   |----->|  Matrix   |    |     Generator -----> Control
  |  Counter  |      |  Logic    |----+     (combinational     Signals
  | (Sequence)|      |(AND-OR or |          logic gates)       to ALU,
  +-----------+      | PLA)      |                             Registers,
                     +-----------+                             Memory
  +-----------+
  |  Flags /  |----> (Condition inputs to control logic)
  | Status    |
  +-----------+
 =================================================================
""",
)

section("17.3 Microprogrammed Control Unit")
definition(
    "<b>Microprogrammed Control Unit:</b> Uses a special read-only memory (Control Memory / Control Store) to store microinstructions. Each machine instruction maps to a sequence of microinstructions stored in the control memory. Executing a machine instruction means fetching and executing its microprogram."
)

web_image(
    IMAGES["microprogrammed_cu.png"],
    local_name="microprogrammed_cu.png",
    width=CW * 0.85,
    height=CW * 0.45,
    caption="Fig 9: Microprogrammed Control Unit block diagram",
    fallback_ascii="""
 MICROPROGRAMMED CONTROL UNIT BLOCK DIAGRAM:
 =================================================================
  +-----------+      +------------------+
  |    IR     |----->| Mapping Logic    |----> Initial address
  | (Opcode)  |      | (Instruction to  |      in Control Memory
  +-----------+      |  microprogram    |             |
                     |  address)        |             |
                     +------------------+             v
                                              +-------+-------+
  +-----------+                              |  CONTROL      |
  |   CAR     |<-----------------------------|  MEMORY       |
  | (Control  |   next address               | (Microprogram |
  |  Address  |                              |  Store / ROM) |
  |  Register)|                              +-------+-------+
  +-----------+                                      |
                                                     v
                                            +--------+--------+
                                            | MICROINSTRUCTION|
                                            | REGISTER (MIR)  |
                                            +--------+--------+
                                                     |
                               +---------------------+------------------+
                               |                     |                  |
                         Control Bits           Next Address        Condition
                         (to ALU, Regs,         Field               Field
                          Memory, Buses)        (CAR update)
 =================================================================
""",
)

section("17.4 Detailed Comparison (PYQ Q2b)")
highlight(
    "<b>PYQ Q2b:</b> Compare hardwired and microprogrammed control units.",
    CARD_MID,
    CYAN,
)
info_table(
    ["Feature", "Hardwired Control Unit", "Microprogrammed Control Unit"],
    [
        [
            "Implementation",
            "Logic circuits (gates, flip-flops, decoders, PLAs). Physically wired.",
            "Control memory (ROM/RAM) stores microinstructions. Software-like approach.",
        ],
        [
            "Speed",
            "FASTER — no memory access needed; direct gate propagation delay only.",
            "SLOWER — must fetch microinstructions from control memory for each step.",
        ],
        [
            "Flexibility",
            "INFLEXIBLE — to change, must redesign and rewire the hardware.",
            "FLEXIBLE — change the microprogram in control memory to modify behaviour.",
        ],
        [
            "Design Complexity",
            "COMPLEX — designing random logic for all instructions is difficult.",
            "SIMPLER — systematic: write microprogram for each instruction.",
        ],
        [
            "Cost",
            "Higher NRE (Non-Recurring Engineering) cost for design.",
            "Lower design cost; control memory may add hardware cost.",
        ],
        [
            "Modification",
            "Requires hardware re-design; not practical to change post-manufacture.",
            "Can update by changing control memory contents (firmware update).",
        ],
        [
            "Bug Fix",
            "Very difficult — hardware must be changed.",
            "Easy — re-flash the control store (microcode update, like Intel does).",
        ],
        [
            "Use Cases",
            "RISC processors (ARM, MIPS) where simplicity and speed matter.",
            "CISC processors (Intel x86) with complex instruction sets.",
        ],
        [
            "Technology Example",
            "RISC CPUs, modern ARM Cortex-A series",
            "Intel 8086, 80286, VAX, older CISC processors",
        ],
    ],
)
tip(
    "PYQ Q2b): Draw BOTH block diagrams + comparison table with at least 5 rows. Always state: Hardwired = FASTER but INFLEXIBLE. Microprogrammed = SLOWER but FLEXIBLE and EASIER to modify. This earns full 4 marks."
)
br()

# ── 18. Control Memory & Microprogram Sequencer ──────────────────────────────
chap_box("18. Control Memory & Microprogram Sequencer")
section("18.1 Control Memory (Control Store)")
definition(
    "<b>Control Memory:</b> A ROM (or PROM/EPROM) that stores the microinstructions forming the microprogram for each machine instruction. Addressed by the Control Address Register (CAR). Each location contains one microinstruction."
)

section("18.2 Microinstruction Format")
code_block(
    """
 MICROINSTRUCTION FORMAT:
 =================================================================
 | F1 (3 bits) | F2 (3 bits) | F3 (3 bits) | CD | BR | AD (7 bits) |
 |             |             |             |    |    |             |
 | ALU/Shift   | Destination | Source      |Cond|Type| Next Address|
 | operation   | register    | register    |    |    | in control  |
 | field       | field       | field       |    |    | memory      |
 =================================================================

 F1 — ALU/Shift operations: ADD, SUB, AND, OR, NOT, shl, shr, etc.
 F2 — Destination register: PC, AR, DR, AC, IR, TR, etc.
 F3 — Source register: Memory (MBR), PC, AR, DR, etc.
 CD — Condition for branching (I-flag, S-flag, carry, zero)
 BR — Branch type: Unconditional, Conditional, Mapping, Return
 AD — Next address in control memory (7-bit = 128 locations)

 MICROPROGRAM SEQUENCE EXAMPLE (Fetch Cycle):
 Address | Microinstruction       | RTL Operation
 --------|------------------------|---------------------------
  000    | AR <- PC               | T0: Copy PC to AR
  001    | DR <- M[AR], PC <- PC+1| T1: Fetch instruction, increment PC
  010    | IR <- DR               | T2: Load instruction into IR
  011    | AR <- IR(addr), CAR <- mapping(IR(opcode))
         |                        | T3: Decode opcode, get operand address
 =================================================================
"""
)

section("18.3 Microprogram Sequencer")
code_block(
    """
 MICROPROGRAM SEQUENCER OPERATION:
 =================================================================
 The sequencer determines the next address in control memory.

 Sources for next address (CAR update):
 1. AD field of current microinstruction (explicit next address)
 2. CAR + 1 (sequential execution of microinstructions)
 3. Mapping ROM output (for instruction fetch -> opcode mapping)
 4. Subroutine return address (for micro-subroutine calls)

 Simplified Sequencer Block:
              CAR (Control Address Register)
               |
               v
         Control Memory (ROM)
               |
               v
         Microinstruction Register (MIR)
          /     |      |      \\
         /      |      |       \\
   F1,F2,F3   CD    BR      AD (next address)
   (control (cond) (branch   |
    signals)        type)    v
                         MUX ----> next CAR value
                          ^
                          |
                    (from mapping, CAR+1, AD, etc.)
 =================================================================
"""
)
br()

# ════════════════════════════════════════════════════════════════════════════
#  PYQ MODEL ANSWERS
# ════════════════════════════════════════════════════════════════════════════
part_box("PYQ — FULL MODEL ANSWERS", CARD_DARK, RED)

chap_box("QUESTION 1 — Complete Model Answers", CARD_MID, RED)

section("Q1a) Draw Von Neumann model and describe its subsystems. [2 Marks]")
highlight("<b>Model Answer:</b>", CARD_MID, CYAN)
body(
    "The Von Neumann Architecture (proposed by John von Neumann in 1945) is a stored-program computer model where both instructions and data are stored in the same memory and accessed via a single shared bus."
)
code_block(
    """
 VON NEUMANN MODEL:
 =================================================================
  +--------+  Address Bus  +-----------------------+
  |        |-------------->|                       |
  |  CPU   |  Data Bus     |    MEMORY UNIT        |
  |        |<------------->| (Stores Instructions  |
  |  +--+  |               |  AND Data together)   |
  |  |CU|  |  Control Bus  |                       |
  |  +--+  |<------------->|  [Program segment]    |
  |  +---+ |               |  [Data segment]       |
  |  |ALU| |               +-----------------------+
  |  +---+ |
  |  Regs  |  <-----> INPUT DEVICES (Keyboard, Disk)
  |  PC,IR |  <-----> OUTPUT DEVICES (Monitor, Printer)
  |  MAR,MDR|
  +--------+
 =================================================================
"""
)
bold("Five Subsystems:")
info_table(
    ["Subsystem", "Description"],
    [
        [
            "CPU (Control Unit + ALU)",
            "Executes instructions. CU fetches, decodes, controls. ALU performs arithmetic and logic.",
        ],
        [
            "Memory Unit",
            "Stores BOTH program instructions and data in the same address space. (RAM)",
        ],
        [
            "Input Devices",
            "Provide data and programs to the computer (keyboard, mouse, disk, scanner).",
        ],
        [
            "Output Devices",
            "Display or store results (monitor, printer, disk, speaker).",
        ],
        [
            "Buses",
            "Single shared bus connects all components. Data Bus, Address Bus, Control Bus.",
        ],
    ],
)
note(
    "Von Neumann Bottleneck: Since instructions and data share the same bus and memory, only one can be accessed at a time, limiting speed."
)

section(
    "Q1b) Classify computer registers into two broad classes with examples. [4 Marks]"
)
highlight("<b>Model Answer:</b>", CARD_MID, CYAN)
bold("Class 1: User-Visible Registers")
definition(
    "Registers that can be referenced and manipulated by machine-language programmer instructions. The programmer can read/write these in their programs."
)
bullet(
    [
        "<b>General Purpose Registers (GPRs):</b> R0-R7 in typical RISC; used for data and address. e.g. EAX, EBX in x86.",
        "<b>Data Registers:</b> Hold operands for ALU operations. e.g. Accumulator (AC).",
        "<b>Address Registers:</b> Hold memory addresses. e.g. Stack Pointer (SP), Index Register.",
        "<b>Condition Code / Flag Register:</b> Status bits (C, Z, S, V) set by ALU; programmer tests for branching.",
    ]
)
bold("Class 2: Control and Status Registers (Not User-Visible)")
definition(
    "Registers used by the processor to manage instruction execution. Cannot be directly accessed by user programs. Used internally by the CPU and OS."
)
bullet(
    [
        "<b>PC (Program Counter):</b> Holds address of the next instruction to fetch. Automatically incremented.",
        "<b>IR (Instruction Register):</b> Holds the current instruction being executed.",
        "<b>MAR (Memory Address Register):</b> Holds address of memory to be accessed. Connected to address bus.",
        "<b>MDR (Memory Data Register):</b> Holds data being read from or written to memory. Connected to data bus.",
    ]
)
tip(
    "Always split clearly: USER-VISIBLE (programmer can use in instructions) vs CONTROL/STATUS (CPU-internal, OS-level only). Give 2 examples for each class."
)

section("Q1c) RTL Block Diagram for: x + yz : AR <- AR + BR [4 Marks]")
highlight("<b>Model Answer:</b>", CARD_MID, CYAN)
body(
    "The statement means: When the Boolean control condition (x + yz) is TRUE (= 1), execute the register transfer AR <- AR + BR."
)
code_block(
    """
 STEP 1: Implement Boolean control function F = x + yz

         x --------\
                    [OR]---> F (Load Enable)
         y --[AND]--/
         z --|

 Logic gates needed:
   - 1 AND gate with inputs y and z -> produces yz
   - 1 OR gate with inputs x and (yz) -> produces F = x + yz

 STEP 2: Connect F to control the n-bit adder and register load

 COMPLETE BLOCK DIAGRAM:
 =================================================================
     x ----+
           |
     y --[AND]---+
     z --|       |
                 [OR]----> F (control function output)
                                |
                    +-----------v-----------+
                    |    LOAD ENABLE        |
                    |   (when F=1, load AR) |
                    +-----------+-----------+
                                |
    AR (n-bit) ---+             |
                  |             |
    BR (n-bit) ---|--> [n-bit   |
                  |    ADDER]---v---> [AR Register]----> AR output
                  |               (loaded when F=1)
                  +-----------> (A input of adder)
                  (B input = BR, A input = AR)

 RTL:
   F     <- x + yz          (logic)
   If F=1: AR <- AR + BR    (register transfer)
 =================================================================
"""
)
tip(
    "Q1c): Examiners want to see: (1) The AND gate for yz, (2) The OR gate for x+(yz) = F, (3) The n-bit adder with AR and BR as inputs, (4) AR register with F connected as load enable. Label all connections."
)

section("Q1d) Build a 4-bit Arithmetic Circuit. Write its function table. [10 Marks]")
highlight("<b>Model Answer:</b>", CARD_MID, CYAN)
body(
    "A 4-bit arithmetic circuit uses 4 Full Adders connected in cascade. The input to the B-side of each adder (Xi) is controlled by selection signals S1 and S0 to perform different operations."
)
code_block(
    """
 DESIGN OF 4-BIT ARITHMETIC CIRCUIT:
 =================================================================

 Each bit-slice has:
   - One Full Adder (FA) with inputs Ai, Xi, Ci
   - One 2-to-1 MUX (or direct logic) to generate Xi from Bi
   - Xi depends on selection bits S1 S0 as follows:

   S1 S0 | Xi     | Operation performed
   ------+--------+-----------------------------
    0  0 | 0      | Xi = 0   -> F = A (transfer)
    0  1 | Bi     | Xi = B   -> F = A + B (add)
    1  0 | NOT Bi | Xi = B'  -> F = A + B' (with Cin=1 gives A-B)
    1  1 | 1      | Xi = 1   -> F = A + 1 (increment)

 CIRCUIT FOR Xi GENERATION (one bit slice):
         S1  S0
          |   |
     +----|---|----+
 Bi -|  MUX / Logic|---> Xi
 B'i-|  (4 options)|
     +-------------+

 FULL ADDER CONNECTION (for all 4 bits):
   A0 Xi0 C0=Cin --> FA0 --> S0, C1
   A1 Xi1 C1     --> FA1 --> S1, C2
   A2 Xi2 C2     --> FA2 --> S2, C3
   A3 Xi3 C3     --> FA3 --> S3, Cout

 COMPLETE FUNCTION TABLE:
 =================================================================
 | S1 | S0 | Cin | Xi     | Function  | Operation              |
 |----|-----|-----|--------|-----------|------------------------|
 |  0 |  0 |  0  |   0    | F = A     | Transfer A             |
 |  0 |  0 |  1  |   0    | F = A+1   | Increment A            |
 |  0 |  1 |  0  |   B    | F = A+B   | Addition               |
 |  0 |  1 |  1  |   B    | F = A+B+1 | Add with carry         |
 |  1 |  0 |  0  |   B'   | F = A+B'  | Subtract with borrow   |
 |  1 |  0 |  1  |   B'   | F = A-B   | Subtraction (2's comp) |
 |  1 |  1 |  0  |   1    | F = A-1   | Decrement A            |
 |  1 |  1 |  1  |   1    | F = A     | Transfer A             |
 =================================================================
 NOTE: For A-B: use S1=1, S0=0, Cin=1
       (A + B's complement + 1 = A - B in 2's complement)
"""
)

section(
    "Q1e) Shift Sequence: R = 11011101. Logical left -> Circular right -> Logical right -> Circular left. [10 Marks]"
)
highlight("<b>Model Answer:</b>", CARD_MID, CYAN)
code_block(
    """
 INITIAL VALUE: R = 1 1 0 1 1 1 0 1
                    (MSB)         (LSB)

 STEP 1: LOGICAL SHIFT LEFT (shl)
   Rule: All bits shift left by 1. MSB is LOST. 0 inserted at LSB.
   Before: 1 1 0 1 1 1 0 1
           |
           MSB (1) is LOST
   After:  1 0 1 1 1 0 1 0  <- 0 inserted at LSB (rightmost)
   R = 1 0 1 1 1 0 1 0

 STEP 2: CIRCULAR SHIFT RIGHT (cir)
   Rule: All bits rotate right. LSB wraps around to MSB. No bits lost.
   Before: 1 0 1 1 1 0 1 0
                           |
                           LSB (0) wraps to MSB position
   After:  0 1 0 1 1 1 0 1  <- 0 (old LSB) becomes new MSB
   R = 0 1 0 1 1 1 0 1

 STEP 3: LOGICAL SHIFT RIGHT (shr)
   Rule: All bits shift right by 1. LSB is LOST. 0 inserted at MSB.
   Before: 0 1 0 1 1 1 0 1
                           |
                           LSB (1) is LOST
   After:  0 0 1 0 1 1 1 0  <- 0 inserted at MSB (leftmost)
   R = 0 0 1 0 1 1 1 0

 STEP 4: CIRCULAR SHIFT LEFT (cil)
   Rule: All bits rotate left. MSB wraps around to LSB. No bits lost.
   Before: 0 0 1 0 1 1 1 0
           |
           MSB (0) wraps to LSB position
   After:  0 1 0 1 1 1 0 0  <- 0 (old MSB) becomes new LSB
   R = 0 1 0 1 1 1 0 0

 SUMMARY TABLE:
 +---------+---------------------------+---------------------------------+
 | State   | Value (binary)            | Operation performed            |
 +---------+---------------------------+---------------------------------+
 | Initial | 1 1 0 1 1 1 0 1           | -                              |
 | After 1 | 1 0 1 1 1 0 1 0           | Logical Shift Left (shl)       |
 | After 2 | 0 1 0 1 1 1 0 1           | Circular Shift Right (cir)     |
 | After 3 | 0 0 1 0 1 1 1 0           | Logical Shift Right (shr)      |
 | After 4 | 0 1 0 1 1 1 0 0           | Circular Shift Left (cil)      |
 +---------+---------------------------+---------------------------------+
"""
)
tip(
    "For shift questions: always show the 8-bit register BEFORE and AFTER each step. Draw an arrow showing which bit enters (0 for logical shifts, the bit that wraps for circular). State clearly which bit is LOST for logical shifts."
)

br()
chap_box("QUESTION 2 — Complete Model Answers", CARD_MID, RED)

section(
    "Q2a) Find decimal value of exponent in excess-127 for IEEE 754 of (1101 0000 .0001)_2. [3 Marks]"
)
highlight("<b>Model Answer:</b>", CARD_MID, CYAN)
code_block(
    """
 GIVEN: Binary number (1101 0000 . 0001)_2 = (1101 0000.0001)_2

 STEP 1: Normalize the binary number.
   1101 0000.0001  x  2^0    (exponent starts at 0)
   Move binary point 7 places to the LEFT:
   1.1010000 0001  x  2^7
   Actual exponent e = 7

 STEP 2: Calculate exponent in EXCESS-127 (biased) form.
   e' = e + 127
   e' = 7 + 127
   e' = 134

 STEP 3: Convert 134 to binary (8-bit).
   134 = 128 + 4 + 2 = 2^7 + 2^2 + 2^1
   134 = 1000 0110

 ANSWER: Exponent in excess-127 form = (1000 0110)_2 = 134 (decimal)

 COMPLETE IEEE 754 SINGLE PRECISION FORMAT:
 Sign bit     = 0  (positive number)
 Exponent e'  = 1000 0110  (134)
 Mantissa     = 1010 0000 0010 0000 0000 0000 (bits after "1.")

 32-bit pattern:
 | 0 | 1000 0110 | 1010 0000 0010 0000 0000 000 |
"""
)

section("Q2b) Compare Hardwired and Microprogrammed Control Units. [4 Marks]")
highlight("<b>Model Answer:</b>", CARD_MID, CYAN)
info_table(
    ["Feature", "Hardwired CU", "Microprogrammed CU"],
    [
        [
            "Basic Principle",
            "Control logic built directly from gates, flip-flops, decoders. Signals hardwired.",
            "Control signals stored as microinstructions in a Control Memory (ROM).",
        ],
        [
            "Speed",
            "Very FAST — pure hardware gate delays only. No memory fetch needed.",
            "SLOWER — must read microinstruction from control memory at each step.",
        ],
        [
            "Flexibility",
            "RIGID — to change, physical hardware must be redesigned and rebuilt.",
            "FLEXIBLE — change the microprogram in ROM to alter instruction set (firmware update).",
        ],
        [
            "Design Effort",
            "DIFFICULT — complex random logic for many instructions is hard to design and verify.",
            "EASIER — systematic: write microcode for each instruction like writing a program.",
        ],
        [
            "Bug Fixing",
            "Hardware bug requires chip redesign — very expensive.",
            "Microcode bug can be fixed by re-flashing control store (e.g. Intel microcode patches).",
        ],
        [
            "Cost",
            "Higher design cost; compact hardware once designed.",
            "Lower design cost; extra ROM chip adds some hardware cost.",
        ],
        [
            "Used In",
            "RISC processors: ARM, MIPS, SPARC",
            "CISC processors: Intel 8086, 80286, VAX, IBM System/360",
        ],
    ],
)
tip(
    "4 marks = draw BOTH block diagrams + at least 4 comparison rows. Key line: Hardwired is FASTER but INFLEXIBLE. Microprogrammed is SLOWER but FLEXIBLE and EASIER to modify/debug."
)

section("Q2c) Add +5 and -4 in 2's complement (4-bit). Check for overflow. [4 Marks]")
highlight("<b>Model Answer:</b>", CARD_MID, CYAN)
code_block(
    """
 4-BIT 2'S COMPLEMENT ADDITION: +5 + (-4)

 STEP 1: Represent numbers in 4-bit 2's complement.
   +5 = 0101   (MSB = 0: positive; 101 = 5)
   -4 = ?
     +4 = 0100
     1's complement: 1011
     +1:             1100
     -4 = 1100   (verify: 1100 = -8+4 = -4. Correct!)

 STEP 2: Add the two 4-bit patterns.
      0 1 0 1   (+5)
   +  1 1 0 0   (-4)
   ---------
    1 0 0 0 1
      ^
      Carry out of bit 3 (sign bit) = 1
      Result (4 bits) = 0001

 STEP 3: Interpret the result.
   Result = 0001 (ignoring the carry out)
   MSB = 0 -> positive number
   0001 = +1

 ANSWER: +5 + (-4) = +1.  CORRECT (5 - 4 = 1)

 STEP 4: Check for OVERFLOW.
   Overflow Rule: Overflow occurs if carry INTO sign bit != carry OUT of sign bit.
   OR: Both inputs have same sign but result has different sign.

   +5 = 0101 (positive), -4 = 1100 (negative) -> DIFFERENT SIGNS.
   When inputs have DIFFERENT signs, overflow CANNOT occur.
   -> NO OVERFLOW.

   Formal check: Cn-1 (carry out of bit 3) = 1
                 Cn-2 (carry into bit 3) = 1
                 V = Cn-1 XOR Cn-2 = 1 XOR 1 = 0 -> NO OVERFLOW. Confirmed.

 EXTRA EXAMPLE (with overflow): +7 + +7
   0111 + 0111 = 1110
   Result MSB = 1 (negative!) but both inputs were positive -> OVERFLOW!
   V = Cn-1 XOR Cn-2 = 0 XOR 1 = 1 -> OVERFLOW detected.
"""
)

section("Q2d) Booth's Multiplication: +7 x +3. [10 Marks]")
highlight("<b>Model Answer:</b>", CARD_MID, CYAN)
code_block(
    """
 BOOTH'S ALGORITHM: +7 x +3 (using 4-bit 2's complement)

 GIVEN:
   Multiplicand M  = +7 = 0111
   -M (2's compl.) = 1001
   Multiplier Q    = +3 = 0011
   Number of bits n = 4
   Registers: A (4-bit accumulator, init=0000), Q (multiplier), Q_1 (1 extra bit, init=0)

 RULES:
   Q0=1, Q_1=0 -> A = A - M  (subtract multiplicand)
   Q0=0, Q_1=1 -> A = A + M  (add multiplicand)
   Q0=1, Q_1=1 -> no operation
   Q0=0, Q_1=0 -> no operation
   After each step: Arithmetic Right Shift the combined (A | Q | Q_1) by 1 bit

 EXECUTION TABLE:
 +---------+----------+------+-----+--------+---------------------------------+
 | Step    | A        | Q    | Q_1 | Q0,Q_1 | Action                         |
 +---------+----------+------+-----+--------+---------------------------------+
 | Initial | 0000     | 0011 |  0  |   -    | Start                          |
 +---------+----------+------+-----+--------+---------------------------------+
 | Step 1  | Q0=1,Q_1=0 -> A = A - M = 0000 + 1001 = 1001                   |
 |         | A=1001   | 0011 |  0  |        | A = A + (-M) = 1001            |
 |         | Arithmetic Right Shift (A Q Q_1):                               |
 |         | 1001 | 0011 | 0 -> shift right by 1 -> 1100 | 1001 | 1         |
 |         | A=1100   | 1001 |  1  |        | After ASR                      |
 +---------+----------+------+-----+--------+---------------------------------+
 | Step 2  | Q0=1,Q_1=1 -> No operation                                      |
 |         | Arithmetic Right Shift:                                          |
 |         | 1100 | 1001 | 1 -> 1110 | 0100 | 1                              |
 |         | A=1110   | 0100 |  1  |        | After ASR                      |
 +---------+----------+------+-----+--------+---------------------------------+
 | Step 3  | Q0=0,Q_1=1 -> A = A + M = 1110 + 0111 = 10101 -> take 4 bits=0101|
 |         | A=0101   | 0100 |  1  |        | A = A + M (ignore carry out)   |
 |         | Arithmetic Right Shift:                                          |
 |         | 0101 | 0100 | 1 -> 0010 | 1010 | 0                              |
 |         | A=0010   | 1010 |  0  |        | After ASR                      |
 +---------+----------+------+-----+--------+---------------------------------+
 | Step 4  | Q0=0,Q_1=0 -> No operation                                      |
 |         | Arithmetic Right Shift:                                          |
 |         | 0010 | 1010 | 0 -> 0001 | 0101 | 0                              |
 |         | A=0001   | 0101 |  0  |        | After ASR                      |
 +---------+----------+------+-----+--------+---------------------------------+
 | RESULT  | A = 0001, Q = 0101                                               |
 |         | Product = A|Q = 0001 0101 = 00010101 in binary                  |
 |         | = 16 + 4 + 1 = 21 (decimal)                                     |
 +---------+----------+------+-----+--------+---------------------------------+

 VERIFICATION: +7 x +3 = +21. CORRECT!
"""
)
tip(
    "Booth's algorithm: Always show the table with columns: Step | A register | Q register | Q_1 bit | Q0,Q_1 | Operation | After ASR. n=4 bit numbers require exactly n=4 steps. Final result = (A concatenated with Q)."
)

section(
    "Q2e) Three ways to represent negative numbers. Range for n-bit register. [10 Marks]"
)
highlight("<b>Model Answer:</b>", CARD_MID, CYAN)
body("Negative numbers can be represented in three formats in a computer:")

bold("1. Sign-Magnitude Representation")
definition(
    "<b>Sign-Magnitude:</b> The MSB (most significant bit) is used as the SIGN bit (0=positive, 1=negative). The remaining n-1 bits store the MAGNITUDE (absolute value) of the number."
)
code_block(
    """
 SIGN-MAGNITUDE (8-bit examples):
   +25 = 0 001 1001    (MSB=0: positive, 0011001 = 25)
   -25 = 1 001 1001    (MSB=1: negative, 0011001 = 25)
   +0  = 0 000 0000    (TWO zeros!)
   -0  = 1 000 0000    (This is a problem!)

 RANGE for n-bit register:
   Smallest: -(2^(n-1) - 1)    e.g. -127 for 8-bit
   Largest:  +(2^(n-1) - 1)    e.g. +127 for 8-bit

 PROBLEM: Two representations of zero (+0 and -0). Arithmetic is complex.
"""
)

bold("2. 1's Complement Representation")
definition(
    "<b>1's Complement:</b> Positive numbers are same as sign-magnitude. Negative numbers are obtained by INVERTING ALL BITS (complementing each bit) of the positive representation."
)
code_block(
    """
 1'S COMPLEMENT (8-bit examples):
   +25 = 0001 1001    (same as sign-magnitude)
   -25 = 1110 0110    (invert every bit of 00011001)

   Verify: 0001 1001 -> invert all bits -> 1110 0110 = -25

   +0  = 0000 0000    (TWO zeros again!)
   -0  = 1111 1111

 RANGE for n-bit register:
   Smallest: -(2^(n-1) - 1)    e.g. -127 for 8-bit
   Largest:  +(2^(n-1) - 1)    e.g. +127 for 8-bit

 ADDITION NOTE: End-around carry — if there is a carry out of the MSB,
 add it back to the LSB of the result.
 PROBLEM: Still has two zeros. End-around carry makes addition complex.
"""
)

bold("3. 2's Complement Representation (Most widely used)")
definition(
    "<b>2's Complement:</b> Positive numbers same as before. Negative numbers obtained by taking 1's complement (invert all bits) and then ADDING 1. This is the standard representation in modern computers."
)
code_block(
    """
 2'S COMPLEMENT (8-bit examples):
   +25 = 0001 1001
   -25 = ?
     Step 1: Invert all bits: 1110 0110   (1's complement)
     Step 2: Add 1:           1110 0111   (2's complement = -25)
   -25 = 1110 0111

   VERIFICATION: 0001 1001 + 1110 0111 = 0000 0000 (with carry out discarded)
   25 + (-25) = 0. CORRECT!

   ONLY ONE ZERO:
   +0 = 0000 0000
   -0? Invert: 1111 1111, add 1: 0000 0000 (carry ignored) = same as +0!
   -> SINGLE representation of zero.

 RANGE for n-bit register:
   Smallest: -2^(n-1)           e.g. -128 for 8-bit (one extra negative!)
   Largest:  +(2^(n-1) - 1)     e.g. +127 for 8-bit

 WHY one extra negative? -128 = 1000 0000. Its 2's complement is also 1000 0000!
 No positive +128 in 8-bit 2's complement.

 ADVANTAGES of 2's complement:
   1. Only ONE zero (no ambiguity)
   2. Subtraction = Add the 2's complement (no special circuit needed)
   3. Wider range (one more negative number)
   4. Simple overflow detection
"""
)

info_table(
    ["Representation", "n-bit Smallest", "n-bit Largest", "Zeros", "Arithmetic"],
    [
        [
            "Sign-Magnitude",
            "-(2^(n-1)-1)  [-127 for n=8]",
            "+(2^(n-1)-1)  [+127 for n=8]",
            "TWO zeros (+0 and -0)",
            "Complex; need separate adder for +/-",
        ],
        [
            "1's Complement",
            "-(2^(n-1)-1)  [-127 for n=8]",
            "+(2^(n-1)-1)  [+127 for n=8]",
            "TWO zeros (+0 and -0)",
            "End-around carry needed",
        ],
        [
            "2's Complement",
            " -2^(n-1)     [-128 for n=8]",
            "+(2^(n-1)-1)  [+127 for n=8]",
            "ONE zero only",
            "Simple; subtraction = add complement",
        ],
    ],
)
tip(
    "Q2e) is 10 marks = define all 3 + show how to convert + 8-bit example for each + range table. State clearly: 2's complement is used in modern computers because it has a single zero and simple arithmetic."
)

# ── Quick Revision ────────────────────────────────────────────────────────────
part_box("QUICK REVISION — KEY CONCEPTS", CARD_DARK, GREEN)
chap_box("Quick Revision Summary", CARD_MID, GREEN)
info_table(
    ["Concept", "One-Line Definition", "Key Exam Points"],
    [
        [
            "Von Neumann",
            "Stored-program model: instructions & data in same memory",
            "5 components; single shared bus; Von Neumann bottleneck",
        ],
        [
            "Harvard",
            "Separate memories and buses for instructions and data",
            "Eliminates bottleneck; faster; used in microcontrollers",
        ],
        [
            "CPU Registers",
            "Fast temporary storage inside the CPU",
            "User-visible (AC, SP, flags) vs Control/Status (PC, IR, MAR, MDR)",
        ],
        [
            "RTL",
            "Symbolic notation for describing micro-operations on registers",
            "R1 <- R2 means copy; P: R1 <- R2 means conditional; M[MAR] = memory access",
        ],
        [
            "Micro-ops",
            "Elementary operations on register contents",
            "3 types: Arithmetic (add, sub), Logic (AND, OR, NOT), Shift (shl, shr, cil, cir)",
        ],
        [
            "Shift Types",
            "Logical: 0 enters; Circular: bits wrap; Arithmetic: sign preserved",
            "ashr = divide by 2 (sign replicated); ashl = multiply by 2 (overflow possible)",
        ],
        [
            "ALSU",
            "Combined unit doing all arithmetic, logic, shift ops via selection bits",
            "S3S2S1S0 select operation; M=0: arithmetic; M=1: logic",
        ],
        [
            "Sign-Magnitude",
            "MSB=sign, rest=magnitude; two zeros",
            "Range: -(2^n-1 - 1) to +(2^n-1 - 1)",
        ],
        [
            "1's Complement",
            "Invert all bits for negative; two zeros; end-around carry",
            "Same range as sign-magnitude",
        ],
        [
            "2's Complement",
            "Invert all + 1 for negative; ONE zero; used in modern CPUs",
            "Range: -2^(n-1) to +(2^(n-1)-1); one extra negative number",
        ],
        [
            "IEEE 754 Single",
            "32-bit: 1 sign + 8 exponent (bias 127) + 23 mantissa",
            "Value = (-1)^S x 1.m x 2^(e'-127)",
        ],
        [
            "IEEE 754 Double",
            "64-bit: 1 sign + 11 exponent (bias 1023) + 52 mantissa",
            "Value = (-1)^S x 1.m x 2^(e'-1023)",
        ],
        [
            "Booth's Algo",
            "Efficient signed multiplication using bit-pair examination",
            "00,11=no-op; 01=add M; 10=subtract M; then arithmetic right shift; n steps for n-bit",
        ],
        [
            "Hardwired CU",
            "Control logic as gates/flip-flops; fast but inflexible",
            "Used in RISC; fast; hard to modify",
        ],
        [
            "Microprogrammed CU",
            "Control signals stored as microinstructions in control memory",
            "Used in CISC; flexible; slow; easy to fix/update via firmware",
        ],
    ],
)

highlight(
    """<b>EXAM WRITING STRATEGY:</b>
  2-mark questions:  Definition + 1 diagram = full marks
  4-mark questions:  Definition + comparison table or block diagram + example
  10-mark questions: Definition + theory + ASCII/labelled diagram + worked example + verification

  ALWAYS: Label all diagrams. Show each step of arithmetic working. Verify final answers.
  FOR SHIFTS: Show 8-bit register value after EVERY step.
  FOR BOOTH'S: Draw the full table (A | Q | Q_1 | operation | after-ASR).
  FOR IEEE 754: Show ALL steps — normalize, identify fields, compute bias, assemble bits.""",
    YELLOW_CARD,
    YELLOW,
)

# ── Build ────────────────────────────────────────────────────────────────────
doc = SimpleDocTemplate(
    "CA_Unit1_2_ExamNotes.pdf",
    pagesize=A4,
    leftMargin=PM,
    rightMargin=PM,
    topMargin=PM,
    bottomMargin=PM,
    title="Computer Architecture Unit I & II Exam Notes",
    author="UIT-RGPV IT404",
)
doc.build(story, onFirstPage=page_decor, onLaterPages=page_decor)
print("PDF built successfully: CA_Unit1_2_ExamNotes.pdf")
