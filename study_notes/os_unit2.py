"""
Operating Systems (IT412) -- Unit II Notes
UIT-RGPV (Autonomous) Bhopal | Semester IV
Complete exam notes: CPU Scheduling, Scheduling Algorithms, IPC,
Process Synchronization, Critical Section, Semaphores, Classical Problems.

Run:  python os_unit2_notes.py
Output: OS_Unit2_Notes.pdf
"""

from __future__ import annotations

import engrapha_notes as en
import engrapha_diagrams as ed
from reportlab.platypus import Table

# =============================================================================
#  THEME & GLOBAL SETUP
#  Using FOREST_DARK — deep green accent, earthy tones
#  Distinct from Unit I (CATPPUCCIN_MOCHA)
# =============================================================================
en.set_story([])
en.set_theme(en.FOREST_DARK)

en.set_global_footer(
    left="Operating Systems (IT412) — Unit II",
    right="UIT-RGPV (Autonomous) Bhopal  |  Semester IV",
    show_page_num=True,
)

diag_theme = ed.DiagramTheme.from_notes_theme(en.get_theme())

# =============================================================================
#  COVER PAGE
# =============================================================================
en.bookmark("Cover Page")
en.suppress_footer(page_only=True)
en.sp(26)

en.cover_card(
    "OPERATING SYSTEMS",
    "Unit II — CPU Scheduling, IPC & Process Synchronization",
)
# en.cover_subtitle(
#     [
#         "Subject Code: IT412  |  UIT-RGPV (Autonomous) Bhopal  |  Semester IV",
#         "CPU Scheduling Criteria & Algorithms, Multiple Processor Scheduling,",
#         "IPC, Critical Section, Semaphores & Classical Synchronization Problems",
#     ]
# )
en.sp(10)
en.rule(en.get_theme().rl(en.get_theme().accent), 1.5)
en.sp(8)

en.info_table(
    ["Section", "Syllabus Topics Covered"],
    [
        [
            "2.1  Process Management",
            "Process creation, termination, cooperation, independence",
        ],
        [
            "2.2  CPU Scheduling Concepts",
            "CPU-I/O burst cycle, preemptive vs non-preemptive",
        ],
        [
            "2.3  Scheduling Criteria",
            "CPU utilization, throughput, turnaround, waiting, response time",
        ],
        [
            "2.4  FCFS Algorithm",
            "First-Come First-Served — Gantt chart, WT, TAT calculation",
        ],
        [
            "2.5  SJF Algorithm",
            "Shortest Job First — non-preemptive and preemptive (SRTF)",
        ],
        [
            "2.6  Priority Scheduling",
            "Non-preemptive and preemptive priority, starvation, aging",
        ],
        ["2.7  Round Robin", "Time quantum, circular queue, context switch overhead"],
        [
            "2.8  Multilevel Queue",
            "Foreground/background, fixed priority, time-slicing",
        ],
        [
            "2.9  Algorithm Evaluation",
            "Deterministic modelling, queuing models, simulation",
        ],
        [
            "2.10 Multiple Processor Scheduling",
            "Homogeneous, load balancing, processor affinity, NUMA",
        ],
        [
            "2.11 Cooperating Processes & IPC",
            "Independent vs cooperating, shared memory, message passing",
        ],
        [
            "2.12 Process Synchronization",
            "Race condition, need for synchronization, critical region",
        ],
        [
            "2.13 Critical Section Problem",
            "Mutual exclusion, progress, bounded waiting, Peterson's solution",
        ],
        [
            "2.14 Semaphores",
            "Binary semaphore, counting semaphore, wait/signal, implementation",
        ],
        [
            "2.15 Classical Problems",
            "Bounded Buffer, Readers-Writers, Dining Philosophers",
        ],
        ["2.16 Exam Questions", "25+ PYQ-style questions with complete answers"],
    ],
    col_widths=["28%", "72%"],
)

# =============================================================================
#  TABLE OF CONTENTS
# =============================================================================
en.br()
en.suppress_footer(page_only=True)
en.toc()

# =============================================================================
#  UNIT DIVIDER
# =============================================================================
en.part_box("UNIT II — CPU SCHEDULING & PROCESS MANAGEMENT")

# =============================================================================
#  2.1  PROCESS MANAGEMENT
# =============================================================================
en.chap_box("2.1  Process Management")

en.section("Process Creation")
en.definition(
    "<b>Process Creation:</b> A new process is created by an existing process using a system call. "
    "The creating process is the <b>parent</b>; the new process is the <b>child</b>. "
    "Children can themselves create further processes, forming a <b>process tree</b>. "
    "In Unix/Linux, every process except <code>init</code> (PID 1) has exactly one parent. "
    "The <code>fork()</code> system call duplicates the parent process — "
    "child gets a copy of parent's address space. "
    "<code>exec()</code> replaces the process image with a new program."
)

en.info_table(
    ["Resource Sharing Option", "Description"],
    [
        [
            "Parent and child share all resources",
            "Child inherits a copy of all parent's resources — full duplication.",
        ],
        [
            "Child shares subset of parent's resources",
            "Child gets only specific files/handles — common in Windows.",
        ],
        ["No sharing", "Parent and child operate completely independently after fork."],
    ],
)

en.section("Independent vs Cooperating Processes")
en.info_table(
    ["Aspect", "Independent Process", "Cooperating Process"],
    [
        [
            "Definition",
            "Cannot affect or be affected by other processes",
            "Can affect or be affected by other executing processes",
        ],
        [
            "Data sharing",
            "No shared data or resources",
            "Shares data (files, memory, variables) with other processes",
        ],
        [
            "Communication",
            "No need for IPC",
            "Requires IPC (shared memory or message passing)",
        ],
        ["Synchronization", "Not needed", "Mandatory — race conditions otherwise"],
        [
            "Examples",
            "Standalone batch jobs, simple calculators",
            "Web server + database, producer-consumer systems",
        ],
        [
            "Advantages",
            "Simple, no synchronization overhead",
            "Information sharing, computation speedup, modularity",
        ],
    ],
)

en.section("Reasons for Cooperating Processes")
en.bullet(
    [
        "<b>Information Sharing:</b> Multiple processes need access to the same data (e.g., shared database records, files).",
        "<b>Computation Speedup:</b> Divide a task into subtasks and run them on multiple processors simultaneously.",
        "<b>Modularity:</b> Divide system functions into separate processes (e.g., compiler, assembler, loader as pipeline stages).",
        "<b>Convenience:</b> User may work on multiple tasks — editing, compiling, printing at the same time.",
    ]
)
en.br()

# =============================================================================
#  2.2  CPU SCHEDULING CONCEPTS
# =============================================================================
en.part_box("UNIT II — CPU SCHEDULING")
en.chap_box("2.2  CPU Scheduling — Core Concepts")

en.section("The CPU–I/O Burst Cycle")
en.definition(
    "<b>CPU–I/O Burst Cycle:</b> Process execution alternates between periods of CPU computation "
    "(<b>CPU burst</b>) and waiting for I/O (<b>I/O burst</b>). "
    "A process begins with a CPU burst, then an I/O burst, then another CPU burst, and so on, "
    "until the final CPU burst ends with a system call to terminate. "
    "The distribution of CPU burst lengths is key to selecting a scheduling algorithm. "
    "<b>I/O-bound processes</b> have many short CPU bursts (e.g., interactive programs). "
    "<b>CPU-bound processes</b> have few long CPU bursts (e.g., scientific computations)."
)

td_burst = ed.TimingDiagram(
    width=en.CW,
    height=160,
    theme=diag_theme,
    caption="Fig 2.1: CPU–I/O burst cycle — alternating CPU and I/O periods",
)
td_burst.signal(
    "CPU Burst", transitions=[(0, 1), (30, 0), (60, 1), (100, 0), (130, 1), (160, 0)]
)
td_burst.signal(
    "I/O Burst", transitions=[(0, 0), (30, 1), (60, 0), (100, 1), (130, 0), (160, 1)]
)
en.story.extend(td_burst.as_flowable())

en.section("Preemptive vs Non-Preemptive Scheduling")
en.definition(
    "<b>Non-Preemptive Scheduling:</b> Once the CPU is allocated to a process, it keeps the CPU "
    "until it releases it voluntarily — either by terminating or by switching to waiting state (I/O). "
    "Simple to implement; no race conditions on kernel data structures. "
    "Used in Windows 3.x and early batch systems. "
    "<b>Preemptive Scheduling:</b> The OS can forcibly take the CPU away from a running process "
    "(e.g., when a higher-priority process arrives or time quantum expires). "
    "Requires hardware timer. Better response time. Used in all modern OSes. "
    "Requires careful synchronization — a process can be preempted in the middle of updating shared data."
)

en.info_table(
    ["Feature", "Non-Preemptive", "Preemptive"],
    [
        [
            "CPU release",
            "Voluntary only (exit or I/O wait)",
            "Forced by OS (timer, priority)",
        ],
        [
            "Starvation risk",
            "High (long job can delay all others)",
            "Reduced (timer ensures fairness)",
        ],
        [
            "Implementation",
            "Simple — no timer required",
            "Complex — needs timer, context switch",
        ],
        [
            "Response time",
            "Poor for interactive users",
            "Good — quick context switching",
        ],
        [
            "Examples",
            "FCFS, non-preemptive SJF, non-preemptive Priority",
            "SRTF, RR, preemptive Priority",
        ],
        [
            "OS type",
            "Batch systems, early Windows",
            "All modern OS (Linux, Windows NT+)",
        ],
    ],
)

en.section("The Dispatcher")
en.definition(
    "<b>Dispatcher:</b> The OS module that gives CPU control to the process selected by the "
    "short-term scheduler. It performs: (1) context switching, (2) switching to user mode, "
    "(3) jumping to the correct location in the user program to restart it. "
    "<b>Dispatch latency</b> is the time the dispatcher takes to stop one process and start another — "
    "this must be minimized as it is pure overhead."
)
en.br()

# =============================================================================
#  2.3  SCHEDULING CRITERIA
# =============================================================================
en.chap_box("2.3  CPU Scheduling Criteria")

en.section("The Five Scheduling Criteria")
en.definition(
    "Scheduling criteria are the metrics used to evaluate and compare CPU scheduling algorithms. "
    "Different algorithms optimize different criteria. "
    "There is no universally optimal algorithm — the right choice depends on system goals."
)

en.info_table(
    ["Criterion", "Goal", "Formula / Meaning"],
    [
        [
            "CPU Utilization",
            "MAXIMIZE — keep CPU as busy as possible.",
            "% of time CPU is busy. Range: 0–100%. Real systems: 40% (lightly) to 90% (heavily loaded).",
        ],
        [
            "Throughput",
            "MAXIMIZE — complete as many processes as possible per unit time.",
            "Number of processes completing per second/minute. Higher = better.",
        ],
        [
            "Turnaround Time (TAT)",
            "MINIMIZE — total time from submission to completion.",
            "TAT = Completion Time − Arrival Time. Includes waiting + executing + I/O.",
        ],
        [
            "Waiting Time (WT)",
            "MINIMIZE — total time spent in the ready queue waiting for CPU.",
            "WT = TAT − Burst Time  (for non-preemptive).\nWT = TAT − Burst Time − Arrival Time.",
        ],
        [
            "Response Time",
            "MINIMIZE — time from request submission to first CPU response (important for interactive systems).",
            "Time from process submission until first response is produced. Different from TAT.",
        ],
    ],
)

en.note(
    "Key formula: <b>TAT = Completion Time − Arrival Time</b>  |  "
    "<b>WT = TAT − Burst Time</b>  |  "
    "<b>Avg WT = Sum of all WT / Number of processes</b>  |  "
    "<b>Avg TAT = Sum of all TAT / Number of processes</b>"
)
en.br()

# =============================================================================
#  2.4  FCFS
# =============================================================================
en.chap_box("2.4  First-Come First-Served (FCFS)")

en.section("FCFS — Definition and Mechanism")
en.definition(
    "<b>FCFS (First-Come First-Served):</b> The simplest CPU scheduling algorithm. "
    "Processes are assigned the CPU in the order they arrive in the ready queue. "
    "It is implemented using a FIFO queue. "
    "When a process enters the ready queue, its PCB is linked to the tail of the queue. "
    "When the CPU is free, the process at the head of the queue is allocated the CPU. "
    "FCFS is <b>non-preemptive</b> — once a process gets the CPU, it runs to completion "
    "(or until it blocks on I/O)."
)

en.section("FCFS — Worked Example")
en.body(
    "Given: P1 (Arrival=0, Burst=24ms), P2 (Arrival=0, Burst=3ms), P3 (Arrival=0, Burst=3ms). "
    "All arrive at time 0. Order: P1, P2, P3."
)
en.info_table(
    [
        "Process",
        "Arrival Time",
        "Burst Time",
        "Completion",
        "TAT = CT−AT",
        "WT = TAT−BT",
    ],
    [
        ["P1", "0", "24 ms", "24", "24 − 0 = 24", "24 − 24 = 0"],
        ["P2", "0", "3 ms", "27", "27 − 0 = 27", "27 − 3 = 24"],
        ["P3", "0", "3 ms", "30", "30 − 0 = 30", "30 − 3 = 27"],
        ["<b>Average</b>", "—", "—", "—", "<b>27.0 ms</b>", "<b>17.0 ms</b>"],
    ],
)
en.tip(
    "Average Waiting Time = (0 + 24 + 27) / 3 = 17 ms. "
    "The <b>Convoy Effect</b>: short processes behind a very long process wait a long time. "
    "If P2, P3 ran first: Avg WT = (0 + 3 + 6) / 3 = 3 ms — much better!"
)

en.info_table(
    ["Aspect", "FCFS"],
    [
        ["Type", "Non-preemptive"],
        ["Implementation", "Simple FIFO queue"],
        ["Starvation", "No — every process eventually gets CPU"],
        ["Convoy Effect", "YES — short processes stuck behind long ones"],
        ["Best for", "Batch systems, non-interactive jobs"],
        ["Worst for", "Interactive / time-sharing systems"],
    ],
)
en.br()

# =============================================================================
#  2.5  SJF
# =============================================================================
en.chap_box("2.5  Shortest Job First (SJF / SRTF)")

en.section("SJF — Definition")
en.definition(
    "<b>SJF (Shortest Job First):</b> Assigns CPU to the process with the smallest next CPU burst. "
    "If two processes have the same burst, FCFS breaks the tie. "
    "SJF is provably <b>optimal</b> — it gives the minimum average waiting time for a given set "
    "of processes (among all non-preemptive algorithms). "
    "The main challenge is that the <b>length of the next CPU burst is unknown</b> in advance — "
    "it must be predicted using an exponential average of past burst lengths."
)

en.section("Predicting Next CPU Burst — Exponential Average")
en.formula_block(r"\tau_{n+1} = \alpha \cdot t_n + (1 - \alpha) \cdot \tau_n")
en.bullet(
    [
        r"<b>τ(n+1)</b>: predicted value of the next CPU burst.",
        r"<b>t(n)</b>: length of the nth (most recent actual) CPU burst.",
        r"<b>τ(n)</b>: our previous prediction for the nth burst.",
        r"<b>α</b>: smoothing factor, 0 ≤ α ≤ 1. α=0.5 is commonly used. "
        "α=0 ignores recent history; α=1 uses only the most recent burst.",
    ]
)

en.section("Non-Preemptive SJF — Worked Example")
en.info_table(
    ["Process", "Arrival Time", "Burst Time", "Completion", "TAT", "WT"],
    [
        ["P1", "0", "6 ms", "6", "6", "0"],
        ["P3", "2", "4 ms", "10", "8", "4"],
        ["P4", "3", "5 ms", "15", "12", "7"],
        ["P2", "0", "8 ms", "23", "23", "15"],
        ["<b>Average</b>", "—", "—", "—", "<b>12.25 ms</b>", "<b>6.5 ms</b>"],
    ],
)
en.note(
    "Execution order: P1 (arrives 0, burst 6) → P3 (arrives 2, burst 4) → "
    "P4 (arrives 3, burst 5) → P2 (arrives 0, burst 8). "
    "At time 6: ready queue has P2 (8ms), P3 (4ms), P4 (5ms) — P3 is shortest."
)

en.section("Preemptive SJF — SRTF (Shortest Remaining Time First)")
en.definition(
    "<b>SRTF (Shortest Remaining Time First):</b> The preemptive version of SJF. "
    "When a new process arrives, if its burst time is less than the <b>remaining time</b> "
    "of the currently running process, the current process is preempted and the new process runs. "
    "SRTF gives the minimum average waiting time among ALL scheduling algorithms (preemptive and non-preemptive)."
)

en.info_table(
    ["Process", "Arrival", "Burst"],
    [["P1", "0", "8"], ["P2", "1", "4"], ["P3", "2", "9"], ["P4", "3", "5"]],
)
en.body(
    "SRTF Gantt: P1 runs 0→1, P2 preempts at t=1 (4 < 7 remaining), P2 runs 1→5, "
    "P4 arrives t=3 (5ms) but P2 has only 2ms left — P2 continues, P4 runs 5→10, "
    "P1 resumes 10→17, P3 runs 17→26. "
    "Avg WT = (9 + 0 + 15 + 2) / 4 = 6.5 ms."
)

en.info_table(
    ["Aspect", "Non-Preemptive SJF", "SRTF (Preemptive SJF)"],
    [
        ["Preemption", "No", "Yes — on new arrival if shorter remaining"],
        [
            "Optimal?",
            "Optimal among non-preemptive",
            "Globally optimal — minimum avg WT",
        ],
        [
            "Starvation",
            "Possible for long jobs",
            "More severe — long jobs may never run",
        ],
        ["Remedy for starvation", "Aging", "Aging"],
        ["Overhead", "Low", "Higher — more context switches"],
    ],
)
en.br()

# =============================================================================
#  2.6  PRIORITY SCHEDULING
# =============================================================================
en.chap_box("2.6  Priority Scheduling")

en.section("Priority Scheduling — Definition")
en.definition(
    "<b>Priority Scheduling:</b> Each process is assigned a priority number (integer). "
    "The CPU is allocated to the process with the highest priority. "
    "Convention varies: in some systems, lower number = higher priority (Linux: -20 highest); "
    "in others, higher number = higher priority. "
    "SJF is a special case of priority scheduling where priority = inverse of next CPU burst length. "
    "Can be preemptive (arriving higher-priority process preempts current) or non-preemptive."
)

en.section("Starvation and Aging")
en.definition(
    "<b>Starvation (Indefinite Blocking):</b> Low-priority processes may never get the CPU "
    "because high-priority processes keep arriving. A process can wait indefinitely — "
    "in 1973, an MIT system shut down and found a process that had been waiting for 10 years! "
    "<b>Aging:</b> The solution. Gradually increase the priority of processes that have been "
    "waiting for a long time. Example: every 15 minutes, increase priority of all waiting "
    "processes by 1 — ensures even the lowest-priority process will eventually run."
)

en.section("Priority Scheduling — Worked Example")
en.body("Given processes (all arrive at time 0). Priority: 1 = highest.")
en.info_table(
    ["Process", "Burst Time", "Priority", "Completion", "TAT", "WT"],
    [
        ["P2", "1 ms", "1 (highest)", "1", "1", "0"],
        ["P5", "5 ms", "2", "6", "6", "1"],
        ["P1", "10 ms", "3", "16", "16", "6"],
        ["P3", "2 ms", "4", "18", "18", "16"],
        ["P4", "1 ms", "5 (lowest)", "19", "19", "18"],
        ["<b>Average</b>", "—", "—", "—", "<b>12.0 ms</b>", "<b>8.2 ms</b>"],
    ],
)
en.br()

# =============================================================================
#  2.7  ROUND ROBIN
# =============================================================================
en.chap_box("2.7  Round Robin (RR) Scheduling")

en.section("Round Robin — Definition")
en.definition(
    "<b>Round Robin (RR):</b> Designed specifically for time-sharing systems. "
    "Similar to FCFS but with preemption. A small time unit called a <b>time quantum</b> "
    "(or time slice) is defined — typically 10–100 milliseconds. "
    "The ready queue is treated as a circular queue. "
    "The CPU is allocated to each process for at most one time quantum. "
    "If the process has a burst > quantum, it is preempted and placed at the back of the ready queue. "
    "If the process has a burst ≤ quantum, it runs to completion within its quantum."
)

en.section("Effect of Time Quantum Size")
en.info_table(
    ["Time Quantum", "Behaviour", "Problem"],
    [
        [
            "Very large (∞)",
            "Degenerates to FCFS — no preemption",
            "Poor response time for interactive users",
        ],
        [
            "Very small (→ 0)",
            "Called processor sharing — N processes each get 1/N CPU speed",
            "Excessive context switches — too much overhead",
        ],
        [
            "Optimal (10–100 ms)",
            "Good balance — each process responds quickly, overhead acceptable",
            "Context switch time should be << quantum (< 10% overhead)",
        ],
    ],
)

en.section("Round Robin — Worked Example (Quantum = 4ms)")
en.body("Processes: P1 (Burst=24), P2 (Burst=3), P3 (Burst=3). All arrive at t=0.")
en.info_table(
    ["Process", "Burst Time", "Completion Time", "TAT = CT−AT", "WT = TAT−BT"],
    [
        ["P1", "24 ms", "30 ms", "30", "30 − 24 = 6"],
        ["P2", "3 ms", "7 ms", "7", "7 − 3 = 4"],
        ["P3", "3 ms", "10 ms", "10", "10 − 3 = 7"],
        ["<b>Average</b>", "—", "—", "<b>15.67 ms</b>", "<b>5.67 ms</b>"],
    ],
)
en.note(
    "Gantt: P1(0-4) → P2(4-7) → P3(7-10) → P1(10-14) → P1(14-18) → P1(18-22) → P1(22-26) → P1(26-30). "
    "P2 and P3 finish early within their first quantum. "
    "Avg WT with FCFS was 17ms; RR gives 5.67ms — much better response."
)

en.info_table(
    ["Aspect", "Round Robin"],
    [
        ["Type", "Preemptive (time quantum)"],
        ["Starvation", "No — every process gets CPU in every quantum cycle"],
        ["Response time", "Good — bounded by (n−1) × quantum"],
        ["Overhead", "Context switch every quantum — higher than FCFS/SJF"],
        ["Best for", "Time-sharing, interactive systems"],
        ["Performance depends on", "Time quantum size — tune carefully"],
    ],
)
en.br()

# =============================================================================
#  2.8  MULTILEVEL QUEUE & FEEDBACK
# =============================================================================
en.chap_box("2.8  Multilevel Queue Scheduling")

en.section("Multilevel Queue Scheduling")
en.definition(
    "<b>Multilevel Queue Scheduling:</b> The ready queue is partitioned into several separate queues "
    "based on process type or priority class. "
    "Each queue has its own scheduling algorithm. "
    "Scheduling must also be done between queues — typically <b>fixed-priority preemptive scheduling</b> "
    "(foreground queue has absolute priority over background) or <b>time-slicing</b> between queues. "
    "Processes are <b>permanently assigned</b> to a queue — no movement between queues."
)

stack_mlq = ed.LayeredStack(
    width=en.CW * 0.60,
    height=200,
    theme=diag_theme,
    caption="Fig 2.2: Multilevel queue — 5 priority levels",
)
stack_mlq.layer("System Processes", sublabel="Highest priority — always runs first")
stack_mlq.layer("Interactive Processes", sublabel="Round Robin scheduling")
stack_mlq.layer("Interactive Editing", sublabel="Round Robin scheduling")
stack_mlq.layer("Batch Processes", sublabel="FCFS scheduling")
stack_mlq.layer("Student Processes", sublabel="Lowest priority — FCFS")
en.story.extend(stack_mlq.as_flowable())

en.section("Multilevel Feedback Queue (MLFQ)")
en.definition(
    "<b>Multilevel Feedback Queue:</b> An extension that allows processes to MOVE between queues. "
    "A process that uses too much CPU time is moved to a lower-priority queue. "
    "A process waiting too long in a low-priority queue is promoted (aging) to a higher-priority queue. "
    "This provides the most general and flexible scheduling — "
    "it can be configured to match any system workload. "
    "MLFQ is the most complex scheduling algorithm and is used in many modern systems."
)

en.info_table(
    ["Queue", "Time Quantum", "Purpose"],
    [
        [
            "Q0 (highest)",
            "8 ms",
            "New processes start here. If not done in 8ms, move to Q1.",
        ],
        ["Q1", "16 ms", "If not done in 16ms, move to Q2."],
        [
            "Q2 (lowest)",
            "FCFS",
            "Long CPU-bound processes run here with no preemption.",
        ],
    ],
)
en.br()

# =============================================================================
#  2.9  ALGORITHM EVALUATION
# =============================================================================
en.chap_box("2.9  Algorithm Evaluation")

en.section("Methods for Evaluating Scheduling Algorithms")
en.info_table(
    ["Method", "Description", "Pros / Cons"],
    [
        [
            "Deterministic Modelling",
            "Apply algorithm to a specific known workload (set of processes with fixed arrival/burst times). "
            "Calculate metrics exactly. Simple worked examples in textbooks.",
            "Pro: Simple, exact. Con: Applies only to that specific input — not general.",
        ],
        [
            "Queuing Models",
            "Use queuing theory (Little's law, Markov chains). Model arrival rate (λ) and service rate (μ). "
            "Derive average queue length, waiting time analytically.",
            "Pro: General mathematical formulas. Con: Requires simplifying assumptions (e.g., Poisson arrivals).",
        ],
        [
            "Simulation",
            "Program a simulation of the scheduler and OS. Use statistical distributions or "
            "recorded real traces as input. Measure metrics over simulated time.",
            "Pro: Accurate, flexible. Con: Expensive to implement and run. Trace collection difficult.",
        ],
        [
            "Implementation",
            "Implement the algorithm in the actual OS and test on real workloads.",
            "Pro: Most accurate. Con: Very costly, may need OS modification, results vary with workload.",
        ],
    ],
)

en.section("Little's Law (Queuing Theory)")
en.definition(
    "<b>Little's Law:</b> A fundamental result from queuing theory that relates "
    "average queue length (n), arrival rate (λ), and average waiting time (W)."
)
en.formula_block(r"n = \lambda \times W")
en.bullet(
    [
        "<b>n</b>: average number of processes in the queue.",
        "<b>λ</b>: average process arrival rate (processes per second).",
        "<b>W</b>: average waiting time per process in the queue.",
        "Example: if λ = 7 processes/sec and W = 2 sec, then n = 14 processes in queue on average.",
    ]
)
en.br()

# =============================================================================
#  2.10  MULTIPLE PROCESSOR SCHEDULING
# =============================================================================
en.chap_box("2.10  Multiple Processor Scheduling")

en.section("Approaches to Multi-Processor Scheduling")
en.definition(
    "<b>Multiple Processor Scheduling:</b> Scheduling when multiple CPUs are available. "
    "More complex than single-processor scheduling. "
    "Two main approaches: "
    "<b>Asymmetric Multiprocessing (AMP):</b> One master processor handles all scheduling "
    "decisions and I/O; other processors execute user processes. Simple — only one processor "
    "accesses system data structures. "
    "<b>Symmetric Multiprocessing (SMP):</b> Each processor is self-scheduling. "
    "All processors share a common ready queue or each has its own private queue. "
    "Most modern systems (Linux, Windows) use SMP."
)

en.section("Key Concepts in Multi-Processor Scheduling")
en.info_table(
    ["Concept", "Description"],
    [
        [
            "Load Balancing",
            "In SMP, keep all CPUs equally busy. Two approaches: "
            "(1) <b>Push migration</b> — OS periodically checks load on each processor; "
            "if imbalanced, pushes tasks to less-loaded processors. "
            "(2) <b>Pull migration</b> — idle processor pulls a task from a busy processor's queue.",
        ],
        [
            "Processor Affinity",
            "A process has an affinity for the processor it is currently running on (warm cache). "
            "<b>Soft affinity:</b> OS tries (but doesn't guarantee) to keep process on same CPU. "
            "<b>Hard affinity:</b> Process specifies which CPUs it may run on (Linux: sched_setaffinity).",
        ],
        [
            "NUMA (Non-Uniform Memory Access)",
            "In systems where CPUs have faster access to local memory than remote memory. "
            "Scheduler must try to keep process on the CPU closest to its allocated memory. "
            "Linux NUMA-aware scheduler considers CPU-memory topology.",
        ],
        [
            "Hyperthreading (SMT)",
            "Intel CPUs present each physical core as 2 logical CPUs to the OS. "
            "OS schedules 2 threads simultaneously on one physical core. "
            "Logical CPUs share FPU and caches but have independent registers and PC.",
        ],
        [
            "Multicore Processors",
            "Multiple cores on one chip share the on-chip cache. "
            "Memory stall cycles (cache miss waiting for memory) waste CPU time. "
            "Hardware designers add a second hardware thread per core so the CPU can "
            "switch to the other thread during memory stalls (coarse-grained or fine-grained multithreading).",
        ],
    ],
)
en.br()

# =============================================================================
#  2.11  IPC
# =============================================================================
en.part_box("UNIT II — INTERPROCESS COMMUNICATION & SYNCHRONIZATION")
en.chap_box("2.11  Interprocess Communication (IPC)")

en.section("What is IPC?")
en.definition(
    "<b>Interprocess Communication (IPC):</b> A mechanism provided by the OS that allows "
    "cooperating processes to exchange data and synchronize their actions. "
    "IPC is necessary because processes in modern OS have separate address spaces — "
    "one process cannot directly read or write another's memory (protection!). "
    "There are two fundamental IPC models: <b>Shared Memory</b> and <b>Message Passing</b>."
)

# Architecture diagram showing IPC models
arch_ipc = ed.ArchitectureDiagram(
    width=en.CW,
    height=200,
    theme=diag_theme,
    caption="Fig 2.3: IPC models — Shared Memory vs Message Passing",
)
arch_ipc.client("p1", "Process A")
arch_ipc.service("shm", "Shared Memory\nRegion")
arch_ipc.client("p2", "Process B")
arch_ipc.service("msg", "Message\nQueue / Pipe")
arch_ipc.connect("p1", "shm", "read/write")
arch_ipc.connect("p2", "shm", "read/write")
arch_ipc.connect("p1", "msg", "send()")
arch_ipc.connect("p2", "msg", "receive()")
en.story.extend(arch_ipc.as_flowable())

en.section("Shared Memory vs Message Passing")
en.info_table(
    ["Feature", "Shared Memory", "Message Passing"],
    [
        [
            "Mechanism",
            "Processes share a region of memory. OS creates the region; processes attach to it.",
            "OS provides send(msg) and receive(msg) primitives. Data copied between processes.",
        ],
        [
            "Speed",
            "Very fast after setup — memory access speed. No kernel involvement per operation.",
            "Slower — each message requires system calls (kernel involvement).",
        ],
        [
            "Synchronization",
            "Programmer must explicitly synchronize (mutex, semaphore) to avoid race conditions.",
            "Synchronization is implicit — message passing naturally synchronizes.",
        ],
        [
            "Amount of data",
            "Best for large data — no copying.",
            "Best for small data / many messages.",
        ],
        [
            "Ease of use",
            "Complex — requires manual synchronization.",
            "Simpler — OS handles communication details.",
        ],
        [
            "Examples",
            "POSIX shm_open(), mmap(), System V shmget()",
            "POSIX pipes, message queues, sockets, MPI",
        ],
        [
            "Used in",
            "Producer-consumer, shared databases, multi-threaded apps",
            "Distributed systems, microservices, client-server",
        ],
    ],
)

en.section("Producer-Consumer Problem (Shared Memory Model)")
en.definition(
    "<b>Producer-Consumer Problem:</b> A classic IPC scenario. "
    "The producer process produces data items and places them in a shared buffer. "
    "The consumer process takes items from the buffer and consumes them. "
    "The buffer is finite — producer must wait if buffer is full; "
    "consumer must wait if buffer is empty. "
    "This requires synchronization between the two processes."
)
en.code_block(
    """/* Shared Memory Producer-Consumer -- Bounded Buffer */
#define BUFFER_SIZE 10
typedef struct {
    int buffer[BUFFER_SIZE];
    int in;   /* index where producer inserts next item */
    int out;  /* index where consumer removes next item */
} shared_data;

/* PRODUCER process */
void producer(shared_data *shm, int item) {
    while (((shm->in + 1) % BUFFER_SIZE) == shm->out)
        ;  /* busy-wait: buffer is full */
    shm->buffer[shm->in] = item;
    shm->in = (shm->in + 1) % BUFFER_SIZE;
}

/* CONSUMER process */
int consumer(shared_data *shm) {
    while (shm->in == shm->out)
        ;  /* busy-wait: buffer is empty */
    int item = shm->buffer[shm->out];
    shm->out = (shm->out + 1) % BUFFER_SIZE;
    return item;
}
/* NOTE: Buffer can hold BUFFER_SIZE-1 items (one slot wasted to distinguish full from empty) */""",
    lang="c",
)
en.br()

# =============================================================================
#  2.12  PROCESS SYNCHRONIZATION
# =============================================================================
en.chap_box("2.12  Process Synchronization")

en.section("The Race Condition Problem")
en.definition(
    "<b>Race Condition:</b> A situation where the outcome of concurrent processes depends on "
    "the order in which they are scheduled (interleaved). "
    "When two or more processes access shared data concurrently and try to modify it, "
    "the final result depends on the particular order of access — which is non-deterministic. "
    "The name comes from the processes 'racing' to access the shared data. "
    "Race conditions lead to <b>data inconsistency</b> and must be prevented."
)

en.section("Classic Race Condition — Counter Example")
en.code_block(
    """/* Both producer and consumer share 'counter' */
/* Register1 and Register2 are local CPU registers */

/* PRODUCER code: counter++ */
register1 = counter;          /* load */
register1 = register1 + 1;   /* increment */
counter = register1;          /* store */

/* CONSUMER code: counter-- */
register2 = counter;          /* load */
register2 = register2 - 1;   /* decrement */
counter = register2;          /* store */

/* RACE CONDITION EXAMPLE:
   Initially counter = 5.
   P1 (producer): register1 = 5
   P1 (producer): register1 = 6        [preempted here!]
   P2 (consumer): register2 = 5
   P2 (consumer): register2 = 4
   P2 (consumer): counter = 4
   P1 (producer): counter = 6          [WRONG! Should be 5]
   
   Expected: counter = 5. Actual: 6 or 4 depending on schedule! */""",
    lang="c",
)

en.warning(
    "Race conditions are extremely difficult to detect and reproduce because they depend "
    "on exact CPU scheduling timing. A program may work correctly 99% of the time and fail "
    "1% — always at the worst possible moment. Prevention through proper synchronization is essential."
)
en.br()

# =============================================================================
#  2.13  CRITICAL SECTION
# =============================================================================
en.chap_box("2.13  The Critical Section Problem")

en.section("Critical Section — Definition")
en.definition(
    "<b>Critical Section:</b> A segment of code in which a process may be accessing "
    "and updating shared data (shared variables, files, tables). "
    "The critical section property requires that when one process is executing in its "
    "critical section, no other process is allowed to execute in its critical section — "
    "the critical sections of different processes are <b>mutually exclusive</b> in time."
)

en.section("Structure of a Process with Critical Section")
en.code_block(
    """/* General structure of a process Pi */
do {
    /* --- ENTRY SECTION --- */
    /* Request permission to enter critical section */
    /* (locking mechanism goes here)               */

    /* --- CRITICAL SECTION --- */
    /* Access/modify shared data HERE */

    /* --- EXIT SECTION --- */
    /* Signal that critical section is done         */
    /* (unlocking mechanism goes here)              */

    /* --- REMAINDER SECTION --- */
    /* Rest of the process (non-critical code)      */

} while (true);""",
    lang="c",
)

en.section("Three Requirements for a Valid Solution")
en.definition(
    "Any correct solution to the critical section problem must satisfy all three conditions simultaneously:"
)
en.info_table(
    ["Requirement", "Definition", "Implication"],
    [
        [
            "1. Mutual Exclusion",
            "If process Pi is executing in its critical section, no other process can execute in its critical section.",
            "This is the fundamental safety property — prevents data corruption.",
        ],
        [
            "2. Progress",
            "If no process is in its critical section and some processes wish to enter, "
            "the selection of which enters next cannot be postponed indefinitely. "
            "Only processes not in the remainder section can participate in this decision.",
            "Prevents deadlock in the entry section — a process cannot be permanently blocked from entering.",
        ],
        [
            "3. Bounded Waiting",
            "There exists a bound (limit) on the number of times other processes are allowed to "
            "enter their critical sections after a process has made a request to enter and "
            "before that request is granted.",
            "Prevents starvation — every process gets its turn eventually.",
        ],
    ],
)

en.section("Peterson's Solution (Two-Process Software Solution)")
en.definition(
    "<b>Peterson's Solution:</b> A classic software solution to the two-process critical section problem. "
    "Uses two shared variables: <code>turn</code> (whose turn it is to enter) and "
    "<code>flag[2]</code> (whether each process wants to enter). "
    "Satisfies all three requirements: mutual exclusion, progress, and bounded waiting. "
    "Note: On modern CPUs with instruction reordering, Peterson's may not work without memory barriers."
)
en.code_block(
    """/* Shared variables */
int turn;          /* whose turn: 0 = P0's turn, 1 = P1's turn */
boolean flag[2];   /* flag[i] = true means Pi wants to enter */

/* Process Pi (i = 0 or 1, j = 1-i) */
do {
    flag[i] = true;       /* I want to enter */
    turn = j;             /* Yield to other process — be polite! */

    /* Wait while: the other wants to enter AND it's their turn */
    while (flag[j] == true && turn == j)
        ;                 /* busy wait (spin) */

    /* --- CRITICAL SECTION --- */

    flag[i] = false;      /* I am done */

    /* --- REMAINDER SECTION --- */

} while (true);

/* PROOF of Mutual Exclusion:
   For both P0 and P1 to be in CS simultaneously:
   flag[0]=flag[1]=true AND (turn=0 AND turn=1) -- IMPOSSIBLE!
   Therefore mutual exclusion holds. */""",
    lang="c",
)

en.section("Hardware Synchronization Primitives")
en.info_table(
    ["Primitive", "Description", "Usage"],
    [
        [
            "test_and_set()",
            "Atomically reads a lock variable and sets it to true in one uninterruptible hardware instruction.",
            "while (test_and_set(&lock)) ; /* spin */  /* CS */  lock = false;",
        ],
        [
            "compare_and_swap()",
            "Atomically: if *value == expected, set *value = new_value and return old value. "
            "Used in lock-free algorithms.",
            "Basis for modern atomic operations in C11 (atomic_compare_exchange).",
        ],
        [
            "Interrupt disabling",
            "Disable interrupts before entering CS; re-enable after. Prevents preemption.",
            "Works on single-CPU systems only. Dangerous — can delay critical system events.",
        ],
    ],
)
en.br()

# =============================================================================
#  2.14  SEMAPHORES
# =============================================================================
en.chap_box("2.14  Semaphores")

en.section("What is a Semaphore?")
en.definition(
    "<b>Semaphore:</b> A synchronization tool proposed by Dijkstra (1965). "
    "A semaphore S is an integer variable that, apart from initialization, "
    "is accessed only through two standard atomic operations: "
    "<b>wait()</b> (originally P, from Dutch 'Proberen' = to test) and "
    "<b>signal()</b> (originally V, from Dutch 'Verhogen' = to increment). "
    "The key property: these operations are executed atomically — "
    "no two processes can execute wait/signal on the same semaphore simultaneously."
)

en.section("Wait and Signal Operations")
en.code_block(
    """/* Classic semaphore operations */

/* wait(S) -- also called P(S) or down(S) */
wait(S) {
    while (S <= 0)
        ;           /* busy wait / spin — test S repeatedly */
    S--;            /* decrement — acquire the resource */
}

/* signal(S) -- also called V(S) or up(S) */
signal(S) {
    S++;            /* increment — release the resource */
}

/* ATOMIC: Both operations must execute as indivisible units.
   The value of S can never be negative in the busy-wait version.
   If S = 0, wait() spins until signal() increments it. */""",
    lang="c",
)

en.section("Types of Semaphores")
en.info_table(
    ["Type", "Initial Value", "Purpose", "Example Use"],
    [
        [
            "Binary Semaphore (Mutex)",
            "1 (can only be 0 or 1)",
            "Provides mutual exclusion. Only one process in critical section at a time. "
            "Equivalent to a mutex lock.",
            "Protecting a shared counter, file, or data structure.",
        ],
        [
            "Counting Semaphore",
            "N (the resource count)",
            "Controls access to a resource with N instances. "
            "Initialized to the number of available resource instances.",
            "Controlling access to a pool of 5 database connections; bounded buffer with N slots.",
        ],
    ],
)

en.section("Semaphore as Mutex — Critical Section")
en.code_block(
    """/* Using binary semaphore (mutex) for critical section */
semaphore mutex;
init(mutex, 1);   /* initialize to 1 -- resource available */

/* Process Pi */
do {
    wait(mutex);    /* P(mutex) -- acquire lock -- S becomes 0 */

    /* --- CRITICAL SECTION --- */

    signal(mutex);  /* V(mutex) -- release lock -- S becomes 1 */

    /* --- REMAINDER SECTION --- */

} while (true);

/* If P1 is in CS: mutex = 0. P2 calls wait(mutex) -- finds S=0 -- spins.
   When P1 calls signal(mutex): mutex = 1. P2 exits spin, enters CS. */""",
    lang="c",
)

en.section("Semaphore for Process Synchronization (Ordering)")
en.code_block(
    """/* Ensure S2 in P2 executes only AFTER S1 in P1 */
semaphore sync;
init(sync, 0);   /* initialize to 0 -- P2 must wait for P1 */

/* Process P1 */         /* Process P2 */
S1;                      wait(sync);    /* blocks if sync=0 */
signal(sync);            S2;            /* runs after S1 */

/* P1 executes S1, then signals sync (sync becomes 1).
   P2 blocks at wait(sync) until P1 signals.
   Guarantees S1 happens-before S2 regardless of scheduling. */""",
    lang="c",
)

en.section("Blocking Semaphore (Non-Busy-Wait Implementation)")
en.definition(
    "<b>Blocking Semaphore:</b> Instead of busy-waiting (spinning), a process that finds "
    "the semaphore value ≤ 0 is placed in a <b>waiting queue</b> associated with that semaphore "
    "and blocked (state → Waiting). When another process calls signal(), one process from "
    "the waiting queue is woken up (state → Ready). "
    "This eliminates wasted CPU cycles from spinning. "
    "Modern semaphore implementations always use blocking."
)
en.code_block(
    """/* Blocking semaphore data structure */
typedef struct {
    int value;           /* semaphore counter */
    list *waiting_queue; /* queue of blocked processes */
} semaphore;

/* Non-busy-wait: block instead of spin */
wait(semaphore *S) {
    S->value--;
    if (S->value < 0) {
        add_to_queue(S->waiting_queue, current_process);
        block();   /* move this process to waiting state */
    }
}

signal(semaphore *S) {
    S->value++;
    if (S->value <= 0) {
        P = remove_from_queue(S->waiting_queue);
        wakeup(P);   /* move P from waiting to ready state */
    }
}
/* Note: S->value can now be negative! |S->value| = # of blocked processes. */""",
    lang="c",
)

en.warning(
    "Deadlock with Semaphores: If P0 executes wait(S) and P1 executes wait(Q), "
    "then P0 executes wait(Q) and P1 executes wait(S) — both wait forever. "
    "This is a deadlock. Correct ordering of wait() calls prevents this."
)
en.br()

# =============================================================================
#  2.15  CLASSICAL SYNCHRONIZATION PROBLEMS
# =============================================================================
en.part_box("UNIT II — CLASSICAL SYNCHRONIZATION PROBLEMS")
en.chap_box("2.15  Classical Problems of Synchronization")

en.section("Problem 1: Bounded Buffer (Producer-Consumer)")
en.definition(
    "<b>Bounded Buffer Problem:</b> A buffer of N slots. "
    "Producer adds items; Consumer removes items. "
    "Three semaphores: <b>mutex</b> (binary, init=1) for mutual exclusion on buffer; "
    "<b>empty</b> (counting, init=N) counts empty slots; "
    "<b>full</b> (counting, init=0) counts full slots. "
    "Producer waits for empty slot; Consumer waits for full slot."
)
en.code_block(
    """/* Bounded Buffer -- N-slot buffer */
semaphore mutex;   init(mutex, 1);    /* mutual exclusion on buffer */
semaphore empty;   init(empty, N);    /* N empty slots initially */
semaphore full;    init(full,  0);    /* 0 full slots initially */

/* PRODUCER */                       /* CONSUMER */
do {                                 do {
    /* produce item */                   wait(full);
    wait(empty);     /* slot free? */    wait(mutex);
    wait(mutex);     /* lock buffer */
    /* add item to buffer */             /* remove item from buffer */
    signal(mutex);   /* unlock */        signal(mutex);
    signal(full);    /* one more full */  signal(empty); /* one more empty */
                                         /* consume item */
} while (true);                      } while (true);

/* empty + full = N always (total slots constant) */
/* mutex ensures only one process modifies buffer at a time */""",
    lang="c",
)

en.section("Problem 2: Readers-Writers Problem")
en.definition(
    "<b>Readers-Writers Problem:</b> A shared database accessed by readers (read-only) "
    "and writers (read-write). Constraint: multiple readers may read simultaneously, "
    "but a writer needs exclusive access — no other reader or writer may access while writing. "
    "<b>First readers-writers problem:</b> No reader is kept waiting unless a writer has already "
    "been granted permission (readers have priority). "
    "<b>Second readers-writers problem:</b> Once a writer is ready, it performs its write as soon "
    "as possible (writers have priority). Both can cause starvation of the other group."
)
en.code_block(
    """/* First Readers-Writers Problem (readers priority) */
semaphore rw_mutex;    init(rw_mutex, 1);  /* writer mutual exclusion */
semaphore mutex;       init(mutex, 1);     /* protect read_count */
int       read_count = 0;                  /* number of active readers */

/* WRITER */                         /* READER */
do {                                 do {
    wait(rw_mutex);  /* exclusive */     wait(mutex);
                                         read_count++;
    /* perform write */                  if (read_count == 1)
                                             wait(rw_mutex); /* first reader blocks writer */
    signal(rw_mutex);                    signal(mutex);

} while (true);                          /* perform read */

                                         wait(mutex);
                                         read_count--;
                                         if (read_count == 0)
                                             signal(rw_mutex); /* last reader releases writer */
                                         signal(mutex);
                                     } while (true);

/* If read_count > 0: writer blocked. rw_mutex free only when read_count == 0 */""",
    lang="c",
)

en.section("Problem 3: Dining Philosophers Problem")
en.definition(
    "<b>Dining Philosophers Problem (Dijkstra, 1965):</b> Five philosophers sit at a round table. "
    "Between each pair of philosophers is one chopstick (5 total). "
    "A philosopher alternates between thinking and eating. "
    "To eat, they need BOTH left and right chopsticks simultaneously. "
    "After eating, they put both chopsticks down. "
    "This problem models the allocation of multiple resources among multiple processes "
    "without deadlock or starvation."
)

en.code_block(
    """/* Dining Philosophers -- Naive (DEADLOCKED) solution */
semaphore chopstick[5];  /* all initialized to 1 */

/* Philosopher i */
do {
    /* think... */

    wait(chopstick[i]);           /* pick up left chopstick */
    wait(chopstick[(i+1) % 5]);   /* pick up right chopstick */

    /* eat... */

    signal(chopstick[i]);         /* put down left */
    signal(chopstick[(i+1) % 5]); /* put down right */

} while (true);

/* DEADLOCK: If all 5 philosophers simultaneously pick up left chopstick,
   all 5 wait for right chopstick -- circular wait -- DEADLOCK! */

/* SOLUTIONS:
   (1) Allow at most 4 philosophers to sit simultaneously.
   (2) Pick up chopsticks only if BOTH are available (atomically).
   (3) Asymmetric solution: odd philosophers pick left-then-right;
       even philosophers pick right-then-left (breaks circular wait). */""",
    lang="c",
)

en.code_block(
    """/* Dining Philosophers -- CORRECT solution (max 4 seated) */
semaphore chopstick[5];   /* initialized to 1 */
semaphore room;           /* initialized to 4 -- at most 4 sit */

/* Philosopher i */
do {
    /* think... */

    wait(room);                       /* only 4 can try to eat at once */
    wait(chopstick[i]);               /* left chopstick */
    wait(chopstick[(i+1) % 5]);       /* right chopstick */

    /* eat... */

    signal(chopstick[(i+1) % 5]);
    signal(chopstick[i]);
    signal(room);                     /* free up seat */

} while (true);

/* With at most 4 philosophers, at least one has both chopsticks available.
   Deadlock is impossible. Starvation is still theoretically possible
   (unfair scheduling) but bounded waiting can be added. */""",
    lang="c",
)

# State machine for philosopher states
sm_phil = ed.StateMachine(
    width=en.CW * 0.70,
    height=180,
    theme=diag_theme,
    caption="Fig 2.4: Dining Philosopher state transitions",
)
sm_phil.state("think", "Thinking", initial=True)
sm_phil.state("hungry", "Hungry\n(Waiting)")
sm_phil.state("eat", "Eating", accepting=True)
sm_phil.transition("think", "hungry", label="gets hungry")
sm_phil.transition("hungry", "eat", label="both chopsticks\navailable")
sm_phil.transition("eat", "think", label="finishes\neating")
en.story.extend(sm_phil.as_flowable())
en.br()

# =============================================================================
#  ALGORITHM COMPARISON MASTER TABLE
# =============================================================================
en.chap_box("CPU Scheduling Algorithm — Master Comparison")

en.section("All Algorithms Side-by-Side")
en.info_table(
    ["Algorithm", "Type", "Selection Criterion", "Starvation", "Overhead", "Best For"],
    [
        [
            "FCFS",
            "Non-preemptive",
            "Arrival order",
            "No",
            "Low",
            "Batch, simple systems",
        ],
        [
            "SJF",
            "Non-preemptive",
            "Shortest burst first",
            "Yes",
            "Medium",
            "Batch, known burst times",
        ],
        [
            "SRTF",
            "Preemptive",
            "Shortest remaining time",
            "Yes",
            "High",
            "Optimal avg WT needed",
        ],
        [
            "Priority",
            "Both",
            "Highest priority first",
            "Yes",
            "Medium",
            "Real-time, tiered systems",
        ],
        [
            "Round Robin",
            "Preemptive",
            "FIFO + time quantum",
            "No",
            "High",
            "Time-sharing, interactive",
        ],
        [
            "MLFQ",
            "Preemptive",
            "Multi-queue + promotion",
            "No",
            "Highest",
            "Modern general-purpose OS",
        ],
    ],
)

en.section("Scheduling Formula Quick Reference")
en.info_table(
    ["Formula", "Meaning"],
    [
        ["TAT = Completion Time − Arrival Time", "Total time process spends in system"],
        ["WT = TAT − Burst Time", "Time spent waiting in ready queue (non-preemptive)"],
        [
            "WT = TAT − Burst Time − Arrival Time",
            "Normalized for processes not arriving at 0",
        ],
        [
            "Response Time = First CPU Time − Arrival Time",
            "Time to first CPU allocation",
        ],
        ["Avg WT = Σ(WT) / N", "Average waiting time over all N processes"],
        ["Avg TAT = Σ(TAT) / N", "Average turnaround time over all N processes"],
        [
            "CPU Utilization = (Busy time / Total time) × 100%",
            "% of time CPU is executing",
        ],
        ["Throughput = N / Total time", "Processes completed per unit time"],
    ],
)
en.br()

# =============================================================================
#  2.16  EXAM QUESTIONS
# =============================================================================
en.part_box("UNIT II — EXAM QUESTIONS & DETAILED ANSWERS")
en.chap_box("2.16  Previous-Year Style Exam Questions")

en.section("2-Mark Questions")

en.highlight(
    "<b>Q1. What are CPU scheduling criteria? Name all five.</b><br/>"
    "A: (1) CPU Utilization — maximize % time CPU is busy. "
    "(2) Throughput — maximize processes completed per unit time. "
    "(3) Turnaround Time — minimize time from submission to completion (TAT = CT − AT). "
    "(4) Waiting Time — minimize time spent in ready queue (WT = TAT − BT). "
    "(5) Response Time — minimize time from request to first response (important for interactive)."
)

en.highlight(
    "<b>Q2. What is the Convoy Effect in FCFS?</b><br/>"
    "A: Convoy Effect occurs in FCFS when a CPU-bound process (long burst) holds the CPU "
    "while many I/O-bound processes (short burst) accumulate in the ready queue. "
    "Short processes must wait for the long process to finish, leading to high average waiting time. "
    "Example: P1 (24ms) followed by P2 (3ms) and P3 (3ms) — Avg WT = 17ms. "
    "If order reversed: Avg WT = 3ms. FCFS is unfair to short processes."
)

en.highlight(
    "<b>Q3. Why is SJF optimal? What is its main drawback?</b><br/>"
    "A: SJF is optimal because it minimizes the average waiting time for a given set of processes. "
    "By executing shorter jobs first, longer jobs experience less waiting overall — a mathematical minimum. "
    "Main drawback: The next CPU burst length is unknown in advance and must be predicted "
    "using exponential average of past bursts (τ(n+1) = α×t(n) + (1−α)×τ(n)). "
    "Additionally, SJF can cause starvation of long processes."
)

en.highlight(
    "<b>Q4. What is the critical section problem? State its three requirements.</b><br/>"
    "A: The critical section problem is how to ensure that when one process is executing "
    "shared code (critical section), no other process executes the same section simultaneously. "
    "Three requirements: (1) <b>Mutual Exclusion</b> — only one process in CS at a time. "
    "(2) <b>Progress</b> — if CS is empty and processes want to enter, decision cannot be postponed. "
    "(3) <b>Bounded Waiting</b> — limit on how many times others enter before a requesting process is granted."
)

en.highlight(
    "<b>Q5. What is a semaphore? Differentiate binary and counting semaphore.</b><br/>"
    "A: A semaphore is an integer synchronization variable accessed only via atomic wait(S) and signal(S). "
    "wait(S): while(S≤0); S--; — signal(S): S++. "
    "<b>Binary semaphore (mutex):</b> value ∈ {0, 1}. Used for mutual exclusion. One process at a time. "
    "<b>Counting semaphore:</b> value initialized to N (resource count). "
    "Controls access to N instances of a resource. Value = number of available instances."
)

en.highlight(
    "<b>Q6. What is a race condition? Give an example.</b><br/>"
    "A: A race condition is when multiple processes access shared data concurrently and "
    "the result depends on execution order. "
    "Example: counter++ is three instructions (load, increment, store). "
    "If producer (counter++) and consumer (counter--) are interleaved, "
    "counter may end at 4, 5, or 6 instead of the correct value of 5. "
    "Race conditions cause data inconsistency and must be prevented using synchronization."
)

en.highlight(
    "<b>Q7. What is preemptive vs non-preemptive scheduling?</b><br/>"
    "A: Non-preemptive: CPU held until process voluntarily releases it (terminates or I/O). "
    "Simple, no timer needed. Examples: FCFS, non-preemptive SJF. "
    "Preemptive: OS can forcibly remove CPU from running process (timer, higher-priority arrival). "
    "Better response time. Requires synchronization. Examples: RR, SRTF, preemptive Priority. "
    "All modern OSes (Linux, Windows) use preemptive scheduling."
)

en.highlight(
    "<b>Q8. What is IPC? Name two models with examples.</b><br/>"
    "A: IPC (Interprocess Communication) is the OS mechanism for cooperating processes "
    "to exchange data and synchronize. "
    "Model 1 — Shared Memory: processes share a memory region; direct access via variables. "
    "Fast but requires explicit synchronization. Examples: POSIX shm_open, mmap. "
    "Model 2 — Message Passing: processes use send()/receive() system calls. "
    "OS copies data between processes. Slower but simpler synchronization. "
    "Examples: pipes, message queues, sockets."
)

en.section("5-Mark Questions")

en.highlight(
    "<b>Q9. Explain FCFS, SJF, and Round Robin with Gantt charts and calculate Avg WT.</b><br/>"
    "A: Given: P1(BT=6), P2(BT=8), P3(BT=7), P4(BT=3). All arrive at t=0. "
    "FCFS: P1→P2→P3→P4. CT: 6,14,21,24. WT: 0,6,14,21. Avg WT = 41/4 = 10.25ms. "
    "SJF: P4→P1→P3→P2. CT: 3,9,16,24. WT: 0,3,9,16. Avg WT = 28/4 = 7.0ms. "
    "RR (q=4): P1(0-4)→P2(4-8)→P3(8-12)→P4(12-15)→P1(15-17)→P2(17-21)→P3(21-24). "
    "Avg WT better than FCFS, response time best."
)

en.highlight(
    "<b>Q10. Explain Peterson's solution to the critical section problem. "
    "Prove it satisfies mutual exclusion.</b><br/>"
    "A: Uses two shared vars: turn (0 or 1) and flag[2] (boolean). "
    "Pi sets flag[i]=true (wants to enter), sets turn=j (yields), "
    "then waits while(flag[j] && turn==j). "
    "Mutual exclusion proof: For both P0 and P1 in CS simultaneously, "
    "flag[0]=flag[1]=true AND (turn=0 AND turn=1) — impossible since turn has one value. "
    "Progress: if Pj not interested (flag[j]=false), Pi enters immediately. "
    "Bounded waiting: after Pi sets flag[i], if turn=j, Pj runs then sets turn=i allowing Pi."
)

en.highlight(
    "<b>Q11. Explain the Bounded Buffer problem with semaphore solution.</b><br/>"
    "A: N-slot buffer shared by producer and consumer. "
    "3 semaphores: mutex=1 (exclusive buffer access), empty=N (empty slots), full=0 (full slots). "
    "Producer: wait(empty) → wait(mutex) → add item → signal(mutex) → signal(full). "
    "Consumer: wait(full) → wait(mutex) → remove item → signal(mutex) → signal(empty). "
    "Analysis: empty+full=N always. mutex ensures no simultaneous buffer access. "
    "Producer blocks when empty=0 (buffer full). Consumer blocks when full=0 (buffer empty)."
)

en.highlight(
    "<b>Q12. Explain the Dining Philosophers problem. What causes deadlock? How to prevent it?</b><br/>"
    "A: 5 philosophers, 5 chopsticks. Need both left+right chopstick to eat. "
    "Naive solution: all pick left simultaneously → wait for right → deadlock (circular wait). "
    "Prevention methods: "
    "(1) Allow at most 4 philosophers to sit (room semaphore init=4). "
    "(2) Asymmetric: odd-numbered pick left-then-right; even pick right-then-left. "
    "(3) Pick both chopsticks atomically in one operation — test-and-set. "
    "Deadlock conditions: mutual exclusion, hold-and-wait, no preemption, circular wait. "
    "Remove any one condition to prevent deadlock."
)

en.section("10-Mark Questions")

en.highlight(
    "<b>Q13. Explain all CPU scheduling algorithms with Gantt charts, advantages/disadvantages, "
    "and calculate Avg Waiting Time for: P1(AT=0,BT=10), P2(AT=1,BT=4), "
    "P3(AT=2,BT=5), P4(AT=3,BT=2).</b><br/>"
    "A: <b>FCFS:</b> P1(0-10)→P2(10-14)→P3(14-19)→P4(19-21). "
    "WT: P1=0, P2=9, P3=12, P4=16. Avg WT = 37/4 = 9.25ms. "
    "<b>Non-Preemptive SJF:</b> P1 runs (only arrival at 0); at t=10: P4(2),P2(4),P3(5). "
    "Order: P1→P4→P2→P3. Gantt: P1(0-10),P4(10-12),P2(12-16),P3(16-21). "
    "WT: P1=0,P4=7,P2=11,P3=14. Avg WT = 32/4 = 8ms. "
    "<b>SRTF:</b> P1(0-1)→P2 arrives(burst=4<9): P2(1-2)→P3 arrives(5>3remaining P2): "
    "P2(2-3)→P4 arrives(2<2remaining P2): P4(3-5)→P2(5-6)→P3(6-11)→P1(11-20). "
    "<b>RR(q=3):</b> Round-robin all processes in arrival order with quantum=3. "
    "Better response time than FCFS."
)

en.highlight(
    "<b>Q14. Explain process synchronization in detail. "
    "Discuss critical section, race condition, semaphores, and classical problems.</b><br/>"
    "A: Process synchronization ensures correct execution of cooperating processes sharing data. "
    "<b>Race Condition:</b> Non-deterministic result when processes access shared data concurrently "
    "(counter++ example — result can be wrong by ±1). "
    "<b>Critical Section:</b> Code accessing shared data. Solution must satisfy: "
    "mutual exclusion, progress, bounded waiting. "
    "<b>Semaphores:</b> wait(S)/signal(S) — binary for mutex, counting for resource pool. "
    "<b>Classical Problems:</b> "
    "Bounded Buffer (producer-consumer): mutex+empty+full semaphores. "
    "Readers-Writers: rw_mutex + mutex + read_count. "
    "Dining Philosophers: deadlock risk — use room semaphore or asymmetric solution."
)

en.section("Quick Revision Table — Unit II")
en.info_table(
    ["Topic", "Key Exam Points"],
    [
        [
            "FCFS",
            "Non-preemptive. FIFO. Convoy Effect = short jobs wait behind long. Simple. No starvation.",
        ],
        [
            "SJF",
            "Optimal avg WT. Non-preemptive. Predicts burst with exponential average. Starvation possible.",
        ],
        [
            "SRTF",
            "Preemptive SJF. Global optimum. Preempts on shorter arrival. More context switches.",
        ],
        [
            "Priority",
            "Higher priority runs first. Starvation → fix with Aging. Preemptive or Non-preemptive.",
        ],
        [
            "Round Robin",
            "Preemptive. Time quantum. No starvation. Best response time. Overhead from frequent switches.",
        ],
        [
            "MLFQ",
            "Multiple queues. Processes demoted on long CPU use. Promoted if waiting too long. Modern OS.",
        ],
        [
            "Scheduling criteria",
            "CPU utilization↑, Throughput↑, TAT↓, WT↓, Response Time↓. TAT=CT−AT. WT=TAT−BT.",
        ],
        [
            "IPC",
            "Shared Memory (fast, manual sync) vs Message Passing (slower, OS handles sync). Producer-Consumer.",
        ],
        [
            "Race Condition",
            "Concurrent shared data access → non-deterministic result. Must prevent via synchronization.",
        ],
        [
            "Critical Section",
            "3 requirements: Mutual Exclusion, Progress, Bounded Waiting.",
        ],
        [
            "Peterson's Solution",
            "flag[] + turn. Software solution. turn=j means 'yield'. Satisfies all 3 requirements.",
        ],
        [
            "Binary Semaphore",
            "0 or 1. Acts as mutex lock. wait()=acquire, signal()=release.",
        ],
        [
            "Counting Semaphore",
            "Init=N. Controls N resource instances. Negative value = # of waiting processes.",
        ],
        [
            "Bounded Buffer",
            "3 semaphores: mutex=1, empty=N, full=0. Producer waits on empty; consumer on full.",
        ],
        [
            "Readers-Writers",
            "Multiple readers simultaneously. Writer exclusive. rw_mutex + mutex + read_count.",
        ],
        [
            "Dining Philosophers",
            "5 philosophers, 5 chopsticks. Naive→deadlock. Fix: room semaphore (max 4) or asymmetric.",
        ],
        [
            "Load Balancing",
            "Push migration (OS checks) + Pull migration (idle CPU pulls). Keeps all CPUs busy.",
        ],
        [
            "Processor Affinity",
            "Soft (try same CPU) vs Hard (must use specified CPUs). Preserves warm cache.",
        ],
    ],
)

en.exam(
    "Most asked topics in IT412 Unit II exams: "
    "(1) CPU scheduling — draw Gantt chart and calculate Avg WT and Avg TAT for FCFS, SJF, RR. "
    "(2) Semaphore definition and solution to Bounded Buffer. "
    "(3) Critical section requirements — mutual exclusion, progress, bounded waiting. "
    "(4) Peterson's solution with code. "
    "(5) Dining Philosophers — identify deadlock, provide solution. "
    "(6) Differentiate preemptive vs non-preemptive. "
    "Always show the Gantt chart step-by-step when calculating scheduling metrics."
)

en.note(
    "Lab connection: Experiments 1–6 implement FCFS, SJF (non-preemptive), SRTF (preemptive SJF), "
    "Round Robin, Priority (non-preemptive), and Priority (preemptive) respectively. "
    "For each experiment: generate random process arrival/burst times, run the algorithm, "
    "print the Gantt chart, and compute Avg WT and Avg TAT."
)

# =============================================================================
#  FLASHCARDS & REVISION
# =============================================================================
en.br()
en.chap_box("Rapid Revision & Flashcards")

en.revision_card(
    "Unit II Mastery Check",
    [
        "Draw Gantt charts and compute Avg WT for FCFS, SJF, and RR for a given process set.",
        "Write the semaphore solution to the Bounded Buffer problem from memory.",
        "State and prove the three critical section requirements with an example.",
        "Explain how Aging solves starvation in Priority Scheduling.",
        "Identify the deadlock scenario in Dining Philosophers and provide two solutions.",
    ],
)

en.flashcard(
    "What is a <b>Race Condition</b>?",
    "When multiple processes access shared data concurrently and the outcome depends "
    "on the exact order of execution — leading to non-deterministic, incorrect results.",
)
en.flashcard(
    "Formula: <b>Turnaround Time</b>",
    "TAT = Completion Time − Arrival Time. " "Waiting Time = TAT − Burst Time.",
)
en.flashcard(
    "What does <b>Aging</b> solve?",
    "Aging prevents starvation in Priority Scheduling by gradually increasing "
    "the priority of processes that have been waiting for a long time.",
)
en.flashcard(
    "Semaphore <b>wait(S)</b> operation",
    "while(S ≤ 0) ; (busy wait)  S--; "
    "In blocking version: S--; if(S<0) block(currentProcess);",
)
en.flashcard(
    "Bounded Buffer — three semaphores",
    "mutex (init=1): exclusive buffer access. "
    "empty (init=N): count of empty slots. "
    "full (init=0): count of full slots.",
)

en.br()
en.chap_box("Index")
en.print_index()

# =============================================================================
#  BUILD DOCUMENT
# =============================================================================
en.build_doc("OS_Unit2_Notes.pdf")

print("Generated: OS_Unit2_Notes.pdf")
