"""
Operating Systems (IT412) -- Unit I Notes
UIT-RGPV (Autonomous) Bhopal | Semester IV
Complete exam notes: OS Introduction, Types, Kernel, System Calls,
Process Concepts, Scheduling, Threads, and Multithreading Models.

Run:  python os_unit1_notes.py
Output: OS_Unit1_Notes.pdf
"""

from __future__ import annotations

import paperforge_notes as pn
import paperforge_diagrams as pd

# =============================================================================
#  THEME & GLOBAL SETUP
#  Using CATPPUCCIN_MOCHA -- warm mauve/lavender palette on deep dark bg
#  Distinct from Java units (OCEAN_DARK, MIDNIGHT_DARK, FOREST_DARK, SUNSET_DARK)
# =============================================================================
pn.set_story([])
my_theme = pn.CATPPUCCIN_MOCHA
my_theme.body_font = "Times-Roman"
my_theme.heading_font = "Courier-Bold"
pn.set_theme(my_theme)

pn.set_global_footer(
    left="Operating Systems (IT412) — Unit I",
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
    "Unit I — Introduction, Processes, Scheduling & Threads",
)
# pn.cover_subtitle(
#     [
#         "Subject Code: IT412  |  UIT-RGPV (Autonomous) Bhopal  |  Semester IV",
#         "Software Types, OS Functions & Services, Kernel, System Calls,",
#         "Process States, PCB, Schedulers, Context Switching, Threads & Multithreading",
#     ]
# )
pn.sp(10)
pn.rule(pn.get_theme().rl(pn.get_theme().accent), 1.5)
pn.sp(8)

pn.info_table(
    ["Section", "Syllabus Topics Covered"],
    [
        [
            "1.1  Software & Types",
            "System software, application software, utility programs",
        ],
        [
            "1.2  Introduction to OS",
            "Definition, goals, role of OS as resource manager & interface",
        ],
        [
            "1.3  OS Functions & Services",
            "Process, memory, file, I/O, security management",
        ],
        [
            "1.4  Types of OS",
            "Batch, multiprogramming, time-sharing, real-time, distributed, embedded",
        ],
        [
            "1.5  Kernel",
            "Kernel definition, monolithic vs microkernel vs hybrid, kernel space",
        ],
        ["1.6  System Calls", "Definition, types, how system calls work, examples"],
        [
            "1.7  Process Concept",
            "Definition, process vs program, process memory layout",
        ],
        [
            "1.8  Process States",
            "5-state model: New → Ready → Running → Waiting → Terminated",
        ],
        [
            "1.9  Process Control Block",
            "PCB fields: PID, state, PC, registers, memory, I/O, accounting",
        ],
        [
            "1.10 Schedulers",
            "Long-term, short-term, medium-term schedulers and their roles",
        ],
        ["1.11 Context Switching", "Definition, steps, overhead, dispatcher role"],
        ["1.12 Threads", "Thread definition, benefits, thread vs process"],
        [
            "1.13 Types of Threads",
            "User-level threads (ULT) vs Kernel-level threads (KLT)",
        ],
        [
            "1.14 Multithreading Models",
            "Many-to-One, One-to-One, Many-to-Many, Two-level",
        ],
        [
            "1.15 Exam Questions",
            "25+ previous-year style questions with detailed answers",
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
#  UNIT DIVIDER
# =============================================================================
pn.part_box("UNIT I — INTRODUCTION TO OPERATING SYSTEMS & PROCESSES")

# =============================================================================
#  1.1  SOFTWARE & TYPES
# =============================================================================
pn.chap_box("1.1  Software and Its Types")


pn.section("What is Software?")
pn.definition(
    "<b>Software:</b> A collection of programs, data, and instructions that tell "
    "a computer what to do. Software is the non-physical, logical component of a "
    "computer system, as opposed to hardware which is the physical component. "
    "Without software, hardware is merely an assembly of electronic components "
    "with no useful purpose."
)

pn.section("Classification of Software")
pn.info_table(
    ["Category", "Description", "Examples"],
    [
        [
            "System Software",
            "Programs that manage and control hardware resources, provide a platform "
            "for other software, and perform housekeeping tasks. Runs continuously "
            "or at system startup.",
            "Operating System (Windows, Linux, macOS), Device Drivers, Firmware, BIOS/UEFI",
        ],
        [
            "Application Software",
            "Programs written to perform specific tasks for end-users. Built on top "
            "of system software using OS APIs. Designed for human productivity.",
            "MS Word, Chrome Browser, VLC Media Player, Games, IDEs (Eclipse, VS Code)",
        ],
        [
            "Utility Software",
            "Specialized programs that help maintain, configure, analyze, or optimize "
            "the computer. Often bundled with the OS or installed separately.",
            "Antivirus (Avast), Disk Cleanup, File Compressor (WinRAR), Task Manager, Backup tools",
        ],
        [
            "Programming Software",
            "Tools that assist programmers in creating, debugging, and maintaining "
            "source code and programs.",
            "Compilers (GCC), Interpreters (Python), Assemblers, Debuggers (GDB), Linkers",
        ],
    ],
)

pn.exam(
    "Exam point: OS is system software that acts as an INTERFACE between the user and "
    "hardware, and as a RESOURCE MANAGER. Always distinguish between system software "
    "(manages hardware) and application software (serves users)."
)

# Layered stack showing software categories
stack_sw = pd.LayeredStack(
    width=pn.CW * 0.55,
    height=200,
    theme=diag_theme,
    caption="Fig 1.1: Software Hierarchy Layers",
)
stack_sw.layer(
    "Application Software", sublabel="User programs: browsers, editors, games"
)
stack_sw.layer(
    "Utility / Programming Tools", sublabel="Compilers, antivirus, debuggers"
)
stack_sw.layer("Operating System", sublabel="Kernel, shell, system services")
stack_sw.layer("Hardware", sublabel="CPU, RAM, Disk, I/O devices")
pn.story.extend(stack_sw.as_flowable())
pn.br()

# =============================================================================
#  1.2  INTRODUCTION TO OPERATING SYSTEM
# =============================================================================
pn.chap_box("1.2  Introduction to Operating Systems")


pn.section("Definition and Goals")
pn.definition(
    "<b>Operating System (OS):</b> A system software program (or set of programs) "
    "that manages computer hardware and software resources and provides a common "
    "set of services to application programs. The OS acts as: "
    "(1) <b>User Interface:</b> Provides a way for users to interact with hardware "
    "(CLI like bash, or GUI like Windows Explorer). "
    "(2) <b>Resource Manager:</b> Allocates and manages CPU, memory, disk, and I/O "
    "devices efficiently among competing processes. "
    "(3) <b>Extended Machine / Virtual Machine:</b> Hides hardware complexity and "
    "provides a clean, abstract, easy-to-use machine for programs and users."
)

pn.body(
    "The two primary goals of an OS are: "
    "<b>Convenience</b> — making the computer easier to use (high-level abstractions "
    "hide hardware details); and "
    "<b>Efficiency</b> — using hardware resources in an optimal way (maximize CPU "
    "utilization, minimize response time, maximize throughput)."
)

pn.section("OS as Resource Manager")
pn.info_table(
    ["Resource", "OS Management Role"],
    [
        [
            "CPU / Processor",
            "Schedules processes and threads; decides which process runs next and for how long.",
        ],
        [
            "Main Memory (RAM)",
            "Allocates and deallocates memory; protects process address spaces.",
        ],
        [
            "Secondary Storage",
            "Manages file systems; maps files to disk blocks; handles disk scheduling.",
        ],
        [
            "I/O Devices",
            "Provides uniform device driver interface; buffers and caches I/O operations.",
        ],
        [
            "Files",
            "Organizes data into named files; controls file creation, deletion, access permissions.",
        ],
        [
            "Networking",
            "Manages network stack; provides socket API for inter-process and network communication.",
        ],
        [
            "Security",
            "Authenticates users; enforces access control; protects against unauthorized access.",
        ],
    ],
)

# Network-style diagram showing OS in the center connecting everything
net_os = pd.NetworkDiagram(
    width=pn.CW,
    height=240,
    theme=diag_theme,
    caption="Fig 1.2: OS as the central manager between users/apps and hardware",
)
net_os.node("os", "Operating\nSystem", x=265, y=120, kind="server")
net_os.node("user", "User", x=60, y=120, kind="host")
net_os.node("apps", "Application\nPrograms", x=60, y=210, kind="generic")
net_os.node("cpu", "CPU", x=265, y=30, kind="generic")
net_os.node("mem", "Memory", x=420, y=60, kind="storage")
net_os.node("disk", "Disk / Files", x=420, y=180, kind="database")
net_os.node("io", "I/O Devices", x=265, y=210, kind="generic")
net_os.link("user", "os", label="commands")
net_os.link("apps", "os", label="system calls")
net_os.link("os", "cpu", label="schedules")
net_os.link("os", "mem", label="allocates")
net_os.link("os", "disk", label="manages")
net_os.link("os", "io", label="controls")
pn.story.extend(net_os.as_flowable())
pn.br()

# =============================================================================
#  1.3  OS FUNCTIONS & SERVICES
# =============================================================================
pn.chap_box("1.3  OS Functions and Services")


pn.section("Core OS Functions")
pn.bullet(
    [
        "<b>Process Management:</b> Creation, deletion, suspension, resumption of processes. Provides mechanisms for process synchronization and communication (IPC). Handles deadlocks.",
        "<b>Memory Management:</b> Allocating/deallocating memory to processes. Keeping track of which parts of memory are in use. Implementing virtual memory (swapping, paging).",
        "<b>File System Management:</b> Creating/deleting files and directories. Mapping file names to disk locations. File access permissions and protection.",
        "<b>I/O System Management:</b> Buffering, caching, and spooling I/O. Providing uniform driver interface hiding hardware details from user programs.",
        "<b>Secondary Storage Management:</b> Free space management, disk scheduling, disk partitioning and mounting.",
        "<b>Security and Protection:</b> User authentication (login), resource access control, protection of process address spaces from each other.",
        "<b>Networking:</b> Providing protocols and abstractions for inter-process communication over networks (TCP/IP stack, sockets).",
        "<b>Command Interpreter (Shell):</b> Reading and executing commands from users or batch files. The shell is the user-facing part of the OS.",
    ]
)

pn.section("OS Services (What the OS provides to programs)")
pn.info_table(
    ["Service", "Description"],
    [
        [
            "Program execution",
            "Load a program into memory and run it. Handle normal and abnormal termination.",
        ],
        [
            "I/O operations",
            "Programs cannot directly access hardware; OS mediates all I/O on behalf of programs.",
        ],
        [
            "File system manipulation",
            "Read, write, create, delete files; search directories; manage permissions.",
        ],
        [
            "Communication",
            "Inter-process communication (IPC) via shared memory or message passing.",
        ],
        [
            "Error detection",
            "Detect and handle hardware errors (memory parity, power failure) and software errors.",
        ],
        [
            "Resource allocation",
            "Allocate CPU cycles, memory, devices to multiple concurrently running processes.",
        ],
        [
            "Accounting",
            "Track resource usage per user/process for billing, optimization, or security audits.",
        ],
        [
            "Protection",
            "Ensure one process cannot interfere with another or with the OS itself.",
        ],
    ],
)
pn.br()

# =============================================================================
#  1.4  TYPES OF OPERATING SYSTEMS
# =============================================================================
pn.chap_box("1.4  Types of Operating Systems")


pn.section("Major OS Categories", keep_with_next=False)
pn.info_table(
    ["Type", "Description", "Key Feature", "Examples"],
    [
        [
            "Batch OS",
            "Jobs are collected into batches and processed one by one without user interaction. "
            "Output returned after job completes.",
            "No direct user-CPU interaction during execution. High throughput for similar jobs.",
            "IBM OS/360, early mainframe systems",
        ],
        [
            "Multiprogramming OS",
            "Multiple jobs loaded into memory simultaneously. When one job waits for I/O, "
            "CPU switches to another ready job.",
            "CPU is never idle as long as jobs are waiting. Maximizes CPU utilization.",
            "IBM OS/MFT, early Unix",
        ],
        [
            "Multitasking / Time-Sharing OS",
            "Extension of multiprogramming where CPU switches rapidly among processes giving "
            "illusion of simultaneity to multiple users.",
            "Response time minimized. Each user gets a time quantum (slice) of CPU.",
            "Unix, Linux, Windows NT/XP/10",
        ],
        [
            "Real-Time OS (RTOS)",
            "Guarantees response within strict time deadlines. Hard RTOS: missing deadline = "
            "catastrophic failure. Soft RTOS: degraded service.",
            "Deterministic timing guarantees. Used in safety-critical systems.",
            "VxWorks, FreeRTOS, QNX, RTLinux",
        ],
        [
            "Distributed OS",
            "Manages a group of networked computers and presents them as a single coherent "
            "system to users.",
            "Resource sharing across network. Transparent access to remote resources.",
            "Amoeba, Plan 9, Google's Borg",
        ],
        [
            "Network OS",
            "Provides services to computers on a network. Each machine has its own OS; "
            "NOS adds sharing features.",
            "File/printer sharing over network. Not transparent — users know resource locations.",
            "Novell NetWare, Windows Server",
        ],
        [
            "Embedded OS",
            "Designed for embedded systems (dedicated purpose devices). Highly constrained "
            "memory and power environment.",
            "Small footprint, fast boot, specific hardware support.",
            "Android (phones), iOS, Embedded Linux, TinyOS",
        ],
        [
            "Mobile OS",
            "Designed for mobile devices with touchscreen UI, battery management, GPS, sensors.",
            "Power-efficient, app sandboxing, OTA updates.",
            "Android, iOS, HarmonyOS",
        ],
    ],
)

pn.section("Batch vs Multiprogramming vs Time-Sharing — Key Comparison")
pn.info_table(
    ["Feature", "Batch OS", "Multiprogramming OS", "Time-Sharing OS"],
    [
        [
            "User Interaction",
            "None during job",
            "None / minimal",
            "Interactive (online)",
        ],
        ["CPU Utilization", "Low (idle during I/O)", "High", "High"],
        ["Response Time", "Hours / days", "Not optimized", "Seconds (low)"],
        ["Number of Users", "Single user", "Single / few", "Many concurrent users"],
        [
            "Main Goal",
            "Throughput",
            "CPU utilization",
            "Response time / user experience",
        ],
        ["Job Switching", "No (sequential)", "On I/O wait", "On time quantum expiry"],
    ],
)
pn.br()

# =============================================================================
#  1.5  KERNEL
# =============================================================================
pn.chap_box("1.5  The Kernel")


pn.section("What is the Kernel?")
pn.definition(
    "<b>Kernel:</b> The core component of an operating system that is always resident "
    "in main memory (RAM) and has complete control over everything in the system. "
    "The kernel is the first program loaded after the bootloader and runs in "
    "<b>privileged / supervisor mode</b> (also called kernel mode or ring 0 on x86). "
    "It directly interacts with hardware and manages the most critical resources: "
    "CPU scheduling, memory management, device drivers, and system calls. "
    "User programs run in <b>user mode</b> (ring 3) with restricted hardware access "
    "and must request kernel services through system calls."
)

pn.section("Kernel Mode vs User Mode")
pn.info_table(
    ["Aspect", "Kernel Mode", "User Mode"],
    [
        [
            "Privilege level",
            "Ring 0 (highest) — full hardware access",
            "Ring 3 (lowest) — restricted access",
        ],
        [
            "Memory access",
            "Can access all physical memory",
            "Only its own virtual address space",
        ],
        [
            "I/O instructions",
            "Can execute all I/O instructions directly",
            "Cannot execute I/O directly; must ask kernel",
        ],
        [
            "Interrupts",
            "Can enable/disable hardware interrupts",
            "Cannot touch interrupt flags",
        ],
        [
            "Error consequence",
            "Kernel panic / system crash",
            "Process segmentation fault / killed",
        ],
        [
            "Who runs here",
            "OS kernel, device drivers, interrupt handlers",
            "All user applications, shells, libraries",
        ],
    ],
)

pn.section("Types of Kernel Architecture")
pn.info_table(
    ["Architecture", "Design Philosophy", "Pros", "Cons", "Examples"],
    [
        [
            "Monolithic Kernel",
            "Entire OS (scheduler, memory manager, file system, drivers) runs as one large "
            "program in kernel space.",
            "Fast — no message passing between components. Well-tested in Linux.",
            "Large codebase. A bug in one driver can crash entire OS. Hard to maintain.",
            "Linux, traditional Unix, MS-DOS",
        ],
        [
            "Microkernel",
            "Only the most essential services run in kernel (IPC, basic scheduling, memory). "
            "Everything else (file system, drivers) runs in user space as servers.",
            "More reliable — server crash doesn't crash kernel. Easier to extend.",
            "Slower — message passing overhead between user-space servers.",
            "Mach, QNX, MINIX 3, L4",
        ],
        [
            "Hybrid Kernel",
            "Compromise: some services in kernel space for speed, others in user space for "
            "modularity. Combines features of both.",
            "Good performance + reasonable modularity.",
            "Complexity of both designs.",
            "Windows NT/10/11, macOS (XNU), Haiku",
        ],
        [
            "Exokernel",
            "Minimalist: kernel only does hardware multiplexing. All abstraction done in "
            "user-level libraries (libOS).",
            "Maximum application flexibility. High performance for specialized use.",
            "Complex to program; each application must manage resources.",
            "MIT Exokernel, Nemesis",
        ],
    ],
)

# Layered diagrams: Monolithic vs Microkernel side by side
from reportlab.platypus import Table, TableStyle

left_k = pd.LayeredStack(
    width=pn.CW * 0.46,
    height=200,
    theme=diag_theme,
    caption="Monolithic Kernel",
)
left_k.layer("User Applications")
left_k.divider()
left_k.layer("Kernel Space", sublabel="Scheduler + Memory + FS + Drivers (all here)")

right_k = pd.LayeredStack(
    width=pn.CW * 0.46,
    height=200,
    theme=diag_theme,
    caption="Microkernel",
)
right_k.layer("User Apps")
right_k.layer("File System Server  |  Driver Servers", sublabel="User space")
right_k.divider()
right_k.layer("Microkernel", sublabel="IPC + Basic Scheduling + Memory only")

left_k.as_flowable()
right_k.as_flowable()

tbl_k = Table(
    [
        [
            pd.ResponsiveDrawingFlowable(left_k.drawing),
            pd.ResponsiveDrawingFlowable(right_k.drawing),
        ]
    ],
    colWidths=[pn.CW * 0.48, pn.CW * 0.48],
)
pn.story.append(tbl_k)
pn.sp(6)
pn.br()

# =============================================================================
#  1.6  SYSTEM CALLS
# =============================================================================
pn.chap_box("1.6  System Calls")


pn.section("What is a System Call?")
pn.definition(
    "<b>System Call:</b> The programmatic interface through which a user-mode program "
    "requests a service from the operating system kernel. "
    "System calls are the ONLY mechanism for user programs to switch from user mode to "
    "kernel mode and access protected OS services (hardware, files, other processes). "
    "They form the boundary between user space and kernel space. "
    "In C on Linux, system calls are wrapped by the standard library (libc): "
    "for example, <code>printf()</code> eventually calls the <code>write()</code> system call."
)

pn.section("How a System Call Works — Step by Step")
pn.bullet(
    [
        "<b>Step 1 (Application):</b> The application calls a library function like <code>read()</code> in C.",
        "<b>Step 2 (Trap / Software Interrupt):</b> The library places the system call number and arguments into CPU registers, then executes a TRAP instruction (INT 0x80 on x86, SYSCALL on x86-64). This triggers a software interrupt.",
        "<b>Step 3 (Mode Switch):</b> The CPU automatically switches from user mode (ring 3) to kernel mode (ring 0). The hardware saves the current program counter and flags onto the kernel stack.",
        "<b>Step 4 (Dispatch):</b> The kernel's interrupt handler runs. It reads the system call number from the register and looks up the system call table to find the right kernel function.",
        "<b>Step 5 (Execution):</b> The kernel function executes, performing the requested service (reading file data, allocating memory, etc.).",
        "<b>Step 6 (Return):</b> The kernel places the return value (or error code) into the return register, then executes IRET (interrupt return). CPU switches back to user mode and resumes execution after the TRAP.",
    ]
)

seq_sc = pd.SequenceDiagram(
    width=650,
    height=280,
    theme=diag_theme,
    caption="Fig 1.3: System call sequence — user program to kernel and back",
)
seq_sc.actor("app", "User App\n(user mode)")
seq_sc.actor("lib", "C Library\n(libc)")
seq_sc.actor("hw", "CPU\nHardware")
seq_sc.actor("kern", "OS Kernel\n(kernel mode)")

seq_sc.message("app", "lib", "read(fd, buf, n)", arrow="solid")
seq_sc.activate("lib")
seq_sc.message("lib", "hw", "INT 0x80 / SYSCALL\n(syscall# in register)", arrow="solid")
seq_sc.activate("hw")
seq_sc.message(
    "hw",
    "kern",
    "mode switch → kernel mode\nPC saved, interrupt dispatched",
    arrow="solid",
)
seq_sc.activate("kern")
seq_sc.message(
    "kern", "kern", "look up syscall table\nexecute sys_read()", arrow="solid"
)
seq_sc.message(
    "kern", "hw", "result in register\nexecute IRET / SYSRET", arrow="dashed"
)
seq_sc.deactivate("kern")
seq_sc.message("hw", "lib", "mode switch → user mode\nresume execution", arrow="dashed")
seq_sc.deactivate("hw")
seq_sc.message("lib", "app", "return bytes read", arrow="dashed")
seq_sc.deactivate("lib")
pn.story.extend(seq_sc.as_flowable())

pn.section("Categories of System Calls")
pn.info_table(
    ["Category", "Purpose", "Examples (Linux / Windows)"],
    [
        [
            "Process Control",
            "Create, terminate, load, execute processes; wait for events.",
            "fork(), exec(), exit(), wait() / CreateProcess(), TerminateProcess()",
        ],
        [
            "File Manipulation",
            "Create, delete, open, close, read, write files.",
            "open(), read(), write(), close(), unlink() / CreateFile(), ReadFile()",
        ],
        [
            "Device Management",
            "Request/release devices, read/write devices.",
            "ioctl(), read(), write() on device files / DeviceIoControl()",
        ],
        [
            "Information Maintenance",
            "Get/set time, date, process attributes, system data.",
            "getpid(), alarm(), sleep() / GetSystemTime(), GetProcessId()",
        ],
        [
            "Communication",
            "Create connections, send/receive messages, shared memory.",
            "pipe(), socket(), send(), recv() / CreatePipe(), SendMessage()",
        ],
        [
            "Protection",
            "Get/set permissions, user identity, access rights.",
            "chmod(), chown(), getuid() / SetFileSecurity(), GetUserName()",
        ],
    ],
)

pn.subsection("Process Creation Example (C Language)")
pn.body(
    "Process control system calls can create complex execution trees. Below is a C code snippet illustrating how `fork()` duplicates the current process to create a child process."
)
pn.code_block(
    """#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    pid_t pid = fork(); // Create a new child process

    if (pid < 0) {
        fprintf(stderr, "Fork Failed\\n");
        return 1;
    } else if (pid == 0) {
        printf("I am the child process! My PID is %d.\\n", getpid());
        // Child executes a new program here (e.g. execvp)
    } else {
        printf("I am the parent process. Child PID is %d.\\n", pid);
        wait(NULL); // Wait for the child to finish
        printf("Child Complete.\\n");
    }
    return 0;
}""",
    lang="c",
)
pn.br()

# =============================================================================
#  1.7  PROCESS CONCEPT
# =============================================================================
pn.part_box("UNIT I — PROCESS MANAGEMENT")
pn.chap_box("1.7  Process Concept")


pn.section("What is a Process?")
pn.definition(
    "<b>Process:</b> A program in execution. A process is an active, dynamic entity — "
    "it is a program (passive, static code on disk) that has been loaded into memory "
    "and is being executed by the CPU. At any given time, a process includes: "
    "the program code (text section), current activity (program counter, CPU registers), "
    "process stack (function parameters, return addresses, local variables), "
    "data section (global variables), and heap (dynamically allocated memory)."
)

pn.section("Process vs Program — Key Distinction")
pn.info_table(
    ["Aspect", "Program", "Process"],
    [
        [
            "Nature",
            "Passive entity — stored on disk as a file",
            "Active entity — alive in memory, executing",
        ],
        [
            "Contents",
            "Code + static data on disk",
            "Code + data + stack + heap + PCB in memory",
        ],
        [
            "Existence",
            "Persistent (until file deleted)",
            "Temporary (created to run, then terminated)",
        ],
        [
            "Instances",
            "One program → multiple processes possible (e.g., 3 Chrome windows)",
            "Each instance is a separate process with its own memory",
        ],
        [
            "Created by",
            "Compiler/linker from source code",
            "OS loader when you run the program",
        ],
        ["Memory", "Not in RAM (until loaded)", "Occupies RAM while running"],
    ],
)

pn.section("Process Memory Layout")
pn.body(
    "When a process is loaded into memory, the OS allocates a virtual address space "
    "divided into distinct sections, each serving a specific purpose:"
)

stack_proc = pd.LayeredStack(
    width=pn.CW * 0.50,
    height=240,
    theme=diag_theme,
    caption="Fig 1.4: Process virtual memory layout (high → low address, top → bottom)",
)
stack_proc.layer(
    "Stack", sublabel="Local vars, function call frames, return addresses (grows ↓)"
)
stack_proc.layer("↑  ↓  (free gap)", sublabel="Stack grows down, heap grows up")
stack_proc.layer("Heap", sublabel="Dynamic memory: malloc/new (grows ↑)")
stack_proc.layer("Data (BSS + initialized)", sublabel="Global and static variables")
stack_proc.layer("Text (Code)", sublabel="Read-only compiled instructions")
pn.story.extend(stack_proc.as_flowable())
pn.br()

# =============================================================================
#  1.8  PROCESS STATES
# =============================================================================
pn.chap_box("1.8  Process States")


pn.section("The Five-State Process Model")
pn.definition(
    "<b>Process State:</b> The current activity or condition of a process at any point "
    "in time. As a process executes, it moves through a sequence of states. "
    "The OS tracks the state of every process and uses this information to make "
    "scheduling decisions. The classic 5-state model includes: "
    "New, Ready, Running, Waiting (Blocked), and Terminated."
)

pn.label("sec_context_switch")
pn.index_entry("Context Switch")
pn.index_entry("Process Control Block (PCB)")

pn.body(
    "A <b>context switch</b> occurs when the CPU switches from executing one process to another. "
    "To do this, the OS must save the current state of the running process (so it can be resumed later) "
    "and load the saved state of the new process."
)

pn.question("Why is a context switch considered 'pure overhead'?")
pn.answer(
    "During a context switch, the OS is doing work (saving/restoring registers, updating memory maps, flushing TLBs), but no useful user-level computation is being performed. Therefore, it is pure overhead. High context switch frequency degrades overall system throughput."
)

pn.subsection("The Process Control Block (PCB)")

pn.info_table(
    ["State", "Description", "What the OS does"],
    [
        [
            "New",
            "Process is being created. PCB allocated, resources requested, program loaded into memory.",
            "Initializes PCB, allocates memory, adds to process table.",
        ],
        [
            "Ready",
            "Process is in memory, all resources allocated, waiting only for CPU. Can run immediately if CPU is free.",
            "Keeps process in ready queue. Scheduler selects from here.",
        ],
        [
            "Running",
            "Process is currently being executed on the CPU. Only ONE process per CPU core can be running at once.",
            "CPU executes process instructions. Timer interrupt may preempt it.",
        ],
        [
            "Waiting / Blocked",
            "Process is waiting for some event (I/O completion, semaphore signal, child termination). Cannot use CPU even if free.",
            "Moves process to wait queue. Resumes to Ready when event occurs.",
        ],
        [
            "Terminated",
            "Process has finished execution (exited normally or killed). Resources being released.",
            "OS reclaims memory, closes files, removes PCB after parent calls wait().",
        ],
    ],
)

pn.section("State Transition Diagram")

sm_proc = pd.StateMachine(
    width=pn.CW,
    height=260,
    theme=diag_theme,
    caption="Fig 1.5: Five-state process model — state transitions",
)
sm_proc.state("new", "New", x=80, y=160, initial=True)
sm_proc.state("ready", "Ready", x=220, y=160)
sm_proc.state("running", "Running", x=370, y=160)
sm_proc.state("waiting", "Waiting\n(Blocked)", x=295, y=50)
sm_proc.state("term", "Terminated", x=500, y=160, accepting=True)

sm_proc.transition("new", "ready", label="admitted\n(long-term scheduler)", pill=True)
sm_proc.transition(
    "ready", "running", label="dispatch\n(short-term scheduler)", offset=15.0, pill=True
)
sm_proc.transition(
    "running",
    "ready",
    label="interrupt /\ntime quantum expired",
    offset=15.0,
    pill=True,
)
sm_proc.transition("running", "waiting", label="I/O or\nevent wait", pill=True)
sm_proc.transition(
    "waiting", "ready", label="I/O complete /\nevent occurred", pill=True
)
sm_proc.transition("running", "term", label="exit()", pill=True)
pn.story.extend(sm_proc.as_flowable())

pn.section("State Transition Summary")
pn.info_table(
    ["Transition", "Cause"],
    [
        [
            "New → Ready",
            "Process creation complete (admitted by long-term scheduler). Resources allocated.",
        ],
        [
            "Ready → Running",
            "CPU dispatcher (short-term scheduler) selects this process from ready queue.",
        ],
        [
            "Running → Ready",
            "Timer interrupt fires (preemption). Higher-priority process arrives. Voluntary yield.",
        ],
        [
            "Running → Waiting",
            "Process requests I/O, waits for semaphore/mutex, or calls sleep()/wait().",
        ],
        [
            "Waiting → Ready",
            "I/O operation completes, interrupt arrives, or semaphore is signaled.",
        ],
        [
            "Running → Terminated",
            "Process calls exit(). Fatal error or signal (kill). Parent terminates child.",
        ],
    ],
)
pn.br()

# =============================================================================
#  1.9  PROCESS CONTROL BLOCK (PCB)
# =============================================================================
pn.chap_box("1.9  Process Control Block (PCB)")


pn.section("What is a PCB?")
pn.definition(
    "<b>Process Control Block (PCB):</b> Also called Task Control Block (TCB). "
    "A data structure maintained by the OS kernel for every process in the system. "
    "The PCB is the complete representation of a process — it stores all information "
    "needed to manage the process and to save/restore its state when context switching. "
    "When a process is created, the OS allocates a PCB; when terminated, the PCB is freed. "
    "The PCB is stored in kernel memory and is protected from user programs."
)

pn.section("PCB Fields (Contents)")
pn.info_table(
    ["PCB Field", "Contents", "Purpose"],
    [
        [
            "Process ID (PID)",
            "Unique integer identifier (e.g., PID=1234)",
            "Identifies the process uniquely in the system.",
        ],
        [
            "Process State",
            "New / Ready / Running / Waiting / Terminated",
            "OS scheduler uses state to manage process.",
        ],
        [
            "Program Counter (PC)",
            "Address of the NEXT instruction to execute",
            "Saved on context switch; restored on resume.",
        ],
        [
            "CPU Registers",
            "Accumulator, index registers, stack pointer, general-purpose registers — all register values",
            "Complete CPU state must be saved on switch.",
        ],
        [
            "CPU Scheduling Info",
            "Priority, scheduling queue pointers, time quantum remaining",
            "Needed by scheduler to make CPU allocation decisions.",
        ],
        [
            "Memory Management Info",
            "Page table base, segment table, memory limits, base/limit registers",
            "Maps process virtual addresses to physical memory.",
        ],
        [
            "Accounting Info",
            "CPU time used, real time elapsed, process start time, job limits",
            "Used for billing, quota enforcement, and profiling.",
        ],
        [
            "I/O Status Info",
            "List of open files, file descriptors, list of allocated I/O devices",
            "Track which devices/files the process is using.",
        ],
        [
            "Parent PID (PPID)",
            "PID of the process that created this process",
            "Supports process hierarchy (parent-child relationship).",
        ],
        [
            "List of Open Files",
            "File descriptor table — each entry points to a file table entry",
            "OS manages file sharing and reference counting.",
        ],
    ],
)

# Flowchart showing context switch using PCB
fc_pcb = pd.Flowchart(
    width=pn.CW,
    height=340,
    theme=diag_theme,
    caption="Fig 1.6: Context switch — PCB save and restore cycle",
)
fc_pcb.terminal("start", "Process P1 Running on CPU")
fc_pcb.process("interrupt", "Interrupt or System Call Occurs")
fc_pcb.process("save_p1", "Save P1 state → PCB1\n(PC, registers, stack pointer)")
fc_pcb.process("select", "Short-term Scheduler: select P2 from Ready Queue")
fc_pcb.process("restore_p2", "Restore P2 state ← PCB2\n(PC, registers, stack pointer)")
fc_pcb.terminal("p2run", "Process P2 Running on CPU")
fc_pcb.edge("start", "interrupt")
fc_pcb.edge("interrupt", "save_p1")
fc_pcb.edge("save_p1", "select")
fc_pcb.edge("select", "restore_p2")
fc_pcb.edge("restore_p2", "p2run")
pn.story.extend(fc_pcb.as_flowable())
pn.br()

pn.subsection("Context Switch CPU Timing Diagram")
pn.body(
    "The diagram below illustrates CPU burst time-slicing and the OS kernel intervening to perform context switches."
)
td_cs = pd.TimingDiagram(
    width=pn.CW,
    height=180,
    caption="Fig 1.6b: CPU execution timing during context switch",
    theme=diag_theme,
)
td_cs.signal("P1 Executing", transitions=[(0, 1), (40, 0), (160, 0)])
td_cs.signal(
    "OS Kernel (Switch)", transitions=[(0, 0), (40, 1), (70, 0), (130, 1), (160, 0)]
)
td_cs.signal("P2 Executing", transitions=[(0, 0), (70, 1), (130, 0)])
pn.story.extend(td_cs.as_flowable())
pn.br()

# =============================================================================
#  1.10  TYPES OF SCHEDULERS
# =============================================================================
pn.chap_box("1.10  Types of Schedulers")


pn.section("The Three Schedulers")
pn.definition(
    "<b>Scheduler:</b> A component of the OS that selects which process should be "
    "given access to a resource (usually the CPU) at any given time. "
    "There are three main types of schedulers, each operating at a different "
    "time scale and controlling a different transition in the process state model."
)

pn.info_table(
    ["Scheduler", "Also Called", "Role", "Frequency", "Controls Transition"],
    [
        [
            "Long-term Scheduler",
            "Job Scheduler / Admission Scheduler",
            "Decides which processes from the job pool (on disk) are admitted to the ready queue in memory. Controls the DEGREE OF MULTIPROGRAMMING (how many processes are in memory).",
            "Infrequent — runs when a new process finishes or new batch jobs arrive (seconds to minutes).",
            "New → Ready (admitted to memory)",
        ],
        [
            "Short-term Scheduler",
            "CPU Scheduler / Dispatcher",
            "Decides which process from the ready queue gets the CPU next. Must be very fast since it runs frequently. Implements the CPU scheduling algorithm (FCFS, SJF, RR, Priority).",
            "Very frequent — runs every few milliseconds (after every timer interrupt, system call, or I/O completion).",
            "Ready → Running",
        ],
        [
            "Medium-term Scheduler",
            "Swapper",
            "Temporarily removes (swaps out) a process from memory to disk to free RAM, and later swaps it back in. Used to reduce degree of multiprogramming temporarily.",
            "Occasional — when memory is overloaded or system is thrashing.",
            "Running/Waiting → Swapped; Swapped → Ready",
        ],
    ],
)

pn.section("Scheduler Interaction Diagram")
net_sched = pd.NetworkDiagram(
    width=650,
    height=250,
    theme=diag_theme,
    caption="Fig 1.7: Three schedulers and their positions in the process lifecycle",
)
net_sched.node("pool", "Job Pool\n(Disk)", x=50, y=100, kind="database")
net_sched.node("lts", "Long-term\nScheduler", x=160, y=100, kind="generic")
net_sched.node("rq", "Ready\nQueue", x=270, y=100, kind="storage")
net_sched.node("sts", "Short-term\nScheduler", x=375, y=100, kind="generic")
net_sched.node("cpu", "CPU", x=480, y=100, kind="server")
net_sched.node("mts", "Medium-term\nScheduler\n(Swapper)", x=270, y=175, kind="generic")

net_sched.link("pool", "lts", label="")
net_sched.link("lts", "rq", label="admit")
net_sched.link("rq", "sts", label="")
net_sched.link("sts", "cpu", label="dispatch")
net_sched.link("mts", "rq", label="swap in")
pn.story.extend(net_sched.as_flowable())
pn.body(
    f"Note: To see how these schedulers interact during a Context Switch, refer back to Page {pn.ref('sec_context_switch')}."
)

pn.exam(
    "Exam point: Long-term scheduler controls DEGREE OF MULTIPROGRAMMING. "
    "Short-term scheduler must be VERY FAST (< 10ms) because it runs every 100ms — "
    "1/10 of CPU time wasted if it takes 10ms. "
    "Medium-term scheduler performs SWAPPING to manage memory pressure."
)
pn.br()

# =============================================================================
#  1.11  CONTEXT SWITCHING
# =============================================================================
pn.chap_box("1.11  Context Switching")


pn.section("What is Context Switching?")
pn.definition(
    "<b>Context Switch:</b> The process of saving the state (context) of a currently "
    "running process into its PCB and loading the saved state of another process "
    "from its PCB so that the CPU can execute the new process. "
    "During a context switch, the CPU is doing NO USEFUL WORK — it is pure overhead. "
    "Context switch time is typically 1–100 microseconds depending on hardware support "
    "(some CPUs have hardware support for fast context saves). "
    "The <b>dispatcher</b> module of the short-term scheduler performs the actual context switch."
)

pn.section("Steps in a Context Switch")
pn.bullet(
    [
        "<b>1. Trigger:</b> An interrupt occurs (timer, I/O completion), or the running process makes a system call or voluntarily yields the CPU.",
        "<b>2. Save Context of Current Process (P1):</b> CPU registers (PC, SP, general-purpose), flags, memory management registers saved into P1's PCB. P1 state changed to Ready (if preempted) or Waiting (if blocking).",
        "<b>3. Update OS Data Structures:</b> Move P1 to appropriate queue (ready or wait). Update scheduling statistics (time used, priority).",
        "<b>4. Select New Process (P2):</b> Short-term scheduler selects P2 from ready queue using scheduling algorithm.",
        "<b>5. Restore Context of New Process (P2):</b> Load P2's saved CPU registers, PC, stack pointer, and memory registers from P2's PCB.",
        "<b>6. Update Memory Maps:</b> Switch page tables / TLB flush (if P2 is a different process — expensive!).",
        "<b>7. Resume Execution:</b> CPU starts executing P2 from where it left off.",
    ]
)

pn.section("Context Switch Overhead")
pn.info_table(
    ["Factor", "Impact"],
    [
        [
            "Register save/restore",
            "Fast — typically just copying register values to/from PCB memory.",
        ],
        [
            "Cache invalidation",
            "When switching to a different process, CPU caches contain P1's data — useless for P2. Cache 'cold start' is expensive.",
        ],
        [
            "TLB flush",
            "Translation Lookaside Buffer must be flushed when switching address spaces (different processes). Very costly.",
        ],
        [
            "Hardware context support",
            "Modern CPUs (x86 TSS, ARM context registers) reduce switch cost. ASID (Address Space IDs) avoid full TLB flushes.",
        ],
        [
            "Thread switch vs Process switch",
            "Thread switch within same process is cheaper — shares address space, no TLB flush needed.",
        ],
    ],
)
pn.br()

# =============================================================================
#  1.12  THREADS
# =============================================================================
pn.part_box("UNIT I — THREADS AND MULTITHREADING")
pn.br()
pn.chap_box("1.12  Threads")


pn.section("What is a Thread?")
pn.definition(
    "<b>Thread:</b> The smallest unit of CPU utilization. Also called a lightweight process (LWP). "
    "A thread is a sequential flow of execution within a process. "
    "A single process can have multiple threads, all sharing the same process resources "
    "(code, data, heap, open files, signals) but each having its own "
    "thread ID, program counter, register set, and private stack. "
    "Threads within the same process can communicate directly through shared memory "
    "without OS overhead, making them much more efficient than separate processes."
)

pn.section("Thread vs Process — Detailed Comparison", keep_with_next=False)
pn.info_table(
    ["Aspect", "Process", "Thread"],
    [
        [
            "Definition",
            "Program in execution — independent entity with full address space",
            "Unit of execution within a process — shares process address space",
        ],
        [
            "Memory",
            "Own code, data, heap, stack — fully isolated from other processes",
            "Own stack only; shares code, data, heap with sibling threads",
        ],
        [
            "Creation overhead",
            "High — OS must allocate new address space, copy/fork resources",
            "Low — only a new stack and thread control block needed",
        ],
        [
            "Communication",
            "Must use IPC (pipes, sockets, shared memory) — complex and slow",
            "Direct shared memory — fast, but requires synchronization",
        ],
        [
            "Context switch",
            "Expensive — must flush TLB, switch page tables",
            "Cheap — stays in same address space, no TLB flush",
        ],
        [
            "Isolation",
            "High — process crash does not affect others",
            "Low — one thread crashing with SIGSEGV kills entire process",
        ],
        [
            "Parallelism",
            "Can run on multiple cores (independent address spaces)",
            "Can run on multiple cores within one process",
        ],
        [
            "Example",
            "Separate Chrome browser windows (different processes)",
            "Browser tabs within one Chrome window (different threads)",
        ],
    ],
)

pn.section("Benefits of Multithreading")
pn.bullet(
    [
        "<b>Responsiveness:</b> One thread handles user input while another does background computation. UI stays responsive even during long operations (e.g., web browser rendering while downloading).",
        "<b>Resource Sharing:</b> Threads share the code and data of the process by default. No need for expensive IPC mechanisms — threads can communicate via shared variables.",
        "<b>Economy:</b> Thread creation and context switching are much faster (and use less memory) than process creation and switching. Solaris: process creation = 30× more expensive than thread creation.",
        "<b>Scalability / Parallelism:</b> On multi-core CPUs, different threads of the same process can execute truly in parallel on different cores, improving throughput.",
        "<b>Server Performance:</b> Multi-threaded servers handle multiple client requests concurrently. Each incoming connection gets its own thread — far more efficient than launching a new process per connection.",
    ]
)

# Diagram: single-threaded vs multi-threaded process
from reportlab.platypus import Table

left_t = pd.LayeredStack(
    width=pn.CW * 0.46,
    height=180,
    theme=diag_theme,
    caption="Single-threaded Process",
)
left_t.layer("Thread (one)", sublabel="Own stack + registers")
left_t.divider()
left_t.layer("Shared: Code + Data + Files + Heap")

right_t = pd.LayeredStack(
    width=pn.CW * 0.46,
    height=180,
    theme=diag_theme,
    caption="Multi-threaded Process",
)
right_t.layer(
    "Thread 1  |  Thread 2  |  Thread 3", sublabel="Each: own stack + registers"
)
right_t.divider()
right_t.layer("Shared: Code + Data + Files + Heap")

left_t.as_flowable()
right_t.as_flowable()

tbl_t = Table(
    [
        [
            pd.ResponsiveDrawingFlowable(left_t.drawing),
            pd.ResponsiveDrawingFlowable(right_t.drawing),
        ]
    ],
    colWidths=[pn.CW * 0.48, pn.CW * 0.48],
)
pn.story.append(tbl_t)
pn.sp(6)
pn.br()

pn.section("Amdahl's Law (Theoretical Speedup)")
pn.definition(
    "Amdahl's Law defines the maximum theoretical speedup of a program using multiple processors in parallel computing."
)
pn.formula_block(r"S(N) = \frac{1}{(1 - P) + \frac{P}{N}}")
pn.bullet(
    [
        "<b>S(N)</b>: Maximum speedup achieved with N threads/processors.",
        "<b>P</b>: Proportion of the program that can be made parallel (0 to 1).",
        "<b>1 - P</b>: The strictly serial portion that cannot be parallelized.",
        "<b>N</b>: Number of processor cores / threads.",
    ]
)
pn.exam(
    "Even with infinite processors (N → ∞), speedup is limited by the serial fraction: 1 / (1 - P)."
)
pn.br()

# =============================================================================
#  1.13  TYPES OF THREADS
# =============================================================================
pn.chap_box("1.13  Types of Threads")


pn.section("User-Level Threads (ULT)")
pn.definition(
    "<b>User-Level Threads (ULT):</b> Threads managed entirely in user space by a "
    "thread library (e.g., POSIX pthreads in user mode, Java green threads, GNU Pth). "
    "The kernel has NO knowledge of these threads — from the kernel's perspective, "
    "the entire process looks like a single-threaded process. "
    "Thread creation, scheduling, and context switching is done by the user-level "
    "thread library without any system calls or kernel involvement."
)

pn.info_table(
    ["Aspect", "User-Level Threads (ULT)"],
    [
        ["Managed by", "User-space thread library (no kernel involvement)"],
        [
            "Kernel awareness",
            "Kernel sees only one process — unaware of individual threads",
        ],
        ["Creation speed", "Very fast — no system call, no mode switch"],
        ["Portability", "Portable — works on any OS that supports processes"],
        [
            "Blocking I/O problem",
            "MAJOR DRAWBACK: if one thread makes a blocking system call (read/write), the ENTIRE PROCESS blocks — no other thread can run",
        ],
        [
            "Multi-core parallelism",
            "Cannot exploit multiple CPU cores — kernel only sees one thread and assigns it to one core",
        ],
        [
            "Examples",
            "POSIX Pthreads (in user mode), Java green threads (old), GNU Pth library",
        ],
    ],
)

pn.section("Kernel-Level Threads (KLT)")
pn.definition(
    "<b>Kernel-Level Threads (KLT):</b> Threads managed directly by the OS kernel. "
    "The kernel maintains a thread control block (TCB) for each thread and performs "
    "all thread operations (creation, scheduling, context switching) via system calls. "
    "Each kernel thread can be independently scheduled on any CPU core. "
    "This is the model used by modern OSes: Windows, Linux (pthreads via NPTL), macOS."
)

pn.info_table(
    ["Aspect", "Kernel-Level Threads (KLT)"],
    [
        ["Managed by", "OS kernel directly — kernel has a TCB for each thread"],
        ["Kernel awareness", "Kernel knows all threads; schedules them independently"],
        [
            "Creation speed",
            "Slower than ULT — requires system call for creation/switch",
        ],
        [
            "Blocking I/O",
            "NO PROBLEM: if one thread blocks, kernel schedules another thread of same process",
        ],
        [
            "Multi-core parallelism",
            "Full support — kernel assigns different threads to different CPU cores simultaneously",
        ],
        ["Overhead", "Higher overhead per thread — each needs kernel data structures"],
        ["Examples", "Linux NPTL (pthreads), Windows threads, Solaris LWP"],
    ],
)

pn.section("ULT vs KLT — Direct Comparison")
pn.info_table(
    ["Feature", "User-Level Threads (ULT)", "Kernel-Level Threads (KLT)"],
    [
        ["Management", "Thread library in user space", "OS kernel"],
        ["Speed", "Faster (no system calls)", "Slower (system calls needed)"],
        ["Portability", "High", "OS-specific"],
        [
            "Blocking system calls",
            "Entire process blocks (MAJOR problem)",
            "Only that thread blocks",
        ],
        [
            "Multi-core support",
            "No (kernel sees one process)",
            "Yes (kernel schedules on any core)",
        ],
        [
            "Crash isolation",
            "One thread crash kills process",
            "One thread crash kills process",
        ],
        ["Use today", "Rare (mostly replaced by KLT)", "Standard on all modern OSes"],
    ],
)
pn.br()

# =============================================================================
#  1.14  MULTITHREADING MODELS
# =============================================================================
pn.chap_box("1.14  Multithreading Models")


pn.section("Overview")
pn.definition(
    "<b>Multithreading Model:</b> The relationship between User-Level Threads (ULT) "
    "and Kernel-Level Threads (KLT) in a given OS implementation. "
    "Since the kernel only schedules kernel threads, user threads must be mapped "
    "to kernel threads to actually run on the CPU. "
    "The mapping strategy defines the multithreading model. "
    "There are four main models: Many-to-One, One-to-One, Many-to-Many, and Two-level."
)

pn.section("Model 1: Many-to-One (M:1)")
pn.info_table(
    ["Aspect", "Details"],
    [
        ["Mapping", "Many user threads → ONE kernel thread"],
        [
            "Thread management",
            "All done by user-level library; kernel sees only one thread",
        ],
        [
            "Blocking problem",
            "One blocking system call blocks ALL user threads (entire process)",
        ],
        ["Multi-core", "Cannot run in parallel on multiple cores — only 1 KLT"],
        ["Advantage", "Very fast thread operations; highly portable"],
        ["Disadvantage", "No parallelism; blocking system calls stop all threads"],
        ["Example", "Solaris Green Threads, GNU Pth (early systems)"],
    ],
)

pn.section("Model 2: One-to-One (1:1)")
pn.info_table(
    ["Aspect", "Details"],
    [
        ["Mapping", "Each user thread → ONE dedicated kernel thread"],
        [
            "Thread management",
            "Kernel manages all threads; each ULT creation creates a KLT",
        ],
        ["Blocking problem", "No problem — other threads continue when one blocks"],
        ["Multi-core", "Full parallelism — different KLTs on different CPU cores"],
        ["Advantage", "True parallelism; no blocking problem; straightforward model"],
        [
            "Disadvantage",
            "Creating many threads is expensive (each needs kernel resources). OS may limit max threads.",
        ],
        [
            "Example",
            "Linux (NPTL/pthreads), Windows NT/XP/10/11 — THE STANDARD MODEL TODAY",
        ],
    ],
)

pn.section("Model 3: Many-to-Many (M:N)")
pn.info_table(
    ["Aspect", "Details"],
    [
        [
            "Mapping",
            "Many user threads → a POOL of kernel threads (M ULT → N KLT, M ≥ N)",
        ],
        [
            "Thread management",
            "User library and kernel cooperate; kernel allocates a pool of KLTs",
        ],
        [
            "Blocking problem",
            "Solved — scheduler activations notify user library when a thread blocks, allowing another ULT to be mapped to a free KLT",
        ],
        ["Multi-core", "Yes — multiple KLTs run on multiple cores"],
        [
            "Advantage",
            "Best of both worlds: fast creation, no blocking problem, parallelism",
        ],
        ["Disadvantage", "Complex implementation; hard to tune M and N correctly"],
        ["Example", "Solaris < 9, IRIX, old HP-UX, Windows with fiber package"],
    ],
)

pn.section("Model 4: Two-Level Model")
pn.definition(
    "<b>Two-Level Model:</b> A variation of the Many-to-Many model that also allows "
    "a user thread to be BOUND to a specific kernel thread (like One-to-One). "
    "This gives maximum flexibility: most threads use the M:N pool for efficiency, "
    "but critical real-time threads can be pinned to a dedicated kernel thread for "
    "guaranteed scheduling. Used in Solaris 9+, IRIX, and some HP-UX versions."
)

pn.section("Multithreading Models — Master Comparison Table")
pn.info_table(
    ["Feature", "Many-to-One", "One-to-One", "Many-to-Many", "Two-Level"],
    [
        ["ULT : KLT ratio", "M : 1", "1 : 1", "M : N (M≥N)", "M : N + bound"],
        ["Blocking problem", "YES — all block", "No", "No (activation)", "No"],
        ["Multi-core parallelism", "NO", "YES", "YES", "YES"],
        ["Creation cost", "Very low", "High", "Medium", "Medium"],
        ["Complexity", "Simple", "Simple", "Complex", "Most complex"],
        ["Max scalability", "Poor", "Limited by KLT limit", "High", "High"],
        [
            "Used in",
            "Old Solaris, GNU Pth",
            "Linux, Windows (today)",
            "Old Solaris, IRIX",
            "Solaris 9+",
        ],
    ],
)

# State machine showing thread lifecycle
sm_thread = pd.StateMachine(
    width=pn.CW,
    height=260,
    theme=diag_theme,
    caption="Fig 1.8: Thread lifecycle (mirrors process state model)",
)
sm_thread.state("born", "Born\n(Created)", x=70, y=160, initial=True)
sm_thread.state("ready", "Ready", x=200, y=160)
sm_thread.state("running", "Running", x=340, y=160)
sm_thread.state("blocked", "Blocked\n(Waiting)", x=270, y=50)
sm_thread.state("dead", "Dead\n(Terminated)", x=480, y=160, accepting=True)

sm_thread.transition("born", "ready", label="start()", pill=True)
sm_thread.transition("ready", "running", label="dispatch", offset=15.0, pill=True)
sm_thread.transition(
    "running", "ready", label="preempt /\nyield", offset=15.0, pill=True
)
sm_thread.transition("running", "blocked", label="I/O /\nwait /\nsleep", pill=True)
sm_thread.transition("blocked", "ready", label="notify /\nI/O done", pill=True)
sm_thread.transition("running", "dead", label="run()\ncompletes", pill=True)
pn.story.extend(sm_thread.as_flowable())
pn.br()

# =============================================================================
#  1.15  EXAM QUESTIONS & ANSWERS
# =============================================================================
pn.part_box("UNIT I — EXAM QUESTIONS & DETAILED ANSWERS")
pn.chap_box("1.15  Previous-Year Style Exam Questions")


pn.section("2-Mark Questions (Short Answer)")

pn.highlight(
    "<b>Q1. What is an Operating System? State its two main goals.</b><br/>"
    "A: An OS is system software that manages computer hardware and software resources "
    "and provides common services to programs. It acts as an interface between user/programs "
    "and hardware. Two goals: (1) <b>Convenience</b> — hides hardware complexity, easy to use; "
    "(2) <b>Efficiency</b> — maximizes resource utilization (CPU, memory, I/O)."
)

pn.highlight(
    "<b>Q2. Differentiate between system software and application software.</b><br/>"
    "A: System software manages hardware and provides a platform for other software "
    "(e.g., OS, device drivers). It runs continuously or at startup. "
    "Application software performs specific user tasks and runs on top of system software "
    "(e.g., MS Word, Chrome, games). System software is closer to hardware; "
    "application software is closer to the user."
)

pn.highlight(
    "<b>Q3. What is a kernel? What is kernel mode?</b><br/>"
    "A: Kernel is the core of the OS that is always in memory with full hardware access. "
    "It manages CPU scheduling, memory, I/O, and device drivers. "
    "Kernel mode (privileged mode / ring 0) is the CPU execution mode in which the kernel runs, "
    "allowing unrestricted access to all hardware instructions and memory. "
    "User programs run in user mode (ring 3) with restricted access."
)

pn.highlight(
    "<b>Q4. What is a system call? Give four categories with examples.</b><br/>"
    "A: A system call is the interface through which user programs request OS kernel services. "
    "They cause a mode switch from user mode to kernel mode. "
    "Categories: (1) Process control — fork(), exec(), exit(). "
    "(2) File manipulation — open(), read(), write(), close(). "
    "(3) Device management — ioctl(), read(). "
    "(4) Information maintenance — getpid(), time(). "
    "(5) Communication — pipe(), socket(), send(), recv()."
)

pn.highlight(
    "<b>Q5. What is a process? How is it different from a program?</b><br/>"
    "A: A process is a program in execution — an active entity in memory with code, data, "
    "stack, heap, and a PCB. A program is a passive entity — code stored on disk. "
    "One program can create multiple processes (e.g., multiple Chrome windows). "
    "A process includes: text section (code), data section (globals), stack (locals), "
    "heap (dynamic memory), and current activity (PC, registers)."
)

pn.highlight(
    "<b>Q6. List and briefly explain the five states of a process.</b><br/>"
    "A: (1) <b>New:</b> Process being created, PCB allocated. "
    "(2) <b>Ready:</b> In memory, waiting for CPU; ready queue. "
    "(3) <b>Running:</b> Currently executing on CPU; only one per core. "
    "(4) <b>Waiting/Blocked:</b> Waiting for I/O or event; CPU-free. "
    "(5) <b>Terminated:</b> Finished execution; resources being freed."
)

pn.highlight(
    "<b>Q7. What is a PCB? List its important fields.</b><br/>"
    "A: Process Control Block is a kernel data structure that stores all information "
    "about a process. Key fields: Process ID (PID), Process State, Program Counter, "
    "CPU Registers, Scheduling Priority, Memory Management info (page table base), "
    "I/O Status (open files, devices), Accounting info (CPU time used), Parent PID. "
    "The PCB is the 'identity card' of a process."
)

pn.highlight(
    "<b>Q8. Differentiate between short-term, long-term, and medium-term schedulers.</b><br/>"
    "A: Long-term (job) scheduler: controls which jobs enter memory — infrequent, "
    "controls degree of multiprogramming. "
    "Short-term (CPU) scheduler: selects which ready process runs next — very frequent "
    "(every 100ms), implements scheduling algorithm. "
    "Medium-term (swapper): swaps processes in/out of memory to manage memory pressure — "
    "occasional."
)

pn.highlight(
    "<b>Q9. What is context switching? What is its overhead?</b><br/>"
    "A: Context switching is saving the state of the current process (into its PCB) and "
    "loading the state of the next process (from its PCB). Steps: interrupt occurs → "
    "save P1 registers/PC → select P2 → restore P2 registers/PC → resume P2. "
    "Overhead: pure wasted time (no useful work). Caused by: register save/restore, "
    "cache invalidation, TLB flush when switching address spaces."
)

pn.highlight(
    "<b>Q10. What is a thread? List four benefits of multithreading.</b><br/>"
    "A: A thread is the smallest unit of CPU execution within a process. "
    "Multiple threads share process resources (code, data, heap, files) but each has "
    "its own stack, PC, and registers. "
    "Benefits: (1) Responsiveness — UI stays live during background work. "
    "(2) Resource sharing — threads share memory directly (no IPC needed). "
    "(3) Economy — cheaper to create/switch than processes. "
    "(4) Scalability — true parallelism on multi-core CPUs."
)

pn.section("5-Mark Questions (Explain with Diagrams)")

pn.highlight(
    "<b>Q11. Explain the different types of operating systems with examples.</b><br/>"
    "A: <b>Batch OS:</b> Jobs collected and processed without interaction (IBM OS/360). "
    "<b>Multiprogramming OS:</b> Multiple jobs in memory; CPU switches on I/O wait (early Unix). "
    "<b>Time-sharing OS:</b> Multiple users share CPU via time quanta; fast response (Linux, Windows). "
    "<b>Real-time OS:</b> Guarantees deadlines; Hard RTOS for safety-critical systems (VxWorks). "
    "<b>Distributed OS:</b> Multiple networked computers as one system (Amoeba, Plan 9). "
    "<b>Embedded OS:</b> For dedicated devices; small footprint (Android, FreeRTOS). "
    "Time-sharing extends multiprogramming by adding rapid CPU switching to serve interactive users."
)

pn.highlight(
    "<b>Q12. Draw and explain the process state transition diagram. What triggers each transition?</b><br/>"
    "A: Five states: New, Ready, Running, Waiting, Terminated. "
    "New→Ready: process admitted (long-term scheduler). "
    "Ready→Running: CPU dispatcher selects process. "
    "Running→Ready: timer interrupt/preemption or voluntary yield. "
    "Running→Waiting: I/O request, semaphore wait, sleep(). "
    "Waiting→Ready: I/O completion, event/signal occurs. "
    "Running→Terminated: exit() call, kill signal, or fatal error. "
    "See Fig 1.5 for the complete state diagram."
)

pn.highlight(
    "<b>Q13. What is a PCB? Explain its role in context switching with a diagram.</b><br/>"
    "A: PCB stores complete process state. During context switch: "
    "1. OS saves running process P1's registers, PC, and memory info → P1's PCB. "
    "2. Scheduler selects process P2 from ready queue. "
    "3. OS restores P2's registers, PC, memory maps from P2's PCB. "
    "4. CPU resumes execution of P2 from where it stopped. "
    "Without PCB, context switching is impossible — the OS would lose track of where "
    "each process was. See Fig 1.6."
)

pn.highlight(
    "<b>Q14. Explain the difference between user-level threads and kernel-level threads. "
    "Which is better and why?</b><br/>"
    "A: ULT: managed by library, fast creation, no kernel knowledge → blocking I/O stops all threads, no multi-core. "
    "KLT: managed by kernel, slower creation → blocking only affects one thread, true multi-core parallelism. "
    "KLT is better for modern systems: handles blocking I/O correctly and exploits multi-core CPUs. "
    "ULT is only faster for thread creation/switch in rare specialized applications. "
    "Modern Linux uses KLT (NPTL) — pthreads are kernel threads."
)

pn.highlight(
    "<b>Q15. Explain multithreading models: Many-to-One, One-to-One, Many-to-Many, Two-Level.</b><br/>"
    "A: <b>Many-to-One (M:1):</b> All user threads map to one kernel thread. Fast but no parallelism; "
    "one block = all block. Example: Solaris Green Threads. "
    "<b>One-to-One (1:1):</b> Each user thread has its own kernel thread. True parallelism; "
    "no blocking problem. Standard today (Linux NPTL, Windows). "
    "<b>Many-to-Many (M:N):</b> M user threads → pool of N kernel threads. No blocking; parallelism; "
    "complex. Example: old Solaris. "
    "<b>Two-Level:</b> M:N + option to bind a specific thread 1:1. Maximum flexibility."
)

pn.section("10-Mark Questions (Detailed)")

pn.highlight(
    "<b>Q16. What is an OS? Explain its functions, services, and role as a resource manager "
    "with a diagram.</b><br/>"
    "A: OS = system software managing hardware for programs and users. "
    "<b>As Resource Manager:</b> Allocates CPU (scheduling), RAM (memory management), "
    "disk (file system), and I/O devices to competing processes efficiently. "
    "<b>Functions:</b> Process management, memory management, file system, I/O management, "
    "security, networking, command interpreter. "
    "<b>Services:</b> Program execution, I/O operations, file manipulation, communication, "
    "error detection, resource allocation, accounting, protection. "
    "See Fig 1.2 for the OS resource manager diagram."
)

pn.highlight(
    "<b>Q17. Explain with a neat diagram how a system call is executed, "
    "covering mode switch, trap instruction, and return.</b><br/>"
    "A: Application calls library function (e.g., read()). "
    "Library places syscall number in CPU register and executes TRAP/INT/SYSCALL instruction. "
    "CPU hardware: saves PC + flags on kernel stack; switches to kernel mode (ring 0). "
    "Kernel's interrupt handler: reads syscall number; dispatches to sys_read() function. "
    "Kernel executes the service; places return value in register. "
    "Kernel executes IRET/SYSRET: CPU restores user context; switches back to user mode. "
    "Library returns result to application. See Fig 1.3 sequence diagram."
)

pn.highlight(
    "<b>Q18. Compare monolithic kernel and microkernel. "
    "Draw their structure and explain trade-offs.</b><br/>"
    "A: <b>Monolithic:</b> Entire OS in kernel space. Fast (no IPC between components). "
    "Fragile (driver bug crashes kernel). Hard to maintain. Examples: Linux, Unix. "
    "<b>Microkernel:</b> Only IPC + basic scheduling + memory in kernel. "
    "File system, drivers in user space as servers. More reliable (server crash ≠ kernel crash). "
    "Slower (message passing overhead). Examples: Mach, QNX, MINIX. "
    "<b>Hybrid (Windows NT):</b> Mix — critical services in kernel for speed, "
    "others in user space for modularity. Best compromise in practice. "
    "See side-by-side layered diagrams in Section 1.5."
)

pn.highlight(
    "<b>Q19. Define process and explain process states, PCB, and context switching together "
    "in one comprehensive answer.</b><br/>"
    "A: Process = program in execution. Has code, data, stack, heap + PCB. "
    "<b>States:</b> New → Ready → Running → Waiting → Terminated (5-state model). "
    "<b>PCB:</b> Kernel data structure with PID, state, PC, registers, memory maps, "
    "scheduling info, I/O status, accounting info. "
    "<b>Context Switch:</b> When OS switches CPU from P1 to P2: saves P1's CPU state → "
    "PCB1; restores P2's CPU state ← PCB2. Overhead = wasted CPU time. "
    "PCB enables context switching; state diagram shows when switches happen."
)

pn.highlight(
    "<b>Q20. Explain threads, types of threads, and all multithreading models with diagrams. "
    "Compare thread vs process.</b><br/>"
    "A: Thread = lightweight execution unit inside process. "
    "Shares: code, data, heap, files. Private: stack, PC, registers. "
    "<b>ULT:</b> managed in user space — fast, portable, but blocking I/O stops all, no parallelism. "
    "<b>KLT:</b> managed by kernel — full parallelism, handles blocking, but higher overhead. "
    "<b>Models:</b> M:1 (no parallelism, old), 1:1 (standard today — Linux/Windows), "
    "M:N (complex, best theoretical), Two-Level (M:N + binding). "
    "Process vs Thread: process isolated, expensive; thread shared, cheap. "
    "See Section 1.12–1.14 for full comparison tables and diagrams."
)

pn.section("Quick Revision Summary — Unit I")
pn.info_table(
    ["Topic", "Key Exam Points"],
    [
        [
            "System Software",
            "Manages hardware. OS, drivers, firmware. Distinct from application software (user tasks).",
        ],
        [
            "OS Definition",
            "Interface between user/programs and hardware + resource manager. Goals: convenience + efficiency.",
        ],
        [
            "OS Types",
            "Batch (no interaction), Multiprogramming (CPU switches on I/O), Time-sharing (quanta), RTOS (deadlines), Distributed, Embedded.",
        ],
        [
            "Kernel",
            "Always-resident core of OS. Runs in kernel mode (ring 0). Monolithic (all in kernel) vs Microkernel (minimal kernel) vs Hybrid.",
        ],
        [
            "Kernel vs User Mode",
            "Kernel: ring 0, full hardware access. User: ring 3, restricted. Mode switch via TRAP/SYSCALL instruction.",
        ],
        [
            "System Call",
            "User → kernel interface. Categories: process, file, device, info, communication, protection. TRAP causes mode switch.",
        ],
        [
            "Process Definition",
            "Program in execution. Has code, data, stack, heap, PCB. NOT same as program (passive code on disk).",
        ],
        [
            "5 Process States",
            "New → Ready → Running → Waiting → Terminated. Key: Running→Waiting on I/O; Waiting→Ready on I/O done.",
        ],
        [
            "PCB Fields",
            "PID, state, PC, registers, scheduling info, memory maps, I/O status, accounting info, PPID.",
        ],
        [
            "Context Switch",
            "Save P1 PCB → select P2 → restore P2 PCB. Pure overhead. Causes: TLB flush, cache cold start.",
        ],
        [
            "Long-term Scheduler",
            "Job → memory. Controls degree of multiprogramming. Infrequent.",
        ],
        [
            "Short-term Scheduler",
            "Ready → Running. CPU scheduling algorithm. Very frequent (every ~100ms).",
        ],
        [
            "Medium-term Scheduler",
            "Swapper. Swaps process in/out of memory. Manages memory pressure.",
        ],
        [
            "Thread Benefits",
            "Responsiveness, resource sharing, economy (cheap to create), scalability (multi-core).",
        ],
        [
            "ULT vs KLT",
            "ULT: fast, no parallelism, blocks all. KLT: slower, true parallelism, solves blocking.",
        ],
        [
            "Many-to-One",
            "Fast, no parallelism, blocking problem. Old Solaris Green Threads.",
        ],
        [
            "One-to-One",
            "Standard today. True parallelism. No blocking issue. Linux (NPTL), Windows.",
        ],
        [
            "Many-to-Many",
            "M ULT → N KLT pool. No blocking, parallelism, complex. Old Solaris, IRIX.",
        ],
        [
            "Two-Level Model",
            "M:N + ability to bind 1:1. Maximum flexibility. Solaris 9+.",
        ],
    ],
)

pn.exam(
    "Most asked topics in IT412 Unit I exams: "
    "(1) Process state diagram — draw and explain ALL transitions. "
    "(2) PCB contents and role in context switching. "
    "(3) Types of OS — batch vs time-sharing vs real-time comparison. "
    "(4) Kernel types — monolithic vs microkernel with diagram. "
    "(5) Multithreading models — all four with mapping diagram. "
    "(6) ULT vs KLT comparison table. "
    "Know these six topics thoroughly for guaranteed marks."
)

pn.note(
    "Reference Books: \n"
    "(1) Silberschatz — 'Operating System Concepts' (Dinosaur Book) — primary reference. \n"
    "(2) S.Haldar & A.A. Arvind — 'Operating Systems', Pearson, 2nd Edition. \n"
    "(3) D.M. Dhamdhere — 'Operating System: A Concept-Based Approach', TMH. \n"
    "(4) Pabitra Pal Choudhury — 'Operating System: Principle and Design', PHI."
)

pn.br()
pn.chap_box("Rapid Revision & Flashcards")
pn.revision_card(
    "Unit I Mastery Check",
    [
        "Differentiate between Multiprogramming, Multitasking, and Multiprocessing.",
        "Draw and explain the 5-state process transition diagram perfectly.",
        "List all the contents of a Process Control Block (PCB).",
        "Explain the roles of Long-term, Short-term, and Medium-term schedulers.",
        "Compare User-level and Kernel-level threads.",
    ],
)

pn.flashcard(
    "What is the <b>Kernel</b>?",
    "The core of the OS that remains in memory at all times. It has complete control over everything in the system.",
)
pn.flashcard(
    "What is a <b>PCB (Process Control Block)</b>?",
    "A data structure in the OS kernel containing all information needed to manage a particular process (State, PC, Registers, Memory info).",
)
pn.flashcard(
    "What is <b>Context Switching</b>?",
    "The process of saving the state of the currently running process (in its PCB) and loading the state of the next process.",
)

pn.br()
pn.chap_box("Index")
pn.print_index()

# =============================================================================
#  BUILD DOCUMENT
# =============================================================================
pn.build_doc("OS_Unit1_Notes.pdf")

print("Generated: OS_Unit1_Notes.pdf")
