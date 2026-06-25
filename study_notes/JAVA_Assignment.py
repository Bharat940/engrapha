"""
Java Programming (IT-408) — Unit III Assignment
UIT-RGPV | Java Applets — Complete Assignment Answers
Safe fonts: Helvetica / Courier only. No Unicode glyphs.
Run: python java_unit3_assignment.py
Output: Java_Unit3_Assignment.pdf
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

PAGE_W, PAGE_H = A4
PM = 1.8 * cm
CW = PAGE_W - 2 * PM

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


import re


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
cover_box(Paragraph("JAVA PROGRAMMING", COVER_H1))
sp(6)
add(Paragraph("Unit III — Java Applets | Complete Assignment Answers", COVER_H2))
add(Paragraph("Subject Code: IT-408 | UIT-RGPV (Autonomous) Bhopal", COVER_INFO))
sp(4)
rule(CYAN, 1.5)
sp(6)
add(
    Paragraph(
        "Topics: Applets, Lifecycle, Architecture, HTML Tags, Banner Applet, Threads",
        COVER_INFO,
    )
)
sp(14)
info_table(
    ["Q. No.", "Topic"],
    [
        [
            "Q1-Q5",
            "Applet basics: definition, Applet class, lifecycle, architecture, paint()",
        ],
        [
            "Q6-Q10",
            "Method differences, display methods, status window, HTML applet tag, parameters",
        ],
        [
            "Q11-Q20",
            "Programs: display message, shapes, banner, background color, HTML file, parameters",
        ],
        [
            "Q21-Q30",
            "Advanced: pause/resume, live time, mouse events, drawing applet, animated applet",
        ],
        [
            "Q31-Q33",
            "Theory: Applet vs Servlet vs Application, deprecation, modern alternatives",
        ],
    ],
)
br()

# ════════════════════════════════════════════════════════════════════════════
#  Q1
# ════════════════════════════════════════════════════════════════════════════
qbox(
    "Q1. What is a Java Applet? How is it different from a standalone Java application?"
)
section("Answer")
definition(
    "<b>Java Applet:</b> A small Java program designed to run inside a web browser or an applet viewer. "
    "It is embedded in an HTML page using the &lt;applet&gt; tag. An applet does not have a main() method; "
    "instead it uses lifecycle methods (init, start, stop, destroy) managed by the browser/applet viewer."
)
info_table(
    ["Feature", "Java Applet", "Standalone Java Application"],
    [
        [
            "Entry Point",
            "No main(); uses init(), start()",
            "Has public static void main(String[] args)",
        ],
        [
            "Execution",
            "Runs inside browser or AppletViewer",
            "Runs directly on JVM via command line",
        ],
        ["GUI", "Uses AWT/Swing; runs in browser window", "Uses AWT/Swing or console"],
        [
            "Security",
            "Sandboxed — limited file/network access",
            "Full access to system resources",
        ],
        ["HTML", "Requires HTML <applet> tag to launch", "No HTML needed"],
        ["Package", "Extends java.applet.Applet", "No extension required"],
        [
            "Deployment",
            "Embedded in web page",
            "Distributed as .jar or .class directly",
        ],
    ],
)
sp(6)

# ════════════════════════════════════════════════════════════════════════════
#  Q2
# ════════════════════════════════════════════════════════════════════════════
qbox("Q2. Explain the Applet class. Which package contains it?")
section("Answer")
body(
    "The <b>Applet class</b> is the superclass of all applets. Every applet must directly or indirectly extend this class."
)
bullet(
    [
        "<b>Package:</b> java.applet (import java.applet.Applet;)",
        "<b>Hierarchy:</b> java.lang.Object -> java.awt.Component -> java.awt.Container -> java.awt.Panel -> java.applet.Applet",
        "Provides lifecycle methods: init(), start(), stop(), destroy()",
        "Provides display methods via inherited java.awt.Graphics",
        "Provides getParameter() to read HTML parameters",
        "Provides showStatus() to display messages in browser status bar",
        "Provides getImage(), getAudioClip() for multimedia",
    ]
)
tip(
    "For Swing-based applets, extend javax.swing.JApplet instead of java.applet.Applet."
)
sp(6)

# ════════════════════════════════════════════════════════════════════════════
#  Q3
# ════════════════════════════════════════════════════════════════════════════
qbox("Q3. Describe the applet lifecycle methods: init(), start(), stop(), destroy()")
section("Answer")
definition(
    "The applet lifecycle is controlled by the browser or AppletViewer. "
    "The four lifecycle methods are called automatically at different stages."
)
info_table(
    ["Method", "Called When", "Purpose", "Called How Many Times"],
    [
        [
            "init()",
            "Applet is first loaded into memory",
            "One-time initialization: set size, load images, initialize variables",
            "Once only",
        ],
        [
            "start()",
            "After init(); also when user revisits the page",
            "Start/resume execution: start threads, begin animation",
            "Multiple times (every visit)",
        ],
        [
            "stop()",
            "User leaves the page or minimizes browser",
            "Pause execution: stop threads, pause animation to save resources",
            "Multiple times (every leave)",
        ],
        [
            "destroy()",
            "Applet is being removed from memory (browser closes tab)",
            "Final cleanup: release resources, close connections",
            "Once only",
        ],
    ],
)
code_block(
    """
 LIFECYCLE ORDER:
 =====================================
  Page Load     -> init() -> start()
  Leave Page    -> stop()
  Return to Page-> start()
  Close Browser -> stop() -> destroy()
 =====================================
"""
)
sp(6)

# ════════════════════════════════════════════════════════════════════════════
#  Q4
# ════════════════════════════════════════════════════════════════════════════
qbox("Q4. Explain Applet Architecture with a diagram.")
section("Answer")

body(
    "Applet architecture describes the overall working structure of a Java Applet, "
    "including how it is loaded, executed, and managed within a web browser environment. "
    "It explains the interaction between the Web Browser, Web Server, JVM (Java Virtual Machine), "
    "and the Applet itself."
)

subsection("1. Web Server")
bullet(
    [
        "Stores HTML file and compiled applet (.class file)",
        "Sends files to browser using HTTP protocol",
    ]
)

subsection("2. Web Browser")
bullet(
    [
        "Acts as client and host environment",
        "Detects <applet> tag in HTML",
        "Requests applet class file from server",
        "Invokes JVM to execute the applet",
    ]
)

subsection("3. Java Virtual Machine (JVM)")
bullet(
    [
        "Executes applet in a secure environment",
        "Converts bytecode into machine code",
        "Provides sandbox security (restricted access)",
        "Handles runtime execution",
    ]
)

subsection("4. Applet Context")
bullet(
    [
        "Environment provided by browser",
        "Enables communication between applet and browser",
        "Provides methods like showStatus() and getImage()",
    ]
)

subsection("5. Applet Lifecycle Methods")
bullet(
    [
        "init() → initialization (called once)",
        "start() → start or resume execution",
        "paint(Graphics g) → display output",
        "stop() → pause execution",
        "destroy() → cleanup resources",
    ]
)

subsection("6. AWT/Swing")
bullet(
    [
        "Provides GUI and drawing tools",
        "Uses Graphics object for rendering",
        "Methods include drawString(), drawRect(), drawOval()",
    ]
)
code_block(
    """
 APPLET ARCHITECTURE DIAGRAM:
 =========================================================
  +------------------+        +-------------------------+
  |   WEB BROWSER    |        |   WEB SERVER            |
  |                  |  HTTP  |                         |
  | HTML Page with   |<------>| Serves .html + .class   |
  | <applet> tag     |        | files to browser        |
  +--------+---------+        +-------------------------+
           |
           | Browser detects <applet> tag
           v
  +--------+---------+
  |    JVM (Java     |
  |  Virtual Machine)|
  |  inside Browser  |
  |                  |
  |  Applet Context  |<------> showStatus(), getImage()
  |  (Browser env.)  |
  +--------+---------+
           |
           | Calls lifecycle methods
           v
  +--------+---------+
  |   YOUR APPLET    |
  |                  |
  | init()           |  <- One-time setup
  | start()          |  <- Begin execution
  | paint(Graphics g)|  <- Draw on screen
  | stop()           |  <- Pause
  | destroy()        |  <- Cleanup
  +------------------+
           |
           v
  +------------------+
  |  AWT/Swing       |
  |  Graphics Object |  <- drawString, drawRect, etc.
  +------------------+
 =========================================================
"""
)
subsection("Working Flow")
bullet(
    [
        "Browser loads HTML page",
        "Applet tag is detected",
        "Applet class is requested from server",
        "JVM loads and runs the applet",
        "Lifecycle methods are executed",
        "Output is displayed using AWT/Swing",
        "stop() and destroy() called when page is closed",
    ]
)
sp(6)

# ════════════════════════════════════════════════════════════════════════════
#  Q5
# ════════════════════════════════════════════════════════════════════════════
qbox("Q5. What is the role of the paint() method in an applet?")
section("Answer")
definition(
    "<b>paint(Graphics g):</b> The method responsible for rendering (drawing) the applet's visual output "
    "on screen. It receives a Graphics object 'g' which provides all drawing tools."
)
bullet(
    [
        "Automatically called by the JVM whenever the applet needs to be drawn or redrawn",
        "Called after init() and start() on first display",
        "Called again whenever the applet window is resized, uncovered, or repaint() is called",
        "The Graphics object 'g' provides methods: drawString(), drawRect(), drawOval(), setColor(), etc.",
        "You should NEVER call paint() directly; call repaint() instead to schedule a repaint",
    ]
)
code_block(
    """
 import java.applet.Applet;
 import java.awt.Graphics;

 public class PaintExample extends Applet {
     public void paint(Graphics g) {
         g.drawString("Hello, Applet!", 50, 50);
         g.drawRect(20, 70, 100, 50);
     }
 }
"""
)
sp(6)

# ════════════════════════════════════════════════════════════════════════════
#  Q6
# ════════════════════════════════════════════════════════════════════════════
qbox("Q6. Differentiate between: init() and start() | stop() and destroy()")
section("Answer")
info_table(
    ["Feature", "init()", "start()"],
    [
        [
            "When called",
            "Once, when applet first loads",
            "After init(); also every time page is revisited",
        ],
        [
            "Purpose",
            "One-time initialization of variables, UI, images",
            "Begin/resume animation or threads",
        ],
        [
            "Frequency",
            "Called exactly ONCE in the applet's life",
            "Called MULTIPLE times (once per page visit)",
        ],
        ["Analogy", "Constructor of a class", "Starting a paused engine"],
    ],
)
info_table(
    ["Feature", "stop()", "destroy()"],
    [
        [
            "When called",
            "User leaves/minimizes the page",
            "Browser closes or applet is removed",
        ],
        [
            "Purpose",
            "Pause execution, stop threads to save CPU",
            "Final cleanup, release all resources",
        ],
        ["Frequency", "Called MULTIPLE times", "Called exactly ONCE at end of life"],
        [
            "After this",
            "start() may be called again",
            "Nothing — applet is gone from memory",
        ],
        ["Analogy", "Pausing a video", "Deleting a file permanently"],
    ],
)
sp(6)

# ════════════════════════════════════════════════════════════════════════════
#  Q7
# ════════════════════════════════════════════════════════════════════════════
qbox(
    "Q7. What are Simple Applet Display Methods? Explain: drawString(), drawRect(), drawOval()"
)
section("Answer")
body(
    "The Graphics class (java.awt.Graphics) provides all drawing methods. It is passed as a parameter to paint(Graphics g)."
)
info_table(
    ["Method", "Syntax", "Description"],
    [
        [
            "drawString()",
            "g.drawString(String str, int x, int y)",
            "Draws text 'str' starting at position (x, y). (x,y) is the baseline-left of the first character.",
        ],
        [
            "drawRect()",
            "g.drawRect(int x, int y, int width, int height)",
            "Draws the outline of a rectangle. (x,y) is top-left corner. width and height define size.",
        ],
        [
            "drawOval()",
            "g.drawOval(int x, int y, int width, int height)",
            "Draws an oval/circle inscribed in the bounding rectangle at (x,y) with given width and height.",
        ],
        [
            "fillRect()",
            "g.fillRect(int x, int y, int width, int height)",
            "Draws a filled (solid) rectangle.",
        ],
        [
            "fillOval()",
            "g.fillOval(int x, int y, int width, int height)",
            "Draws a filled (solid) oval/circle.",
        ],
        [
            "drawLine()",
            "g.drawLine(int x1, int y1, int x2, int y2)",
            "Draws a line from point (x1,y1) to point (x2,y2).",
        ],
        [
            "setColor()",
            "g.setColor(Color c)",
            "Sets the current drawing color. e.g. g.setColor(Color.RED)",
        ],
    ],
)
sp(6)

# ════════════════════════════════════════════════════════════════════════════
#  Q8
# ════════════════════════════════════════════════════════════════════════════
qbox("Q8. What is the Status Window in an applet?")
section("Answer")
definition(
    "<b>Status Window:</b> The status bar at the bottom of the browser or AppletViewer window. "
    "An applet can display short informational messages in this area using the showStatus() method."
)
bullet(
    [
        "Method: <b>showStatus(String message)</b>",
        "Inherited from the Applet class",
        "Useful for showing progress messages, mouse coordinates, or hints",
        "The message appears in the browser's status bar (bottom strip)",
        "Does not affect the applet's drawing area",
    ]
)
code_block(
    """
 public void mouseClicked(MouseEvent e) {
     showStatus("Mouse clicked at: " + e.getX() + ", " + e.getY());
 }
"""
)
sp(6)

# ════════════════════════════════════════════════════════════════════════════
#  Q9
# ════════════════════════════════════════════════════════════════════════════
qbox("Q9. Explain the HTML <applet> tag and its attributes.")
section("Answer")
definition(
    "The &lt;applet&gt; tag is used in HTML to embed a Java applet in a web page. "
    "The browser uses this tag to locate and run the compiled .class file."
)
info_table(
    ["Attribute", "Description", "Example"],
    [
        [
            "code",
            "Name of the compiled .class file (required)",
            'code="MyApplet.class"',
        ],
        [
            "width",
            "Width of the applet display area in pixels (required)",
            'width="300"',
        ],
        [
            "height",
            "Height of the applet display area in pixels (required)",
            'height="200"',
        ],
        [
            "codebase",
            "Directory path where the .class file is located (optional)",
            'codebase="classes/"',
        ],
        [
            "alt",
            "Text shown if browser cannot run the applet",
            'alt="Applet not supported"',
        ],
        ["name", "Name for applet-to-applet communication", 'name="myApp"'],
        ["archive", "JAR file containing the applet", 'archive="app.jar"'],
        [
            "<param>",
            "Passes parameters to the applet (child tag)",
            '&lt;param name="color" value="red"&gt;',
        ],
    ],
)
code_block(
    """
 <html>
 <body>
   <applet code="MyApplet.class" width="400" height="300">
     <param name="message" value="Hello World">
     Your browser does not support Java applets.
   </applet>
 </body>
 </html>
"""
)
sp(6)

# ════════════════════════════════════════════════════════════════════════════
#  Q10
# ════════════════════════════════════════════════════════════════════════════
qbox("Q10. How are parameters passed to an applet using HTML?")
section("Answer")
body(
    "Parameters are passed using &lt;param&gt; tags inside the &lt;applet&gt; tag in HTML, and read inside the applet using getParameter()."
)
bold("HTML Side:")
code_block(
    """
 <applet code="ParamApplet.class" width="300" height="200">
   <param name="username" value="Rahul">
   <param name="color"    value="blue">
 </applet>
"""
)
bold("Java Applet Side:")
code_block(
    """
 import java.applet.Applet;
 import java.awt.*;

 public class ParamApplet extends Applet {
     String username, color;

     public void init() {
         username = getParameter("username");  // reads "Rahul"
         color    = getParameter("color");     // reads "blue"
         if (username == null) username = "Guest";  // default if not set
     }

     public void paint(Graphics g) {
         g.drawString("Hello, " + username + "! Favorite color: " + color, 30, 50);
     }
 }
"""
)
tip(
    "Always check for null after getParameter() in case the param is not defined in HTML."
)
sp(6)

# ════════════════════════════════════════════════════════════════════════════
#  Q11
# ════════════════════════════════════════════════════════════════════════════
qbox('Q11. Write a simple applet to display: "Welcome to Java Applet Programming"')
code_block(
    """
 import java.applet.Applet;
 import java.awt.Graphics;
 import java.awt.Font;
 import java.awt.Color;

 /*
  * <applet code="WelcomeApplet.class" width="400" height="150"></applet>
  */
 public class WelcomeApplet extends Applet {
     public void paint(Graphics g) {
         g.setColor(Color.BLUE);
         g.setFont(new Font("Arial", Font.BOLD, 18));
         g.drawString("Welcome to Java Applet Programming", 40, 80);
     }
 }
"""
)
sp(6)

# ════════════════════════════════════════════════════════════════════════════
#  Q12
# ════════════════════════════════════════════════════════════════════════════
qbox("Q12. Create an applet that draws: Rectangle, Circle, Line")
code_block(
    """
 import java.applet.Applet;
 import java.awt.*;

 /*
  * <applet code="ShapesApplet.class" width="400" height="300"></applet>
  */
 public class ShapesApplet extends Applet {
     public void paint(Graphics g) {
         // Draw Rectangle
         g.setColor(Color.RED);
         g.drawRect(30, 30, 120, 60);
         g.drawString("Rectangle", 50, 110);

         // Draw Circle (Oval with equal width and height)
         g.setColor(Color.GREEN);
         g.drawOval(200, 30, 80, 80);
         g.drawString("Circle", 215, 130);

         // Draw Line
         g.setColor(Color.BLUE);
         g.drawLine(30, 180, 330, 180);
         g.drawString("Line", 170, 200);

         // Filled shapes
         g.setColor(Color.ORANGE);
         g.fillRect(30, 220, 80, 40);
         g.setColor(Color.MAGENTA);
         g.fillOval(200, 220, 60, 60);
     }
 }
"""
)
sp(6)

# ════════════════════════════════════════════════════════════════════════════
#  Q13
# ════════════════════════════════════════════════════════════════════════════
qbox("Q13. Write an applet to display multiple messages using paint().")
code_block(
    """
 import java.applet.Applet;
 import java.awt.*;

 /*
  * <applet code="MultiMessageApplet.class" width="400" height="250"></applet>
  */
 public class MultiMessageApplet extends Applet {
     public void paint(Graphics g) {
         g.setFont(new Font("Helvetica", Font.BOLD, 16));
         g.setColor(Color.RED);
         g.drawString("Line 1: Hello, World!", 50, 50);

         g.setColor(Color.BLUE);
         g.drawString("Line 2: Java Applet Demo", 50, 90);

         g.setColor(Color.GREEN);
         g.drawString("Line 3: UIT-RGPV IT-408", 50, 130);

         g.setColor(Color.MAGENTA);
         g.drawString("Line 4: Unit III - Applets", 50, 170);

         g.setColor(Color.BLACK);
         g.drawString("Line 5: Multiple Messages Example", 50, 210);
     }
 }
"""
)
sp(6)

# ════════════════════════════════════════════════════════════════════════════
#  Q14
# ════════════════════════════════════════════════════════════════════════════
qbox("Q14. Create an applet to display: Name, Class, Roll Number")
code_block(
    """
 import java.applet.Applet;
 import java.awt.*;

 /*
  * <applet code="StudentInfoApplet.class" width="350" height="200"></applet>
  */
 public class StudentInfoApplet extends Applet {
     public void paint(Graphics g) {
         g.setFont(new Font("Arial", Font.BOLD, 15));
         g.setColor(Color.DARK_GRAY);

         g.drawString("Name      :  Rahul Sharma",     40, 60);
         g.drawString("Class     :  B.Tech IT - 4th Year", 40, 100);
         g.drawString("Roll No.  :  0112IT211050",     40, 140);
     }
 }
"""
)
sp(6)

# ════════════════════════════════════════════════════════════════════════════
#  Q15
# ════════════════════════════════════════════════════════════════════════════
qbox("Q15. Write an applet that changes background color.")
code_block(
    """
 import java.applet.Applet;
 import java.awt.*;

 /*
  * <applet code="BackgroundColorApplet.class" width="350" height="200"></applet>
  */
 public class BackgroundColorApplet extends Applet {
     public void init() {
         // Set background color in init()
         setBackground(Color.CYAN);
     }

     public void paint(Graphics g) {
         g.setFont(new Font("Arial", Font.BOLD, 16));
         g.setColor(Color.RED);
         g.drawString("Background color is CYAN!", 50, 80);

         // Draw a filled box with different color to show contrast
         g.setColor(Color.BLUE);
         g.fillRect(50, 100, 200, 50);
         g.setColor(Color.WHITE);
         g.drawString("Blue filled box", 80, 132);
     }
 }
"""
)
sp(6)

# ════════════════════════════════════════════════════════════════════════════
#  Q16
# ════════════════════════════════════════════════════════════════════════════
qbox("Q16. Create a Simple Banner Applet with scrolling text.")
code_block(
    """
 import java.applet.Applet;
 import java.awt.*;

 /*
  * <applet code="BannerApplet.class" width="400" height="100"></applet>
  */
 public class BannerApplet extends Applet implements Runnable {
     String message = "  *** Welcome to Java Applet Banner! *** ";
     Thread t;
     int xPos;

     public void init() {
         setBackground(Color.BLACK);
         xPos = getWidth();   // start from right edge
     }

     public void start() {
         t = new Thread(this);
         t.start();
     }

     public void run() {
         while (true) {
             xPos -= 3;  // scroll speed: decrease to scroll left
             if (xPos < -message.length() * 8) {
                 xPos = getWidth();  // reset to right side
             }
             repaint();
             try {
                 Thread.sleep(50);  // 50ms delay = ~20 fps
             } catch (InterruptedException e) {
                 return;
             }
         }
     }

     public void stop() {
         t = null;  // stop the thread
     }

     public void paint(Graphics g) {
         g.setColor(Color.BLACK);
         g.fillRect(0, 0, getWidth(), getHeight());
         g.setFont(new Font("Arial", Font.BOLD, 20));
         g.setColor(Color.YELLOW);
         g.drawString(message, xPos, 55);
     }

     public void update(Graphics g) {
         paint(g);  // prevent flickering
     }
 }
"""
)
sp(6)

# ════════════════════════════════════════════════════════════════════════════
#  Q17
# ════════════════════════════════════════════════════════════════════════════
qbox("Q17. Modify the banner applet to: Change text color / Adjust scrolling speed")
code_block(
    """
 import java.applet.Applet;
 import java.awt.*;

 /*
  * <applet code="ColoredBannerApplet.class" width="400" height="100">
  *   <param name="speed" value="5">
  *   <param name="color" value="green">
  * </applet>
  */
 public class ColoredBannerApplet extends Applet implements Runnable {
     String message = "  *** Java Banner with Color & Speed! *** ";
     Thread t;
     int xPos, speed;
     Color textColor;

     public void init() {
         setBackground(Color.BLACK);
         xPos = getWidth();

         // Read speed from HTML param (default = 3)
         String speedParam = getParameter("speed");
         speed = (speedParam != null) ? Integer.parseInt(speedParam) : 3;

         // Read color from HTML param (default = yellow)
         String colorParam = getParameter("color");
         if      (colorParam == null)            textColor = Color.YELLOW;
         else if (colorParam.equals("green"))    textColor = Color.GREEN;
         else if (colorParam.equals("red"))      textColor = Color.RED;
         else if (colorParam.equals("cyan"))     textColor = Color.CYAN;
         else                                    textColor = Color.WHITE;
     }

     public void start() { t = new Thread(this); t.start(); }

     public void run() {
         while (true) {
             xPos -= speed;
             if (xPos < -message.length() * 8) xPos = getWidth();
             repaint();
             try { Thread.sleep(50); } catch (InterruptedException e) { return; }
         }
     }

     public void stop() { t = null; }

     public void paint(Graphics g) {
         g.setColor(Color.BLACK);
         g.fillRect(0, 0, getWidth(), getHeight());
         g.setFont(new Font("Arial", Font.BOLD, 20));
         g.setColor(textColor);
         g.drawString(message, xPos, 55);
     }

     public void update(Graphics g) { paint(g); }
 }
"""
)
sp(6)

# ════════════════════════════════════════════════════════════════════════════
#  Q18
# ════════════════════════════════════════════════════════════════════════════
qbox("Q18. Create an applet that uses Status Window to display messages.")
code_block(
    """
 import java.applet.Applet;
 import java.awt.*;
 import java.awt.event.*;

 /*
  * <applet code="StatusWindowApplet.class" width="350" height="200"></applet>
  */
 public class StatusWindowApplet extends Applet implements MouseMotionListener {

     public void init() {
         addMouseMotionListener(this);
         setBackground(Color.LIGHT_GRAY);
         showStatus("Move your mouse over the applet!");
     }

     public void paint(Graphics g) {
         g.setFont(new Font("Arial", Font.BOLD, 14));
         g.setColor(Color.BLUE);
         g.drawString("Move mouse to see status window!", 30, 80);
         g.drawString("Status bar updates at bottom.", 30, 110);
     }

     // MouseMotionListener methods
     public void mouseMoved(MouseEvent e) {
         showStatus("Mouse at: X=" + e.getX() + ", Y=" + e.getY());
     }

     public void mouseDragged(MouseEvent e) {
         showStatus("Dragging at: X=" + e.getX() + ", Y=" + e.getY());
     }
 }
"""
)
sp(6)

# ════════════════════════════════════════════════════════════════════════════
#  Q19
# ════════════════════════════════════════════════════════════════════════════
qbox("Q19. Write an HTML file to execute an applet using <applet> tag")
code_block(
    """
 <!-- File: index.html -->
 <!DOCTYPE html>
 <html>
 <head>
     <title>Java Applet Demo</title>
 </head>
 <body>
     <h2>Java Applet Example</h2>
     <p>The applet is running below:</p>

     <applet code="WelcomeApplet.class" width="400" height="150">
         Your browser does not support Java applets.
         Please install Java plugin or use AppletViewer.
     </applet>

     <p>If you see a gray box, Java plugin may not be installed.</p>

     <!-- To run using AppletViewer from command line: -->
     <!-- appletviewer index.html -->
 </body>
 </html>
"""
)
tip(
    "To run: Save as index.html in the same folder as WelcomeApplet.class. Then run: appletviewer index.html"
)
sp(6)

# ════════════════════════════════════════════════════════════════════════════
#  Q20
# ════════════════════════════════════════════════════════════════════════════
qbox("Q20. Create an applet that reads parameters from HTML and displays them.")
code_block(
    """
 // File: ParamDisplayApplet.java
 import java.applet.Applet;
 import java.awt.*;

 public class ParamDisplayApplet extends Applet {
     String name, branch, year;

     public void init() {
         name   = getParameter("name");
         branch = getParameter("branch");
         year   = getParameter("year");
         if (name   == null) name   = "Unknown";
         if (branch == null) branch = "Unknown";
         if (year   == null) year   = "Unknown";
     }

     public void paint(Graphics g) {
         g.setFont(new Font("Arial", Font.BOLD, 15));
         g.setColor(Color.BLUE);
         g.drawString("Name   : " + name,   30, 60);
         g.drawString("Branch : " + branch, 30, 100);
         g.drawString("Year   : " + year,   30, 140);
     }
 }
"""
)
code_block(
    """
 <!-- File: param.html -->
 <html><body>
   <applet code="ParamDisplayApplet.class" width="350" height="200">
     <param name="name"   value="Rahul Sharma">
     <param name="branch" value="Information Technology">
     <param name="year"   value="4th Year">
   </applet>
 </body></html>
"""
)
sp(6)
br()

# ════════════════════════════════════════════════════════════════════════════
#  Q21
# ════════════════════════════════════════════════════════════════════════════
qbox(
    "Q21. Improve the banner applet: Add pause/resume feature using mouse click events"
)
code_block(
    """
 import java.applet.Applet;
 import java.awt.*;
 import java.awt.event.*;

 /*
  * <applet code="PauseBannerApplet.class" width="400" height="100"></applet>
  */
 public class PauseBannerApplet extends Applet
                                implements Runnable, MouseListener {
     String message = "  *** Click to Pause / Resume the Banner! *** ";
     Thread t;
     int xPos;
     boolean paused = false;

     public void init() {
         setBackground(Color.BLACK);
         xPos = getWidth();
         addMouseListener(this);
     }

     public void start() { t = new Thread(this); t.start(); }

     public void run() {
         while (true) {
             if (!paused) {
                 xPos -= 3;
                 if (xPos < -message.length() * 8) xPos = getWidth();
                 repaint();
             }
             try { Thread.sleep(50); } catch (InterruptedException e) { return; }
         }
     }

     public void stop() { t = null; }

     public void mouseClicked(MouseEvent e) {
         paused = !paused;  // toggle pause/resume
         showStatus(paused ? "Banner PAUSED. Click to resume." : "Banner RESUMED.");
     }

     // Unused MouseListener methods
     public void mousePressed(MouseEvent e)  {}
     public void mouseReleased(MouseEvent e) {}
     public void mouseEntered(MouseEvent e)  {}
     public void mouseExited(MouseEvent e)   {}

     public void paint(Graphics g) {
         g.setColor(Color.BLACK);
         g.fillRect(0, 0, getWidth(), getHeight());
         g.setFont(new Font("Arial", Font.BOLD, 18));
         g.setColor(paused ? Color.RED : Color.YELLOW);
         g.drawString(message, xPos, 55);
         if (paused) {
             g.setColor(Color.WHITE);
             g.setFont(new Font("Arial", Font.PLAIN, 11));
             g.drawString("PAUSED - Click to resume", 130, 85);
         }
     }

     public void update(Graphics g) { paint(g); }
 }
"""
)
sp(6)

# ════════════════════════════════════════════════════════════════════════════
#  Q22
# ════════════════════════════════════════════════════════════════════════════
qbox("Q22. Create an applet to display current system time (live update)")
code_block(
    """
 import java.applet.Applet;
 import java.awt.*;
 import java.util.*;
 import java.text.SimpleDateFormat;

 /*
  * <applet code="LiveClockApplet.class" width="350" height="120"></applet>
  */
 public class LiveClockApplet extends Applet implements Runnable {
     Thread t;
     String timeStr = "";

     public void init()  { setBackground(Color.BLACK); }
     public void start() { t = new Thread(this); t.start(); }
     public void stop()  { t = null; }

     public void run() {
         SimpleDateFormat sdf = new SimpleDateFormat("HH:mm:ss  dd-MM-yyyy");
         while (Thread.currentThread() == t) {
             timeStr = sdf.format(new Date());
             repaint();
             try { Thread.sleep(1000); } catch (InterruptedException e) { return; }
         }
     }

     public void paint(Graphics g) {
         g.setColor(Color.BLACK);
         g.fillRect(0, 0, getWidth(), getHeight());
         g.setFont(new Font("Courier New", Font.BOLD, 26));
         g.setColor(Color.GREEN);
         g.drawString(timeStr, 30, 70);
         g.setFont(new Font("Arial", Font.PLAIN, 12));
         g.setColor(Color.GRAY);
         g.drawString("Live System Clock - updates every second", 20, 100);
     }

     public void update(Graphics g) { paint(g); }
 }
"""
)
sp(6)

# ════════════════════════════════════════════════════════════════════════════
#  Q23
# ════════════════════════════════════════════════════════════════════════════
qbox("Q23. Develop an applet using parameters like: Text and Color")
code_block(
    """
 import java.applet.Applet;
 import java.awt.*;

 /*
  * <applet code="TextColorParamApplet.class" width="400" height="150">
  *   <param name="text"  value="Hello from HTML Parameter!">
  *   <param name="color" value="red">
  * </applet>
  */
 public class TextColorParamApplet extends Applet {
     String text;
     Color  color;

     public void init() {
         text = getParameter("text");
         if (text == null) text = "Default Text (no param set)";

         String c = getParameter("color");
         if      (c == null)           color = Color.BLACK;
         else if (c.equals("red"))     color = Color.RED;
         else if (c.equals("green"))   color = Color.GREEN;
         else if (c.equals("blue"))    color = Color.BLUE;
         else if (c.equals("magenta")) color = Color.MAGENTA;
         else                          color = Color.BLACK;
     }

     public void paint(Graphics g) {
         g.setColor(Color.LIGHT_GRAY);
         g.fillRect(0, 0, getWidth(), getHeight());
         g.setFont(new Font("Arial", Font.BOLD, 18));
         g.setColor(color);
         g.drawString(text, 30, 80);
     }
 }
"""
)
sp(6)

# ════════════════════════════════════════════════════════════════════════════
#  Q24
# ════════════════════════════════════════════════════════════════════════════
qbox("Q24. Create an applet that shows mouse click coordinates")
code_block(
    """
 import java.applet.Applet;
 import java.awt.*;
 import java.awt.event.*;

 /*
  * <applet code="MouseCoordApplet.class" width="400" height="300"></applet>
  */
 public class MouseCoordApplet extends Applet implements MouseListener {
     int clickX = -1, clickY = -1;
     int clickCount = 0;

     public void init() {
         addMouseListener(this);
         setBackground(Color.WHITE);
     }

     public void paint(Graphics g) {
         g.setFont(new Font("Arial", Font.BOLD, 14));
         g.setColor(Color.DARK_GRAY);
         g.drawString("Click anywhere on the applet!", 80, 30);

         if (clickX >= 0) {
             // Draw a small circle at click point
             g.setColor(Color.RED);
             g.fillOval(clickX - 5, clickY - 5, 10, 10);

             // Show coordinates
             g.setColor(Color.BLUE);
             g.drawString("Clicked at: X=" + clickX + ", Y=" + clickY, 80, 260);
             g.drawString("Total Clicks: " + clickCount, 80, 280);

             // Draw crosshair
             g.setColor(Color.GRAY);
             g.drawLine(clickX - 15, clickY, clickX + 15, clickY);
             g.drawLine(clickX, clickY - 15, clickX, clickY + 15);
         }
     }

     public void mouseClicked(MouseEvent e) {
         clickX = e.getX();
         clickY = e.getY();
         clickCount++;
         repaint();
     }

     public void mousePressed(MouseEvent e)  {}
     public void mouseReleased(MouseEvent e) {}
     public void mouseEntered(MouseEvent e)  {}
     public void mouseExited(MouseEvent e)   {}
 }
"""
)
sp(6)

# ════════════════════════════════════════════════════════════════════════════
#  Q25
# ════════════════════════════════════════════════════════════════════════════
qbox("Q25. Design a simple drawing applet using mouse")
code_block(
    """
 import java.applet.Applet;
 import java.awt.*;
 import java.awt.event.*;
 import java.util.*;

 /*
  * <applet code="DrawingApplet.class" width="500" height="400"></applet>
  */
 public class DrawingApplet extends Applet implements MouseMotionListener, MouseListener {
     // Store all drawn points as (x,y) pairs
     java.util.List<int[]> points = new ArrayList<>();
     boolean drawing = false;
     int lastX, lastY;

     public void init() {
         setBackground(Color.WHITE);
         addMouseMotionListener(this);
         addMouseListener(this);
         showStatus("Press and drag to draw. Click to place dots.");
     }

     public void paint(Graphics g) {
         g.setColor(Color.BLUE);
         for (int[] p : points) {
             g.fillOval(p[0]-2, p[1]-2, 4, 4);
         }
     }

     public void mouseDragged(MouseEvent e) {
         points.add(new int[]{e.getX(), e.getY()});
         repaint();
         showStatus("Drawing at: " + e.getX() + ", " + e.getY());
     }

     public void mouseClicked(MouseEvent e) {
         Graphics g = getGraphics();
         g.setColor(Color.RED);
         g.fillOval(e.getX()-4, e.getY()-4, 8, 8);
     }

     public void mouseMoved(MouseEvent e)    {}
     public void mousePressed(MouseEvent e)  {}
     public void mouseReleased(MouseEvent e) {}
     public void mouseEntered(MouseEvent e)  {}
     public void mouseExited(MouseEvent e)   {}
 }
"""
)
sp(6)

# ════════════════════════════════════════════════════════════════════════════
#  Q26
# ════════════════════════════════════════════════════════════════════════════
qbox("Q26. Explain initialization and termination of an applet with code")
section("Answer")
bold("Initialization:")
body(
    "When an applet is loaded, the browser calls init() once. This is where you set up the applet — initialize variables, set sizes, load resources, add listeners."
)
bold("Termination:")
body(
    "When the browser closes or navigates away permanently, stop() is called followed by destroy(). destroy() should release all resources."
)
code_block(
    """
 import java.applet.Applet;
 import java.awt.*;

 public class LifecycleDemo extends Applet {
     String status = "Not started";

     // INITIALIZATION - called once when applet loads
     public void init() {
         setBackground(Color.LIGHT_GRAY);
         status = "init() called - Applet initialized";
         System.out.println(status);
     }

     // START - called after init and every time page is revisited
     public void start() {
         status = "start() called - Applet running";
         System.out.println(status);
         repaint();
     }

     // STOP - called when user leaves the page
     public void stop() {
         status = "stop() called - Applet paused";
         System.out.println(status);
     }

     // TERMINATION - called once when applet is destroyed
     public void destroy() {
         status = "destroy() called - Applet terminated";
         System.out.println(status);
         // Release resources here: close streams, stop threads, etc.
     }

     public void paint(Graphics g) {
         g.setFont(new Font("Arial", Font.BOLD, 14));
         g.setColor(Color.BLUE);
         g.drawString("Current State: " + status, 20, 80);
     }
 }
"""
)
sp(6)

# ════════════════════════════════════════════════════════════════════════════
#  Q27
# ════════════════════════════════════════════════════════════════════════════
qbox("Q27. Write a complete applet program with corresponding HTML file.")
bold("Java File: CompleteApplet.java")
code_block(
    """
 import java.applet.Applet;
 import java.awt.*;
 import java.awt.event.*;

 public class CompleteApplet extends Applet implements MouseListener {
     String msg = "Click inside the applet!";
     Color bg = Color.LIGHT_GRAY;

     public void init() {
         setBackground(bg);
         addMouseListener(this);
         setFont(new Font("Arial", Font.BOLD, 16));
     }

     public void paint(Graphics g) {
         g.setColor(Color.BLUE);
         g.drawRect(10, 10, getWidth()-20, getHeight()-20);
         g.setColor(Color.RED);
         g.drawString(msg, 40, getHeight()/2);
     }

     public void mouseClicked(MouseEvent e) {
         msg = "Clicked at (" + e.getX() + ", " + e.getY() + ")";
         repaint();
     }
     public void mousePressed(MouseEvent e)  {}
     public void mouseReleased(MouseEvent e) {}
     public void mouseEntered(MouseEvent e)  { showStatus("Mouse entered applet"); }
     public void mouseExited(MouseEvent e)   { showStatus("Mouse left applet"); }
 }
"""
)
bold("HTML File: complete.html")
code_block(
    """
 <!DOCTYPE html>
 <html>
 <head><title>Complete Applet Demo</title></head>
 <body>
   <h2>Complete Java Applet Demo</h2>
   <applet code="CompleteApplet.class" width="450" height="200">
     Your browser does not support Java applets.
     Please use: appletviewer complete.html
   </applet>
   <p>Click inside the applet to see mouse coordinates!</p>
 </body>
 </html>
"""
)
sp(6)

# ════════════════════════════════════════════════════════════════════════════
#  Q28
# ════════════════════════════════════════════════════════════════════════════
qbox("Q28. Create an applet that displays shapes based on user input.")
code_block(
    """
 import java.applet.Applet;
 import java.awt.*;
 import java.awt.event.*;

 /*
  * <applet code="ShapeInputApplet.class" width="400" height="300"></applet>
  */
 public class ShapeInputApplet extends Applet implements ActionListener {
     Button btnRect, btnCircle, btnLine;
     String currentShape = "none";

     public void init() {
         setBackground(Color.WHITE);
         setLayout(new FlowLayout());

         btnRect   = new Button("Rectangle");
         btnCircle = new Button("Circle");
         btnLine   = new Button("Line");

         btnRect.addActionListener(this);
         btnCircle.addActionListener(this);
         btnLine.addActionListener(this);

         add(btnRect);
         add(btnCircle);
         add(btnLine);
     }

     public void actionPerformed(ActionEvent e) {
         currentShape = e.getActionCommand();
         repaint();
     }

     public void paint(Graphics g) {
         g.setColor(Color.BLUE);
         g.drawString("Selected: " + currentShape, 150, 80);

         g.setColor(Color.RED);
         if (currentShape.equals("Rectangle")) {
             g.drawRect(100, 100, 180, 100);
         } else if (currentShape.equals("Circle")) {
             g.drawOval(130, 100, 120, 120);
         } else if (currentShape.equals("Line")) {
             g.drawLine(80, 150, 300, 150);
         }
     }
 }
"""
)
sp(6)

# ════════════════════════════════════════════════════════════════════════════
#  Q29
# ════════════════════════════════════════════════════════════════════════════
qbox("Q29. Design a digital banner advertisement applet.")
code_block(
    """
 import java.applet.Applet;
 import java.awt.*;

 /*
  * <applet code="AdBannerApplet.class" width="500" height="120"></applet>
  */
 public class AdBannerApplet extends Applet implements Runnable {
     String[] ads = {
         "  ** Buy Now - 50% OFF on all Electronics! **  ",
         "  ** Visit www.example.com for Best Deals! **  ",
         "  ** Limited Time Offer - Hurry Up! **         ",
     };
     int currentAd = 0;
     int xPos;
     Thread t;
     Color[] colors = { Color.YELLOW, Color.CYAN, Color.GREEN };

     public void init() {
         setBackground(Color.BLACK);
         xPos = getWidth();
     }

     public void start() { t = new Thread(this); t.start(); }
     public void stop()  { t = null; }

     public void run() {
         while (Thread.currentThread() == t) {
             xPos -= 4;
             if (xPos < -ads[currentAd].length() * 9) {
                 xPos = getWidth();
                 currentAd = (currentAd + 1) % ads.length;  // rotate ads
             }
             repaint();
             try { Thread.sleep(40); } catch (InterruptedException e) { return; }
         }
     }

     public void paint(Graphics g) {
         // Background gradient effect (alternating colors)
         g.setColor(Color.BLACK);
         g.fillRect(0, 0, getWidth(), getHeight());

         // Border
         g.setColor(Color.ORANGE);
         g.drawRect(2, 2, getWidth()-4, getHeight()-4);
         g.drawRect(4, 4, getWidth()-8, getHeight()-8);

         // Ad text
         g.setFont(new Font("Arial", Font.BOLD, 22));
         g.setColor(colors[currentAd]);
         g.drawString(ads[currentAd], xPos, 70);
     }

     public void update(Graphics g) { paint(g); }
 }
"""
)
sp(6)

# ════════════════════════════════════════════════════════════════════════════
#  Q30
# ════════════════════════════════════════════════════════════════════════════
qbox("Q30. Build an animated applet using threads")
code_block(
    """
 import java.applet.Applet;
 import java.awt.*;

 /*
  * <applet code="AnimatedBallApplet.class" width="500" height="350"></applet>
  */
 public class AnimatedBallApplet extends Applet implements Runnable {
     int ballX = 50, ballY = 50;
     int dx = 4, dy = 3;          // velocity
     int ballSize = 40;
     Thread t;
     Color ballColor = Color.RED;

     public void init()  { setBackground(Color.WHITE); }
     public void start() { t = new Thread(this); t.start(); }
     public void stop()  { t = null; }

     public void run() {
         while (Thread.currentThread() == t) {
             // Move ball
             ballX += dx;
             ballY += dy;

             // Bounce off walls
             if (ballX <= 0 || ballX >= getWidth() - ballSize) {
                 dx = -dx;
                 ballColor = new Color((int)(Math.random()*256),
                                       (int)(Math.random()*256),
                                       (int)(Math.random()*256));
             }
             if (ballY <= 0 || ballY >= getHeight() - ballSize) {
                 dy = -dy;
                 ballColor = new Color((int)(Math.random()*256),
                                       (int)(Math.random()*256),
                                       (int)(Math.random()*256));
             }

             repaint();
             try { Thread.sleep(30); } catch (InterruptedException e) { return; }
         }
     }

     public void paint(Graphics g) {
         g.setColor(Color.WHITE);
         g.fillRect(0, 0, getWidth(), getHeight());
         g.setColor(Color.BLACK);
         g.drawRect(0, 0, getWidth()-1, getHeight()-1);

         // Draw bouncing ball
         g.setColor(ballColor);
         g.fillOval(ballX, ballY, ballSize, ballSize);
         g.setColor(Color.BLACK);
         g.drawOval(ballX, ballY, ballSize, ballSize);

         g.setFont(new Font("Arial", Font.PLAIN, 11));
         g.setColor(Color.GRAY);
         g.drawString("Animated bouncing ball using Thread", 120, getHeight()-10);
     }

     public void update(Graphics g) { paint(g); }
 }
"""
)
sp(6)
br()

# ════════════════════════════════════════════════════════════════════════════
#  Q31
# ════════════════════════════════════════════════════════════════════════════
qbox("Q31. Compare: Applet, Servlet, and Java Application")
section("Answer")
info_table(
    ["Feature", "Java Applet", "Java Servlet", "Java Application"],
    [
        [
            "What it is",
            "Client-side Java program embedded in browser",
            "Server-side Java program running on web server",
            "Standalone Java program running on JVM",
        ],
        [
            "Runs on",
            "Client (browser) side",
            "Server side (inside Servlet Container like Tomcat)",
            "Local machine, any OS with JVM",
        ],
        [
            "Entry point",
            "init(), start() (no main())",
            "doGet(), doPost() (no main())",
            "public static void main(String[] args)",
        ],
        [
            "GUI",
            "Yes — has graphical display in browser",
            "No — generates HTML/text response",
            "Yes (Swing/AWT) or Console",
        ],
        [
            "Execution",
            "Embedded in HTML with <applet> tag",
            "Called via HTTP URL from browser",
            "Run directly: java ClassName",
        ],
        [
            "Use Case",
            "Interactive UI in browser (now deprecated)",
            "Web backend: process forms, database queries",
            "Desktop apps, tools, batch processing",
        ],
        [
            "Security",
            "Sandboxed — restricted access",
            "Full server access",
            "Full system access",
        ],
        [
            "Status",
            "DEPRECATED (removed in Java 9+)",
            "Widely used for web development",
            "Standard Java programming model",
        ],
        [
            "Package",
            "java.applet.Applet",
            "javax.servlet.HttpServlet",
            "No special package needed",
        ],
    ],
)
sp(6)

# ════════════════════════════════════════════════════════════════════════════
#  Q32
# ════════════════════════════════════════════════════════════════════════════
qbox("Q32. Why are Java Applets deprecated?")
section("Answer")
body(
    "Java Applets were officially deprecated in Java 9 (2017) and completely removed in Java 17 (2021). The reasons are:"
)
bullet(
    [
        "<b>Security Vulnerabilities:</b> Applets ran in the browser with access to JVM, making them a frequent target for malware and exploits. Browsers disabled Java plugins by default after multiple CVEs.",
        "<b>Browser Plugin Support Dropped:</b> All major browsers (Chrome 2015, Firefox 2017, Edge, Safari) removed support for NPAPI plugins, which was the mechanism Java used to run in browsers.",
        "<b>Performance:</b> Applets required downloading and starting a full JVM in the browser, causing slow load times compared to JavaScript.",
        "<b>User Experience:</b> Required Java Runtime Environment (JRE) to be installed on the client machine. Most users did not have it.",
        "<b>Better Alternatives Emerged:</b> HTML5, CSS3, JavaScript (and frameworks like React/Angular) can do everything applets did — without plugins, faster, and more securely.",
        "<b>Mobile Incompatibility:</b> Applets never worked on Android or iOS devices.",
        "<b>Maintenance Burden:</b> Oracle found maintaining the browser plugin a significant security and engineering cost with little benefit.",
    ]
)
sp(6)

# ════════════════════════════════════════════════════════════════════════════
#  Q33
# ════════════════════════════════════════════════════════════════════════════
qbox("Q33. Suggest modern alternatives to Applets")
section("Answer")
info_table(
    ["Alternative", "Technology", "Use Case", "Advantage over Applets"],
    [
        [
            "HTML5 Canvas",
            "HTML5 + JavaScript",
            "2D graphics, animations, games in browser",
            "No plugin needed; works on all browsers and mobile",
        ],
        [
            "WebGL",
            "JavaScript + OpenGL ES",
            "3D graphics and animations in browser",
            "Hardware-accelerated; no plugin; universal support",
        ],
        [
            "JavaScript Frameworks",
            "React, Angular, Vue.js",
            "Interactive web UIs, single-page apps",
            "Fast, no plugin, full browser support, mobile-friendly",
        ],
        [
            "JavaFX",
            "Java (Desktop)",
            "Rich desktop GUI applications",
            "Modern replacement for Swing/AWT for desktop apps",
        ],
        [
            "Java Web Start",
            "JNLP (now also deprecated)",
            "Running Java apps from browser link",
            "Was a transition tech; also now removed in Java 11",
        ],
        [
            "WebSockets + Java Backend",
            "HTML5 + Spring Boot / Servlets",
            "Real-time web apps (chat, live data)",
            "Proper client-server separation; scalable",
        ],
        [
            "Progressive Web Apps (PWA)",
            "HTML5 + JS + Service Workers",
            "App-like experience in browser",
            "Offline support, installable, no plugin",
        ],
        [
            "Flutter Web",
            "Dart/Flutter",
            "Cross-platform UI for web, mobile, desktop",
            "Single codebase; rich animations; Google-backed",
        ],
    ],
)
highlight(
    "<b>Summary:</b> For web-based interactive content, use HTML5 + JavaScript. "
    "For desktop Java applications, use JavaFX or Swing. "
    "For server-side web logic, use Servlets / Spring Boot. "
    "Java Applets served their purpose in the 1990s-2000s but are completely obsolete today.",
    YELLOW_CARD,
    YELLOW,
)
sp(6)

# ════════════════════════════════════════════════════════════════════════════
#  BUILD PDF
# ════════════════════════════════════════════════════════════════════════════
doc = SimpleDocTemplate(
    "Java_Unit3_Assignment.pdf",
    pagesize=A4,
    leftMargin=PM,
    rightMargin=PM,
    topMargin=PM,
    bottomMargin=PM,
    title="Java Programming Unit III Assignment - IT408",
    author="UIT-RGPV",
)
doc.build(story, onFirstPage=page_decor, onLaterPages=page_decor)
print("PDF built successfully: Java_Unit3_Assignment.pdf")
