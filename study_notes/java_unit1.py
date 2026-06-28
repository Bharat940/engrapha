"""
Java Programming (IT408) -- Unit I Notes
UIT-RGPV (Autonomous) Bhopal | Semester IV
Complete exam notes with Java syntax highlighting and vector diagrams.
Run: python java_unit1.py
Output: Java_Unit1_Notes.pdf
"""

from __future__ import annotations

import engrapha_notes as en
import engrapha_diagrams as ed

# =============================================================================
#  THEME & GLOBAL FOOTER SETUP
# =============================================================================
en.set_story([])
en.set_theme(en.CATPPUCCIN_MOCHA)

# Set the global academic footer across all pages (except cover/TOC)
en.set_global_footer(
    left="Java Programming (IT408) -- Unit I",
    right="UIT-RGPV (Autonomous) Bhopal",
    show_page_num=True,
)

diag_theme = ed.DiagramTheme.from_notes_theme(en.get_theme())

# =============================================================================
#  COVER PAGE
# =============================================================================
en.bookmark("Cover Page")
en.suppress_footer(page_only=True)
en.sp(28)

en.cover_card("JAVA PROGRAMMING", "Unit I -- Language Fundamentals & OOP")
# en.cover_subtitle(
#     [
#         "Subject Code: IT408  |  UIT-RGPV (Autonomous) Bhopal  |  Semester IV",
#         "Complete Exam Notes with OOP Fundamentals, Installation, Compilation, Language Elements,",
#         "Data Types, Casting, Operators, Control Statements, and Arrays",
#     ]
# )
en.sp(10)
en.rule(en.get_theme().rl(en.get_theme().accent), 1.5)
en.sp(8)

en.info_table(
    ["Section", "Syllabus Topics Covered"],
    [
        [
            "1.1 OOP Concepts",
            "OOP Paradigm vs POP, Objects, Classes, Inheritance, Polymorphism, Encapsulation, Abstraction, Memory Layout",
        ],
        [
            "1.2 Overview of Java",
            "History, Java Buzzwords (Features), Platform Independence, Bytecode, Java Virtual Machine (JVM)",
        ],
        [
            "1.3 Environment Setup & JVM",
            "JDK vs. JRE vs. JVM, JVM Internal Architecture, Environment Variables (PATH, CLASSPATH)",
        ],
        [
            "1.4 First Program & Process",
            "HelloWorld program analysis, Compilation & Execution process, JVM Class File binary structure",
        ],
        [
            "1.5 Lexical Basics & Comments",
            "Keywords, Identifiers (Rules & Conventions), Literals, Comment types (Single, Multi, Javadoc)",
        ],
        [
            "1.6 Data Types, Variables & Scope",
            "Primitive Data Types (size & range), Instance vs. Class vs. Local variables, Block Scope and Variable Lifetime",
        ],
        [
            "1.7 Type Conversion & Casting",
            "Automatic (Widening) conversion, Explicit (Narrowing) casting, Type Promotion rules in expressions",
        ],
        [
            "1.8 Operators & Precedence",
            "Arithmetic, Bitwise, Relational, Logical, Assignment, Shift operators, Precedence & Associativity table",
        ],
        [
            "1.9 Control Statements",
            "Selection (if-else, switch case fall-through), Iteration (while, do-while, for loops), Jump statements (break, continue)",
        ],
        [
            "1.10 Arrays in Java",
            "Single-dimensional & Multi-dimensional arrays, Array memory layout, Jagged / Irregular arrays",
        ],
        [
            "1.11 Exam Flashcards",
            "High-yield revision cards, core definitions, and key exam focus areas for Unit I",
        ],
    ],
    col_widths=["30%", "70%"],
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
en.part_box("UNIT I -- JAVA LANGUAGE FUNDAMENTALS & OOP")

# =============================================================================
#  1.1  OBJECT-ORIENTED PROGRAMMING CONCEPTS
# =============================================================================
en.chap_box("1.1  Object-Oriented Programming (OOP) Concepts")
en.section("OOP Paradigm vs Procedure-Oriented Programming")
en.body(
    "Java is built entirely around the <b>Object-Oriented Programming (OOP)</b> paradigm. "
    "Unlike procedure-oriented programming (like C) which focuses on writing code algorithms "
    "to operate on data, OOP organizes programs around data (objects) and methods that interact with them."
)

en.info_table(
    [
        "Feature",
        "Procedure-Oriented Programming (POP)",
        "Object-Oriented Programming (OOP)",
    ],
    [
        ["Programming Approach", "Top-down approach", "Bottom-up approach"],
        [
            "Primary Entity",
            "Functions and algorithms",
            "Objects containing state and behavior",
        ],
        [
            "Data Movement",
            "Data moves openly from function to function",
            "Objects communicate via message passing",
        ],
        [
            "Data Security",
            "No access specifiers; data is highly vulnerable",
            "Private access specifiers enable data hiding",
        ],
        [
            "Code Reusability",
            "Limited; requires duplicating function modules",
            "High; achieved via class inheritance",
        ],
        [
            "Polymorphism",
            "Not supported; no function overloading",
            "Supported; overloading and overriding allowed",
        ],
    ],
)

en.definition(
    "<b>Object:</b> An instance of a class. It represents a real-world entity with a state "
    "(attributes/fields) and behavior (methods). For example, a Student object has states like "
    "name, rollNumber, and behaviors like study(), attendClass()."
)
en.definition(
    "<b>Class:</b> A blueprint, template, or user-defined data type from which individual objects "
    "are created. It defines the structure and behavior that objects of the class will possess. "
    "A class is a logical entity (requires no heap space), while an object is a physical entity."
)

en.section("Object Memory Layout in Java")
en.bullet(
    [
        "<b>Stack Memory:</b> Stores the local variables and the object reference variable. "
        "The reference variable (e.g. <i>Student s</i>) holds the memory address pointing to the heap.",
        "<b>Heap Memory:</b> Stores the actual object itself, including all its instance variables. "
        "Allocated dynamically at runtime using the <i>new</i> keyword.",
        "<b>Method Area (Class Area):</b> Stores the bytecode of class methods, constant pool, "
        "and static variables shared across all instances.",
    ]
)

en.section("Core Principles of OOP")
en.bullet(
    [
        "<b>Encapsulation:</b> The process of wrapping data (variables) and code (methods) together "
        "as a single unit (a class). By declaring variables as private, we achieve data hiding, "
        "restricting direct access and forcing modification only via public getter/setter methods.",
        "<b>Inheritance:</b> A mechanism that allows a new class (subclass/child) to acquire the "
        "properties and behaviors of an existing class (superclass/parent) using the <i>extends</i> "
        "keyword. This promotes code reusability.",
        "<b>Polymorphism:</b> The ability of a message or object to be displayed or behave in "
        "multiple forms. In Java, this is realized via method overloading (compile-time polymorphism) "
        "and method overriding (runtime polymorphism).",
        "<b>Abstraction:</b> The concept of hiding internal implementation details and showing "
        "only essential features to the user. It is achieved in Java using abstract classes and interfaces.",
    ]
)

en.section("Polymorphism: Overloading vs. Overriding")
en.info_table(
    ["Property", "Method Overloading (Compile-time)", "Method Overriding (Runtime)"],
    [
        [
            "Resolution Time",
            "Resolved during compilation (Static Binding)",
            "Resolved during execution (Dynamic Binding)",
        ],
        [
            "Location",
            "Must occur within the same class",
            "Must occur between Superclass and Subclass",
        ],
        [
            "Method Signature",
            "Must differ (different parameter counts or types)",
            "Must be identical (same name, parameters, and return type)",
        ],
        ["Inheritance", "Not required", "Required"],
    ],
)

en.info_table(
    ["OOP Principle", "Java Implementation Mechanism", "Primary Benefit"],
    [
        [
            "Encapsulation",
            "Access specifiers (private, public, protected), getters/setters",
            "Data security and control",
        ],
        [
            "Inheritance",
            "The 'extends' keyword, superclass-subclass relationship",
            "Code reusability and hierarchy",
        ],
        [
            "Polymorphism",
            "Method overloading (static) and method overriding (dynamic)",
            "Flexibility and extensible systems",
        ],
        [
            "Abstraction",
            "Abstract classes, Interfaces",
            "Reduced complexity and separation of concerns",
        ],
    ],
)

en.sp(4)
en.section("OOP Principles Visualized")
en.body(
    "Below is a UML Class Diagram showing the core concepts of object-oriented design: "
    "<b>Abstraction</b> (abstract superclass Vehicle), <b>Encapsulation</b> (private variable brand with public getter), "
    "and <b>Inheritance</b> (subclasses Car and Bicycle extending Vehicle)."
)

cd = ed.ClassDiagram(
    width=en.CW,
    height=165,
    theme=diag_theme,
    caption="Fig 1.1: UML Class Diagram demonstrating Inheritance, Encapsulation, and Abstraction",
    class_w=120,
)
cd.uml_class(
    "Vehicle",
    "Vehicle",
    stereotype="abstract",
    attributes=["-brand: String"],
    methods=["+ honk(): void", "+ getBrand(): String"],
)
cd.uml_class(
    "Car", "Car", attributes=["-modelName: String"], methods=["+ drive(): void"]
)
cd.uml_class(
    "Bicycle", "Bicycle", attributes=["-gearCount: int"], methods=["+ pedal(): void"]
)

cd.relate("Car", "Vehicle", kind="inheritance")
cd.relate("Bicycle", "Vehicle", kind="inheritance")

en.story.extend(cd.as_flowable())
en.br()

# =============================================================================
#  1.2  OVERVIEW OF JAVA
# =============================================================================
en.chap_box("1.2  Overview of Java & Key Features")
en.section("What is Java?")
en.body(
    "Java is a general-purpose, concurrent, class-based, object-oriented programming language "
    "originally developed by Sun Microsystems (led by James Gosling, Patrick Naughton, Mike Sheridan, "
    "and their 'Green Team') in 1995. Initially named <i>Oak</i> (after an oak tree outside Gosling's office), "
    "it was later renamed to <i>Java</i> (inspired by Java coffee). Sun Microsystems was later acquired "
    "by Oracle Corporation in 2010, which now maintains the language."
)

en.section("Features of Java (The Java Buzzwords)")
en.info_table(
    ["Feature", "Explanation", "Significance in Exams & Industry"],
    [
        [
            "Simple",
            "Easy to learn with a clean syntax based on C/C++ but removes complex/unsafe elements.",
            "No pointers, explicit memory deallocation (free), or multiple inheritance.",
        ],
        [
            "Platform Independent",
            "Write Once, Run Anywhere (WORA). Compilation produces bytecode, not machine code.",
            "Compiled bytecode (.class) can run on any operating system as long as it has a compatible JVM.",
        ],
        [
            "Secure",
            "Executes inside a virtual machine sandbox with strict memory safety rules.",
            "No direct memory pointer manipulation prevents buffer overflows and pointer corruption.",
        ],
        [
            "Robust",
            "Strong type-checking, exception handling, and automatic garbage collection.",
            "Memory management is handled automatically; runtime exception handling prevents abrupt crashes.",
        ],
        [
            "Architecture Neutral",
            "Integers, floats, and characters have fixed sizes across all target platforms.",
            "A 32-bit integer is always 32-bit, whether running on 32-bit, 64-bit, x86, or ARM CPUs.",
        ],
        [
            "Multi-threaded",
            "Built-in support for executing multiple threads of execution concurrently.",
            "Allows developers to write highly interactive, responsive, and high-concurrency applications.",
        ],
        [
            "Distributed",
            "Built-in capabilities for network operations and remote communication.",
            "Supports protocols like HTTP and TCP/IP, and mechanisms like Remote Method Invocation (RMI).",
        ],
        [
            "Dynamic",
            "Classes are loaded on-demand at runtime, and classes can adapt dynamically.",
            "Supports dynamic class loading, runtime reflection, and dynamic bindings.",
        ],
        [
            "High Performance",
            "Uses a Just-In-Time (JIT) compiler to compile bytecode to native code.",
            "Bridges the gap between compiled languages (like C++) and purely interpreted languages.",
        ],
    ],
)

en.note(
    "Java's platform independence is driven by the compile-and-interpret design. The compiler (javac) "
    "translates source code to bytecode (.class), which is then interpreted/JITcompiled at runtime by "
    "the local OS-specific Java Virtual Machine (JVM). Thus, <b>Java the language</b> is platform independent, "
    "but <b>the JVM itself</b> is platform dependent since it must interface with the native operating system."
)
en.br()

# =============================================================================
#  1.3  INSTALLATION & ENVIRONMENT SETUP
# =============================================================================
en.chap_box("1.3  Java Environment Setup: JDK vs. JRE vs. JVM")
en.section("Comparing the Core Components")
en.body(
    "When setting up Java, it is crucial to understand the distinct roles of the JVM, JRE, and JDK "
    "in the development and execution lifecycle."
)

en.definition(
    "<b>JVM (Java Virtual Machine):</b> An abstract computing machine that provides the runtime "
    "execution environment for Java bytecode. It is platform-dependent (different JVMs are written "
    "for Windows, macOS, Linux) and translates bytecode to native CPU instructions."
)
en.definition(
    "<b>JRE (Java Runtime Environment):</b> The minimum environment required to <i>run</i> Java "
    "programs. It contains the JVM, standard Java class libraries, and other supporting files. It "
    "does not contain development tools like compilers (javac) or debuggers."
)
en.definition(
    "<b>JDK (Java Development Kit):</b> The complete software development environment containing "
    "the JRE plus tools (javac compiler, java interpreter, jdb debugger, javadoc tool) needed to "
    "<i>write and compile</i> Java applications."
)

en.info_table(
    ["Component", "Target Audience", "Key Contents"],
    [
        [
            "JVM",
            "Underlying Execution Layer",
            "Interpreter, JIT Compiler, Garbage Collector, Class Loader",
        ],
        ["JRE", "End Users / Runners", "JVM + Core Standard Libraries (rt.jar, etc.)"],
        [
            "JDK",
            "Developers / Authors",
            "JRE + Compilers (javac), debuggers (jdb), packagers (jar)",
        ],
    ],
)

en.section("JVM Internal Architecture")
en.bullet(
    [
        "<b>ClassLoader Subsystem:</b> Responsible for loading, linking, and initializing class files. "
        "Loading is done via 3 class loaders: Bootstrap (loads core libraries), Extension (loads classes from ext folder), "
        "and Application (loads from classpath). Linking involves Verification (bytecode checks), "
        "Preparation (static variables allocated defaults), and Resolution (references resolved). "
        "Initialization runs static blocks and assigns actual static values.",
        "<b>Runtime Data Areas:</b> The memory allocated by the JVM. Divided into 5 areas: "
        "1. <i>Method Area:</i> Stores class structures, constant pools, and static variables (shared). "
        "2. <i>Heap:</i> Stores all instantiated objects and arrays (shared). "
        "3. <i>JVM Stacks:</i> Stores local variables and stack frames for method calls (thread-private). "
        "4. <i>PC Registers:</i> Stores current instruction address (thread-private). "
        "5. <i>Native Method Stack:</i> Stores native code state (thread-private).",
        "<b>Execution Engine:</b> Executes the bytecode. Contains: "
        "1. <i>Interpreter:</i> Reads bytecode line-by-line (slower). "
        "2. <i>JIT Compiler:</i> Dynamically compiles frequently executed code (hotspots) to native instructions for performance. "
        "3. <i>Garbage Collector:</i> Automatically detects and deallocates unreferenced heap objects.",
    ]
)

en.section("Setting Environment Variables")
en.bullet(
    [
        "<b>PATH:</b> Tells the operating system shell where to find developer executable tools "
        "like the compiler (javac) and interpreter (java). Points to <i>C:\\Program Files\\Java\\jdk-xx\\bin</i>.",
        "<b>CLASSPATH:</b> Tells the JVM and compiler where to search for user-defined libraries, "
        "packages, and external class files (e.g. JAR libraries) during compilation or runtime. "
        "Can be overridden at command line using the <i>-cp</i> or <i>--class-path</i> option (e.g., <i>java -cp . HelloWorld</i>).",
    ]
)

en.sp(4)
en.section("JDK vs. JRE vs. JVM Nested Relationship")
en.body(
    "A visual representation of the Java development environment hierarchy. The JDK contains the JRE, "
    "and the JRE contains the JVM."
)

stack = ed.LayeredStack(
    width=en.CW * 0.7,
    height=150,
    theme=diag_theme,
    caption="Fig 1.2: Nested Architecture of JDK, JRE, and JVM",
)
stack.layer(
    "JDK (Java Development Kit)",
    sublabel="Development Tools: javac, java, jdb, jar, javadoc",
)
stack.layer(
    "JRE (Java Runtime Environment)",
    sublabel="Runtime Libraries (rt.jar, charsets.jar) + JVM",
)
stack.layer(
    "JVM (Java Virtual Machine)",
    sublabel="Execution Engine: JIT, Class Loader, Garbage Collector",
)

en.story.extend(stack.as_flowable())
en.br()

# =============================================================================
#  1.4  FIRST SIMPLE PROGRAM & COMPILATION FLOW
# =============================================================================
en.chap_box("1.4  First Simple Program & Compilation Flow")
en.section("First Simple Java Program")
en.body(
    "Here is a basic Java program that prints a message to the console. In Java, all code "
    "must reside inside a class. The filename must match the name of the public class."
)

en.code_block(
    """
// HelloWorld.java
// In Java, all code must reside inside a class. 
// Public class name must match the source filename.
public class HelloWorld {
    
    // The main method is the entry point of the program.
    // public: accessible by JVM from outside the class.
    // static: can be invoked without class instances.
    // void: returns no value.
    // String[] args: accepts command-line string parameters.
    public static void main(String[] args) {
        
        // System: built-in standard tool class.
        // out: static standard console output PrintStream.
        // println: prints the given string with a newline.
        System.out.println("Hello, World!");
    }
}
""",
    lang="java",
)

en.section("Step-by-Step Compilation & Execution")
en.bullet(
    [
        "<b>Step 1 (Source):</b> The programmer writes code in <i>HelloWorld.java</i>.",
        "<b>Step 2 (Compilation):</b> The compiler `javac HelloWorld.java` generates bytecode in <i>HelloWorld.class</i>.",
        "<b>Step 3 (Execution):</b> The interpreter `java HelloWorld` executes the bytecode via the JVM.",
    ]
)

# Compilation network diagram
net_comp = ed.NetworkDiagram(
    width=en.CW,
    height=150,
    theme=diag_theme,
    caption="Fig 1.3: Java Compilation and Virtual Machine Execution Lifecycle",
)
net_comp.node("src", "Source File\n(Hello.java)", x=45, y=80, kind="host")
net_comp.node(
    "javac", "Java Compiler\n(javac compiler tool)", x=145, y=80, kind="server"
)
net_comp.node("bytecode", "Bytecode File\n(Hello.class)", x=245, y=80, kind="storage")
net_comp.node("jvm", "JVM Interpreter/JIT\n(java launcher)", x=345, y=80, kind="server")
net_comp.node(
    "os", "Machine Execution\n(Windows/Linux/macOS)", x=445, y=80, kind="cloud"
)

net_comp.link("src", "javac", bidirectional=False)
net_comp.link("javac", "bytecode", bidirectional=False)
net_comp.link("bytecode", "jvm", bidirectional=False)
net_comp.link("jvm", "os", bidirectional=False)

en.story.extend(net_comp.as_flowable())

en.sp(4)
en.section("JVM Class File (.class) Binary Structure")
en.body(
    "Every compiled Java class file starts with a specific binary sequence "
    "containing metadata, version indexes, constant tables, and bytecode. The header begins "
    "with a magic number signature <i>0xCAFEBABE</i>. Below is the 32-bit field structure:"
)

en.packet_format(
    "JVM Class File (.class) Header structure",
    [
        ("Magic Number (0xCAFEBABE)", 32),
        ("Minor Version", 16),
        ("Major Version", 16),
        ("Constant Pool Count", 16),
        ("Access Flags", 16),
        ("This Class Index", 16),
        ("Super Class Index", 16),
    ],
    bit_ruler=True,
)

en.info_table(
    ["Class File Field", "Size (Bits)", "Description & Exam Relevance"],
    [
        [
            "Magic Number",
            "32 bits",
            "Always contains 0xCAFEBABE. Used by JVM to identify valid class files.",
        ],
        [
            "Minor / Major Version",
            "16 + 16 bits",
            "Specifies the compiler version (e.g. Major version 52 is Java 8, 61 is Java 17). JVM refuses to run if major version is higher than supported.",
        ],
        [
            "Constant Pool Count",
            "16 bits",
            "The number of entries in the constant pool table plus one.",
        ],
        [
            "Access Flags",
            "16 bits",
            "Mask of flags denoting permissions/properties (e.g., public, final, abstract, interface).",
        ],
        [
            "This Class Index",
            "16 bits",
            "Points to a class entry in the constant pool representing this class name.",
        ],
        [
            "Super Class Index",
            "16 bits",
            "Points to a class entry in the constant pool representing the parent class name.",
        ],
    ],
)
en.br()

# =============================================================================
#  1.5  KEYWORDS, IDENTIFIERS, LITERALS, AND COMMENTS
# =============================================================================
en.chap_box("1.5  Java Keywords, Identifiers, Literals, and Comments")
en.section("Java Keywords")
en.body(
    "Keywords are reserved words that have predefined meanings in Java and cannot be used as "
    "variable, class, or method names. Java has 50+ keywords, which can be categorized as follows:"
)
en.info_table(
    ["Category", "Keywords", "Description"],
    [
        [
            "Data Types",
            "byte, short, int, long, float, double, char, boolean, void",
            "Define the type of data a variable or method return holds.",
        ],
        [
            "Control Flow",
            "if, else, switch, case, default, for, while, do, break, continue, return",
            "Manage loop iterations and conditional branches.",
        ],
        [
            "Access Modifiers",
            "private, protected, public",
            "Control visibility and scope of classes and members.",
        ],
        [
            "OOP & Class",
            "class, interface, extends, implements, new, this, super, static, abstract, final",
            "Declare structures, manage inheritance, state binding, and instantiation.",
        ],
        [
            "Exceptions",
            "try, catch, finally, throw, throws, assert",
            "Handle run-time errors and perform debugging assertions.",
        ],
        [
            "Special / Unused",
            "const, goto",
            "Reserved keywords that currently have no function in Java.",
        ],
    ],
)

en.section("Identifiers (Naming Rules & Conventions)")
en.definition(
    "<b>Identifier:</b> Names given to classes, methods, variables, packages, and arrays. "
    "Rules for valid identifiers in Java: "
    "1. Must start with a letter (A-Z, a-z), underscore (_), or dollar sign ($). "
    "2. Subsequent characters can be digits (0-9). "
    "3. Cannot contain spaces or special characters (like @, #, %). "
    "4. Keywords cannot be used as identifiers. "
    "5. Java is case-sensitive (e.g., 'value' and 'Value' are distinct)."
)
en.body(
    "<b>Standard Naming Conventions (CamelCase):</b><br/>"
    "• <b>Classes / Interfaces:</b> PascalCase (e.g., <i>MyFirstClass</i>, <i>StudentDetails</i>). Start with an uppercase letter.<br/>"
    "• <b>Variables / Methods:</b> camelCase (e.g., <i>rollNumber</i>, <i>calculateTotalMarks()</i>). Start with a lowercase letter.<br/>"
    "• <b>Constants:</b> UPPER_CASE (e.g., <i>MAX_VALUE</i>, <i>PI_CONSTANT</i>). Separated by underscores."
)

en.section("Literals")
en.definition(
    "<b>Literal:</b> A constant value assigned directly to a variable. Types of literals in Java: "
    "1. <i>Integer Literals:</i> Decimal (42), Binary (0b1010), Hexadecimal (0x2A), and Octal (052). Supports underscores (e.g. 1_000_000) for readability since Java 7. "
    "2. <i>Floating-Point:</i> Float (3.14f) and Double (3.14159). "
    "3. <i>Character:</i> Unicode character ('a'), Escape sequences ('\\n', '\\t', '\\b'), and Unicode values ('\\u0041' for 'A'). "
    '4. <i>String:</i> Sequence of characters enclosed in double quotes (e.g., "Java"). String literals are stored in the String Constant Pool in heap memory. '
    "5. <i>Boolean & Null:</i> true, false, and null."
)

en.section("Types of Comments")
en.info_table(
    ["Comment Style", "Syntax", "Purpose & Scope"],
    [
        [
            "Single-line Comment",
            "// This is a comment",
            "For brief notes on a single line. Ignored by compiler.",
        ],
        [
            "Multi-line Comment",
            "/* This is a comment block */",
            "For longer descriptions spanning multiple lines. Ignored by compiler.",
        ],
        [
            "Javadoc Comment",
            "/** This is documentation */",
            "Documentation comment used by the Javadoc utility to automatically build HTML API references.",
        ],
    ],
)
en.br()

# =============================================================================
#  1.6  DATA TYPES, VARIABLES, AND INITIALIZATION
# =============================================================================
en.chap_box("1.6  Data Types, Variables, and Scope")
en.section("Data Types -- Size and Range")
en.body(
    "Java is a strongly typed language, meaning every variable must have a declared type before "
    "compilation. Java has 8 primitive data types (integers, floats, characters, booleans)."
)

en.info_table(
    ["Data Type", "Size (Bits)", "Default Value", "Range of Values"],
    [
        ["byte", "8 bits (1 byte)", "0", "-128 to 127"],
        ["short", "16 bits (2 bytes)", "0", "-32,768 to 32,767"],
        ["int", "32 bits (4 bytes)", "0", "-2,147,483,648 to 2,147,483,647"],
        [
            "long",
            "64 bits (8 bytes)",
            "0L",
            "-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807",
        ],
        [
            "float",
            "32 bits (4 bytes)",
            "0.0f",
            "IEEE 754 float (approx 7 decimal digits accuracy)",
        ],
        [
            "double",
            "64 bits (8 bytes)",
            "0.0d",
            "IEEE 754 double (approx 15 decimal digits accuracy)",
        ],
        ["char", "16 bits (2 bytes)", "'\\u0000'", "Unicode characters (0 to 65,535)"],
        ["boolean", "Virtual size", "false", "true or false"],
    ],
)

en.section("Instance Variables vs. Class (Static) Variables vs. Local Variables")
en.info_table(
    ["Variable Type", "Declared Location", "Default Value", "Memory Scope & Lifetime"],
    [
        [
            "Instance Variable",
            "Inside class, outside methods. Non-static.",
            "Initialized to default value (e.g. 0, null, false).",
            "Stored in heap. Created when object is instantiated; destroyed when garbage collected.",
        ],
        [
            "Class / Static Variable",
            "Inside class, outside methods. Declared static.",
            "Initialized to default value.",
            "Stored in method area. Created when class is loaded; destroyed when class is unloaded.",
        ],
        [
            "Local Variable",
            "Inside methods, constructors, or blocks.",
            "No default value. Must be explicitly initialized before reading.",
            "Stored on stack frame. Created when block is entered; destroyed when block is exited.",
        ],
    ],
)

en.section("Declaring Variables & Dynamic Initialization")
en.body(
    "A variable is a container that holds a value of a specified data type. In addition to "
    "static initialization, Java allows <b>dynamic initialization</b>, where a variable is "
    "initialized at runtime using an expression or method output."
)

en.code_block(
    """
// InitializationDemo.java
public class InitializationDemo {
    public static void main(String[] args) {
        // Static initialization: value is set at compile time
        double base = 3.0;
        double height = 4.0;

        // Dynamic initialization: calculated at runtime
        // Math.sqrt() returns double to initialize hypotenuse
        double sumOfSquares = (base * base) + (height * height);
        double hypotenuse = Math.sqrt(sumOfSquares);

        System.out.println("Hypotenuse is: " + hypotenuse);
    }
}
""",
    lang="java",
)

en.section("Scope and Lifetime of Variables")
en.definition(
    "<b>Scope:</b> Determines the visibility and accessibility of a variable in a program. "
    "Java variables are scoped to the block `{}` in which they are declared. Blocks can be "
    "nested, but inner blocks can access outer variables, while outer blocks cannot access inner variables. "
    "<b>Lifetime:</b> The duration for which a variable remains active in memory (from creation to destruction)."
)

en.code_block(
    """
// ScopeDemo.java
public class ScopeDemo {
    public static void main(String[] args) {
        int x = 10; // Visible to all code within main method
        
        if (x == 10) {
            int y = 20; // y is visible ONLY inside this block
            
            // Inner block can read outer variables
            System.out.println("Inner block x, y: " + x + ", " + y);
            x = y * 2;
        }
        // y = 100; // ERROR! y is out of scope here
        System.out.println("Outer block x: " + x);
    }
}
""",
    lang="java",
)
en.br()

# =============================================================================
#  1.7  TYPE CONVERSION AND CASTING
# =============================================================================
en.chap_box("1.7  Type Conversion and Casting")
en.section("Automatic (Widening) vs. Explicit (Narrowing) Conversion")
en.body(
    "Java handles type conversion automatically when converting compatible types of smaller size "
    "to larger size. However, explicit casting is required when converting a larger type to a smaller type."
)

en.definition(
    "<b>Widening (Automatic) Conversion:</b> Happens when target type is compatible and is "
    "larger than the source. No data loss occurs. "
    "Order: byte -> short -> int -> long -> float -> double."
)
en.definition(
    "<b>Narrowing (Explicit) Casting:</b> Happens when target type is smaller than source or "
    "is incompatible. Data loss may occur (truncation of decimals, integer overflow). "
    "Syntax: `(targetType) value`."
)

en.code_block(
    """
// ConversionDemo.java
public class ConversionDemo {
    public static void main(String[] args) {
        int iVal = 42;
        // Widening: int (32-bit) automatically promoted to double
        double dVal = iVal;
        System.out.println("Widening (int to double): " + dVal);

        double pi = 3.14159;
        // Narrowing: double cast to int. Decimal part truncated.
        int integerPi = (int) pi;
        System.out.println("Narrowing (double to int): " + integerPi);

        // Integer overflow / truncation mapping
        int bigInt = 258;
        // Explicit cast to byte (range -128 to 127). 
        // 258 % 256 = 2 (byte holds remainder)
        byte bVal = (byte) bigInt;
        System.out.println("Int 258 cast to byte: " + bVal);
    }
}
""",
    lang="java",
)

en.section("Type Promotion Rules in Expressions")
en.body(
    "When evaluating mathematical expressions, Java automatically promotes operand types to prevent data loss. "
    "The rules are applied in the following order:"
)
en.bullet(
    [
        "<b>Byte, Short, Char to Int:</b> All `byte`, `short`, and `char` operands are automatically promoted to `int` before arithmetic operations.",
        "<b>Promotion to Long:</b> If any operand is `long`, the entire expression is promoted to `long`.",
        "<b>Promotion to Float:</b> If any operand is `float`, the entire expression is promoted to `float`.",
        "<b>Promotion to Double:</b> If any operand is `double`, the entire expression is promoted to `double`.",
    ]
)
en.note(
    "<b>Exam Trap: The Byte Addition Compilation Error</b><br/>"
    "Consider the following code:<br/>"
    "<code>byte a = 40;<br/>"
    "byte b = 50;<br/>"
    "byte c = a + b; // COMPILATION ERROR!</code><br/>"
    "Even though 40 + 50 = 90 fits in a byte (range -128 to 127), the expression <code>a + b</code> "
    "is promoted to <code>int</code> at evaluation. Assigning an <code>int</code> to a <code>byte</code> variable "
    "requires explicit casting: <code>byte c = (byte)(a + b);</code>."
)
en.br()

# =============================================================================
#  1.8  OPERATORS AND EXPRESSIONS
# =============================================================================
en.chap_box("1.8  Operators and Precedence")
en.section("Java Operator Categories")
en.body(
    "Operators are tokens that perform specific calculations on one, two, or three operands. "
    "Java categorizes them based on their logic and execution precedence."
)

en.info_table(
    ["Operator Category", "Symbols", "Usage Example & Description"],
    [
        [
            "Arithmetic",
            "+, -, *, /, %, ++, --",
            "x = a % b; // Computes remainder of integer division",
        ],
        [
            "Relational",
            "==, !=, >, <, >=, <=",
            "if (a >= b) { ... } // Comparison operations",
        ],
        [
            "Logical (Short-Circuit)",
            "&&, ||, !",
            "if (isWeekend && hasTime) { ... } // Boolean conditions",
        ],
        [
            "Bitwise",
            "&, |, ^, ~, <<, >>, >>>",
            "result = flags & 0x0F; // Bit masking and shifting",
        ],
        [
            "Assignment",
            "=, +=, -=, *=, /=",
            "count += 1; // Shorthand arithmetic assignment",
        ],
        [
            "Ternary",
            "? :",
            "max = (a > b) ? a : b; // Inline conditional (if-else) expression",
        ],
    ],
)

en.section("Operator Precedence and Associativity")
en.body(
    "When multiple operators appear in a single expression, their execution order is determined "
    "by precedence. Operators with higher precedence are evaluated first. If they have equal precedence, "
    "associativity determines the direction (left-to-right or right-to-left):"
)

en.info_table(
    ["Precedence Level", "Operator Symbols", "Description", "Associativity"],
    [
        ["1 (Highest)", "expr++ , expr--", "Postfix operators", "Left-to-Right"],
        ["2", "++expr , --expr , + , - , ~ , !", "Unary operators", "Right-to-Left"],
        ["3", "* , / , %", "Multiplicative", "Left-to-Right"],
        ["4", "+ , -", "Additive", "Left-to-Right"],
        ["5", "<< , >> , >>>", "Shift operators", "Left-to-Right"],
        [
            "6",
            "< , > , <= , >= , instanceof",
            "Relational and type comparison",
            "Left-to-Right",
        ],
        ["7", "== , !=", "Equality comparison", "Left-to-Right"],
        ["8", "&", "Bitwise AND", "Left-to-Right"],
        ["9", "^", "Bitwise XOR", "Left-to-Right"],
        ["10", "|", "Bitwise OR", "Left-to-Right"],
        ["11", "&&", "Short-circuit Logical AND", "Left-to-Right"],
        ["12", "||", "Short-circuit Logical OR", "Left-to-Right"],
        ["13", "? :", "Ternary operator", "Right-to-Left"],
        [
            "14 (Lowest)",
            "= , += , -= , *= , /= , %=",
            "Assignment operators",
            "Right-to-Left",
        ],
    ],
)

en.section("Short-Circuit (&&, ||) vs. Logical (&, |) Operators")
en.bullet(
    [
        "<b>&& (Short-Circuit AND):</b> Evaluates the right-hand operand ONLY if the left-hand operand is true. "
        "Useful for preventing runtime crashes. For example: <i>if (str != null && str.length() > 0)</i> will not crash even if <i>str</i> is null.",
        "<b>& (Boolean Logical AND):</b> Always evaluates both operands regardless of the left operand value. Slower in logical expressions.",
        "<b>|| (Short-Circuit OR):</b> Evaluates the right-hand operand ONLY if the left-hand operand is false. If left is true, the result is immediately true.",
        "<b>| (Boolean Logical OR):</b> Always evaluates both operands regardless of the left operand value.",
    ]
)

en.section("Bitwise Shift Operators")
en.bullet(
    [
        "<b><< (Left Shift):</b> Shifts bits to the left, filling empty spaces on the right with zeros. Multiplies by 2 for each shift position.",
        "<b>>> (Signed Right Shift):</b> Shifts bits to the right, filling empty spaces on the left with the sign bit (preserves negative sign).",
        "<b>>>> (Unsigned Right Shift):</b> Shifts bits to the right, filling empty spaces on the left with zeros regardless of sign (always results in positive).",
    ]
)

en.code_block(
    """
// OperatorDemo.java
public class OperatorDemo {
    public static void main(String[] args) {
        // Ternary operator example
        int a = 10, b = 20;
        // Assigns b (20) because condition is false
        int max = (a > b) ? a : b; 
        System.out.println("Max value using ternary: " + max);

        // Bitwise operators
        int val = 8; // Binary: 0000 1000
        // Shift left by 2 positions (8 * 4 = 32)
        int leftShifted = val << 2; 
        System.out.println("8 left shifted by 2: " + leftShifted);

        int negativeVal = -8; // Binary: 1111 1000 (Two's complement)
        // Signed shift (sign bit preserved): -4
        int signedShift = negativeVal >> 1; 
        // Unsigned shift (zero filled): positive
        int unsignedShift = negativeVal >>> 1; 
        System.out.println("Signed shift of -8: " + signedShift);
        System.out.println("Unsigned shift of -8: " + unsignedShift);
    }
}
""",
    lang="java",
)
en.br()

# =============================================================================
#  1.9  CONTROL STATEMENTS
# =============================================================================
en.chap_box("1.9  Control Statements")
en.section("Selection, Iteration, and Jump Statements")
en.body(
    "Control statements determine the flow of program execution based on condition evaluations. "
    "They are categorized into Selection (conditional execution), Iteration (looping), and Jumps."
)

en.info_table(
    ["Flow Type", "Statements", "Purpose & Syntax Structure"],
    [
        [
            "Selection",
            "if, if-else, switch-case",
            "Choose between alternative execution paths based on boolean evaluations.",
        ],
        [
            "Iteration",
            "while, do-while, for, enhanced-for",
            "Repeatedly execute a block of code while a condition is true.",
        ],
        [
            "Jump",
            "break, continue, return",
            "Alter the standard flow, escaping loops or exiting functions directly.",
        ],
    ],
)

en.section("The Switch Statement & Case Fall-Through")
en.bullet(
    [
        "<b>Switch Expression Types:</b> The switch expression must evaluate to: <i>byte</i>, <i>short</i>, <i>char</i>, <i>int</i>, "
        "their corresponding wrapper classes (Byte, Short, Character, Integer), <i>String</i> (since Java 7), or an <i>Enum</i>.",
        "<b>Case Fall-Through:</b> If a <i>break</i> statement is omitted at the end of a case block, "
        "execution will continue ('fall through') into the statements of subsequent cases regardless of their condition, until a break or the end of the switch is reached.",
        "<b>Constant Expression:</b> Each case label value must be a compile-time constant expression of the same type as the switch expression.",
    ]
)

en.section("Loops: While vs. Do-While")
en.info_table(
    ["Property", "While Loop", "Do-While Loop"],
    [
        [
            "Type of Control",
            "Entry-controlled loop (pre-test). Condition checked before body is run.",
            "Exit-controlled loop (post-test). Condition checked after body is run.",
        ],
        [
            "Minimum Executions",
            "0 times (body might never run if condition starts false).",
            "1 time (body runs at least once before checking condition).",
        ],
        [
            "Syntax Structure",
            "<code>while(condition) { body }</code>",
            "<code>do { body } while(condition);</code>",
        ],
    ],
)

en.section("Code Demonstration -- Loops & Switch Case")
en.code_block(
    """
// ControlFlowDemo.java
public class ControlFlowDemo {
    public static void main(String[] args) {
        // 1. Switch Statement
        int choice = 2;
        switch (choice) {
            case 1:
                System.out.println("Selected Option 1");
                break; // Escape switch block
            case 2:
                System.out.println("Selected Option 2");
                break;
            default:
                System.out.println("Invalid Selection");
        }

        // 2. Demonstration of break and continue in a loop
        System.out.println("Looping with jump statements:");
        for (int i = 1; i <= 5; i++) {
            if (i == 2) {
                continue; // Skip print for 2
            }
            if (i == 5) {
                break; // Exit loop when i reaches 5
            }
            System.out.println("Value: " + i);
        }
    }
}
""",
    lang="java",
)

en.sp(4)
en.section("Labeled loops (labeled break and continue)")
en.body(
    "In Java, you can attach a label to nested loops. A labeled <i>break</i> or <i>continue</i> "
    "will transfer control directly out of or to the next iteration of the designated loop "
    "rather than just the innermost loop."
)

en.code_block(
    """
// LabeledLoopDemo.java
public class LabeledLoopDemo {
    public static void main(String[] args) {
        // Outer loop label
        outerLoop: 
        for (int i = 1; i <= 3; i++) {
            for (int j = 1; j <= 3; j++) {
                if (i == 2 && j == 2) {
                    // Breaks the designated outer loop
                    break outerLoop; 
                }
                System.out.println("i=" + i + ", j=" + j);
            }
        }
    }
}
""",
    lang="java",
)
en.br()

# =============================================================================
#  1.10  ARRAYS IN JAVA
# =============================================================================
en.chap_box("1.10  Arrays in Java")
en.section("Understanding Array Creation & Memory Layout")
en.body(
    "An array is a collection of variables of the same type referenced by a common name. "
    "Unlike C/C++, Java arrays are objects allocated dynamically on the heap. Memory is managed "
    "automatically by the Garbage Collector."
)

en.bullet(
    [
        "<b>Step 1: Declaration:</b> Declares the reference variable. No memory is allocated on the heap yet. "
        "Syntax: <code>int[] arr;</code> (Preferred) or <code>int arr[];</code>. <i>Note: Specifying size during declaration (e.g. <code>int[5] arr;</code>) is a compilation error!</i>",
        "<b>Step 2: Instantiation:</b> Allocates heap memory for the array elements and sets them to default values. "
        "Syntax: <code>arr = new int[5];</code>. The size of the array is fixed at this step and cannot be changed.",
        "<b>Step 3: Initialization:</b> Assigns specific values to array indexes (0-indexed). "
        "Syntax: <code>arr[0] = 100;</code>. Alternatively, use an array initializer: <code>int[] arr = {10, 20, 30};</code>.",
    ]
)

en.note(
    "<b>Array Properties: length Variable vs. String length() Method</b><br/>"
    "• To get the size of an <b>array</b>, use the read-only instance variable <code>.length</code> (e.g., <code>arr.length</code>). "
    "There are no parentheses because it is an instance field.<br/>"
    "• To get the length of a <b>String</b> object, use the method <code>.length()</code> (e.g., <code>str.length()</code>). "
    "It has parentheses because it is a method call."
)

en.section("Jagged / Irregular Arrays")
en.body(
    "Since multidimensional arrays are implemented as arrays of arrays, the nested arrays do "
    "not need to have the same length. This is known as a <b>jagged or irregular array</b>."
)

en.code_block(
    """
// ArrayDemo.java
public class ArrayDemo {
    public static void main(String[] args) {
        // 1. One-dimensional array declaration and initialization
        int[] scoreArray = {90, 85, 95}; // Implicit allocation
        System.out.println("First score in scoreArray: " + scoreArray[0]);

        // 2. Irregular (Jagged) Array allocation
        // Declare 2D array with fixed row size
        int[][] jagged = new int[3][];
        
        // Instantiate varying columns for each row
        jagged[0] = new int[2]; // Row 0 has 2 columns
        jagged[1] = new int[4]; // Row 1 has 4 columns
        jagged[2] = new int[1]; // Row 2 has 1 column

        // Initialize values into the jagged array using length property
        int count = 10;
        for (int i = 0; i < jagged.length; i++) {
            for (int j = 0; j < jagged[i].length; j++) {
                jagged[i][j] = count;
                count += 5;
            }
        }

        // Print the elements in a tabular representation
        System.out.println("Jagged Array Output:");
        for (int i = 0; i < jagged.length; i++) {
            System.out.print("Row " + i + ": ");
            for (int j = 0; j < jagged[i].length; j++) {
                System.out.print(jagged[i][j] + " ");
            }
            System.out.println(); // Newline
        }
    }
}
""",
    lang="java",
)
en.br()

# =============================================================================
#  1.11  QUICK REVISION SUMMARY
# =============================================================================
en.chap_box("1.11  Quick Revision Exam Flashcards")
en.section("Exam Key Focus Areas")
en.highlight(
    "<b>Q: Why is Java platform independent but JVM is platform dependent?</b><br/>"
    "A: The Java compiler javac compiles source code to Bytecode (.class) which is standard and "
    "platform-neutral. However, the JVM must interpret this bytecode into native CPU binary instructions "
    "of the specific operating system. Hence, a Windows machine needs a Windows-specific JVM, "
    "while a macOS machine needs a macOS-specific JVM."
)
en.highlight(
    "<b>Q: What is compile-time type checking?</b><br/>"
    "A: In Java, type checking is strictly performed by the compiler before program execution. "
    "Every variable, parameter, and return type must be declared explicitly, preventing memory safety "
    "crashes or incompatible types in assignments at runtime."
)
en.highlight(
    "<b>Q: What is the difference between >> and >>> operators?</b><br/>"
    "A: The signed shift operator (>>) preserves the sign bit (fills left vacancies with the value "
    "of the sign bit: 1 if negative, 0 if positive). The unsigned shift operator (>>>) fills left "
    "vacancies with zeros regardless of whether the original value was positive or negative."
)
en.highlight(
    "<b>Q: What is the difference between the == operator and the equals() method?</b><br/>"
    "A: The <code>==</code> operator compares reference memory addresses for objects (checking if they point to the same "
    "location on the heap) or direct values for primitives. The <code>.equals()</code> method is designed to compare "
    "the logical content/values inside the objects (often overridden in classes like String for value comparison)."
)
en.highlight(
    "<b>Q: Can a Java program execute without the main() method?</b><br/>"
    "A: Prior to Java 7, yes, we could execute static initializer blocks without a main method. However, "
    "from Java 7 onwards, the JVM checks for the presence of the main method (with the exact signature "
    "<code>public static void main(String[] args)</code>) before initializing execution, so it is strictly mandatory."
)
en.highlight(
    "<b>Q: How do break and continue differ inside loops?</b><br/>"
    "A: The <code>break</code> statement immediately terminates the loop execution entirely, passing control to the "
    "first statement outside the loop body. The <code>continue</code> statement skips only the remaining statements "
    "in the current iteration and jumps directly to the next loop iteration condition evaluation/increment."
)

en.note(
    "Make sure to practice writing class structures, simple programs, type casting rules, and loop control "
    "with jump statements (break/continue) for your exam!"
)

# =============================================================================
#  BUILD DOCUMENT
# =============================================================================
en.build_doc("Java_Unit1_Notes.pdf")
print("Generated: Java_Unit1_Notes.pdf")
