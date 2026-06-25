"""
Operating Systems (IT412) -- Unit V Notes
UIT-RGPV (Autonomous) Bhopal | Semester IV
Complete exam notes: File System, File and Directory Concepts, Attributes, Operations,
File Types, Directory Structures, Linux File System, FAT, I-node, File Access Methods,
Allocation Methods, Free Space Management, Disk Management, Disk Access Time, Disk Scheduling.

Run:  python os_unit5.py
Output: OS_Unit5_Notes.pdf
"""

from __future__ import annotations

import paperforge_notes as pn
import paperforge_diagrams as pd
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors

# =============================================================================
#  THEME — MIDNIGHT_DARK: deep indigo/violet accent
#  Unit I = CATPPUCCIN_MOCHA, II = FOREST_DARK, III = SUNSET_DARK, IV = OCEAN_DARK, V = MIDNIGHT_DARK
# =============================================================================
pn.set_story([])
pn.set_theme(pn.MIDNIGHT_DARK)

pn.set_global_footer(
    left="Operating Systems (IT412) — Unit V",
    right="UIT-RGPV (Autonomous) Bhopal  |  Semester IV",
    show_page_num=True,
)

diag_theme = pd.DiagramTheme.from_notes_theme(pn.get_theme())

# =============================================================================
#  COVER PAGE
# =============================================================================
pn.bookmark("Cover Page")
pn.suppress_footer(page_only=True)
pn.sp(26)

pn.cover_card(
    "OPERATING SYSTEMS",
    "Unit V — File System & Disk Management",
)
# pn.cover_subtitle(
#     [
#         "Subject Code: IT412  |  UIT-RGPV (Autonomous) Bhopal  |  Semester IV",
#         "File System Structures, Access Methods, Allocation Strategies, I-nodes, FAT,",
#         "Free Space Management, Disk Structure, Latency, RAID & Disk Scheduling Algorithms",
#     ]
# )
pn.sp(10)
pn.rule(pn.get_theme().rl(pn.get_theme().accent), 1.5)
pn.sp(8)

pn.info_table(
    ["Section", "Syllabus Topics Covered"],
    [
        [
            "5.1  File & Directory Concepts",
            "File attributes, operations, file types, directory structures (Single/Two-level, Tree, Acyclic, General), Mounting, File sharing (Hard/Soft links)",
        ],
        [
            "5.2  File Access Methods",
            "Sequential access, Direct (Random) access, Indexed access, ISAM structures",
        ],
        [
            "5.3  File Allocation Methods",
            "Contiguous (Compaction, fit algorithms), Linked (FAT centralization), and Indexed allocation (Multi-level & Combined schemes)",
        ],
        [
            "5.4  Free Space Management",
            "Bit vector (bit map address math), Linked list, Grouping, Counting algorithms, Space maps (ZFS)",
        ],
        [
            "5.5  UNIX I-node & Directory Implementation",
            "Directory tables (Linear list, Hash tables), Unix I-node structure, direct & indirect pointers, file size math",
        ],
        [
            "5.6  Linux & FAT Filesystems",
            "File Allocation Table (FAT12/FAT16/FAT32), Linux ext4 block layout, journaling levels, extents",
        ],
        [
            "5.7  Disk Structure & RAID Systems",
            "Physical disk parameters (platters, cylinders, tracks, sectors), physical/logical formatting, MBR/GPT, bad block sparing, RAID levels (0, 1, 4, 5, 6, 10)",
        ],
        [
            "5.8  Disk Access Time",
            "Seek time, Rotational latency, Transfer time calculations, formulas, RPM conversions",
        ],
        [
            "5.9  Disk Scheduling Algorithms",
            "FCFS, SSTF, SCAN, C-SCAN, LOOK, C-LOOK algorithms, step-by-step worked numericals",
        ],
        [
            "5.10 Exam Questions & Revision",
            "25+ PYQ-style exam questions (2-mark, 5-mark, 10-mark) with detailed calculations and Anki flashcards",
        ],
    ],
    col_widths=["28%", "72%"],
)

# =============================================================================
#  TABLE OF CONTENTS
# =============================================================================
pn.br()
pn.suppress_footer(page_only=True)
pn.toc()

# =============================================================================
#  PART I: FILE SYSTEMS
# =============================================================================
pn.part_box("UNIT V — PART A: FILE SYSTEMS & STORAGE MANAGEMENT")

# =============================================================================
#  5.1  FILE & DIRECTORY CONCEPTS
# =============================================================================
pn.chap_box("5.1  File & Directory Concepts")

pn.section("What is a File?")
pn.definition(
    "<b>File:</b> A named, logical collection of related information that is recorded "
    "on secondary storage. From the user's perspective, a file is the smallest allocation "
    "unit of logical secondary storage. The OS maps these logical files onto physical "
    "storage media (disks, SSDs, magnetic tapes). Files contain both program instructions "
    "and data (numeric, alphabetic, alphanumeric, or binary)."
)

pn.section("File Attributes")
pn.body(
    "A file's attributes vary across operating systems but typically include the following:"
)
pn.bullet(
    [
        "<b>Name:</b> The symbolic file name, which is the only information kept in human-readable form.",
        "<b>Identifier:</b> A unique tag (usually a number) that identifies the file within the filesystem (e.g., inode number).",
        "<b>Type:</b> Needed for systems that support different file types (e.g., text, binary, executable).",
        "<b>Location:</b> A pointer to the physical device and the block location of the file on that device.",
        "<b>Size:</b> The current size of the file (in bytes, words, or blocks) and optionally the maximum allowed size.",
        "<b>Protection:</b> Access-control information that determines who can read, write, or execute the file.",
        "<b>Time, Date, and User Identification:</b> Metadata for creation, last modification, and last use (useful for security and backup).",
    ]
)

pn.section("File Operations")
pn.body(
    "The Operating System provides system calls to perform basic file operations. The six basic file operations are:"
)
pn.info_table(
    ["Operation", "OS Action & System Call Mechanism"],
    [
        [
            "Create",
            "Finds space in the filesystem for the new file, and enters the file details (name, location) into the directory.",
        ],
        [
            "Write",
            "Finds the file using its directory entry. The OS keeps a write pointer to write data at the current position.",
        ],
        [
            "Read",
            "Reads data from the current read pointer position. The OS updates the pointer after reading.",
        ],
        [
            "Reposition (Seek)",
            "Changes the current file position pointer to a specified value without reading or writing (random access).",
        ],
        [
            "Delete",
            "Searches the directory for the file. Releases all associated disk blocks and removes the directory entry.",
        ],
        [
            "Truncate",
            "Keeps all file attributes but deletes the actual file content, resetting the file size to 0 and releasing its blocks.",
        ],
    ],
)

pn.section("Path Resolution & Mounting")
pn.definition(
    "<b>Path Resolution:</b> The process of translating a hierarchical path string "
    "(e.g., <code>/home/user/notes.txt</code>) into a physical block address. "
    "The OS starts at the root directory inode (usually inode 2), searches its directory table for "
    "the next component (e.g., 'home'), retrieves its inode, reads its directory table, "
    "and repeats this process until the target file's inode is found."
)
pn.body(
    "<b>Mounting:</b> A filesystem must be mounted before it can be accessed by the system. "
    "Mounting attaches the root directory of a new filesystem partition (on a USB or second disk) "
    "to a specified folder in the existing directory tree (called the <b>mount point</b>). "
    "The OS redirects any traversal into the mount point folder to the root of the newly mounted device."
)

pn.section("File Sharing: Hard Links vs Symbolic Links")
pn.info_table(
    ["Criterion", "Hard Link", "Symbolic Link (Soft Link / Symlink)"],
    [
        [
            "Definition",
            "A direct directory entry pointing to the same underlying I-node as the original file.",
            "A special type of file that contains a text path string to the target file.",
        ],
        [
            "Link Counter",
            "Increments the link count in the I-node metadata.",
            "Does not affect the target file's I-node link count.",
        ],
        [
            "Deletion Behavior",
            "If the original file is deleted, the data remains accessible via the hard link until the count reaches 0.",
            "If the target file is deleted, the symlink becomes a 'broken link' (points to a non-existent path).",
        ],
        [
            "Cross-Filesystem",
            "Cannot span across different disk partitions or filesystems (requires same inode table).",
            "Can point to files on any filesystem or partition.",
        ],
        [
            "Directories",
            "Normally forbidden on directories to prevent circular loops.",
            "Allowed on directories.",
        ],
    ],
)

pn.section("Directory Structures")
pn.definition(
    "<b>Directory:</b> A structure containing information about files (e.g., name, type, address). "
    "It acts as a translation table mapping file names to directory entries."
)
pn.body(
    "Operating systems structure directories in several ways to support search, creation, deletion, renaming, and nesting:"
)

pn.subsection("1. Single-Level Directory")
pn.body(
    "All files are contained in a single directory. It is shared by all users. "
    "<b>Drawbacks:</b> Naming collisions (two users cannot use the same name) and grouping problems (cannot organize files by subject)."
)

pn.subsection("2. Two-Level Directory")
pn.body(
    "Each user has their own <b>User File Directory (UFD)</b>. The OS maintains a single <b>Master File Directory (MFD)</b> "
    "that indexes the UFDs. "
    "<b>Pros:</b> Solves naming collisions. "
    "<b>Cons:</b> Still lacks hierarchical grouping; sharing files between users is difficult."
)

pn.subsection("3. Tree-Structured Directory")
pn.body(
    "A multi-level tree hierarchy. Users can create subdirectories to organize files. "
    "The directory contains files and subdirectory pointers. Every file has a unique path name "
    "(Absolute path from root, e.g., <code>/home/user/notes.txt</code>; or Relative path from current working directory)."
)

pn.subsection("4. Acyclic-Graph Directory")
pn.body(
    "Allows directories to share subdirectories and files. Unlike a simple tree, a shared file/directory "
    "can exist in two different parent directories. "
    "Implemented via <b>links</b> (pointers to another file/directory) or duplicate directory entries. "
    "<b>Issues:</b> Multiple paths to the same file; deletion handling (dangling pointers if the original file is deleted — "
    "solved by keeping a reference count in the file metadata)."
)

pn.subsection("5. General Graph Directory")
pn.body(
    "Allows cycles within the directory structure (e.g., a subdirectory points back to a parent directory). "
    "<b>Issues:</b> Traversals (searching) can loop infinitely. Deleting files requires <b>garbage collection</b> "
    "or cycle-detection algorithms to reclaim space because reference counts might never reach 0 due to self-referencing loops."
)
pn.br()

# =============================================================================
#  5.2  FILE ACCESS METHODS
# =============================================================================
pn.chap_box("5.2  File Access Methods")

pn.section("Access Methods Comparison")
pn.definition(
    "Operating systems support different access methods depending on the application requirements. "
    "The three primary methods are Sequential Access, Direct (Random) Access, and Indexed Access."
)
pn.sp(4)

pn.info_table(
    ["Access Method", "Operation Principle", "Typical Applications & Examples"],
    [
        [
            "Sequential Access",
            "Information is processed in order, one record after another. "
            "Operations: <code>read_next()</code>, <code>write_next()</code>, <code>reset()</code>. "
            "No jumping forward or backward without passing intermediate bytes.",
            "Editors, compilers, magnetic tape files, audio/video streaming files.",
        ],
        [
            "Direct Access\n(Random Access)",
            "A file is made of fixed-length logical blocks. "
            "Allows reading/writing blocks in any arbitrary order. "
            "Operations: <code>read(block_n)</code>, <code>write(block_n)</code>, <code>seek(block_n)</code>.",
            "Databases, key-value stores, virtual disk images, filesystem metadata blocks.",
        ],
        [
            "Indexed Access",
            "An index file is created containing pointers to various blocks of the primary file. "
            "To find a record, search the index first (fast binary search), get the block pointer, "
            "then access the data block directly.",
            "Large database lookup indexes, ISAM (Indexed Sequential Access Method).",
        ],
    ],
)
pn.br()

# =============================================================================
#  5.3  FILE ALLOCATION METHODS
# =============================================================================
pn.chap_box("5.3  File Allocation Methods")

pn.section("The Allocation Problem")
pn.body(
    "The allocation problem is: how to allocate physical disk blocks to files "
    "so that disk space is utilized effectively and files can be accessed quickly. "
    "There are three major methods: Contiguous, Linked, and Indexed."
)

pn.section("1. Contiguous Allocation")
pn.definition(
    "<b>Contiguous Allocation:</b> Each file occupies a set of contiguous blocks on the disk. "
    "The directory entry for a file needs only: <b>start block address</b> and <b>length</b> (number of blocks)."
)
pn.bullet(
    [
        "<b>Advantages:</b> Excellent read/write performance. "
        "The disk head only needs to seek to the start block; subsequent blocks are read without seeking. "
        "Supports both sequential and direct access.",
        "<b>Disadvantages:</b> External fragmentation — over time, free space is broken into small chunks. "
        "Difficult to declare file size at creation; files cannot grow easily if adjacent blocks are occupied. "
        "Dynamic storage allocation algorithms (First-Fit, Best-Fit, Worst-Fit) must be used, and disk compaction "
        "is required to merge free spaces.",
    ]
)

pn.section("2. Linked Allocation")
pn.definition(
    "<b>Linked Allocation:</b> Each file is a linked list of disk blocks. "
    "The blocks can be scattered anywhere on the disk. "
    "Each block contains a pointer to the next block. "
    "The directory entry needs only: <b>start block pointer</b> and <b>end block pointer</b>."
)
pn.bullet(
    [
        "<b>Advantages:</b> No external fragmentation. "
        "Any free block can satisfy a block request. Files can grow dynamically without limit.",
        "<b>Disadvantages:</b> Poor random access speed. "
        "To access block 10, the OS must read blocks 1 through 9 sequentially to follow the pointers. "
        "Pointer space overhead — e.g., 4 bytes out of a 512-byte block are used for pointers (0.78% loss). "
        "Reliability risk — if a single block pointer gets corrupted, the rest of the file is lost. "
        "<b>Remedy:</b> File Allocation Table (FAT) clusters all pointers in a separate table, solving random access latency.",
    ]
)

pn.section("3. Indexed Allocation")
pn.definition(
    "<b>Indexed Allocation:</b> Each file has its own <b>index block</b>, which is an array of disk block pointers. "
    "The i-th entry in the index block points to the i-th physical block of the file. "
    "The directory entry contains only the address of the index block."
)
pn.bullet(
    [
        "<b>Advantages:</b> Supports direct (random) access. "
        "To read block i, lookup index_block[i] to get the block address. No external fragmentation.",
        "<b>Disadvantages:</b> Pointer overhead. "
        "Even very small files (e.g., 10 bytes) require an entire index block (typically 4 KB), wasting space. "
        "If a file is extremely large, a single index block cannot hold all pointers. "
        "OS must use multi-level indexing, linked index blocks, or combined schemes.",
    ]
)

pn.section("Master Allocation Comparison Table")
pn.info_table(
    ["Criterion", "Contiguous Allocation", "Linked Allocation", "Indexed Allocation"],
    [
        ["External Fragmentation", "Yes (Requires compaction)", "None", "None"],
        [
            "Sequential Access Speed",
            "Excellent (Near-zero seeks)",
            "Good (Slower due to seeks)",
            "Good (Requires reading index)",
        ],
        [
            "Random Access Speed",
            "Excellent (Direct calculation)",
            "Very Poor (O(N) traversal)",
            "Excellent (Direct index lookup)",
        ],
        [
            "Metadata Space Overhead",
            "Very Low (Start, length)",
            "Low (1 pointer per block)",
            "High (Entire index block per file)",
        ],
        [
            "File Growth Capability",
            "Poor (Blocked by neighbors)",
            "Excellent (Dynamic growth)",
            "Excellent (Up to index block limit)",
        ],
    ],
)
pn.br()

# =============================================================================
#  5.4  FREE SPACE MANAGEMENT
# =============================================================================
pn.chap_box("5.4  Free Space Management")

pn.section("Tracking Free Blocks")
pn.body(
    "To allocate disk blocks to files, the OS must maintain a list of all free disk blocks. "
    "The four primary free-space management techniques are:"
)

pn.subsection("1. Bit Vector (Bit Map)")
pn.definition(
    "<b>Bit Vector:</b> The free space is represented as a sequence of bits (bit map). "
    "Each block is represented by 1 bit: "
    "<code>Bit = 1</code> indicates the block is FREE. "
    "<code>Bit = 0</code> indicates the block is ALLOCATED."
)
pn.bullet(
    [
        "<b>Advantages:</b> Extremely simple and efficient to find the first free block or n consecutive free blocks. "
        "Many CPUs provide bit-manipulation instructions to quickly find the first '1' bit in a word.",
        "<b>Search Math:</b> To locate the block number of the first free block, we scan words of the bit vector: "
        "$$\\text{Block } \\# = (\\text{Bits per word}) \\times (\\text{Number of zero-valued words}) + \\text{Index of first 1-bit}$$.",
        "<b>Disadvantage:</b> The bit map must be kept in RAM for efficiency. "
        "For a 1 TB disk with 4 KB blocks, we have 250,000,000 blocks, requiring a 30 MB bit vector. "
        "For larger disks, keeping the entire bit vector in RAM becomes expensive.",
    ]
)

pn.subsection("2. Linked List")
pn.body(
    "All free blocks are linked together. The first free block contains a pointer to the next free block, and so on. "
    "The OS keeps a pointer to the head of this list. "
    "<b>Pros:</b> No extra disk space is wasted (pointers are inside the free blocks themselves). "
    "<b>Cons:</b> Finding contiguous free blocks is extremely slow. Traversing the list requires disk seeks."
)

pn.subsection("3. Grouping")
pn.body(
    "A modification of the linked list. The first free block stores the addresses of <code>N</code> free blocks. "
    "The first <code>N-1</code> blocks are actually free. The <code>N</code>-th block contains the addresses of another "
    "<code>N</code> free blocks, and so on. "
    "<b>Pro:</b> Addresses of multiple free blocks can be read quickly, reducing list traversal seeks."
)

pn.subsection("4. Counting")
pn.body(
    "Instead of keeping a list of every free block, we keep track of the address of the first free block "
    "and the number (count) of contiguous free blocks that follow it. "
    "Each entry in the free-space list consists of: <b>Disk Block Address</b> and <b>Count</b>. "
    "<b>Pro:</b> Highly efficient when disk space is allocated contiguously (reduces the size of the free list)."
)

pn.subsection("5. ZFS Space Maps")
pn.body(
    "Modern filesystems like ZFS use <b>Space Maps</b>. Rather than writing bit maps, ZFS log-structures free space "
    "allocations using an append-only log of events (e.g., 'allocate block 10', 'free blocks 20-25'). "
    "This list is read into memory and constructed into AVL trees for super-fast, low-overhead lookup."
)
pn.br()

# =============================================================================
#  5.5  UNIX I-NODE & DIRECTORY IMPLEMENTATION
# =============================================================================
pn.chap_box("5.5  UNIX I-node & Directory Implementation")

pn.section("Directory Implementation")
pn.body(
    "A directory maps file names to metadata and block pointers. The two primary methods are:"
)
pn.bullet(
    [
        "<b>Linear List:</b> A simple list of file names with pointers to data blocks. "
        "Creation requires searching the list to ensure no duplicate names (O(N) search). "
        "Deletion also requires O(N) search. Very simple to code but slow for directories with thousands of files.",
        "<b>Hash Table:</b> A hash function is applied to the file name to get a directory entry index. "
        "Reduces directory search time to O(1) average. "
        "<b>Drawbacks:</b> Collision handling (two names hashing to same index); "
        "resizing the hash table as directory grows; hash function computation overhead.",
    ]
)

pn.section("The UNIX I-node Structure")
pn.definition(
    "<b>I-node (Index Node):</b> A data structure on disk that represents a file in UNIX/Linux systems. "
    "It contains all metadata about the file (owner, permissions, size, timestamps) EXCEPT the file name. "
    "It also contains pointers to the actual data blocks storing the file's contents."
)
pn.body(
    "To support both very small and very large files efficiently, a standard UNIX I-node contains "
    "<b>15 pointers</b> in its block-lookup table:"
)
pn.bullet(
    [
        "<b>Direct Pointers (0 to 11):</b> 12 pointers that point directly to data blocks. "
        "If block size is 4 KB, direct pointers can address up to <code>12 × 4 KB = 48 KB</code>. "
        "Ensures very fast access for small files.",
        "<b>Single Indirect Pointer (12):</b> Points to an <b>index block</b> that contains pointers to data blocks. "
        "If block size is 4 KB and each pointer is 4 bytes, the index block holds <code>4096 / 4 = 1024</code> pointers. "
        "Addresses up to <code>1024 × 4 KB = 4 MB</code>.",
        "<b>Double Indirect Pointer (13):</b> Points to an index block that contains pointers to 1024 single indirect index blocks. "
        "Addresses up to <code>1024 × 1024 × 4 KB = 1024^2 × 4 KB = 4 GB</code>.",
        "<b>Triple Indirect Pointer (14):</b> Points to an index block containing pointers to 1024 double indirect blocks. "
        "Addresses up to <code>1024 × 1024 × 1024 × 4 KB = 1024^3 × 4 KB = 4 TB</code>.",
    ]
)

pn.section("UNIX I-node Address Translation Sequence")
seq_inode = pd.SequenceDiagram(
    width=pn.CW,
    height=250,
    theme=diag_theme,
    caption="Fig 5.1: UNIX I-node — Multi-level address translation sequence",
    margin=45.0,
)
seq_inode.actor("vfs", "VFS (OS)")
seq_inode.actor("inode", "I-node Table")
seq_inode.actor("ind", "Indirect Blocks\n(RAM Cache)")
seq_inode.actor("disk", "Physical Disk")
seq_inode.message("vfs", "inode", "Read file offset 5,000,000 (Block 1220)")
seq_inode.activate("inode")
seq_inode.message(
    "inode",
    "inode",
    "Verify: 1220 > 12 (Direct) and\n1220 < 1036 (Single Ind). Double Ind block 13 used.",
    arrow="solid",
)
seq_inode.message("inode", "disk", "Fetch Double Indirect Block index", arrow="solid")
seq_inode.message("disk", "inode", "Index block data", arrow="dashed")
seq_inode.message(
    "inode", "ind", "Resolve Double Indirect Offset pointer", arrow="solid"
)
seq_inode.activate("ind")
seq_inode.message("ind", "disk", "Fetch Single Indirect index block", arrow="solid")
seq_inode.message("disk", "ind", "Pointers data", arrow="dashed")
seq_inode.message("ind", "disk", "Fetch final data block", arrow="solid")
seq_inode.message("disk", "ind", "File data blocks", arrow="dashed")
seq_inode.deactivate("ind")
seq_inode.deactivate("inode")
seq_inode.message("inode", "vfs", "Return file data bytes", arrow="dashed")
pn.story.extend(seq_inode.as_flowable())
pn.sp(8)

pn.section("Worked Example: UNIX I-node Capacity Calculation")
pn.highlight(
    "<b>Problem:</b> Given a UNIX filesystem with 4 KB block size and 4-byte disk addresses. "
    "Calculate the maximum file size that can be supported by an I-node with 12 direct, "
    "1 single indirect, 1 double indirect, and 1 triple indirect pointer.<br/><br/>"
    "<b>Solution:</b><br/>"
    "1. Number of pointers per index block = 4 KB / 4 bytes = 1024 pointers.<br/>"
    "2. <b>Direct blocks:</b> 12 blocks × 4 KB = 48 KB.<br/>"
    "3. <b>Single indirect:</b> 1024 blocks × 4 KB = 4,096 KB = 4 MB.<br/>"
    "4. <b>Double indirect:</b> 1024² blocks × 4 KB = 1,048,576 blocks × 4 KB = 4,194,304 KB = 4 GB.<br/>"
    "5. <b>Triple indirect:</b> 1024³ blocks × 4 KB = 1,073,741,824 blocks × 4 KB = 4,294,967,296 KB = 4 TB.<br/>"
    "6. <b>Total maximum file size:</b> 48 KB + 4 MB + 4 GB + 4 TB = <b>4.004 TB</b>."
)
pn.br()

# =============================================================================
#  5.6  LINUX & FAT FILESYSTEMS
# =============================================================================
pn.chap_box("5.6  Linux & FAT Filesystems")

pn.section("FAT (File Allocation Table) Filesystem")
pn.definition(
    "<b>FAT Filesystem:</b> A simple filesystem layout introduced by Microsoft. "
    "It uses a table called the File Allocation Table located at the start of the disk partition. "
    "The disk is divided into fixed-size clusters, and the FAT has one entry per cluster."
)
pn.body("How FAT works for file allocation:")
pn.bullet(
    [
        "A file's directory entry contains its name and the <b>starting cluster number</b>.",
        "The FAT table is indexed by cluster number. For a cluster <code>C</code>, the entry <code>FAT[C]</code> "
        "contains the address of the <b>next cluster</b> in the file.",
        "A special value (e.g., <code>0xFFFF</code> for FAT16) in <code>FAT[C]</code> indicates End of File (EOF).",
        "Unused clusters are marked with <code>0</code>.",
        "<b>FAT Varieties:</b> FAT12 (12-bit entries), FAT16 (16-bit entries, max partition size 2 GB), "
        "FAT32 (32-bit entries, max file size 4 GB, max partition size 2 TB).",
    ]
)

pn.section("Linux ext4 Filesystem")
pn.definition(
    "<b>ext4 (Fourth Extended Filesystem):</b> The default filesystem for most modern Linux distributions. "
    "It improves on ext3 by supporting larger volume sizes (up to 1 Exabyte) and files (up to 16 Terabytes), "
    "and using extents instead of traditional block pointer indexing."
)
pn.bullet(
    [
        "<b>Extents:</b> Instead of allocating space block-by-block and listing individual pointers, "
        "ext4 allocates space in contiguous ranges of blocks called <b>extents</b>. "
        "An extent is represented as: <code>(Starting block number, Number of blocks)</code>. "
        "A single extent can represent up to 128 MB of contiguous space, drastically reducing the metadata size "
        "for large files and reducing external fragmentation.",
        "<b>Journaling:</b> Writes changes to a temporary circular log (journal) before committing them to the main filesystem. "
        "If a power loss occurs, the OS reads the journal to recover the filesystem to a consistent state instantly, "
        "avoiding slow full-disk checks (like <code>fsck</code>). "
        "Modes: <i>Journal</i> (metadata + data logged), <i>Ordered</i> (metadata logged, data written first - default), "
        "<i>Writeback</i> (metadata logged, data written asynchronously).",
        "<b>Delayed Allocation:</b> Delays block allocation on disk until data is flushed from RAM cache. "
        "Allows the OS to allocate large contiguous block sets, reducing fragmentation.",
    ]
)

pn.section("FAT vs Linux Filesystem Layout")
left_fs = pd.LayeredStack(width=pn.CW * 0.46, height=180)
left_fs.layer("Boot Sector", sublabel="Metadata & BIOS Parameter Block")
left_fs.layer("File Allocation Table", sublabel="Linked cluster indices")
left_fs.layer("Root Directory", sublabel="Pointers to first clusters")
left_fs.layer("Data Clusters", sublabel="Actual file content space")

right_fs = pd.LayeredStack(width=pn.CW * 0.46, height=180)
right_fs.layer("Boot Block / Superblock", sublabel="FS size, limits, mount counts")
right_fs.layer("Group Descriptors", sublabel="Offsets of bitmaps & tables")
right_fs.layer("Bitmaps & Inode Table", sublabel="Block/Inode usage lists")
right_fs.layer("Data Blocks", sublabel="Raw files and subdirs data")

left_fs.build()
right_fs.build()

tbl_layout = Table(
    [
        [
            pd.ResponsiveDrawingFlowable(left_fs.drawing),
            pd.ResponsiveDrawingFlowable(right_fs.drawing),
        ]
    ],
    colWidths=[pn.CW * 0.48, pn.CW * 0.48],
)
tbl_layout.setStyle(
    TableStyle(
        [
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ]
    )
)
pn.add(tbl_layout)
pn.br()

# =============================================================================
#  PART II: DISK MANAGEMENT
# =============================================================================
pn.part_box("UNIT V — PART B: DISK MANAGEMENT & SCHEDULING")

# =============================================================================
#  5.7  DISK STRUCTURE & RAID SYSTEMS
# =============================================================================
pn.chap_box("5.7  Disk Structure & RAID Systems")

pn.section("Physical Disk Structure")
pn.definition(
    "<b>Magnetic Disk:</b> A secondary storage device made of magnetic platters that rotate "
    "rapidly. Data is read and written by magnetic heads mounted on a moving actuator arm."
)
pn.body(
    "The physical geometry of a hard disk drive (HDD) consists of the following components:"
)
pn.bullet(
    [
        "<b>Platters:</b> Flat circular disks coated with magnetic material. A disk contains multiple platters.",
        "<b>Tracks:</b> Each platter surface is divided logically into concentric rings called tracks.",
        "<b>Sectors:</b> Each track is divided into smaller segments called sectors (usually 512 bytes or 4 KB in size). "
        "The sector is the smallest unit of physical transfer on a disk.",
        "<b>Cylinders:</b> The set of all tracks at a given arm position across all platters. "
        "If a disk has 4 platters (8 surfaces), a cylinder consists of 8 concentric tracks.",
    ]
)

pn.section("Disk Formatting & Management")
pn.bullet(
    [
        "<b>Physical Formatting (Low-Level Formatting):</b> Performed at the factory. "
        "Divides the magnetic platters into sectors. Writes headers, trailers, and Error-Correcting Codes (ECC) "
        "for each sector so the disk controller can identify sectors and detect read errors.",
        "<b>Logical Formatting (High-Level Formatting):</b> Performed by the user/OS. "
        "Divides the disk into partitions and writes filesystem data structures (boot block, free space maps, "
        "inode tables, root directory) onto the disk. The disk is now ready to mount and store files.",
        "<b>Boot Block:</b> When powered on, ROM bootstrap loader loads a larger boot loader from the boot block "
        "(MBR or GPT) on the disk, which then loads the full OS kernel.",
        "<b>Sector Sparing:</b> Disk controller maps bad sector addresses internally to a set of healthy spare sectors.",
    ]
)

pn.section("RAID (Redundant Array of Independent Disks)")
pn.definition(
    "<b>RAID:</b> A technology that combines multiple physical hard drives into a single logical "
    "unit to achieve data redundancy (fault tolerance) and/or performance improvement (speed)."
)
pn.sp(4)

pn.info_table(
    ["RAID Level", "Mechanism & Concept", "Pros, Cons & Applications"],
    [
        [
            "RAID 0\n(Striping)",
            "Splits data blocks evenly across multiple disks without redundancy. "
            "E.g., Block 1 on Disk 1, Block 2 on Disk 2.",
            "<b>Pros:</b> Fast read/write speeds. "
            "<b>Cons:</b> No fault tolerance. If one disk fails, all data is lost. "
            "Used in video editing caches.",
        ],
        [
            "RAID 1\n(Mirroring)",
            "Duplicates data identically onto two or more disks. "
            "Disk 2 is an exact clone of Disk 1.",
            "<b>Pros:</b> High fault tolerance. Tolerates N-1 failures. "
            "<b>Cons:</b> High cost (50% storage overhead). "
            "Used in OS boot drives.",
        ],
        [
            "RAID 5\n(Distributed Parity)",
            "Stripes data blocks across three or more disks and distributes "
            "parity blocks across all disks. Parity is calculated via XOR.",
            "<b>Pros:</b> Good read performance, storage-efficient. Tolerates 1 disk failure. "
            "<b>Cons:</b> Parity write penalty. "
            "Used in file servers.",
        ],
        [
            "RAID 6\n(Double Distributed Parity)",
            "Stripes data and writes two independent distributed parity blocks "
            "(P and Q) per stripe. Requires at least 4 disks.",
            "<b>Pros:</b> Tolerates 2 concurrent disk failures. "
            "<b>Cons:</b> Slow write performance due to double parity calculations.",
        ],
        [
            "RAID 10\n(Stripe of Mirrors)",
            "A hybrid scheme combining RAID 1 and RAID 0. Disks are mirrored (RAID 1) "
            "and then striped (RAID 0). Requires at least 4 disks.",
            "<b>Pros:</b> Excellent performance and redundancy. "
            "<b>Cons:</b> High disk cost (50% storage overhead).",
        ],
    ],
)
pn.br()

# =============================================================================
#  5.8  DISK ACCESS TIME
# =============================================================================
pn.chap_box("5.8  Disk Access Time")

pn.section("Components of Disk Access Time")
pn.definition(
    "<b>Disk Access Time:</b> The total time taken by the disk drive to locate and transfer "
    "a requested block of data. It is the sum of three distinct components: Seek Time, "
    "Rotational Latency, and Transfer Time."
)

pn.formula_block(r"T_{access} = T_{seek} + T_{rotational\_latency} + T_{transfer}")
pn.sp(4)

pn.info_table(
    ["Component", "Definition & Formula", "Key Determining Factors"],
    [
        [
            "Seek Time\n(T_seek)",
            "The time taken to move the disk arm to the cylinder containing the requested sector. "
            "This is the slowest component of disk access.",
            "Distance to travel, acceleration/deceleration of the actuator arm.",
        ],
        [
            "Rotational Latency\n(T_rotational)",
            "The time taken for the requested sector to rotate under the read/write head. "
            "<b>Average Rotational Latency:</b> "
            "$$\\text{Avg } T_{rotational} = \\frac{1}{2 \\times \\text{RPM}} \\times 60 \\text{ seconds}$$",
            "Disk rotation speed (RPM). E.g., for 7200 RPM, avg latency = 60 / (2 × 7200) = 4.17 ms.",
        ],
        [
            "Transfer Time\n(T_transfer)",
            "The time taken to physically read/write the data from/to the platter surface. "
            "$$T_{transfer} = \\frac{\\text{Bytes to Transfer}}{\\text{Rotation Speed} \\times \\text{Track Capacity}}$$",
            "Data size, disk density, rotation speed.",
        ],
    ],
)
pn.br()

# =============================================================================
#  5.9  DISK SCHEDULING ALGORITHMS
# =============================================================================
pn.chap_box("5.9  Disk Scheduling Algorithms")

pn.section("Why Disk Scheduling?")
pn.body(
    "Since seek time is the dominant factor in disk access overhead, the OS schedules "
    "the order of pending disk read/write requests to minimize the total seek distance "
    "(head movement). The major disk scheduling algorithms are:"
)

pn.info_table(
    ["Algorithm", "Selection Criterion / Operation", "Pros & Cons"],
    [
        [
            "FCFS\n(First-Come, First-Served)",
            "Requests are serviced in the order they arrive in the queue. No reordering.",
            "<b>Pros:</b> Simple, fair, no starvation. "
            "<b>Cons:</b> High head travel; no optimization.",
        ],
        [
            "SSTF\n(Shortest Seek Time First)",
            "Selects the request closest to the current head position (minimizes immediate seek).",
            "<b>Pros:</b> Low average waiting time. "
            "<b>Cons:</b> Can cause <b>starvation</b> of far requests if new close requests keep arriving.",
        ],
        [
            "SCAN\n(Elevator Algorithm)",
            "Head moves in one direction servicing all requests until it reaches the **very end** of the disk, "
            "then reverses direction and services requests in the opposite direction.",
            "<b>Pros:</b> Prevents starvation; uniform wait. "
            "<b>Cons:</b> Unfair to requests that just missed the sweep; moves arm to the extreme end even if no requests are there.",
        ],
        [
            "C-SCAN\n(Circular SCAN)",
            "Head moves in one direction servicing requests. When it reaches the **very end**, "
            "it immediately jumps back to the **start** (cylinder 0) without servicing any requests on the return trip.",
            "<b>Pros:</b> Provides a highly uniform waiting time for all cylinders. "
            "<b>Cons:</b> Jumps all the way back to cylinder 0.",
        ],
        [
            "LOOK",
            "Like SCAN, but the arm only goes as far as the **last request** in the current direction. "
            "It reverses immediately without traveling to the extreme edge of the disk.",
            "<b>Pros:</b> Saves unnecessary head travel. "
            "<b>Cons:</b> Marginally more logic.",
        ],
        [
            "C-LOOK",
            "Like C-SCAN, but the arm only travels to the last request in the current direction, "
            "then jumps directly back to the **first request** at the other side of the disk.",
            "<b>Pros:</b> Most efficient sweep algorithm. "
            "<b>Cons:</b> Slightly complex controller logic.",
        ],
    ],
)

pn.section("Disk Controller State Machine Model")
sm_disk = pd.StateMachine(
    width=pn.CW * 0.75,
    height=200,
    theme=diag_theme,
    caption="Fig 5.2: State transition model of a disk I/O request lifecycle",
)
sm_disk.state("queue", "Request Queue\n(in OS Device Driver)", initial=True)
sm_disk.state("seek", "Seeking\n(Arm moving to Cylinder)")
sm_disk.state("rotate", "Rotational Latency\n(Waiting for Sector)")
sm_disk.state("transfer", "Transferring Data\n(Sector Read/Write)")
sm_disk.state("done", "Complete\n(Interrupt triggered)", accepting=True)
sm_disk.transition("queue", "seek", label="Scheduler chooses next request")
sm_disk.transition("seek", "rotate", label="Heads aligned on Cylinder")
sm_disk.transition("rotate", "transfer", label="Sector passes under Head")
sm_disk.transition("transfer", "done", label="All bytes transferred")
pn.story.extend(sm_disk.as_flowable())
pn.sp(8)

pn.section("Worked Numericals: Disk Scheduling algorithms")
pn.body(
    "<b>Problem Statement:</b> Given a disk queue with requests for blocks: "
    "<code>[98, 183, 37, 122, 14, 124, 65, 67]</code>. "
    "The head starts at cylinder <b>53</b>. The disk has cylinders ranging from <b>0 to 199</b>. "
    "Calculate the total head movement (seek distance) for FCFS, SSTF, SCAN (moving toward 0), "
    "and C-SCAN (moving toward 199)."
)

pn.subsection("1. FCFS (First-Come, First-Served)")
pn.body("Head path: 53 → 98 → 183 → 37 → 122 → 14 → 124 → 65 → 67")
pn.info_table(
    ["Step transition", "Calculation", "Head travel"],
    [
        ["53 to 98", "|98 - 53|", "45"],
        ["98 to 183", "|183 - 98|", "85"],
        ["183 to 37", "|37 - 183|", "146"],
        ["37 to 122", "|122 - 37|", "85"],
        ["122 to 14", "|14 - 122|", "108"],
        ["14 to 124", "|124 - 14|", "110"],
        ["124 to 65", "|65 - 124|", "59"],
        ["65 to 67", "|67 - 65|", "2"],
        ["Total Seek Distance", "45+85+146+85+108+110+59+2", "<b>640 cylinders</b>"],
    ],
)

pn.subsection("2. SSTF (Shortest Seek Time First)")
pn.body("Sorted requests: 14, 37, 65, 67, 98, 122, 124, 183. Starting head: 53.")
pn.info_table(
    ["Current Head", "Closest Request", "Calculation", "Head Travel"],
    [
        ["53", "65 (diff 12 vs 16 to 37)", "|65 - 53|", "12"],
        ["65", "67 (diff 2 vs 28 to 37)", "|67 - 65|", "2"],
        ["67", "37 (diff 30 vs 31 to 98)", "|37 - 67|", "30"],
        ["37", "14 (diff 23 vs 61 to 98)", "|14 - 37|", "23"],
        ["14", "98 (closest remaining)", "|98 - 14|", "84"],
        ["98", "122 (diff 24 vs 26 to 124)", "|122 - 98|", "24"],
        ["122", "124 (diff 2 vs 61 to 183)", "|124 - 122|", "2"],
        ["124", "183 (last remaining)", "|183 - 124|", "59"],
        ["Total Seek Distance", "12+2+30+23+84+24+2+59", "<b>236 cylinders</b>"],
    ],
)

pn.subsection("3. SCAN (moving toward 0)")
pn.body(
    "Head starts at 53 and moves toward 0. It services all requests in its path (37, 14), "
    "reaches the boundary cylinder 0, then reverses toward 199, servicing remaining requests (65, 67, 98, 122, 124, 183)."
)
pn.info_table(
    ["Head Path", "Cylinder Range / Math", "Seek Distance"],
    [
        ["53 → 37 → 14 → 0", "53 - 0", "53"],
        ["0 → 65 → 67 → 98 → 122 → 124 → 183", "183 - 0", "183"],
        ["Total Seek Distance", "53 + 183", "<b>236 cylinders</b>"],
    ],
)

pn.subsection("4. C-SCAN (moving toward 199)")
pn.body(
    "Head starts at 53 and moves toward 199. It services 65, 67, 98, 122, 124, 183, reaches the "
    "boundary cylinder 199, jumps directly to 0 (no service), then moves toward 199, servicing 14, 37."
)
pn.info_table(
    ["Head Path", "Cylinder Range / Math", "Seek Distance"],
    [
        ["53 → 65 → 67 → 98 → 122 → 124 → 183 → 199", "199 - 53", "146"],
        ["199 → 0 (jump)", "0 (no head travel cost counted)", "0"],
        ["0 → 14 → 37", "37 - 0", "37"],
        ["Total Seek Distance", "146 + 0 + 37", "<b>183 cylinders</b>"],
    ],
)
pn.br()

# =============================================================================
#  5.10 EXAM QUESTIONS & ANSWERS
# =============================================================================
pn.part_box("UNIT V — EXAM QUESTIONS & DETAILED ANSWERS")
pn.chap_box("5.10 Previous-Year Style Exam Questions")

pn.section("2-Mark Questions (Short Concept Qs)")

pn.highlight(
    "<b>Q1. What is seek time vs rotational latency?</b><br/>"
    "A: Seek time is the time taken to move the disk arm to the correct cylinder (track). "
    "Rotational latency is the time taken for the target sector to rotate under the read/write head. "
    "Seek time is a mechanical movement and is significantly slower than rotational latency."
)

pn.highlight(
    "<b>Q2. What is sector sparing?</b><br/>"
    "A: Sector sparing is a bad-block management technique where the disk controller reallocates "
    "the address of a defective (bad) sector to a reserved healthy spare sector. "
    "This mapping is transparent to the operating system."
)

pn.highlight(
    "<b>Q3. What is an I-node in Linux?</b><br/>"
    "A: An I-node (index node) is a disk data structure that represents a file. "
    "It stores all file metadata (owner, permissions, size, timestamps) and block address pointers, "
    "but does not store the file name, which is kept in directory entries."
)

pn.highlight(
    "<b>Q4. Define average rotational latency for a 5400 RPM disk.</b><br/>"
    "A: A 5400 RPM disk makes 5400 rotations per minute, or 90 rotations per second. "
    "One rotation takes 1/90 seconds ≈ 11.1 ms. "
    "Average rotational latency is half the time of one rotation: 11.1 / 2 = <b>5.56 ms</b>."
)

pn.highlight(
    "<b>Q5. What is the convoy effect in disk scheduling?</b><br/>"
    "A: The convoy effect in FCFS disk scheduling occurs when a request for a cylinder "
    "far away from the current position causes the head to sweep across the entire disk, "
    "forcing subsequent close requests to wait a long time, causing queue buildup."
)

pn.highlight(
    "<b>Q6. Why is a soft link different from a hard link?</b><br/>"
    "A: A hard link is an actual directory entry pointing directly to the file's I-node, "
    "incrementing its link counter. A symbolic (soft) link is a separate file that contains "
    "a text path pointer to the target file. Deleting the original file breaks a symbolic link, "
    "but a hard link remains valid as long as its count is greater than zero."
)

pn.highlight(
    "<b>Q7. What is filesystem journaling?</b><br/>"
    "A: Journaling is a technique where filesystem updates are written first to a circular log "
    "(journal) before committing them to the main directory structures. This ensures filesystem "
    "integrity can be instantly restored in the event of a sudden power loss."
)

pn.highlight(
    "<b>Q8. What are extents in Linux ext4 filesystem?</b><br/>"
    "A: Extents represent contiguous block ranges allocated to a file at once, denoted as "
    "<code>(starting_block, count)</code>. This replaces the traditional block-by-block pointer list, "
    "greatly reducing file metadata size and enhancing I/O speed."
)

pn.highlight(
    "<b>Q9. Define RAID 0 and state its primary disadvantage.</b><br/>"
    "A: RAID 0 uses data striping across multiple disks to optimize performance. Its primary "
    "disadvantage is the lack of redundancy: it has no fault tolerance. If one disk fails, "
    "the entire logical volume is corrupted."
)

pn.highlight(
    "<b>Q10. Explain Master Boot Record (MBR) role in booting.</b><br/>"
    "A: The MBR is the first sector (sector 0) of a bootable partition. It contains the primary "
    "partition table and the bootstrap loader code. When system powers on, BIOS loads MBR "
    "into RAM, executing the loader to find and boot the active partition's OS kernel."
)

pn.section("5-Mark Questions (Detailed Explanations)")

pn.highlight(
    "<b>Q11. Compare Contiguous, Linked, and Indexed file allocation methods.</b><br/>"
    "A: (1) <b>Contiguous Allocation:</b> Files occupy contiguous blocks. Fast sequential/random access, "
    "but suffers from external fragmentation and file growth limitations. "
    "(2) <b>Linked Allocation:</b> Blocks are linked via pointers. No external fragmentation, easy file growth, "
    "but poor random access (must traverse links) and pointer space overhead. "
    "(3) <b>Indexed Allocation:</b> File has an index block storing block pointers. Supports direct access, "
    "no external fragmentation, but has index block space overhead, especially for small files."
)

pn.highlight(
    "<b>Q12. Explain the directory structures used in filesystems.</b><br/>"
    "A: (1) <b>Single-Level:</b> All files in one folder. Naming conflicts, no nesting. "
    "(2) <b>Two-Level:</b> One folder per user. Solves naming conflicts, no grouping. "
    "(3) <b>Tree-Structured:</b> Standard hierarchical folder structure. Path names, nesting. "
    "(4) <b>Acyclic-Graph:</b> Allows folders/files to have multiple parents (sharing via links). "
    "Requires reference counting to prevent dangling pointers upon deletion. "
    "(5) <b>General Graph:</b> Cycles allowed. Traversal loops possible; requires garbage collection."
)

pn.highlight(
    "<b>Q13. Describe the methods of free space management.</b><br/>"
    "A: (1) <b>Bit Map / Vector:</b> Array of bits representing blocks (1=free, 0=allocated). "
    "Fast lookup, but must fit in RAM. "
    "(2) <b>Linked List:</b> Free blocks linked via pointers. Easy to implement, but slow to traverse. "
    "(3) <b>Grouping:</b> First free block holds addresses of next N-1 free blocks. "
    "(4) <b>Counting:</b> Keeps track of first free block address and the number of contiguous free blocks following it."
)

pn.highlight(
    "<b>Q14. Discuss the concept of directory implementation via linear list and hash tables.</b><br/>"
    "A: (1) <b>Linear List:</b> File names and block pointers are stored in a simple sequence. "
    "Easy to implement, but requires O(N) search to find, delete, or check duplicate entries during file creation. "
    "(2) <b>Hash Table:</b> Uses a hash function on the filename to map it to a directory hash list. "
    "Provides extremely fast average lookup time (O(1)). "
    "However, requires handling hash collisions (chaining/open addressing) and table resizing overhead."
)

pn.highlight(
    "<b>Q15. Explain RAID levels 1, 5, and 6 in details.</b><br/>"
    "A: (1) <b>RAID 1 (Mirroring):</b> Data is cloned identically onto a mirror drive. "
    "Provides excellent redundancy, quick reads, but suffers from 100% capacity overhead. "
    "(2) <b>RAID 5 (Distributed Parity):</b> Stripes blocks across disks and distributes parity data. "
    "Tolerates 1 disk failure, utilizes space efficiently, but has write speed overhead. "
    "(3) <b>RAID 6 (Double Distributed Parity):</b> Uses two independent parity layers (P and Q). "
    "Can handle the simultaneous failure of up to 2 disks, but requires complex block parity calculation."
)

pn.highlight(
    "<b>Q16. Describe physical and logical disk formatting.</b><br/>"
    "A: (1) <b>Physical (Low-Level) Formatting:</b> Divides the disk platter surfaces into sectors "
    "and writes headers, trailers, and Error-Correcting Code (ECC) blocks. Performed by manufacturer. "
    "(2) <b>Logical (High-Level) Formatting:</b> Partitioning the disk and initializing filesystem metadata structures. "
    "It creates the boot block, superblock/partition descriptors, inode tables, free-space allocation bitmaps, "
    "and the root directory table, preparing the disk for mounting."
)

pn.section("10-Mark Questions (Complex Analysis & Numericals)")

pn.highlight(
    "<b>Q17. Explain the UNIX I-node block pointer layout in detail. "
    "Compute the maximum file size supported if the block size is 8 KB and pointer size is 8 bytes.</b><br/>"
    "A: The UNIX I-node contains 15 pointers: 12 direct (points to data blocks), "
    "1 single indirect (index block of pointers), 1 double indirect (index of index blocks), "
    "and 1 triple indirect (index of double indirect blocks).<br/><br/>"
    "<b>Calculation:</b><br/>"
    "1. Pointers per index block = 8 KB / 8 bytes = 1024 pointers.<br/>"
    "2. <b>Direct blocks:</b> 12 × 8 KB = 96 KB.<br/>"
    "3. <b>Single indirect:</b> 1024 × 8 KB = 8,192 KB = 8 MB.<br/>"
    "4. <b>Double indirect:</b> 1024² × 8 KB = 1,048,576 × 8 KB = 8,388,608 KB = 8 GB.<br/>"
    "5. <b>Triple indirect:</b> 1024³ × 8 KB = 1,073,741,824 × 8 KB = 8,589,934,592 KB = 8 TB.<br/>"
    "6. <b>Total max size:</b> 96 KB + 8 MB + 8 GB + 8 TB = <b>8.008 Terabytes</b>."
)

pn.highlight(
    "<b>Q18. Explain FCFS, SSTF, SCAN, and C-SCAN disk scheduling algorithms. "
    "A disk queue has pending requests: [86, 147, 91, 177, 94, 150]. "
    "Current head position is at 143 (prev 125, toward larger numbers). "
    "Calculate the total head movement for SSTF, SCAN, and LOOK (cylinders 0-199).</b><br/>"
    "A: Sorted queue: 86, 91, 94, 147, 150, 177. Starting head = 143.<br/><br/>"
    "<b>SSTF:</b> Head chooses closest request first.<br/>"
    "143 → 147 (travel |147-143| = 4)<br/>"
    "147 → 150 (travel |150-147| = 3)<br/>"
    "150 → 177 (travel |177-150| = 27)<br/>"
    "177 → 94 (travel |94-177| = 83)<br/>"
    "94 → 91 (travel |91-94| = 3)<br/>"
    "91 → 86 (travel |86-91| = 5)<br/>"
    "Total SSTF Seek Distance = 4 + 3 + 27 + 83 + 3 + 5 = <b>125 cylinders</b>.<br/><br/>"
    "<b>SCAN (moving toward larger numbers / 199):</b><br/>"
    "Services 147, 150, 177, then reaches end 199. Reverses toward 0, services 94, 91, 86.<br/>"
    "Path: 143 → 147 → 150 → 177 → 199 (travel 199 - 143 = 56).<br/>"
    "199 → 94 → 91 → 86 (travel 199 - 86 = 113).<br/>"
    "Total SCAN Seek Distance = 56 + 113 = <b>169 cylinders</b>.<br/><br/>"
    "<b>LOOK (moving toward larger numbers / 199):</b><br/>"
    "Like SCAN but reverses immediately at the last request (177) without traveling to 199.<br/>"
    "Path: 143 → 147 → 150 → 177 (travel 177 - 143 = 34).<br/>"
    "177 → 94 → 91 → 86 (travel 177 - 86 = 91).<br/>"
    "Total LOOK Seek Distance = 34 + 91 = <b>125 cylinders</b>."
)

pn.highlight(
    "<b>Q19. Describe the File Allocation Table (FAT) filesystem layout and cluster allocation. "
    "What are its advantages and disadvantages compared to UNIX I-node?</b><br/>"
    "A: <b>FAT structure:</b> It centralizes allocation pointers into a table at the start of the disk partition. "
    "The partition directory entry points to the first cluster number. The FAT table is indexed by cluster number; "
    "each entry stores the next cluster number in the chain, or an EOF marker.<br/><br/>"
    "<b>Comparison with UNIX I-node:</b><br/>"
    "1. <b>Random Access:</b> In FAT, random access requires traversing the table from the beginning (slow if table is on disk, "
    "requiring caching in RAM). I-node provides fast direct indexing (O(1)) via direct/indirect pointers.<br/>"
    "2. <b>Space Overhead:</b> FAT table size is proportional to the disk size, not file size. "
    "I-node overhead is proportional to the number and size of open/created files.<br/>"
    "3. <b>Reliability:</b> FAT table corruption corrupts the entire filesystem. Inodes partition metadata, "
    "confining corruption to single files."
)

pn.section("Quick Revision Table — Unit V")
pn.info_table(
    ["Topic", "Key Exam Points"],
    [
        [
            "File Attributes",
            "Name, Identifier (inode), Type, Location, Size, Protection, Timestamps.",
        ],
        [
            "Directory Structures",
            "Single-level (naming conflicts), Two-level (user folders), Tree (nested paths), "
            "Acyclic graph (sharing/links), General graph (cycles allowed, garbage collection).",
        ],
        [
            "Allocation Methods",
            "Contiguous (best performance, external fragmentation) vs "
            "Linked (no fragmentation, poor random access) vs "
            "Indexed (index block, supports direct access).",
        ],
        [
            "Free Space Management",
            "Bit Vector (1 bit/block, fast but memory overhead) vs "
            "Linked List (no overhead, slow search) vs Grouping vs Counting.",
        ],
        [
            "UNIX I-node",
            "12 Direct, 1 Single Indirect, 1 Double Indirect, 1 Triple Indirect pointers.",
        ],
        [
            "Linux ext4 Features",
            "Extents (block ranges), journaling (fast recovery), delayed allocation.",
        ],
        [
            "Disk Access Time",
            "Access Time = Seek Time + Rotational Latency + Transfer Time. Seek is slowest.",
        ],
        [
            "Disk Scheduling",
            "FCFS (fair, slow) | SSTF (fast, starvation risk) | "
            "SCAN (elevator, sweeps to end) | C-SCAN (uniform wait, return sweep empty).",
        ],
        [
            "Boot Block & Bad Blocks",
            "Bootstrap loader in ROM loads OS from boot block. Bad blocks mapped via sector sparing.",
        ],
    ],
)

pn.exam(
    "Unit V High-Frequency Exam Topics: "
    "(1) Disk scheduling numericals — calculate seek distance for SSTF, SCAN, C-SCAN. "
    "(2) UNIX I-node layout diagram and file size capacity calculations. "
    "(3) File allocation methods: Contiguous vs Linked vs Indexed. "
    "(4) Directory structures: Acyclic graph, cycles, links, and deletion issues. "
    "(5) Free space management: Bit map and Linked List trade-offs. "
    "Always state the formulas clearly before performing scheduling calculations."
)

# =============================================================================
#  FLASHCARDS & REVISION
# =============================================================================
pn.br()
pn.chap_box("Rapid Revision & Flashcards")

pn.revision_card(
    "Unit V Mastery Check",
    [
        "Draw a layout diagram of a UNIX I-node with direct and indirect pointers.",
        "Calculate the maximum file size supported by an I-node with 4 KB block size.",
        "Compare SCAN and C-SCAN scheduling in terms of fairness and seek distance.",
        "Explain how journaling protects filesystem integrity during power failures.",
        "Describe the purpose of sector sparing in bad block management.",
    ],
)

pn.flashcard(
    "What is <b>Sector Sparing</b>?",
    "A technique where the disk controller transparently redirects read/write requests "
    "from a damaged (bad) sector to a healthy spare sector on the disk.",
)
pn.flashcard(
    "What is the average <b>Rotational Latency</b>?",
    "The average time for the requested sector to rotate under the head, "
    "calculated as: 1 / (2 × Rotation Speed in RPS).",
)
pn.flashcard(
    "UNIX I-node pointer counts",
    "Contains 15 pointers: 12 direct pointers, 1 single indirect, "
    "1 double indirect, and 1 triple indirect pointer.",
)
pn.flashcard(
    "Difference: <b>LOOK</b> vs <b>SCAN</b>",
    "SCAN travels all the way to the boundary cylinder (0 or 199) regardless of requests, "
    "while LOOK reverses direction as soon as there are no further requests in that direction.",
)
pn.flashcard(
    "What is a Linux <b>Extent</b>?",
    "A contiguous range of physical blocks allocated to a file at once, represented "
    "as (start block, count), which reduces metadata size and fragmentation.",
)

# =============================================================================
#  BUILD DOCUMENT
# =============================================================================
pn.build_doc("OS_Unit5_Notes.pdf")

print("Generated: OS_Unit5_Notes.pdf")
