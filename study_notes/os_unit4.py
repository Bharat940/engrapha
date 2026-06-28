"""
Operating Systems (IT412) -- Unit IV Notes
UIT-RGPV (Autonomous) Bhopal | Semester IV
Complete exam notes: Paging, TLB, Page Fault, Segmentation with Paging,
Effective Access Time, Virtual Memory, Demand Paging, Page Replacement
Algorithms, Frame Allocation, Thrashing, OS Security.

Run:  python os_unit4_notes.py
Output: OS_Unit4_Notes.pdf  |  OS_Unit4_Notes_html/  |  OS_Unit4_Notes.pptx
"""

from __future__ import annotations

import engrapha_notes as en
import engrapha_diagrams as ed
from reportlab.platypus import Table

# =============================================================================
#  THEME — OCEAN_DARK: deep teal/blue accent
#  Unit I = CATPPUCCIN_MOCHA, II = FOREST_DARK, III = SUNSET_DARK, IV = OCEAN_DARK
# =============================================================================
en.set_story([])
en.set_theme(en.OCEAN_DARK)

en.set_global_footer(
    left="Operating Systems (IT412) — Unit IV",
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
    "Unit IV — Virtual Memory, Paging, Segmentation & Security",
)
# en.cover_subtitle(
#     [
#         "Subject Code: IT412  |  UIT-RGPV (Autonomous) Bhopal  |  Semester IV",
#         "Paging, TLB, Page Fault, Segmentation with Paging, EAT,",
#         "Virtual Memory, Demand Paging, Page Replacement, Thrashing, Security",
#     ]
# )
en.sp(10)
en.rule(en.get_theme().rl(en.get_theme().accent), 1.5)
en.sp(8)

en.info_table(
    ["Section", "Syllabus Topics Covered"],
    [
        [
            "4.1  Paging",
            "Page, frame, page table, address translation, hardware support",
        ],
        [
            "4.2  Paging Issues",
            "Page table size, hierarchical paging, hashed & inverted page tables",
        ],
        [
            "4.3  TLB & Effective Access Time",
            "Translation Lookaside Buffer, hit ratio, EAT calculation",
        ],
        ["4.4  Page Fault", "Handling steps, pure demand paging, hardware support"],
        [
            "4.5  Segmentation",
            "Logical segments, segment table, address translation, protection",
        ],
        [
            "4.6  Segmentation with Paging",
            "Combined scheme, Intel x86 architecture, logical→linear→physical",
        ],
        [
            "4.7  Virtual Memory — Concepts",
            "Definition, benefits, overlay vs virtual memory, swap space",
        ],
        ["4.8  Demand Paging", "Lazy loading, page fault rate, copy-on-write"],
        ["4.9  Demand Segmentation", "Segmentation extended with demand loading"],
        [
            "4.10 Page Replacement Algorithms",
            "FIFO, Optimal, LRU, LRU-Approximation, Belady's Anomaly",
        ],
        [
            "4.11 Allocation of Frames",
            "Fixed vs dynamic allocation, local vs global replacement",
        ],
        ["4.12 Thrashing", "Causes, effects, Working Set Model, Page-Fault Frequency"],
        ["4.13 Security in OS", "Security problem, goals, authentication, threats"],
        [
            "4.14 Security Techniques",
            "Encryption, access control, firewalls, intrusion detection",
        ],
        [
            "4.15 Exam Questions",
            "25+ PYQ-style questions with detailed answers and numericals",
        ],
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
#  PART I: PAGING & SEGMENTATION
# =============================================================================
en.part_box("UNIT IV — PART A: PAGING & MEMORY MANAGEMENT")

# =============================================================================
#  4.1  PAGING
# =============================================================================
en.chap_box("4.1  Paging")

en.section("What is Paging?")
en.definition(
    "<b>Paging:</b> A memory management scheme that eliminates external fragmentation "
    "by dividing both physical memory and logical address space into fixed-size equal-sized blocks. "
    "Physical memory blocks are called <b>frames</b>. "
    "Logical address blocks are called <b>pages</b>. "
    "Page size = Frame size (power of 2, typically 4 KB on modern systems). "
    "A process's pages can be loaded into any available frames — "
    "they need NOT be contiguous in physical memory. "
    "The OS maintains a <b>page table</b> per process that maps page numbers to frame numbers."
)

en.section("Paging Address Translation")
en.definition(
    "A logical address is divided into two parts by the hardware: "
    "<b>Page Number (p)</b> — used as an index into the page table to find the frame number. "
    "<b>Page Offset (d)</b> — combined with the frame number to give the physical address."
)

en.formula_block(
    r"\text{Logical Address} = (p,\ d) \quad \text{where } d < \text{page size}"
)
en.formula_block(r"\text{Physical Address} = f \times \text{page\_size} + d")
en.body(
    "Where f = frame number obtained from page_table[p], and d = page offset. "
    "If page size = 2^n bytes, then d uses the lower n bits and p uses the remaining upper bits of the logical address."
)

en.info_table(
    ["Parameter", "Formula", "Example (page size = 4 KB = 2^12)"],
    [
        [
            "Page number (p)",
            "logical_address >> n (upper bits)",
            "Logical 0x3A4F >> 12 = page 3",
        ],
        [
            "Page offset (d)",
            "logical_address & (page_size − 1)",
            "Logical 0x3A4F & 0xFFF = 0xA4F",
        ],
        [
            "Physical address",
            "frame[p] × page_size + d",
            "If frame[3]=7: 7×4096 + 0xA4F = 0x7A4F",
        ],
        [
            "Number of pages",
            "⌈logical_addr_space / page_size⌉",
            "128 KB / 4 KB = 32 pages",
        ],
    ],
)

en.section("Paging — Address Translation Diagram")
seq_paging = ed.SequenceDiagram(
    width=en.CW,
    height=240,
    theme=diag_theme,
    caption="Fig 4.1: Paging — logical address to physical address translation",
)
seq_paging.actor("cpu", "CPU")
seq_paging.actor("pt", "Page Table\n(in RAM or PTBR)")
seq_paging.actor("mmu", "MMU")
seq_paging.actor("ram", "Physical RAM")
seq_paging.message("cpu", "mmu", "Logical addr (p=3, d=0xA4F)", arrow="solid")
seq_paging.activate("mmu")
seq_paging.message("mmu", "pt", "page_table[3] = ?", arrow="solid")
seq_paging.message("pt", "mmu", "frame number = 7", arrow="dashed")
seq_paging.message("mmu", "mmu", "Physical = 7 × 4096 + 0xA4F\n= 0x7A4F", arrow="solid")
seq_paging.message("mmu", "ram", "Access 0x7A4F", arrow="solid")
seq_paging.message("ram", "mmu", "Data", arrow="dashed")
seq_paging.deactivate("mmu")
seq_paging.message("mmu", "cpu", "Return data", arrow="dashed")
en.story.extend(seq_paging.as_flowable())

en.section("Paging Advantages and Disadvantages")
en.info_table(
    ["Aspect", "Detail"],
    [
        [
            "No External Fragmentation",
            "Any free frame can hold any page — no contiguous requirement. Fragmentation eliminated.",
        ],
        [
            "Internal Fragmentation",
            "A process's last page may not fill an entire frame. Avg waste = half a page per process.",
        ],
        [
            "OS Overhead",
            "OS must maintain a page table per process. Large address spaces = very large page tables.",
        ],
        [
            "Sharing",
            "Two processes can share a physical frame (shared libraries, copy-on-write fork).",
        ],
        [
            "Protection",
            "Each page table entry has protection bits (read/write/execute). MMU enforces them.",
        ],
        [
            "Locality",
            "Paging supports virtual memory by loading only needed pages (demand paging).",
        ],
    ],
)
en.br()

# =============================================================================
#  4.2  PAGING ISSUES — LARGE PAGE TABLES
# =============================================================================
en.chap_box("4.2  Paging Issues — Page Table Size & Solutions")

en.section("The Page Table Size Problem")
en.definition(
    "<b>Problem:</b> For a 32-bit logical address space with 4 KB pages, "
    "the page table has 2^32 / 2^12 = 2^20 = 1,048,576 entries. "
    "If each entry is 4 bytes → page table size = 4 MB per process. "
    "With 100 concurrent processes → 400 MB just for page tables. "
    "For 64-bit address spaces, this is astronomically worse. "
    "Three solutions: Hierarchical Paging, Hashed Page Tables, Inverted Page Tables."
)

en.section("Solution 1: Hierarchical (Multi-Level) Paging")
en.definition(
    "<b>Hierarchical Paging:</b> Divide the logical address into multiple parts, "
    "each indexing a level of a tree of page tables. "
    "Two-level example: logical address divided into outer page number (p1), "
    "inner page number (p2), and offset (d). "
    "Only the outer page table and the inner pages actually used are loaded into RAM "
    "— unused portions of the address space consume no memory."
)
en.formula_block(
    r"\text{Two-Level: } (p_1,\ p_2,\ d) \rightarrow \text{outer\_table}[p_1][p_2] = f"
)
en.info_table(
    ["Levels", "Address Space Covered", "Used By"],
    [
        ["2-level", "32-bit address space", "Intel x86-32, early MIPS"],
        ["3-level", "48-bit address space", "Intel x86-64 (PML3)"],
        ["4-level", "48-bit virtual address", "AMD64, Linux kernel (PML4)"],
        ["5-level", "57-bit virtual address", "Intel Ice Lake+ (PML5, Linux 4.14+)"],
    ],
)

en.section("Solution 2: Hashed Page Tables")
en.definition(
    "<b>Hashed Page Table:</b> Common in address spaces larger than 32 bits. "
    "The page number is hashed into a hash table. Each entry in the hash table contains "
    "a chain of elements: (virtual page number, frame number, next pointer). "
    "A search walks the chain until the virtual page number matches. "
    "Efficient for sparse address spaces."
)

en.section("Solution 3: Inverted Page Table")
en.definition(
    "<b>Inverted Page Table:</b> Instead of one page table per process, "
    "there is ONE table for the entire physical memory — "
    "one entry per physical frame (not per virtual page). "
    "Each entry stores: (PID, virtual page number). "
    "To translate, search the table for (PID, p) → entry index is the frame number. "
    "Dramatically reduces memory for page tables. "
    "Drawback: linear search is slow — use hash table for lookup. "
    "Sharing pages is difficult. "
    "Used by IBM PowerPC, UltraSPARC."
)

en.info_table(
    ["Scheme", "Memory Usage", "Lookup Speed", "Sharing Support"],
    [
        [
            "Single-level page table",
            "High (entire address space covered)",
            "O(1) — direct index",
            "Easy",
        ],
        [
            "Hierarchical page table",
            "Low (sparse pages not allocated)",
            "O(k) — k levels",
            "Moderate",
        ],
        ["Hashed page table", "Moderate", "O(1) avg with hash", "Moderate"],
        [
            "Inverted page table",
            "Very low (one entry per frame)",
            "O(n) — need hash",
            "Difficult",
        ],
    ],
)
en.br()

# =============================================================================
#  4.3  TLB & EFFECTIVE ACCESS TIME
# =============================================================================
en.chap_box("4.3  TLB & Effective Access Time (EAT)")

en.section("Translation Lookaside Buffer (TLB)")
en.definition(
    "<b>TLB (Translation Lookaside Buffer):</b> A small, fast, fully-associative cache "
    "inside the MMU that stores recent page-number to frame-number translations. "
    "Each TLB entry: (page number, frame number, valid bit, dirty bit, ASID). "
    "On every memory access, the TLB is searched in parallel with the page table — "
    "if found (TLB hit), frame number is available immediately without a RAM access. "
    "TLBs typically hold 64–1024 entries and achieve hit ratios of 90–99%."
)

en.info_table(
    ["Scenario", "Memory Accesses Required", "Explanation"],
    [
        [
            "TLB Hit",
            "1 (data access only)",
            "Frame number found in TLB → use it directly → 1 RAM access for data.",
        ],
        [
            "TLB Miss",
            "2 (page table + data)",
            "Page table lookup in RAM (1 access) + data access (1 access).",
        ],
    ],
)

en.section("ASID — Address Space Identifiers")
en.definition(
    "<b>ASID (Address Space Identifier):</b> A tag added to each TLB entry that identifies "
    "which process the entry belongs to. Without ASIDs, the TLB must be flushed completely "
    "on every context switch (very expensive). "
    "With ASIDs, TLB entries from different processes can coexist — only entries with "
    "a matching ASID are used for the current process. "
    "The TLB needs flushing only when ASIDs are exhausted (typically 8-bit = 256 ASIDs)."
)

en.section("Effective Access Time (EAT) Calculation")
en.definition(
    "<b>Effective Access Time (EAT):</b> The average time to access a memory location, "
    "taking into account TLB hit probability and the time for TLB and memory lookups."
)
en.formula_block(
    r"\text{EAT} = h \times (t_{TLB} + t_{mem}) + (1-h) \times (t_{TLB} + 2 \times t_{mem})"
)
en.bullet(
    [
        "<b>h</b>: TLB hit ratio (probability that page is found in TLB).",
        "<b>t_TLB</b>: TLB access time (typically 1–5 ns).",
        "<b>t_mem</b>: Main memory access time (typically 50–100 ns).",
    ]
)

en.section("EAT Worked Examples")
en.info_table(
    ["Given", "Calculation", "Result"],
    [
        [
            "t_mem = 100 ns, t_TLB = 20 ns, h = 0.80",
            "EAT = 0.80 × (20+100) + 0.20 × (20+200)\n     = 0.80 × 120 + 0.20 × 220\n     = 96 + 44",
            "EAT = 140 ns",
        ],
        [
            "t_mem = 100 ns, t_TLB = 0 ns (ideal), h = 0.90",
            "EAT = 0.90 × (0+100) + 0.10 × (0+200)\n     = 90 + 20",
            "EAT = 110 ns  (10% overhead vs 100 ns ideal)",
        ],
        [
            "t_mem = 200 ns, t_TLB = 10 ns, h = 0.98",
            "EAT = 0.98 × (10+200) + 0.02 × (10+400)\n     = 0.98 × 210 + 0.02 × 410\n     = 205.8 + 8.2",
            "EAT = 214 ns  (nearly as fast as single access)",
        ],
    ],
)

en.exam(
    "EAT Formula: EAT = h×(t_TLB + t_mem) + (1−h)×(t_TLB + 2×t_mem). "
    "Simplifies to: EAT = t_TLB + t_mem + (1−h)×t_mem = t_TLB + (2−h)×t_mem. "
    "Higher hit ratio → EAT closer to t_mem. "
    "ALWAYS include t_TLB in both hit and miss cases."
)
en.br()

# =============================================================================
#  4.4  PAGE FAULT
# =============================================================================
en.chap_box("4.4  Page Fault")

en.section("What is a Page Fault?")
en.definition(
    "<b>Page Fault:</b> A hardware exception triggered by the MMU when a process "
    "attempts to access a page that is not currently loaded in main memory "
    "(valid bit = 0 in its page table entry). "
    "The CPU traps to the OS page-fault handler. "
    "The OS must locate the page on secondary storage (swap space or file system), "
    "bring it into a free frame, update the page table, and restart the instruction. "
    "Page faults are the mechanism that enables virtual memory — "
    "processes can reference more memory than physically exists."
)

en.section("Pure Demand Paging")
en.definition(
    "<b>Pure Demand Paging:</b> Never load a page into memory until it is required. "
    "A process starts with NO pages in memory. The first instruction causes a page fault. "
    "Subsequent instructions cause more faults until the working set is loaded. "
    "Extreme case of lazy loading. "
    "<b>Prepaging:</b> Opposite approach — load multiple pages at startup to reduce initial fault rate."
)

en.section("Page Fault Rate and Performance")
en.formula_block(r"\text{EAT} = (1-p) \times t_{mem} + p \times t_{page\_fault}")
en.bullet(
    [
        "<b>p</b>: probability of a page fault (fault rate, 0 ≤ p ≤ 1).",
        "<b>t_mem</b>: memory access time (ns).",
        "<b>t_page_fault</b>: page fault service time, including disk I/O (≈ 8 ms = 8,000,000 ns).",
        "For t_mem = 200 ns, t_fault = 8 ms, p = 0.001: EAT = 0.999×200 + 0.001×8,000,000 = 8,199.8 ns → 40× slowdown.",
        "Conclusion: page fault rate must be kept very low (< 1 in 400,000 accesses) to avoid significant slowdown.",
    ]
)

en.section("Page Fault Handling — Step by Step")
fc_pf = ed.Flowchart(
    width=440,
    height=620,
    theme=diag_theme,
    caption="Fig 4.2: Complete page fault handling flow",
)
fc_pf.terminal("access", "Process accesses\npage P")
fc_pf.decision("valid", "Valid?")
fc_pf.terminal("hit", "Access succeeds")
fc_pf.process("trap", "Trap to OS\nhandler")
fc_pf.decision("valid2", "Legal?")
fc_pf.terminal("seg", "Trap: seg fault\nkill process")
fc_pf.process("find", "Find page\non disk")
fc_pf.decision("frame", "Free frame?")
fc_pf.process("replace", "Select victim\nframe")
fc_pf.decision("dirty_check", "Dirty?")
fc_pf.process("dirty", "Page out\n(write to disk)")
fc_pf.process("load", "Page in\n(load to frame)")
fc_pf.process("update", "Update page\ntable")
fc_pf.terminal("restart", "Restart\ninstruction")

fc_pf.edge("access", "valid")
fc_pf.edge("valid", "hit", branch="yes")
fc_pf.edge("valid", "trap", branch="no")
fc_pf.edge("trap", "valid2")
fc_pf.edge("valid2", "seg", branch="no")
fc_pf.edge("valid2", "find", branch="yes")
fc_pf.edge("find", "frame")
fc_pf.edge("frame", "replace", branch="no")
fc_pf.edge("frame", "load", branch="yes")
fc_pf.edge("replace", "dirty_check")
fc_pf.edge("dirty_check", "dirty", branch="yes")
fc_pf.edge("dirty_check", "load", branch="no")
fc_pf.edge("dirty", "load")
fc_pf.edge("load", "update")
fc_pf.edge("update", "restart")
en.story.extend(fc_pf.as_flowable())
en.br()

# =============================================================================
#  4.5  SEGMENTATION
# =============================================================================
en.chap_box("4.5  Segmentation")

en.section("Segmentation — Overview")
en.definition(
    "<b>Segmentation:</b> A memory management scheme that supports the user's view of memory. "
    "A program is a collection of segments: code, data, stack, heap, symbol table, shared library. "
    "Each segment has a name (or number) and a length. "
    "<b>Logical address:</b> (segment number s, offset d). "
    "<b>Segment table:</b> maps (s, d) → physical address. "
    "Each segment table entry has: <b>base</b> (starting physical address) and <b>limit</b> (length). "
    "Physical address = segment_table[s].base + d (provided d < limit)."
)

en.section("Segmentation Address Translation")
en.info_table(
    ["Step", "Operation", "Hardware Action"],
    [
        [
            "1. Extract s and d",
            "CPU generates logical address (s, d)",
            "Hardware splits the address into segment number and offset",
        ],
        [
            "2. Validate s",
            "Check s < segment table length",
            "Else: trap — invalid segment",
        ],
        [
            "3. Validate d",
            "Check d < segment_table[s].limit",
            "Else: trap — segment bounds violation (segmentation fault)",
        ],
        [
            "4. Check permissions",
            "Verify operation (R/W/X) against protection bits in PTE",
            "Else: trap — protection violation",
        ],
        ["5. Compute physical", "PA = segment_table[s].base + d", "Add base to offset"],
        ["6. Access memory", "Access physical address PA", "Normal RAM access"],
    ],
)

en.section("Segmentation Advantages and Disadvantages")
en.info_table(
    ["Aspect", "Detail"],
    [
        [
            "Programmer View",
            "Matches the programmer's logical structure — code, data, stack are separate named units.",
        ],
        [
            "Sharing",
            "Segments can be shared between processes (e.g., shared library code segment).",
        ],
        [
            "Protection",
            "Different protection bits per segment — code = execute only; data = read/write.",
        ],
        [
            "Flexible Size",
            "Each segment can grow/shrink independently (heap segment can expand).",
        ],
        [
            "External Fragmentation",
            "MAIN DISADVANTAGE: variable-size segments create holes in physical memory over time.",
        ],
        ["No Internal Fragmentation", "A segment is exactly as large as needed."],
    ],
)

en.section("Segmentation vs Paging")
en.info_table(
    ["Feature", "Paging", "Segmentation"],
    [
        [
            "Logical unit",
            "Fixed-size page (no logical meaning)",
            "Variable-size segment (code, data, stack)",
        ],
        [
            "Programmer aware?",
            "No — transparent to programmer",
            "Yes — programmer names segments",
        ],
        ["External fragmentation", "None", "Yes — major drawback"],
        ["Internal fragmentation", "Yes — last page may be partially filled", "None"],
        ["Sharing", "Page-level sharing (complex)", "Segment-level sharing (natural)"],
        ["Protection", "Per-page protection bits", "Per-segment protection bits"],
    ],
)
en.br()

# =============================================================================
#  4.6  SEGMENTATION WITH PAGING
# =============================================================================
en.chap_box("4.6  Segmentation with Paging")

en.section("Combined Segmentation and Paging")
en.definition(
    "<b>Segmentation with Paging:</b> A hybrid scheme that combines the logical structure "
    "of segmentation with the physical convenience of paging. "
    "Each segment is divided into pages. "
    "The programmer sees logical segments; the OS uses paging to manage each segment. "
    "Eliminates external fragmentation (from segmentation) while preserving the "
    "programmer's logical view. "
    "Address translation: Logical address → (segment, page, offset) → physical address."
)

en.section("Intel x86 Architecture — Logical to Physical")
en.body(
    "Intel x86-32 uses a two-step translation: "
    "(1) Segment selector + offset → Linear (virtual) address (segmentation). "
    "(2) Linear address → Physical address (paging, using page directory + page table). "
    "In practice, modern 64-bit Linux/Windows set all segment bases to 0 and "
    "limit to maximum — effectively disabling segmentation and using only paging."
)

fc_seg_page = ed.Flowchart(
    width=en.CW,
    height=140,
    theme=diag_theme,
    caption="Fig 4.3: Intel x86 — Logical address → Linear address → Physical address",
    direction="LR",
    scale_factor=0.95,
)
fc_seg_page.terminal("logical", "Logical Address\n(Selector + Offset)", x=60, y=50)
fc_seg_page.process("seg_unit", "Segmentation Unit", x=170, y=50)
fc_seg_page.process("page_unit", "Paging Unit", x=330, y=50)
fc_seg_page.terminal("physical", "Physical Address\n(in RAM)", x=440, y=50)
fc_seg_page.edge("logical", "seg_unit")
fc_seg_page.edge("seg_unit", "page_unit", label="Linear Address")
fc_seg_page.edge("page_unit", "physical")
en.story.extend(fc_seg_page.as_flowable())

en.section("Address Translation in Segmentation-with-Paging")
en.formula_block(
    r"\text{Logical: } (s,\ p,\ d) \ \rightarrow \ \text{page table base} \ \rightarrow \ f \ \rightarrow \ f \times \text{pagesize} + d"
)
en.info_table(
    ["Component", "Role"],
    [
        [
            "Segment table",
            "Maps segment number s → base address of that segment's page table",
        ],
        ["Page table (per segment)", "Maps page number p → frame number f"],
        [
            "Offset d",
            "Byte offset within the page/frame — unchanged throughout translation",
        ],
        ["Physical address", "f × page_size + d"],
    ],
)
en.br()

# =============================================================================
#  4.7  VIRTUAL MEMORY — CONCEPTS
# =============================================================================
en.part_box("UNIT IV — PART B: VIRTUAL MEMORY & PAGE REPLACEMENT")
en.chap_box("4.7  Virtual Memory — Concepts")

en.section("What is Virtual Memory?")
en.definition(
    "<b>Virtual Memory:</b> A technique that allows a process to execute even when "
    "only PART of it is loaded in main memory. "
    "The rest remains on secondary storage (disk). "
    "From the programmer's perspective, each process has a large, contiguous address space "
    "(virtual address space) that may be much larger than physical RAM. "
    "The OS and MMU work together to provide the illusion that the entire program is in memory, "
    "transparently swapping pages between RAM and disk as needed."
)

en.section("Benefits of Virtual Memory")
en.bullet(
    [
        "<b>Programs larger than physical RAM can run:</b> Only the actively-used portion needs to be in memory.",
        "<b>More processes can run concurrently:</b> Each process uses only the frames it currently needs, freeing RAM for others.",
        "<b>Faster process startup:</b> Only the first page (entry point) needs to be loaded — the rest is loaded on demand.",
        "<b>Copy-on-Write (COW) for fork():</b> Parent and child share pages initially; a private copy is made only on first write.",
        "<b>Memory-Mapped Files:</b> Files are mapped into the virtual address space — file I/O becomes memory access.",
        "<b>Shared Libraries:</b> A single copy of a shared library's pages can be mapped into multiple processes' address spaces.",
    ]
)

en.section("Virtual Address Space vs Physical Memory")
left_va = ed.LayeredStack(
    width=en.CW * 0.46,
    height=240,
    theme=diag_theme,
    caption="Virtual Address Space (per process)",
)
left_va.layer("Stack (grows ↓)", sublabel="High addresses")
left_va.layer("Shared Libraries", sublabel="Memory-mapped region")
left_va.layer("Heap (grows ↑)", sublabel="Dynamic allocation")
left_va.layer("Data + BSS", sublabel="Global variables")
left_va.layer("Text (Code)", sublabel="Low addresses — read-only")

right_va = ed.LayeredStack(
    width=en.CW * 0.46,
    height=240,
    theme=diag_theme,
    caption="Physical Memory (shared by all)",
)
right_va.layer("OS Kernel", sublabel="Always resident")
right_va.layer("Process A frames", sublabel="Actively used pages")
right_va.layer("Process B frames", sublabel="Actively used pages")
right_va.layer("Free Frames", sublabel="Available for page-in")

left_va.as_flowable()
right_va.as_flowable()
tbl_va = Table(
    [
        [
            ed.ResponsiveDrawingFlowable(left_va.drawing),
            ed.ResponsiveDrawingFlowable(right_va.drawing),
        ]
    ],
    colWidths=[en.CW * 0.48, en.CW * 0.48],
)
en.story.append(tbl_va)
en.sp(6)
en.br()

# =============================================================================
#  4.8  DEMAND PAGING
# =============================================================================
en.chap_box("4.8  Demand Paging")

en.section("Demand Paging — Definition")
en.definition(
    "<b>Demand Paging:</b> A virtual memory technique where pages are loaded into RAM "
    "ONLY when they are first accessed (demanded), not when the process starts. "
    "This is a form of lazy evaluation applied to memory. "
    "When a page that is not in RAM is accessed, a page fault occurs, "
    "and the OS loads that specific page from disk. "
    "Demand paging is implemented using a <b>lazy swapper</b> (also called a pager) — "
    "a swapper that never swaps a page into memory unless it will be needed."
)

en.section("Hardware Support for Demand Paging")
en.info_table(
    ["Hardware Component", "Role in Demand Paging"],
    [
        [
            "Page table with valid/invalid bit",
            "Valid (1) = page in RAM. Invalid (0) = page not in RAM (triggers page fault).",
        ],
        [
            "Secondary storage (swap space)",
            "Holds pages not currently in RAM. OS manages a swap partition/file.",
        ],
        [
            "Page fault handler (OS)",
            "Software that handles the page fault interrupt: find page, load it, restart instruction.",
        ],
        [
            "Restart capability",
            "CPU must be able to restart any instruction after a page fault. Complex for instructions that modify multiple memory locations (e.g., string moves).",
        ],
    ],
)

en.section("Copy-on-Write (COW)")
en.definition(
    "<b>Copy-on-Write (COW):</b> An optimization used with fork(). "
    "When a parent process calls fork(), instead of immediately copying all parent pages, "
    "both parent and child processes share the same physical pages marked as read-only. "
    "When either process tries to WRITE to a shared page, a page fault occurs, "
    "the OS makes a private copy of that page for the writing process, "
    "and the write proceeds on the private copy. "
    "Pages that are never written are never copied — significant performance improvement. "
    "Used by Linux, macOS, Windows."
)
en.br()

# =============================================================================
#  4.9  DEMAND SEGMENTATION
# =============================================================================
en.chap_box("4.9  Demand Segmentation")

en.section("Demand Segmentation — Definition")
en.definition(
    "<b>Demand Segmentation:</b> An extension of demand paging to segmented memory systems. "
    "Segments are loaded into memory on demand — only when a segment is first accessed "
    "does the OS load it from secondary storage. "
    "Each segment table entry has a valid/invalid bit. "
    "When a segment is accessed with valid bit = 0, a segment fault occurs and the OS loads the segment. "
    "Less common than demand paging since modern systems prefer paging. "
    "Multics was a historical system that used demand segmentation with paging."
)

en.info_table(
    ["Scheme", "Unit of Transfer", "Fault Name", "Common in"],
    [
        [
            "Demand Paging",
            "Fixed-size page",
            "Page fault",
            "All modern OS (Linux, Windows, macOS)",
        ],
        [
            "Demand Segmentation",
            "Variable-size segment",
            "Segment fault",
            "Historical (Multics). Rare today.",
        ],
        [
            "Combined",
            "Pages within segments",
            "Page fault",
            "Intel x86 (segmentation mostly disabled)",
        ],
    ],
)
en.br()

# =============================================================================
#  4.10  PAGE REPLACEMENT ALGORITHMS
# =============================================================================
en.chap_box("4.10  Page Replacement Algorithms")

en.section("Why Page Replacement?")
en.definition(
    "<b>Page Replacement:</b> When a page fault occurs and there are no free frames available, "
    "the OS must select a <b>victim frame</b> — an existing page to remove from RAM to make room. "
    "If the victim page has been modified (dirty bit = 1), it must be written back to disk first. "
    "The page replacement algorithm determines WHICH page to evict. "
    "Goal: minimize the page fault rate (minimize disk I/O). "
    "<b>Reference string:</b> The sequence of page accesses — used to evaluate algorithms."
)

en.section("Algorithm 1: FIFO — First-In First-Out")
en.definition(
    "<b>FIFO:</b> Replaces the page that has been in memory the LONGEST (the oldest). "
    "Implemented using a simple queue — new pages enter at the tail; "
    "eviction removes from the head. "
    "Simple but not always optimal — may evict frequently-used pages. "
    "Suffers from <b>Belady's Anomaly</b>: increasing frames can increase fault count."
)

en.section("Belady's Anomaly")
en.definition(
    "<b>Belady's Anomaly:</b> The counter-intuitive phenomenon in FIFO where adding more "
    "frames can actually INCREASE the number of page faults. "
    "Example: Reference string 1,2,3,4,1,2,5,1,2,3,4,5 "
    "gives 9 faults with 3 frames but 10 faults with 4 frames. "
    "Only FIFO suffers this anomaly. LRU, Optimal, and stack algorithms do not."
)

en.section("Algorithm 2: Optimal (OPT / Bélády's)")
en.definition(
    "<b>Optimal Algorithm (OPT):</b> Replace the page that will NOT be used for the "
    "LONGEST time in the future. "
    "Provably optimal — achieves the minimum possible page fault rate for any given reference string. "
    "<b>BUT: It is impossible to implement</b> — requires knowledge of future page references. "
    "Used as a benchmark to evaluate how close other algorithms get to the optimum."
)

en.section("Algorithm 3: LRU — Least Recently Used")
en.definition(
    "<b>LRU:</b> Replace the page that was LEAST RECENTLY USED — "
    "the page not referenced for the longest time in the past. "
    "Based on the principle of temporal locality: recently-used pages are likely to be used again soon. "
    "Excellent performance — close to Optimal in practice. "
    "Does NOT suffer from Belady's Anomaly (it is a stack algorithm). "
    "<b>Implementation challenge:</b> True LRU requires tracking the exact time of last use "
    "for every page on every memory reference — too expensive in hardware."
)

en.section("LRU Implementation Approximations")
en.info_table(
    ["Implementation", "Description", "Hardware Cost"],
    [
        [
            "Counter-based LRU",
            "Each PTE has a 64-bit counter. On every memory access, copy clock to that page's counter. Evict the page with smallest counter.",
            "Hardware must update ALL PTE counters on every access — impractical.",
        ],
        [
            "Stack-based LRU",
            "Maintain a doubly-linked list of pages ordered by recency. On access, move page to top. On eviction, remove from bottom.",
            "Software overhead per access — too slow.",
        ],
        [
            "Reference bit approximation",
            "Hardware sets reference bit = 1 on any access. OS periodically shifts reference bits right and clears them. Evict page with all zeros.",
            "Low hardware cost. Used in practice by many OS.",
        ],
        [
            "Second-Chance (Clock) Algorithm",
            "FIFO queue with reference bits. On eviction: if ref bit = 1, give second chance (clear bit, move to back). If bit = 0, evict.",
            "Very practical. Used in Linux and BSD.",
        ],
    ],
)

en.section("Algorithm 4: Second-Chance (Clock) Algorithm")
en.definition(
    "<b>Second-Chance (Clock) Algorithm:</b> A practical LRU approximation. "
    "Pages arranged in a circular queue (clock hand). "
    "On page fault: examine page at clock hand. "
    "If reference bit = 0 → evict this page. "
    "If reference bit = 1 → give it a second chance: clear bit to 0, advance hand, repeat. "
    "A page with reference bit = 1 that just got cleared won't be evicted until the hand "
    "comes back around. Degenerates to FIFO when all bits are 0. "
    "Enhanced Clock uses both reference bit R and dirty bit M for better decisions."
)

en.section(
    "Worked Example — FIFO, LRU, Optimal (Reference String: 7,0,1,2,0,3,0,4,2,3,0,3,2, 3 frames)"
)
en.info_table(
    ["Algorithm", "Total Faults", "Hits", "Notes"],
    [
        ["FIFO", "10", "3", "No Belady anomaly visible in this example."],
        ["LRU", "9", "4", "Better than FIFO. Close to Optimal."],
        ["Optimal", "8", "5", "Lower bound — theoretical only."],
    ],
)

en.subsection("FIFO Trace (3 frames) — Ref: 7,0,1,2,0,3,0,4,2,3,0,3,2")
en.info_table(
    ["Ref", "Frame 0 (oldest)", "Frame 1", "Frame 2 (newest)", "Fault?"],
    [
        ["7", "7", "—", "—", "F"],
        ["0", "7", "0", "—", "F"],
        ["1", "7", "0", "1", "F"],
        ["2", "2", "0", "1", "F  (evict 7)"],
        ["0", "2", "0", "1", "Hit"],
        ["3", "2", "3", "1", "F  (evict 0)"],
        ["0", "2", "3", "0", "F  (evict 1)"],
        ["4", "4", "3", "0", "F  (evict 2)"],
        ["2", "4", "2", "0", "F  (evict 3)"],
        ["3", "4", "2", "3", "F  (evict 0)"],
        ["0", "0", "2", "3", "F  (evict 4)"],
        ["3", "0", "2", "3", "Hit"],
        ["2", "0", "2", "3", "Hit"],
    ],
)
en.note("FIFO Faults = 10, Hits = 3")

en.subsection("LRU Trace (3 frames) — same reference string")
en.info_table(
    ["Ref", "Frames (LRU→MRU)", "Fault?"],
    [
        ["7", "[7, —, —]", "F"],
        ["0", "[7, 0, —]", "F"],
        ["1", "[7, 0, 1]", "F"],
        ["2", "[0, 1, 2]  evict 7", "F"],
        ["0", "[1, 2, 0]  (0 hit)", "Hit"],
        ["3", "[2, 0, 3]  evict 1", "F"],
        ["0", "[2, 3, 0]  (0 hit)", "Hit"],
        ["4", "[3, 0, 4]  evict 2", "F"],
        ["2", "[0, 4, 2]  evict 3", "F"],
        ["3", "[4, 2, 3]  evict 0", "F"],
        ["0", "[2, 3, 0]  evict 4", "F"],
        ["3", "[2, 0, 3]  (3 hit)", "Hit"],
        ["2", "[0, 3, 2]  (2 hit)", "Hit"],
    ],
)
en.note("LRU Faults = 9, Hits = 4  |  LRU < FIFO in this example")

en.section(
    "Worked Example 2 — FIFO, LRU, Optimal (Ref: 1,2,3,4,2,1,5,6,2,1,2,3,7,6,3,2,1,2,3,6 | 3 frames)"
)
en.info_table(
    ["Algorithm", "Total Faults", "Notes"],
    [
        ["FIFO", "16", "Reference Unit I PYQ answer."],
        ["LRU", "15", "1 fewer fault than FIFO."],
        ["Optimal", "11", "Best possible — theoretical lower bound."],
    ],
)
en.br()

# =============================================================================
#  4.11  ALLOCATION OF FRAMES
# =============================================================================
en.chap_box("4.11  Allocation of Frames")

en.section("How Many Frames to Give Each Process?")
en.definition(
    "<b>Frame Allocation:</b> The OS must decide how many frames to allocate to each process. "
    "Minimum allocation: the minimum number of frames required to execute an instruction. "
    "(Determined by CPU architecture — e.g., indirect addressing may require 6 frames minimum.) "
    "Maximum allocation: total number of physical frames available. "
    "The allocation policy affects page fault rate and overall system performance."
)

en.section("Fixed Allocation Policies")
en.info_table(
    ["Policy", "Description", "Formula", "Pros / Cons"],
    [
        [
            "Equal Allocation",
            "Divide frames equally among all processes.",
            "Frames per process = total_frames / n_processes",
            "Simple. Ignores process size — small processes waste frames, large processes starve.",
        ],
        [
            "Proportional Allocation",
            "Allocate frames proportional to the process's logical address space size.",
            "Frames_i = (size_i / Σsize) × total_frames",
            "Fair relative to size. Still may not reflect actual memory need.",
        ],
        [
            "Priority-Based Allocation",
            "Allocate frames proportional to process priority (not size).",
            "High-priority processes get more frames.",
            "Better for real-time. Low-priority processes may starve.",
        ],
    ],
)

en.section("Local vs Global Replacement")
en.info_table(
    ["Strategy", "Description", "Effect"],
    [
        [
            "Local Replacement",
            "A process can only replace its OWN frames when it needs a new page. Each process has a fixed frame pool.",
            "Process performance depends only on its own behavior. One process cannot harm another. Limited flexibility.",
        ],
        [
            "Global Replacement",
            "A process can replace ANY frame (including frames belonging to other processes). The OS selects victim globally.",
            "Higher overall throughput — better frame utilisation. But one process can take frames from another, harming its performance. Used by most OS (Linux, Windows).",
        ],
    ],
)
en.br()

# =============================================================================
#  4.12  THRASHING
# =============================================================================
en.chap_box("4.12  Thrashing")

en.section("What is Thrashing?")
en.definition(
    "<b>Thrashing:</b> A condition where a process (or the whole system) spends more time "
    "handling page faults and swapping pages than doing useful computation. "
    "A process is thrashing when it does not have enough frames for its <b>working set</b> — "
    "every few memory accesses cause a page fault. "
    "The CPU utilisation drops sharply. "
    "If the OS sees low CPU utilisation, it may increase the degree of multiprogramming "
    "(add more processes), which makes thrashing worse — a vicious cycle."
)

en.section("Causes and Effects of Thrashing")
en.info_table(
    ["Cause", "Effect"],
    [
        [
            "Too few frames per process",
            "Every instruction requires a page fault — each access evicts a page the next instruction needs.",
        ],
        [
            "High degree of multiprogramming",
            "Many processes compete for a small pool of frames — all thrash simultaneously.",
        ],
        [
            "Poor page replacement algorithm",
            "Frequently-used pages are evicted prematurely.",
        ],
        [
            "CPU scheduling response to low utilisation",
            "OS detects low CPU use → loads more processes → fewer frames each → more faults → CPU even less used.",
        ],
    ],
)

en.section("Thrashing: CPU Utilisation vs Degree of Multiprogramming")
en.body(
    "As the number of processes increases, CPU utilisation first rises (good — more work done), "
    "then collapses suddenly as the system enters thrashing. "
    "The OS should detect the knee of the curve and prevent adding more processes beyond it."
)

en.section("Solution 1: Working Set Model")
en.definition(
    "<b>Working Set Model (Denning, 1968):</b> A process's working set W(t, Δ) at time t "
    "is the set of pages referenced in the last Δ memory references (working set window). "
    "The working set approximates the process's current locality — "
    "the set of pages it actively needs. "
    "If a process has enough frames for its entire working set, it will not thrash. "
    "The OS tracks working sets and suspends processes if the total frames needed "
    "exceeds physical memory."
)
en.formula_block(r"W(t, \Delta) = \{ \text{pages referenced in } (t - \Delta,\ t] \}")
en.bullet(
    [
        "If Σ|W(i)| > total frames → suspend a process to free frames.",
        "Δ too small → working set misses entire locality.",
        "Δ too large → working set encompasses too many pages (imprecise).",
        "Δ = ∞ → entire program in memory (no paging benefit).",
    ]
)

en.section("Solution 2: Page-Fault Frequency (PFF)")
en.definition(
    "<b>Page-Fault Frequency (PFF):</b> Monitor the actual page fault rate per process "
    "and use it as direct feedback to control frame allocation. "
    "Set an upper threshold and a lower threshold on the acceptable fault rate. "
    "If fault rate > upper threshold → process needs more frames (give it one). "
    "If fault rate < lower threshold → process has too many frames (take one back). "
    "If fault rate is too high and no free frames → suspend a process (reduce multiprogramming)."
)
en.br()

# =============================================================================
#  4.13  SECURITY IN OPERATING SYSTEM
# =============================================================================
en.part_box("UNIT IV — PART C: SECURITY IN OPERATING SYSTEM")
en.chap_box("4.13  Security in Operating Systems")

en.section("The Security Problem")
en.definition(
    "<b>Security Problem:</b> A computer system is secure if its resources are used "
    "and accessed as intended under all circumstances. "
    "Security requires preventing unauthorised access, modification, destruction, or "
    "disclosure of information. "
    "Security flaws can occur at hardware, OS, application, or network level — "
    "even one vulnerability in the chain can compromise the entire system. "
    "Security involves both technical measures and organisational policies."
)

en.section("Security Goals (CIA Triad + More)")
en.info_table(
    ["Goal", "Definition", "Example Threat"],
    [
        [
            "Confidentiality",
            "Prevent unauthorised disclosure of information.",
            "Eavesdropping, data leakage, keylogging",
        ],
        [
            "Integrity",
            "Prevent unauthorised modification of data or programs.",
            "Malware tampering, man-in-the-middle attack",
        ],
        [
            "Availability",
            "Ensure authorised users can access resources when needed.",
            "Denial of Service (DoS), ransomware",
        ],
        [
            "Authentication",
            "Verify the identity of users and programs.",
            "Password theft, phishing, spoofing",
        ],
        [
            "Non-repudiation",
            "Ensure a party cannot deny an action they performed.",
            "Transaction disputes, email forgery",
        ],
        [
            "Authorisation",
            "Ensure users can only access resources they are permitted to.",
            "Privilege escalation, access control bypass",
        ],
    ],
)

en.section("Common Security Threats and Attacks")
en.info_table(
    ["Threat Category", "Description", "Examples"],
    [
        [
            "Malware",
            "Malicious software designed to damage or gain unauthorised access.",
            "Viruses, worms, trojans, ransomware, spyware, rootkits",
        ],
        [
            "Social Engineering",
            "Manipulating users into revealing credentials or taking unsafe actions.",
            "Phishing, pretexting, baiting, spear-phishing",
        ],
        [
            "Buffer Overflow",
            "Writing past the end of a buffer to overwrite adjacent memory (stack frame, return address).",
            "Stack smashing, heap overflow, format string attacks",
        ],
        [
            "Privilege Escalation",
            "A process or user gains higher privileges than authorised.",
            "Kernel exploit, SUID abuse, container escape",
        ],
        [
            "Denial of Service",
            "Overwhelming a system/service to prevent legitimate use.",
            "SYN flood, UDP flood, DDoS, resource exhaustion",
        ],
        [
            "Man in the Middle",
            "Attacker intercepts communication between two parties.",
            "ARP poisoning, SSL stripping, Wi-Fi eavesdropping",
        ],
        [
            "SQL Injection",
            "Inserting malicious SQL into input fields to query/modify database.",
            "Authentication bypass, data extraction",
        ],
        [
            "Zero-Day Exploit",
            "Attack exploiting an unknown vulnerability before a patch exists.",
            "Stuxnet, Heartbleed (before disclosure)",
        ],
    ],
)

en.section("Levels Where Security Must Be Implemented")
stack_sec = ed.LayeredStack(
    width=en.CW * 0.55,
    height=220,
    theme=diag_theme,
    caption="Fig 4.4: Security must be enforced at all layers",
)
stack_sec.layer(
    "Application Security", sublabel="Input validation, authentication, secure coding"
)
stack_sec.layer("OS Security", sublabel="Access control, process isolation, patching")
stack_sec.layer("Network Security", sublabel="Firewalls, IDS/IPS, encryption, VPN")
stack_sec.layer(
    "Hardware Security", sublabel="TPM, secure boot, physical access control"
)
en.story.extend(stack_sec.as_flowable())
en.br()

# =============================================================================
#  4.14  SECURITY TECHNIQUES
# =============================================================================
en.chap_box("4.14  Security Techniques")

en.section("1. Authentication")
en.definition(
    "<b>Authentication:</b> The process of verifying the identity of a user, process, or device. "
    "Three factors of authentication: "
    "(1) <b>Something you know:</b> password, PIN, passphrase, security question. "
    "(2) <b>Something you have:</b> hardware token, smart card, OTP generator, phone (SMS/app). "
    "(3) <b>Something you are:</b> biometrics — fingerprint, iris scan, face recognition, voice. "
    "<b>Multi-Factor Authentication (MFA):</b> Requires 2+ factors — significantly stronger than single-factor."
)

en.info_table(
    ["Authentication Method", "How It Works", "Strength"],
    [
        [
            "Password (hashed + salted)",
            "User enters password; OS hashes with a random salt and compares to stored hash. Salt prevents rainbow table attacks.",
            "Moderate — vulnerable to brute force, phishing, reuse",
        ],
        [
            "One-Time Password (OTP)",
            "A fresh password generated for each login (TOTP/HOTP).",
            "Strong — not replayable even if intercepted",
        ],
        [
            "Public Key / Certificate",
            "User proves possession of private key corresponding to a registered public key.",
            "Very strong — used in SSH, TLS, code signing",
        ],
        [
            "Biometrics",
            "Physical or behavioural characteristics measured and compared.",
            "Strong for physical access; variable for remote",
        ],
        [
            "MFA (2FA/3FA)",
            "Combines multiple factors — knowledge + possession, or knowledge + biometric.",
            "Strongest practical scheme for user authentication",
        ],
    ],
)

en.section("2. Cryptography / Encryption")
en.definition(
    "<b>Encryption:</b> Transforming readable plaintext into unreadable ciphertext using a key. "
    "Only authorised parties with the correct key can decrypt. "
    "Protects confidentiality of data at rest and in transit."
)
en.info_table(
    ["Type", "Description", "Algorithms", "Use Cases"],
    [
        [
            "Symmetric Encryption",
            "Same key for encryption and decryption. Fast.",
            "AES-256, DES (obsolete), ChaCha20",
            "Disk encryption (AES), file encryption, VPN tunnels",
        ],
        [
            "Asymmetric (Public Key)",
            "Public key encrypts; private key decrypts. Slow.",
            "RSA-2048/4096, ECC, ElGamal",
            "TLS/HTTPS, SSH, digital signatures, key exchange",
        ],
        [
            "Hash Functions",
            "One-way transformation. Same input always gives same output. Not reversible.",
            "SHA-256, SHA-3, bcrypt (password), MD5 (obsolete)",
            "Password storage, data integrity verification, digital signatures",
        ],
    ],
)

en.section("3. Access Control")
en.definition(
    "<b>Access Control:</b> The mechanism that determines which users or processes can access "
    "which resources, and what operations they can perform. "
    "<b>DAC (Discretionary AC):</b> Resource owner controls access. Example: UNIX file permissions (rwxr-xr--). "
    "<b>MAC (Mandatory AC):</b> System enforces access based on security labels/classifications. Used in government systems. "
    "<b>RBAC (Role-Based AC):</b> Access based on user's role (admin, user, developer). Most common in enterprise. "
    "<b>ABAC (Attribute-Based AC):</b> Access based on attributes of user, resource, and environment. Most flexible."
)

en.section("4. Firewalls")
en.definition(
    "<b>Firewall:</b> A hardware or software system that monitors and controls incoming/outgoing "
    "network traffic based on predetermined security rules. "
    "Acts as a barrier between a trusted internal network and an untrusted external network."
)
en.info_table(
    ["Firewall Type", "How It Works", "Example"],
    [
        [
            "Packet Filter",
            "Examines each packet's IP header (source/dest IP, port, protocol). Stateless.",
            "iptables (Linux netfilter rules)",
        ],
        [
            "Stateful Inspection",
            "Tracks connection state; allows return traffic for established connections.",
            "Windows Firewall, most enterprise firewalls",
        ],
        [
            "Application Layer (WAF)",
            "Deep packet inspection; understands HTTP/FTP/DNS protocols; blocks malicious payloads.",
            "ModSecurity, Cloudflare WAF",
        ],
        [
            "Next-Gen Firewall (NGFW)",
            "Combines stateful inspection + application awareness + IDS/IPS integration.",
            "Palo Alto, Cisco ASA, FortiGate",
        ],
    ],
)

en.section("5. Intrusion Detection Systems (IDS)")
en.definition(
    "<b>IDS (Intrusion Detection System):</b> Monitors system or network activity for signs of attacks. "
    "<b>NIDS (Network IDS):</b> Monitors network traffic packets. "
    "<b>HIDS (Host IDS):</b> Monitors system calls, file changes, log files on a single host. "
    "<b>Signature-based IDS:</b> Compares activity against a database of known attack signatures. "
    "<b>Anomaly-based IDS:</b> Learns normal behaviour; flags deviations (catches zero-days but more false positives). "
    "<b>IPS (Intrusion Prevention System):</b> Like IDS but also actively blocks detected attacks."
)

en.section("6. Secure Boot and TPM")
en.info_table(
    ["Technique", "Description"],
    [
        [
            "Secure Boot",
            "UEFI firmware verifies that each bootloader and OS kernel is signed by a trusted key before executing. Prevents rootkits from loading before the OS.",
        ],
        [
            "TPM (Trusted Platform Module)",
            "Hardware chip that stores cryptographic keys, certificates, and measurements of system state. Used for disk encryption (BitLocker), attestation, and secure key storage.",
        ],
        [
            "Address Space Layout Randomisation (ASLR)",
            "OS randomises the memory addresses of stack, heap, and libraries on each execution. Makes buffer overflow exploits harder to target correctly.",
        ],
        [
            "Data Execution Prevention (DEP/NX)",
            "Hardware marks memory regions as either executable or writable but not both. Prevents shellcode injection into data regions (stack, heap).",
        ],
        [
            "Sandboxing",
            "Isolates a process or application in a restricted environment with limited system call access (e.g., browser tab, mobile app, container).",
        ],
    ],
)

en.section("7. Security at OS Level — Summary")
en.info_table(
    ["OS Security Mechanism", "Purpose"],
    [
        [
            "User accounts and UID/GID",
            "Each process runs under a user identity; enforced by kernel for every resource access.",
        ],
        [
            "UNIX file permissions (rwx)",
            "Owner/group/others permission bits control file read, write, execute access.",
        ],
        [
            "Capabilities (POSIX)",
            "Fine-grained privileges replacing binary root/non-root distinction.",
        ],
        [
            "SELinux / AppArmor",
            "Mandatory Access Control frameworks that confine programs to defined security policies.",
        ],
        [
            "Chroot / Containers / VMs",
            "Process isolation techniques that limit resource access and contain breaches.",
        ],
        [
            "System call filtering (seccomp)",
            "Restrict which system calls a process can make — used in sandboxes (Chrome, Docker).",
        ],
        [
            "Audit logging",
            "Record security-relevant events (logins, file access, privilege changes) for forensic analysis.",
        ],
    ],
)
en.br()

# =============================================================================
#  MASTER COMPARISON & FORMULA TABLES
# =============================================================================
en.chap_box("Unit IV — Master Summary Tables")

en.section("Page Replacement Algorithms — Comparison")
en.info_table(
    [
        "Algorithm",
        "Victim Selection",
        "Belady's Anomaly",
        "Implementable?",
        "Performance",
    ],
    [
        [
            "FIFO",
            "Oldest page (first in)",
            "YES — more frames can mean more faults!",
            "Yes — simple queue",
            "Poor to moderate",
        ],
        [
            "Optimal (OPT)",
            "Furthest future use",
            "No (stack algorithm)",
            "NO — needs future knowledge",
            "Best possible (theoretical)",
        ],
        [
            "LRU",
            "Least recently used (longest ago used)",
            "No (stack algorithm)",
            "Approximate in practice",
            "Close to Optimal",
        ],
        [
            "Second-Chance",
            "LRU approx. using reference bit + FIFO",
            "No",
            "Yes — clock pointer + ref bits",
            "Good practical performance",
        ],
        [
            "Enhanced Clock",
            "Uses R bit + D bit (dirty)",
            "No",
            "Yes",
            "Better than basic Second-Chance",
        ],
    ],
)

en.section("Virtual Memory Key Formulas")
en.info_table(
    ["Formula", "Variables", "Use"],
    [
        [
            "Physical Addr = f × page_size + d",
            "f=frame#, d=offset",
            "Basic paging address translation",
        ],
        [
            "Page number p = logical_addr >> n",
            "n = log2(page_size)",
            "Extract page number from logical address",
        ],
        [
            "Offset d = logical_addr & (page_size − 1)",
            "n = log2(page_size)",
            "Extract page offset from logical address",
        ],
        [
            "EAT = h×(t_TLB+t_m) + (1−h)×(t_TLB+2t_m)",
            "h=hit ratio",
            "Effective access time with TLB",
        ],
        [
            "EAT = (1−p)×t_m + p×t_fault",
            "p=page fault rate",
            "Access time with demand paging",
        ],
        [
            "Frames_i = (size_i / Σsize) × total_frames",
            "Proportional allocation",
            "Frame allocation per process",
        ],
        [
            "Page table entries = logical_addr_space / page_size",
            "",
            "Number of entries in page table",
        ],
        [
            "Page table size = entries × PTE_size",
            "PTE_size = 4 or 8 bytes",
            "Memory consumed by page table",
        ],
    ],
)
en.br()

# =============================================================================
#  4.15  EXAM QUESTIONS & ANSWERS
# =============================================================================
en.part_box("UNIT IV — EXAM QUESTIONS & DETAILED ANSWERS")
en.chap_box("4.15  Previous-Year Style Exam Questions")

en.section("2-Mark Questions")

en.highlight(
    "<b>Q1. What is paging? How does it avoid external fragmentation?</b><br/>"
    "A: Paging divides physical memory into fixed-size frames and logical memory into same-size pages. "
    "Any free frame can hold any page — there is no requirement for contiguous physical allocation. "
    "Therefore external fragmentation is completely eliminated. "
    "Only internal fragmentation remains (last page may be partially filled). "
    "Address translation: CPU generates (page#, offset) → page table gives frame# → physical = frame×size + offset."
)

en.highlight(
    "<b>Q2. What is a TLB? What is its purpose?</b><br/>"
    "A: TLB (Translation Lookaside Buffer) is a small, fast, fully-associative hardware cache "
    "inside the MMU that stores recent page-to-frame translations. "
    "Without TLB, every memory access requires 2 RAM accesses (page table + data). "
    "With TLB hit: only 1 RAM access needed. "
    "EAT = h×(t_TLB + t_mem) + (1−h)×(t_TLB + 2×t_mem). "
    "Hit ratios of 90–99% give near-single-access performance."
)

en.highlight(
    "<b>Q3. What is a page fault? List the steps to handle it.</b><br/>"
    "A: A page fault occurs when a process accesses a page with valid bit = 0 in its PTE "
    "(page not in RAM). "
    "Handling steps: "
    "(1) MMU raises page fault trap → OS handler. "
    "(2) Check if reference is legal (in process's VAS). "
    "(3) Find a free frame (or evict a victim). "
    "(4) Load the page from disk into the frame. "
    "(5) Update PTE: frame#, valid bit = 1. "
    "(6) Restart the faulting instruction."
)

en.highlight(
    "<b>Q4. What is virtual memory? State its benefits.</b><br/>"
    "A: Virtual memory allows a process to execute when only PART of it is in RAM — "
    "the rest resides on disk. "
    "Benefits: (1) Programs larger than RAM can run. "
    "(2) More processes can share RAM simultaneously. "
    "(3) Fast process startup (only entry page needed). "
    "(4) Copy-on-Write for efficient fork(). "
    "(5) Shared library pages shared across processes. "
    "(6) Memory-mapped file I/O."
)

en.highlight(
    "<b>Q5. Differentiate between segmentation and paging.</b><br/>"
    "A: Paging: fixed-size units (pages/frames), no external fragmentation, "
    "yes internal fragmentation, programmer-invisible, hardware-managed. "
    "Segmentation: variable-size units matching logical program structure, "
    "yes external fragmentation, no internal fragmentation, programmer-visible "
    "(code/data/stack named), protects at segment level. "
    "Modern systems (x86-64) use paging only — segmentation mostly disabled."
)

en.highlight(
    "<b>Q6. What is demand paging? How does it differ from regular paging?</b><br/>"
    "A: Regular (pre-loading) paging loads all pages at process startup. "
    "Demand paging: pages loaded only when accessed for the first time — lazy loading. "
    "Process starts with 0 pages in RAM; first instruction causes page fault; "
    "OS loads only the needed page. "
    "Benefits: reduced startup time, less memory usage, more processes can fit in RAM. "
    "Cost: page fault overhead on first access to each page."
)

en.highlight(
    "<b>Q7. What is Belady's Anomaly? Which algorithms suffer from it?</b><br/>"
    "A: Belady's Anomaly: increasing the number of frames can INCREASE the number of page faults. "
    "Counter-intuitive — more memory = more faults. "
    "Example: FIFO with ref string 1,2,3,4,1,2,5,1,2,3,4,5: "
    "3 frames → 9 faults, 4 frames → 10 faults. "
    "ONLY FIFO suffers from Belady's Anomaly. "
    "LRU, Optimal, and all stack algorithms do NOT."
)

en.highlight(
    "<b>Q8. What is thrashing? What causes it and how can it be prevented?</b><br/>"
    "A: Thrashing: a process spends more time handling page faults than executing useful code. "
    "CPU utilisation drops sharply. "
    "Cause: process does not have enough frames for its working set. "
    "OS may add more processes (thinking CPU is underutilised), worsening thrashing. "
    "Prevention: (1) Working Set Model — allocate enough frames for each process's working set. "
    "(2) Page-Fault Frequency — if fault rate > upper bound → give more frames; "
    "if no free frames → suspend a process."
)

en.highlight(
    "<b>Q9. What is the CIA triad in OS security?</b><br/>"
    "A: CIA = Confidentiality, Integrity, Availability. "
    "Confidentiality: prevent unauthorised disclosure (encrypt data). "
    "Integrity: prevent unauthorised modification (checksums, signatures). "
    "Availability: ensure authorised users can access resources (prevent DoS). "
    "All three must be maintained for a system to be considered secure."
)

en.highlight(
    "<b>Q10. What is ASLR? Why is it used?</b><br/>"
    "A: ASLR (Address Space Layout Randomisation): OS randomises the base addresses of "
    "stack, heap, libraries, and executable on each run. "
    "Used to prevent buffer overflow exploits — an attacker cannot hardcode target addresses "
    "because they are different on every execution. "
    "Combined with DEP/NX (data not executable), it makes memory-based exploits much harder. "
    "Supported by Linux, Windows (Vista+), macOS."
)

en.section("5-Mark Questions")

en.highlight(
    "<b>Q11. Explain paging address translation with a diagram. "
    "Calculate physical address for: page size = 1 KB, page number = 3, "
    "offset = 100, frame number for page 3 = 7.</b><br/>"
    "A: Logical address = (p=3, d=100). Page table lookup: frame[3] = 7. "
    "Physical address = 7 × 1024 + 100 = 7168 + 100 = 7268. "
    "Translation: CPU generates logical address → split into (p, d) → "
    "page table indexed by p → frame number f → physical = f × page_size + d. "
    "See Fig 4.1 for full sequence diagram."
)

en.highlight(
    "<b>Q12. Calculate EAT given: t_mem = 200 ns, t_TLB = 20 ns, hit ratio = 0.85.</b><br/>"
    "A: EAT = h × (t_TLB + t_mem) + (1−h) × (t_TLB + 2×t_mem). "
    "EAT = 0.85 × (20 + 200) + 0.15 × (20 + 400). "
    "EAT = 0.85 × 220 + 0.15 × 420. "
    "EAT = 187 + 63 = 250 ns. "
    "Compare: no TLB would give 2 × 200 = 400 ns. "
    "TLB reduces access time from 400 ns to 250 ns — 37.5% improvement."
)

en.highlight(
    "<b>Q13. Compare FIFO, LRU, and Optimal page replacement with a worked example. "
    "Reference string: 1,2,3,4,1,2,5,1,2,3,4,5  |  3 frames.</b><br/>"
    "A: FIFO trace: Faults when pages must be evicted. "
    "FIFO order = page loaded first is evicted first. "
    "LRU trace: Evict the page not used for the longest time. "
    "Optimal trace: Evict the page used furthest in the future. "
    "Results: FIFO = 9 faults, LRU = 9 faults, Optimal = 7 faults. "
    "If FIFO is given 4 frames: faults = 10 (more than 3 frames!) — this is Belady's Anomaly. "
    "LRU with 4 frames: faults = 8 — no anomaly."
)

en.highlight(
    "<b>Q14. Explain segmentation with paging. Draw the address translation diagram.</b><br/>"
    "A: Logical address = (segment s, page p, offset d). "
    "Step 1: Segment table[s] → gives base address of page table for segment s. "
    "Step 2: Page table[p] → gives frame number f. "
    "Step 3: Physical address = f × page_size + d. "
    "Combines benefits of segmentation (logical programmer view, protection per segment) "
    "with paging (no external fragmentation, flexible allocation). "
    "Intel x86 architecture uses this scheme — but modern OSes set segment base = 0 "
    "and treat address space as flat, using only paging."
)

en.highlight(
    "<b>Q15. Explain the Working Set Model for thrashing prevention. Define W(t, Δ).</b><br/>"
    "A: W(t, Δ) = set of pages referenced in the most recent Δ accesses (working set window). "
    "The working set approximates the process's current locality. "
    "Algorithm: (1) Track W for each process. "
    "(2) Allocate |W(i)| frames to process i. "
    "(3) If Σ|W(i)| > total frames → reduce degree of multiprogramming "
    "(suspend a process until Σ|W(i)| ≤ total frames). "
    "Key insight: a process must have at least |W(i)| frames to avoid thrashing."
)

en.section("10-Mark Questions")

en.highlight(
    "<b>Q16. Explain paging and virtual memory in detail. Include: "
    "page table, TLB, EAT calculation, demand paging, page fault handling, "
    "and page replacement algorithms (FIFO, LRU, Optimal) with a numerical example.</b><br/>"
    "A: <b>Paging:</b> Physical memory in frames; logical in pages. "
    "Page table maps p → f. Physical = f × size + d. No external fragmentation. "
    "<b>TLB:</b> Fast cache for page translations. EAT = h×(t_TLB+t_m) + (1−h)×(t_TLB+2t_m). "
    "<b>Demand Paging:</b> Pages loaded on first access. Valid bit = 0 → page fault → load page → restart. "
    "<b>Page Fault:</b> Trap → find page on disk → free/evict frame → load → update PTE → restart. "
    "<b>Page Replacement:</b> FIFO (oldest evicted, Belady possible), "
    "LRU (LRU evicted, no Belady, near-Optimal), "
    "Optimal (best possible, unimplementable). "
    "For ref string 7,0,1,2,0,3,0,4,2,3,0,3,2 with 3 frames: "
    "FIFO=10, LRU=9, Optimal=8 faults. See Section 4.10."
)

en.highlight(
    "<b>Q17. Explain security in operating systems comprehensively. "
    "Cover: security goals, threats, authentication methods, encryption, "
    "access control, firewalls, and OS-level security mechanisms.</b><br/>"
    "A: <b>Security Goals (CIA+):</b> Confidentiality, Integrity, Availability, "
    "Authentication, Authorisation, Non-repudiation. "
    "<b>Threats:</b> Malware, buffer overflow, privilege escalation, DoS, social engineering, SQL injection. "
    "<b>Authentication:</b> Something you know/have/are; MFA combines multiple factors. "
    "<b>Encryption:</b> Symmetric (AES for speed), Asymmetric (RSA/ECC for key exchange), "
    "Hash (SHA-256 for integrity, bcrypt for passwords). "
    "<b>Access Control:</b> DAC (owner-controlled), MAC (system-enforced labels), RBAC (role-based). "
    "<b>Firewalls:</b> Packet filter, stateful inspection, application-layer (WAF). "
    "<b>OS Mechanisms:</b> UID/GID, file permissions (rwx), capabilities, SELinux, "
    "seccomp, ASLR, DEP/NX, secure boot, TPM, sandboxing. "
    "See Section 4.13–4.14."
)

en.section("Quick Revision Table — Unit IV")
en.info_table(
    ["Topic", "Key Exam Points"],
    [
        [
            "Paging basics",
            "Page=logical, Frame=physical. Size equal. Page table maps p→f. Physical=f×size+d.",
        ],
        [
            "Internal fragmentation",
            "Last page may not fill a frame. Avg = half page per process.",
        ],
        ["External fragmentation", "ZERO — paging eliminates it completely."],
        [
            "Hierarchical paging",
            "Multi-level page tables. 32-bit→2 levels. 64-bit→4 levels. Only sparse pages allocated.",
        ],
        [
            "Inverted page table",
            "ONE table for all physical frames. Entry=(PID, page#). Saves memory; search with hash.",
        ],
        [
            "TLB",
            "Fast MMU cache for page translations. Hit ratio 90–99%. ASID avoids flush on context switch.",
        ],
        [
            "EAT formula",
            "EAT = h×(t_TLB+t_m) + (1−h)×(t_TLB+2t_m). Higher h → EAT closer to single access.",
        ],
        [
            "Page fault",
            "Valid bit=0 → trap → find page → free frame → load → update PTE → restart instruction.",
        ],
        [
            "Demand paging",
            "Lazy loading. Pages loaded only on first access. Enables virtual memory > physical RAM.",
        ],
        [
            "COW",
            "fork() shares pages read-only. Private copy made only on first write. Used in Linux.",
        ],
        [
            "Segmentation",
            "Variable-size named units (code, data, stack). External frag. Protection per segment.",
        ],
        [
            "Seg with paging",
            "Each segment has its own page table. Eliminates external frag, keeps logical view.",
        ],
        ["FIFO replacement", "Evict oldest. Simple. Belady's Anomaly possible."],
        [
            "LRU replacement",
            "Evict LRU page. No Belady. Near-Optimal. Expensive to implement exactly.",
        ],
        [
            "Optimal replacement",
            "Evict furthest future use. Best faults. Cannot implement. Benchmark only.",
        ],
        [
            "Belady's Anomaly",
            "FIFO: more frames → more faults. LRU and Optimal immune (stack algorithms).",
        ],
        [
            "Second-Chance (Clock)",
            "FIFO + reference bit. If R=1: clear + move on. If R=0: evict. Practical LRU approximation.",
        ],
        [
            "Frame allocation",
            "Equal, proportional (by size), or priority-based. Local vs global replacement.",
        ],
        [
            "Thrashing",
            "More faulting than executing. Cause: too few frames for working set. Fix: WSM or PFF.",
        ],
        [
            "Working Set Model",
            "W(t,Δ): pages used in last Δ refs. Allocate |W| frames. Suspend if Σ|W| > total frames.",
        ],
        [
            "Security CIA",
            "Confidentiality + Integrity + Availability. All three required for secure system.",
        ],
        [
            "Authentication factors",
            "Know (password) + Have (token/OTP) + Are (biometric). MFA = 2+ factors.",
        ],
        [
            "Encryption types",
            "Symmetric (AES, same key, fast). Asymmetric (RSA, public/private, slow). Hash (SHA-256).",
        ],
        [
            "Access control",
            "DAC (owner decides), MAC (system labels), RBAC (role-based). Most OS uses DAC+RBAC.",
        ],
        [
            "ASLR + DEP/NX",
            "ASLR: randomise memory layout → defeats hardcoded exploit addresses. DEP: data not executable.",
        ],
        [
            "Firewall types",
            "Packet filter (IP/port), stateful (connection tracking), application (deep inspection).",
        ],
    ],
)

en.exam(
    "Most asked topics in IT412 Unit IV exams: "
    "(1) Paging address translation with numerical — calculate physical address from (page#, offset, frame#). "
    "(2) TLB EAT calculation — substitute values into formula. "
    "(3) Page replacement FIFO, LRU, Optimal — trace for a given reference string with 3 frames. "
    "(4) Explain thrashing with causes and Working Set Model solution. "
    "(5) Segmentation vs paging comparison table. "
    "(6) OS security — CIA triad, authentication methods, encryption types. "
    "Always show step-by-step page table traces when solving page replacement numericals."
)

en.note(
    "Unit IV builds on Unit III (paging replaces contiguous allocation; no external fragmentation). "
    "Unit IV page replacement connects to Unit II (scheduling criteria) — "
    "page fault rate = a new 'criterion' for memory performance. "
    "Reference: Silberschatz Chapters 8–9 (Paging, Virtual Memory), Chapter 15 (Security). "
    "CO4: Demonstrate paging and segmentation. CO target for Unit IV."
)

# =============================================================================
#  FLASHCARDS & REVISION
# =============================================================================
en.br()
en.chap_box("Rapid Revision & Flashcards")

en.revision_card(
    "Unit IV Mastery Check",
    [
        "Calculate physical address given: page size, page number, offset, and frame number.",
        "Compute EAT given TLB access time, memory access time, and hit ratio.",
        "Trace FIFO, LRU, and Optimal page replacement for a given reference string.",
        "Explain the six steps of page fault handling in order.",
        "Describe the Working Set Model and explain how it prevents thrashing.",
        "Compare symmetric and asymmetric encryption — when is each used?",
    ],
)

en.flashcard(
    "Paging: <b>Physical Address</b> formula",
    "Physical Address = Frame# × Page_Size + Offset. "
    "Page# = Logical_Address >> n  (upper bits, n = log2 page_size). "
    "Offset = Logical_Address & (Page_Size − 1)  (lower n bits).",
)
en.flashcard(
    "<b>TLB Effective Access Time (EAT)</b>",
    "EAT = h × (t_TLB + t_mem) + (1−h) × (t_TLB + 2×t_mem). "
    "h = hit ratio. t_TLB = TLB access time. t_mem = memory access time.",
)
en.flashcard(
    "<b>Belady's Anomaly</b>",
    "FIFO page replacement: more frames can cause MORE page faults. "
    "LRU and Optimal are stack algorithms — immune to Belady's Anomaly.",
)
en.flashcard(
    "<b>Thrashing</b> — definition and fix",
    "Thrashing: more time handling page faults than executing. "
    "Fix 1: Working Set Model — allocate |W(t,Δ)| frames. "
    "Fix 2: Page-Fault Frequency — adjust frames based on fault rate.",
)
en.flashcard(
    "<b>CIA Triad</b> in OS Security",
    "Confidentiality: prevent unauthorised disclosure. "
    "Integrity: prevent unauthorised modification. "
    "Availability: ensure authorised access is possible.",
)
en.flashcard(
    "Segmentation vs Paging: key difference",
    "Paging: fixed-size units, no external frag, programmer-invisible. "
    "Segmentation: variable-size named units (code/data/stack), external frag, programmer-visible.",
)

en.br()
en.chap_box("Index")
en.print_index()

# =============================================================================
#  BUILD DOCUMENT
# =============================================================================
en.build_doc("OS_Unit4_Notes.pdf")

print("Generated: OS_Unit4_Notes.pdf")
