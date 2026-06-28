"""
Computer Architecture (IT-404) -- Unit I Notes
UIT-RGPV (Autonomous) Bhopal | Semester IV
Complete exam notes with vector diagrams.
Run: python ca_unit1_notes.py
Output: CA_Unit1_Notes.pdf
"""

from __future__ import annotations

import engrapha_notes as en
import engrapha_diagrams as ed
from reportlab.platypus import Paragraph, Table, TableStyle

# =============================================================================
#  THEME SETUP
# =============================================================================
en.set_story([])
en.set_theme(en.CATPPUCCIN_MOCHA)

diag_theme = ed.DiagramTheme.from_notes_theme(en.get_theme())


def intersect_segments(p1, p2, p3, p4):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4
    denom = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1)
    if abs(denom) < 1e-9:
        return None
    ua = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / denom
    ub = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / denom
    if 0.0 <= ua <= 1.0 and 0.0 <= ub <= 1.0:
        return x1 + ua * (x2 - x1), y1 + ua * (y2 - y1)
    return None


def clip_polygon(poly_points, cx, cy, tx, ty):
    from engrapha_diagrams.layout import edge_clip_rect

    p1 = (cx, cy)
    p2 = (tx, ty)
    n = len(poly_points) // 2
    for i in range(n):
        p3 = (poly_points[2 * i], poly_points[2 * i + 1])
        next_idx = (i + 1) % n
        p4 = (poly_points[2 * next_idx], poly_points[2 * next_idx + 1])
        pt = intersect_segments(p1, p2, p3, p4)
        if pt is not None:
            return pt
    return edge_clip_rect(cx, cy, 56.0, 28.0, tx, ty)


def clip_alu(cx, cy, w, h, tx, ty):
    pts = [
        cx - w / 2,
        cy + h / 2,
        cx - w / 6,
        cy + h / 2,
        cx,
        cy + h / 6,
        cx + w / 6,
        cy + h / 2,
        cx + w / 2,
        cy + h / 2,
        cx + w / 4,
        cy - h / 2,
        cx - w / 4,
        cy - h / 2,
    ]
    return clip_polygon(pts, cx, cy, tx, ty)


def clip_mux(cx, cy, w, h, tx, ty):
    pts = [
        cx - w / 2,
        cy + h / 2,
        cx + w / 2,
        cy + h / 2,
        cx + w / 4,
        cy - h / 2,
        cx - w / 4,
        cy - h / 2,
    ]
    return clip_polygon(pts, cx, cy, tx, ty)


def clip_input(cx, cy, w, h, tx, ty):
    skew = 6.0
    pts = [
        cx - w / 2 + skew,
        cy + h / 2,
        cx + w / 2 + skew,
        cy + h / 2,
        cx + w / 2,
        cy - h / 2,
        cx - w / 2,
        cy - h / 2,
    ]
    return clip_polygon(pts, cx, cy, tx, ty)


# =============================================================================
#  CUSTOM CPU DIAGRAM NODE DRAWERS
# =============================================================================
def draw_alu(diag, cx, cy, w, h, fill, stroke):
    import engrapha_diagrams.shapes as S

    # V-notched ALU block
    pts = [
        cx - w / 2,
        cy + h / 2,
        cx - w / 6,
        cy + h / 2,
        cx,
        cy + h / 6,
        cx + w / 6,
        cy + h / 2,
        cx + w / 2,
        cy + h / 2,
        cx + w / 4,
        cy - h / 2,
        cx - w / 4,
        cy - h / 2,
    ]
    diag._add(S.polygon(pts, fill=fill, stroke=stroke, stroke_width=1.5))


def draw_register(diag, cx, cy, w, h, fill, stroke):
    import engrapha_diagrams.shapes as S

    # Rounded rectangle representing a register, split into 4 fields
    diag._add(
        S.rounded_rect(
            cx - w / 2,
            cy - h / 2,
            w,
            h,
            rx=3,
            fill=fill,
            stroke=stroke,
            stroke_width=1.5,
        )
    )
    for i in range(1, 4):
        x = cx - w / 2 + i * (w / 4)
        diag._add(S.solid_line(x, cy - h / 2, x, cy + h / 2, color=stroke, width=0.8))


def draw_cu(diag, cx, cy, w, h, fill, stroke):
    import engrapha_diagrams.shapes as S

    # Control unit with a horizontal partition and decoder line patterns at the bottom
    diag._add(
        S.rounded_rect(
            cx - w / 2,
            cy - h / 2,
            w,
            h,
            rx=4,
            fill=fill,
            stroke=stroke,
            stroke_width=1.5,
        )
    )
    diag._add(
        S.solid_line(
            cx - w / 2, cy - h / 6, cx + w / 2, cy - h / 6, color=stroke, width=1.0
        )
    )
    for i in range(1, 6):
        x = cx - w / 2 + i * (w / 6)
        diag._add(S.solid_line(x, cy - h / 2, x, cy - h / 6, color=stroke, width=0.6))


def draw_mux(diag, cx, cy, w, h, fill, stroke):
    import engrapha_diagrams.shapes as S

    # MUX is a trapezoid narrow at bottom
    pts = [
        cx - w / 2,
        cy + h / 2,
        cx + w / 2,
        cy + h / 2,
        cx + w / 4,
        cy - h / 2,
        cx - w / 4,
        cy - h / 2,
    ]
    diag._add(S.polygon(pts, fill=fill, stroke=stroke, stroke_width=1.5))


def draw_flags(diag, cx, cy, w, h, fill, stroke):
    import engrapha_diagrams.shapes as S

    # Status flags register with Z, N, C, V cells
    diag._add(
        S.rounded_rect(
            cx - w / 2,
            cy - h / 2,
            w,
            h,
            rx=3,
            fill=fill,
            stroke=stroke,
            stroke_width=1.5,
        )
    )
    for i in range(1, 4):
        x = cx - w / 2 + i * (w / 4)
        diag._add(S.solid_line(x, cy - h / 2, x, cy + h / 2, color=stroke, width=0.8))
    t = diag.theme
    flag_chars = ["Z", "N", "C", "V"]
    for i, char in enumerate(flag_chars):
        fx = cx - w / 2 + (i + 0.5) * (w / 4)
        diag._add(
            S.label(
                fx,
                cy - 3.0,
                char,
                font=t.font_name_bold,
                size=7.0,
                color=stroke,
                anchor="middle",
            )
        )


def draw_input(diag, cx, cy, w, h, fill, stroke):
    import engrapha_diagrams.shapes as S

    # Slanted keyboard shape
    diag._add(
        S.parallelogram(
            cx - w / 2,
            cy - h / 2,
            w,
            h,
            skew=6.0,
            fill=fill,
            stroke=stroke,
            stroke_width=1.5,
        )
    )
    diag._add(
        S.solid_line(cx - w / 2 + 2, cy, cx + w / 2 + 2, cy, color=stroke, width=0.6)
    )
    for i in range(1, 5):
        x1 = cx - w / 2 + i * (w / 5)
        x2 = x1 + 3.0
        diag._add(S.solid_line(x1, cy - h / 2, x2, cy + h / 2, color=stroke, width=0.6))


def draw_output(diag, cx, cy, w, h, fill, stroke):
    import engrapha_diagrams.shapes as S

    # Monitor screen shape
    diag._add(
        S.rounded_rect(
            cx - w / 2,
            cy - h / 6,
            w,
            h * 2 / 3,
            rx=3,
            fill=fill,
            stroke=stroke,
            stroke_width=1.5,
        )
    )
    diag._add(
        S.plain_rect(
            cx - w / 2 + 3,
            cy - h / 6 + 3,
            w - 6,
            h * 2 / 3 - 6,
            fill=fill,
            stroke=stroke,
            stroke_width=0.6,
        )
    )
    diag._add(
        S.solid_line(
            cx - w / 4, cy - h / 2, cx + w / 4, cy - h / 2, color=stroke, width=1.5
        )
    )
    diag._add(S.solid_line(cx, cy - h / 6, cx, cy - h / 2, color=stroke, width=1.5))


def draw_logic_unit(diag, cx, cy, w, h, fill, stroke):
    import engrapha_diagrams.shapes as S

    diag._add(
        S.rounded_rect(
            cx - w / 2,
            cy - h / 2,
            w,
            h,
            rx=3,
            fill=fill,
            stroke=stroke,
            stroke_width=1.5,
        )
    )
    # Simple logic gate symbols inside
    diag._add(S.solid_line(cx - 15, cy + 4, cx - 7, cy + 4, color=stroke, width=0.8))
    diag._add(S.solid_line(cx - 15, cy - 4, cx - 7, cy - 4, color=stroke, width=0.8))
    diag._add(S.circle(cx - 7, cy, 4, fill="none", stroke=stroke, stroke_width=0.8))

    diag._add(S.solid_line(cx + 5, cy + 4, cx + 10, cy + 4, color=stroke, width=0.8))
    diag._add(S.solid_line(cx + 5, cy - 4, cx + 10, cy - 4, color=stroke, width=0.8))
    diag._add(S.circle(cx + 10, cy, 4, fill="none", stroke=stroke, stroke_width=0.8))


def draw_shift_unit(diag, cx, cy, w, h, fill, stroke):
    import engrapha_diagrams.shapes as S

    diag._add(
        S.rounded_rect(
            cx - w / 2,
            cy - h / 2,
            w,
            h,
            rx=3,
            fill=fill,
            stroke=stroke,
            stroke_width=1.5,
        )
    )
    t = diag.theme
    diag._add(
        S.label(
            cx - 10,
            cy - 3.0,
            "<<",
            font=t.font_name_bold,
            size=8.0,
            color=stroke,
            anchor="middle",
        )
    )
    diag._add(
        S.label(
            cx + 10,
            cy - 3.0,
            ">>",
            font=t.font_name_bold,
            size=8.0,
            color=stroke,
            anchor="middle",
        )
    )


# =============================================================================

#  COVER PAGE
# =============================================================================
en.bookmark("Cover Page")
en.sp(28)
t = Table(
    [
        [Paragraph("COMPUTER ARCHITECTURE", en.COVER_H1)],
        [Paragraph("Unit I -- Complete Exam Notes", en.COVER_H2)],
    ],
    colWidths=[en.CW],
)
t.setStyle(
    TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, -1), en.get_theme().rl(en.get_theme().surface)),
            ("TOPPADDING", (0, 0), (-1, -1), 22),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 22),
            ("LEFTPADDING", (0, 0), (-1, -1), 20),
            ("RIGHTPADDING", (0, 0), (-1, -1), 20),
            ("BOX", (0, 0), (-1, -1), 2.5, en.get_theme().rl(en.get_theme().accent)),
        ]
    )
)
en.add(t)
en.sp(14)
en.add(Paragraph("Prepared by: Bharat Dangi  |  Subject Code: IT-404  |  UIT-RGPV (Autonomous) Bhopal", en.COVER_SUB))
en.add(Paragraph("Semester IV  |  Based on University Syllabus 2024-25", en.COVER_SUB))
en.sp(10)
en.rule(en.get_theme().rl(en.get_theme().accent), 1.5)
en.sp(8)

en.info_table(
    ["Topic", "Coverage"],
    [
        [
            "1.1 Computer Architecture vs Organization",
            "Definitions, differences, scope",
        ],
        ["1.2 Computer Generations", "Gen I-V hardware, key milestones"],
        ["1.3 Von Neumann Model", "Architecture, stored-program concept, components"],
        ["1.4 CPU Organization", "ALU, CU, datapath, internal structure"],
        ["1.5 Register Organization", "Types of registers, PC, IR, MAR, MDR, AC, SP"],
        [
            "1.6 Register Transfer Language",
            "RTL notation, conditional transfers, operations",
        ],
        ["1.7 Bus and Memory Transfers", "Common bus, read/write operations, timing"],
        ["1.8 Arithmetic Micro-operations", "Add, subtract, increment, decrement, BCD"],
        [
            "1.9 Logic Micro-operations",
            "AND, OR, XOR, NOT, selective set/clear/complement",
        ],
        ["1.10 Shift Micro-operations", "Logical, circular, arithmetic shifts"],
        [
            "1.11 Arithmetic Logic Shift Unit (ALSU)",
            "Combined hardware design, select lines",
        ],
        ["1.12 Quick Revision Summary", "Key formulas, tables, and exam flashcards"],
    ],
)
en.br()

# =============================================================================
#  UNIT DIVIDER
# =============================================================================
en.part_box("UNIT I -- COMPUTER ARCHITECTURE FUNDAMENTALS")

# =============================================================================
#  1.1  COMPUTER ARCHITECTURE vs ORGANIZATION
# =============================================================================
en.chap_box("1.1  Computer Architecture vs. Computer Organization")
en.section("Definitions")

en.definition(
    "<b>Computer Architecture:</b> Refers to those attributes of a system that have "
    "a direct impact on the <b>logical execution of a program</b>. It describes the "
    "structure and behavior of the computer as seen by the programmer -- instruction "
    "set, number of bits used for data, I/O mechanisms, and addressing techniques. "
    "Architecture is <i>what</i> the computer does."
)
en.definition(
    "<b>Computer Organization:</b> Refers to the <b>operational units and their "
    "interconnections</b> that realize the architectural specifications. It deals with "
    "hardware implementation details that are transparent to the programmer -- control "
    "signals, interfaces between CPU and memory, and the technology used. "
    "Organization is <i>how</i> the computer does it."
)

en.section("Key Differences")
en.info_table(
    ["Aspect", "Computer Architecture", "Computer Organization"],
    [
        [
            "Focus",
            "Logical structure visible to programmer",
            "Physical hardware implementation",
        ],
        [
            "Examples",
            "Instruction set, addressing modes, data types",
            "Control signals, bus width, clock speed",
        ],
        [
            "Visibility",
            "Visible to programmer (ISA level)",
            "Transparent to programmer",
        ],
        [
            "Changes",
            "Rarely changes (backward compatibility)",
            "Can change with technology",
        ],
        ["Scope", "Design of instruction set (ISA)", "Design of processor internals"],
        [
            "Analogy",
            "Architect designs the blueprint",
            "Civil engineer builds the structure",
        ],
    ],
)

en.body(
    "Two machines may have the <b>same architecture</b> (same ISA) but different "
    "organizations. For example, all x86-compatible processors share the same "
    "architecture but differ vastly in their internal organization (pipeline depth, "
    "cache size, clock frequency). This is the IBM compatibility story -- the ISA "
    "remained stable across generations while the organization evolved."
)
en.tip(
    "Architecture = ISA (what instructions exist, data formats, addressing). "
    "Organization = Implementation (how ALU is built, what bus topology is used). "
    "Same architecture can have multiple organizations."
)
en.br()

# =============================================================================
#  1.2  COMPUTER GENERATIONS
# =============================================================================
en.chap_box("1.2  Computer Generations")
en.section("Overview")
en.body(
    "The history of digital computers is divided into five generations, each "
    "characterized by a major shift in the underlying switching technology, "
    "programming model, and performance capabilities."
)

en.info_table(
    ["Generation", "Period", "Technology", "Key Features", "Examples"],
    [
        [
            "First",
            "1946-1955",
            "Vacuum tubes",
            "Machine language only. Huge, hot, slow. Batch processing. "
            "Thousands of vacuum tubes. Memory: mercury delay lines, magnetic drums.",
            "ENIAC, UNIVAC I, IBM 701",
        ],
        [
            "Second",
            "1955-1964",
            "Transistors",
            "Assembly language + FORTRAN/COBOL. Smaller, faster, cheaper. "
            "Magnetic core memory. I/O processors introduced.",
            "IBM 7094, CDC 1604, Honeywell 400",
        ],
        [
            "Third",
            "1964-1971",
            "Integrated Circuits (SSI/MSI)",
            "Standardized ISA (IBM 360). Operating systems, multiprogramming, "
            "time-sharing. Cache memory introduced. ICs on single chip.",
            "IBM System/360, DEC PDP-8",
        ],
        [
            "Fourth",
            "1971-present",
            "VLSI / ULSI Microprocessors",
            "Entire CPU on one chip. Personal computers, GUIs, networking. "
            "RISC architecture. Parallel processing. Semiconductor RAM.",
            "Intel 4004, 8086, Pentium, ARM",
        ],
        [
            "Fifth",
            "Present-future",
            "AI chips, Quantum",
            "Artificial intelligence, neural networks, quantum computing. "
            "Massively parallel architectures. Natural language interfaces.",
            "Google TPU, IBM Quantum, GPUs",
        ],
    ],
)

en.section("Key Milestones Timeline")
en.bullet(
    [
        "<b>1946:</b> ENIAC (Electronic Numerical Integrator And Computer) -- first general-purpose electronic digital computer. 18,000 vacuum tubes, 30 tons, 150kW power.",
        "<b>1947:</b> Transistor invented at Bell Labs by Shockley, Bardeen, and Brattain.",
        "<b>1951:</b> UNIVAC I -- first commercial computer delivered to US Census Bureau.",
        "<b>1958:</b> Integrated Circuit (IC) invented by Jack Kilby (TI) and Robert Noyce (Fairchild).",
        "<b>1964:</b> IBM System/360 -- first computer family with compatible ISA across models.",
        "<b>1971:</b> Intel 4004 -- first microprocessor (4-bit, 2300 transistors).",
        "<b>1981:</b> IBM PC introduced -- standardized personal computer architecture.",
        "<b>1993:</b> Pentium processor -- 32-bit superscalar with 3.1 million transistors.",
        "<b>2006:</b> Intel Core 2 Duo -- first mainstream multi-core x86 processor.",
    ]
)
en.tip(
    "Generations: (1) Vacuum tubes, (2) Transistors, (3) ICs, (4) VLSI/Microprocessors, (5) AI/Quantum. "
    "Each generation brought roughly 1000x improvement in speed and cost-efficiency."
)
en.br()

# =============================================================================
#  1.3  VON NEUMANN MODEL
# =============================================================================
en.chap_box("1.3  Von Neumann Model (Stored-Program Concept)")
en.section("The Stored-Program Concept")

en.definition(
    "<b>Von Neumann Architecture:</b> A computer architecture proposed by John von "
    "Neumann in 1945 (in the EDVAC report) in which both <b>program instructions "
    "and data are stored in the same memory</b>. The CPU fetches instructions from "
    "memory, decodes them, and executes them sequentially. This model forms the "
    "basis of virtually all modern general-purpose computers."
)

en.section("Key Principles of the Von Neumann Model")
en.bullet(
    [
        "<b>Stored-Program Concept:</b> Instructions are stored in memory just like data. The program can be modified by the computer itself during execution.",
        "<b>Sequential Execution:</b> Instructions are executed one after another in the order they appear in memory, unless a branch/jump instruction alters the sequence.",
        "<b>Single Memory Space:</b> Both instructions and data share the same address space and the same memory bus (the Von Neumann bottleneck).",
        "<b>Binary Representation:</b> All data and instructions are represented in binary.",
        "<b>Centralized Control:</b> The Control Unit (CU) directs all operations by reading instructions and generating control signals.",
    ]
)

en.section("Von Neumann Architecture -- Block Diagram")

net_vn = ed.NetworkDiagram(
    width=en.CW,
    height=280,
    theme=diag_theme,
    caption="Fig 1: Von Neumann Computer Architecture -- stored-program model",
)
# Top row: CU (left-centre) and ALU (right-centre)
net_vn.node("cu", "Control Unit\n(CU)", x=175, y=65, kind="custom", custom_draw=draw_cu)
net_vn.node(
    "alu",
    "Arithmetic Logic\nUnit (ALU)",
    x=345,
    y=65,
    kind="custom",
    custom_draw=draw_alu,
    custom_clip=clip_alu,
)
# Middle row: peripherals on each side
net_vn.node(
    "input",
    "Input Device\n(Keyboard, etc.)",
    x=65,
    y=155,
    kind="custom",
    custom_draw=draw_input,
    custom_clip=clip_input,
)
net_vn.node(
    "output",
    "Output Device\n(Display, etc.)",
    x=450,
    y=155,
    kind="custom",
    custom_draw=draw_output,
)
# Bottom: Memory
net_vn.node("mem", "Memory Unit\n(Instructions + Data)", x=255, y=230, kind="database")

# ── Data paths ──────────────────────────────────────────────────────────────
net_vn.link("input", "alu", label="Data")
net_vn.link("alu", "output", label="Data")
net_vn.link("alu", "mem", label="Data")
# ── Memory ↔ CU (instruction fetch + control; one bidirectional link avoids
#    duplicate-edge label collision at the shared midpoint) ──────────────────
net_vn.link("mem", "cu", label="Instr/Ctrl", bidirectional=True)
# ── Control signals from CU to the three remaining components ────────────────
net_vn.link("cu", "alu", label="Control", bidirectional=False)
net_vn.link("cu", "input", label="Control", bidirectional=False)
net_vn.link("cu", "output", label="Control", bidirectional=False)
en.story.extend(net_vn.as_flowable())


en.section("Von Neumann Components")
en.info_table(
    ["Component", "Function", "Details"],
    [
        [
            "Memory Unit",
            "Stores instructions and data",
            "Addressed in words. CPU reads/writes via MAR and MDR. "
            "Both program and data reside here.",
        ],
        [
            "Arithmetic Logic Unit (ALU)",
            "Performs all arithmetic and logic operations",
            "ADD, SUB, AND, OR, XOR, shift, compare. "
            "Operates on data fetched from registers.",
        ],
        [
            "Control Unit (CU)",
            "Fetches, decodes, and executes instructions",
            "Reads instruction from memory into IR, "
            "generates control signals for each micro-operation.",
        ],
        [
            "Registers",
            "Fast internal CPU storage",
            "PC (Program Counter), IR (Instruction Register), "
            "AC (Accumulator), MAR, MDR, SP.",
        ],
        [
            "Input/Output (I/O)",
            "Interfaces with external world",
            "Keyboard, monitor, disk, network. "
            "Controlled by CU via I/O instructions.",
        ],
    ],
)

en.section("The Fetch-Decode-Execute Cycle")
en.definition(
    "<b>Instruction Cycle (Fetch-Decode-Execute):</b> The fundamental operating "
    "cycle of a von Neumann computer. Every instruction passes through three phases: "
    "(1) Fetch the instruction from memory using the PC, (2) Decode the opcode to "
    "determine what operation to perform, (3) Execute the operation."
)

fc_fde = ed.Flowchart(
    width=en.CW,
    height=320,
    theme=diag_theme,
    caption="Fig 2: Fetch-Decode-Execute cycle with RTL operations",
)
fc_fde.terminal("start", "START")
fc_fde.process("fetch", "FETCH: MAR <- PC; MBR <- M[MAR]; IR <- MBR; PC <- PC + 1")
fc_fde.process("decode", "DECODE: Analyze IR opcode and addressing mode")
fc_fde.decision("type", "Instruction Type?")
fc_fde.process("mem_op", "MEMORY: MAR <- EA; MBR <- M[MAR] or M[MAR] <- MBR")
fc_fde.process("alu_op", "ALU: AC <- AC op MBR (arithmetic or logic)")
fc_fde.process("branch", "BRANCH: If condition true, PC <- EA")
fc_fde.process("exec", "EXECUTE and update flags (Z, N, C, V)")
fc_fde.terminal("halt", "Halt or next instruction")

fc_fde.edge("start", "fetch")
fc_fde.edge("fetch", "decode")
fc_fde.edge("decode", "type")
fc_fde.edge("type", "mem_op", branch="Memory")
fc_fde.edge("type", "alu_op", branch="ALU")
fc_fde.edge("type", "branch", branch="Branch")
fc_fde.edge("mem_op", "exec")
fc_fde.edge("alu_op", "exec")
fc_fde.edge("branch", "exec")
fc_fde.edge("exec", "halt")
fc_fde.edge("halt", "fetch", orthogonal=True)
en.story.extend(fc_fde.as_flowable())

en.section("Von Neumann Bottleneck")
en.highlight(
    "<b>Von Neumann Bottleneck:</b> Since instructions and data share the same "
    "memory and the same bus, the CPU must alternate between fetching instructions "
    "and fetching data. This single shared bus between CPU and memory limits overall "
    "throughput. Modern solutions include: cache memory, Harvard architecture "
    "(separate instruction and data buses), pipelining, and prefetch buffers."
)
en.tip(
    "Von Neumann = stored-program concept. Both program and data in same memory. "
    "Bottleneck = single bus for instructions and data. "
    "Harvard architecture solves this with separate instruction and data buses (used in DSPs and microcontrollers)."
)
en.br()

# =============================================================================
#  1.4  CPU ORGANIZATION
# =============================================================================
en.chap_box("1.4  CPU Organization")
en.section("Internal Structure of the CPU")
en.definition(
    "<b>CPU (Central Processing Unit):</b> The brain of the computer. It consists "
    "of the <b>Arithmetic Logic Unit (ALU)</b>, the <b>Control Unit (CU)</b>, and "
    "a set of <b>Registers</b>. The CPU fetches instructions from memory, decodes "
    "them, and controls all operations through the datapath."
)

en.section("ALU -- Arithmetic Logic Unit")
en.definition(
    "<b>ALU:</b> The functional core of the CPU that performs all <b>arithmetic "
    "operations</b> (add, subtract, multiply, divide) and <b>logical operations</b> "
    "(AND, OR, XOR, NOT, shift). It takes two operands from registers, applies the "
    "operation selected by control lines, and writes the result back."
)
en.bullet(
    [
        "<b>Inputs:</b> Two n-bit operands (A and B) from registers plus carry-in.",
        "<b>Outputs:</b> Result (n bits) plus status flags: Z (zero), N (negative), C (carry), V (overflow).",
        "<b>Select lines:</b> A set of control bits (from the CU) that select the operation (ADD, AND, XOR, etc.).",
        "<b>Combinational circuit:</b> ALU is a purely combinational (non-clocked) circuit -- output appears combinationally based on inputs.",
    ]
)

en.section("Control Unit (CU)")
en.definition(
    "<b>Control Unit:</b> Generates all <b>control signals</b> needed to coordinate "
    "the activity of the CPU. It reads the instruction from the IR (Instruction "
    "Register), decodes the opcode, and produces a sequence of control signals that "
    "activate the correct datapath components (ALU operation, register enables, memory "
    "read/write, I/O control)."
)
en.info_table(
    ["CU Type", "How Control Signals Are Generated", "Speed", "Flexibility"],
    [
        [
            "Hardwired CU",
            "Fixed combinational/sequential logic gates. Control signals wired directly.",
            "Very fast (combinational logic)",
            "Not flexible -- hard to modify",
        ],
        [
            "Microprogrammed CU",
            "Each instruction maps to a microprogram (microinstructions stored in control memory).",
            "Slower (microprogram fetch needed)",
            "Very flexible -- easy to modify microcode",
        ],
    ],
)

en.section("Datapath Organization")
en.body(
    "The <b>datapath</b> is the collection of functional units (ALU, registers, buses) "
    "and their interconnections. The datapath is controlled by the CU. A typical "
    "single-bus datapath has one internal bus shared by all registers and the ALU."
)

net_cpu = ed.NetworkDiagram(
    width=en.CW,
    height=350,
    theme=diag_theme,
    caption="Fig 3: CPU Internal Organization -- single-bus datapath",
)

# ── Top row: Control Unit, Registers, ALU + Flags ──────────────────────────
net_cpu.node(
    "cu",
    "Control\nUnit (CU)",
    x=70,
    y=310,
    kind="custom",
    custom_draw=draw_cu,
    label_pos="above",
)
net_cpu.node(
    "temp",
    "TEMP\nReg",
    x=190,
    y=270,
    kind="custom",
    custom_draw=draw_register,
    label_pos="left",
)
net_cpu.node(
    "alu",
    "ALU",
    x=310,
    y=270,
    kind="custom",
    custom_draw=draw_alu,
    custom_clip=clip_alu,
)
net_cpu.node(
    "flags",
    "Flags",
    x=430,
    y=270,
    kind="custom",
    custom_draw=draw_flags,
    label_pos="right",
)

# ── Internal Bus (horizontal bar in the middle) ───────────────────────────────
net_cpu.node("bus", "◄─── INTERNAL CPU BUS (16/32-bit) ───►", x=250, y=170, kind="bus")

# ── Bottom row: CPU registers evenly spaced ───────────────────────────────────
net_cpu.node(
    "pc", "PC\n(Prog Ctr)", x=50, y=70, kind="custom", custom_draw=draw_register
)
net_cpu.node(
    "ir", "IR\n(Instr Reg)", x=150, y=70, kind="custom", custom_draw=draw_register
)
net_cpu.node(
    "mar", "MAR\n(Mem Addr)", x=250, y=70, kind="custom", custom_draw=draw_register
)
net_cpu.node(
    "mdr", "MDR\n(Mem Data)", x=350, y=70, kind="custom", custom_draw=draw_register
)
net_cpu.node(
    "ac", "AC\n(Accum.)", x=450, y=70, kind="custom", custom_draw=draw_register
)

# ── Registers → Bus (vertical stubs, no labels for cleanliness) ──────────────
net_cpu.link("pc", "bus", label="")
net_cpu.link("ir", "bus", label="")
net_cpu.link("mar", "bus", label="")
net_cpu.link("mdr", "bus", label="")
net_cpu.link("ac", "bus", label="")

# ── TEMP feeds ALU as one operand, Bus fills TEMP ────────────────────────────
net_cpu.link("temp", "bus", label="")
net_cpu.link("temp", "alu", label="B op")

# ── ALU ──────────────────────────────────────────────────────────────────────
net_cpu.link("ac", "alu", label="A op", bidirectional=False)
net_cpu.link("alu", "flags", label="Status", bidirectional=False)
net_cpu.link("alu", "bus", label="Result", bidirectional=False)

# ── CU control/decode paths ───────────────────────────────────────────────────
net_cpu.link("ir", "cu", label="Opcode", bidirectional=False)
net_cpu.link("cu", "bus", label="Ctrl Sigs", bidirectional=False)
net_cpu.link("cu", "alu", label="ALU Sel", bidirectional=False)
en.story.extend(net_cpu.as_flowable())

en.tip(
    "<b>Key Datapath Flow:</b> The internal CPU bus (◄─── INTERNAL CPU BUS (16/32-bit) ───►) "
    "serves as the primary communication channel. All CPU registers (PC, IR, MAR, MDR, AC) "
    "and temporary registers feed into or read from this shared bus to coordinate micro-operations."
)
en.br()

# =============================================================================
#  1.5  REGISTER ORGANIZATION
# =============================================================================
en.chap_box("1.5  Register Organization")
en.section("What Are Registers?")
en.definition(
    "<b>Registers:</b> Small, extremely fast storage locations <b>inside the CPU</b> "
    "used to hold operands, addresses, and status information during instruction "
    "execution. Registers are implemented using flip-flops (D-type) and are the "
    "fastest component in the memory hierarchy. Access time is typically 1 CPU clock cycle."
)

en.section("Types of CPU Registers")
en.info_table(
    ["Register", "Full Name", "Size", "Function"],
    [
        [
            "PC",
            "Program Counter",
            "n bits",
            "Holds the address of the NEXT instruction to be fetched. "
            "Automatically incremented after each fetch. Modified by branch/jump instructions.",
        ],
        [
            "IR",
            "Instruction Register",
            "n bits",
            "Holds the CURRENT instruction being executed. "
            "The opcode and operand fields are decoded from here by the CU.",
        ],
        [
            "MAR",
            "Memory Address Register",
            "n bits",
            "Holds the MEMORY ADDRESS for the current read or write operation. "
            "Connected directly to the address bus.",
        ],
        [
            "MDR / MBR",
            "Memory Data Register / Memory Buffer Register",
            "n bits",
            "Holds the DATA being transferred to or from memory. "
            "Connected directly to the data bus. Interface between CPU and memory.",
        ],
        [
            "AC",
            "Accumulator",
            "n bits",
            "General-purpose register that accumulates results. "
            "In single-address machines, one operand is always the AC. "
            "Holds ALU result.",
        ],
        [
            "SP",
            "Stack Pointer",
            "n bits",
            "Points to the TOP of the stack in memory. "
            "Decremented on PUSH (stack grows downward), incremented on POP.",
        ],
        [
            "PSW / SR",
            "Program Status Word / Status Register",
            "n bits",
            "Holds processor flags: Z (zero), N (negative), C (carry out), "
            "V (overflow), I (interrupt enable), S (supervisor mode).",
        ],
        [
            "IX / BR",
            "Index / Base Register",
            "n bits",
            "Used in indexed and base addressing modes. "
            "Effective address = base/index register content + offset.",
        ],
        [
            "GP R0-R15",
            "General-Purpose Registers",
            "n bits",
            "In RISC architectures, a register file of 16-32 general-purpose "
            "registers replaces dedicated AC. Programmer-visible.",
        ],
    ],
)

en.section("Register Sizes and Memory Addressing")
en.code_block("""
 REGISTER SIZES AND ADDRESSING:
 ======================================================
 PC size = log2(Memory size in words)
   Example: 64K word memory -> PC = 16 bits

 MAR size = log2(Total addressable memory locations)
   Example: 4GB memory (byte-addressable) -> MAR = 32 bits

 MDR size = Word size of the machine
   Example: 32-bit machine -> MDR = 32 bits

 IR size = Instruction word length
   Example: 16-bit instruction set -> IR = 16 bits

 FLAGS in PSW (Status Register):
   Z (Zero)     : Set if result is 0
   N (Negative) : Set if result MSB = 1 (negative in 2's complement)
   C (Carry)    : Set if carry-out from MSB (unsigned overflow)
   V (Overflow) : Set if signed overflow (wrong sign result)
   I (Interrupt): If set, interrupt requests are enabled
""")

en.section("Register File Organization (RISC Style)")
en.body(
    "Modern RISC processors use a <b>register file</b> -- an array of n general-purpose "
    "registers (typically 16 or 32) with two read ports and one write port. This allows "
    "reading two source operands and writing one result per clock cycle."
)

stack_reg = ed.LayeredStack(
    width=en.CW * 0.55,
    height=200,
    theme=diag_theme,
    caption="Fig 4: Register hierarchy in the CPU memory hierarchy",
)
stack_reg.layer("CPU Registers (R0-R15)", sublabel="~1 cycle, 32-64 bytes, fastest")
stack_reg.divider()
stack_reg.layer("L1 Cache", sublabel="~4 cycles, 32-64 KB")
stack_reg.layer("L2 Cache", sublabel="~12 cycles, 256 KB - 1 MB")
stack_reg.layer("Main Memory (RAM)", sublabel="~100-300 cycles, GB range")
stack_reg.layer("Secondary Storage (Disk/SSD)", sublabel="millions of cycles, TB range")
en.story.extend(stack_reg.as_flowable())

en.tip(
    "PC = address of NEXT instruction. IR = CURRENT instruction. "
    "MAR = memory address. MDR = memory data (the value). "
    "AC = accumulator (result holder). SP = top of stack. "
    "PSW flags: Z, N, C, V -- set by ALU after every operation."
)
en.br()

# =============================================================================
#  1.6  REGISTER TRANSFER LANGUAGE (RTL)
# =============================================================================
en.chap_box("1.6  Register Transfer Language (RTL)")
en.section("What is RTL?")
en.definition(
    "<b>Register Transfer Language (RTL):</b> A formal notation used to describe "
    "the <b>micro-operations</b> performed during instruction execution. RTL "
    "specifies how data is transferred between registers and how the ALU transforms "
    "data. It is the standard language for describing hardware behavior at the "
    "register-transfer level of abstraction."
)

en.section("RTL Notation Rules")
en.info_table(
    ["RTL Symbol", "Meaning", "Example"],
    [
        ["R1, R2, ...", "Registers", "R1 holds the value 1010"],
        ["M[MAR]", "Memory location at address in MAR", "M[MAR] <- MDR (write)"],
        ["<-", "Transfer / assignment", "R2 <- R1 (copy R1 into R2)"],
        ["R1(i)", "Bit i of register R1", "IR(15) = MSB of IR (sign bit)"],
        ["R1(7:0)", "Bits 7 to 0 of R1", "Low byte of R1"],
        [",", "Simultaneous transfer", "R1 <- R2, R2 <- R1 (swap)"],
        [":", "Conditional (if-then)", "T1: R1 <- R1 + R2"],
        ["If (cond)", "Conditional transfer", "If (Z=1) then PC <- R3"],
        ["+, -, *", "Arithmetic operations", "AC <- AC + MDR"],
        ["AND, OR, XOR", "Logic operations", "R1 <- R1 AND R2"],
        ["shl, shr", "Shift operations", "R1 <- shl R1"],
    ],
)

en.section("Micro-Operation Examples")
en.code_block("""
 COMMON RTL MICRO-OPERATIONS:
 ======================================================
 1. SIMPLE TRANSFER:
    R2 <- R1              : Copy contents of R1 to R2
    MAR <- PC             : Load PC value into MAR (for memory fetch)

 2. FETCH CYCLE (Instruction Fetch in RTL):
    T0: MAR <- PC
    T1: MBR <- M[MAR], PC <- PC + 1
    T2: IR  <- MBR

 3. ARITHMETIC:
    R3 <- R1 + R2         : Add R1 and R2, store in R3
    R1 <- R1 + 1          : Increment R1
    AC <- AC - MDR        : Subtract MDR from Accumulator

 4. LOGIC:
    R1 <- R1 AND R2       : Bitwise AND
    R1 <- R1 OR mask      : Set bits using OR mask
    R1 <- R1 XOR R1       : Clear R1 to zero (XOR with itself)
    R1 <- NOT R1          : One's complement (bitwise invert)

 5. SHIFT:
    R1 <- shl R1          : Shift left (multiply by 2)
    R1 <- shr R1          : Logical shift right (divide by 2, unsigned)
    R1 <- ashr R1         : Arithmetic shift right (sign-extended)

 6. CONDITIONAL:
    If (AC < 0) then PC <- R_branch   : Branch if accumulator is negative
    If (Z = 1) then PC <- PC + offset  : Branch if Zero flag set

 7. SIMULTANEOUS (parallel transfers):
    R1 <- R2, R2 <- R1    : Swap R1 and R2 in one clock cycle
    MAR <- PC, PC <- PC+1 : Load MAR and increment PC simultaneously
""")

en.section("Timing and Control Steps")
en.body(
    "In a clocked digital system, each register transfer takes one <b>clock cycle</b>. "
    "A sequence of micro-operations is described using timing labels T0, T1, T2, ... "
    "where each T represents one clock period. The control unit generates the appropriate "
    "control signals during each Tn to activate the required transfers."
)
en.code_block("""
 EXECUTE CYCLE for ADD Instruction (single-address machine):
 ======================================================
 Assume instruction: ADD M  (AC <- AC + M[operand address])

 T0: MAR <- PC
 T1: MBR <- M[MAR], PC <- PC + 1
 T2: IR  <- MBR                          (fetch complete)

 Decode: opcode = ADD

 T3: MAR <- IR(operand field)            (get operand address)
 T4: MBR <- M[MAR]                       (fetch operand from memory)
 T5: AC  <- AC + MBR                     (execute: add operand to AC)
""")
en.tip(
    "RTL is essential for exam questions on instruction cycles. "
    "Fetch cycle is always: MAR<-PC, MBR<-M[MAR], PC<-PC+1, IR<-MBR. "
    "Know this sequence cold -- it appears in every CA exam."
)
en.br()

# =============================================================================
#  1.7  BUS AND MEMORY TRANSFERS
# =============================================================================
en.chap_box("1.7  Bus and Memory Transfers")
en.section("The Common Bus System")
en.definition(
    "<b>Bus:</b> A shared communication pathway consisting of a set of wires over "
    "which data, addresses, and control signals are transferred between CPU components "
    "and memory. A <b>common bus</b> connects multiple registers and the ALU so that "
    "any register can transfer data to any other register."
)

en.section("Types of Buses")
en.info_table(
    ["Bus Type", "Lines", "Direction", "Function"],
    [
        [
            "Data Bus",
            "n bits (word size)",
            "Bidirectional",
            "Carries actual data and instructions between CPU and memory/I/O.",
        ],
        [
            "Address Bus",
            "k bits (k = log2 of memory size)",
            "Unidirectional (CPU -> Memory)",
            "Specifies the memory location or I/O device being accessed.",
        ],
        [
            "Control Bus",
            "Various",
            "Both directions",
            "Carries control signals: MemRead, MemWrite, I/O Read, I/O Write, "
            "bus request/grant, interrupt lines, clock.",
        ],
    ],
)

en.section("Common Bus with Multiplexer / Three-State Logic")
en.body(
    "To prevent bus contention (two sources driving the bus simultaneously), "
    "each device is connected to the bus through <b>three-state (tri-state) buffers</b>. "
    "Only one device may be enabled (output = 0 or 1) at a time; all others are in "
    "the high-impedance (Z) state, effectively disconnected from the bus."
)
en.code_block("""
 THREE-STATE BUFFER TRUTH TABLE:
 ======================================================
 Enable (EN) | Input (D) | Output (Y)
 ----------------------------------------
     1        |     0     |     0       (active low)
     1        |     1     |     1       (active high)
     0        |     X     |     Z       (high-impedance = disconnected)

 BUS TRANSFER OPERATION (RTL + Control Signals):
 ======================================================
 Transfer R1 -> R3 via common bus:
   1. Assert BUS_CTRL[R1] = 1    : Enable R1's tri-state buffer (R1 drives bus)
   2. Assert LD[R3] = 1          : Enable load (clock) for R3
   3. Clock edge occurs          : R3 <- BUS value = R1
   4. Deassert BUS_CTRL[R1] = 0  : Disable R1's buffer (bus released)

 ALU Operation with Bus:
   Step 1: Load operand A into ALU input register via bus
   Step 2: Load operand B into ALU input register via bus
   Step 3: Assert ALU_OP select lines (e.g., 001 = ADD)
   Step 4: Result appears at ALU output -> loaded into destination via bus
""")

en.section("Memory Read and Write Operations")
en.info_table(
    ["Operation", "RTL Steps", "Control Signals"],
    [
        [
            "Memory READ",
            "T0: MAR <- Address\n"
            "T1: MDR <- M[MAR] (assert MemRead)\n"
            "T2: R <- MDR",
            "MemRead = 1, address on address bus, "
            "data appears on data bus after memory access time",
        ],
        [
            "Memory WRITE",
            "T0: MAR <- Address\n"
            "T1: MDR <- Data\n"
            "T2: M[MAR] <- MDR (assert MemWrite)",
            "MemWrite = 1, address on address bus, "
            "data on data bus, memory latches data",
        ],
    ],
)

# Memory bus timing diagram
td_mem = ed.TimingDiagram(
    width=en.CW,
    height=190,
    theme=diag_theme,
    caption="Fig 5: Memory Read cycle timing -- address valid, MemRead asserted, data valid",
)
td_mem.clock("CLK", period=20.0, cycles=6)
td_mem.signal("ADDR_VALID", transitions=[(0, 0), (10, 1), (110, 0)])
td_mem.signal("MEM_READ", transitions=[(0, 0), (30, 1), (90, 0)])
td_mem.signal("DATA_VALID", transitions=[(0, 0), (70, 1), (110, 0)])
td_mem.signal("MDR_LOAD", transitions=[(0, 0), (85, 1), (105, 0)])
en.story.extend(td_mem.as_flowable())

en.tip(
    "Three buses: Address (CPU->Mem, unidirectional), Data (bidirectional), Control (both). "
    "Tri-state buffers prevent bus contention. Only one device drives the bus at a time. "
    "Memory read: assert MAR, assert MemRead, wait for data, latch into MDR."
)
en.br()

# =============================================================================
#  1.8  ARITHMETIC MICRO-OPERATIONS
# =============================================================================
en.chap_box("1.8  Arithmetic Micro-Operations")
en.section("Overview")
en.definition(
    "<b>Arithmetic Micro-Operations:</b> Basic operations performed by the ALU "
    "that involve numerical computations on binary data stored in registers. "
    "These include addition, subtraction, increment, decrement, and BCD arithmetic."
)

en.section("List of Arithmetic Micro-Operations")
en.info_table(
    ["Operation", "RTL Notation", "Description"],
    [
        ["Add", "R3 <- R1 + R2", "Binary addition of R1 and R2"],
        ["Add with carry", "R3 <- R1 + R2 + Cin", "Add including carry-in flag"],
        ["Subtract", "R3 <- R1 - R2", "Binary subtraction (R1 - R2)"],
        ["Subtract with borrow", "R3 <- R1 - R2 - Bin", "Subtract with borrow-in"],
        ["Increment", "R1 <- R1 + 1", "Add 1 to register"],
        ["Decrement", "R1 <- R1 - 1", "Subtract 1 from register"],
        ["Negate (2's complement)", "R1 <- NOT(R1) + 1", "Arithmetic negation"],
        ["Transfer", "R3 <- R1", "Pass A (identity)"],
        ["Transfer Complement", "R3 <- NOT(R1)", "Bitwise complement of A"],
        [
            "Multiply (conceptual)",
            "R3:R4 <- R1 x R2",
            "Product in double-length register",
        ],
        [
            "Divide (conceptual)",
            "R3 <- R1 / R2, R4 <- R1 MOD R2",
            "Quotient and remainder",
        ],
    ],
)

en.section("Binary Addition and Carry Propagation")
en.code_block("""
 BINARY ADDITION EXAMPLE (8-bit):
 ======================================================
   1011 0110   (182)   R1
 + 0110 1010   (106)   R2
 -----------
   1 0001 0000  (288)  -> Result: 00010000 with Carry-out C = 1

 FLAGS set after this addition:
   C (Carry) = 1    : Unsigned overflow (result > 255)
   V (Overflow) = 0 : Both operands positive, result positive -> no signed overflow
   Z (Zero) = 0     : Result is not zero
   N (Negative) = 0 : MSB of result = 0

 2's COMPLEMENT SUBTRACTION (R1 - R2):
 ======================================================
   Subtraction is performed as: R1 + (NOT R2) + 1
   This avoids building a separate subtractor circuit.
   The carry-out from the MSB is the BORROW indicator (inverted).

 Example: 9 - 5 = 4  (8-bit)
   9  = 0000 1001
   5  = 0000 0101 -> NOT(5) = 1111 1010, +1 = 1111 1011 (-5 in 2's complement)
   0000 1001 + 1111 1011 = 1 0000 0100
   Result = 0000 0100 = 4, Carry-out = 1 (no borrow -> subtraction is positive)
""")

en.section("BCD Arithmetic")
en.definition(
    "<b>BCD (Binary Coded Decimal) Addition:</b> When adding two BCD digits, "
    "if the result exceeds 9 (binary 1001) or a carry-out occurs, add 6 (0110) "
    "to the 4-bit result to skip the invalid states (1010 to 1111) and propagate "
    "carry to the next BCD digit."
)
en.code_block("""
 BCD ADDITION EXAMPLE:
 ======================================================
   BCD digit 1: 0111  (7 in BCD)
 + BCD digit 2: 0110  (6 in BCD)
 -------------------------
   Sum:         1101  (13 in binary, but 13 > 9 -> INVALID in BCD!)
   Add 6:     + 0110
              -------
               1 0011  (carry=1, BCD digit=3) -> Result = 13 in BCD (1 3)

 Rule: if Sum > 9 or Carry-out = 1, add 0110 to the 4-bit sum.
""")

en.tip(
    "Subtraction = addition of 2's complement. "
    "2's complement of X = NOT(X) + 1. "
    "BCD add: if sum > 9 or carry, add 6. "
    "Flags: Z (zero result), N (MSB=1), C (carry/borrow), V (signed overflow)."
)
en.br()

# =============================================================================
#  1.9  LOGIC MICRO-OPERATIONS
# =============================================================================
en.chap_box("1.9  Logic Micro-Operations")
en.section("Overview")
en.definition(
    "<b>Logic Micro-Operations:</b> Bitwise operations performed on registers "
    "treating each bit independently. These operations are used for <b>masking</b> "
    "(selective clear/set), <b>selective complement</b>, and <b>bit testing</b>."
)

en.section("Basic Logic Operations and Truth Tables")
en.info_table(
    ["Operation", "RTL", "Bit 0 Result", "Bit 1 Result", "Common Use"],
    [
        [
            "AND",
            "R3 <- R1 AND R2",
            "0 AND 0 = 0, 0 AND 1 = 0, 1 AND 1 = 1",
            "",
            "Masking -- clear selected bits",
        ],
        [
            "OR",
            "R3 <- R1 OR R2",
            "0 OR 0 = 0, 0 OR 1 = 1, 1 OR 1 = 1",
            "",
            "Selective set bits",
        ],
        [
            "XOR",
            "R3 <- R1 XOR R2",
            "0 XOR 0 = 0, 0 XOR 1 = 1, 1 XOR 1 = 0",
            "",
            "Selective complement, compare",
        ],
        [
            "NOT (Complement)",
            "R3 <- NOT R1",
            "NOT 0 = 1, NOT 1 = 0",
            "",
            "Bitwise invert (ones complement)",
        ],
        [
            "NAND",
            "R3 <- NOT(R1 AND R2)",
            "Complement of AND",
            "",
            "Universal gate, memory cells",
        ],
        [
            "NOR",
            "R3 <- NOT(R1 OR R2)",
            "Complement of OR",
            "",
            "Universal gate, PLC logic",
        ],
        [
            "XNOR",
            "R3 <- NOT(R1 XOR R2)",
            "Complement of XOR",
            "",
            "Equality test (compare bits)",
        ],
    ],
)

en.section("Applications of Logic Micro-Operations")
en.subsection("Selective Bit Operations Using Masks")
en.code_block("""
 LOGIC MICRO-OPERATION APPLICATIONS:
 ======================================================
 Let A = 1010 1100  (data register)
     B = 0000 1111  (mask register)

 1. SELECTIVE CLEAR (AND with complement of mask):
    A AND (NOT B) = 1010 1100 AND 1111 0000 = 1010 0000
    Clears the bits where mask B = 1 (lower 4 bits cleared)

 2. SELECTIVE SET (OR with mask):
    A OR B = 1010 1100 OR 0000 1111 = 1010 1111
    Sets the bits where mask B = 1 (lower 4 bits set to 1)

 3. SELECTIVE COMPLEMENT (XOR with mask):
    A XOR B = 1010 1100 XOR 0000 1111 = 1010 0011
    Complements the bits where mask B = 1 (lower 4 bits inverted)

 4. MASK (isolate bits with AND):
    A AND B = 1010 1100 AND 0000 1111 = 0000 1100
    Isolates the lower nibble (clears all other bits)

 5. CLEAR REGISTER (XOR with itself):
    A XOR A = 0000 0000     (always zero regardless of A)

 6. CHECK IF BIT IS SET:
    If (A AND mask) != 0 -> bit is set
    Example: Check bit 3 of A: A AND 0000 1000
""")

en.section("Logic Operations in Flowchart")
fc_logic = ed.Flowchart(
    width=en.CW,
    height=230,
    theme=diag_theme,
    caption="Fig 6: Selective bit manipulation using logic micro-operations",
)
fc_logic.terminal("start", "START")
fc_logic.io_box("input", "Load register A and mask B")
fc_logic.decision("op", "Select Operation")
fc_logic.process("and_op", "A <- A AND B\n(Mask / Clear)")
fc_logic.process("or_op", "A <- A OR B\n(Selective Set)")
fc_logic.process("xor_op", "A <- A XOR B\n(Selective Complement)")
fc_logic.process("not_op", "A <- NOT A\n(Full Complement)")
fc_logic.io_box("output", "Store result A")
fc_logic.terminal("end", "END")

fc_logic.edge("start", "input")
fc_logic.edge("input", "op")
fc_logic.edge("op", "and_op", branch="AND")
fc_logic.edge("op", "or_op", branch="OR")
fc_logic.edge("op", "xor_op", branch="XOR")
fc_logic.edge("op", "not_op", branch="NOT")
fc_logic.edge("and_op", "output")
fc_logic.edge("or_op", "output")
fc_logic.edge("xor_op", "output")
fc_logic.edge("not_op", "output")
fc_logic.edge("output", "end")
en.story.extend(fc_logic.as_flowable())

en.tip(
    "AND = masking (clear bits). OR = setting bits. XOR = complementing bits. "
    "XOR with itself = 0 (clear register). AND with 0 = 0 (clear). OR with 1 = 1 (set). "
    "These are used extensively in OS kernels, device drivers, and bit field manipulation."
)
en.br()

# =============================================================================
#  1.10  SHIFT MICRO-OPERATIONS
# =============================================================================
en.chap_box("1.10  Shift Micro-Operations")
en.section("Types of Shifts")
en.definition(
    "<b>Shift Micro-Operations:</b> Operations that move the bits of a register "
    "left or right by one or more positions. The difference between shift types "
    "lies in what bit is shifted into the vacated position and what happens to "
    "the bit shifted out."
)

en.info_table(
    ["Shift Type", "RTL Symbol", "Left Shift Behavior", "Right Shift Behavior"],
    [
        [
            "Logical Shift",
            "shl / shr",
            "Shift left, 0 fills from right. MSB -> Carry.",
            "Shift right, 0 fills from left. LSB -> Carry.",
        ],
        [
            "Circular Shift\n(Rotate)",
            "cil / cir",
            "Shift left, MSB wraps to LSB position.",
            "Shift right, LSB wraps to MSB position.",
        ],
        [
            "Arithmetic Shift",
            "ashl / ashr",
            "Shift left, 0 fills from right (same as logical left).",
            "Shift right, SIGN BIT (MSB) is replicated. Preserves sign.",
        ],
        [
            "Rotate through Carry",
            "rcl / rcr",
            "Shift left, Carry -> LSB, MSB -> new Carry.",
            "Shift right, Carry -> MSB, LSB -> new Carry.",
        ],
    ],
)

en.section("Shift Operation Details with Examples")
en.code_block("""
 SHIFT MICRO-OPERATION EXAMPLES (8-bit register):
 ======================================================
 Original value: 1011 0110  (182 unsigned / -74 signed)

 1. LOGICAL LEFT SHIFT (shl by 1):
    MSB out -> 1 (Carry = 1)
    Result:  0110 1100  (108) = 182 * 2 - 256 = -72 (overflow!)
    Effect:  Multiply by 2 (unsigned). Effective only if no carry-out.

 2. LOGICAL RIGHT SHIFT (shr by 1):
    LSB out -> 0 (Carry = 0)
    0 fills at MSB.
    Result:  0101 1011  (91) = floor(182 / 2)
    Effect:  Divide by 2 (unsigned, rounds down).

 3. ARITHMETIC RIGHT SHIFT (ashr by 1):
    LSB out -> 0 (Carry = 0)
    Sign bit (1) replicated at MSB.
    Result:  1101 1011  = -37 (approximately -74 / 2 rounded toward -inf)
    Effect:  Divide by 2 preserving sign (signed right shift in C: >> for signed ints).

 4. CIRCULAR LEFT SHIFT / ROTATE LEFT (cil by 1):
    MSB (1) wraps around to LSB.
    Result:  0110 1101
    No bits are lost -- useful for cryptographic operations.

 5. ARITHMETIC LEFT SHIFT (ashl by 1):
    Same as logical left shift. 0 fills from right.
    Result:  0110 1100
    Multiplies by 2. Overflow if MSB changes (V flag set).

 6. ROTATE RIGHT THROUGH CARRY (rcr by 1):
    Old Carry = 1 fills MSB. LSB -> New Carry.
    Old carry:   1
    Result:  1101 1011  (Carry out = 0)
    Used in multi-precision arithmetic.

 KEY MULTIPLICATION / DIVISION BY POWERS OF 2:
 ======================================================
   Left shift by n  = multiply by 2^n  (if no overflow)
   Right shift by n = divide by 2^n    (logical: unsigned, arithmetic: signed)
""")

en.section("Shift Hardware -- Barrel Shifter")
en.definition(
    "<b>Barrel Shifter:</b> A combinational circuit that can shift an n-bit "
    "word by any number of positions (0 to n-1) in a single clock cycle "
    "(as opposed to a serial shifter that takes n cycles for an n-bit shift). "
    "Modern CPUs use barrel shifters for variable-length shifts."
)
en.tip(
    "Logical shift: fill with 0. Arithmetic right shift: fill with sign bit. "
    "Rotate (circular): no bits lost, MSB/LSB wraps. "
    "Arithmetic left shift n = multiply by 2^n. Arithmetic right shift n = divide by 2^n (signed). "
    "Barrel shifter shifts any amount in ONE clock cycle."
)
en.br()

# =============================================================================
#  1.11  ARITHMETIC LOGIC SHIFT UNIT (ALSU)
# =============================================================================
en.chap_box("1.11  Arithmetic Logic Shift Unit (ALSU)")
en.section("Overview")
en.definition(
    "<b>Arithmetic Logic Shift Unit (ALSU):</b> A combined hardware unit that "
    "implements all arithmetic micro-operations, logic micro-operations, and "
    "shift micro-operations in a single circuit. The ALSU is the central "
    "computational element of the CPU. It selects among its operations using "
    "a set of <b>function select lines</b> driven by the Control Unit."
)

en.section("ALSU Structure")
en.body(
    "The ALSU contains three parallel sub-units: an <b>Arithmetic Unit</b> "
    "(built from full adders + mux for subtraction/pass), a <b>Logic Unit</b> "
    "(AND, OR, XOR, NOT gates), and a <b>Shift Unit</b> (barrel shifter). "
    "A multiplexer at the output selects which sub-unit's result propagates to "
    "the output register based on the operation select lines."
)

en.section("ALSU Select Lines and Operations")
en.info_table(
    ["S3", "S2", "S1", "S0", "Cin", "Operation", "Function"],
    [
        ["0", "0", "0", "0", "0", "F = A", "Transfer A"],
        ["0", "0", "0", "0", "1", "F = A + 1", "Increment A"],
        ["0", "0", "0", "1", "0", "F = A + B", "Add"],
        ["0", "0", "0", "1", "1", "F = A + B + 1", "Add with carry"],
        ["0", "0", "1", "0", "0", "F = A + B'", "Subtract (via B complement)"],
        ["0", "0", "1", "0", "1", "F = A - B", "Subtract (2's complement)"],
        ["0", "0", "1", "1", "0", "F = A - 1", "Decrement A"],
        ["0", "1", "0", "0", "X", "F = A AND B", "AND (logic)"],
        ["0", "1", "0", "1", "X", "F = A OR B", "OR (logic)"],
        ["0", "1", "1", "0", "X", "F = A XOR B", "XOR (logic)"],
        ["0", "1", "1", "1", "X", "F = NOT A", "Complement (logic)"],
        ["1", "0", "0", "0", "X", "F = shl A", "Shift left logical"],
        ["1", "0", "0", "1", "X", "F = shr A", "Shift right logical"],
        ["1", "0", "1", "0", "X", "F = cil A", "Circular (rotate) left"],
        ["1", "0", "1", "1", "X", "F = cir A", "Circular (rotate) right"],
        ["1", "1", "0", "0", "X", "F = ashr A", "Arithmetic shift right"],
    ],
)

en.section("ALSU Block Diagram (Conceptual)")

net_alsu = ed.NetworkDiagram(
    width=en.CW,
    height=310,
    theme=diag_theme,
    caption="Fig 7: Arithmetic Logic Shift Unit -- combined functional block diagram",
)
net_alsu.node(
    "A",
    "Register A\n(Operand 1)",
    x=80,
    y=210,
    kind="custom",
    custom_draw=draw_register,
)
net_alsu.node(
    "B", "Register B\n(Operand 2)", x=80, y=90, kind="custom", custom_draw=draw_register
)
net_alsu.node(
    "arith",
    "Arithmetic\nUnit (+/-/INC)",
    x=220,
    y=225,
    kind="custom",
    custom_draw=draw_alu,
    custom_clip=clip_alu,
)
net_alsu.node(
    "logic",
    "Logic Unit\n(AND/OR/XOR/NOT)",
    x=220,
    y=150,
    kind="custom",
    custom_draw=draw_logic_unit,
)
net_alsu.node(
    "shift",
    "Shift Unit\n(SHL/SHR/ROT)",
    x=220,
    y=75,
    kind="custom",
    custom_draw=draw_shift_unit,
)
net_alsu.node(
    "mux",
    "Output\nMux (4x1)",
    x=360,
    y=150,
    kind="custom",
    custom_draw=draw_mux,
    custom_clip=clip_mux,
)
net_alsu.node(
    "result",
    "Result\nRegister F",
    x=460,
    y=150,
    kind="custom",
    custom_draw=draw_register,
)
net_alsu.node("flags", "Flags", x=460, y=75, kind="custom", custom_draw=draw_flags)
net_alsu.node("ctrl", "Control Unit", x=360, y=275, kind="custom", custom_draw=draw_cu)
net_alsu.link("A", "arith", label="")
net_alsu.link("B", "arith", label="")
net_alsu.link("A", "logic", label="")
net_alsu.link("B", "logic", label="")
net_alsu.link("A", "shift", label="")
net_alsu.link("arith", "mux", label="")
net_alsu.link("logic", "mux", label="")
net_alsu.link("shift", "mux", label="")
net_alsu.link("mux", "result", label="F")
net_alsu.link("result", "flags", label="status")
net_alsu.link("ctrl", "mux", label="S3..S0")
en.story.extend(net_alsu.as_flowable())


en.section("ALSU Flowchart -- Operation Selection")
fc_alsu = ed.Flowchart(
    width=en.CW,
    height=290,
    theme=diag_theme,
    caption="Fig 8: ALSU operation selection based on control unit select lines",
)
fc_alsu.terminal("start", "Instruction Decoded by CU")
fc_alsu.process("load", "Load A and B from registers onto ALSU inputs")
fc_alsu.decision("sel", "Select Lines S3..S0?")
fc_alsu.process("arith_exec", "Arithmetic Unit: ADD / SUB / INC / DEC")
fc_alsu.process("logic_exec", "Logic Unit: AND / OR / XOR / NOT")
fc_alsu.process("shift_exec", "Shift Unit: SHL / SHR / ROT / ASHR")
fc_alsu.process("store", "Output Mux selects result; update Flags Z,N,C,V")
fc_alsu.terminal("end", "Write result F to destination register")

fc_alsu.edge("start", "load")
fc_alsu.edge("load", "sel")
fc_alsu.edge("sel", "arith_exec", branch="S3=0, Arith")
fc_alsu.edge("sel", "logic_exec", branch="S3=0, Logic")
fc_alsu.edge("sel", "shift_exec", branch="S3=1, Shift")
fc_alsu.edge("arith_exec", "store")
fc_alsu.edge("logic_exec", "store")
fc_alsu.edge("shift_exec", "store")
fc_alsu.edge("store", "end")
en.story.extend(fc_alsu.as_flowable())

en.section("Status Flags Generated by ALSU")
en.info_table(
    ["Flag", "Name", "Set Condition", "Cleared Condition", "Use"],
    [
        [
            "Z",
            "Zero",
            "Result = 0 (all bits zero)",
            "Result != 0",
            "BEQ, BNE branch instructions",
        ],
        [
            "N",
            "Negative",
            "MSB of result = 1",
            "MSB = 0",
            "BMI, BPL branch instructions",
        ],
        [
            "C",
            "Carry",
            "Carry-out from MSB in arithmetic",
            "No carry-out",
            "Multi-precision arithmetic, BCS/BCC",
        ],
        [
            "V",
            "Overflow",
            "Signed overflow (sign bit wrong)",
            "No signed overflow",
            "BOV branch, overflow detection",
        ],
    ],
)
en.tip(
    "ALSU = Arithmetic Unit + Logic Unit + Shift Unit + Output Mux. "
    "CU provides select lines S3..S0 to choose the operation. "
    "Output mux selects result from whichever sub-unit is active. "
    "Status flags (Z, N, C, V) are set combinationally from the result."
)
en.br()

# =============================================================================
#  1.12  QUICK REVISION SUMMARY
# =============================================================================
en.part_box("UNIT I -- QUICK REVISION SUMMARY")
en.chap_box("Key Concepts at a Glance")

en.info_table(
    ["Topic", "Key Point to Remember"],
    [
        [
            "Architecture vs Organization",
            "Architecture = ISA (what). Organization = hardware implementation (how). "
            "Same architecture can have different organizations.",
        ],
        [
            "Generation 1-5",
            "(1)Vacuum tubes, (2)Transistors, (3)ICs, (4)VLSI/Microprocessor, (5)AI/Quantum. "
            "Each gen ~1000x better cost/performance.",
        ],
        [
            "Von Neumann Model",
            "Stored-program: instructions and data in same memory. "
            "Bottleneck = single bus shared by instructions and data. "
            "Harvard arch solves it with separate buses.",
        ],
        [
            "Fetch-Decode-Execute Cycle",
            "T0: MAR<-PC. T1: MBR<-M[MAR], PC<-PC+1. T2: IR<-MBR. "
            "Then decode opcode and execute. This is THE fundamental CPU cycle.",
        ],
        [
            "CPU Organization",
            "CPU = ALU + CU + Registers. ALU: combinational, does arithmetic/logic. "
            "CU: generates control signals. Registers: fastest storage.",
        ],
        [
            "Key Registers",
            "PC = next instruction addr. IR = current instruction. "
            "MAR = memory address. MDR = memory data. AC = result. SP = stack top. "
            "PSW = flags (Z,N,C,V).",
        ],
        [
            "RTL Notation",
            "R2 <- R1 = transfer. M[MAR] = memory location. "
            "Comma (,) = simultaneous. Timing steps T0,T1,T2,... = one clock each.",
        ],
        [
            "Arithmetic Micro-ops",
            "ADD, SUB, INC, DEC, NEGATE. SUB = ADD 2's complement. "
            "2's complement = NOT + 1. BCD: add 6 if sum > 9 or carry.",
        ],
        [
            "Logic Micro-ops",
            "AND = mask/clear. OR = selective set. XOR = selective complement/compare. "
            "NOT = ones complement. XOR with self = 0.",
        ],
        [
            "Shift Micro-ops",
            "Logical: fill 0. Arithmetic right: fill sign bit. "
            "Circular: MSB/LSB wraps. Left shift n = x2^n. Right shift n = /2^n. "
            "Barrel shifter: variable shift in 1 clock.",
        ],
        [
            "ALSU Structure",
            "Arithmetic Unit + Logic Unit + Shift Unit + Output Mux. "
            "CU drives select lines S3..S0. Mux picks output. "
            "Flags Z,N,C,V set from result.",
        ],
        [
            "Status Flags",
            "Z = result zero. N = MSB set (negative). C = carry out (unsigned overflow). "
            "V = signed overflow (sign bit wrong). Used by conditional branch instructions.",
        ],
        [
            "Bus Types",
            "Address bus (CPU->Mem, unidirectional, k bits). "
            "Data bus (bidirectional, n bits = word size). "
            "Control bus (MemRead, MemWrite, I/O signals).",
        ],
        [
            "Three-State Buffers",
            "Prevent bus contention. Enable=1: drive bus (0 or 1). "
            "Enable=0: high-impedance Z (disconnected). "
            "Only one source drives bus at a time.",
        ],
    ],
)

en.highlight(
    "<b>UNIT I EXAM BLUEPRINT:</b>  "
    "2-mark: Differentiate architecture vs organization. List CPU registers. "
    "State the stored-program concept. Define RTL.  "
    "5-mark: Explain Von Neumann model with block diagram. "
    "Describe fetch-decode-execute cycle with RTL. "
    "Explain types of shift micro-operations with examples. "
    "Explain logic micro-operation applications (AND/OR/XOR masking).  "
    "10-mark: Explain ALSU with block diagram and operation table. "
    "Explain computer generations with technology and examples. "
    "Describe register organization (all key registers, sizes, functions). "
    "Explain bus and memory transfers with timing diagram.",
)

en.sp(10)
en.rule(en.get_theme().rl(en.get_theme().accent), 1.0)
en.sp(6)
en.add(
    Paragraph(
        "Computer Architecture IT-404 Unit I -- Bharat Dangi  |  UIT-RGPV (Autonomous) Bhopal | Semester IV",
        en.COVER_SUB,
    )
)

# =============================================================================
#  BUILD PDF
# =============================================================================
en.build_doc("CA_Unit1_Notes.pdf", title="Computer Architecture - Unit I Notes", author="Bharat Dangi")
print("Generated: CA_Unit1_Notes.pdf")
