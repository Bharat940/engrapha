"""
Operating Systems (IT412) -- Unit III Notes
UIT-RGPV (Autonomous) Bhopal | Semester IV
Complete exam notes: Deadlock (conditions, RAG, prevention, avoidance,
detection, recovery) and Memory Management (binding, logical/physical
addressing, MMU, contiguous allocation, partitioning strategies).

Run:  python os_unit3_notes.py
Output: OS_Unit3_Notes.pdf  |  OS_Unit3_Notes_html/  |  OS_Unit3_Notes.pptx
"""

from __future__ import annotations

import engrapha_notes as en
import engrapha_diagrams as ed
from reportlab.platypus import Table

# =============================================================================
#  THEME & GLOBAL SETUP
#  Using SUNSET_DARK — warm amber/orange accent on deep dark bg
#  Distinct from Unit I (CATPPUCCIN_MOCHA) and Unit II (FOREST_DARK)
# =============================================================================
en.set_story([])
en.set_theme(en.SUNSET_DARK)

en.set_global_footer(
    left="Operating Systems (IT412) — Unit III",
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
    "Unit III — Deadlock & Memory Management",
)
# en.cover_subtitle(
#     [
#         "Subject Code: IT412  |  UIT-RGPV (Autonomous) Bhopal  |  Semester IV",
#         "Deadlock: Conditions, RAG, Prevention, Avoidance (Banker's Algorithm),",
#         "Detection, Recovery — Memory Management: Binding, MMU, Contiguous Allocation",
#     ]
# )
en.sp(10)
en.rule(en.get_theme().rl(en.get_theme().accent), 1.5)
en.sp(8)

en.info_table(
    ["Section", "Syllabus Topics Covered"],
    [
        ["3.1  Deadlock — Introduction", "Definition, system model, resource types"],
        [
            "3.2  Necessary Conditions",
            "Mutual exclusion, hold & wait, no preemption, circular wait",
        ],
        [
            "3.3  Resource Allocation Graph",
            "RAG notation, request/assignment edges, cycle detection",
        ],
        [
            "3.4  Deadlock Prevention",
            "Attacking each of the four necessary conditions",
        ],
        [
            "3.5  Deadlock Avoidance",
            "Safe state, Banker's Algorithm, Resource-Request Algorithm",
        ],
        [
            "3.6  Deadlock Detection",
            "Single-instance RAG (wait-for graph), multi-instance detection algorithm",
        ],
        [
            "3.7  Deadlock Recovery",
            "Process termination, resource preemption, rollback",
        ],
        [
            "3.8  Memory Management — Intro",
            "Goals, address spaces, memory hierarchy",
        ],
        [
            "3.9  Address Binding",
            "Compile-time, load-time, execution-time binding",
        ],
        [
            "3.10 Logical vs Physical Address",
            "Address space, MMU, base-limit registers, dynamic relocation",
        ],
        [
            "3.11 Contiguous Allocation",
            "Single-partition, multi-partition (fixed & variable), fragmentation",
        ],
        [
            "3.12 Partition Strategies",
            "First Fit, Best Fit, Worst Fit — comparison and worked examples",
        ],
        ["3.13 Exam Questions", "25+ PYQ-style questions with complete answers"],
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
#  PART DIVIDER
# =============================================================================
en.part_box("UNIT III — PART A: DEADLOCK")

# =============================================================================
#  3.1  DEADLOCK — INTRODUCTION
# =============================================================================
en.chap_box("3.1  Deadlock — Introduction")

en.section("What is a Deadlock?")
en.definition(
    "<b>Deadlock:</b> A situation in a multiprogramming system where two or more "
    "processes are permanently blocked, each waiting for a resource that is held by "
    "another process in the set. No process in the set can make progress — "
    "they are all stuck waiting forever. "
    "Deadlock is a <b>permanent blocking</b> condition (unlike starvation, which is "
    "indefinite but not necessarily permanent). "
    "Classic analogy: two cars meeting on a one-lane bridge — neither can advance without "
    "the other reversing, and neither is willing to reverse."
)

en.section("System Model")
en.body(
    "A system consists of a finite number of resources distributed among competing processes. "
    "Resources are classified into types: CPU cycles, memory space, I/O devices, semaphores, files."
)
en.info_table(
    ["Resource Concept", "Description"],
    [
        [
            "Resource Types",
            "Each resource type R(i) has W(i) identical instances. "
            "Example: 2 printers = one resource type with 2 instances.",
        ],
        [
            "Resource Usage Sequence",
            "A process must: (1) <b>Request</b> the resource, "
            "(2) <b>Use</b> the resource, (3) <b>Release</b> the resource.",
        ],
        [
            "Blocking on Request",
            "If no instance is available when a process requests, the process must wait "
            "until a resource instance is released.",
        ],
        [
            "Preemptable Resources",
            "Can be forcibly taken away without harm (e.g., CPU, memory with swapping). "
            "Deadlock rarely involves preemptable resources.",
        ],
        [
            "Non-preemptable Resources",
            "Cannot be taken away without causing failure (e.g., printers mid-job, CD writers). "
            "Deadlocks mostly involve non-preemptable resources.",
        ],
    ],
)

en.tip(
    "Deadlock involves ONLY non-preemptable resources. "
    "Preemptable resources can always be reclaimed by the OS, preventing deadlock."
)
en.br()

# =============================================================================
#  3.2  NECESSARY CONDITIONS FOR DEADLOCK
# =============================================================================
en.chap_box("3.2  Necessary Conditions for Deadlock")

en.section("Coffman's Four Necessary Conditions (1971)")
en.definition(
    "<b>Coffman's Conditions:</b> Deadlock can occur if and only if ALL FOUR of the "
    "following conditions hold simultaneously. If even one condition is absent, "
    "deadlock cannot occur. These conditions were identified by Coffman, Elphick, "
    "and Shoshani in 1971 and form the theoretical foundation for all deadlock handling."
)

en.info_table(
    ["Condition", "Definition", "Example"],
    [
        [
            "1. Mutual Exclusion",
            "At least one resource must be held in a non-shareable mode — "
            "only one process can use the resource at a time. "
            "If another process requests that resource, it must wait.",
            "A printer can only print one job at a time. "
            "A mutex semaphore can only be held by one process.",
        ],
        [
            "2. Hold and Wait",
            "A process must be holding at least one resource AND simultaneously "
            "waiting to acquire additional resources currently held by other processes.",
            "P1 holds resource R1 and waits for R2. " "P2 holds R2 and waits for R1.",
        ],
        [
            "3. No Preemption",
            "Resources cannot be forcibly taken from a process. "
            "A resource can only be released voluntarily by the process holding it, "
            "after that process has completed its task.",
            "OS cannot forcibly take a printer from a process mid-print. "
            "A lock cannot be forcibly released from another process.",
        ],
        [
            "4. Circular Wait",
            "There must exist a set of waiting processes {P0, P1, ..., Pn} such that "
            "P0 is waiting for a resource held by P1, "
            "P1 is waiting for a resource held by P2, ..., "
            "Pn is waiting for a resource held by P0.",
            "P0 waits for P1's resource, P1 waits for P2's resource, "
            "P2 waits for P0's resource — a cycle.",
        ],
    ],
)

en.warning(
    "ALL FOUR conditions must hold simultaneously for deadlock to occur. "
    "Deadlock prevention works by ensuring at least one condition can NEVER hold. "
    "This is the key insight for deadlock prevention strategies."
)

# State machine showing deadlock cycle
sm_dl = ed.StateMachine(
    width=en.CW * 0.72,
    height=200,
    theme=diag_theme,
    caption="Fig 3.1: Circular wait — the fourth condition shown as a process cycle",
)
sm_dl.state("p0", "P0\n(holds R0)", x=100, y=100, initial=False)
sm_dl.state("p1", "P1\n(holds R1)", x=280, y=40)
sm_dl.state("p2", "P2\n(holds R2)", x=460, y=100)
sm_dl.state("p3", "P3\n(holds R3)", x=280, y=175)
sm_dl.transition("p0", "p1", label="waits for R1")
sm_dl.transition("p1", "p2", label="waits for R2")
sm_dl.transition("p2", "p3", label="waits for R3")
sm_dl.transition("p3", "p0", label="waits for R0")
en.story.extend(sm_dl.as_flowable())
en.br()

# =============================================================================
#  3.3  RESOURCE ALLOCATION GRAPH (RAG)
# =============================================================================
en.chap_box("3.3  Resource Allocation Graph (RAG)")

en.section("RAG — Definition and Notation")
en.definition(
    "<b>Resource Allocation Graph (RAG):</b> A directed graph used to precisely describe "
    "the state of resource allocation in a system and to detect deadlock. "
    "Proposed by Holt (1972). "
    "<b>Vertices:</b> Two types — Process nodes (circles) and Resource nodes (rectangles). "
    "Each dot inside a rectangle represents one instance of that resource. "
    "<b>Edges:</b> Two types — "
    "<b>Request edge</b> (P → R): Process P is requesting/waiting for resource R. "
    "<b>Assignment edge</b> (R → P): An instance of resource R is assigned to process P."
)

en.section("RAG Rules for Deadlock Detection")
en.info_table(
    ["RAG Scenario", "Conclusion"],
    [
        [
            "No cycle in RAG",
            "No deadlock exists. System is in a safe state.",
        ],
        [
            "Cycle exists AND each resource type has exactly ONE instance",
            "DEADLOCK EXISTS. A cycle is both necessary and sufficient for deadlock.",
        ],
        [
            "Cycle exists AND resource types have MULTIPLE instances",
            "Deadlock MAY exist. Need further analysis (e.g., Banker's Algorithm). "
            "The cycle is necessary but not sufficient.",
        ],
    ],
)

en.section("RAG Example — Deadlock Case")
en.body(
    "Three processes P1, P2, P3. Three resource types R1 (1 instance), "
    "R2 (2 instances), R3 (1 instance). "
    "Assignments: R1→P1, R2→P1, R2→P2, R3→P3. "
    "Requests: P1→R2 (waiting), P2→R3 (waiting), P3→R1 (waiting)."
)

net_rag = ed.NetworkDiagram(
    width=en.CW,
    height=350,
    theme=diag_theme,
    caption="Fig 3.2: RAG showing a deadlock — cycle P1→R2→P2→R3→P3→R1→P1",
)
net_rag.node("p1", "Process P1", x=245, y=280, kind="server")
net_rag.node("r2", "Resource R2\n[2 instances]", x=380, y=200, kind="database", label_pos="right")
net_rag.node("p2", "Process P2", x=380, y=100, kind="server")
net_rag.node("r3", "Resource R3\n[1 instance]", x=245, y=40, kind="database")
net_rag.node("p3", "Process P3", x=110, y=100, kind="server")
net_rag.node("r1", "Resource R1\n[1 instance]", x=110, y=200, kind="database", label_pos="left")
net_rag.link("r1", "p1", label="assigned")
net_rag.link("r2", "p1", label="assigned")
net_rag.link("p1", "r2", label="requests")
net_rag.link("r2", "p2", label="assigned")
net_rag.link("p2", "r3", label="requests")
net_rag.link("r3", "p3", label="assigned")
net_rag.link("p3", "r1", label="requests")
en.story.extend(net_rag.as_flowable())

en.section("RAG Example — No Deadlock (Cycle but Multiple Instances)")
en.body(
    "A cycle in a RAG does NOT guarantee deadlock when resource types have multiple instances. "
    "If some process outside the cycle can complete and release resources, "
    "the cycle can be broken. "
    "Example: R2 has 2 instances. P3 holds one instance and is not in any cycle. "
    "P3 can complete → release R2 → P1 or P2 can proceed → cycle breaks → no deadlock."
)
en.br()

# =============================================================================
#  3.4  DEADLOCK PREVENTION
# =============================================================================
en.chap_box("3.4  Deadlock Prevention")

en.section("Strategy: Ensure at Least One Condition Cannot Hold")
en.definition(
    "<b>Deadlock Prevention:</b> A set of methods that ensure at least one of the "
    "four necessary conditions for deadlock can never hold. "
    "By invalidating one condition system-wide, deadlock becomes structurally impossible. "
    "Prevention is the most conservative approach — it restricts how processes request resources, "
    "which may reduce system efficiency or throughput."
)

en.info_table(
    ["Condition to Attack", "Prevention Method", "How It Works", "Drawbacks"],
    [
        [
            "1. Mutual Exclusion",
            "Make resources shareable",
            "For shareable resources (read-only files, counters), allow simultaneous access. "
            "Deadlock cannot arise from shared resources. "
            "Some resources are inherently non-shareable (printers, locks) — cannot always apply.",
            "Not applicable to all resources. Cannot eliminate mutex from critical sections.",
        ],
        [
            "2. Hold and Wait",
            "Request all resources at once (or release before requesting more)",
            "Method A: Process must request ALL resources it needs before starting. "
            "Granted only if ALL are available simultaneously. "
            "Method B: Process must release ALL held resources before requesting new ones.",
            "Low resource utilization (resources held but unused). "
            "Starvation possible — a process needing many resources may wait indefinitely.",
        ],
        [
            "3. No Preemption",
            "Allow preemption of resources",
            "If a process holding resources requests another that is unavailable: "
            "Option A: Preempt ALL resources held by the waiting process — add to available pool. "
            "Option B: Preempt resources from other waiting processes if they have what's needed. "
            "Process restarts only when ALL resources (old + new) are available.",
            "Only works for resources whose state can be saved/restored (CPU, memory). "
            "Difficult for printers, disk writes. High overhead from rollbacks.",
        ],
        [
            "4. Circular Wait",
            "Total ordering of resource types",
            "Assign a unique integer to each resource type. "
            "Processes must request resources in strictly increasing order of enumeration. "
            "Example: if printer=1, scanner=2, disk=3 — a process may request printer then disk, "
            "but never disk first then printer.",
            "Difficult to order resources in practice. "
            "May force processes to request resources they don't need just to maintain order.",
        ],
    ],
)

en.exam(
    "Most commonly asked: Explain deadlock prevention by attacking the circular wait condition. "
    "Answer: Assign a unique total ordering to all resource types. "
    "All processes must request resources in increasing order of their assigned numbers. "
    "This makes a circular wait structurally impossible."
)
en.br()

# =============================================================================
#  3.5  DEADLOCK AVOIDANCE — BANKER'S ALGORITHM
# =============================================================================
en.chap_box("3.5  Deadlock Avoidance — Banker's Algorithm")

en.section("Safe State — The Core Concept")
en.definition(
    "<b>Safe State:</b> A system state is safe if there exists a <b>safe sequence</b> — "
    "an ordering of all processes such that for each process Pi in the sequence, "
    "the resources Pi still needs can be satisfied by the currently available resources "
    "PLUS the resources held by all processes Pj where j < i (i.e., Pj has already finished). "
    "In a safe state, deadlock is impossible because every process can eventually complete. "
    "In an unsafe state, deadlock is possible (but not guaranteed). "
    "<b>Deadlock avoidance:</b> Keep the system always in a safe state by only granting "
    "resource requests that keep the system safe."
)

en.info_table(
    ["State", "Property"],
    [
        [
            "Safe State",
            "A safe sequence exists. All processes can eventually complete. No deadlock possible.",
        ],
        [
            "Unsafe State",
            "No safe sequence exists. Deadlock is possible (but processes may still complete by luck).",
        ],
        [
            "Deadlock State",
            "A subset of processes are permanently blocked. System cannot progress without intervention.",
        ],
    ],
)

# Diagram: relationship between safe, unsafe, deadlock
net_safe = ed.NetworkDiagram(
    width=en.CW,
    height=160,
    theme=diag_theme,
    caption="Fig 3.3: Safe ⊂ Unsafe ⊂ All states — avoidance keeps system in safe region",
)
net_safe.node("safe", "SAFE\nStates", x=125, y=80, kind="generic")
net_safe.node("unsafe", "UNSAFE\nStates", x=245, y=80, kind="generic")
net_safe.node("dl", "DEADLOCK\nStates", x=365, y=80, kind="firewall")
net_safe.link("safe", "unsafe", label="resource\ngrant may move")
net_safe.link("unsafe", "dl", label="processes\nblock")
en.story.extend(net_safe.as_flowable())

en.section("Banker's Algorithm — Data Structures")
en.definition(
    "<b>Banker's Algorithm (Dijkstra, 1965):</b> A deadlock avoidance algorithm for systems "
    "where each process declares its MAXIMUM resource needs in advance. "
    "Named after a bank that ensures it never allocates cash such that it can no longer "
    "satisfy all customers. The OS acts like the banker — it only approves a resource "
    "request if the resulting state remains safe."
)

en.body(
    "For n processes and m resource types, the algorithm uses these data structures:"
)
en.info_table(
    ["Structure", "Size", "Meaning"],
    [
        [
            "Available[m]",
            "Vector of length m",
            "Available[j] = number of available instances of resource type Rj.",
        ],
        [
            "Max[n][m]",
            "n×m matrix",
            "Max[i][j] = maximum number of instances of Rj that process Pi may request.",
        ],
        [
            "Allocation[n][m]",
            "n×m matrix",
            "Allocation[i][j] = number of instances of Rj currently allocated to Pi.",
        ],
        [
            "Need[n][m]",
            "n×m matrix",
            "Need[i][j] = Max[i][j] − Allocation[i][j]. Remaining resource need of Pi.",
        ],
    ],
)

en.section("Safety Algorithm (Check if State is Safe)")
en.code_block(
    """/* Safety Algorithm -- O(n^2 * m) */

Work[m]   = Available[m];          /* copy of available resources */
Finish[n] = {false, false, ..., false};  /* all processes unfinished */

/* Repeat until no more processes can be added to sequence */
while (some Finish[i] == false) {
    /* Find process Pi such that:
       (a) Finish[i] == false  (not yet finished)
       (b) Need[i] <= Work     (its remaining need can be met) */
    
    if (such Pi found) {
        Work   = Work + Allocation[i];  /* Pi finishes, releases its resources */
        Finish[i] = true;               /* mark Pi as finished */
        /* Add Pi to safe sequence */
    } else {
        break;  /* no such process found -- system is UNSAFE */
    }
}

if (all Finish[i] == true)
    return SAFE;   /* safe sequence found */
else
    return UNSAFE; /* deadlock possible */""",
    lang="c",
)

en.section("Resource-Request Algorithm (Process Pi Requests Resources)")
en.code_block(
    """/* Resource-Request Algorithm for process Pi */
/* Request[i][m] = resource request vector for Pi */

/* Step 1: Check request does not exceed declared maximum */
if (Request[i] > Need[i])
    ERROR("Process exceeded maximum claim");

/* Step 2: Check request does not exceed available resources */
if (Request[i] > Available)
    Pi must WAIT (resources not available);

/* Step 3: Pretend to allocate -- temporarily update state */
Available    = Available - Request[i];
Allocation[i] = Allocation[i] + Request[i];
Need[i]       = Need[i] - Request[i];

/* Step 4: Run Safety Algorithm on new pretend state */
if (Safety_Algorithm() == SAFE) {
    GRANT the request;   /* new state is safe -- commit allocation */
} else {
    /* ROLLBACK: restore old state */
    Available    = Available + Request[i];
    Allocation[i] = Allocation[i] - Request[i];
    Need[i]       = Need[i] + Request[i];
    Pi must WAIT;        /* granting would lead to unsafe state */
}""",
    lang="c",
)

en.section("Banker's Algorithm — Worked Example")
en.body(
    "5 processes (P0–P4), 3 resource types: A (10 instances), B (5 instances), C (7 instances). "
    "Current snapshot at time T0:"
)
en.info_table(
    ["Process", "Allocation (A B C)", "Max (A B C)", "Need (A B C)"],
    [
        ["P0", "0  1  0", "7  5  3", "7  4  3"],
        ["P1", "2  0  0", "3  2  2", "1  2  2"],
        ["P2", "3  0  2", "9  0  2", "6  0  0"],
        ["P3", "2  1  1", "2  2  2", "0  1  1"],
        ["P4", "0  0  2", "4  3  3", "4  3  1"],
    ],
)
en.body(
    "Available = A:3, B:3, C:2  (Total − Sum of Allocation = [10,5,7] − [7,2,5] = [3,3,2])."
)
en.info_table(
    ["Step", "Work (A B C)", "Process Run", "Reason Need ≤ Work?", "Finish"],
    [
        [
            "1",
            "3  3  2",
            "P1",
            "Need[P1]=(1,2,2) ≤ (3,3,2) ✓",
            "Work=(3+2,3+0,2+0)=(5,3,2)",
        ],
        [
            "2",
            "5  3  2",
            "P3",
            "Need[P3]=(0,1,1) ≤ (5,3,2) ✓",
            "Work=(5+2,3+1,2+1)=(7,4,3)",
        ],
        [
            "3",
            "7  4  3",
            "P4",
            "Need[P4]=(4,3,1) ≤ (7,4,3) ✓",
            "Work=(7+0,4+0,3+2)=(7,4,5)",
        ],
        [
            "4",
            "7  4  5",
            "P0",
            "Need[P0]=(7,4,3) ≤ (7,4,5) ✓",
            "Work=(7+0,4+1,5+0)=(7,5,5)",
        ],
        [
            "5",
            "7  5  5",
            "P2",
            "Need[P2]=(6,0,0) ≤ (7,5,5) ✓",
            "Work=(7+3,5+0,5+2)=(10,5,7)",
        ],
    ],
)
en.tip(
    "Safe sequence: P1 → P3 → P4 → P0 → P2. "
    "The system is in a SAFE state. "
    "All Finish[i] = true at the end, confirming safety."
)

en.section("Banker's Algorithm — Request Example")
en.body(
    "Now suppose P1 requests (1, 0, 2). "
    "Step 1: Request (1,0,2) ≤ Need[P1] (1,2,2) ✓. "
    "Step 2: Request (1,0,2) ≤ Available (3,3,2) ✓. "
    "Step 3: Pretend allocation — Available=(2,3,0), Allocation[P1]=(3,0,2), Need[P1]=(0,2,0). "
    "Step 4: Run Safety — safe sequence P1,P3,P4,P0,P2 still exists. "
    "Result: GRANT the request."
)

en.info_table(
    ["Algorithm", "Requirement", "Pros", "Cons"],
    [
        [
            "Banker's Algorithm",
            "Processes declare maximum resource needs in advance",
            "Never enters unsafe state. Deadlock impossible.",
            "Processes rarely know maximum needs in advance. "
            "Overhead of safety check per request. Not used in practice for full systems.",
        ],
    ],
)
en.br()

# =============================================================================
#  3.6  DEADLOCK DETECTION
# =============================================================================
en.chap_box("3.6  Deadlock Detection")

en.section("When to Use Detection Instead of Prevention/Avoidance")
en.definition(
    "<b>Deadlock Detection:</b> Allow the system to enter a deadlocked state, "
    "then detect it and recover. Used when the overhead of prevention/avoidance is "
    "too high, or when deadlock is expected to be rare. "
    "The OS must provide: (1) an algorithm to examine the state and determine if deadlock has occurred, "
    "(2) a recovery scheme to resolve the deadlock."
)

en.section("Detection — Single Instance of Each Resource Type")
en.definition(
    "<b>Wait-For Graph:</b> A simplified version of the RAG for single-instance resources. "
    "Obtained by collapsing resource nodes — only process nodes remain. "
    "An edge Pi → Pj exists if Pi is waiting for a resource held by Pj. "
    "<b>Deadlock exists if and only if the wait-for graph contains a cycle.</b> "
    "The OS periodically runs a cycle-detection algorithm (O(n²)) on this graph."
)

net_wfg = ed.NetworkDiagram(
    width=en.CW,
    height=240,
    theme=diag_theme,
    caption="Fig 3.4: Wait-for graph — cycle P1→P2→P3→P1 indicates deadlock",
)
net_wfg.node("p1", "Process P1", x=145, y=120, kind="server")
net_wfg.node("p2", "Process P2", x=245, y=40, kind="server")
net_wfg.node("p3", "Process P3", x=345, y=120, kind="server")
net_wfg.node("p4", "Process P4", x=245, y=200, kind="server")
net_wfg.link("p1", "p2", label="waits for")
net_wfg.link("p2", "p3", label="waits for")
net_wfg.link("p3", "p1", label="waits for")
net_wfg.link("p4", "p1", label="waits for")
en.story.extend(net_wfg.as_flowable())
en.body(
    "P1, P2, P3 are deadlocked (cycle). P4 is also blocked waiting for P1, "
    "but P4 is not part of the deadlock cycle itself."
)

en.section("Detection — Multiple Instances of Each Resource Type")
en.definition(
    "<b>Detection Algorithm for Multiple Instances:</b> Similar in structure to the Banker's "
    "Safety Algorithm but uses the ACTUAL current allocation (not maximum needs). "
    "Uses: Available, Allocation, and Request (= current actual requests, not maximum need)."
)
en.code_block(
    """/* Deadlock Detection Algorithm -- Multiple Resource Instances */
/* O(n^2 * m) */

Work[m]   = Available[m];
Finish[n] = {false if Allocation[i] != 0, else true};
/* (A process with no resources allocated is assumed to not be deadlocked) */

while (some Finish[i] == false) {
    /* Find Pi such that:
       (a) Finish[i] == false
       (b) Request[i] <= Work   (Pi's current requests can be satisfied) */
    
    if (such Pi found) {
        Work   = Work + Allocation[i];  /* Pi completes, returns resources */
        Finish[i] = true;
    } else {
        break;
    }
}

/* Any process with Finish[i] == false is DEADLOCKED */
if (some Finish[i] == false)
    report deadlock involving all such processes;""",
    lang="c",
)

en.section("When and How Often to Run the Detection Algorithm?")
en.info_table(
    ["Frequency Strategy", "Pros", "Cons"],
    [
        [
            "Run every time a request cannot be granted immediately",
            "Identifies exactly which process caused the deadlock. Early detection.",
            "High overhead if requests are frequent and many are blocked.",
        ],
        [
            "Run at fixed time intervals (e.g., every hour)",
            "Low overhead. Predictable cost.",
            "By the time deadlock is detected, many processes may have joined. Hard to identify cause.",
        ],
        [
            "Run when CPU utilization drops below threshold (e.g., 40%)",
            "Heuristic — deadlock often manifests as low CPU utilization.",
            "Low CPU may have other causes (I/O-bound workload, idle system).",
        ],
    ],
)
en.br()

# =============================================================================
#  3.7  DEADLOCK RECOVERY
# =============================================================================
en.chap_box("3.7  Deadlock Recovery")

en.section("Recovery Strategies")
en.definition(
    "<b>Deadlock Recovery:</b> Once a deadlock is detected, the OS must break it. "
    "There are two main approaches: (1) <b>Process Termination</b> — abort one or more processes "
    "to break the circular wait. (2) <b>Resource Preemption</b> — forcibly take resources from "
    "some processes and give them to others. "
    "Both approaches have costs and trade-offs."
)

en.section("Method 1: Process Termination")
en.info_table(
    ["Option", "Description", "Pros", "Cons"],
    [
        [
            "Abort ALL deadlocked processes",
            "Terminate every process involved in the deadlock. "
            "All held resources become available.",
            "Guaranteed to break deadlock immediately.",
            "Very expensive — all work done by all aborted processes is lost.",
        ],
        [
            "Abort ONE process at a time",
            "Terminate one deadlocked process, run detection algorithm again. "
            "Repeat until deadlock is resolved.",
            "Less wasteful — stop as soon as deadlock is broken.",
            "High overhead — must re-run detection algorithm after each abort.",
        ],
    ],
)
en.body(
    "When aborting one process at a time, the OS uses these criteria to choose the victim:"
)
en.bullet(
    [
        "<b>Process priority:</b> Abort the lowest-priority process first.",
        "<b>CPU time used:</b> Abort the process that has used the least CPU time (least work lost).",
        "<b>Resources held:</b> Abort the process holding the most resources (breaks deadlock fastest).",
        "<b>Resources needed:</b> Abort the process needing the most resources to complete.",
        "<b>Number of processes to abort:</b> Minimize the number of processes that need to be terminated.",
        "<b>Interactive vs batch:</b> Prefer aborting batch processes over interactive ones.",
    ]
)

en.section("Method 2: Resource Preemption")
en.info_table(
    ["Issue", "Consideration"],
    [
        [
            "Selecting a victim",
            "Choose which process to preempt resources from. "
            "Minimize cost — consider time used, resources held, number of rollbacks needed.",
        ],
        [
            "Rollback",
            "Cannot just take a resource mid-use. Process must be rolled back to a safe state "
            "where it did not yet hold the preempted resource. "
            "Requires checkpointing (periodic saving of process state).",
        ],
        [
            "Starvation",
            "If the same process is always chosen as victim, it may starve. "
            "Solution: include number of rollbacks as a cost factor — "
            "after a process has been victimized K times, it must not be victimized again.",
        ],
    ],
)

fc_recovery = ed.Flowchart(
    width=en.CW * 0.70,
    height=300,
    theme=diag_theme,
    caption="Fig 3.5: Deadlock recovery decision flowchart",
)
fc_recovery.terminal("start", "Deadlock Detected")
fc_recovery.decision("method", "Recovery Method?")
fc_recovery.process("abort_all", "Abort ALL\ndeadlocked processes")
fc_recovery.process("select_victim", "Select Victim Process\n(min cost)")
fc_recovery.process("preempt", "Preempt Resources\nfrom Victim")
fc_recovery.process("rollback", "Rollback Victim\nto Safe Checkpoint")
fc_recovery.terminal("resolved", "Deadlock Resolved")
fc_recovery.edge("start", "method")
fc_recovery.edge("method", "abort_all", branch="abort all")
fc_recovery.edge("method", "select_victim", branch="preempt")
fc_recovery.edge("abort_all", "resolved")
fc_recovery.edge("select_victim", "preempt")
fc_recovery.edge("preempt", "rollback")
fc_recovery.edge("rollback", "resolved")
en.story.extend(fc_recovery.as_flowable())

en.section("Deadlock Handling — Strategy Comparison")
en.info_table(
    ["Strategy", "Approach", "Cost", "Used In"],
    [
        [
            "Prevention",
            "Ensure one of four conditions never holds system-wide.",
            "Low runtime overhead. High resource waste (conservative).",
            "Embedded RTOS, safety-critical systems.",
        ],
        [
            "Avoidance",
            "Banker's Algorithm — only grant safe requests.",
            "Medium overhead per request. Requires max declaration.",
            "Rarely used in practice — assumptions too strong.",
        ],
        [
            "Detection + Recovery",
            "Allow deadlock; detect it; break it.",
            "Low normal overhead. High recovery cost when deadlock occurs.",
            "Most databases, some general-purpose OS (as fallback).",
        ],
        [
            "Ignore (Ostrich Algorithm)",
            "Pretend deadlock never happens. Reboot if stuck.",
            "Zero overhead. Correctness not guaranteed.",
            "Windows, many Linux systems (deadlock considered rare).",
        ],
    ],
)
en.br()

# =============================================================================
#  PART DIVIDER
# =============================================================================
en.part_box("UNIT III — PART B: MEMORY MANAGEMENT")

# =============================================================================
#  3.8  MEMORY MANAGEMENT INTRODUCTION
# =============================================================================
en.chap_box("3.8  Introduction to Memory Management")

en.section("Why Memory Management?")
en.definition(
    "<b>Memory Management:</b> The OS subsystem responsible for managing the hierarchy "
    "of memory in a computer system. Its goals are: "
    "(1) <b>Protection:</b> Ensure one process cannot access another's memory. "
    "(2) <b>Relocation:</b> Allow processes to be loaded anywhere in physical memory. "
    "(3) <b>Sharing:</b> Allow multiple processes to share common code/data safely. "
    "(4) <b>Logical Organization:</b> Organize memory in logical units (segments, pages). "
    "(5) <b>Physical Organization:</b> Manage the transfer of information between main memory and secondary storage."
)

en.section("Memory Hierarchy")
stack_mem = ed.LayeredStack(
    width=en.CW * 0.55,
    height=230,
    theme=diag_theme,
    caption="Fig 3.6: Memory hierarchy — speed vs capacity trade-off",
)
stack_mem.layer("CPU Registers", sublabel="<1 ns  |  ~1 KB  |  Fastest, most expensive")
stack_mem.layer("Cache (L1/L2/L3)", sublabel="1–10 ns  |  1–32 MB  |  SRAM")
stack_mem.layer("Main Memory (RAM)", sublabel="50–100 ns  |  4–64 GB  |  DRAM")
stack_mem.layer("SSD / Flash Storage", sublabel="0.1 ms  |  128 GB–4 TB")
stack_mem.layer(
    "HDD / Magnetic Disk", sublabel="5–15 ms  |  1–20 TB  |  Slowest, cheapest"
)
en.story.extend(stack_mem.as_flowable())

en.section("Memory Terminology")
en.info_table(
    ["Term", "Definition"],
    [
        [
            "Address Space",
            "The range of addresses a process can use. Logical address space = set of all logical addresses generated by a program.",
        ],
        [
            "Physical Memory",
            "The actual RAM chips in the computer. Accessed via physical addresses.",
        ],
        [
            "Logical (Virtual) Address",
            "The address generated by the CPU — as seen by the process. Also called virtual address.",
        ],
        [
            "Physical Address",
            "The actual address in RAM — what the memory unit sees. May differ from logical address at run time.",
        ],
        [
            "Memory Map",
            "The mapping from logical addresses to physical addresses, maintained by the OS and hardware MMU.",
        ],
        [
            "Fragmentation",
            "Wasted memory space. Internal fragmentation: wasted space inside an allocated partition. "
            "External fragmentation: free memory scattered in small non-contiguous chunks.",
        ],
    ],
)
en.br()

# =============================================================================
#  3.9  ADDRESS BINDING
# =============================================================================
en.chap_box("3.9  Address Binding")

en.section("What is Address Binding?")
en.definition(
    "<b>Address Binding:</b> The process of mapping instructions and data to actual memory addresses. "
    "A program typically uses symbolic addresses in source code (variable names). "
    "These are bound (mapped) to actual numeric addresses at different stages. "
    "The binding can happen at three different times in a program's lifecycle."
)

en.info_table(
    ["Binding Time", "When It Occurs", "Description", "Flexibility"],
    [
        [
            "Compile-Time Binding",
            "During compilation",
            "If the memory location of the process is KNOWN at compile time, "
            "the compiler generates absolute (physical) addresses directly in the code. "
            "The program must be loaded at that exact address. "
            "If start address changes, the program must be recompiled.",
            "None — process must always load at same address. "
            "Example: Early DOS programs, .COM files.",
        ],
        [
            "Load-Time Binding",
            "When program is loaded into memory by OS loader",
            "Compiler generates <b>relocatable code</b> using relative addresses. "
            "The loader converts these to absolute addresses at load time "
            "based on where in physical memory the program is placed. "
            "Program can be loaded anywhere — but cannot be moved after loading.",
            "Medium — can be loaded at any address, but position fixed after loading.",
        ],
        [
            "Execution-Time Binding\n(Runtime Binding)",
            "During execution, dynamically by hardware",
            "Process can be moved during execution — the hardware MMU translates "
            "logical addresses to physical addresses dynamically at every memory access. "
            "The process uses logical addresses; the MMU adds the base register value. "
            "Requires hardware support (base and limit registers, MMU).",
            "Maximum — process can be swapped, compacted, or moved at any time. "
            "Used by all modern OSes.",
        ],
    ],
)

fc_binding = ed.Flowchart(
    width=en.CW,
    height=280,
    theme=diag_theme,
    caption="Fig 3.7: Address binding stages from source code to execution",
)
fc_binding.terminal("src", "Source Code\n(Symbolic names: int x, label L)")
fc_binding.process("compile", "Compiler\n(Translates to relocatable object code)")
fc_binding.process(
    "link", "Linker / Assembler\n(Combines modules, resolves external refs)"
)
fc_binding.process(
    "load", "Loader / OS\n(Loads into physical memory at a chosen address)"
)
fc_binding.terminal(
    "exec", "CPU Execution\n(MMU translates logical → physical at runtime)"
)
fc_binding.edge("src", "compile")
fc_binding.edge("compile", "link")
fc_binding.edge("link", "load")
fc_binding.edge("load", "exec")
en.story.extend(fc_binding.as_flowable())
en.br()

# =============================================================================
#  3.10  LOGICAL VS PHYSICAL ADDRESS, MMU
# =============================================================================
en.chap_box("3.10  Logical vs Physical Address & MMU")

en.section("Logical Address vs Physical Address")
en.definition(
    "<b>Logical Address:</b> The address generated by the CPU during program execution. "
    "Also called a <b>virtual address</b>. The program only ever sees logical addresses — "
    "it has no knowledge of where in physical RAM it is located. "
    "<b>Physical Address:</b> The actual address of a location in physical main memory (RAM). "
    "This is the address that appears on the memory address bus and selects the RAM location. "
    "<b>Key difference:</b> At compile-time and load-time binding, logical and physical addresses "
    "are the same. At execution-time binding, they differ — the MMU translates."
)

en.info_table(
    ["Property", "Logical Address", "Physical Address"],
    [
        [
            "Generated by",
            "CPU (program counter, data accesses)",
            "Memory Management Unit (MMU)",
        ],
        ["Seen by", "Process / programmer", "RAM hardware"],
        ["Range", "0 to max of logical address space", "0 to max of physical RAM"],
        [
            "Fixed?",
            "Fixed by program structure",
            "Varies — depends on where OS loaded process",
        ],
        [
            "Binding time",
            "Exists at all times",
            "Only exists at execution-time binding",
        ],
    ],
)

en.section("Memory Management Unit (MMU)")
en.definition(
    "<b>MMU (Memory Management Unit):</b> A hardware device (often on-chip with the CPU) "
    "that maps logical addresses to physical addresses at runtime. "
    "Every memory access by the CPU goes through the MMU. "
    "The simplest MMU uses a <b>relocation register</b> (base register): "
    "Physical Address = Logical Address + Relocation Register (base). "
    "This allows the OS to place a process anywhere in RAM — just update the base register."
)

seq_mmu = ed.SequenceDiagram(
    width=en.CW,
    height=220,
    theme=diag_theme,
    caption="Fig 3.8: MMU address translation — logical to physical",
)
seq_mmu.actor("cpu", "CPU")
seq_mmu.actor("mmu", "MMU\n(Hardware)")
seq_mmu.actor("ram", "Physical RAM")
seq_mmu.message("cpu", "mmu", "Logical address: 346", arrow="solid")
seq_mmu.activate("mmu")
seq_mmu.message(
    "mmu",
    "mmu",
    "Physical = 346 + base(14000) = 14346\nCheck: 346 &lt; limit(3000) ✓",
    arrow="solid",
)
seq_mmu.message("mmu", "ram", "Physical address: 14346", arrow="solid")
seq_mmu.activate("ram")
seq_mmu.message("ram", "mmu", "Data at address 14346", arrow="dashed")
seq_mmu.deactivate("ram")
seq_mmu.message("mmu", "cpu", "Return data to CPU", arrow="dashed")
seq_mmu.deactivate("mmu")
en.story.extend(seq_mmu.as_flowable())

en.section("Base and Limit Registers")
en.definition(
    "<b>Base Register:</b> Holds the smallest legal physical memory address for the process. "
    "<b>Limit Register:</b> Contains the size (length) of the process's address space. "
    "<b>Address validation:</b> If logical address ≥ limit → trap to OS (memory protection violation). "
    "Otherwise, physical address = base + logical address. "
    "These registers are loaded by the OS during context switch — each process has its own base/limit values. "
    "User mode programs cannot modify base/limit registers (privileged instructions)."
)

en.formula_block(
    r"\text{Physical Address} = \text{Base Register} + \text{Logical Address}"
)
en.formula_block(r"\text{Valid if: Logical Address} < \text{Limit Register}")

en.note(
    "The base-limit register scheme is the foundation of contiguous memory allocation. "
    "Modern systems use paging and segmentation (Unit IV) which extend this concept "
    "to non-contiguous allocation with page tables instead of a single base register."
)
en.br()

# =============================================================================
#  3.11  CONTIGUOUS MEMORY ALLOCATION
# =============================================================================
en.chap_box("3.11  Contiguous Memory Allocation")

en.section("What is Contiguous Allocation?")
en.definition(
    "<b>Contiguous Memory Allocation:</b> Each process is allocated a single, "
    "contiguous (uninterrupted) block of physical memory. "
    "The process occupies one region of RAM from start address to end address with "
    "no gaps in between. The MMU's base+limit register scheme directly supports this. "
    "Simple to implement and manage, but suffers from fragmentation problems."
)

en.section("Single-Partition Allocation")
en.definition(
    "<b>Single-Partition Allocation:</b> One user process in memory at a time. "
    "Memory is divided into two regions: OS (resident in low memory at fixed address) "
    "and user process (occupies all remaining memory). "
    "The OS is protected by a fence register — any user access below the fence causes a trap. "
    "Simple but poor CPU utilization — CPU idle during I/O operations. "
    "Used in early batch systems (MS-DOS style)."
)

stack_single = ed.LayeredStack(
    width=en.CW * 0.45,
    height=190,
    theme=diag_theme,
    caption="Fig 3.9: Single-partition allocation",
)
stack_single.layer("User Process", sublabel="One process at a time")
stack_single.divider()
stack_single.layer("OS Kernel", sublabel="Fixed low-memory region")
en.story.extend(stack_single.as_flowable())

en.section("Multiple-Partition Allocation")
en.definition(
    "<b>Multiple-Partition Allocation:</b> Memory is divided into multiple partitions "
    "so that several processes can reside in memory simultaneously (multiprogramming). "
    "Two approaches: <b>Fixed Partitioning</b> (partitions of fixed sizes decided at boot) "
    "and <b>Variable Partitioning</b> (partitions created dynamically to fit each process exactly)."
)

en.section("Fixed Partitioning")
en.info_table(
    ["Property", "Fixed Partitioning"],
    [
        [
            "Partition sizes",
            "Decided at system initialization time. Cannot change while system runs.",
        ],
        [
            "Degree of multiprogramming",
            "Limited to number of partitions (e.g., 4 partitions = max 4 processes in memory).",
        ],
        [
            "Internal fragmentation",
            "Wasted space INSIDE a partition — process smaller than partition. "
            "Example: 3 KB process in 5 KB partition → 2 KB wasted internally.",
        ],
        [
            "External fragmentation",
            "Does not exist — partition slots are predefined and process fits in one slot.",
        ],
        [
            "Implementation",
            "Very simple. Used in IBM OS/360 MFT (Multiprogramming with Fixed Tasks).",
        ],
    ],
)

en.section("Variable (Dynamic) Partitioning")
en.definition(
    "<b>Variable Partitioning:</b> Partitions are created dynamically as processes arrive. "
    "Each process gets a partition of EXACTLY the size it needs. "
    "Initially, all memory is one large free block (hole). "
    "As processes are allocated and freed, holes of various sizes appear throughout memory. "
    "The OS maintains a list of free holes and searches for a fit when a new process arrives."
)
en.info_table(
    ["Property", "Variable Partitioning"],
    [
        [
            "Internal fragmentation",
            "None — partition matches process size exactly.",
        ],
        [
            "External fragmentation",
            "Significant — over time, free memory is scattered in many small non-contiguous holes. "
            "Total free memory may be sufficient but no single hole is large enough.",
        ],
        [
            "Compaction",
            "Solution to external fragmentation: shuffle all processes to one end of memory, "
            "merge all free space into one large hole. Expensive — requires moving live processes. "
            "Only possible with execution-time (runtime) binding.",
        ],
        [
            "Coalescing",
            "When a process terminates, if adjacent partitions are also free, "
            "merge them into one larger hole automatically.",
        ],
    ],
)

# Visual showing memory states
stack_var = ed.LayeredStack(
    width=en.CW * 0.40,
    height=270,
    theme=diag_theme,
    caption="Variable partitioning: external fragmentation",
)
stack_var.layer("P3  (200 KB)", sublabel="")
stack_var.layer("FREE  (80 KB)", sublabel="← hole")
stack_var.layer("P2  (120 KB)", sublabel="")
stack_var.layer("FREE  (40 KB)", sublabel="← hole")
stack_var.layer("P4  (160 KB)", sublabel="")
stack_var.layer("OS  (100 KB)", sublabel="")
en.story.extend(stack_var.as_flowable())
en.br()

# =============================================================================
#  3.12  PARTITION PLACEMENT STRATEGIES
# =============================================================================
en.chap_box("3.12  Partition Placement Strategies")

en.section("Overview of Hole Selection Strategies")
en.definition(
    "When a process needs memory and multiple free holes are available, "
    "which hole should the OS choose? Three classical strategies exist. "
    "The OS maintains a list of free holes (sorted by address or size depending on strategy). "
    "The choice affects performance, fragmentation, and search time."
)

en.info_table(
    ["Strategy", "Selection Rule", "Implementation", "Produces"],
    [
        [
            "First Fit",
            "Allocate the FIRST hole that is large enough. "
            "Search from the beginning of the hole list (or from where last search left off — next fit variant).",
            "Unsorted list. Search stops at first fit. O(n) average but early termination.",
            "Fast allocation. Leaves large holes at end of memory. "
            "Creates small unusable fragments at the beginning over time.",
        ],
        [
            "Best Fit",
            "Allocate the SMALLEST hole that is large enough. "
            "Must search the entire hole list to find the smallest sufficient hole.",
            "Sort free list by size (ascending), or scan entire list. O(n).",
            "Minimizes wasted space in chosen hole. Produces many tiny leftover holes that may be too small to use. "
            "Worse external fragmentation overall.",
        ],
        [
            "Worst Fit",
            "Allocate the LARGEST hole available. " "Must search the entire hole list.",
            "Sort free list by size (descending), or scan entire list. O(n).",
            "Leftover fragment is as large as possible — more likely to be usable by a future process. "
            "But wastes large holes quickly. Generally performs worst in practice.",
        ],
    ],
)

en.section("Worked Example — First Fit, Best Fit, Worst Fit")
en.body(
    "Free holes (in order of address): 600 KB, 500 KB, 200 KB, 300 KB, 700 KB. "
    "Process requests in order: P1=212 KB, P2=417 KB, P3=112 KB, P4=426 KB."
)

en.info_table(
    [
        "Process",
        "Request",
        "First Fit (hole used)",
        "Best Fit (hole used)",
        "Worst Fit (hole used)",
    ],
    [
        [
            "P1",
            "212 KB",
            "600 KB hole → 388 KB left",
            "300 KB hole → 88 KB left",
            "700 KB hole → 488 KB left",
        ],
        [
            "P2",
            "417 KB",
            "500 KB hole → 83 KB left",
            "500 KB hole → 83 KB left",
            "600 KB hole → 183 KB left",
        ],
        [
            "P3",
            "112 KB",
            "388 KB leftover from P1 → 276 KB left",
            "200 KB hole → 88 KB left",
            "488 KB leftover from P1 → 376 KB left",
        ],
        [
            "P4",
            "426 KB",
            "500 KB hole (or 700 KB if no 500 left) — depends on order",
            "FAILS — no single hole ≥ 426 KB left (83 KB, 88 KB, 88 KB, 276 KB, 700 KB → 700 fits)",
            "500 KB hole → 74 KB left",
        ],
    ],
)

en.note(
    "First Fit and Best Fit are generally better than Worst Fit in terms of "
    "storage utilization and speed. Simulations show First Fit is best in speed; "
    "Best Fit produces the least wasted space on average in many workloads. "
    "In practice, First Fit is most commonly implemented."
)

en.section("Fragmentation — Summary")
en.info_table(
    ["Type", "Where", "Caused By", "Solution"],
    [
        [
            "Internal Fragmentation",
            "INSIDE an allocated partition",
            "Fixed partition larger than process size. "
            "Also occurs in paging (last page may not be full).",
            "Use variable-size partitions. Reduce page size (Unit IV trade-off).",
        ],
        [
            "External Fragmentation",
            "OUTSIDE allocated areas — in free space between partitions",
            "Variable partitioning over time creates scattered small holes. "
            "Total free space sufficient but non-contiguous.",
            "Compaction (expensive), Paging/Segmentation (Unit IV — eliminates it).",
        ],
    ],
)

en.formula_block(
    r"\text{50-percent rule: } \frac{1}{3} \text{ of memory wasted on average with First Fit}"
)
en.note(
    "The 50-percent rule states that given N allocated blocks, approximately 0.5N more blocks "
    "will be lost to fragmentation with First Fit. About 1/3 of all memory is unusable due to "
    "external fragmentation in variable partitioning. This motivates paging (Unit IV)."
)
en.br()

# =============================================================================
#  DEADLOCK & MEMORY — MASTER COMPARISON TABLES
# =============================================================================
en.chap_box("Unit III — Master Summary Tables")

en.section("Deadlock Handling Strategies — Quick Reference")
en.info_table(
    ["Method", "Core Idea", "Overhead", "Starvation?", "Used In"],
    [
        [
            "Prevention\n(Mutual Exclusion)",
            "Make resources shareable if possible",
            "None",
            "No",
            "Rarely (can't always share)",
        ],
        [
            "Prevention\n(Hold & Wait)",
            "Request all resources before start",
            "High waste",
            "Yes",
            "Simple batch systems",
        ],
        [
            "Prevention\n(No Preemption)",
            "Allow OS to forcibly reclaim resources",
            "High rollback cost",
            "Possible",
            "CPU registers, memory",
        ],
        [
            "Prevention\n(Circular Wait)",
            "Total ordering of resource types",
            "Low",
            "No",
            "OS kernel lock ordering",
        ],
        [
            "Avoidance\n(Banker's)",
            "Only grant safe requests",
            "Medium per request",
            "No",
            "Academic; rarely practical",
        ],
        [
            "Detection + Recovery",
            "Allow deadlock; detect; kill/preempt",
            "Periodic algorithm",
            "Possible if same victim chosen",
            "Databases, some OS",
        ],
        [
            "Ostrich Algorithm",
            "Ignore deadlock (rare in practice)",
            "None",
            "N/A",
            "Windows, Linux (reboot)",
        ],
    ],
)

en.section("Memory Allocation Strategies — Quick Reference")
en.info_table(
    ["Strategy", "Rule", "Internal Frag", "External Frag", "Speed"],
    [
        [
            "Single Partition",
            "One process, all remaining RAM",
            "Yes (unused RAM)",
            "No",
            "Instant",
        ],
        [
            "Fixed Multi-Partition",
            "Pre-divided fixed-size slots",
            "Yes (process &lt; partition)",
            "No",
            "Fast",
        ],
        [
            "Variable Partition",
            "Exact-size partition per process",
            "None",
            "Yes (over time)",
            "Medium",
        ],
        ["First Fit", "First hole ≥ size", "Varies", "Yes", "Fastest"],
        ["Best Fit", "Smallest hole ≥ size", "Least", "Worst (tiny leftovers)", "Slow"],
        ["Worst Fit", "Largest hole", "Most", "Moderate", "Slow"],
    ],
)

en.section("Key Formulas — Unit III Quick Reference")
en.info_table(
    ["Formula / Rule", "Application"],
    [
        [
            "Need[i][j] = Max[i][j] − Allocation[i][j]",
            "Banker's Algorithm — remaining resource need per process",
        ],
        [
            "Physical Address = Base Register + Logical Address",
            "MMU relocation — contiguous allocation with base register",
        ],
        [
            "Valid Access: Logical Address &lt; Limit Register",
            "Memory protection — trap on out-of-bounds access",
        ],
        [
            "Safe Sequence: Need[Pi] ≤ Work after Pj (j&lt;i) completes",
            "Banker's Safety Algorithm — condition for process to run next",
        ],
        [
            "50-percent rule: ~1/3 memory wasted with First Fit",
            "External fragmentation estimate in variable partitioning",
        ],
    ],
)
en.br()

# =============================================================================
#  3.13  EXAM QUESTIONS & ANSWERS
# =============================================================================
en.part_box("UNIT III — EXAM QUESTIONS & DETAILED ANSWERS")
en.chap_box("3.13  Previous-Year Style Exam Questions")

en.section("2-Mark Questions")

en.highlight(
    "<b>Q1. What is a deadlock? State the four necessary conditions.</b><br/>"
    "A: Deadlock = a situation where a set of processes are permanently blocked, "
    "each waiting for a resource held by another in the set. "
    "Four necessary conditions (Coffman, 1971): "
    "(1) Mutual Exclusion — resource held non-shareably. "
    "(2) Hold and Wait — process holds one resource while waiting for another. "
    "(3) No Preemption — resources cannot be forcibly taken from a process. "
    "(4) Circular Wait — circular chain of processes, each waiting for the next's resource."
)

en.highlight(
    "<b>Q2. What is a Resource Allocation Graph (RAG)? How is deadlock detected using it?</b><br/>"
    "A: RAG is a directed graph with two types of nodes: processes (circles) and "
    "resources (rectangles, dots = instances). "
    "Request edge P→R: P is waiting for R. Assignment edge R→P: instance of R given to P. "
    "Deadlock detection: If RAG has NO cycle → no deadlock. "
    "If cycle exists AND each resource has ONE instance → deadlock guaranteed. "
    "If cycle exists AND resources have multiple instances → deadlock possible (further analysis needed)."
)

en.highlight(
    "<b>Q3. What is a safe state? How does it relate to deadlock avoidance?</b><br/>"
    "A: A safe state is one where a safe sequence of processes exists — "
    "each process can eventually complete using currently available + future released resources. "
    "Deadlock avoidance (Banker's Algorithm) keeps the system always in a safe state by "
    "only granting resource requests that leave the system in a safe state. "
    "Safe → No deadlock possible. Unsafe → deadlock is possible (not guaranteed)."
)

en.highlight(
    "<b>Q4. Differentiate between deadlock prevention and deadlock avoidance.</b><br/>"
    "A: Prevention: ensures at least one of the four necessary conditions NEVER holds — "
    "system-wide policy (e.g., total ordering of resources to prevent circular wait). "
    "Static constraints. May waste resources. "
    "Avoidance: allows all four conditions but carefully checks each request — "
    "only grants if resulting state is safe (Banker's Algorithm). "
    "Requires advance declaration of maximum resource needs. Dynamic per-request checking."
)

en.highlight(
    "<b>Q5. What is address binding? Name its three types.</b><br/>"
    "A: Address binding = mapping program instructions and data to memory addresses. "
    "(1) Compile-time: compiler generates absolute addresses — process must load at fixed address. "
    "(2) Load-time: compiler generates relocatable code — loader assigns final addresses at load time. "
    "(3) Execution-time (runtime): MMU dynamically translates logical to physical addresses "
    "during execution — requires hardware support. Modern OS uses execution-time binding."
)

en.highlight(
    "<b>Q6. What is the difference between logical and physical address?</b><br/>"
    "A: Logical (virtual) address: generated by CPU — what the process sees. "
    "Physical address: actual location in RAM — what the memory hardware sees. "
    "At compile/load-time binding: logical = physical. "
    "At execution-time binding: logical ≠ physical — MMU translates logical + base = physical. "
    "The user program only works with logical addresses; MMU is invisible to it."
)

en.highlight(
    "<b>Q7. What is the MMU? Explain its role in memory management.</b><br/>"
    "A: MMU (Memory Management Unit) = hardware device that translates logical addresses "
    "to physical addresses at runtime. Every CPU memory access passes through the MMU. "
    "In the simplest scheme: Physical = Logical + Base Register. "
    "Also provides protection: if Logical ≥ Limit Register → trap (segmentation fault). "
    "The OS sets the base and limit registers during context switch to isolate processes."
)

en.highlight(
    "<b>Q8. What is fragmentation? Distinguish between internal and external fragmentation.</b><br/>"
    "A: Fragmentation = wasted memory space. "
    "Internal fragmentation: wasted space INSIDE an allocated block — "
    "process is smaller than the partition it was given (occurs in fixed partitioning, paging). "
    "External fragmentation: wasted space OUTSIDE allocations — "
    "free memory exists but is scattered in many small non-contiguous holes "
    "(occurs in variable partitioning). Total free space may be enough but no single hole is. "
    "Solution: compaction (expensive) or paging/segmentation (Unit IV)."
)

en.section("5-Mark Questions")

en.highlight(
    "<b>Q9. Explain the Banker's Algorithm with a worked example.</b><br/>"
    "A: Banker's Algorithm avoids deadlock by only granting resource requests that keep "
    "the system in a safe state. Data structures: Available, Max, Allocation, Need (= Max − Allocation). "
    "<b>Safety Algorithm:</b> Find a process whose Need ≤ Work (Work = Available initially). "
    "Simulate it completing — add its Allocation to Work. Repeat. "
    "If all processes finish → safe sequence found. "
    "Example: 3 processes, 1 resource type. Available=3. "
    "P0: Allocation=1, Need=2. P1: Allocation=2, Need=1. P2: Allocation=3, Need=2. "
    "Work=3. P1: Need(1)≤Work(3) → Work=3+2=5. P0: Need(2)≤5 → Work=5+1=6. "
    "P2: Need(2)≤6 → Work=6+3=9. Safe sequence: P1→P0→P2."
)

en.highlight(
    "<b>Q10. Explain deadlock recovery methods.</b><br/>"
    "A: Once deadlock is detected, two recovery approaches: "
    "<b>Process Termination:</b> "
    "(a) Abort ALL deadlocked processes — guaranteed to break deadlock but very expensive. "
    "(b) Abort one process at a time (using criteria: priority, CPU time, resources held, "
    "interactive vs batch) — less wasteful but must re-run detection after each abort. "
    "<b>Resource Preemption:</b> "
    "(a) Select victim process (min cost). "
    "(b) Rollback victim to a checkpoint state. "
    "(c) Give preempted resource to another process. "
    "Issue: starvation — same process repeatedly chosen as victim. "
    "Solution: include rollback count in cost calculation."
)

en.highlight(
    "<b>Q11. Compare First Fit, Best Fit, and Worst Fit memory allocation strategies with examples.</b><br/>"
    "A: All three search a list of free holes. "
    "<b>First Fit:</b> Allocates the FIRST hole ≥ request size. Fastest. "
    "<b>Best Fit:</b> Allocates the SMALLEST hole ≥ request size. Least internal waste per allocation "
    "but creates many tiny unusable leftover holes. "
    "<b>Worst Fit:</b> Allocates the LARGEST hole. Leftover is large (more likely usable) "
    "but wastes large holes. Poorest performance overall. "
    "Example: Holes = [100KB, 500KB, 200KB, 300KB, 600KB]. Request = 212 KB. "
    "First Fit → 500 KB hole (288 KB left). Best Fit → 300 KB hole (88 KB left). "
    "Worst Fit → 600 KB hole (388 KB left). "
    "First Fit and Best Fit are generally better than Worst Fit."
)

en.highlight(
    "<b>Q12. Explain contiguous memory allocation — fixed and variable partitioning.</b><br/>"
    "A: Contiguous allocation: each process occupies a single contiguous block of RAM. "
    "<b>Fixed Partitioning:</b> Memory divided into fixed-size partitions at boot. "
    "Each partition holds one process. Degree of multiprogramming = number of partitions. "
    "Problem: internal fragmentation (process smaller than partition). "
    "<b>Variable Partitioning:</b> Partitions created dynamically to exactly fit each process. "
    "No internal fragmentation. Problem: external fragmentation accumulates over time. "
    "Solutions: (1) Compaction — move all processes to one end (costly, needs runtime binding). "
    "(2) Coalescing — merge adjacent free holes automatically on process termination. "
    "(3) Better placement strategy (First Fit / Best Fit)."
)

en.section("10-Mark Questions")

en.highlight(
    "<b>Q13. Explain all aspects of deadlock: definition, conditions, RAG, prevention, "
    "avoidance (Banker's Algorithm), detection, and recovery.</b><br/>"
    "A: <b>Definition:</b> Permanent blocking of processes — each holds resources another needs. "
    "<b>4 Conditions (Coffman):</b> Mutual exclusion, Hold-and-wait, No preemption, Circular wait. "
    "<b>RAG:</b> Directed graph. Request edge P→R, Assignment edge R→P. "
    "Deadlock iff cycle + single-instance resources. "
    "<b>Prevention:</b> Eliminate one condition — e.g., total resource ordering eliminates circular wait. "
    "<b>Avoidance (Banker's):</b> Only grant requests keeping system safe. "
    "Need ≤ Available check using safety algorithm. "
    "<b>Detection:</b> Wait-for graph for single instances. Multi-instance: "
    "safety-like algorithm with Request instead of Need. "
    "<b>Recovery:</b> Abort processes (all or one at a time) or preempt resources with rollback. "
    "Choose victim by cost (priority, CPU time, resources held)."
)

en.highlight(
    "<b>Q14. Explain memory management in OS. Discuss address binding, logical vs physical "
    "address, MMU, and contiguous allocation strategies in detail.</b><br/>"
    "A: <b>Memory management goals:</b> Protection, relocation, sharing, organization. "
    "<b>Address Binding:</b> Mapping program addresses to memory. "
    "Compile-time (fixed address), load-time (relocatable), execution-time (runtime MMU). "
    "<b>Logical vs Physical:</b> Logical = CPU-generated address. Physical = RAM address. "
    "Differ at execution-time binding. MMU translates: Physical = Logical + Base. "
    "<b>Base and Limit:</b> Base gives start of process. Limit gives size. "
    "MMU checks Logical &lt; Limit for protection. Loaded by OS on each context switch. "
    "<b>Contiguous Allocation:</b> "
    "Single partition: one process, simple, low utilization. "
    "Fixed multi-partition: N partitions, N processes max, internal fragmentation. "
    "Variable partition: exact size, no internal fragmentation, external fragmentation. "
    "Solved by First Fit / Best Fit and compaction."
)

en.section("Quick Revision Table — Unit III")
en.info_table(
    ["Topic", "Key Exam Points"],
    [
        [
            "Deadlock Definition",
            "Permanent block. Each process waits for resource held by another. Non-preemptable resources.",
        ],
        [
            "4 Necessary Conditions",
            "Mutual exclusion + Hold & Wait + No Preemption + Circular Wait. ALL four must hold.",
        ],
        [
            "RAG",
            "P→R: request. R→P: assignment. Cycle + single instance = deadlock. Cycle + multi = possible.",
        ],
        [
            "Prevention: Circular Wait",
            "Total ordering of resources. Processes request in increasing order only.",
        ],
        [
            "Prevention: Hold & Wait",
            "Request all resources before starting OR release all before requesting new ones.",
        ],
        [
            "Safe State",
            "Safe sequence exists. Every process can eventually complete. No deadlock possible.",
        ],
        [
            "Banker's Algorithm",
            "Need = Max − Allocation. Safety: find Pi where Need[i] ≤ Work. Grant only if safe after.",
        ],
        [
            "Detection (single instance)",
            "Wait-for graph. Deadlock iff cycle exists.",
        ],
        [
            "Detection (multi-instance)",
            "Safety-like algorithm with Request (actual). Unfinished = deadlocked.",
        ],
        [
            "Recovery",
            "Abort (all/one at a time) or Preempt (rollback to checkpoint). Avoid starvation.",
        ],
        [
            "Address Binding",
            "Compile-time (fixed), Load-time (relocatable), Execution-time (MMU, dynamic).",
        ],
        [
            "Logical vs Physical",
            "Logical = CPU address. Physical = RAM address. MMU: Physical = Logical + Base.",
        ],
        [
            "MMU",
            "Hardware translates logical→physical. Base register + Limit register. Protection via limit check.",
        ],
        [
            "Single Partition",
            "One process in memory. Simple. OS + one user process. Low utilization.",
        ],
        [
            "Fixed Partition",
            "Pre-divided. Internal fragmentation. Degree of multiprogramming = number of partitions.",
        ],
        [
            "Variable Partition",
            "Dynamic exact-size. No internal frag. External fragmentation. Solved by compaction.",
        ],
        [
            "First Fit",
            "First hole ≥ size. Fastest. Best overall performance.",
        ],
        [
            "Best Fit",
            "Smallest sufficient hole. Least waste per alloc. Produces tiny unusable leftovers.",
        ],
        [
            "Worst Fit",
            "Largest hole. Leaves large fragments. Worst overall performance.",
        ],
        [
            "External Fragmentation",
            "Free space scattered. 1/3 of memory wasted (50% rule). Solution: paging (Unit IV).",
        ],
    ],
)

en.exam(
    "Most asked topics in IT412 Unit III exams: "
    "(1) State and explain Coffman's four necessary conditions for deadlock with examples. "
    "(2) Explain the Banker's Algorithm (Safety + Resource-Request) with a worked example. "
    "(3) Draw and explain the Resource Allocation Graph — show deadlock and no-deadlock cases. "
    "(4) Explain First Fit, Best Fit, Worst Fit with a numerical example showing hole selection. "
    "(5) Differentiate between logical and physical address with MMU diagram. "
    "(6) Compare fixed vs variable partitioning — internal vs external fragmentation. "
    "Always show the Banker's safety sequence step-by-step when working examples."
)

en.note(
    "Unit III connects to Unit IV (Paging eliminates external fragmentation from Unit III) "
    "and Unit II (Semaphores from Unit II are the resources that cause deadlock — "
    "the dining philosophers deadlock from Section 2.15 is a perfect Unit III example). "
    "Reference: Silberschatz Chapter 7 (Deadlock), Chapter 8 (Memory Management)."
)

# =============================================================================
#  FLASHCARDS & REVISION
# =============================================================================
en.br()
en.chap_box("Rapid Revision & Flashcards")

en.revision_card(
    "Unit III Mastery Check",
    [
        "State all four Coffman necessary conditions and give a real-world example of each.",
        "Draw a RAG showing deadlock and explain why a cycle with multi-instance resources may not be deadlock.",
        "Run the Banker's Safety Algorithm on a given Allocation/Max/Available table.",
        "Calculate hole selection using First Fit, Best Fit, and Worst Fit for a given hole list and request.",
        "Explain why variable partitioning causes external fragmentation and how compaction solves it.",
    ],
)

en.flashcard(
    "Coffman's 4 conditions for <b>Deadlock</b>",
    "1. Mutual Exclusion — non-shareable resource. "
    "2. Hold and Wait — holds one, waits for another. "
    "3. No Preemption — cannot forcibly take resource. "
    "4. Circular Wait — P0→P1→P2→...→P0 wait chain.",
)
en.flashcard(
    "Banker's Algorithm: <b>Need</b> formula",
    "Need[i][j] = Max[i][j] − Allocation[i][j]. "
    "It is the remaining resource need of process i for resource j.",
)
en.flashcard(
    "<b>Safe State</b> definition",
    "A state where a safe sequence exists — every process can eventually complete "
    "using available + future released resources. Deadlock impossible in safe state.",
)
en.flashcard(
    "<b>First Fit</b> vs <b>Best Fit</b>",
    "First Fit: first hole large enough — fastest, good overall. "
    "Best Fit: smallest sufficient hole — least internal waste per allocation, "
    "but creates many tiny unusable leftover holes.",
)
en.flashcard(
    "<b>MMU</b> address translation",
    "Physical Address = Logical Address + Base Register. "
    "Protection: Logical Address &lt; Limit Register (else trap).",
)
en.flashcard(
    "Internal vs External <b>Fragmentation</b>",
    "Internal: wasted space INSIDE a partition (fixed partitioning, paging last page). "
    "External: wasted space BETWEEN partitions — free but scattered (variable partitioning).",
)

en.br()
en.chap_box("Index")
en.print_index()

# =============================================================================
#  BUILD DOCUMENT
# =============================================================================
en.build_doc("OS_Unit3_Notes.pdf")

print("Generated: OS_Unit3_Notes.pdf")
