"""
Computer Architecture (IT-404) -- Unit IV Notes
UIT-RGPV (Autonomous) Bhopal | Semester IV
Complete exam notes with vector diagrams.
Run: python ca_unit4_notes.py
Output: CA_Unit4_Notes.pdf
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
en.set_theme(en.OCEAN_DARK)

diag_theme = ed.DiagramTheme.from_notes_theme(en.get_theme())

# =============================================================================
#  COVER PAGE
# =============================================================================
en.bookmark("Cover Page")
en.suppress_footer(page_only=True)
en.sp(28)
t = Table(
    [
        [Paragraph("COMPUTER ARCHITECTURE", en.COVER_H1)],
        [Paragraph("Unit IV -- Complete Exam Notes", en.COVER_H2)],
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
en.add(
    Paragraph(
        "Prepared by: Bharat Dangi  |  Subject Code: IT-404  |  UIT-RGPV (Autonomous) Bhopal",
        en.COVER_SUB,
    )
)
en.add(Paragraph("Semester IV  |  Based on University Syllabus 2024-25", en.COVER_SUB))
en.sp(10)
en.rule(en.get_theme().rl(en.get_theme().accent), 1.5)
en.sp(8)

en.info_table(
    ["Topic", "Coverage"],
    [
        [
            "4.1 Computer Memory System Overview",
            "Types, classification, characteristics",
        ],
        [
            "4.2 Memory Hierarchy",
            "Hierarchy levels, cost-speed trade-off, locality of reference",
        ],
        [
            "4.3 Main Memory -- RAM",
            "SRAM vs DRAM, internal organisation, refresh, chip select",
        ],
        ["4.4 Main Memory -- ROM", "ROM types: Masked, PROM, EPROM, EEPROM, Flash"],
        [
            "4.5 Memory Address Map",
            "Address assignment, chip select logic, address decoding",
        ],
        ["4.6 Auxiliary Memory", "Magnetic disk, magnetic tape, optical storage"],
        [
            "4.7 Associative Memory (CAM)",
            "Content-addressable, argument register, key register, match logic",
        ],
        ["4.8 Cache Memory", "Cache concept, hit ratio, average access time"],
        [
            "4.9 Cache Mapping -- Direct",
            "Direct mapping, tag/block/word fields, address partition",
        ],
        [
            "4.10 Cache Mapping -- Associative",
            "Full associative, tag/word fields, CAM-based lookup",
        ],
        [
            "4.11 Cache Mapping -- Set-Associative",
            "k-way sets, tag/set/word fields, worked examples",
        ],
        [
            "4.12 Cache Write Policy",
            "Write-through, buffered write-through, write-back",
        ],
        [
            "4.13 Cache Performance",
            "Hit ratio, miss penalty, average access time calculation",
        ],
        ["4.14 Cache Replacement Algorithms", "LRU, FIFO, LFU, Random"],
        [
            "4.15 Virtual Memory",
            "Address space vs memory space, virtual-to-physical mapping",
        ],
        ["4.16 Address Mapping -- Paging", "Page table, presence bit, page fault, TLB"],
        [
            "4.17 Segmentation",
            "Segments, logical address, segment table, page-segment combined",
        ],
        [
            "4.18 TLB -- Translation Lookaside Buffer",
            "Associative page table, TLB hit/miss, effective access time",
        ],
        [
            "4.19 Page Fault and Replacement",
            "Page fault handling, FIFO, LRU, Optimal algorithms",
        ],
        ["4.20 Quick Revision Summary", "Key formulas, tables, and exam flashcards"],
    ],
)
en.br()
en.suppress_footer(page_only=True)
en.toc()

# =============================================================================
#  UNIT DIVIDER
# =============================================================================
en.footer(
    left="IT-404: Computer Architecture", right="Unit IV Notes", show_page_num=True
)
en.part_box("UNIT IV -- COMPUTER MEMORY SYSTEM")

# =============================================================================
#  4.1  COMPUTER MEMORY SYSTEM OVERVIEW
# =============================================================================
en.chap_box("4.1  Computer Memory System Overview")
en.section("Classification of Memory")
en.definition(
    "<b>Computer Memory:</b> Any device that can store binary information (0s and 1s) "
    "for later retrieval. Computer memories differ in speed, cost, capacity, and "
    "volatility. The memory system of a modern computer is organized as a hierarchy "
    "of different memory types to achieve the best balance of performance and cost."
)

en.info_table(
    ["Characteristic", "Description", "Examples"],
    [
        ["Access time", "Time to read or write one word", "RAM: 5-100ns, Disk: 3-10ms"],
        [
            "Capacity",
            "Total number of bits storable",
            "Cache: KB-MB, RAM: GB, Disk: TB",
        ],
        ["Cost per bit", "Price to store one bit", "SRAM>DRAM>Flash>Disk>Tape"],
        [
            "Volatility",
            "Does data survive power-off?",
            "RAM: volatile, ROM/Disk: non-volatile",
        ],
        [
            "Access method",
            "How data is located",
            "Random (RAM), Sequential (tape), Direct (disk)",
        ],
        [
            "Transfer unit",
            "How many bits move at once",
            "Bit (serial), Word (parallel), Block (disk)",
        ],
    ],
)

en.section("Semiconductor Memory Classification")
en.body(
    "Semiconductor memory is the primary technology for main memory and cache. "
    "It divides into two families: <b>Read/Write Memory (RAM)</b> which can be "
    "both read and written during normal operation, and <b>Read-Only Memory (ROM)</b> "
    "which is programmed once (or rarely) and only read during normal operation."
)

mem_tree = ed.NetworkDiagram(
    width=en.CW,
    height=240,
    theme=diag_theme,
    caption="Fig 1: Classification of semiconductor memory",
)
# Manual coordinate placement to ensure wide horizontal spacing (zero collision)
mem_tree.node("mem", "Semiconductor Memory", x=222, y=185, kind="server")
mem_tree.node("ram", "Read/Write (RAM)", x=100, y=115, kind="generic")
mem_tree.node("rom", "Read Only (ROM)", x=345, y=115, kind="generic")

mem_tree.node("sram", "Static RAM\n(SRAM)", x=55, y=45, kind="host")
mem_tree.node("dram", "Dynamic RAM\n(DRAM)", x=145, y=45, kind="host")

mem_tree.node("masked", "Masked ROM", x=235, y=45, kind="host")
mem_tree.node("prom", "PROM", x=310, y=45, kind="host")
mem_tree.node("eprom", "EPROM", x=385, y=45, kind="host")
mem_tree.node("eeprom", "EEPROM / Flash", x=460, y=45, kind="host")

mem_tree.link("mem", "ram")
mem_tree.link("mem", "rom")
mem_tree.link("ram", "sram")
mem_tree.link("ram", "dram")
mem_tree.link("rom", "masked")
mem_tree.link("rom", "prom")
mem_tree.link("rom", "eprom")
mem_tree.link("rom", "eeprom")
en.story.extend(mem_tree.as_flowable())
en.br()

# =============================================================================
#  4.2  MEMORY HIERARCHY
# =============================================================================
en.chap_box("4.2  Memory Hierarchy")
en.section("Why a Hierarchy?")
en.definition(
    "<b>Memory Hierarchy:</b> A layered organisation of memory types arranged by speed, "
    "cost, and capacity. Faster memories are more expensive per bit and smaller in capacity, "
    "so they sit at the top of the hierarchy in small quantities. Slower, cheaper, larger "
    "memories sit at the bottom. The CPU sees only the top levels but benefits from the "
    "large capacity of lower levels through automatic data movement managed by hardware and OS."
)
en.body(
    "The hierarchy works because of the <b>principle of locality of reference</b>: programs "
    "tend to access a small set of memory locations repeatedly over short periods of time "
    "(temporal locality) and to access locations near recently accessed locations (spatial locality)."
)

en.section("Locality of Reference")
en.info_table(
    ["Type", "Definition", "Example", "Exploited By"],
    [
        [
            "Temporal locality",
            "Recently accessed locations are likely to be accessed again soon",
            "Loop counter variable accessed every iteration",
            "Cache memory keeps recently accessed blocks",
        ],
        [
            "Spatial locality",
            "Locations near recently accessed locations are likely to be accessed soon",
            "Array elements accessed sequentially",
            "Cache loads full cache lines (16-64 bytes at once)",
        ],
    ],
)

en.section("Memory Hierarchy Levels")
hier_stack = ed.LayeredStack(
    width=en.CW,
    height=310,
    theme=diag_theme,
    caption="Fig 2: Memory hierarchy -- speed decreases and capacity increases downward",
)
hier_stack.layer(
    "CPU Registers",
    sublabel="~0-1 cycle  |  32-256 bytes  |  SRAM flip-flops  |  Highest cost/bit",
)
hier_stack.layer(
    "L1 Cache (on-chip)",
    sublabel="~4 cycles   |  16-64 KB      |  SRAM  |  Built into CPU die",
)
hier_stack.layer(
    "L2 Cache (on-chip)",
    sublabel="~12 cycles  |  256KB - 2MB   |  SRAM  |  On-chip, slightly larger",
)
hier_stack.layer(
    "L3 Cache (shared)",
    sublabel="~30-40 cycles | 4-32MB       |  SRAM  |  Shared among cores",
)
hier_stack.divider()
hier_stack.layer(
    "Main Memory (RAM)",
    sublabel="~50-300 cycles | 4-64 GB     |  DRAM  |  Moderate cost, volatile",
)
hier_stack.divider()
hier_stack.layer(
    "SSD / NVMe Storage",
    sublabel="~10K cycles  |  128GB-4TB    |  NAND Flash  |  Non-volatile, fast disk",
)
hier_stack.layer(
    "HDD / Magnetic Disk",
    sublabel="~10M cycles  |  500GB-20TB   |  Magnetic  |  Cheap, slow, non-volatile",
)
hier_stack.layer(
    "Magnetic Tape / Archive",
    sublabel="~100M cycles |  TB range     |  Magnetic  |  Lowest cost/bit",
)
en.story.extend(hier_stack.as_flowable())

en.info_table(
    ["Level", "Technology", "Typical Size", "Access Time", "Managed By"],
    [
        ["Registers", "SRAM FF", "Bytes", "<1 ns", "Compiler / programmer"],
        ["L1 Cache", "SRAM", "32-64 KB", "~1-2 ns", "Hardware (cache controller)"],
        ["L2 Cache", "SRAM", "256KB-2MB", "~5-10 ns", "Hardware (cache controller)"],
        ["L3 Cache", "SRAM", "4-32 MB", "~20-40 ns", "Hardware (cache controller)"],
        ["Main Memory", "DRAM", "4-64 GB", "~50-100 ns", "OS / hardware"],
        ["SSD", "NAND Flash", "256GB-4TB", "~50-100 us", "OS file system"],
        ["HDD", "Magnetic disk", "500GB-20TB", "~5-10 ms", "OS file system"],
        ["Tape", "Magnetic tape", "TB+", "seconds", "Operator / backup system"],
    ],
)
en.tip(
    "Memory hierarchy: Speed DOWN, Capacity UP, Cost DOWN as you go lower. "
    "Locality of reference is why caches work: programs reuse the same small set of locations. "
    "Each level acts as a buffer for the level below. "
    "L1 hit: ~4 cycles. L2 hit: ~12 cycles. RAM: ~200 cycles. Disk: millions of cycles."
)
en.br()

# =============================================================================
#  4.3  MAIN MEMORY -- RAM
# =============================================================================
en.chap_box("4.3  Main Memory -- RAM (SRAM and DRAM)")
en.section("Static RAM (SRAM)")
en.definition(
    "<b>SRAM (Static Random-Access Memory):</b> Uses a <b>flip-flop</b> circuit (typically "
    "4-6 transistors per bit) to store each bit. Once written, the bit remains stable as long "
    "as power is applied -- no periodic refresh is needed. SRAM is much faster than DRAM "
    "but occupies more chip area and consumes more power per bit. Used for CPU cache memories."
)
en.bullet(
    [
        "<b>Cell structure:</b> 4-transistor or 6-transistor cross-coupled inverter (bistable latch).",
        "<b>Refresh:</b> Not required. The flip-flop holds its state indefinitely while powered.",
        "<b>Access time:</b> 0.5 ns to 5 ns (very fast).",
        "<b>Density:</b> Low (6 transistors per cell vs 1 transistor + 1 capacitor for DRAM).",
        "<b>Applications:</b> CPU registers, L1/L2/L3 cache, TLB, small buffer memories.",
    ]
)

en.section("Dynamic RAM (DRAM)")
en.definition(
    "<b>DRAM (Dynamic Random-Access Memory):</b> Stores each bit as a charge in a "
    "<b>capacitor</b> (1 transistor + 1 capacitor per bit). The capacitor leaks charge "
    "over time (in milliseconds), so the memory must be <b>periodically refreshed</b> -- "
    "the charge is read and rewritten before it discharges to zero. DRAM is much denser "
    "and cheaper than SRAM but slower. Used for main memory."
)
en.bullet(
    [
        "<b>Cell structure:</b> 1 transistor (switch) + 1 capacitor (storage).",
        "<b>Refresh:</b> Required every 8-64 ms. During refresh the row is read and rewritten.",
        "<b>Access time:</b> 10-100 ns (slower than SRAM due to sense amplifiers and refresh).",
        "<b>Density:</b> Very high -- billions of cells per chip.",
        "<b>Applications:</b> Main system RAM (DDR4, DDR5 are types of DRAM).",
    ]
)

en.section("SRAM vs DRAM Comparison")
en.info_table(
    ["Property", "SRAM", "DRAM"],
    [
        [
            "Storage element",
            "Flip-flop (6 transistors)",
            "Capacitor + transistor (2 components)",
        ],
        ["Refresh needed", "No", "Yes (every 8-64 ms)"],
        ["Speed", "Very fast (0.5-5 ns)", "Slower (10-100 ns)"],
        ["Cell area", "Large (6T)", "Small (1T+1C)"],
        ["Cost per bit", "High", "Low"],
        ["Density", "Low", "High (Gb per chip)"],
        [
            "Power consumption",
            "Higher (active gates)",
            "Lower idle, but refresh adds power",
        ],
        ["Volatility", "Volatile", "Volatile"],
        ["Application", "Cache, registers", "Main memory (DDR4/5, LPDDR)"],
    ],
)

en.section("Typical RAM Chip Organization")
en.body(
    "A RAM chip is characterised by its <b>word capacity</b> (number of addressable locations) "
    "and <b>word size</b> (bits per location). A 128 x 8 RAM chip has 128 locations of 8 bits each "
    "(= 1024 bits = 1 Kbit). Key external signals on a RAM chip:"
)
en.info_table(
    ["Pin/Signal", "Direction", "Function"],
    [
        ["Address lines (A0-Ak)", "Input", "Selects one of the 2^k memory locations"],
        [
            "Data lines (D0-Dn)",
            "Bidirectional",
            "Data to write (input) or data read (output)",
        ],
        [
            "CS1, CS2 (Chip Select)",
            "Input",
            "Enable the chip. CS1=1 AND CS2=0 to enable (typically)",
        ],
        [
            "RD (Read Enable)",
            "Input",
            "When 1: place selected word on data bus (output mode)",
        ],
        ["WR (Write Enable)", "Input", "When 1: write data bus into selected location"],
        [
            "Output (tri-state)",
            "Output",
            "High-impedance when not selected, prevents bus contention",
        ],
    ],
)
en.code_block("""
 RAM CHIP FUNCTION TABLE (CS1=1, CS2=0 for operation):
 ======================================================
 CS1 | CS2 | RD | WR | Operation          | Data Bus State
 ----|-----|----|----|--------------------|-----------------
  0  |  X  |  X |  X | Inhibit (not sel.) | High-impedance (Z)
  X  |  1  |  X |  X | Inhibit (not sel.) | High-impedance (Z)
  1  |  0  |  1 |  0 | READ: data -> bus  | Output word at address
  1  |  0  |  0 |  1 | WRITE: bus -> RAM  | Input (latch bus into cell)
  1  |  0  |  0 |  0 | Inhibit            | High-impedance (Z)
""")
en.tip(
    "SRAM: flip-flop stores bit, NO refresh needed, fast, expensive. "
    "DRAM: capacitor stores bit, MUST refresh periodically, slow, cheap, dense. "
    "Main memory uses DRAM. Cache uses SRAM. "
    "Chip Select pins allow multiple chips to share the same data/address bus."
)
en.br()

# =============================================================================
#  4.4  MAIN MEMORY -- ROM
# =============================================================================
en.chap_box("4.4  Main Memory -- ROM (Read-Only Memory)")
en.section("ROM Overview")
en.definition(
    "<b>ROM (Read-Only Memory):</b> A semiconductor memory whose contents are "
    "permanently or semi-permanently programmed and can only be <b>read</b> during "
    "normal CPU operation. ROM is <b>non-volatile</b> -- data is retained without "
    "power. ROM is used for firmware, BIOS, boot loaders, and look-up tables."
)

en.section("Types of ROM")
en.info_table(
    ["Type", "Full Name", "Programming Method", "Erasure", "Typical Use"],
    [
        [
            "Masked ROM",
            "Mask-programmed ROM",
            "During chip fabrication (metal mask layer). Factory only.",
            "Not erasable",
            "Mass production (console game cartridges, embedded firmware)",
        ],
        [
            "PROM",
            "Programmable ROM",
            "User programs once using a PROM programmer (fuses or anti-fuses blown).",
            "Not erasable (one-time)",
            "Field-programmable, small batches",
        ],
        [
            "EPROM",
            "Erasable PROM",
            "UV light erases entire chip (expose through quartz window). Then reprogram electrically.",
            "UV light (whole chip)",
            "Prototyping, firmware development; recognisable by quartz window on package",
        ],
        [
            "EEPROM",
            "Electrically Erasable PROM",
            "Electrically erased and reprogrammed byte-by-byte.",
            "Electrical (byte-by-byte)",
            "Configuration storage, calibration data, small non-volatile RAM replacement",
        ],
        [
            "Flash",
            "Flash EEPROM",
            "Electrically erased in sectors/blocks (not byte-by-byte). Faster than EEPROM.",
            "Electrical (sector/block)",
            "SSD, USB drives, SD cards, smartphone storage, BIOS chip",
        ],
    ],
)
en.tip(
    "ROM types: Masked (factory) -> PROM (one-time user) -> EPROM (UV erase) -> EEPROM (byte electrical erase) -> Flash (sector electrical erase). "
    "Flash is the modern standard -- SSDs and USB drives use Flash. "
    "ROM is non-volatile. RAM is volatile. "
    "A typical ROM chip has address and data lines but only a CS and Output-Enable (OE) -- no WR pin."
)
# Removed manual page break to let content flow naturally without creating mostly blank pages

# =============================================================================
#  4.5  MEMORY ADDRESS MAP
# =============================================================================
en.chap_box("4.5  Memory Address Map")
en.section("Concept")
en.definition(
    "<b>Memory Address Map:</b> A table that specifies which memory chip (RAM or ROM) "
    "responds to which range of addresses on the CPU's address bus. Each chip occupies "
    "a contiguous block of the address space determined by the chip's capacity. "
    "Address decoding hardware ensures only the chip whose address range is selected "
    "drives the data bus -- all others are in high-impedance."
)
en.body(
    "The designer assigns address ranges to chips based on available address bus lines. "
    "High-order address bits select the chip (chip select decoding); low-order bits are "
    "connected directly to the chip's internal address lines."
)

en.section("Memory Address Map Example (Morris Mano)")
en.code_block("""
 EXAMPLE MEMORY ADDRESS MAP:
 ======================================================
 System: 512 bytes RAM (4 x 128-byte chips) + 512 bytes ROM (1 x 512-byte chip)
 Total memory: 1024 bytes -> needs 10 address bits (A0-A9)
 Address bus: 16 bits (A0-A15). Lines A10-A15 unused (assumed 0).

 Component | Hex Address Range | Bus Lines Usage
 ----------|-------------------|--------------------------------------------------
 RAM 1     | 0x0000 - 0x007F   | A9=0,A8=0,A7=0: 000 XXXXXXX  (A6-A0 = 7 bits)
 RAM 2     | 0x0080 - 0x00FF   | A9=0,A8=0,A7=1: 001 XXXXXXX
 RAM 3     | 0x0100 - 0x017F   | A9=0,A8=1,A7=0: 010 XXXXXXX
 RAM 4     | 0x0180 - 0x01FF   | A9=0,A8=1,A7=1: 011 XXXXXXX
 ROM       | 0x0200 - 0x03FF   | A9=1: 1XXXXXXXXX           (A8-A0 = 9 bits)

 Key insight:
   A9=0 -> CPU is accessing RAM (lines A8,A7 select which RAM chip)
   A9=1 -> CPU is accessing ROM

 Address line A9 is used as the RAM/ROM chip-select:
   A9=0: assert CS on RAM decoder, deassert ROM CS
   A9=1: assert CS on ROM chip, deassert RAM decoder
""")

net_mem_map = ed.NetworkDiagram(
    width=en.CW,
    height=260,
    theme=diag_theme,
    caption="Fig 3: Memory address map -- CPU, address decoder, RAM and ROM chips",
)
net_mem_map.node("cpu", "CPU", x=60, y=140, kind="server")
net_mem_map.node("dec", "Address Decoder\n(A9, A8, A7)", x=190, y=140, kind="generic")
net_mem_map.node("ram1", "RAM 1\n(0000-007F)", x=330, y=205, kind="database")
net_mem_map.node("ram2", "RAM 2\n(0080-00FF)", x=330, y=155, kind="database")
net_mem_map.node("ram3", "RAM 3\n(0100-017F)", x=330, y=105, kind="database")
net_mem_map.node("rom", "ROM\n(0200-03FF)", x=330, y=55, kind="storage")
net_mem_map.node("databus", "16-bit Data Bus", x=190, y=50, kind="switch")

net_mem_map.link("cpu", "dec", label="Address Bus")
net_mem_map.link("dec", "ram1", label="CS")
net_mem_map.link("dec", "ram2", label="CS")
net_mem_map.link("dec", "ram3", label="CS")
net_mem_map.link("dec", "rom", label="CS")
net_mem_map.link("cpu", "databus", label="Data Bus")
net_mem_map.link("ram1", "databus")
net_mem_map.link("ram2", "databus")
net_mem_map.link("rom", "databus")
en.story.extend(net_mem_map.as_flowable())

en.tip(
    "Memory address map: high-order address bits go to address decoder (chip select). "
    "Low-order bits go directly to chip address inputs. "
    "Example: 128-byte chip needs 7 address bits (2^7=128). "
    "RAM/ROM distinction: one address bit differentiates RAM block from ROM block. "
    "Total address bits = log2(total memory size in bytes)."
)
en.br()

# =============================================================================
#  4.6  AUXILIARY MEMORY
# =============================================================================
en.chap_box("4.6  Auxiliary Memory")
en.section("Purpose")
en.definition(
    "<b>Auxiliary Memory (Secondary Storage):</b> Non-volatile, large-capacity storage "
    "outside the CPU and main memory. Used to store programs and data that are too large "
    "to fit in main memory or that must be retained when power is removed. Access is much "
    "slower than main memory. Data must be loaded into RAM before the CPU can process it."
)

en.info_table(
    ["Type", "Technology", "Access Method", "Capacity", "Speed", "Use Case"],
    [
        [
            "Magnetic Disk (HDD)",
            "Spinning magnetic platters",
            "Direct (seek + rotational latency)",
            "500 GB - 20 TB",
            "5-10 ms",
            "OS files, user data, databases",
        ],
        [
            "Solid State Drive (SSD)",
            "NAND Flash",
            "Direct (electronic, no moving parts)",
            "128 GB - 8 TB",
            "50-100 us",
            "OS boot drive, fast storage",
        ],
        [
            "Magnetic Tape",
            "Magnetic oxide on plastic tape",
            "Sequential (must fast-forward/rewind)",
            "TB range",
            "Seconds to minutes",
            "Backup, archival, cold storage",
        ],
        [
            "Optical (CD/DVD/Blu-ray)",
            "Laser reads pits/lands",
            "Direct",
            "700 MB - 100 GB",
            "~100 ms",
            "Media distribution, archival",
        ],
    ],
)

en.section("Magnetic Disk Structure")
en.code_block("""
 MAGNETIC DISK KEY CONCEPTS:
 ======================================================
 Physical structure:
   Platters:   Multiple circular metal/glass disks coated with magnetic material.
   Tracks:     Concentric circles on each platter surface (numbered from outside in).
   Cylinders:  All tracks at the same radial position across all platters.
   Sectors:    Each track divided into fixed-size sectors (typically 512 bytes or 4 KB).
   Read/Write heads: One per surface; all heads move together (same cylinder).

 Address of a disk location: (Cylinder, Head, Sector)

 Disk access time = Seek time + Rotational latency + Transfer time
   Seek time:          Head moves to the correct cylinder  (~3-15 ms)
   Rotational latency: Disk rotates to bring sector under head (~0-8 ms avg = 0.5 rotation)
   Transfer time:      Data transferred at disk rotation rate (very small, ~0.1 ms/sector)

 EXAMPLE: 7200 RPM disk
   Rotational speed: 7200 rotations/minute = 120 rotations/second
   One full rotation: 1/120 = 8.33 ms
   Average rotational latency: 8.33/2 = 4.17 ms
""")
en.br()

# =============================================================================
#  4.7  ASSOCIATIVE MEMORY (CAM)
# =============================================================================
en.chap_box("4.7  Associative Memory (Content-Addressable Memory)")
en.section("What is Associative Memory?")
en.definition(
    "<b>Associative Memory (Content-Addressable Memory -- CAM):</b> A memory unit "
    "accessed by the <b>content</b> of the data rather than by a specific address or "
    "location. When a search key (argument) is presented, all words in memory are "
    "compared in <b>parallel</b> simultaneously. Words that match the argument set "
    "a corresponding bit in the <b>match register</b>. The matching word(s) can then "
    "be read out. CAM is used for TLBs, network routing tables, and cache tag arrays."
)

en.section("Hardware Organisation")
en.bullet(
    [
        "<b>Memory Array:</b> m words, each n bits wide.",
        "<b>Argument Register (A):</b> n-bit register holding the search key.",
        "<b>Key Register (K):</b> n-bit mask -- only bits where K=1 are compared. K=0 means 'don't care'.",
        "<b>Match Register (M):</b> m-bit register. M[i]=1 if word i matched the argument.",
        "<b>Match Logic:</b> Each bit position uses XNOR (equality) gate. All unmasked positions must match for the word to be marked in M.",
    ]
)

en.code_block("""
 ASSOCIATIVE MEMORY OPERATION EXAMPLE:
 ======================================================
 Argument Register A = 1 1 0 1 1  0 1 0
 Key Register      K = 0 0 0 0 0  1 1 1
                                   ^^^  only rightmost 3 bits compared (K=1 positions)

 Memory word 1:   1 0 1 0 1  0 1 0   -> Compare rightmost 3: 010 vs A=010 -> MATCH  -> M[1]=1
 Memory word 2:   1 1 0 1 1  1 0 0   -> Compare rightmost 3: 100 vs A=010 -> NO MATCH -> M[2]=0
 Memory word 3:   0 0 0 1 0  0 1 0   -> Compare rightmost 3: 010 vs A=010 -> MATCH  -> M[3]=1

 Match logic per bit: use XNOR(A_bit, Word_bit). Output is 1 if equal.
   Then OR with NOT(K_bit): if K=0 (don't care), force 1 regardless of comparison.
   AND all n outputs -> 1 only if ALL unmasked bits matched.

 WRITE OPERATION:
   Set Write signal = 1.
   Data is loaded into all memory cells simultaneously (broadcast write).
   Usually the match register selects which word to write.
""")

en.section("Associative vs Random-Access Memory")
en.info_table(
    ["Property", "RAM (Address-Accessed)", "CAM (Content-Accessed)"],
    [
        [
            "Access method",
            "Address (location) specified first",
            "Content (data) specified first",
        ],
        [
            "Search",
            "O(1) with address -- direct access",
            "Parallel search of ALL words simultaneously",
        ],
        [
            "Hardware",
            "Simple decoder, one access at a time",
            "Complex -- comparator per bit per word",
        ],
        ["Speed", "Fast but sequential for search", "Very fast for parallel search"],
        ["Cost", "Cheap per bit", "Expensive (more circuitry per cell)"],
        [
            "Use case",
            "General-purpose storage",
            "TLB, cache tags, routing tables, network lookup",
        ],
    ],
)
en.tip(
    "CAM = Content-Addressable Memory. Search by DATA, not by address. "
    "Argument register: search key. Key register: mask (1=compare, 0=don't care). "
    "Match register: one bit per word; 1=match. "
    "Used in TLBs and cache tag arrays where fast parallel lookup is essential."
)
en.br()

# =============================================================================
#  4.8  CACHE MEMORY
# =============================================================================
en.chap_box("4.8  Cache Memory -- Concept and Performance")
en.section("Why Cache?")
en.definition(
    "<b>Cache Memory:</b> A small, fast SRAM memory placed between the CPU and the "
    "larger, slower DRAM main memory. When the CPU requests a word, the cache controller "
    "first checks if the word is in cache (a <b>cache hit</b>). If yes, the word is "
    "returned in cache access time (~1-10 ns). If not (a <b>cache miss</b>), the word "
    "is fetched from main memory AND a full <b>cache line</b> (block of 16-64 bytes) "
    "is loaded into cache for future use."
)
en.body(
    "Cache works because of the principle of locality of reference. When the CPU fetches "
    "a word from main memory on a miss, it loads an entire <b>cache block</b> (e.g., 64 bytes) "
    "into a <b>cache line</b>. Future accesses to nearby addresses will find the data already "
    "in cache (spatial locality)."
)

en.section("Hit Ratio and Average Access Time")
en.definition(
    "<b>Hit Ratio (h):</b> The fraction of all memory references that are found in cache. "
    "h = (number of cache hits) / (total memory references). "
    "Typical hit ratios: 0.85 to 0.99."
)
en.code_block("""
 AVERAGE ACCESS TIME FORMULA:
 ======================================================
 Let:
   Tc = Cache access time   (e.g., 10 ns)
   Tm = Main memory access time (e.g., 100 ns)
   h  = Hit ratio (e.g., 0.9)

 METHOD 1 (Simultaneous access -- cache and MM accessed together on miss):
   Tavg = h * Tc + (1 - h) * Tm
   Example: Tavg = 0.9 * 10 + 0.1 * 100 = 9 + 10 = 19 ns

 METHOD 2 (Sequential access -- check cache first, then MM on miss):
   Tavg = h * Tc + (1 - h) * (Tc + Tm)
   Example: Tavg = 0.9 * 10 + 0.1 * (10 + 100) = 9 + 11 = 20 ns

 MISS PENALTY: The extra time for a cache miss = Tm (or Tc + Tm)

 EXAMPLE (from reference notes):
   Tc = 50 ns, Tm = 500 ns, h = 0.9  (read operations only)
   Sequential: Tavg = 0.9*50 + 0.1*(500+50) = 45 + 55 = 100 ns

 EXAMPLE with Read/Write mix (write-through policy):
   PR = 0.8 (80% reads), PW = 0.2 (20% writes)
   hR = 0.9 (read hit ratio), hW = 0 (writes always go to main memory with write-through)
   Tavg(R) = 0.9*50 + 0.1*(500+50) = 100 ns
   Tavg(W) = 500 ns (write always to main memory)
   Tavg = Tavg(R)*PR + Tavg(W)*PW = 100*0.8 + 500*0.2 = 80 + 100 = 180 ns
   Average hit ratio = hR*PR + hW*PW = 0.9*0.8 + 0*0.2 = 0.72
""")
en.br()

# =============================================================================
#  4.9  DIRECT MAPPING
# =============================================================================
en.chap_box("4.9  Cache Mapping -- Direct Mapping")
en.section("Concept")
en.definition(
    "<b>Direct Mapping:</b> Each block of main memory is mapped to exactly ONE specific "
    "cache line. The cache line number is determined by: cache_line = block_number MOD "
    "number_of_cache_lines. If two blocks map to the same line and both are needed, "
    "they continuously replace each other (thrashing). Requires only one tag comparison."
)

en.section("Address Partition")
en.frame_format(
    "Direct Mapping -- Memory Address Partition",
    [
        ("TAG", "t bits"),
        ("BLOCK (Cache Line Index)", "k bits"),
        ("WORD (Offset)", "w bits"),
    ],
)
en.code_block("""
 DIRECT MAPPING ADDRESS FIELDS:
 ======================================================
 Word field (w bits):  Selects one word within the cache block.
                       Block size = 2^w words.

 Block field (k bits): Selects the cache line (index into cache).
                       Number of cache lines = 2^k.

 Tag field (t bits):   Stored with each cache line to identify which
                       main memory block currently occupies that line.
                       Total address bits = t + k + w.
                       t = (total address bits) - k - w

 OPERATION:
   1. CPU generates address: [TAG | BLOCK | WORD]
   2. Use BLOCK field to select cache line.
   3. Compare TAG field with stored tag in that cache line.
   4. If tags MATCH AND valid bit = 1: HIT -- return word at WORD offset.
   5. If tags MISMATCH or valid = 0: MISS -- fetch block from main memory,
      overwrite cache line, update tag.

 ADVANTAGE: Simple, fast (single comparison).
 DISADVANTAGE: Thrashing if two frequently used blocks map to same line.
""")

en.section("Worked Example -- Direct Mapping")
en.code_block("""
 DIRECT MAPPING EXAMPLE (from Morris Mano):
 ======================================================
 Main memory: 4096 pages x 16 words = 65536 words total
 Address bits: 16 (12 bits page + 4 bits word)
 Cache: 128 lines x 16 words

 Address partition:
   Word field w = 4 bits  (2^4 = 16 words per block)
   Block field k = 7 bits (2^7 = 128 cache lines)
   Tag field   t = 16 - 7 - 4 = 5 bits

 Example 1: Cache size = 1K words, Block size = 128 words, MM = 64K words
   w = log2(128) = 7 bits
   k = log2(1K/128) = log2(8) = 3 bits
   total address = log2(64K) = 16 bits
   t = 16 - 3 - 7 = 6 bits

 Address format: [ TAG(6) | BLOCK(3) | WORD(7) ] = 16 bits total

 CACHE MISS: Bring entire 128-word block from MM into cache line #(BLOCK field).
 Store TAG to identify which MM block is now in this cache line.
 Next access to same block: TAG matches -> HIT (fast access).
""")

# Direct mapping diagram
net_direct = ed.NetworkDiagram(
    width=en.CW,
    height=240,
    theme=diag_theme,
    caption="Fig 4: Direct mapping -- each MM block maps to exactly one cache line",
)
net_direct.node("addr", "CPU Address\n[TAG|BLOCK|WORD]", x=65, y=125, kind="generic")
net_direct.node("idx", "Cache Line\nIndex (BLOCK field)", x=200, y=195, kind="generic")
net_direct.node("cache", "Cache Array\n(128 lines)", x=340, y=125, kind="database")
net_direct.node("cmp", "Tag Compare\n(stored vs new)", x=340, y=55, kind="generic")
net_direct.node("hit", "HIT: return\nword at WORD offset", x=470, y=90, kind="server")
net_direct.node(
    "miss", "MISS: fetch block\nfrom main mem", x=470, y=160, kind="storage"
)

net_direct.link("addr", "idx", label="BLOCK bits")
net_direct.link("idx", "cache", label="select line")
net_direct.link("cache", "cmp", label="stored tag")
net_direct.link("addr", "cmp", label="TAG bits")
net_direct.link("cmp", "hit", label="match")
net_direct.link("cmp", "miss", label="mismatch")
en.story.extend(net_direct.as_flowable())

en.tip(
    "Direct mapping: cache_line = block_number MOD number_of_lines. "
    "Address = [TAG | BLOCK | WORD]. BLOCK selects line; TAG identifies MM block. "
    "ONE comparison per lookup. Simple, fast, but susceptible to thrashing."
)
en.br()

# =============================================================================
#  4.10  ASSOCIATIVE MAPPING
# =============================================================================
en.chap_box("4.10  Cache Mapping -- Associative Mapping")
en.section("Concept")
en.definition(
    "<b>Associative (Fully-Associative) Mapping:</b> A main memory block can be placed "
    "in ANY cache line -- there is no fixed mapping. The tag of each cache line contains "
    "the full block number from main memory. To find a word, ALL cache tags are compared "
    "simultaneously in parallel (using CAM). Very flexible -- no thrashing due to index "
    "conflicts. But expensive: requires a comparator for every cache line."
)

en.section("Address Partition")
en.frame_format(
    "Associative Mapping -- Memory Address Partition",
    [("TAG (full block number)", "t bits"), ("WORD (offset within block)", "w bits")],
)
en.code_block("""
 ASSOCIATIVE MAPPING ADDRESS FIELDS:
 ======================================================
 Word field (w bits): Same as direct -- selects word within block.
 Tag field (t bits):  Contains the FULL main memory block number.
                      t = total address bits - w

 OPERATION:
   1. CPU generates address: [TAG | WORD]
   2. Compare TAG simultaneously with ALL stored tags in cache (parallel CAM search).
   3. If any line's tag matches: HIT -- read word at WORD offset in matching line.
   4. If no match: MISS -- load block from main memory into any free (or replaced) cache line.

 ADVANTAGE: Maximum flexibility -- any block goes anywhere. No thrashing.
 DISADVANTAGE: Expensive -- needs one comparator per cache line. Hardware cost is O(n).
               For 1024-line cache: 1024 simultaneous comparisons!

 Example: MM = 4096 pages x 16 words, Cache = 128 lines x 16 words
   w = 4 bits (16 words per block)
   t = 12 bits (full 12-bit page number stored as tag)
   Address format: [ TAG(12) | WORD(4) ] = 16 bits
""")
en.tip(
    "Associative mapping: NO index field. Tag = full block number. "
    "Parallel CAM search of all tags simultaneously. "
    "Maximum flexibility -- no conflict misses. "
    "Hardware expensive -- 1 comparator per cache line. "
    "Used when cache is small or in TLBs."
)
en.br()

# =============================================================================
#  4.11  SET-ASSOCIATIVE MAPPING
# =============================================================================
en.chap_box("4.11  Cache Mapping -- Set-Associative Mapping")
en.section("Concept")
en.definition(
    "<b>Set-Associative Mapping:</b> A compromise between direct mapping and fully "
    "associative mapping. The cache is divided into <b>sets</b>, each containing "
    "<b>k cache lines</b> (k-way set-associative). A main memory block is mapped "
    "to a specific SET (determined by address bits, like direct mapping) but can "
    "go into any of the k lines within that set (like associative mapping). "
    "Only k tag comparisons are needed (k << number of lines)."
)

en.section("Address Partition")
en.frame_format(
    "Set-Associative Mapping -- Memory Address Partition",
    [("TAG", "t bits"), ("SET (index)", "s bits"), ("WORD (offset)", "w bits")],
)
en.code_block("""
 SET-ASSOCIATIVE MAPPING:
 ======================================================
 Word field (w bits):  Block size = 2^w words.
 Set field  (s bits):  Number of sets = 2^s.
 Tag field  (t bits):  Total address bits - s - w.

 OPERATION:
   1. CPU generates address: [TAG | SET | WORD]
   2. Use SET field to select which set to search.
   3. Compare TAG with stored tags of ALL k lines in that set (k comparisons).
   4. If any line's tag matches: HIT.
   5. If no match: MISS -- load block into one of the k lines in the set
      (using replacement policy if all k lines are occupied).

 EXAMPLE: 2-way Set-Associative Cache
   MM = 64K x 16-bit words, Cache = 2048 words total, Block = 4 words
   k = 2 (2-way: each set has 2 lines)
   w = log2(4) = 2 bits
   Total lines = 2048 / 4 = 512 lines
   Number of sets = 512 / 2 = 256 sets
   s = log2(256) = 8 bits
   Total address = log2(64K) = 16 bits (assuming 16-bit address)
   Wait: 64K words -> need log2(64K)=16 bits if word-addressed
   t = 16 - 8 - 2 = 6 bits
   TAG(6) | SET(8) | WORD(2) = 16 bits

 For a 4-way set-associative cache, each set has 4 lines -> 4 comparisons.
""")

en.section("Comparison of Cache Mapping Methods")
en.info_table(
    ["Property", "Direct Mapping", "Associative Mapping", "Set-Associative"],
    [
        [
            "Block placement",
            "Exactly 1 cache line (fixed)",
            "Any cache line",
            "Any line within a set",
        ],
        [
            "Tag field size",
            "Small (t = addr - k - w)",
            "Large (t = addr - w)",
            "Medium (t = addr - s - w)",
        ],
        [
            "Comparisons per lookup",
            "1 (single comparison)",
            "All lines simultaneously",
            "k (lines per set)",
        ],
        [
            "Hardware cost",
            "Low (one comparator)",
            "High (n comparators)",
            "Moderate (k comparators)",
        ],
        [
            "Conflict misses",
            "High (two blocks compete for same line)",
            "None",
            "Low (k lines per set share)",
        ],
        [
            "Typical use",
            "Simple caches",
            "TLBs (small, fast)",
            "Modern CPU caches (L1, L2, L3)",
        ],
        [
            "Example",
            "k=1 (each set=1 line)",
            "k=n (one set=all lines)",
            "k=2,4,8,16-way",
        ],
    ],
)

# Side-by-side mapping comparison stacks
left_sa = ed.LayeredStack(
    width=en.CW * 0.44,
    height=180,
    theme=diag_theme,
    caption="2-Way Set-Associative (2 lines/set)",
)
left_sa.layer("Set 0 -- Line 0, Line 1", sublabel="2 comparisons for Set 0 lookup")
left_sa.layer("Set 1 -- Line 0, Line 1", sublabel="2 comparisons for Set 1 lookup")
left_sa.layer("Set 2 -- Line 0, Line 1", sublabel="2 comparisons for Set 2 lookup")
left_sa.layer("...", sublabel="256 sets total (8-bit set index)")

right_sa = ed.LayeredStack(
    width=en.CW * 0.44,
    height=180,
    theme=diag_theme,
    caption="4-Way Set-Associative (4 lines/set)",
)
right_sa.layer("Set 0 -- Line 0,1,2,3", sublabel="4 comparisons for Set 0 lookup")
right_sa.layer("Set 1 -- Line 0,1,2,3", sublabel="4 comparisons for Set 1 lookup")
right_sa.layer("...", sublabel="128 sets total (7-bit set index)")

left_sa.as_flowable()
right_sa.as_flowable()

tbl_sa = Table(
    [
        [
            ResponsiveDrawingFlowable(left_sa.drawing),
            ResponsiveDrawingFlowable(right_sa.drawing),
        ]
    ],
    colWidths=[en.CW * 0.48, en.CW * 0.48],
)
tbl_sa.setStyle(
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
en.add(tbl_sa)
en.sp(6)
en.add(
    Paragraph(
        "Fig 5 (left): 2-way set-associative cache.  |  Fig 5 (right): 4-way set-associative cache.",
        en.COVER_SUB,
    )
)

en.tip(
    "Set-associative: SET field selects set; TAG compares within set. "
    "k-way: k lines per set, k simultaneous comparisons. "
    "2-way SA: two blocks can share a set without conflict. "
    "Modern CPUs: L1 = 4-8 way, L2 = 8-16 way, L3 = 16-32 way set-associative."
)
en.br()

# =============================================================================
#  4.12  CACHE WRITE POLICY
# =============================================================================
en.chap_box("4.12  Cache Write Policy")
en.section("The Cache Consistency Problem")
en.body(
    "When the CPU writes data, two copies can exist: one in cache and one in main memory. "
    "If these diverge, data inconsistency occurs. Three write policies manage this:"
)

en.info_table(
    [
        "Policy",
        "Mechanism",
        "Main Memory State",
        "Bus Traffic",
        "Advantage",
        "Disadvantage",
    ],
    [
        [
            "Write-Through",
            "Every write to cache is immediately also written to main memory.",
            "Always up-to-date (consistent)",
            "High (every write goes to MM)",
            "Simple; MM always valid; easy to implement",
            "Slow for write-heavy workloads; bus saturated",
        ],
        [
            "Buffered Write-Through",
            "Write to cache AND to a write buffer; CPU continues; buffer writes to MM in background.",
            "Updated with small delay",
            "Moderate (buffered)",
            "CPU not stalled for writes; MM still updated",
            "Reads after buffer-full may stall; slightly more complex",
        ],
        [
            "Write-Back (Copy-Back)",
            "Write only to cache. Mark line dirty. Write to MM only when line is evicted.",
            "May be stale (dirty bit tracks this)",
            "Low (only on eviction)",
            "Fastest for write-heavy; less bus traffic",
            "Complex; stale MM (coherence issues in multiprocessors); data lost on power failure",
        ],
    ],
)

en.code_block("""
 WRITE-THROUGH vs WRITE-BACK COMPARISON:
 ======================================================
 Scenario: CPU writes to location X repeatedly in a loop (1000 times)

 WRITE-THROUGH:
   Each write -> cache updated + MM updated = 1000 main memory writes.
   Bus is busy with all 1000 writes. Slow.

 WRITE-BACK:
   Each write -> only cache updated (dirty bit set).
   MM updated only ONCE when the cache line is evicted.
   Only 1 main memory write for 1000 CPU writes. Fast.
   BUT: during 1000 writes, MM has STALE data.
        If another device (DMA, second CPU) reads MM, it gets wrong data.

 DIRTY BIT:
   Each cache line has one extra bit (dirty/modified bit).
   Dirty=0: clean, MM and cache are identical. Can evict freely.
   Dirty=1: modified, cache has newer data than MM. MUST write back before eviction.
""")

fc_write = ed.Flowchart(
    width=en.CW,
    height=450,
    theme=diag_theme,
    caption="Fig 6: Write-back cache write policy flowchart",
)
# Manual coordinates to resolve overlap collisions and provide clear flow path
fc_write.terminal("start", "CPU Write Request to address A", x=280, y=410)
fc_write.decision("hit", "Cache hit at line L?", x=280, y=345)
fc_write.process("upd_cache", "Update data in cache line L; set dirty bit = 1", x=480, y=345)
fc_write.decision("evict", "Need to evict line L for new block? (miss)", x=280, y=270)
fc_write.decision("dirty", "Evicted line L is dirty?", x=280, y=180)
fc_write.process("wb", "Write dirty line L back to main memory", x=80, y=180)
fc_write.process("fetch", "Fetch block from main memory into cache line L", x=280, y=105)
fc_write.process("load", "Load new block, update cache, set dirty bit = 1", x=280, y=30)
fc_write.terminal("done", "Write complete", x=480, y=30)

fc_write.edge("start", "hit")
fc_write.edge("hit", "upd_cache", branch="yes")
fc_write.edge("hit", "evict", branch="no")
# Manual path to route around dirty node: from evict, route right to x=450, down to y=105, then left to fetch
fc_write.edge("evict", "fetch", branch="no (free line)", path=[(450, 270), (450, 105)])
fc_write.edge("evict", "dirty", branch="yes (replace)")
fc_write.edge("dirty", "wb", branch="yes")
fc_write.edge("dirty", "fetch", branch="no")
fc_write.edge("wb", "fetch", orthogonal=True)
fc_write.edge("fetch", "load")
fc_write.edge("load", "done")
fc_write.edge("upd_cache", "done", orthogonal=True)
en.story.extend(fc_write.as_flowable())

en.tip(
    "Write-through: every write hits both cache AND main memory. Simple, slow. "
    "Write-back: write only cache (set dirty bit). Write to MM only on eviction. Fast. "
    "Dirty bit: 0=clean (MM up-to-date), 1=modified (cache newer than MM). "
    "Write-through preferred in multiprocessor systems (simpler coherence)."
)
en.br()

# =============================================================================
#  4.13  CACHE PERFORMANCE
# =============================================================================
en.chap_box("4.13  Cache Performance -- Worked Examples")
en.section("Performance Formulas")
en.code_block("""
 CACHE PERFORMANCE KEY FORMULAS:
 ======================================================
 Hit ratio h = (number of hits) / (total accesses)
 Miss rate  = 1 - h

 Average Access Time (Tavg):
   SIMULTANEOUS (cache and MM accessed together, MM result used on miss):
     Tavg = h * Tc + (1 - h) * Tm

   SEQUENTIAL (try cache first; miss then access MM):
     Tavg = h * Tc + (1 - h) * (Tc + Tm)

 Miss Penalty:  Tm  (time lost on a cache miss)
 Speedup from cache = Tm / Tavg

 WORKED EXAMPLE 1 (from reference notes):
 ==========================================
 Given: Tc = 50 ns, Tm = 500 ns, h = 0.9  (read operations only)
 Sequential access time:
   Tavg = 0.9 * 50 + (0.1) * (50 + 500)
        = 45 + 55 = 100 ns

 WORKED EXAMPLE 2 (with read/write mix, write-through):
 =======================================================
 Given: Tc=50ns, Tm=500ns, hR=0.9, PRead=0.8, PWrite=0.2
 Write-through: every write goes to MM (hW effectively 0)
   Tavg(Read)  = 0.9*50 + 0.1*(50+500) = 100 ns
   Tavg(Write) = 500 ns  (always write to MM)
   Tavg = Tavg(R)*PR + Tavg(W)*PW
        = 100*0.8 + 500*0.2 = 80 + 100 = 180 ns
   Effective average hit ratio = hR*PR + 0*PW = 0.9*0.8 = 0.72

 WORKED EXAMPLE 3 (two-level cache):
 =====================================
 L1 cache: Tc1 = 10 ns, h1 = 0.9
 L2 cache: Tc2 = 50 ns, h2 = 0.8  (hit rate among L1 misses)
 Main memory: Tm = 500 ns
   On L1 hit (prob=0.9): access time = Tc1 = 10 ns
   On L1 miss, L2 hit (prob=0.1*0.8=0.08): access time = Tc1 + Tc2 = 60 ns
   On both miss (prob=0.1*0.2=0.02): access time = Tc1 + Tc2 + Tm = 560 ns
   Tavg = 0.9*10 + 0.08*60 + 0.02*560
        = 9 + 4.8 + 11.2 = 25 ns
""")
en.br()

# =============================================================================
#  4.14  CACHE REPLACEMENT ALGORITHMS
# =============================================================================
en.chap_box("4.14  Cache Replacement Algorithms")
en.section("Need for Replacement")
en.body(
    "When a cache miss occurs and the cache is full, an existing cache line must "
    "be replaced (evicted) to make room for the new block. For <b>direct-mapped</b> "
    "caches there is no choice -- the incoming block replaces whatever is in the "
    "fixed cache line. For <b>associative</b> and <b>set-associative</b> caches, "
    "a replacement policy must select which existing line to evict."
)

en.info_table(
    ["Algorithm", "Rule", "Implementation", "Performance", "Notes"],
    [
        [
            "LRU\n(Least Recently Used)",
            "Evict the line that was accessed LEAST RECENTLY.",
            "Aging counter per line; increment all on each access; reset matched line's counter to 0.",
            "Best (closest to optimal)",
            "Most commonly used in L1/L2 caches. Counter bit overhead.",
        ],
        [
            "FIFO\n(First In First Out)",
            "Evict the line that was loaded into cache FIRST (oldest resident).",
            "Queue or circular pointer; rotate on each miss.",
            "Good",
            "Easy to implement. Does not consider recent usage.",
        ],
        [
            "LFU\n(Least Frequently Used)",
            "Evict the line with the FEWEST total accesses.",
            "Frequency counter per line.",
            "Moderate",
            "Good for skewed access patterns. Risk: old heavily-used lines never evict.",
        ],
        [
            "Random",
            "Evict a randomly chosen line.",
            "Hardware random number generator.",
            "Slightly inferior to LRU",
            "Simplest hardware. Surprisingly close to LRU in practice.",
        ],
        [
            "Optimal (OPT/MIN)",
            "Evict the line that will NOT be used for the LONGEST future time.",
            "Requires future knowledge -- impossible in hardware.",
            "Theoretical best (lower bound)",
            "Used as benchmark for comparing other algorithms. Impossible to implement exactly.",
        ],
    ],
)

en.section("LRU Example (2-way set-associative)")
en.code_block("""
 LRU REPLACEMENT EXAMPLE (2-way set-associative, Set 0):
 ======================================================
 Set 0 has 2 lines: Line A, Line B
 Access sequence: Block 1, Block 2, Block 1, Block 3

 Access 1 -- Block 1:  MISS. Load Block 1 into Line A.  State: [B1, -]
 Access 2 -- Block 2:  MISS. Load Block 2 into Line B.  State: [B1, B2]. LRU=B1 (older)
 Access 3 -- Block 1:  HIT.  B1 recently used.           State: [B1, B2]. LRU=B2 (now older)
 Access 4 -- Block 3:  MISS. Evict LRU=B2. Load Block 3. State: [B1, B3]

 Result: Block 2 was evicted (least recently used before the miss).

 FIFO for same sequence:
 Access 1 -- Block 1:  MISS. Load Block 1. Queue: [B1]
 Access 2 -- Block 2:  MISS. Load Block 2. Queue: [B1, B2]
 Access 3 -- Block 1:  HIT.  No change.    Queue: [B1, B2] (FIFO ignores recent use!)
 Access 4 -- Block 3:  MISS. Evict B1 (first in).  Queue: [B2, B3]
 Result: Block 1 was just used but FIFO evicts it! (FIFO anomaly)
""")
en.tip(
    "LRU: evict least recently used. Best performance, needs usage tracking. "
    "FIFO: evict oldest loaded. Simple but ignores recent use. "
    "Optimal: evict least-soon-needed. Theoretical only. "
    "Random: surprisingly competitive with LRU in practice and simpler hardware."
)
en.br()

# =============================================================================
#  4.15  VIRTUAL MEMORY
# =============================================================================
en.chap_box("4.15  Virtual Memory")
en.section("What is Virtual Memory?")
en.definition(
    "<b>Virtual Memory:</b> A hardware and OS technique that gives each process the "
    "illusion of having a large, contiguous private address space (the <b>virtual address "
    "space</b> or <b>address space</b>) even though the physical main memory is smaller "
    "and shared. The OS and hardware MMU (Memory Management Unit) transparently map "
    "virtual addresses to physical addresses on every memory access."
)

en.section("Address Space vs Memory Space")
en.definition(
    "<b>Virtual Address (Logical Address):</b> The address generated by the CPU / programmer. "
    "The set of all virtual addresses is the <b>address space</b> (size = N). "
    "<b>Physical Address:</b> The actual location in main memory. "
    "The set of all physical addresses is the <b>memory space</b> (size = M). "
    "Virtual memory allows N >> M -- the program can be LARGER than physical RAM."
)
en.code_block("""
 VIRTUAL MEMORY ADDRESS SPACE EXAMPLE (Morris Mano):
 ======================================================
 Main memory capacity: 32K words  -> physical address = 15 bits (2^15 = 32K)
 Auxiliary memory:    1024K words -> virtual address  = 20 bits (2^20 = 1024K)

 Address space:  N = 1024K (virtual addresses use 20 bits)
 Memory space:   M = 32K   (physical addresses use 15 bits)

 The CPU generates 20-bit virtual addresses.
 A mapping table translates each 20-bit virtual address to a 15-bit physical address.
 Only the currently active portion of the program resides in main memory.
 Inactive pages reside in auxiliary memory (disk), fetched on demand (page fault).
""")

en.section("Virtual-to-Physical Address Mapping Overview")
fc_vm = ed.Flowchart(
    width=en.CW,
    height=500,
    theme=diag_theme,
    caption="Fig 7: Virtual memory address translation flow",
)
# Manual coordinate placement to prevent overlapping lines and node collisions
fc_vm.terminal("start", "CPU generates virtual address (VA)", x=280, y=450)
fc_vm.process("split", "Split VA into: Page Number + Page Offset (Word)", x=280, y=395)
fc_vm.process("tlb", "Check TLB (associative page table) for page number", x=280, y=340)
fc_vm.decision("tlb_hit", "TLB hit?", x=280, y=270)
fc_vm.process("pa", "Get frame number from TLB entry", x=80, y=270)
fc_vm.process("pt", "Access Page Table in main memory", x=480, y=270)
fc_vm.decision("present", "Presence bit = 1?", x=480, y=190)
fc_vm.process("pf", "PAGE FAULT: load page from disk to MM, update page table", x=680, y=190)
fc_vm.process("frame", "Get frame number from page table; update TLB", x=480, y=110)
fc_vm.process("phys", "Physical address = Frame Number + Page Offset", x=280, y=110)
fc_vm.terminal("done", "Access main memory at physical address", x=280, y=30)

fc_vm.edge("start", "split")
fc_vm.edge("split", "tlb")
fc_vm.edge("tlb", "tlb_hit")
fc_vm.edge("tlb_hit", "pa", branch="yes")
fc_vm.edge("tlb_hit", "pt", branch="no")
fc_vm.edge("pa", "phys", orthogonal=True)
fc_vm.edge("pt", "present")
fc_vm.edge("present", "frame", branch="yes")
fc_vm.edge("present", "pf", branch="no")
fc_vm.edge("pf", "frame", orthogonal=True)
fc_vm.edge("frame", "phys", orthogonal=True)
fc_vm.edge("phys", "done")
en.story.extend(fc_vm.as_flowable())
en.br()

# =============================================================================
#  4.16  ADDRESS MAPPING -- PAGING
# =============================================================================
en.chap_box("4.16  Address Mapping -- Paging")
en.section("Paged Virtual Memory")
en.definition(
    "<b>Paging:</b> Virtual memory is divided into fixed-size units called <b>pages</b>. "
    "Physical memory is divided into equal-size units called <b>frames (blocks)</b>. "
    "A page can be loaded into any free frame. A <b>page table</b> maps each page "
    "number to its frame number (block number in physical memory). The page table is "
    "stored in main memory (or a fast associative memory -- TLB)."
)

en.section("Page Table Structure")
en.code_block("""
 PAGING ADDRESS TRANSLATION:
 ======================================================
 Virtual Address: [ Page Number (p bits) | Page Offset (d bits) ]
 Physical Address: [ Frame Number (f bits) | Page Offset (d bits) ]

 Page size = Block size = 2^d words (same offset used in both addresses).

 PAGE TABLE (stored in main memory):
   Indexed by page number. Each entry contains:
   - PRESENCE BIT (P): 1 = page is in main memory; 0 = page is on disk.
   - FRAME NUMBER: Which physical frame holds this page (if P=1).
   - DIRTY BIT: 1 = page has been modified (must write back to disk on eviction).
   - REFERENCE BIT: 1 = page was recently accessed (used by LRU replacement).
   - PROTECTION BITS: Read/Write/Execute permissions.

 TRANSLATION (if P=1):
   Virtual page number -> index into page table -> get frame number.
   Physical address = [frame number | page offset].

 EXAMPLE:
   Virtual address space: 8K words (8 pages x 1K words/page), p=3 bits, d=10 bits
   Memory space: 4K words (4 frames x 1K words/frame), f=2 bits

   Page table:
   Page 0 -> Frame 3 (P=1)
   Page 1 -> Frame 0 (P=1)
   Page 2 -> Frame 1 (P=1)
   Page 3 ->  ---    (P=0, on disk)
   ...

   Virtual address 1 | 0000100010 (page 1, offset 34):
   Page 1 -> Frame 0.
   Physical address: 00 | 0000100010 = frame 0, offset 34.
""")

en.section("Page Fault Handling")
en.definition(
    "<b>Page Fault:</b> Occurs when the CPU references a virtual page whose presence "
    "bit is 0 (the page is not in main memory). The OS suspends the current process, "
    "locates the page on disk, finds (or frees) a physical frame, loads the page "
    "into that frame, updates the page table, and resumes the process. Page faults "
    "are handled by the OS through an interrupt-like mechanism called a <b>trap</b>."
)
en.info_table(
    ["Step", "Action", "Handled By"],
    [
        [
            "1",
            "CPU generates virtual address; P bit = 0 in page table",
            "Hardware (MMU)",
        ],
        ["2", "Hardware raises a page-fault trap (exception)", "Hardware"],
        ["3", "OS saves current process state (PC, registers)", "OS kernel"],
        [
            "4",
            "OS identifies which page is needed (from faulting virtual address)",
            "OS kernel",
        ],
        [
            "5",
            "OS finds a free frame or evicts a page (replacement algorithm)",
            "OS kernel",
        ],
        [
            "6",
            "OS initiates disk I/O to load the faulting page into the chosen frame",
            "OS / DMA",
        ],
        [
            "7",
            "OS updates page table: set P=1, update frame number, clear dirty bit",
            "OS kernel",
        ],
        [
            "8",
            "OS resumes faulting process; it re-executes the faulting instruction",
            "Hardware",
        ],
    ],
)
en.br()

# =============================================================================
#  4.17  SEGMENTATION
# =============================================================================
en.chap_box("4.17  Segmentation")
en.section("What is Segmentation?")
en.definition(
    "<b>Segmentation:</b> A virtual memory technique that divides the program's address "
    "space into variable-size logical units called <b>segments</b> (e.g., code segment, "
    "data segment, stack segment, subroutine). Each segment has a name and a length. "
    "A <b>segment table</b> maps segment numbers to physical base addresses and lengths. "
    "Unlike paging (fixed-size), segments reflect the logical structure of the program."
)
en.bullet(
    [
        "<b>Logical address:</b> (Segment number, Offset within segment).",
        "<b>Segment table entry:</b> Base address (where segment starts in physical memory) + Limit (segment length).",
        "<b>Protection:</b> Offset must be less than the segment length (bounds check).",
        "<b>Benefit:</b> Segments match program structure. Easy to share code segments between processes.",
        "<b>Drawback:</b> Variable-size segments lead to external fragmentation in physical memory.",
    ]
)

en.section("Segmented Paging (Combined)")
en.definition(
    "<b>Segmented Paging:</b> Combines segmentation and paging. The logical address "
    "is divided into three fields: Segment number, Page number within segment, and Word "
    "offset within page. A segment table points to a page table for each segment. "
    "The page table maps page numbers to frame numbers. Used in Intel x86 protected mode."
)
en.code_block("""
 SEGMENTED PAGING ADDRESS FORMAT:
 ======================================================
 Logical Address: [ Segment # | Page # | Word Offset ]

 Translation (two-table mapping):
   1. Segment # -> Segment Table -> Page Table Base Address for this segment
   2. Page # + Page Table Base -> Page Table Entry -> Frame Number
   3. Physical address = [ Frame Number | Word Offset ]

 THREE memory accesses per reference:
   (1) Segment table lookup (2) Page table lookup (3) Actual data access
   This is TOO SLOW -> TLB caches recent translations.

 With TLB:
   If (Segment #, Page #) found in TLB: only ONE memory access (the data).
   If not in TLB: full two-table lookup, then cache in TLB.
""")
en.br()

# =============================================================================
#  4.18  TLB -- TRANSLATION LOOKASIDE BUFFER
# =============================================================================
en.chap_box("4.18  Translation Lookaside Buffer (TLB)")
en.section("Why TLB?")
en.definition(
    "<b>TLB (Translation Lookaside Buffer):</b> A small, fast <b>associative memory</b> "
    "(CAM) that caches the most recently used page table entries. On every memory access, "
    "the TLB is searched in parallel for the current page number. If found (TLB hit), "
    "the frame number is retrieved in ~1 cycle without accessing main memory for the page "
    "table. If not found (TLB miss), the page table in main memory is accessed and the "
    "TLB is updated."
)
en.body(
    "A TLB typically has 32-2048 entries. Each entry stores: "
    "Virtual Page Number (tag), Physical Frame Number (data), Valid bit, Dirty bit, "
    "and protection bits. TLB hit rates are typically 99%+."
)

en.section("Effective Memory Access Time with TLB")
en.code_block("""
 TLB EFFECTIVE ACCESS TIME FORMULA:
 ======================================================
 Let:
   Ttlb = TLB access time      (e.g., 2 ns -- fast associative lookup)
   Tm   = Main memory access time (e.g., 100 ns)
   h    = TLB hit rate          (typically 0.95 to 0.999)

 TLB HIT:  access time = Ttlb + Tm  (TLB lookup + 1 memory access for data)
 TLB MISS: access time = Ttlb + Tm + Tm  (TLB lookup + MM for page table + MM for data)

 Effective Access Time (EAT):
   EAT = h * (Ttlb + Tm) + (1 - h) * (Ttlb + Tm + Tm)
       = Ttlb + Tm + (1 - h) * Tm
       = Ttlb + (2 - h) * Tm

 EXAMPLE:
   Ttlb = 2 ns, Tm = 100 ns, h = 0.95
   EAT = 2 + (2 - 0.95) * 100 = 2 + 1.05 * 100 = 2 + 105 = 107 ns
   Without TLB (page table always in MM): access = Tm + Tm = 200 ns
   TLB speedup: 200 / 107 = 1.87x faster

 SEGMENTED PAGING EAT (segment table + page table in MM):
   Without TLB: 3 * Tm = 300 ns (segment table + page table + data)
   With TLB (hit): Ttlb + Tm = 102 ns
   EAT = h*(Ttlb+Tm) + (1-h)*(Ttlb+3*Tm)
       = 0.95*(102) + 0.05*(302) = 96.9 + 15.1 = 112 ns
""")

# TLB architecture diagram
net_tlb = ed.NetworkDiagram(
    width=en.CW,
    height=260,
    theme=diag_theme,
    caption="Fig 8: TLB architecture -- associative cache for page table entries",
)
net_tlb.node("cpu", "CPU\n(virtual addr)", x=40, y=130, kind="server")
net_tlb.node("tlb", "TLB\n(Associative Memory)", x=220, y=70, kind="database")
net_tlb.node("pt", "Page Table\n(in Main Memory)", x=220, y=190, kind="database")
net_tlb.node("mm", "Main Memory\n(physical data)", x=430, y=130, kind="storage", label_pos="right")
net_tlb.node("hit", "TLB Hit:\nframe # direct", x=430, y=50, kind="generic")
net_tlb.node("miss", "TLB Miss:\nupdate TLB", x=430, y=210, kind="generic")

net_tlb.link("cpu", "tlb", label="page # (parallel search)")
net_tlb.link("tlb", "hit", label="hit: frame #")
net_tlb.link("hit", "mm", label="access data")
net_tlb.link("cpu", "pt", label="miss: lookup page table")
net_tlb.link("pt", "miss", label="frame #")
net_tlb.link("miss", "tlb", label="update TLB")
net_tlb.link("miss", "mm", label="access data")
en.story.extend(net_tlb.as_flowable())

en.tip(
    "TLB = fast CAM for page table entries. Hit rate typically > 99%. "
    "TLB hit: Ttlb + Tm (just data access). TLB miss: Ttlb + 2*Tm (page table + data). "
    "EAT = h*(Ttlb+Tm) + (1-h)*(Ttlb+2*Tm). "
    "TLB is flushed on context switch (process change) since virtual->physical mappings change."
)
en.br()

# =============================================================================
#  4.19  PAGE FAULT AND REPLACEMENT ALGORITHMS
# =============================================================================
en.chap_box("4.19  Page Fault and Page Replacement Algorithms")
en.section("Page Replacement Overview")
en.body(
    "When a page fault occurs and main memory is full, the OS must choose a "
    "<b>victim page</b> to evict from memory to disk to make room for the new page. "
    "The goal is to evict the page least likely to be referenced in the near future."
)

en.info_table(
    ["Algorithm", "Policy", "Implementation", "Property"],
    [
        [
            "FIFO",
            "Evict the page that was LOADED FIRST (oldest in memory).",
            "Maintain a queue of page load times. Evict the head.",
            "Simple. May suffer Belady's Anomaly (more frames -> more faults with FIFO).",
        ],
        [
            "LRU\n(Least Recently Used)",
            "Evict the page that was accessed LEAST RECENTLY (furthest in the past).",
            "Aging counter per page OR stack implementation. Hardware support needed.",
            "Good approximation of optimal. No Belady's anomaly. Most common.",
        ],
        [
            "LFU\n(Least Frequently Used)",
            "Evict the page with the SMALLEST access count.",
            "Access counter per page. Increment on each reference.",
            "Favors frequently accessed pages. Old heavily-used pages may never be replaced.",
        ],
        [
            "Optimal (OPT)",
            "Evict the page that will NOT be needed for the LONGEST time in the future.",
            "Requires knowledge of future references -- impossible online.",
            "Theoretical lower bound on page faults. Used as benchmark.",
        ],
        [
            "Random",
            "Evict a randomly selected page.",
            "Hardware random number generator.",
            "Simple. No anomaly. Performance between FIFO and LRU.",
        ],
    ],
)

en.section("FIFO and LRU Worked Example")
en.code_block("""
 PAGE REPLACEMENT EXAMPLE (3 frames, reference string: 1,2,3,4,1,2,5,1,2,3,4,5)
 ======================================================

 FIFO (First-In, First-Out):
 Reference | Frames (F1,F2,F3) | Page Fault?
 ----------|-------------------|------------
     1     | [1, -, -]         | YES (fault 1)
     2     | [1, 2, -]         | YES (fault 2)
     3     | [1, 2, 3]         | YES (fault 3)
     4     | [4, 2, 3]         | YES (evict 1: oldest, fault 4)
     1     | [4, 1, 3]         | YES (evict 2, fault 5)
     2     | [4, 1, 2]         | YES (evict 3, fault 6)
     5     | [5, 1, 2]         | YES (evict 4, fault 7)
     1     | [5, 1, 2]         | no hit (1 in frame 2)
     2     | [5, 1, 2]         | no hit (2 in frame 3)
     3     | [5, 3, 2]         | YES (evict 1, fault 8)
     4     | [5, 3, 4]         | YES (evict 2, fault 9)
     5     | [5, 3, 4]         | no hit
 Total FIFO page faults: 9

 LRU (Least Recently Used):
 Reference | Frames (LRU order)| Page Fault? | Evict
 ----------|-------------------|-------------|------
     1     | [1]               | YES         |
     2     | [1,2]             | YES         |
     3     | [1,2,3]           | YES         |
     4     | [2,3,4]           | YES         | evict 1 (LRU)
     1     | [3,4,1]           | YES         | evict 2 (LRU)
     2     | [4,1,2]           | YES         | evict 3 (LRU)
     5     | [1,2,5]           | YES         | evict 4 (LRU)
     1     | [2,5,1]           | no          | 1 most recent
     2     | [5,1,2]           | no          |
     3     | [1,2,3]           | YES         | evict 5 (LRU)
     4     | [2,3,4]           | YES         | evict 1 (LRU)
     5     | [3,4,5]           | YES         | evict 2 (LRU)
 Total LRU page faults: 10 (for this string; LRU is better on average)
""")
en.tip(
    "Page replacement: choose victim when frames are full and page fault occurs. "
    "FIFO: evict oldest loaded -- simple, may thrash. "
    "LRU: evict least recently used -- best practical. "
    "Optimal: evict least-soon-needed -- theoretical, impossible online. "
    "Belady's Anomaly: only FIFO can have MORE page faults with MORE frames."
)
en.br()

# =============================================================================
#  4.20  QUICK REVISION SUMMARY
# =============================================================================
en.part_box("UNIT IV -- QUICK REVISION SUMMARY")
en.chap_box("Key Concepts at a Glance")

en.info_table(
    ["Topic", "Key Point to Remember"],
    [
        [
            "Memory Hierarchy",
            "CPU Registers > L1 > L2 > L3 Cache (SRAM) > Main Memory (DRAM) > SSD > HDD > Tape. "
            "Speed decreases, cost decreases, capacity increases down the hierarchy.",
        ],
        [
            "Locality of Reference",
            "Temporal: same address used again soon. Spatial: nearby addresses used soon. "
            "This is WHY caches work.",
        ],
        [
            "SRAM vs DRAM",
            "SRAM: flip-flop, NO refresh, fast (1-5 ns), expensive. -> Cache. "
            "DRAM: capacitor, MUST refresh periodically, slower (50-100 ns), cheap. -> Main memory.",
        ],
        [
            "ROM Types",
            "Masked (factory) -> PROM (one-time user) -> EPROM (UV erase) -> EEPROM (byte erase) -> Flash (block erase). "
            "Flash = SSDs, USB drives. Non-volatile.",
        ],
        [
            "Memory Address Map",
            "High address bits -> chip select decoder. Low address bits -> chip internal address. "
            "Total address bits = log2(total memory bytes).",
        ],
        [
            "Associative Memory (CAM)",
            "Search by CONTENT, not address. Argument reg (search key) + Key reg (mask). "
            "Match register = 1 for each matching word. Parallel search. Used in TLBs.",
        ],
        [
            "Cache Hit Ratio",
            "h = hits / total accesses. Typical: 0.85-0.99. "
            "Tavg = h*Tc + (1-h)*(Tc+Tm)  [sequential] OR  h*Tc + (1-h)*Tm  [simultaneous].",
        ],
        [
            "Direct Mapping",
            "cache_line = block_number MOD num_lines. Address = [TAG|BLOCK|WORD]. "
            "1 comparison. Simple but thrash-prone.",
        ],
        [
            "Associative Mapping",
            "Any block -> any cache line. Address = [TAG|WORD]. Parallel search all tags. "
            "No conflict misses. Expensive hardware.",
        ],
        [
            "Set-Associative Mapping",
            "Block -> specific SET, any line within set. Address = [TAG|SET|WORD]. "
            "k comparisons per set. Best balance of cost and performance.",
        ],
        [
            "Write-Through",
            "Every write -> cache AND main memory immediately. MM always consistent. "
            "High bus traffic.",
        ],
        [
            "Write-Back",
            "Write only to cache (dirty bit = 1). Write to MM only on line eviction. "
            "Fast, less traffic, but MM may be stale.",
        ],
        [
            "Cache Replacement: LRU",
            "Evict line not used for longest time. Best performance. Aging counters needed.",
        ],
        [
            "Cache Replacement: FIFO",
            "Evict oldest loaded line. Simple. Belady's Anomaly possible.",
        ],
        [
            "Virtual Memory",
            "Virtual (logical) address space N > physical memory space M. "
            "CPU uses virtual addresses; MMU translates to physical addresses.",
        ],
        [
            "Paging",
            "Fixed-size pages/frames. Page table maps page# to frame#. "
            "Virtual = [page# | offset]. Physical = [frame# | offset].",
        ],
        [
            "Page Table Entry",
            "Presence bit (P): 1=in RAM, 0=on disk. Frame number. Dirty bit. Reference bit.",
        ],
        [
            "Page Fault",
            "P=0: page not in RAM. OS loads page from disk to a free/replaced frame. "
            "Update page table, resume process.",
        ],
        [
            "TLB",
            "Fast CAM caching recent page table entries. Hit: Ttlb + Tm. Miss: Ttlb + 2*Tm. "
            "EAT = h*(Ttlb+Tm) + (1-h)*(Ttlb+2*Tm). Hit rate typically > 99%.",
        ],
        [
            "Segmentation",
            "Variable-size logical segments (code, data, stack). "
            "Logical address = (segment#, offset). Segment table -> base + limit. "
            "Combined with paging: segmented paging with two-level translation.",
        ],
        [
            "Page Replacement: LRU",
            "Evict least recently USED page. No Belady's anomaly. Most practical.",
        ],
        [
            "Page Replacement: Optimal",
            "Evict page not needed for longest FUTURE time. Theoretical best. Impossible online.",
        ],
    ],
)

en.highlight(
    "<b>UNIT IV EXAM BLUEPRINT:</b>  "
    "2-mark: Differentiate SRAM and DRAM. Define hit ratio. "
    "State write-through and write-back. Define page fault. Define TLB.  "
    "5-mark: Explain cache direct mapping with address field calculation. "
    "Explain 2-way set-associative mapping with example. "
    "Compare write-through and write-back cache write policies. "
    "Explain virtual memory with address space and memory space. "
    "Explain LRU page replacement with example.  "
    "10-mark: Explain memory hierarchy with diagram. "
    "Explain associative memory (CAM) with hardware organisation. "
    "Explain cache mapping (direct, associative, set-associative) with worked examples. "
    "Explain virtual memory paging with page table and page fault handling. "
    "Explain TLB with effective access time calculation and architecture diagram. "
    "Explain segmented paging with logical address format and translation.",
)

en.sp(10)
en.rule(en.get_theme().rl(en.get_theme().accent), 1.0)
en.sp(6)
en.add(
    Paragraph(
        "Computer Architecture IT-404 Unit IV -- Bharat Dangi  |  UIT-RGPV (Autonomous) Bhopal | Semester IV",
        en.COVER_SUB,
    )
)

# =============================================================================
#  BUILD PDF
# =============================================================================
en.build_doc(
    "CA_Unit4_Notes.pdf",
    title="Computer Architecture - Unit IV Notes",
    author="Bharat Dangi",
)
print("Generated: CA_Unit4_Notes.pdf")
