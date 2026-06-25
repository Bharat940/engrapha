"""
Computer Architecture (IT-404) -- Unit III Notes
UIT-RGPV (Autonomous) Bhopal | Semester IV
Complete exam notes with vector diagrams.
Run: python ca_unit3_notes.py
Output: CA_Unit3_Notes.pdf
"""

from __future__ import annotations

import paperforge_notes as pn
import paperforge_diagrams as pd
from reportlab.platypus import Paragraph, Table, TableStyle
from paperforge_diagrams import ResponsiveDrawingFlowable

# =============================================================================
#  THEME SETUP
# =============================================================================
pn.set_story([])
pn.set_theme(pn.SUNSET_DARK)

diag_theme = pd.DiagramTheme.from_notes_theme(pn.get_theme())


# =============================================================================
#  CUSTOM NODE DRAWERS (reused across diagrams)
# =============================================================================
def draw_register(diag, cx, cy, w, h, fill, stroke):
    import paperforge_diagrams.shapes as S

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
    import paperforge_diagrams.shapes as S

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


def draw_flags(diag, cx, cy, w, h, fill, stroke):
    import paperforge_diagrams.shapes as S

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
    for i, ch in enumerate(["Z", "N", "C", "V"]):
        fx = cx - w / 2 + (i + 0.5) * (w / 4)
        diag._add(
            S.label(
                fx,
                cy - 3.0,
                ch,
                font=t.font_name_bold,
                size=7.0,
                color=stroke,
                anchor="middle",
            )
        )


# =============================================================================
#  COVER PAGE
# =============================================================================
pn.bookmark("Cover Page")
pn.suppress_footer(page_only=True)
pn.sp(14)
t = Table(
    [
        [Paragraph("COMPUTER ARCHITECTURE", pn.COVER_H1)],
        [Paragraph("Unit III -- Complete Exam Notes", pn.COVER_H2)],
    ],
    colWidths=[pn.CW],
)
t.setStyle(
    TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, -1), pn.get_theme().rl(pn.get_theme().surface)),
            ("TOPPADDING", (0, 0), (-1, -1), 16),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 16),
            ("LEFTPADDING", (0, 0), (-1, -1), 20),
            ("RIGHTPADDING", (0, 0), (-1, -1), 20),
            ("BOX", (0, 0), (-1, -1), 2.5, pn.get_theme().rl(pn.get_theme().accent)),
        ]
    )
)
pn.add(t)
pn.sp(8)
pn.add(
    Paragraph(
        "Prepared by: Bharat Dangi  |  Subject Code: IT-404  |  UIT-RGPV (Autonomous) Bhopal",
        pn.COVER_SUB,
    )
)
pn.add(Paragraph("Semester IV  |  Based on University Syllabus 2024-25", pn.COVER_SUB))
pn.sp(6)
pn.rule(pn.get_theme().rl(pn.get_theme().accent), 1.5)
pn.sp(4)

pn.info_table(
    ["Topic", "Coverage"],
    [
        ["3.1 CPU Organization", "Program sequencing, instruction execution overview"],
        [
            "3.2 Stack Organization",
            "Stack structure, PUSH/POP, memory stack, register stack",
        ],
        [
            "3.3 Reverse Polish Notation",
            "Postfix notation, expression evaluation with stack",
        ],
        [
            "3.4 - 3.8 Instruction Formats",
            "Zero, one, two, and three-address instruction formats",
        ],
        ["3.9 RISC vs CISC", "Characteristics, trade-offs, pipeline friendliness"],
        [
            "3.10 Addressing Modes",
            "Immediate, direct, indirect, register, indexed, relative, base",
        ],
        [
            "3.11 Instruction Set Completeness",
            "Data transfer, data manipulation, and program control instructions",
        ],
        ["3.12 Modes of Transfer", "Programmed I/O, interrupt-driven, DMA"],
        [
            "3.13 Priority Interrupt",
            "Vectored interrupt, daisy chaining, priority levels",
        ],
        ["3.14 DMA", "DMA controller, cycle stealing, burst mode, block transfer"],
        [
            "3.15 Input Output Processor (IOP)",
            "IOP structure, channel programs, DMA vs IOP",
        ],
        ["3.16 Quick Revision Summary", "Key formulas, tables, and exam flashcards"],
    ],
)
pn.br()
pn.suppress_footer(page_only=True)
pn.toc()

# =============================================================================
#  UNIT DIVIDER
# =============================================================================
pn.footer(left="IT-404: Computer Architecture", right="Unit III Notes", show_page_num=True)
pn.part_box("UNIT III -- CPU, INSTRUCTION FORMATS, I/O AND INTERRUPTS")

# =============================================================================
#  3.1  CPU ORGANIZATION
# =============================================================================
pn.chap_box("3.1  CPU Organization")
pn.section("Overview")
pn.definition(
    "<b>CPU (Central Processing Unit):</b> The part of the computer that performs the "
    "bulk of data-processing operations. The CPU is made up of three major parts:<br/>"
    "1. <b>Register Set:</b> Stores intermediate data used during the execution of instructions.<br/>"
    "2. <b>Arithmetic Logic Unit (ALU):</b> Performs the required arithmetic and logic micro-operations for executing instructions.<br/>"
    "3. <b>Control Unit (CU):</b> Supervises the transfer of information among the registers and instructs the ALU as to which operation to perform."
)
pn.body(
    "Beyond the basic fetch-decode-execute cycle covered in Unit I, the CPU must "
    "also handle <b>interrupts</b> (external events that divert normal program flow), "
    "<b>stack operations</b> for subroutine calls and expression evaluation, and "
    "<b>I/O transfers</b> through programmed polling, interrupt, or DMA."
)

# CPU Major Parts block diagram (matching Fig 8-1 in notes)
net_cpu = pd.NetworkDiagram(
    width=pn.CW,
    height=220,
    theme=diag_theme,
    caption="Fig 1a: Major Components of the CPU (Register Set, ALU, and Control Unit)",
)
net_cpu.node("registers", "Register Set\n(Intermediate Storage)", x=80, y=105, kind="server")
net_cpu.node("alu", "Arithmetic Logic Unit (ALU)\n(Micro-operations execution)", x=250, y=155, kind="generic")
net_cpu.node("cu", "Control Unit (CU)\n(Supervises & directs ALU)", x=250, y=55, kind="generic")
net_cpu.node("bus", "System Bus\n(Data/Addr/Ctrl)", x=420, y=105, kind="switch")

net_cpu.link("registers", "alu", label="Data path")
net_cpu.link("registers", "cu", label="Status/Data")
net_cpu.link("cu", "alu", label="Control lines")
net_cpu.link("registers", "bus", label="")
net_cpu.link("cu", "bus", label="Bus control")
pn.story.extend(net_cpu.as_flowable())
pn.sp(8)

pn.section("Program Sequencing")
pn.bullet(
    [
        "<b>Sequential:</b> PC increments after each fetch (PC <- PC + 1 or +instruction length).",
        "<b>Branch/Jump:</b> PC is loaded with the target address on branch.",
        "<b>Subroutine call:</b> Saves return PC on stack, then jumps to subroutine.",
        "<b>Interrupt:</b> Saves PC and PSW, then jumps to the ISR vector address.",
    ]
)

# CPU fetch-execute state machine
sm_cpu = pd.StateMachine(
    width=pn.CW,
    height=200,
    theme=diag_theme,
    caption="Fig 1b: CPU instruction-cycle state machine",
)
sm_cpu.state("fetch", "Fetch", x=140, y=150, initial=True)
sm_cpu.state("decode", "Decode", x=340, y=150)
sm_cpu.state("execute", "Execute", x=340, y=50)
sm_cpu.state("intr", "Interrupt", x=140, y=50)
sm_cpu.transition("fetch", "decode", label="IR <- M[PC], PC++")
sm_cpu.transition("decode", "execute", label="decode opcode")
sm_cpu.transition("execute", "intr", label="complete op")
sm_cpu.transition("intr", "fetch", label="no interrupt")
sm_cpu.transition("intr", "fetch", label="service ISR")
pn.story.extend(sm_cpu.as_flowable())

pn.tip(
    "CPU cycle: Fetch -> Decode -> Execute -> Interrupt Check -> Fetch. "
    "Interrupt check happens after every instruction. "
    "If interrupt pending and enabled: save PC/PSW, jump to ISR."
)
pn.br()

# =============================================================================
#  3.2  STACK ORGANIZATION
# =============================================================================
pn.chap_box("3.2  Stack Organization")
pn.section("What is a Stack?")
pn.definition(
    "<b>Stack:</b> A Last-In-First-Out (LIFO) storage device that stores information "
    "in such a manner that the item stored last is the first item retrieved. "
    "The operation of a stack can be compared to a stack of trays: the last tray placed "
    "on top is the first to be taken off. In digital computers, a stack is simulated in "
    "memory or registers, where the insertion/deletion of items is managed by "
    "incrementing or decrementing a <b>Stack Pointer (SP)</b> register that points to the top item."
)
pn.body(
    "Contrary to physical trays, the physical registers or memory locations of a computer stack "
    "are always available for reading and writing; it is simply the <i>content</i> of the words "
    "that is logically pushed or popped by updating the address in the SP register."
)

pn.section("Register Stack (64-Word Hardware Stack)")
pn.body(
    "A stack can be organized as a collection of a finite number of memory words or registers. "
    "For a <b>64-word register stack</b> (Fig 2a):<br/>"
    "• <b>Stack Pointer (SP):</b> Contains 6 bits (since 2<sup>6</sup> = 64) with address values from 0 to 63 (000000 to 111111 in binary).<br/>"
    "• <b>Wrap-Around:</b> When 63 is incremented by 1, it wraps around to 0. When 0 is decremented by 1, it wraps around to 63.<br/>"
    "• <b>FULL Register:</b> A 1-bit register set to 1 when the stack is full of items.<br/>"
    "• <b>EMTY Register:</b> A 1-bit register set to 1 when the stack is empty of items.<br/>"
    "• <b>DR (Data Register):</b> Holds the binary data to be written into or read out of the stack."
)
pn.code_block("""
 REGISTER STACK MICRO-OPERATIONS:
 ======================================================
 Initial: SP = 0, EMTY = 1, FULL = 0

 PUSH OPERATION (if FULL = 0):
   SP <- SP + 1          (increment stack pointer)
   M[SP] <- DR           (write item from DR to top of stack)
   If (SP = 0) then:
     FULL <- 1           (check if stack is full, happens on 64th PUSH)
   EMTY <- 0             (mark stack as not empty)

 POP OPERATION (if EMTY = 0):
   DR <- M[SP]           (read item from top of stack into DR)
   SP <- SP - 1          (decrement stack pointer)
   If (SP = 0) then:
     EMTY <- 1           (check if stack is empty, happens when SP returns to 0)
   FULL <- 0             (mark stack as not full)

 Note: A push when FULL = 1 or a pop when EMTY = 1 results in an erroneous operation.
""")

pn.section("Memory Stack")
pn.body(
    "A memory stack is implemented in a portion of random-access memory (RAM) attached to the CPU, "
    "using a processor register as the Stack Pointer (SP). As shown in Fig 2b:<br/>"
    "• <b>Memory Partitioning:</b> The computer memory is partitioned into three segments: <i>Program</i> (pointed to by PC), "
    "<i>Data</i> (pointed to by AR), and <i>Stack</i> (pointed to by SP). All registers share a common address bus.<br/>"
    "• <b>Growth Direction:</b> The memory stack grows with <b>decreasing addresses</b>. The initial SP value is 4001. "
    "The first item stored is at address 4000, the second at 3999, down to a stack limit of 3000.<br/>"
    "• <b>Stack Limit Checking:</b> Two registers are used to hold the limits: one for the <i>upper limit</i> (3000 in this case) "
    "and one for the <i>lower limit</i> (4001). After a PUSH, SP is compared with the upper limit; after a POP, SP is compared with the lower limit to prevent overflow or underflow."
)
pn.code_block("""
 MEMORY STACK MICRO-OPERATIONS (Grows Downward):
 ======================================================
 Initial: SP = 4001, Limit = 3000

 PUSH OPERATION:
   SP <- SP - 1          (decrement stack pointer first)
   M[SP] <- DR           (write item from DR to memory stack)

 POP OPERATION:
   DR <- M[SP]           (read top item from memory stack into DR)
   SP <- SP + 1          (increment stack pointer)
""")

# Stack visual diagrams (Fig 2a and Fig 2b side-by-side)
reg_stack = pd.LayeredStack(
    width=pn.CW * 0.44,
    height=220,
    theme=diag_theme,
    caption="Fig 2a: 64-Word Register Stack (Grows Upward)",
)
reg_stack.layer("Location 0 (Last word / FULL marker)", sublabel="SP wraps to 0 here")
reg_stack.layer("Location 63", sublabel="")
reg_stack.layer("Location 3: Item C <-- SP = 3 (Top of stack)", sublabel="")
reg_stack.layer("Location 2: Item B", sublabel="")
reg_stack.layer("Location 1: Item A (First stored item)", sublabel="")
reg_stack.layer("Location 0 (Initial: EMTY = 1)", sublabel="SP points here initially")

mem_stack = pd.LayeredStack(
    width=pn.CW * 0.44,
    height=220,
    theme=diag_theme,
    caption="Fig 2b: Memory Stack (Grows Downward)",
)
mem_stack.layer("Address 4001 (Initial SP: Empty)", sublabel="Lower limit")
mem_stack.layer("Address 4000: Item A (First stored item)", sublabel="")
mem_stack.layer("Address 3999: Item B", sublabel="")
mem_stack.layer("Address 3998: Item C <-- SP = 3998 (Top of stack)", sublabel="")
mem_stack.layer("...", sublabel="")
mem_stack.layer("Address 3000 (Full stack limit)", sublabel="Upper limit")

reg_stack.as_flowable()
mem_stack.as_flowable()

tbl_stack = Table(
    [
        [
            ResponsiveDrawingFlowable(reg_stack.drawing),
            ResponsiveDrawingFlowable(mem_stack.drawing),
        ]
    ],
    colWidths=[pn.CW * 0.48, pn.CW * 0.48],
)
tbl_stack.setStyle(
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
pn.add(tbl_stack)
pn.sp(6)
pn.add(
    Paragraph(
        "Fig 2a (left): 64-word Register Stack growing upward.  |  Fig 2b (right): Memory Stack growing downward in RAM.",
        pn.COVER_SUB,
    )
)
pn.sp(8)

pn.section("Key Stack Organization Points")
pn.bullet(
    [
        "<b>Stack Pointer (SP) points to Top of Stack:</b><br/>"
        "  - <i>Push:</i> First increment/decrement SP, then write to memory location.<br/>"
        "  - <i>Pop:</i> First read location, then decrement/increment SP.",
        "<b>Stack Pointer (SP) points to Next Empty Location:</b><br/>"
        "  - <i>Push:</i> First write to memory location, then increment/decrement SP.<br/>"
        "  - <i>Pop:</i> First decrement/increment SP, then read location.",
        "<b>Stack growing by INCREASING memory address (e.g. Fig 2a):</b><br/>"
        "  - SP is updated by <i>incrementing</i> for Push, and <i>decrementing</i> for Pop.",
        "<b>Stack growing by DECREASING memory address (e.g. Fig 2b):</b><br/>"
        "  - SP is updated by <i>decrementing</i> for Push, and <i>incrementing</i> for Pop."
    ]
)

# Stack push/pop sequence diagram
seq_stack = pd.SequenceDiagram(
    width=pn.CW,
    height=220,
    theme=diag_theme,
    caption="Fig 2c: Stack PUSH and POP operations with subroutine call",
)
seq_stack.actor("cpu", "CPU")
seq_stack.actor("sp", "Stack Pointer (SP)")
seq_stack.actor("mem", "Memory Stack")
seq_stack.message("cpu", "sp", "CALL: SP <- SP - 1", arrow="solid")
seq_stack.message("cpu", "mem", "M[SP] <- Return Address", arrow="solid")
seq_stack.message("cpu", "sp", "PC <- Subroutine Address", arrow="solid")
seq_stack.divider("Inside Subroutine -- PUSH local variables")
seq_stack.message("cpu", "sp", "SP <- SP - 1", arrow="solid")
seq_stack.message("cpu", "mem", "M[SP] <- R1 (save register)", arrow="solid")
seq_stack.divider("Return from Subroutine")
seq_stack.message("cpu", "mem", "R1 <- M[SP] (restore register)", arrow="dashed")
seq_stack.message("cpu", "sp", "SP <- SP + 1", arrow="solid")
seq_stack.message("cpu", "mem", "PC <- M[SP] (return address)", arrow="dashed")
seq_stack.message("cpu", "sp", "SP <- SP + 1", arrow="solid")
pn.story.extend(seq_stack.as_flowable())

pn.tip(
    "Stack is LIFO. SP points to current TOP. "
    "Push: SP--, M[SP]=data. Pop: data=M[SP], SP++. "
    "Subroutine call: push PC, jump. Return: pop PC. "
    "Stack grows downward (toward lower addresses) in most architectures."
)
pn.br()

# =============================================================================
#  3.3  REVERSE POLISH NOTATION (RPN)
# =============================================================================
pn.chap_box("3.3  Reverse Polish Notation (RPN / Postfix)")
pn.section("What is RPN?")
pn.definition(
    "<b>Reverse Polish Notation (Postfix Notation):</b> A mathematical notation in "
    "which every operator follows its operands. No parentheses are needed because "
    "the order of operations is unambiguous. RPN is directly executable on a stack "
    "machine -- each operand is pushed onto the stack, and each operator pops its "
    "operands, computes the result, and pushes the result back."
)

pn.info_table(
    ["Notation", "Example", "How Parsed"],
    [
        [
            "Infix (normal)",
            "(A + B) * (C - D)",
            "Operators between operands, parentheses needed",
        ],
        ["Prefix (Polish)", "* + A B - C D", "Operator before operands, right-to-left"],
        [
            "Postfix (RPN)",
            "A B + C D - *",
            "Operator after operands, left-to-right stack evaluation",
        ],
    ],
)

pn.section("Infix to Postfix Conversion")
pn.code_block("""
 INFIX TO POSTFIX CONVERSION ALGORITHM:
 ======================================================
 Rules:
   1. Scan the infix expression left to right.
   2. If operand: output it directly.
   3. If '(': push to operator stack.
   4. If ')': pop and output until '(' is found; discard '('.
   5. If operator: pop and output operators of >= precedence from stack,
      then push the current operator.
   6. End: pop and output all remaining operators from stack.

 Precedence: * / (high) > + - (low)

 EXAMPLE: Convert  (A + B) * C - D / E  to postfix

 Token | Action                | Stack         | Output
 ------|----------------------|---------------|------------------
   (   | Push (               | (             |
   A   | Output A             | (             | A
   +   | Push +               | ( +           | A
   B   | Output B             | ( +           | A B
   )   | Pop until (: output+ | empty         | A B +
   *   | Push *               | *             | A B +
   C   | Output C             | *             | A B + C
   -   | Pop * (higher), push- | -             | A B + C *
   D   | Output D             | -             | A B + C * D
   /   | Push / (higher than-) | - /           | A B + C * D
   E   | Output E             | - /           | A B + C * D E
  End  | Pop all: /  then -   | empty         | A B + C * D E / -

 Result: A B + C * D E / -
""")

pn.section("Example 3: Postfix Evaluation of (3 * 4) + (5 * 6)")
pn.body(
    "<b>Arithmetic Expression:</b> (3 * 4) + (5 * 6)<br/>"
    "<b>Reverse Polish Notation (RPN):</b> 3 4 * 5 6 * +<br/>"
    "Scanning this RPN expression from left to right yields the following stack operations:"
)
pn.code_block("""
 STEP-BY-STEP STACK TRACE FOR: 3 4 * 5 6 * +
 ======================================================
 Token | Action                                 | Stack (TOS on right)
 ------|----------------------------------------|---------------------
   3   | PUSH 3                                 | [3]
   4   | PUSH 4                                 | [3, 4]
   *   | POP 4, POP 3; Multiply 3*4=12; PUSH 12 | [12]
   5   | PUSH 5                                 | [12, 5]
   6   | PUSH 6                                 | [12, 5, 6]
   *   | POP 6, POP 5; Multiply 5*6=30; PUSH 30 | [12, 30]
   +   | POP 30, POP 12; Add 12+30=42; PUSH 42  | [42]

 Final result: 42 (remains on top of the stack)
""")

pn.section("Example 5: Evaluation of (3 + 4) * [ 10 * ( 2 + 6 ) + 8 ]")
pn.body(
    "Let us convert this complex expression to postfix and trace its evaluation using a stack:<br/>"
    "• <b>Infix:</b> (3 + 4) * [ 10 * ( 2 + 6 ) + 8 ]<br/>"
    "• <b>RPN:</b> 3 4 + 10 2 6 + * 8 + *"
)
pn.info_table(
    ["Token", "Action / Operation", "Stack State (TOS on right)", "Intermediate Result"],
    [
        ["3", "PUSH operand 3", "[3]", ""],
        ["4", "PUSH operand 4", "[3, 4]", ""],
        ["+", "POP 4, 3; Compute 3 + 4 = 7; PUSH 7", "[7]", "7"],
        ["10", "PUSH operand 10", "[7, 10]", ""],
        ["2", "PUSH operand 2", "[7, 10, 2]", ""],
        ["6", "PUSH operand 6", "[7, 10, 2, 6]", ""],
        ["+", "POP 6, 2; Compute 2 + 6 = 8; PUSH 8", "[7, 10, 8]", "8"],
        ["*", "POP 8, 10; Compute 10 * 8 = 80; PUSH 80", "[7, 80]", "80"],
        ["8", "PUSH operand 8", "[7, 80, 8]", ""],
        ["+", "POP 8, 80; Compute 80 + 8 = 88; PUSH 88", "[7, 88]", "88"],
        ["*", "POP 88, 7; Compute 7 * 88 = 616; PUSH 616", "[616]", "616"],
    ],
)
pn.sp(6)

# RPN flowchart
fc_rpn = pd.Flowchart(
    width=pn.CW,
    height=280,
    theme=diag_theme,
    caption="Fig 3: Postfix (RPN) expression evaluation using a stack",
)
fc_rpn.terminal("start", "START: Read postfix expression left to right")
fc_rpn.io_box("read", "Read next token")
fc_rpn.decision("end", "End of expression?")
fc_rpn.decision("operand", "Token is operand?")
fc_rpn.process("push", "PUSH operand onto stack")
fc_rpn.process("pop2", "POP B (top), POP A (below)")
fc_rpn.process("compute", "Compute A op B using operator")
fc_rpn.process("push_r", "PUSH result onto stack")
fc_rpn.io_box("result", "POP stack -> final result")
fc_rpn.terminal("done", "END")

fc_rpn.edge("start", "read")
fc_rpn.edge("read", "end")
fc_rpn.edge("end", "result", branch="yes")
fc_rpn.edge("end", "operand", branch="no")
fc_rpn.edge("operand", "push", branch="yes")
fc_rpn.edge("operand", "pop2", branch="no")
fc_rpn.edge("push", "read", orthogonal=True)
fc_rpn.edge("pop2", "compute")
fc_rpn.edge("compute", "push_r")
fc_rpn.edge("push_r", "read", orthogonal=True)
fc_rpn.edge("result", "done")
pn.story.extend(fc_rpn.as_flowable())

pn.tip(
    "RPN (postfix): operators follow operands. No parentheses needed. "
    "Evaluate with stack: operand -> PUSH, operator -> POP 2, compute, PUSH result. "
    "Stack machines (Java JVM, HP calculators, Forth) use RPN natively."
)
pn.br()

# =============================================================================
#  3.4  INSTRUCTION FORMATS
# =============================================================================
pn.chap_box("3.4  Instruction Formats")
pn.section("What is an Instruction Format?")
pn.definition(
    "<b>Instruction Format:</b> The binary layout of a machine instruction -- "
    "how many bits are devoted to the opcode, addressing mode, and operand fields. "
    "The format determines the power of each instruction, the size of addressable "
    "memory, and the number of registers accessible. Designers balance instruction "
    "word length, addressing range, and hardware complexity."
)

pn.section("General Instruction Word Layout")
pn.frame_format(
    "Generic Instruction Word (16-bit example)",
    [
        ("OPCODE", "4-6 bits"),
        ("MODE", "2-3 bits"),
        ("OPERAND / ADDRESS", "remaining bits"),
    ],
)
pn.body(
    "The <b>opcode</b> identifies the operation (ADD, LOAD, BRANCH, etc.). "
    "The <b>mode field</b> specifies the addressing mode (immediate, direct, "
    "indirect, register, etc.). The <b>operand/address field</b> provides the "
    "data value or memory address needed for the operation."
)

pn.section("Types of Instruction Formats by Number of Addresses")
pn.info_table(
    ["Format", "Fields", "Registers/Memory Accesses", "Code Density", "Typical ISA"],
    [
        [
            "Zero-address",
            "Opcode only",
            "Stack implicit -- no explicit address",
            "Most compact code (push/pop)",
            "Forth, Java bytecode, HP RPL",
        ],
        [
            "One-address",
            "Opcode + 1 address",
            "1 explicit (AC implicit)",
            "Compact -- AC always one operand",
            "Early ACC machines, 8080",
        ],
        [
            "Two-address",
            "Opcode + 2 addresses",
            "2 explicit (dest = src1 usually)",
            "Moderate",
            "x86 (destination also source)",
        ],
        [
            "Three-address",
            "Opcode + 3 addresses",
            "3 explicit (dest, src1, src2)",
            "Larger instruction word",
            "RISC (MIPS, ARM, RISC-V)",
        ],
    ],
)
pn.tip(
    "More addresses per instruction = more work per instruction but larger instruction word. "
    "RISC typically uses three-address instructions with fixed-length 32-bit words. "
    "CISC may use 0, 1, 2, or 3 addresses in variable-length instructions."
)
pn.br()

# =============================================================================
#  3.5  ZERO-ADDRESS INSTRUCTIONS
# =============================================================================
pn.chap_box("3.5  Zero-Address Instructions")
pn.section("Concept")
pn.definition(
    "<b>Zero-Address Instructions:</b> Instructions that contain only an opcode -- "
    "no explicit operand address. Both operands are implicitly on the top of the "
    "stack. The CPU always operates on the stack top (TOS) and the element below it "
    "(NOS -- Next on Stack). Used in pure stack-based (zero-address) architectures."
)

pn.code_block("""
 ZERO-ADDRESS INSTRUCTION SET EXAMPLE (Stack Machine):
 ======================================================
 Instructions: PUSH addr, POP addr, ADD, SUB, MUL, DIV, NOT

 Compute: X = (A + B) * (C + D)

 Equivalent infix:  (A+B) * (C+D)
 Postfix (RPN):      A B + C D + *

 Machine code (zero-address):
   PUSH A    ; TOS <- A
   PUSH B    ; TOS <- B
   ADD       ; Pop B, Pop A; Push A+B. TOS <- (A+B)
   PUSH C    ; TOS <- C
   PUSH D    ; TOS <- D
   ADD       ; Pop D, Pop C; Push C+D. TOS <- (C+D)
   MUL       ; Pop (C+D), Pop (A+B); Push (A+B)*(C+D). TOS <- (A+B)*(C+D)
   POP X     ; M[X] <- TOS. Store result in X.

 Number of instructions: 8 (for this expression)
 No address fields in arithmetic instructions (ADD, MUL) -- just opcode!
""")

pn.tip(
    "Zero-address machines use a hardware stack for all computation. "
    "PUSH and POP move data between memory and stack. "
    "Arithmetic instructions (ADD, SUB, MUL) have NO address field. "
    "Used in Java Virtual Machine (JVM) and HP scientific calculators."
)
pn.br()

# =============================================================================
#  3.6  ONE-ADDRESS INSTRUCTIONS
# =============================================================================
pn.chap_box("3.6  One-Address Instructions")
pn.section("Concept")
pn.definition(
    "<b>One-Address Instructions:</b> Instructions that contain the opcode and "
    "one explicit operand address. The second operand is always the "
    "<b>Accumulator (AC)</b> -- a dedicated CPU register. Results are always "
    "placed back in the AC. Also called <b>Accumulator-Based</b> architecture."
)
pn.code_block("""
 ONE-ADDRESS INSTRUCTION SET EXAMPLE (Accumulator Machine):
 ======================================================
 Instructions: LOAD addr, STORE addr, ADD addr, SUB addr, MUL addr, DIV addr

 Compute: X = (A + B) * (C + D)

 Machine code (one-address / accumulator):
   LOAD  A    ; AC <- M[A]           (AC = A)
   ADD   B    ; AC <- AC + M[B]      (AC = A+B)
   STORE T    ; M[T] <- AC           (save A+B to temporary memory location T)
   LOAD  C    ; AC <- M[C]           (AC = C)
   ADD   D    ; AC <- AC + M[D]      (AC = C+D)
   MUL   T    ; AC <- AC * M[T]      (AC = (C+D)*(A+B))
   STORE X    ; M[X] <- AC           (store final result)

 Number of instructions: 7
 Each instruction has exactly 1 address field (the memory operand).
 AC is the implicit destination for all arithmetic.
""")

pn.tip(
    "One-address: AC is always the implicit operand and destination. "
    "Requires STORE/LOAD for temporary values (like T). "
    "More instructions needed than two/three-address. "
    "Classic examples: Intel 8080, MOS 6502."
)
pn.br()

# =============================================================================
#  3.7  TWO-ADDRESS INSTRUCTIONS
# =============================================================================
pn.chap_box("3.7  Two-Address Instructions")
pn.section("Concept")
pn.definition(
    "<b>Two-Address Instructions:</b> Instructions that contain the opcode and "
    "two operand addresses. One address is the source, and the other is both the "
    "second source AND the destination (the result overwrites one source operand). "
    "This is the format used by Intel x86 for most arithmetic and logic operations."
)
pn.code_block("""
 TWO-ADDRESS INSTRUCTION FORMAT:
 ======================================================
 Format: OPCODE  Dest/Src1,  Src2
 Effect: Dest <- Dest op Src2

 Compute: X = (A + B) * (C + D)

 Machine code (two-address, using registers R1, R2):
   MOV  R1, A    ; R1 <- M[A]
   ADD  R1, B    ; R1 <- R1 + M[B]  = A+B
   MOV  R2, C    ; R2 <- M[C]
   ADD  R2, D    ; R2 <- R2 + M[D]  = C+D
   MUL  R1, R2   ; R1 <- R1 * R2 = (A+B)*(C+D)
   MOV  X,  R1   ; M[X] <- R1       (store final result in X)

 Number of instructions: 6
 Each instruction has 2 address fields.
 DRAWBACK: one source operand is destroyed (overwritten by result).
           Must save values if needed again.
""")

pn.frame_format(
    "Two-Address Instruction Word (16-bit example)",
    [
        ("OPCODE (4b)", "4 bits"),
        ("DEST (4b)", "4 bits"),
        ("SRC (4b)", "4 bits"),
        ("MODE (4b)", "4 bits"),
    ],
)
pn.tip(
    "Two-address: result overwrites one source (Dest <- Dest op Src). "
    "x86 family uses this format (e.g., ADD EAX, EBX means EAX = EAX + EBX). "
    "Need extra MOV instructions to preserve operands before overwriting."
)
pn.br()

# =============================================================================
#  3.8  THREE-ADDRESS INSTRUCTIONS
# =============================================================================
pn.chap_box("3.8  Three-Address Instructions")
pn.section("Concept")
pn.definition(
    "<b>Three-Address Instructions:</b> Instructions that contain the opcode and "
    "three operand addresses -- two source operands and one distinct destination. "
    "No source is destroyed. This allows maximum flexibility and is the format "
    "used by RISC architectures (MIPS, ARM, RISC-V)."
)
pn.code_block("""
 THREE-ADDRESS INSTRUCTION FORMAT:
 ======================================================
 Format: OPCODE  Dest,  Src1,  Src2
 Effect: Dest <- Src1 op Src2

 Compute: X = (A + B) * (C + D)

 Machine code (three-address, using registers R1, R2):
   ADD  R1, A, B    ; R1 <- M[A] + M[B]
   ADD  R2, C, D    ; R2 <- M[C] + M[D]
   MUL  X, R1, R2   ; M[X] <- R1 * R2  = (A+B)*(C+D)

 Number of instructions: 3  (fewest instructions for this expression!)
 Sources are NEVER destroyed -- destination is always separate.

 TRADE-OFF: Instruction word must be wide enough for 3 address fields.
   Example: 3 x 5-bit register fields + 6-bit opcode = 21 bits minimum.
   MIPS and ARM use fixed 32-bit instructions with 3 register fields.
""")

pn.frame_format(
    "Three-Address RISC Instruction Word (32-bit)",
    [
        ("OPCODE (6b)", "6 bits"),
        ("DEST (5b)", "5 bits"),
        ("SRC1 (5b)", "5 bits"),
        ("SRC2 (5b)", "5 bits"),
        ("FUNCT/IMM (11b)", "11 bits"),
    ],
)

pn.section("Comparison of All Four Address Formats")
pn.info_table(
    [
        "Format",
        "Instructions for (A+B)*(C+D)",
        "Instruction Width",
        "Source Preserved?",
        "Example ISA",
    ],
    [
        [
            "Zero-address",
            "8 (PUSH/POP + ops)",
            "Short (opcode only)",
            "N/A (stack)",
            "Forth, JVM",
        ],
        [
            "One-address",
            "7 (LOAD/STORE/ops)",
            "Medium (opcode + 1 addr)",
            "No (AC overwritten)",
            "8080, 6502",
        ],
        [
            "Two-address",
            "6 (MOV + ops)",
            "Medium (opcode + 2 addr)",
            "No (dest overwritten)",
            "x86 (Intel)",
        ],
        [
            "Three-address",
            "3 (ops)",
            "Wider (opcode + 3 addr)",
            "Yes (separate dest)",
            "MIPS, ARM, RISC-V",
        ],
    ],
)
pn.tip(
    "Three-address: fewest instructions, widest word. "
    "Two-address: x86 style, one source destroyed. "
    "One-address: accumulator style, many LOAD/STORE needed. "
    "Zero-address: stack machine, most compact per instruction but most instructions."
)
pn.br()

# =============================================================================
#  3.9  RISC vs CISC
# =============================================================================
pn.chap_box("3.9  RISC vs CISC Characteristics")
pn.section("Definitions")
pn.definition(
    "<b>RISC (Reduced Instruction Set Computer):</b> A CPU design philosophy that "
    "uses a small set of simple, fixed-length instructions that each execute in "
    "exactly one clock cycle (when pipelined). All computation is performed in "
    "registers. Only LOAD and STORE access memory."
)
pn.definition(
    "<b>CISC (Complex Instruction Set Computer):</b> A CPU design philosophy that "
    "uses a large set of complex, variable-length instructions. A single instruction "
    "may perform multiple operations (e.g., multiply-accumulate, string move). "
    "Instructions can directly access memory operands."
)

pn.section("Major Characteristics")
pn.subsection("RISC major characteristics")
pn.bullet(
    [
        "<b>Relatively few instructions:</b> Typically under 100 simple instructions.",
        "<b>Relatively few addressing modes:</b> Simplifies instruction decoding.",
        "<b>Memory access limited to LOAD and STORE:</b> Only dedicated instructions access memory.",
        "<b>Register-to-register operations:</b> All operations are done within the registers of the CPU.",
        "<b>Fixed-length, easily decoded instructions:</b> Easy to decode simultaneously by the control unit.",
        "<b>Single-cycle instruction execution:</b> Pipelined stages allow 1-cycle throughput.",
        "<b>Hardwired control:</b> Hardwired control logic is preferred over microprogrammed control for speed."
    ]
)
pn.subsection("CISC major characteristics")
pn.bullet(
    [
        "<b>Large instruction set:</b> Typically from 100 to 250 instructions.",
        "<b>Specialized instructions:</b> Instructions that perform specialized tasks and are used infrequently.",
        "<b>Large variety of addressing modes:</b> Typically from 5 to 20 different modes.",
        "<b>Variable-length instruction formats:</b> Requires complex decoding logic to frame instructions.",
        "<b>Memory-resident operands:</b> Instructions can directly manipulate operands residing in memory."
    ]
)

pn.section("CISC vs RISC Comparison Table")
pn.info_table(
    ["Characteristic", "RISC", "CISC"],
    [
        [
            "Instruction count",
            "Large (many simple instructions)",
            "Small (few complex instructions)",
        ],
        ["Instruction length", "Fixed (e.g., 32 bits)", "Variable (1-15 bytes in x86)"],
        [
            "Instruction complexity",
            "Simple, each does one operation",
            "Complex, each may do multiple operations",
        ],
        [
            "Execution time",
            "1 cycle per instruction (pipelined)",
            "Multiple cycles per complex instruction",
        ],
        [
            "Registers",
            "Large register file (16-32 GP registers)",
            "Fewer general-purpose registers",
        ],
        [
            "Memory access",
            "Only LOAD and STORE access memory",
            "Any instruction can access memory",
        ],
        [
            "Addressing modes",
            "Few (register, immediate, base+offset)",
            "Many (direct, indirect, indexed, auto-increment, etc.)",
        ],
        ["Control unit", "Hardwired (fast)", "Microprogrammed (flexible, slower)"],
        [
            "Pipelining",
            "Excellent (fixed length, simple stages)",
            "Difficult (variable length, multi-cycle ops)",
        ],
        [
            "Code density",
            "Larger code (more instructions)",
            "Smaller code (fewer but complex instructions)",
        ],
        [
            "Compiler burden",
            "Higher (compiler must optimize sequences)",
            "Lower (single instruction can do more)",
        ],
        [
            "Examples",
            "ARM, MIPS, RISC-V, PowerPC, SPARC",
            "Intel x86, x86-64, IBM System/360",
        ],
    ],
)

# RISC vs CISC pipeline diagram
left_pipe = pd.LayeredStack(
    width=pn.CW * 0.44,
    height=200,
    theme=diag_theme,
    caption="RISC Pipeline (simple, efficient)",
)
left_pipe.layer("IF -- Instruction Fetch", sublabel="Fixed 32-bit word, fast")
left_pipe.layer("ID -- Instruction Decode", sublabel="Simple decode, 1 cycle")
left_pipe.layer("EX -- Execute", sublabel="ALU operation, registers only")
left_pipe.layer("MEM -- Memory Access", sublabel="Only LOAD/STORE touch memory")
left_pipe.layer("WB -- Write Back", sublabel="Result to register file")

right_pipe = pd.LayeredStack(
    width=pn.CW * 0.44,
    height=200,
    theme=diag_theme,
    caption="CISC Pipeline (complex, variable)",
)
right_pipe.layer("Prefetch Queue", sublabel="Variable-length instruction bytes")
right_pipe.layer("Decode (1-3 cycles)", sublabel="Complex microcode dispatch")
right_pipe.layer("Micro-op execution", sublabel="Micro-operations issued to units")
right_pipe.layer("Memory (optional)", sublabel="Operand can be memory address")
right_pipe.layer("Retire / Writeback", sublabel="Result committed in order")

left_pipe.as_flowable()
right_pipe.as_flowable()

tbl_pipe = Table(
    [
        [
            ResponsiveDrawingFlowable(left_pipe.drawing),
            ResponsiveDrawingFlowable(right_pipe.drawing),
        ]
    ],
    colWidths=[pn.CW * 0.48, pn.CW * 0.48],
)
tbl_pipe.setStyle(
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
pn.add(tbl_pipe)
pn.sp(6)
pn.add(
    Paragraph(
        "Fig 4 (left): RISC 5-stage pipeline (IF/ID/EX/MEM/WB).  |  Fig 4 (right): CISC variable pipeline with micro-op dispatch.",
        pn.COVER_SUB,
    )
)

pn.tip(
    "RISC: fixed-length instructions, large register file, hardwired CU, pipelining-friendly. "
    "CISC: variable-length, few registers, microprogrammed CU, compact code. "
    "Modern x86 (Intel/AMD) internally translates CISC instructions to RISC-like micro-ops!"
)
pn.br()

# =============================================================================
#  3.10  ADDRESSING MODES
# =============================================================================
pn.chap_box("3.10  Addressing Modes")
pn.section("What is an Addressing Mode?")
pn.definition(
    "<b>Addressing Mode:</b> The method by which the CPU determines the effective "
    "address (EA) of the operand for an instruction. The EA is the actual memory "
    "address or register that holds the data. Different addressing modes provide "
    "flexibility for accessing arrays, stack frames, and program-relative data."
)

pn.section("All Major Addressing Modes")
pn.info_table(
    ["Mode", "Effective Address (EA) Formula", "Example Syntax", "Explanation / Use Case"],
    [
        [
            "Implied / Inherent",
            "Operand is implicit in opcode",
            "PUSH, POP, CMA",
            "Operands on stack top or implied register (e.g. Accumulator)",
        ],
        [
            "Immediate",
            "Operand is part of instruction",
            "MOV A, #20",
            "Initializing registers to a constant value",
        ],
        [
            "Register",
            "EA = Selected processor register",
            "MOV R1, R2",
            "Operands reside in registers; no memory access",
        ],
        [
            "Register Indirect",
            "EA = [Register contents]",
            "MOV A, (R0)",
            "Selected register contains the memory address of the operand",
        ],
        [
            "Direct (Absolute)",
            "EA = Address part of instruction",
            "MOV A, 2000",
            "Operand resides in memory; its address is given directly",
        ],
        [
            "Indirect",
            "EA = M[Address part of instruction]",
            "LOAD R1, @100",
            "Instruction address part points to a memory word that holds the EA",
        ],
        [
            "Relative (PC-Relative)",
            "EA = PC + Address part of instruction",
            "BNE 24",
            "Content of PC is added to the offset; used for branch instructions",
        ],
        [
            "Indexed",
            "EA = Index Register (XR) + Address part",
            "LOAD R1, 100(R2)",
            "Index register contains offset; used for array indexing",
        ],
        [
            "Base Register",
            "EA = Base Register (BR) + Address part",
            "LOAD R1, R2+#8",
            "Base register contains segment base; used for memory relocation",
        ],
    ],
)

pn.section("Relative Addressing Mode Example")
pn.body(
    "<b>Relative Addressing Mode Example:</b><br/>"
    "Assume that the Program Counter (PC) contains the number <b>825</b> and the address part of the instruction "
    "contains the number <b>24</b>. During the fetch phase, the instruction at location 825 is read from memory, and the "
    "PC is immediately incremented by one to <b>826</b>. The effective address (EA) computation is:<br/>"
    "<b>EA = incremented PC + address part = 826 + 24 = 850</b>."
)

pn.section("Addressing Mode Examples (RTL)")
pn.code_block("""
 ADDRESSING MODE SUMMARY WITH EXAMPLES:
 ======================================================
 Instruction field: OPCODE | MODE | ADDRESS/OPERAND

 1. IMPLIED:       PUSH               EA = TOS (implied stack top)
                   CMA                EA = AC (complement accumulator)

 2. IMMEDIATE:     MOV A, #20         Operand = 20 (stored in instruction itself)
                   AC <- 20

 3. REGISTER:      MOV R1, R2         EA = R2 (no memory access)
                   R1 <- R2

 4. REG INDIRECT:  MOV A, (R0)        EA = M[R0] (R0 holds memory pointer)
                   AC <- M[R0]

 5. DIRECT:        MOV A, 2000        EA = 2000
                   AC <- M[2000]

 6. INDIRECT:      LOAD R1, @100      EA = M[100] (address 100 holds pointer to EA)
                   R1 <- M[M[100]]

 7. PC-RELATIVE:   BNE 24             EA = PC + 24 (PC is already incremented)
                   PC <- PC + 24

 8. INDEXED:       LOAD R1, 100(R2)   EA = 100 + R2 (R2 acts as index register XR)
                   R1 <- M[100 + R2]

 9. BASE REGISTER: LOAD R1, R2+#8     EA = R2 + 8 (R2 acts as base register BR)
                   R1 <- M[R2 + 8]
""")

pn.tip(
    "Know the EA formula for each mode. "
    "Immediate: no memory access, value in instruction. "
    "Direct: 1 memory access. Indirect: 2 memory accesses (pointer). "
    "Indexed: EA = base + index (used for arrays). "
    "PC-relative: used for branches (position-independent code)."
)
pn.br()

# =============================================================================
#  3.11  INSTRUCTION SET COMPLETENESS
# =============================================================================
pn.chap_box("3.11  Instruction Set Completeness")
pn.section("Concept")
pn.definition(
    "<b>Instruction Set Completeness:</b> An instruction set is said to be complete "
    "if it contains a sufficient set of instructions in each basic category to allow "
    "the user to write programs for any computational task. Although computers differ "
    "in their addressing modes, the fundamental operations they support are highly standardized."
)
pn.body(
    "Most computer instructions fall into one of three basic categories:<br/>"
    "1. <b>Data Transfer Instructions:</b> Move data from one location to another without altering its content.<br/>"
    "2. <b>Data Manipulation Instructions:</b> Perform arithmetic, logical, or shift operations to process data.<br/>"
    "3. <b>Program Control Instructions:</b> Modify the Program Counter (PC) to alter the flow of execution."
)

pn.section("1. Data Transfer Instructions")
pn.body(
    "These instructions transfer data between memory and processor registers, between registers, "
    "or between registers and I/O devices. Table 8-5 lists typical data transfer instructions:"
)
pn.info_table(
    ["Instruction Name", "Mnemonic Mapped in Many ISAs", "Operation Description"],
    [
        ["Load", "LD / LDR", "Transfer word from memory to CPU register (e.g. AC)"],
        ["Store", "ST / STR", "Transfer word from CPU register to memory"],
        ["Move", "MOV", "Transfer data between registers, or register and memory"],
        ["Exchange", "XCH / SWP", "Swap information between two registers, or register and memory"],
        ["Input", "IN", "Transfer data from peripheral device to CPU register"],
        ["Output", "OUT", "Transfer data from CPU register to peripheral device"],
        ["Push", "PUSH", "Transfer word from register to top of memory stack"],
        ["Pop", "POP", "Transfer word from top of memory stack to register"],
    ],
)
pn.sp(6)

pn.section("2. Data Manipulation Instructions")
pn.body(
    "These instructions perform calculations and logic processing. They are divided into three types:<br/>"
    "• <b>Arithmetic Instructions:</b> The four basic operations are Addition, Subtraction, Multiplication, and Division. "
    "If multiplication/division are missing in hardware, they are implemented via software subroutines.<br/>"
    "• <b>Logical and Bit Manipulation:</b> Perform bitwise operations on strings of bits in registers. Useful for clearing, setting, "
    "or testing specific bits. Table 8-8 lists logical operations:<br/>"
    "• <b>Shift Instructions:</b> Shift bits left or right. Can be <i>logical shifts</i> (fill with 0s), "
    "<i>arithmetic shifts</i> (preserve sign bit on right shift), or <i>rotate-type shifts</i> (circular shifts)."
)
pn.info_table(
    ["Logical Operation", "Typical Mnemonic", "Operation Description"],
    [
        ["Clear", "CLR", "Replace all bits of the operand with 0's"],
        ["Complement", "COM / NOT", "Invert all bits (produce 1's complement)"],
        ["Logical AND", "AND", "Bitwise AND operation; used to clear/mask groups of bits"],
        ["Logical OR", "OR", "Bitwise OR operation; used to set groups of bits to 1"],
        ["Logical XOR", "XOR", "Bitwise Exclusive OR; used to complement groups of bits"],
    ],
)
pn.sp(6)

pn.section("3. Program Control Instructions")
pn.body(
    "Program control instructions change the value of the Program Counter (PC) to break the "
    "sequential flow of execution. This provides decision-making capability and branching:<br/>"
    "• <b>Unconditional Branch / Jump:</b> Forces a branch to a specified memory address without checking any conditions.<br/>"
    "• <b>Conditional Branch / Jump:</b> Checks status flags (e.g. Zero, Sign, Carry, Overflow). If the condition is met, "
    "the PC is loaded with the target address. If the condition is not met, the PC remains unchanged and the next sequential instruction is executed."
)
pn.sp(8)

# =============================================================================
#  3.12  MODES OF DATA TRANSFER
# =============================================================================
pn.chap_box("3.12  Modes of Data Transfer (I/O)")
pn.section("Overview")
pn.definition(
    "<b>Modes of Transfer:</b> The different methods by which data is transferred "
    "between the central computer (CPU/Memory) and external I/O devices. "
    "Data transfer to and from peripherals may be handled in one of three possible modes:<br/>"
    "1. <b>Programmed I/O:</b> CPU is in constant control of the transfer and must poll status flags.<br/>"
    "2. <b>Interrupt-Initiated I/O:</b> CPU continues normal execution, and the interface interrupts when ready.<br/>"
    "3. <b>Direct Memory Access (DMA):</b> Data is transferred directly between the peripheral and memory without CPU intervention."
)

pn.info_table(
    ["Mode", "How It Works", "CPU Involvement", "Speed", "Use Case"],
    [
        [
            "Programmed I/O\n(Polling)",
            "CPU continuously checks (polls) the I/O device status register in a busy-wait loop.",
            "100% (CPU cannot do other work while waiting)",
            "Slow (limited by polling rate)",
            "Simple microcontrollers, very slow devices",
        ],
        [
            "Interrupt-Driven I/O",
            "CPU issues I/O command and continues executing. Device interrupts CPU when ready.",
            "Low (only during ISR execution)",
            "Moderate (overhead per byte for context save/restore)",
            "Keyboards, serial ports, general I/O",
        ],
        [
            "Direct Memory Access\n(DMA)",
            "DMA controller transfers data directly between I/O device and memory without CPU intervention.",
            "Minimal (only at start and end of transfer)",
            "Very fast (bus-rate transfer)",
            "Disk, network, audio, GPU transfers (large blocks)",
        ],
    ],
)
pn.sp(6)

pn.section("Programmed I/O Handshaking Protocol")
pn.body(
    "In the programmed I/O method, the I/O device has no direct access to memory. A transfer requires the CPU to execute "
    "instructions to move data first to a CPU register and then to memory. Below is the detailed handshake procedure "
    "for data transfer from a device into the CPU:<br/>"
    "1. <b>Data Valid:</b> The I/O device places a byte of data on the I/O bus and enables the <i>Data Valid</i> line.<br/>"
    "2. <b>Data Accepted & Flag F:</b> The interface accepts the byte into its data register, enables the <i>Data Accepted</i> line, "
    "and sets the <b>F (Flag) bit</b> in its status register to 1.<br/>"
    "3. <b>Device Hold:</b> The device disables its Data Valid line, but will not transfer the next byte until the Data Accepted line is disabled.<br/>"
    "4. <b>CPU Read:</b> The CPU executes instructions to read the status register. If F = 1, it reads the data register, which "
    "clears the F flag back to 0.<br/>"
    "5. <b>Handshake Reset:</b> Once the F flag is cleared, the interface disables the Data Accepted line, allowing the I/O device to "
    "send the next data byte."
)
pn.sp(6)

# I/O mode comparison sequence diagram
seq_io = pd.SequenceDiagram(
    width=pn.CW,
    height=280,
    theme=diag_theme,
    caption="Fig 6: Three modes of I/O transfer -- polling, interrupt, and DMA",
)
seq_io.actor("cpu", "CPU")
seq_io.actor("io", "I/O Device")
seq_io.actor("mem", "Memory")
seq_io.divider("Mode 1: Programmed I/O (Polling)")
seq_io.message("cpu", "io", "Issue I/O command", arrow="solid")
seq_io.message("cpu", "io", "Poll: Is data ready? (repeat until yes)", arrow="solid")
seq_io.message("io", "cpu", "Data ready", arrow="dashed")
seq_io.message("cpu", "mem", "CPU writes data to memory", arrow="solid")
seq_io.divider("Mode 2: Interrupt-Driven I/O")
seq_io.message("cpu", "io", "Issue I/O command, then continue", arrow="solid")
seq_io.message("io", "cpu", "INTERRUPT: data ready", arrow="dashed")
seq_io.message("cpu", "mem", "ISR: CPU transfers data to memory", arrow="solid")
seq_io.divider("Mode 3: DMA")
seq_io.message(
    "cpu", "io", "Program DMA controller (address, count, direction)", arrow="solid"
)
seq_io.message("io", "mem", "DMA transfers data directly to memory", arrow="solid")
seq_io.message("io", "cpu", "INTERRUPT: DMA complete", arrow="dashed")
pn.story.extend(seq_io.as_flowable())

pn.tip(
    "Programmed I/O: CPU polls -- wastes CPU time. "
    "Interrupt-Driven: device signals CPU -- efficient for slow devices. "
    "DMA: controller moves data to/from memory -- CPU is free. "
    "Rule: use DMA for large fast transfers (disk, video); interrupt for slow devices."
)
pn.br()

# =============================================================================
#  3.13  PRIORITY INTERRUPT AND DAISY CHAINING
# =============================================================================
pn.chap_box("3.13  Priority Interrupt and Daisy Chaining")
pn.section("Interrupt Concept")
pn.definition(
    "<b>Interrupt:</b> A signal to the CPU from an external device (or software) "
    "indicating that it needs immediate attention. When an interrupt is accepted, "
    "the CPU suspends the current program, saves its state (PC, PSW), executes an "
    "<b>Interrupt Service Routine (ISR)</b>, then restores state and resumes."
)

pn.section("Types of Interrupts")
pn.info_table(
    ["Type", "Source", "Maskable?", "Examples"],
    [
        [
            "Hardware (External)",
            "I/O devices, timers, external signals",
            "Yes (via IF flag)",
            "Keyboard ready, disk complete, timer tick",
        ],
        [
            "Software (Trap/SVC)",
            "Program executes INT instruction",
            "No",
            "System calls (OS services), debug breakpoints",
        ],
        [
            "Exception (Internal)",
            "CPU detects error during execution",
            "No",
            "Divide by zero, illegal opcode, page fault, overflow",
        ],
        [
            "NMI (Non-Maskable)",
            "Critical hardware failure",
            "No (always serviced)",
            "Power failure, memory parity error, watchdog",
        ],
    ],
)

pn.section("Priority Interrupt -- Vectored Interrupts")
pn.definition(
    "<b>Vectored Interrupt:</b> Each interrupting device is assigned a unique "
    "<b>interrupt vector</b> -- the address of its ISR stored in an interrupt "
    "vector table. When a device interrupts, it places its vector number on the "
    "data bus and the CPU fetches the ISR address from the corresponding entry "
    "in the interrupt vector table. No software polling needed."
)
pn.code_block("""
 INTERRUPT VECTOR TABLE EXAMPLE (x86 style):
 ======================================================
 Address   | Vector | ISR Description
 ----------|--------|---------------------------
   0x00    |   0    | Divide-by-Zero ISR
   0x04    |   1    | Single-Step Debug ISR
   0x08    |   2    | NMI ISR
   0x0C    |   3    | Breakpoint ISR
   ...     |  ...   | ...
   0x80    |  32    | Timer IRQ0 ISR
   0x84    |  33    | Keyboard IRQ1 ISR
   0x88    |  34    | Serial Port IRQ2 ISR
   ...     |  ...   | ...

 INTERRUPT ACCEPTANCE SEQUENCE:
   1. Device asserts INTR (interrupt request) line.
   2. CPU checks IF (Interrupt Flag). If IF=1: acknowledge.
   3. CPU asserts INTA (interrupt acknowledge).
   4. Device places vector number V on data bus.
   5. CPU reads V, looks up ISR address = IVT[V].
   6. CPU saves PC and PSW to stack.
   7. CPU loads PC <- IVT[V] (jumps to ISR).
   8. ISR executes, clears the interrupt source.
   9. ISR executes IRET: restores PC and PSW from stack.
""")

pn.section("Daisy Chaining (Serial Priority)")
pn.definition(
    "<b>Daisy Chaining:</b> A hardware method for resolving multiple simultaneous "
    "interrupt requests. All devices share a common interrupt line (INTR). "
    "The CPU's interrupt acknowledge (INTA) signal is passed serially through all "
    "devices -- the first device in the chain that has a pending interrupt captures "
    "the acknowledge and places its vector on the bus. Devices nearer the CPU have "
    "higher priority."
)

net_daisy = pd.NetworkDiagram(
    width=pn.CW,
    height=200,
    theme=diag_theme,
    caption="Fig 7: Daisy-chain interrupt priority -- INTA propagates through devices",
)
net_daisy.node("cpu", "CPU", x=55, y=130, kind="server")
net_daisy.node("dev1", "Device 1\n(Highest Priority)", x=175, y=130, kind="host")
net_daisy.node("dev2", "Device 2\n(Medium Priority)", x=300, y=130, kind="host")
net_daisy.node("dev3", "Device 3\n(Lowest Priority)", x=420, y=130, kind="host")
net_daisy.node("intr_bus", "Common INTR Line", x=240, y=50, kind="bus")

net_daisy.link("cpu", "dev1", label="INTA")
net_daisy.link("dev1", "dev2", label="INTA (if Dev1 idle)")
net_daisy.link("dev2", "dev3", label="INTA (if Dev2 idle)")
net_daisy.link("cpu", "intr_bus", label="INTR")
net_daisy.link("dev1", "intr_bus")
net_daisy.link("dev2", "intr_bus")
net_daisy.link("dev3", "intr_bus")
pn.story.extend(net_daisy.as_flowable())

pn.code_block("""
 DAISY CHAIN OPERATION:
 ======================================================
 1. One or more devices assert the shared INTR line HIGH.
 2. CPU finishes current instruction, detects INTR, asserts INTA.
 3. INTA propagates from CPU toward Device 1:
      - If Device 1 has pending interrupt: Device 1 BLOCKS INTA
        and places its vector on data bus. Higher priority served.
      - If Device 1 has NO pending interrupt: Device 1 PASSES INTA
        to Device 2 (ripple effect).
 4. First device with pending interrupt captures INTA, sends vector.
 5. CPU uses vector to jump to that device's ISR.

 PRIORITY: Device 1 > Device 2 > Device 3 (position in chain)

 ADVANTAGES:
   Simple hardware (just wire INTA in series).
   No software arbitration needed.

 DISADVANTAGES:
   Low-priority devices may be starved if high-priority is always active.
   Adding devices requires rewiring.
   Propagation delay limits speed with many devices.
""")

pn.tip(
    "Daisy chain: priority determined by position in chain (nearest CPU = highest). "
    "INTA passes through chain; first device with pending interrupt captures it. "
    "Alternative: parallel priority encoder (each device has dedicated interrupt line). "
    "Vectored interrupts: device places ISR address on bus (no software polling needed)."
)
pn.br()

# =============================================================================
#  3.14  DIRECT MEMORY ACCESS (DMA)
# =============================================================================
pn.chap_box("3.14  Direct Memory Access (DMA)")
pn.section("DMA Overview")
pn.definition(
    "<b>DMA (Direct Memory Access):</b> A hardware mechanism that allows I/O "
    "devices to transfer data directly to or from main memory WITHOUT involving "
    "the CPU for each data word. The CPU programs the DMA controller with the "
    "memory address, byte count, and direction, then the DMA controller autonomously "
    "handles the transfer -- freeing the CPU to execute other instructions."
)

pn.section("DMA Controller Registers")
pn.info_table(
    ["Register", "Contents", "Purpose"],
    [
        [
            "Address Register",
            "Starting memory address for the transfer",
            "DMA increments this after each word transferred",
        ],
        [
            "Word Count Register",
            "Number of words (bytes) to transfer",
            "DMA decrements after each transfer; done when zero",
        ],
        [
            "Control Register",
            "Transfer direction (read/write), interrupt enable, start bit",
            "Controls DMA operation mode",
        ],
        [
            "Status Register",
            "Done flag, error flag, bus granted flag",
            "CPU reads to check transfer completion",
        ],
    ],
)

pn.section("DMA Transfer Modes")
pn.info_table(
    ["Mode", "How It Works", "CPU Impact", "Use Case"],
    [
        [
            "Burst Mode\n(Block Transfer)",
            "DMA seizes bus and transfers ALL words without releasing until complete.",
            "CPU blocked from bus for entire transfer (may take ms).",
            "Disk/tape sector reads, GPU texture upload",
        ],
        [
            "Cycle Stealing",
            "DMA steals ONE bus cycle at a time from the CPU, then releases bus.",
            "CPU slowed (each stolen cycle adds latency) but not fully blocked.",
            "Streaming devices -- audio, serial lines",
        ],
        [
            "Transparent Mode\n(Hidden DMA)",
            "DMA only transfers when CPU is not using the bus (idle cycles).",
            "CPU is unaffected -- no slowdown.",
            "Low-priority background transfers",
        ],
    ],
)

pn.section("DMA Transfer Flowchart")
fc_dma = pd.Flowchart(
    width=pn.CW,
    height=340,
    theme=diag_theme,
    caption="Fig 8: DMA transfer operation -- initialization and autonomous data movement",
)
fc_dma.terminal("start", "CPU programs DMA:\nAddress, Count, Direction")
fc_dma.process("init", "DMA Controller initialized;\nCPU resumes normal execution")
fc_dma.process("req", "I/O Device ready;\nDMA asserts Bus Request (BR)")
fc_dma.decision("grant", "CPU grants bus?\n(Bus Grant BG asserted)")
fc_dma.process("wait", "DMA waits for bus\n(CPU finishes memory cycle)")
fc_dma.process("xfer", "DMA transfers 1 word:\nDevice <-> Memory[Address]")
fc_dma.process("update", "Address++; Count--")
fc_dma.decision("done", "Count == 0?")
fc_dma.process("next", "Request bus for\nnext word")
fc_dma.process("intr", "DMA raises Interrupt\n(transfer complete)")
fc_dma.terminal("end", "CPU services interrupt:\nprocess transferred data")

fc_dma.edge("start", "init")
fc_dma.edge("init", "req")
fc_dma.edge("req", "grant")
fc_dma.edge("grant", "wait", branch="no")
fc_dma.edge("grant", "xfer", branch="yes")
fc_dma.edge("wait", "grant", orthogonal=True)
fc_dma.edge("xfer", "update")
fc_dma.edge("update", "done")
fc_dma.edge("done", "intr", branch="yes")
fc_dma.edge("done", "next", branch="no")
fc_dma.edge("next", "req", orthogonal=True)
fc_dma.edge("intr", "end")
pn.story.extend(fc_dma.as_flowable())

pn.section("DMA Architecture")
net_dma = pd.NetworkDiagram(
    width=pn.CW,
    height=260,
    theme=diag_theme,
    caption="Fig 9: DMA system architecture -- CPU, DMA controller, memory, and device",
)
net_dma.node("cpu", "CPU", x=90, y=200, kind="server")
net_dma.node("dma", "DMA Controller", x=250, y=200, kind="generic")
net_dma.node("mem", "Main Memory", x=410, y=200, kind="database")
net_dma.node("bus", "System Bus", x=250, y=110, kind="switch")
net_dma.node("device", "I/O Device\n(Disk/NIC)", x=410, y=40, kind="storage")
net_dma.link("cpu", "bus", label="Address/Data/Ctrl")
net_dma.link("dma", "bus", label="Bus Request/Grant")
net_dma.link("mem", "bus", label="")
net_dma.link("cpu", "dma", label="Program & Interrupt")
net_dma.link("device", "dma", label="Data Ready")
net_dma.link("device", "mem", label="Direct Transfer (via DMA)")
pn.story.extend(net_dma.as_flowable())

pn.tip(
    "DMA: CPU programs controller (address, count, mode), then steps aside. "
    "DMA arbitrates for bus and transfers data directly to/from memory. "
    "Interrupt CPU when done. Cycle stealing: 1 cycle at a time (less CPU impact). "
    "Burst mode: fastest but CPU locked out until done."
)
pn.br()

# =============================================================================
#  3.15  INPUT-OUTPUT PROCESSOR (IOP)
# =============================================================================
pn.chap_box("3.15  Input-Output Processor (IOP)")
pn.section("What is an IOP?")
pn.definition(
    "<b>Input-Output Processor (IOP):</b> A specialized processor dedicated to "
    "handling I/O operations on behalf of the main CPU. Unlike a simple DMA "
    "controller (which only moves data), an IOP can execute a sequence of I/O "
    "instructions (a <b>channel program</b> or <b>I/O program</b>) stored in "
    "memory. The IOP operates autonomously, freeing the main CPU completely."
)

pn.section("IOP vs DMA Comparison")
pn.info_table(
    ["Feature", "DMA Controller", "I/O Processor (IOP)"],
    [
        [
            "Intelligence",
            "Fixed function: transfer data between device and memory",
            "Programmable: executes I/O channel programs",
        ],
        [
            "Instruction set",
            "None (hardwired address/count/control)",
            "Has its own instruction set (I/O instructions)",
        ],
        [
            "Program storage",
            "Registers only (address, count, control)",
            "Channel program stored in main memory",
        ],
        [
            "Flexibility",
            "Limited: one device, one transfer direction",
            "High: can handle complex I/O sequences",
        ],
        [
            "Bus sharing",
            "Shares main CPU bus (cycle stealing or burst)",
            "May have dedicated I/O bus",
        ],
        [
            "Interrupt to CPU",
            "At end of single transfer",
            "At end of entire I/O operation sequence",
        ],
        ["Examples", "8237 DMA chip, SoC DMA", "IBM 360 Channel, Intel 8089 IOP"],
    ],
)

pn.section("Channel Program")
pn.definition(
    "<b>Channel Program:</b> A sequence of I/O instructions (Channel Command Words -- CCW) "
    "stored in main memory that the IOP executes to perform a complete I/O operation. "
    "The CPU only sets up the pointer to the channel program, then resumes. "
    "The IOP fetches and executes CCWs autonomously."
)
pn.code_block("""
 CHANNEL PROGRAM EXAMPLE (IBM 360 style):
 ======================================================
 Goal: Read one disk sector (512 bytes) into memory buffer at address 5000

 CPU initializes IOP:
   Stores pointer to channel program at IOP Control Block address.
   Issues START I/O (SIO) instruction.
   CPU resumes normal execution.

 IOP executes channel program:
   CCW 1: SEEK  cylinder=10, head=2    ; Position disk head
   CCW 2: SEARCH ID  sector=5          ; Find correct sector
   CCW 3: READ   count=512, addr=5000  ; Read 512 bytes to M[5000]
   CCW 4: (end-of-chain flag set)       ; Signal completion

 IOP notifies CPU:
   IOP raises interrupt when all CCWs complete.
   CPU reads IOP status to check for errors.

 IOP ADVANTAGES:
   CPU is 100% free during entire I/O sequence.
   Complex I/O operations (seek + read + verify) in one channel program.
   Multiple IOPs can run simultaneously (parallel I/O).
""")

pn.section("IOP System Architecture")
net_iop = pd.NetworkDiagram(
    width=pn.CW,
    height=260,
    theme=diag_theme,
    caption="Fig 10: IOP system architecture -- main CPU, IOP, and I/O devices",
)
net_iop.node("cpu", "Main CPU", x=100, y=190, kind="server")
net_iop.node(
    "mem", "Main Memory\n(Channel Programs + Data)", x=220, y=100, kind="database"
)
net_iop.node("iop", "I/O Processor\n(IOP / Channel)", x=340, y=190, kind="server")
net_iop.node("dev1", "Disk Drive", x=460, y=230, kind="storage")
net_iop.node("dev2", "Tape Drive", x=460, y=170, kind="storage")
net_iop.node("dev3", "Network NIC", x=460, y=110, kind="host")
net_iop.link("cpu", "mem", label="Program + Data Bus")
net_iop.link("cpu", "iop", label="SIO Command & Interrupt")
net_iop.link("iop", "mem", label="Fetch CCWs & Store Data")
net_iop.link("iop", "dev1", label="I/O Bus")
net_iop.link("iop", "dev2", label="I/O Bus")
net_iop.link("iop", "dev3", label="I/O Bus")
pn.story.extend(net_iop.as_flowable())

pn.tip(
    "IOP = smart DMA that executes I/O channel programs. "
    "CPU issues START I/O, then does other work. "
    "IOP fetches CCWs from memory and controls devices autonomously. "
    "Interrupt CPU only when the full I/O program (not just one transfer) completes. "
    "IBM mainframes use channel processors (IOP concept) extensively."
)
pn.br()

# =============================================================================
#  3.16  QUICK REVISION SUMMARY
# =============================================================================
pn.part_box("UNIT III -- QUICK REVISION SUMMARY")
pn.chap_box("Key Concepts at a Glance")

pn.info_table(
    ["Topic", "Key Point to Remember"],
    [
        [
            "CPU Instruction Cycle",
            "Fetch -> Decode -> Execute -> Interrupt Check -> Fetch. "
            "Interrupt check after EVERY instruction. Save PC/PSW before ISR.",
        ],
        [
            "Stack (LIFO)",
            "SP points to top. PUSH: SP--, M[SP]=data. POP: data=M[SP], SP++. "
            "Stack grows downward (toward lower addresses) in most architectures.",
        ],
        [
            "Subroutine Call",
            "CALL: push return address (PC) onto stack, jump to subroutine. "
            "RET: pop return address from stack, jump back.",
        ],
        [
            "RPN (Postfix)",
            "Operators follow operands. No parentheses needed. "
            "Evaluate: operand->PUSH; operator->POP 2, compute, PUSH result. "
            "Example: 5 3 + 2 * = (5+3)*2 = 16.",
        ],
        [
            "Infix to Postfix",
            "Scan left to right. Operand->output. '('->push. ')'->pop until '('. "
            "Operator->pop higher/equal precedence, then push current.",
        ],
        [
            "Zero-Address",
            "Stack machine. All arithmetic implicit on stack TOS. "
            "Only PUSH/POP have address. Compact per instruction but many instructions.",
        ],
        [
            "One-Address",
            "Accumulator (AC) is always implicit operand/destination. "
            "One address in instruction. Many LOAD/STORE needed. Example: 8080.",
        ],
        [
            "Two-Address",
            "Dest <- Dest op Src. Source is destroyed (overwritten). "
            "x86 uses this: ADD EAX, EBX means EAX = EAX + EBX.",
        ],
        [
            "Three-Address",
            "Dest <- Src1 op Src2. Sources preserved. "
            "RISC (MIPS/ARM): ADD R1, R2, R3 means R1 = R2 + R3. Fewest instructions.",
        ],
        [
            "RISC Characteristics",
            "Fixed-length instructions, large register file, load/store only memory access, "
            "hardwired CU, pipelining-friendly, simple addressing modes.",
        ],
        [
            "CISC Characteristics",
            "Variable-length instructions, few registers, memory-to-memory ops possible, "
            "microprogrammed CU, many addressing modes, compact code.",
        ],
        [
            "Immediate Addressing",
            "Operand IS the value (no memory access). EA = instruction field. "
            "Example: ADD R1, #5 -> R1 = R1 + 5.",
        ],
        [
            "Indirect Addressing",
            "Two memory accesses: first fetch gives address, second gives data. "
            "EA = M[address]. Used for pointer dereferencing.",
        ],
        [
            "Indexed Addressing",
            "EA = Base + Index register. Used for array access A[i]. "
            "Index register holds array subscript.",
        ],
        [
            "PC-Relative Addressing",
            "EA = PC + offset. Used for branch instructions. "
            "Enables position-independent code (PIC).",
        ],
        [
            "Programmed I/O (Polling)",
            "CPU busy-waits polling device status. Simple but wastes CPU. "
            "Use only for very simple/fast devices.",
        ],
        [
            "Interrupt-Driven I/O",
            "Device interrupts CPU when ready. CPU does other work while I/O proceeds. "
            "ISR handles the data transfer. Good for slow devices.",
        ],
        [
            "DMA",
            "DMA controller transfers blocks of data between device and memory without CPU. "
            "CPU programs DMA (address, count, mode), then is free. "
            "Interrupt CPU when done.",
        ],
        [
            "Daisy Chain Priority",
            "INTA propagates serially. Nearest CPU device = highest priority. "
            "First device with pending interrupt captures INTA and sends vector.",
        ],
        [
            "DMA Modes",
            "Burst: seizes bus entire block (fastest, CPU blocked). "
            "Cycle stealing: one word at a time (CPU slowed). "
            "Transparent: uses idle bus cycles (CPU unaffected).",
        ],
        [
            "IOP vs DMA",
            "IOP executes channel programs (sequences of I/O commands). "
            "DMA just moves data (fixed function). IOP is smarter and more flexible. "
            "IBM mainframe channels are IOPs.",
        ],
    ],
)

pn.highlight(
    "<b>UNIT III EXAM BLUEPRINT:</b>  "
    "2-mark: Define RPN. State PUSH/POP operations. Differentiate RISC and CISC. "
    "List addressing modes. Distinguish DMA and IOP.  "
    "5-mark: Convert infix to postfix and evaluate (show stack trace). "
    "Explain zero/one/two/three-address instructions with examples for (A+B)*(C+D). "
    "Explain daisy-chain interrupt with diagram. "
    "Explain DMA transfer with flowchart.  "
    "10-mark: Explain all addressing modes with EA formula and examples. "
    "Compare programmed I/O, interrupt-driven I/O, and DMA with diagrams. "
    "Explain IOP with channel program example and architecture diagram. "
    "Compare RISC and CISC in detail with pipeline diagram.",
)

pn.sp(10)
pn.rule(pn.get_theme().rl(pn.get_theme().accent), 1.0)
pn.sp(6)
pn.add(
    Paragraph(
        "Computer Architecture IT-404 Unit III -- Bharat Dangi  |  UIT-RGPV (Autonomous) Bhopal | Semester IV",
        pn.COVER_SUB,
    )
)

# =============================================================================
#  BUILD PDF
# =============================================================================
pn.build_doc(
    "CA_Unit3_Notes.pdf",
    title="Computer Architecture - Unit III Notes",
    author="Bharat Dangi",
)
print("Generated: CA_Unit3_Notes.pdf")
