"""
Computer Architecture (IT-404) -- Unit V Notes
UIT-RGPV (Autonomous) Bhopal | Semester IV
Complete exam notes with vector diagrams.
Run: python ca_unit5_notes.py
Output: CA_Unit5_Notes.pdf
"""

from __future__ import annotations

import engrapha_notes as en
import engrapha_diagrams as ed
from reportlab.platypus import Paragraph, Table, TableStyle
from engrapha_diagrams import ResponsiveDrawingFlowable

# =============================================================================
#  THEME SETUP
# =============================================================================
en.set_story([])
en.set_theme(en.MIDNIGHT_DARK)

diag_theme = ed.DiagramTheme.from_notes_theme(en.get_theme())

# =============================================================================
#  COVER PAGE
# =============================================================================
en.bookmark("Cover Page")
en.suppress_footer(page_only=True)
en.sp(12)
t = Table(
    [
        [Paragraph("COMPUTER ARCHITECTURE", en.COVER_H1)],
        [Paragraph("Unit V -- Complete Exam Notes", en.COVER_H2)],
    ],
    colWidths=[en.CW],
)
t.setStyle(
    TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, -1), en.get_theme().rl(en.get_theme().surface)),
            ("TOPPADDING", (0, 0), (-1, -1), 12),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
            ("LEFTPADDING", (0, 0), (-1, -1), 20),
            ("RIGHTPADDING", (0, 0), (-1, -1), 20),
            ("BOX", (0, 0), (-1, -1), 2.5, en.get_theme().rl(en.get_theme().accent)),
        ]
    )
)
en.add(t)
en.sp(8)
en.add(
    Paragraph(
        "Prepared by: Bharat Dangi  |  Subject Code: IT-404  |  UIT-RGPV (Autonomous) Bhopal",
        en.COVER_SUB,
    )
)
en.add(Paragraph("Semester IV  |  Based on University Syllabus 2024-25", en.COVER_SUB))
en.sp(4)
en.rule(en.get_theme().rl(en.get_theme().accent), 1.5)
en.sp(4)

en.info_table(
    ["Topic", "Coverage"],
    [
        [
            "5.1 Parallel Processing Overview",
            "Definition, motivation, Flynn's classification (SISD, SIMD, MISD, MIMD)",
        ],
        [
            "5.2 Pipelining -- General Concepts",
            "Pipeline structure, space-time diagram, clock cycle, pipeline registers",
        ],
        [
            "5.3 Pipeline Performance",
            "Speedup factor, efficiency, throughput, worked examples",
        ],
        [
            "5.4 Pipeline Hazards",
            "Structural, data, and control hazards; solutions and stalls",
        ],
        [
            "5.5 Arithmetic Pipeline",
            "Floating-point add/sub pipeline, 4-segment example, numerical worked examples",
        ],
        [
            "5.6 Instruction Pipeline",
            "Four-segment instruction pipeline (FI, DA, FO, EX), branch effects",
        ],
        [
            "5.7 Vector Processing",
            "Vector registers, SIMD, memory-to-memory vs register-to-register",
        ],
        [
            "5.8 Matrix Multiplication",
            "Inner product, pipeline execution of matrix multiply",
        ],
        [
            "5.9 Memory Interleaving",
            "Module organization, interleaved access, effective memory cycle time",
        ],
        [
            "5.10 Array Processors",
            "Attached array processor, SIMD array processor, masking, PE organization",
        ],
        [
            "5.11 Multiprocessors",
            "Definition, characteristics, tightly vs loosely coupled, MIMD",
        ],
        ["5.12 Quick Revision Summary", "Key formulas, tables, and exam flashcards"],
    ],
)
en.br()
en.suppress_footer(page_only=True)
en.toc()

# =============================================================================
#  UNIT DIVIDER
# =============================================================================
en.footer(
    left="IT-404: Computer Architecture", right="Unit V Notes", show_page_num=True
)
en.part_box("UNIT V -- PARALLEL PROCESSING")

# =============================================================================
#  5.1  PARALLEL PROCESSING OVERVIEW
# =============================================================================
en.chap_box("5.1  Parallel Processing Overview")
en.section("What is Parallel Processing?")
en.definition(
    "<b>Parallel Processing:</b> A large class of techniques used to provide simultaneous "
    "data-processing tasks for the purpose of increasing the computational speed of a "
    "computer system. Instead of processing each instruction sequentially (as in a "
    "conventional computer), a parallel processing system performs concurrent data "
    "processing to achieve faster execution time. The key metric improved is "
    "<b>throughput</b> -- the amount of processing accomplished during a given time interval."
)
en.body("Three classic forms of parallelism found in modern computers:")
en.bullet(
    [
        "<b>Instruction-level parallelism:</b> While an instruction is being executed in the ALU, the next instruction is fetched from memory (pipeline overlap).",
        "<b>Functional-unit parallelism:</b> The system has two or more ALUs and executes two or more instructions simultaneously.",
        "<b>Processor-level parallelism:</b> Two or more processors operate concurrently, each running independent instruction streams.",
    ]
)

en.section("Flynn's Classification")
en.definition(
    "<b>Flynn's Classification (1966):</b> A taxonomy introduced by M. J. Flynn that "
    "categorizes computer organizations by the number of simultaneous <b>instruction streams</b> "
    "and <b>data streams</b>. An <b>instruction stream</b> is the sequence of instructions "
    "read from memory. A <b>data stream</b> is the sequence of data operated upon in the processor."
)

en.info_table(
    ["Class", "Full Name", "Description", "Examples"],
    [
        [
            "SISD",
            "Single Instruction,\nSingle Data",
            "One control unit, one processor, one memory. Instructions executed sequentially. "
            "May have internal pipeline parallelism.",
            "Traditional von Neumann computers, early CPUs",
        ],
        [
            "SIMD",
            "Single Instruction,\nMultiple Data",
            "One control unit broadcasts the same instruction to multiple processing units, "
            "each operating on different data simultaneously. Shared multimodule memory.",
            "GPU, vector computers, array processors, MMX/SSE/AVX extensions",
        ],
        [
            "MISD",
            "Multiple Instruction,\nSingle Data",
            "Multiple processors execute different instructions on the same data stream. "
            "Theoretical only -- no practical system uses this organization.",
            "No practical implementation (theoretical interest only)",
        ],
        [
            "MIMD",
            "Multiple Instruction,\nMultiple Data",
            "Multiple processors each fetch their own instruction stream and operate "
            "on their own data stream. Processors may interact via shared memory or network.",
            "Multiprocessors, multicomputers, modern multi-core CPUs, clusters",
        ],
    ],
)

# Flynn's classification network diagram
net_flynn = ed.NetworkDiagram(
    width=650,
    height=280,
    theme=diag_theme,
    caption="Fig 1: Flynn's Classification -- four organizations of parallel computer systems",
)
net_flynn.node("flynn", "Flynn's\nClassification", x=285, y=230, kind="generic")
net_flynn.node("sisd", "SISD\n1 IS, 1 DS\n(Von Neumann)", x=60, y=130, kind="host")
net_flynn.node("simd", "SIMD\n1 IS, N DS\n(Vector/Array)", x=210, y=130, kind="server")
net_flynn.node("misd", "MISD\nN IS, 1 DS\n(Theoretical)", x=360, y=130, kind="generic")
net_flynn.node(
    "mimd", "MIMD\nN IS, N DS\n(Multiprocessor)", x=510, y=130, kind="server"
)

net_flynn.node(
    "sisd_ex",
    "Sequential CPU\nPipeline inside",
    x=60,
    y=40,
    kind="database",
    label_pos="right",
)
net_flynn.node(
    "simd_ex",
    "GPU / SSE\nArray Processor",
    x=210,
    y=40,
    kind="database",
    label_pos="right",
)
net_flynn.node(
    "misd_ex", "No real\nexample", x=360, y=40, kind="storage", label_pos="right"
)
net_flynn.node(
    "mimd_ex",
    "Multi-core\nMulticomputer",
    x=510,
    y=40,
    kind="database",
    label_pos="right",
)

net_flynn.link("flynn", "sisd")
net_flynn.link("flynn", "simd")
net_flynn.link("flynn", "misd")
net_flynn.link("flynn", "mimd")
net_flynn.link("sisd", "sisd_ex", label="e.g.")
net_flynn.link("simd", "simd_ex", label="e.g.")
net_flynn.link("misd", "misd_ex", label="e.g.")
net_flynn.link("mimd", "mimd_ex", label="e.g.")
en.story.extend(net_flynn.as_flowable())

en.tip(
    "Flynn's classification: IS = Instruction Stream, DS = Data Stream. "
    "SISD = sequential (traditional). SIMD = vector/GPU. MISD = theoretical only. "
    "MIMD = multiprocessor (most powerful, most common today). "
    "Modern multi-core processors are MIMD at the core level."
)
en.br()

# =============================================================================
#  5.2  PIPELINING -- GENERAL CONCEPTS
# =============================================================================
en.chap_box("5.2  Pipelining -- General Concepts")
en.section("What is Pipelining?")
en.definition(
    "<b>Pipelining:</b> A technique of decomposing a sequential process into "
    "sub-operations (stages), with each sub-process being executed in a special "
    "dedicated segment that operates concurrently with all other segments. A pipeline "
    "is analogous to an industrial assembly line: multiple tasks are in progress "
    "simultaneously, each at a different stage of completion. The overlapping of "
    "computation is made possible by associating a <b>pipeline register</b> with "
    "each segment, which holds intermediate results and provides isolation between stages."
)
en.body("The general structure of a pipeline consists of:")
en.bullet(
    [
        "<b>Combinational segments (S1, S2, ..., Sk):</b> Each performs a sub-operation on the data passing through.",
        "<b>Inter-stage registers (R1, R2, ..., Rk-1):</b> Latch the output of one stage and feed the next. Clocked simultaneously.",
        "<b>Common clock:</b> All registers are triggered by the same clock. Data moves one stage forward per clock cycle.",
    ]
)

# 4-segment pipeline structure
pipe_stack = ed.LayeredStack(
    width=en.CW,
    height=200,
    theme=diag_theme,
    caption="Fig 2: General structure of a 4-segment pipeline with inter-stage registers",
)
pipe_stack.layer("Input", sublabel="Task enters the pipeline here")
pipe_stack.layer(
    "Segment S1  -->  Register R1",
    sublabel="Sub-operation 1: result latched in R1 each clock cycle",
)
pipe_stack.layer(
    "Segment S2  -->  Register R2",
    sublabel="Sub-operation 2: result latched in R2 each clock cycle",
)
pipe_stack.layer(
    "Segment S3  -->  Register R3",
    sublabel="Sub-operation 3: result latched in R3 each clock cycle",
)
pipe_stack.layer(
    "Segment S4  -->  Output",
    sublabel="Sub-operation 4: final result produced every clock cycle once full",
)
en.story.extend(pipe_stack.as_flowable())

en.section("Space-Time Diagram")
en.definition(
    "<b>Space-Time Diagram:</b> A diagram that shows the segment utilization as a "
    "function of time. The horizontal axis represents time in clock cycles and the "
    "vertical axis gives the segment number. It is used to visualize pipeline "
    "behavior and identify when the pipe is full and producing one result per cycle."
)
en.code_block("""
 SPACE-TIME DIAGRAM -- 4-SEGMENT PIPELINE, 6 TASKS (T1 to T6):
 ======================================================
 Segment | Clk1 | Clk2 | Clk3 | Clk4 | Clk5 | Clk6 | Clk7 | Clk8 | Clk9
 --------|------|------|------|------|------|------|------|------|------
    S1   |  T1  |  T2  |  T3  |  T4  |  T5  |  T6  |      |      |
    S2   |      |  T1  |  T2  |  T3  |  T4  |  T5  |  T6  |      |
    S3   |      |      |  T1  |  T2  |  T3  |  T4  |  T5  |  T6  |
    S4   |      |      |      |  T1  |  T2  |  T3  |  T4  |  T5  |  T6

 Observation:
   - Cycles 1-3: Pipeline filling up (not all segments busy).
   - Cycle 4 onward: Pipeline is FULL -- one task completes per cycle.
   - Total clock cycles = k + (n - 1) = 4 + (6 - 1) = 9 cycles.
   - Once full: one output every clock cycle, regardless of number of stages.
""")

en.section("Clock Cycle Determination")
en.definition(
    "<b>Clock Cycle (Tp):</b> The time period of the pipeline clock. It must be long "
    "enough for the slowest segment to complete its computation PLUS the inter-stage "
    "register delay. Let <b>tm</b> = maximum stage delay (slowest segment), "
    "<b>d</b> = inter-stage register delay. Then:"
)
en.code_block("""
 CLOCK CYCLE FORMULA:
 ======================================================
 Tp = tm + d

 Where:
   tm = maximum stage delay (slowest pipeline segment)
   d  = inter-stage register (latch) delay

 In practice: tm >> d, so Tp ≈ tm

 EXAMPLE:
   Stage delays: t1=60ns, t2=70ns, t3=100ns, t4=80ns
   Inter-stage delay: d = 10ns
   Tp = max(60, 70, 100, 80) + 10 = 100 + 10 = 110 ns
   The clock cycle is dominated by the SLOWEST segment (S3 = 100ns).

 KEY INSIGHT:
   To improve pipeline speed, split the slowest segment into two shorter segments.
   This adds one more stage but reduces Tp.
""")

en.tip(
    "Pipeline clock = slowest stage delay + register overhead. "
    "Once pipeline is full: 1 result per clock cycle. "
    "Total cycles for n tasks in k-stage pipeline = k + (n - 1). "
    "Split the bottleneck segment to reduce clock period and boost throughput."
)
en.br()

# =============================================================================
#  5.3  PIPELINE PERFORMANCE
# =============================================================================
en.chap_box("5.3  Pipeline Performance -- Speedup, Efficiency, Throughput")
en.section("Performance Formulas")
en.code_block("""
 PIPELINE PERFORMANCE FORMULAS:
 ======================================================
 Notation:
   k  = number of pipeline stages
   n  = number of tasks to execute
   Tp = pipeline clock cycle time
   Tn = time to execute one task without pipeline (non-pipelined time)

 TOTAL PIPELINE TIME:
   Tk = [k + (n - 1)] * Tp

 NON-PIPELINED TIME (for n tasks):
   T_nonpipe = n * Tn

 SPEEDUP FACTOR (Sk):
   Sk = (n * Tn) / ([k + (n - 1)] * Tp)

 MAXIMUM SPEEDUP (as n -> infinity):
   As n >> k:  k + (n-1) approaches n, so:
   Sk_max = Tn / Tp
   If Tn = k * Tp (ideal case, each stage equally divides the task):
   Sk_max = k   (speedup equals number of stages)

 EFFICIENCY (Ek):
   Ek = Sk / k
   (Fraction of time each stage is usefully occupied)

 THROUGHPUT:
   Throughput = n / Tk = n / ([k + (n-1)] * Tp)  [tasks per unit time]
""")

en.section("Worked Example 1 (Standard)")
en.code_block("""
 EXAMPLE 1:
 ======================================================
 Given: Non-pipelined time Tn = 100 ns
        Pipeline stages k = 6
        Pipeline clock Tp = 20 ns
        Number of tasks n = 200

 i) Speedup ratio:
    Sk = (n * Tn) / ([k + (n-1)] * Tp)
       = (200 * 100) / ([6 + 199] * 20)
       = 20000 / (205 * 20)
       = 20000 / 4100
       = 4.878

 ii) Maximum speedup:
    Sk_max = k = 6   (theoretical upper limit)

 iii) Efficiency:
    Ek = Sk / k = 4.878 / 6 = 0.813 = 81.3%

 iv) Throughput:
    Tk = [6 + 199] * 20 = 205 * 20 = 4100 ns
    Throughput = 200 / 4100 = 0.04878 tasks/ns
               = 48.78 million tasks/second
""")

en.section("Worked Example 2 (Segment Splitting)")
en.code_block("""
 EXAMPLE 2 (Arithmetic Pipeline Segment Splitting):
 ======================================================
 Given:  Stage delays: t1=50ns, t2=30ns, t3=95ns, t4=45ns
         Inter-stage register delay: tr = 5 ns
         Number of tasks n = 100

 PART (a): Original 4-segment pipeline
   Tp = max(50, 30, 95, 45) + 5 = 95 + 5 = 100 ns
   Total time = [4 + (100-1)] * 100 = [4 + 99] * 100 = 103 * 100 = 10300 ns
   Tn = 50 + 30 + 95 + 45 + 5 = 225 ns (non-pipeline sequential time)
   Speedup = (100 * 225) / 10300 = 22500 / 10300 = 2.18

 PART (b): Split segment 3 (95ns) into two segments (50ns + 45ns)
           New pipeline has 5 segments
   Tp = max(50, 30, 50, 45, 45) + 5 = 50 + 5 = 55 ns
   Total time = [5 + (100-1)] * 55 = [5 + 99] * 55 = 104 * 55 = 5720 ns
   (About half of original -- improvement by splitting bottleneck!)
   Tn = 50 + 30 + 50 + 45 + 45 + 5 = 225 ns (unchanged)
   Speedup = (100 * 225) / 5720 = 22500 / 5720 = 3.93

 KEY OBSERVATION:
   By splitting the slowest segment from 95ns into two stages of 50ns and 45ns,
   we reduced Tp from 100ns to 55ns, nearly doubling the speedup (2.18 -> 3.93).
""")

en.section("Space-Time Diagram -- 6-Stage Pipeline, 8 Tasks")
en.code_block("""
 SPACE-TIME DIAGRAM -- 6-SEGMENT PIPELINE, 8 TASKS (T1 to T8):
 ======================================================
 k=6, n=8
 Total clock cycles = k + (n-1) = 6 + 7 = 13 clock cycles

 Seg | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | C9 | C10| C11| C12| C13
 ----|----|----|----|----|----|----|----|----|----|----|----|----|----
  S1 | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 |    |    |    |    |
  S2 |    | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 |    |    |    |
  S3 |    |    | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 |    |    |
  S4 |    |    |    | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 |    |
  S5 |    |    |    |    | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 |
  S6 |    |    |    |    |    | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8

 First output (T1) appears at end of cycle 6.
 After that: one output per cycle (T2 at C7, T3 at C8, ..., T8 at C13).
""")

en.tip(
    "Speedup = (n * Tn) / ([k + n - 1] * Tp). Maximum speedup = k (number of stages). "
    "Efficiency = Speedup / k. Throughput = n / total_time. "
    "Split bottleneck stages to reduce clock period. "
    "Total cycles = k + n - 1 (k to fill, then 1 per task)."
)
en.br()

# =============================================================================
#  5.4  PIPELINE HAZARDS
# =============================================================================
en.chap_box("5.4  Pipeline Hazards")
en.section("What is a Pipeline Hazard?")
en.definition(
    "<b>Pipeline Hazard (Conflict):</b> A situation that prevents an instruction "
    "from executing during its designated clock cycle in the pipeline. Hazards reduce "
    "pipeline performance by causing <b>stalls</b> (also called bubbles) -- idle cycles "
    "where a stage cannot proceed and must wait. There are three major categories."
)

en.info_table(
    ["Hazard Type", "Cause", "Example", "Solutions"],
    [
        [
            "Structural Hazard\n(Resource Conflict)",
            "Two pipeline stages need the same hardware resource at the same time.",
            "Single shared memory: instruction fetch (IF) and data memory access (MEM) "
            "both need the memory in the same cycle.",
            "1. Duplicate resources (separate instruction and data memory -- Harvard architecture). "
            "2. Stall the pipeline (insert bubble).",
        ],
        [
            "Data Hazard\n(Data Dependency)",
            "An instruction needs the result of a previous instruction that has not yet "
            "written back its result.",
            "ADD R1, R2, R3 followed immediately by SUB R4, R1, R5. "
            "SUB needs R1 before ADD has written it.",
            "1. Pipeline stall (insert NOP bubbles until data is ready). "
            "2. Operand forwarding / bypassing (feed ALU output directly back to ALU input). "
            "3. Compiler scheduling (reorder instructions to avoid dependency).",
        ],
        [
            "Control Hazard\n(Branch Hazard)",
            "A branch instruction changes the PC; the pipeline has already fetched "
            "and partially executed instructions that should not run.",
            "BEQ instruction: pipeline fetched next 3 sequential instructions while "
            "branch target is being computed.",
            "1. Pipeline stall (flush wrongly fetched instructions). "
            "2. Branch prediction (guess taken/not-taken; flush on misprediction). "
            "3. Delayed branching (execute instruction(s) after branch regardless -- branch delay slot). "
            "4. Branch target buffer (cache recent branch targets).",
        ],
    ],
)

en.section("Structural Hazard -- Von Neumann vs Harvard Architecture")
en.body(
    "A Von Neumann computer has a <b>single memory</b> for both instructions and data. "
    "A pipelined von Neumann processor suffers from structural hazard because the IF "
    "stage and the MEM stage cannot both access memory in the same cycle. "
    "The <b>Harvard architecture</b> resolves this by providing <b>separate instruction "
    "memory and data memory</b> with separate buses, allowing simultaneous access."
)

left_vn = ed.LayeredStack(
    width=en.CW * 0.44,
    height=180,
    theme=diag_theme,
    caption="Von Neumann: Single Memory (Structural Hazard Risk)",
)
left_vn.layer("CPU (IF + MEM share one bus)", sublabel="IF and MEM compete for access")
left_vn.layer("Single Memory Bus", sublabel="Only one access per cycle")
left_vn.layer(
    "Unified Memory (Instructions + Data)", sublabel="All data in one address space"
)

right_ha = ed.LayeredStack(
    width=en.CW * 0.44,
    height=180,
    theme=diag_theme,
    caption="Harvard: Separate Memories (No Structural Hazard)",
)
right_ha.layer(
    "CPU (IF and MEM independent)", sublabel="Simultaneous access to both memories"
)
right_ha.layer("Instruction Bus | Data Bus", sublabel="Two independent buses")
right_ha.layer(
    "Instruction Memory | Data Memory", sublabel="Physically separate -- no conflict"
)

left_vn.as_flowable()
right_ha.as_flowable()

tbl_arch = Table(
    [
        [
            ResponsiveDrawingFlowable(left_vn.drawing),
            ResponsiveDrawingFlowable(right_ha.drawing),
        ]
    ],
    colWidths=[en.CW * 0.48, en.CW * 0.48],
)
tbl_arch.setStyle(
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
en.add(tbl_arch)
en.sp(6)
en.add(
    Paragraph(
        "Fig 3 (left): Von Neumann -- shared memory causes structural hazard.  |  "
        "Fig 3 (right): Harvard -- separate memories eliminate structural hazard.",
        en.COVER_SUB,
    )
)
en.sp(8)

en.section("Data Hazard -- Operand Forwarding")
en.body(
    "The simplest solution to a data hazard is to <b>stall the pipeline</b> by inserting "
    "NOP (no-operation) bubbles until the required data is available. A faster solution is "
    "<b>operand forwarding (bypassing)</b>: the ALU result is fed directly back to the ALU "
    "input through a multiplexer, bypassing the register file write-back. This avoids stalls "
    "in most cases and requires only extra multiplexers and forwarding detection logic."
)
en.code_block("""
 DATA HAZARD EXAMPLE AND SOLUTIONS:
 ======================================================
 Code sequence:
   I1: ADD R1, R2, R3   ; R1 <- R2 + R3  (writes R1 in WB stage, cycle 5)
   I2: SUB R4, R1, R5   ; R4 <- R1 - R5  (needs R1 in EX stage, cycle 4 -- too early!)
   I3: AND R6, R1, R7   ; R6 <- R1 AND R7 (needs R1 in EX stage, cycle 5 -- just in time)

 WITHOUT FORWARDING (stall approach):
   Cycle: 1    2    3    4    5    6    7    8
   I1:    IF   ID   EX   MEM  WB
   I2:    -    IF   ID  stall stall EX  MEM  WB    (2 stall cycles inserted)
   I3:    -    -    IF  stall stall ID  EX   MEM

 WITH FORWARDING (bypass approach):
   Cycle: 1    2    3    4    5    6    7
   I1:    IF   ID   EX   MEM  WB
   I2:    -    IF   ID   EX*  MEM  WB       (* R1 forwarded from I1's EX output)
   I3:    -    -    IF   ID   EX   MEM  WB  (* R1 forwarded from I1's MEM/WB)
   No stalls needed! Forwarding logic detects dependency and routes data.
""")

en.section("Control Hazard -- Branch Handling")
en.code_block("""
 CONTROL HAZARD EXAMPLE:
 ======================================================
 Instruction pipeline (4 stages: IF, ID, EX, WB):
   Cycle:  1    2    3    4    5    6
   BEQ:    IF   ID   EX   WB
   I+1:    -    IF   ID  FLUSH  (wrongly fetched -- branch taken!)
   I+2:    -    -    IF  FLUSH  (wrongly fetched -- flushed!)
   Target: -    -    -    IF    EX   WB  (correct instruction now fetched)

 SOLUTIONS TO CONTROL HAZARD:
 1. STALL: Insert bubbles after branch until target is known.
           Simple but wastes cycles. If branch resolved in ID: 1 cycle wasted.
           If resolved in EX: 2 cycles wasted per branch.

 2. BRANCH PREDICTION:
    Static: always predict not-taken (continue sequential fetch).
            If wrong: flush fetched instructions and restart from target.
    Dynamic: use Branch History Table (BHT) or Branch Target Buffer (BTB).
             Track recent branch outcomes and predict accordingly.
             Modern processors achieve 95%+ prediction accuracy.

 3. DELAYED BRANCHING (RISC technique):
    Instructions immediately after branch (delay slots) are ALWAYS executed.
    Compiler fills delay slots with useful instructions.
    If no useful instruction: fill with NOP.
    Used in MIPS architecture (1 delay slot).
""")

en.tip(
    "Three hazard types: Structural (resource conflict), Data (dependency), Control (branch). "
    "Structural: fix with Harvard architecture (separate I-cache and D-cache). "
    "Data: fix with forwarding/bypassing (no stall) or stall insertion. "
    "Control: fix with branch prediction, delayed branching, or stall+flush."
)
en.br()

# =============================================================================
#  5.5  ARITHMETIC PIPELINE
# =============================================================================
en.chap_box("5.5  Arithmetic Pipeline")
en.section("Overview")
en.definition(
    "<b>Arithmetic Pipeline:</b> A pipeline unit designed to perform arithmetic "
    "operations (typically floating-point) by decomposing the computation into "
    "sequential sub-operations executed in dedicated pipeline stages. Arithmetic "
    "pipelines are found in high-speed scientific computers and are used for "
    "floating-point operations, fixed-point multiplication, and similar "
    "computationally intensive tasks. They are a form of <b>data stream pipelining</b> "
    "(as opposed to instruction stream pipelining)."
)

en.section("Floating-Point Adder/Subtractor Pipeline (4 Segments)")
en.body(
    "Floating-point addition and subtraction can be decomposed into four natural sub-operations, "
    "each implemented as one pipeline stage. Given two normalized floating-point numbers:<br/>"
    "<b>X = A x 2<super>a</super></b> and <b>Y = B x 2<super>b</super></b> where A, B are mantissas "
    "and a, b are exponents, the four pipeline stages are:"
)

en.info_table(
    ["Stage", "Segment", "Operation", "Details"],
    [
        [
            "S1",
            "Exponent Compare",
            "Subtract exponents: a - b",
            "Determine which number has the larger exponent. Choose the larger exponent as the result exponent.",
        ],
        [
            "S2",
            "Mantissa Align",
            "Shift mantissa of smaller-exponent number right",
            "Shift right by |a - b| positions so both mantissas have the same exponent. "
            "Shift must be a combinational circuit to minimize delay.",
        ],
        [
            "S3",
            "Mantissa Add/Sub",
            "Add or subtract the aligned mantissas",
            "Perform the arithmetic on the now-aligned mantissas to get the raw result.",
        ],
        [
            "S4",
            "Normalize Result",
            "Shift result to normalized form",
            "Shift mantissa left until the form is 1.XXXX (non-zero leading digit). "
            "Adjust exponent accordingly (increment or decrement).",
        ],
    ],
)

# Floating-point pipeline diagram
net_fp = ed.NetworkDiagram(
    width=800,
    height=200,
    theme=diag_theme,
    caption="Fig 4: 4-segment floating-point adder/subtractor pipeline with inter-stage registers",
)
net_fp.node("in", "X, Y Inputs\n(Normalized FP)", x=40, y=100, kind="generic")
net_fp.node("s1", "S1\nCompare\nExponents", x=130, y=100, kind="server")
net_fp.node("r1", "R1", x=220, y=100, kind="storage")
net_fp.node("s2", "S2\nAlign\nMantissas", x=310, y=100, kind="server")
net_fp.node("r2", "R2", x=400, y=100, kind="storage")
net_fp.node("s3", "S3\nAdd / Sub\nMantissas", x=490, y=100, kind="server")
net_fp.node("r3", "R3", x=580, y=100, kind="storage")
net_fp.node("s4", "S4\nNormalize\nResult", x=670, y=100, kind="server")
net_fp.node("out", "Z Output\n(Normalized FP)", x=760, y=100, kind="generic")

net_fp.link("in", "s1", bidirectional=False)
net_fp.link("s1", "r1", bidirectional=False)
net_fp.link("r1", "s2", bidirectional=False)
net_fp.link("s2", "r2", bidirectional=False)
net_fp.link("r2", "s3", bidirectional=False)
net_fp.link("s3", "r3", bidirectional=False)
net_fp.link("r3", "s4", bidirectional=False)
net_fp.link("s4", "out", bidirectional=False)
en.story.extend(net_fp.as_flowable())

en.section("Numerical Example -- FP Addition Pipeline")
en.code_block("""
 FLOATING-POINT PIPELINE NUMERICAL EXAMPLE:
 ======================================================
 Inputs (decimal for clarity):
   X = 0.9504 x 10^3
   Y = 0.8200 x 10^2

 SEGMENT S1 (Compare Exponents):
   Difference = 3 - 2 = 1
   Larger exponent = 3 (result exponent = 3)

 SEGMENT S2 (Align Mantissas -- shift Y right by 1):
   X = 0.9504 x 10^3  (unchanged)
   Y = 0.0820 x 10^3  (mantissa shifted right by 1, exponent adjusted to 3)

 SEGMENT S3 (Add Mantissas):
   Z = 0.9504 + 0.0820 = 1.0324 x 10^3
   (Raw sum -- mantissa overflows past 1.0, needs normalization)

 SEGMENT S4 (Normalize Result):
   Shift mantissa right by 1, increment exponent by 1:
   Z = 0.10324 x 10^4  (normalized)

 RESULT: Z = 0.10324 x 10^4 = 1032.4  (correct: 950.4 + 82.0 = 1032.4)

 PIPELINE CLOCK CALCULATION (binary pipeline):
   t1=60ns, t2=70ns, t3=100ns, t4=80ns, tr=10ns (register delay)
   Tp = max(60, 70, 100, 80) + 10 = 100 + 10 = 110 ns
   Non-pipeline sequential time: Tn = 60 + 70 + 100 + 80 + 10 = 320 ns
   Speedup (for large n): Tn / Tp = 320 / 110 = 2.91
""")

en.section("FP Pipeline Worked Example -- Total Time and Speedup")
en.code_block("""
 EXAMPLE: t1=50ns, t2=30ns, t3=95ns, t4=45ns, tr=5ns, n=100 pairs

 PART (a): 4-segment pipeline
   Tp = max(50, 30, 95, 45) + 5 = 95 + 5 = 100 ns
   Total time = [4 + (100 - 1)] * 100 = 103 * 100 = 10300 ns = 10.3 us
   Tn = 50 + 30 + 95 + 45 + 5 = 225 ns
   Speedup = (100 * 225) / 10300 = 22500 / 10300 = 2.18

 PART (b): Split S3 (95ns) into two segments (50ns + 45ns)
           New pipeline: k=5, stages = 50, 30, 50, 45, 45 ns
   Tp = max(50, 30, 50, 45, 45) + 5 = 50 + 5 = 55 ns
   Total time = [5 + (100 - 1)] * 55 = 104 * 55 = 5720 ns (about half!)
   Tn = 50 + 30 + 50 + 45 + 45 + 5 = 225 ns
   Speedup = (100 * 225) / 5720 = 22500 / 5720 = 3.93

 CONCLUSION: Splitting the bottleneck segment (S3) increased speedup from 2.18 to 3.93.
             The cost is one additional pipeline register and slightly more complex control.
""")

en.tip(
    "FP pipeline stages: (1) Compare exponents, (2) Align mantissas, "
    "(3) Add/subtract mantissas, (4) Normalize result. "
    "Clock = slowest stage + register delay. "
    "Split bottleneck stages to reduce clock period. "
    "Non-pipeline time Tn = sum of all stage delays."
)
en.br()

# =============================================================================
#  5.6  INSTRUCTION PIPELINE
# =============================================================================
en.chap_box("5.6  Instruction Pipeline")
en.section("Overview")
en.definition(
    "<b>Instruction Pipeline:</b> A pipeline that processes the instruction stream "
    "itself (rather than data). Consecutive instructions are read from memory while "
    "previous instructions are being executed in other segments. This causes the "
    "instruction fetch and execute phases to overlap. The general steps for processing "
    "an instruction are: (1) Fetch, (2) Decode + EA calculation, (3) Fetch operand, "
    "(4) Execute, (5) Store result."
)

en.section("Four-Segment Instruction Pipeline")
en.body(
    "By combining decode with effective address calculation (segment 2) and combining "
    "execution with result storage (segment 4), the instruction cycle reduces to "
    "four natural pipeline stages:"
)
en.info_table(
    ["Stage", "Abbreviation", "Operation", "Details"],
    [
        [
            "FI",
            "Fetch Instruction",
            "Read next instruction from memory into FIFO buffer",
            "Uses a FIFO instruction queue. When execution unit is not using memory, "
            "control increments PC and fetches consecutive instructions proactively.",
        ],
        [
            "DA",
            "Decode + Address",
            "Decode opcode and calculate effective address",
            "Determine the addressing mode and compute the EA of the operand. "
            "Combined into one stage to save pipeline stages.",
        ],
        [
            "FO",
            "Fetch Operand",
            "Read operand from memory at the effective address",
            "For register operands, no memory access needed (register read is fast). "
            "Separate data memory or bus prevents conflict with FI stage.",
        ],
        [
            "EX",
            "Execute",
            "Perform ALU operation and store result",
            "Execute the decoded operation on the fetched operand. "
            "Write result to destination register or memory.",
        ],
    ],
)

en.code_block("""
 FOUR-SEGMENT INSTRUCTION PIPELINE SPACE-TIME DIAGRAM:
 ======================================================
 Assumption: Separate instruction and data memories (Harvard-style).
             FI and FO can proceed simultaneously without memory conflict.

 Cycle:  1    2    3    4    5    6    7
  FI   | I1 | I2 | I3 | I4 | I5 | I6 | I7 |
  DA   |    | I1 | I2 | I3 | I4 | I5 | I6 |
  FO   |    |    | I1 | I2 | I3 | I4 | I5 |
  EX   |    |    |    | I1 | I2 | I3 | I4 |

 At cycle 4:
   EX is executing instruction I1.
   FO is fetching operand for instruction I2.
   DA is decoding instruction I3 and calculating its EA.
   FI is fetching instruction I4 from memory.
   FOUR instructions are in progress simultaneously!

 BRANCH INSTRUCTION EFFECT:
   If I3 is a branch (taken):
   - Complete I1 (EX) and I2 (FO) -- they are already in progress.
   - FLUSH the instruction buffer (delete I4, I5, I6, ... from FIFO).
   - Restart pipeline from new branch target address.
   - Pipeline penalty = 2 cycles (wasted I2's DA and I3's decode).
   Same penalty applies when an interrupt is acknowledged.
""")

# 4-segment instruction pipeline flowchart
fc_ipipe = ed.Flowchart(
    width=en.CW,
    height=600,
    theme=diag_theme,
    caption="Fig 5: Four-segment instruction pipeline operation and branch handling",
)
fc_ipipe.terminal("start", "BEGIN: PC points to first instruction", x=240, y=560)
fc_ipipe.process(
    "fi", "FI: Fetch instruction from memory into FIFO; PC <- PC + 1", x=240, y=500
)
fc_ipipe.process(
    "da", "DA: Decode opcode; calculate Effective Address (EA)", x=240, y=430
)
fc_ipipe.process(
    "fo", "FO: Fetch operand from M[EA] (if memory operand needed)", x=240, y=360
)
fc_ipipe.process(
    "ex", "EX: Execute operation; write result to destination", x=240, y=290
)
fc_ipipe.decision("branch", "Is instruction a branch or interrupt?", x=240, y=210)
fc_ipipe.process(
    "flush", "FLUSH instruction FIFO buffer; discard all pending fetches", x=240, y=140
)
fc_ipipe.process("newpc", "Load PC with branch target address", x=240, y=80)
fc_ipipe.terminal("done", "Continue pipeline from new PC", x=240, y=20)

fc_ipipe.edge("start", "fi")
fc_ipipe.edge("fi", "da")
fc_ipipe.edge("da", "fo")
fc_ipipe.edge("fo", "ex")
fc_ipipe.edge("ex", "branch")
fc_ipipe.edge("branch", "flush", branch="yes")
fc_ipipe.edge("branch", "fi", branch="no", orthogonal=True)
fc_ipipe.edge("flush", "newpc")
fc_ipipe.edge("newpc", "done")
en.story.extend(fc_ipipe.as_flowable())

en.tip(
    "Instruction pipeline: FI -> DA -> FO -> EX. Four stages, 4 instructions in progress. "
    "FIFO instruction buffer smooths memory fetch. "
    "Branch/interrupt: flush buffer, restart from new address (branch penalty = pipeline depth - 1). "
    "Separate instruction and data memory prevents structural hazard between FI and FO."
)
en.br()

# =============================================================================
#  5.7  VECTOR PROCESSING
# =============================================================================
en.chap_box("5.7  Vector Processing")
en.section("What is Vector Processing?")
en.definition(
    "<b>Vector Processing:</b> An approach to high-performance computation that "
    "performs arithmetic operations on entire <b>arrays (vectors)</b> of integers or "
    "floating-point numbers simultaneously, avoiding the overhead of loop control "
    "mechanisms found in general-purpose scalar computers. Each element of a vector "
    "operand is a scalar quantity (integer, float, logical value, or character). "
    "This is a form of SIMD -- Single Instruction, Multiple Data."
)
en.body(
    "A general-purpose computer adds two arrays using a loop (one element at a time). "
    "A vector processor adds both arrays in a <b>single vector instruction</b>, "
    "operating on all elements in parallel. For this to work, the operations on "
    "different elements must be <b>independent</b> (no data dependency between elements)."
)

en.info_table(
    ["Property", "Scalar Processing", "Vector Processing"],
    [
        [
            "Operation unit",
            "One element at a time",
            "All elements simultaneously (or pipelined)",
        ],
        [
            "Loop overhead",
            "One loop iteration per element",
            "No loop -- single vector instruction",
        ],
        ["Instruction type", "Scalar (ADD R1, R2)", "Vector (VADD V1, V2, V3)"],
        [
            "Data source",
            "Registers or memory word",
            "Vector registers (hold multiple elements)",
        ],
        [
            "Best for",
            "General-purpose programs, control flow",
            "Numerical arrays, scientific computing, DSP",
        ],
        ["Examples", "Intel x86 scalar ALU", "Cray-1, GPU shader units, Intel AVX-512"],
    ],
)

en.section("Vector Instruction Types")
en.body(
    "Vector instructions fall into four classes based on operand type (V = vector, S = scalar) "
    "and number of operands:"
)
en.info_table(
    ["Type", "Example", "Operation", "Description"],
    [
        [
            "V op V -> V",
            "VADD V1, V2, V3",
            "V1[i] <- V2[i] + V3[i]",
            "Binary vector-vector operation (most common)",
        ],
        [
            "V op S -> V",
            "VSMUL V1, V2, S1",
            "V1[i] <- V2[i] * S1",
            "Scale a vector by a scalar value",
        ],
        [
            "op V -> V",
            "VNEG V1, V2",
            "V1[i] <- -V2[i]",
            "Unary operation on each element",
        ],
        [
            "op V -> S",
            "VSUM S1, V1",
            "S1 <- sum(V1[i])",
            "Reduction: collapse a vector to a scalar",
        ],
    ],
)

en.section("Vector Register Architecture")
en.body(
    "Vector processors use <b>vector registers</b> -- special-purpose registers that hold "
    "multiple data elements. The number of elements a vector register holds is the "
    "<b>vector length</b> (or <b>n</b>). Two architectural styles exist:"
)
en.info_table(
    ["Architecture", "Description", "Operand Source", "Examples"],
    [
        [
            "Register-to-Register\n(Load/Store)",
            "All vector operations performed on vector registers. "
            "Separate VLOAD and VSTORE instructions move data to/from memory.",
            "Vector registers (fast, no memory latency during compute)",
            "Cray-1, Fujitsu VP-200, Intel SSE/AVX",
        ],
        [
            "Memory-to-Memory",
            "Operands fetched directly from main memory for each instruction. "
            "Results written back to memory.",
            "Main memory (slower, higher bandwidth required)",
            "TI-ASC, CDC STAR-100, Cyber-205",
        ],
    ],
)

en.section("Pipelined Vector Processor")
en.body(
    "Most vector instructions are pipelined because they perform the same operation "
    "repeatedly on different data elements. The pipeline has a <b>start-up latency</b> "
    "(filling the pipe) but once full, produces one result per clock cycle. "
    "Longer vectors amortize the start-up delay over more elements, yielding better efficiency."
)
en.code_block("""
 VECTOR PIPELINE EXAMPLE: VADD V1, V2, V3  (n=8 elements, k=4 stage FP pipeline)
 ======================================================
 Stage: FP add pipeline has 4 stages (compare, align, add, normalize)

 Element | S1  | S2  | S3  | S4  (stage)
 --------|-----|-----|-----|-----
   e1    | C1  | C2  | C3  | C4  <- result at cycle 4
   e2    | C2  | C3  | C4  | C5  <- result at cycle 5
   e3    | C3  | C4  | C5  | C6
   e4    | C4  | C5  | C6  | C7
   e5    | C5  | C6  | C7  | C8
   e6    | C6  | C7  | C8  | C9
   e7    | C7  | C8  | C9  | C10
   e8    | C8  | C9  | C10 | C11  <- last result at cycle 11

 Total = k + (n - 1) = 4 + 7 = 11 cycles for all 8 elements.
 After start-up (first 4 cycles): 1 result per cycle.

 MASKING: Vector processors use a mask register (one bit per element).
          If mask bit i = 1: element i participates in the operation.
          If mask bit i = 0: element i is skipped (inactive PE).
          Used for conditional vector operations (e.g., only add positive elements).
""")

net_vpipe = ed.NetworkDiagram(
    width=en.CW,
    height=200,
    theme=diag_theme,
    caption="Fig 6: Pipelined vector processor -- vector register file feeds FP pipeline units",
)
net_vpipe.node("mem_l", "Memory Load\n(VLOAD Port)", x=50, y=160, kind="storage")
net_vpipe.node("mem_s", "Memory Store\n(VSTORE Port)", x=50, y=40, kind="storage")
net_vpipe.node(
    "vrf",
    "Vector Register File\n(V0 - V7, each holds n elements)",
    x=170,
    y=100,
    kind="database",
)
net_vpipe.node("fpadd", "FP Adder Pipeline\n(4 stages)", x=300, y=150, kind="server")
net_vpipe.node(
    "fpmul", "FP Multiplier Pipeline\n(4 stages)", x=300, y=50, kind="server"
)
net_vpipe.node("out", "Result Vector\n(back to VRF)", x=430, y=100, kind="database")

net_vpipe.link("mem_l", "vrf", label="VLOAD", bidirectional=False)
net_vpipe.link("vrf", "mem_s", label="VSTORE", bidirectional=False)
net_vpipe.link("vrf", "fpadd", label="Src 1\nSrc 2", bidirectional=False)
net_vpipe.link("vrf", "fpmul", label="Src 1\nSrc 2", bidirectional=False)
net_vpipe.link("fpadd", "out", label="Result", bidirectional=False)
net_vpipe.link("fpmul", "out", label="Result", bidirectional=False)
net_vpipe.link("out", "vrf", label="Write back", bidirectional=False)
en.story.extend(net_vpipe.as_flowable())

en.tip(
    "Vector processing: single instruction operates on all array elements. "
    "Vector register holds n elements (vector length). "
    "Register-to-register: operations on registers (fast). Memory-to-memory: slower. "
    "Masking: bit vector controls which elements participate. "
    "Pipelining within vector unit gives 1 result/cycle after startup."
)
en.br()

# =============================================================================
#  5.8  MATRIX MULTIPLICATION
# =============================================================================
en.chap_box("5.8  Matrix Multiplication")
en.section("Overview")
en.definition(
    "<b>Matrix Multiplication:</b> One of the most computationally intensive operations "
    "in scientific computing. Multiplying two n x n matrices requires n<super>3</super> "
    "multiply-add (linked multiply-accumulate) operations and produces n<super>2</super> "
    "inner products. It is an ideal workload for pipelined vector processors."
)

en.section("Mathematical Definition")
en.code_block("""
 MATRIX MULTIPLICATION: C = A x B  (3x3 example)

 A = | a11  a12  a13 |     B = | b11  b12  b13 |
     | a21  a22  a23 |         | b21  b22  b23 |
     | a31  a32  a33 |         | b31  b32  b33 |

 Each element of result matrix C is an INNER PRODUCT:
   C[i][j] = sum over k of (A[i][k] * B[k][j])

 Example: C[1][1] = a11*b11 + a12*b21 + a13*b31
          (3 multiplications + 3 additions = 3 multiply-add operations)

 For n x n matrices:
   Total multiply-add operations = n^2 * n = n^3
   3x3: 9 inner products * 3 multiply-adds each = 27 operations
   100x100: 100^2 * 100 = 1,000,000 operations
   1000x1000: 1,000,000,000 operations (1 billion!)
""")

en.section("Pipeline Execution of Matrix Multiplication")
en.body(
    "A pipelined vector processor executes matrix multiplication using linked FP multiply "
    "and FP add pipelines. Assume each pipeline has 4 stages. The pairs (Ai, Bi) are "
    "fed into the multiplier at one pair per cycle. The multiplier output feeds directly "
    "into the adder (chained pipelines), and the running sum is accumulated."
)
en.code_block("""
 PIPELINED MATRIX MULTIPLY (3x3, computing one row of C):
 ======================================================
 Computing C[1][j] for all j simultaneously using pipelined inner products.

 All segment registers initialized to 0.

 Cycle 1: Multiply A[1][1] * B[1][j] -> enters multiplier pipeline
 Cycle 2: Multiply A[1][2] * B[2][j] -> enters multiplier pipeline
 Cycle 3: Multiply A[1][3] * B[3][j] -> enters multiplier pipeline

 Cycles 1-8: Pipeline filling up (8 cycles for two 4-stage pipelines in series)
 Cycle 9: First multiply result exits, enters adder
 Cycle 10: Running sum accumulates
 ...
 Cycle 11: Final sum C[1][j] available

 PIPELINE ADVANTAGE:
   Sequential: 3 multiplications + 3 additions = 6 operations * delay = slow
   Pipelined: all 3 pairs fed in 3 cycles, result in 3 + (4+4-1) cycles
   For large n: pipeline provides near-linear speedup proportional to n^3 operations

 CHAINING:
   Multiplier output is directly connected to adder input.
   Two pipelines operate concurrently: multiplication and accumulation overlap.
   This is called PIPELINE CHAINING.
""")

# Matrix multiply pipeline
net_matmul = ed.NetworkDiagram(
    width=en.CW,
    height=240,
    theme=diag_theme,
    caption="Fig 7: Chained FP multiply + FP add pipeline for matrix multiplication",
)
net_matmul.node(
    "a", "A[i][k] Vector\n(from VRF or Memory)", x=50, y=180, kind="database"
)
net_matmul.node(
    "b", "B[k][j] Vector\n(from VRF or Memory)", x=50, y=80, kind="database"
)
net_matmul.node(
    "mul", "FP Multiplier\nPipeline\n(4 stages)", x=170, y=130, kind="server"
)
net_matmul.node("acc", "FP Adder\nPipeline\n(4 stages)", x=300, y=130, kind="server")
net_matmul.node("init", "Accumulator\nInit (0)", x=300, y=50, kind="generic")
net_matmul.node(
    "res", "C[i][j]\n(Inner Product\nResult)", x=460, y=130, kind="database"
)
net_matmul.link("a", "mul", label="Ai", bidirectional=False)
net_matmul.link("b", "mul", label="Bi", bidirectional=False)
net_matmul.link("mul", "acc", label="Ai*Bi (chained)", bidirectional=False)
net_matmul.link("init", "acc", bidirectional=False)
net_matmul.link("acc", "res", label="Running sum", bidirectional=False)
net_matmul.link("res", "acc", label="C += Ai*Bi", bidirectional=False)
en.story.extend(net_matmul.as_flowable())

en.tip(
    "Matrix multiply: n^3 multiply-add operations for n x n matrices. "
    "Pipeline chaining: multiplier output directly feeds adder input. "
    "Pipelined execution: feed one (Ai, Bi) pair per cycle. "
    "Both pipelines run concurrently -- maximum throughput. "
    "Supercomputer performance measured in FLOPS (floating-point operations per second)."
)
en.br()

# =============================================================================
#  5.9  MEMORY INTERLEAVING
# =============================================================================
en.chap_box("5.9  Memory Interleaving")
en.section("Need for Memory Interleaving")
en.definition(
    "<b>Memory Interleaving:</b> A technique for increasing effective memory bandwidth "
    "by dividing memory into multiple independent modules, each with its own address "
    "and data registers, so that multiple memory accesses can proceed in parallel. "
    "Pipeline and vector processors often require simultaneous access to memory from "
    "two or more sources -- for example, an instruction pipeline needs to fetch an "
    "instruction and an operand at the same time."
)

en.section("Memory Module Organization")
en.body(
    "The memory is partitioned into a number of modules, each connected to a common "
    "address bus and data bus. A memory module consists of a memory array with its "
    "own Address Register (AR) and Data Register (DR). The two least significant "
    "bits of the address select the module (for a 4-module system). Each module "
    "can honor a memory request independently of the state of other modules."
)

en.code_block("""
 MEMORY MODULE ORGANIZATION (4-Module Example):
 ======================================================
 Address bits: A[31:2] = word address within module, A[1:0] = module select

 Module 0: addresses 0, 4, 8, 12, 16, ... (A[1:0] = 00)
 Module 1: addresses 1, 5, 9, 13, 17, ... (A[1:0] = 01)
 Module 2: addresses 2, 6, 10, 14, 18, ... (A[1:0] = 10)
 Module 3: addresses 3, 7, 11, 15, 19, ... (A[1:0] = 11)

 ADDRESS DECODE:
   Module selected by LEAST SIGNIFICANT BITS of address.
   Remaining bits address the specific location within the module.

 SIMULTANEOUS ACCESS:
   CPU requests M[4], M[5], M[6], M[7] (4 consecutive words):
   These map to Module 0, 1, 2, 3 respectively.
   All four modules start their memory cycles simultaneously!
   All four words are available after ONE memory cycle time.
   Effective memory cycle time reduced by factor of 4.
""")

net_inter = ed.NetworkDiagram(
    width=en.CW,
    height=260,
    theme=diag_theme,
    caption="Fig 8: Four-module interleaved memory -- parallel access for vector/pipeline processors",
)
net_inter.node("cpu", "CPU / DMA\nRequests", x=50, y=130, kind="server")
net_inter.node(
    "abus",
    "Common Address Bus\n(A[31:2] + Module Select A[1:0])",
    x=210,
    y=200,
    kind="switch",
)
net_inter.node("dbus", "Common Data Bus\n(Bidirectional)", x=210, y=60, kind="switch")
net_inter.node(
    "m0",
    "Module 0\nAR0 + DR0\n(Even addr. 0,4,8...)",
    x=370,
    y=200,
    kind="database",
    label_pos="right",
)
net_inter.node(
    "m1",
    "Module 1\nAR1 + DR1\n(Addr. 1,5,9...)",
    x=370,
    y=140,
    kind="database",
    label_pos="right",
)
net_inter.node(
    "m2",
    "Module 2\nAR2 + DR2\n(Addr. 2,6,10...)",
    x=370,
    y=80,
    kind="database",
    label_pos="right",
)
net_inter.node(
    "m3",
    "Module 3\nAR3 + DR3\n(Odd addr. 3,7,11...)",
    x=370,
    y=20,
    kind="database",
    label_pos="right",
)

net_inter.link("cpu", "abus", label="Address")
net_inter.link("cpu", "dbus", label="Data")
net_inter.link("abus", "m0", label="CS0")
net_inter.link("abus", "m1", label="CS1")
net_inter.link("abus", "m2", label="CS2")
net_inter.link("abus", "m3", label="CS3")
net_inter.link("m0", "dbus")
net_inter.link("m1", "dbus")
net_inter.link("m2", "dbus")
net_inter.link("m3", "dbus")
en.story.extend(net_inter.as_flowable())

en.section("Interleaved Access -- Staggered Timing")
en.code_block("""
 INTERLEAVED MEMORY ACCESS TIMING (4-way interleaved, memory cycle = 4T):
 ======================================================
 Requests to Module 0, 1, 2, 3 are staggered by T each:

 Time:     0    T    2T   3T   4T   5T   6T   7T
 Mod 0:  [Read0                 ] [Read4              ]
 Mod 1:       [Read1              ]  [Read5            ]
 Mod 2:            [Read2           ]    [Read6         ]
 Mod 3:                 [Read3        ]       [Read7     ]

 Result:   At times 4T, 5T, 6T, 7T: one word delivered per T.
           Effective memory bandwidth = 4x single-module bandwidth.

 KEY FORMULA:
   If memory cycle time = Tm and n modules:
   Stagger delay between successive requests = Tm / n
   Effective cycle time for sequential burst access = Tm / n
   Speedup = n  (ideal, for long sequential access patterns)

 LIMITATIONS:
   Works best for sequential (consecutive address) accesses.
   Random access patterns do not benefit (may still be limited by Tm).
   Two requests to same module in same cycle still cause conflict.
""")

en.tip(
    "Memory interleaving: n modules, consecutive addresses distributed across modules. "
    "Module selected by least significant address bits. "
    "Parallel access: n consecutive words fetched in ~1 memory cycle time. "
    "Effective bandwidth up to n times higher for sequential access. "
    "Essential for vector processors that need to stream array elements."
)
en.br()

# =============================================================================
#  5.10  ARRAY PROCESSORS
# =============================================================================
en.chap_box("5.10  Array Processors")
en.section("Types of Array Processors")
en.definition(
    "<b>Array Processor:</b> A processor that performs computations on large arrays "
    "of data. There are two distinct types:<br/>"
    "1. <b>Attached Array Processor:</b> An auxiliary co-processor attached to a general-purpose "
    "host computer to accelerate specific numerical tasks. The host handles general computation; "
    "the array processor handles vector/matrix operations.<br/>"
    "2. <b>SIMD Array Processor:</b> A computer with multiple processing elements (PEs) "
    "operating in parallel under a single control unit. All PEs execute the same instruction "
    "but on different data -- a true SIMD organization."
)

en.section("SIMD Array Processor Organization")
en.body("The general block diagram of an SIMD array processor contains:")
en.bullet(
    [
        "<b>Master Control Unit (MCU):</b> Decodes instructions and determines how each is executed. "
        "Scalar and program control instructions execute within the MCU. "
        "Vector instructions are broadcast to all PEs simultaneously.",
        "<b>Processing Elements (PEs):</b> A set of identical processing units, each with an ALU, "
        "floating-point unit, working registers, and a local memory (M). Each PE operates on its "
        "own data stored in its local memory.",
        "<b>Main Program Memory:</b> Stores the program (instructions). Accessed by the MCU.",
        "<b>PE Local Memory (M):</b> Each PE has its own local memory holding its portion of "
        "the vector operands. Vector data is distributed to local memories before parallel execution.",
        "<b>Masking:</b> Each PE has a flag bit (active/inactive). When the flag = 1, the PE "
        "participates in the vector instruction. When flag = 0, the PE is idle. "
        "This allows conditional vector operations and handles vectors shorter than the PE count.",
    ]
)

en.section("SIMD Array Processor Example")
en.code_block("""
 SIMD ARRAY PROCESSOR EXAMPLE: Vector Addition C = A + B
 ======================================================
 Assume 64 Processing Elements (PEs), vector length = 64.

 Step 1 (MCU): Distribute vector A -- store a[i] in local memory M[i] of PE i.
 Step 2 (MCU): Distribute vector B -- store b[i] in local memory M[i] of PE i.
 Step 3 (MCU): Broadcast instruction: FADD c[i] <- a[i] + b[i]
 Step 4 (All 64 PEs simultaneously): Each PE reads a[i] and b[i] from its own M[i],
               computes a[i] + b[i], stores result as c[i].
 Step 5 (MCU): Collect results c[i] from each PE's local memory.

 Result: 64 additions performed SIMULTANEOUSLY in ONE instruction cycle!
         A 64-element vector add takes the same time as a single scalar add.

 MASKING EXAMPLE (vector length = 40, PE count = 64):
   Set flags: PE 0-39 active (flag=1), PE 40-63 inactive (flag=0).
   Broadcast FADD: only PE 0-39 execute; PE 40-63 remain idle.

 VECTOR LENGTH > PE COUNT (e.g., 200 elements, 64 PEs):
   MCU divides into 3 passes:
     Pass 1: PE 0-63 handle elements 0-63.
     Pass 2: PE 0-63 handle elements 64-127.
     Pass 3: PE 0-39 handle elements 128-199 (masking PE 40-63).
""")

net_simd = ed.NetworkDiagram(
    width=en.CW,
    height=280,
    theme=diag_theme,
    caption="Fig 9: SIMD Array Processor -- MCU broadcasts to all PEs simultaneously",
)
net_simd.node(
    "mcu",
    "Master Control Unit\n(MCU)\nDecodes & broadcasts",
    x=220,
    y=240,
    kind="server",
    label_pos="right",
)
net_simd.node(
    "prog",
    "Program Memory\n(Instructions)",
    x=60,
    y=240,
    kind="database",
    label_pos="left",
)
net_simd.node("pe0", "PE 0\nALU+FPU\nLocal M0", x=60, y=130, kind="host")
net_simd.node("pe1", "PE 1\nALU+FPU\nLocal M1", x=150, y=130, kind="host")
net_simd.node("pe2", "PE 2\nALU+FPU\nLocal M2", x=290, y=130, kind="host")
net_simd.node("pen", "PE n-1\nALU+FPU\nLocal Mn", x=380, y=130, kind="host")
net_simd.node("ibc", "Instruction Broadcast\nBus", x=220, y=60, kind="switch")

net_simd.link("prog", "mcu", label="Fetch program")
net_simd.link("mcu", "ibc", label="Broadcast instruction")
net_simd.link("ibc", "pe0")
net_simd.link("ibc", "pe1")
net_simd.link("ibc", "pe2")
net_simd.link("ibc", "pen")
en.story.extend(net_simd.as_flowable())

en.section("Comparison: Attached Array Processor vs SIMD Array Processor")
en.info_table(
    ["Feature", "Attached Array Processor", "SIMD Array Processor"],
    [
        [
            "Connection to host",
            "Auxiliary co-processor, attached to host bus",
            "Standalone -- IS the main computer",
        ],
        [
            "Control",
            "Host CPU sends tasks; array processor executes",
            "Master control unit (MCU) controls all PEs",
        ],
        [
            "Number of processors",
            "Typically one specialized processor",
            "Many identical PEs (8 to thousands)",
        ],
        [
            "Programming",
            "Host sends vector operations; array processor handles them",
            "MCU broadcasts single instruction to all PEs",
        ],
        [
            "Flexibility",
            "High -- host handles non-vector tasks",
            "Low -- best only for regular vector/matrix work",
        ],
        [
            "Examples",
            "Intel Phi (Knights Landing, attached mode), GPU as co-processor",
            "ILLIAC IV, MasPar MP-1, Connection Machine CM-2",
        ],
    ],
)

en.tip(
    "SIMD array processor: one MCU + many identical PEs. "
    "Same instruction broadcast to all PEs; each operates on its own local data. "
    "Masking: flag per PE controls participation (vector length < PE count). "
    "Limitations: poor at irregular data access, branching, and non-vector code."
)
en.br()

# =============================================================================
#  5.11  MULTIPROCESSORS
# =============================================================================
en.chap_box("5.11  Multiprocessors")
en.section("What is a Multiprocessor?")
en.definition(
    "<b>Multiprocessor System:</b> An interconnection of two or more CPUs with "
    "shared memory and I/O equipment, controlled by a single operating system "
    "that provides interaction among all processors. Unlike a computer network "
    "(where autonomous computers communicate via message passing), a multiprocessor "
    "system has all processors cooperating under one OS in solving a single problem. "
    "Multiprocessors are classified as MIMD -- Multiple Instruction, Multiple Data."
)

en.section("Characteristics of Multiprocessors")
en.bullet(
    [
        "<b>MIMD Organization:</b> Each processor has its own instruction stream and data stream. "
        "Processors operate concurrently but independently on different parts of a task.",
        "<b>Single OS:</b> One operating system manages all processors, memory, and I/O. "
        "This distinguishes a multiprocessor from a computer network (which has multiple OSes).",
        "<b>Shared resources:</b> Processors share main memory and I/O devices. "
        "Communication between processors occurs through shared memory (reads/writes to common locations).",
        "<b>Reliability:</b> If one processor fails, others can continue. The OS reassigns tasks "
        "to working processors, providing fault tolerance.",
        "<b>Two forms of parallelism:</b> (a) Multiple independent jobs run in parallel (throughput). "
        "(b) A single job partitioned into parallel tasks (speed-up).",
        "<b>Motivation:</b> Emergence of cheap microprocessors made large multiprocessor systems "
        "economically feasible. VLSI allows thousands of processors on a chip (e.g. GPUs, CMPs).",
    ]
)

en.section("Tightly Coupled vs Loosely Coupled Multiprocessors")
en.info_table(
    [
        "Feature",
        "Tightly Coupled\n(Shared Memory)",
        "Loosely Coupled\n(Distributed Memory)",
    ],
    [
        [
            "Memory organization",
            "Common shared global memory accessible by all processors",
            "Each processor has its own private local memory",
        ],
        [
            "Communication mechanism",
            "Read/write to shared memory locations (fast)",
            "Message passing through interconnection network (slower)",
        ],
        [
            "OS",
            "Single OS managing all processors and shared memory",
            "Each node may have its own OS; global coordinator manages tasks",
        ],
        [
            "Scalability",
            "Limited -- memory becomes a bottleneck as processors increase",
            "Highly scalable -- adding nodes does not create a shared bottleneck",
        ],
        [
            "Inter-processor interaction",
            "High -- processors share data efficiently via cache/RAM",
            "Low to moderate -- packet-based message passing",
        ],
        [
            "Cache",
            "Usually each CPU has a local cache; plus shared global memory",
            "Local memory acts as cache for the node; no shared cache",
        ],
        [
            "Suitable for",
            "Tasks with frequent shared-data access (tightly coupled tasks)",
            "Tasks with minimal data sharing (loosely coupled tasks)",
        ],
        [
            "Examples",
            "SMP servers (Intel Xeon multi-socket), NUMA systems",
            "Beowulf clusters, distributed computing (MPI-based HPC)",
        ],
    ],
)

# Tightly vs loosely coupled diagram
left_tight = ed.NetworkDiagram(
    width=en.CW * 0.44,
    height=200,
    theme=diag_theme,
    caption="Tightly Coupled Multiprocessor",
)
left_tight.node("c1", "CPU 1\n+ Cache", x=35, y=160, kind="server")
left_tight.node("c2", "CPU 2\n+ Cache", x=100, y=160, kind="server")
left_tight.node("c3", "CPU 3\n+ Cache", x=165, y=160, kind="server")
left_tight.node("bus", "Shared Memory Bus", x=100, y=90, kind="switch")
left_tight.node("mem", "Shared\nGlobal Memory", x=100, y=30, kind="database")
left_tight.link("c1", "bus")
left_tight.link("c2", "bus")
left_tight.link("c3", "bus")
left_tight.link("bus", "mem")

right_loose = ed.NetworkDiagram(
    width=en.CW * 0.44,
    height=200,
    theme=diag_theme,
    caption="Loosely Coupled Multiprocessor",
)
right_loose.node("n1", "Node 1\nCPU + Local Mem", x=35, y=160, kind="server")
right_loose.node("n2", "Node 2\nCPU + Local Mem", x=100, y=160, kind="server")
right_loose.node("n3", "Node 3\nCPU + Local Mem", x=165, y=160, kind="server")
right_loose.node("net", "Interconnection\nNetwork", x=100, y=80, kind="switch")
right_loose.link("n1", "net", label="msg")
right_loose.link("n2", "net", label="msg")
right_loose.link("n3", "net", label="msg")

left_tight.as_flowable()
right_loose.as_flowable()

tbl_mp = Table(
    [
        [
            ResponsiveDrawingFlowable(left_tight.drawing),
            ResponsiveDrawingFlowable(right_loose.drawing),
        ]
    ],
    colWidths=[en.CW * 0.48, en.CW * 0.48],
)
tbl_mp.setStyle(
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
en.add(tbl_mp)
en.sp(6)
en.add(
    Paragraph(
        "Fig 10 (left): Tightly coupled -- shared global memory via bus.  |  "
        "Fig 10 (right): Loosely coupled -- private memory with message-passing network.",
        en.COVER_SUB,
    )
)
en.sp(8)

en.section("Multiprocessor vs Multicomputer")
en.info_table(
    ["Aspect", "Multiprocessor", "Multicomputer (Network)"],
    [
        [
            "OS",
            "Single shared OS controls all processors",
            "Each computer has its own independent OS",
        ],
        [
            "Memory",
            "Shared global memory (tightly coupled)",
            "No shared memory -- private memory per computer",
        ],
        [
            "Communication",
            "Shared memory read/write",
            "Network message passing (TCP/IP, MPI, etc.)",
        ],
        [
            "Cooperation",
            "All processors cooperate under one OS",
            "Computers may or may not communicate",
        ],
        [
            "Physical boundary",
            "Single system with multiple CPUs",
            "Multiple physically separate computers",
        ],
        [
            "Example",
            "Dual-socket Intel Xeon server",
            "University compute cluster, Internet",
        ],
    ],
)

en.tip(
    "Multiprocessor: multiple CPUs, single OS, shared memory, MIMD. "
    "Tightly coupled: shared global memory (fast but limited scalability). "
    "Loosely coupled: private memory + message passing (scalable). "
    "Distinguishing feature vs multicomputer: one shared OS vs multiple independent OSes."
)
en.br()

# =============================================================================
#  5.12  QUICK REVISION SUMMARY
# =============================================================================
en.part_box("UNIT V -- QUICK REVISION SUMMARY")
en.chap_box("Key Concepts at a Glance")

en.info_table(
    ["Topic", "Key Point to Remember"],
    [
        [
            "Flynn's Classification",
            "SISD: one CPU, sequential (Von Neumann). "
            "SIMD: one control, many data units (vector/GPU). "
            "MISD: theoretical only. "
            "MIMD: many CPUs, many data streams (multiprocessors, multi-core).",
        ],
        [
            "Pipeline Structure",
            "k stages with inter-stage registers. Common clock Tp = tm + d (slowest stage + register delay). "
            "All stages work simultaneously on different tasks.",
        ],
        [
            "Pipeline Total Time",
            "Tk = [k + (n - 1)] * Tp for n tasks in k-stage pipeline. "
            "First result at cycle k; then one result per cycle.",
        ],
        [
            "Speedup Formula",
            "Sk = (n * Tn) / ([k + (n - 1)] * Tp). "
            "Maximum speedup as n -> inf: Sk_max = k (number of stages). "
            "Assumes Tn = k * Tp (uniform stage times).",
        ],
        [
            "Efficiency and Throughput",
            "Efficiency Ek = Sk / k (fraction of stages usefully occupied). "
            "Throughput = n / Tk = n / ([k + n - 1] * Tp).",
        ],
        [
            "Bottleneck Splitting",
            "Split the slowest pipeline stage into two shorter stages to reduce Tp. "
            "Adds one stage but can nearly double speedup.",
        ],
        [
            "Structural Hazard",
            "Two stages need same resource (e.g., single memory). "
            "Fix: Harvard architecture (separate instruction and data memory).",
        ],
        [
            "Data Hazard",
            "Instruction needs result of previous instruction not yet written back. "
            "Fix: stall (bubbles) OR operand forwarding/bypassing (preferred).",
        ],
        [
            "Control Hazard",
            "Branch instruction: wrongly fetched sequential instructions must be flushed. "
            "Fix: stall, branch prediction, or delayed branching (MIPS delay slot).",
        ],
        [
            "Arithmetic Pipeline (FP Add)",
            "4 stages: (1) Compare exponents, (2) Align mantissas, "
            "(3) Add/subtract mantissas, (4) Normalize result. "
            "Tp = max stage delay + register delay.",
        ],
        [
            "Instruction Pipeline (4-stage)",
            "FI (Fetch Instruction) -> DA (Decode + Address) -> FO (Fetch Operand) -> EX (Execute). "
            "FIFO instruction buffer. Branch/interrupt: flush buffer, restart.",
        ],
        [
            "Vector Processing",
            "Single instruction operates on entire array. Vector registers hold n elements. "
            "Register-to-register (fast) or memory-to-memory (slower). "
            "Masking controls which elements participate.",
        ],
        [
            "Matrix Multiplication",
            "n x n matrix multiply = n^3 multiply-add operations = n^2 inner products. "
            "Pipeline chaining: multiplier output feeds directly into adder pipeline.",
        ],
        [
            "Memory Interleaving",
            "n memory modules. Consecutive addresses map to different modules (via LSBs of address). "
            "Up to n simultaneous accesses. Effective bandwidth up to n times higher.",
        ],
        [
            "SIMD Array Processor",
            "MCU + n identical PEs each with local memory. "
            "Same instruction broadcast to all PEs; each works on its own data. "
            "Masking for partial vectors. Limited to regular numeric problems.",
        ],
        [
            "Attached Array Processor",
            "Auxiliary co-processor attached to general-purpose host. "
            "Host handles general code; array processor accelerates vector/matrix ops.",
        ],
        [
            "Tightly Coupled Multiprocessor",
            "Shared global memory, single OS. "
            "Fast inter-processor communication via shared memory. "
            "Memory bus is bottleneck for many processors.",
        ],
        [
            "Loosely Coupled Multiprocessor",
            "Private memory per node, message passing over network. "
            "Highly scalable. Good when inter-task data sharing is low.",
        ],
        [
            "Multiprocessor vs Multicomputer",
            "Multiprocessor: one shared OS + shared memory. "
            "Multicomputer: independent OSes + private memories + network. "
            "Multiprocessors cooperate; multicomputers may or may not.",
        ],
    ],
)

en.highlight(
    "<b>UNIT V EXAM BLUEPRINT:</b>  "
    "2-mark: State Flynn's classification. Define pipeline hazard. "
    "Define speedup factor. Distinguish tightly vs loosely coupled multiprocessor. "
    "State types of data hazards.  "
    "5-mark: Explain Flynn's classification with diagrams. "
    "Derive speedup, efficiency, and throughput formulas with example. "
    "Explain structural, data, and control hazards with solutions. "
    "Explain 4-segment FP arithmetic pipeline with numerical example. "
    "Explain memory interleaving with 4-module diagram.  "
    "10-mark: Explain pipelining with space-time diagram, speedup, efficiency, throughput (complete worked example). "
    "Explain 4-segment instruction pipeline with space-time diagram and branch effect. "
    "Explain vector processing and matrix multiplication with pipeline chaining. "
    "Explain SIMD array processor with block diagram, PE organization, and masking. "
    "Explain multiprocessor characteristics with tightly vs loosely coupled comparison.",
)

en.sp(10)
en.rule(en.get_theme().rl(en.get_theme().accent), 1.0)
en.sp(6)
en.add(
    Paragraph(
        "Computer Architecture IT-404 Unit V -- Bharat Dangi  |  UIT-RGPV (Autonomous) Bhopal | Semester IV",
        en.COVER_SUB,
    )
)

# =============================================================================
#  BUILD PDF
# =============================================================================
en.build_doc(
    "CA_Unit5_Notes.pdf",
    title="Computer Architecture - Unit V Notes",
    author="Bharat Dangi",
)
print("Generated: CA_Unit5_Notes.pdf")
