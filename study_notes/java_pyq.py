"""
Java Programming (IT-408) -- Previous Year Question Answers
UIT-RGPV (Autonomous) Bhopal | Semester IV
Covers: May-June 2024, June 2022, July-Dec 2024, May-June 2025
Run: python java_pyq.py
Output: Java_PYQ_Answers.pdf
"""

from __future__ import annotations

import paperforge_notes as pn
import paperforge_diagrams as pd

# =============================================================================
#  THEME & GLOBAL FOOTER SETUP
# =============================================================================
pn.set_story([])
pn.set_theme(pn.DARK)

pn.set_global_footer(
    left="Java Programming (IT-408) -- PYQ Answers",
    right="UIT-RGPV (Autonomous) Bhopal",
    show_page_num=True,
)

diag_theme = pd.DiagramTheme.from_notes_theme(pn.get_theme())

# =============================================================================
#  COVER PAGE
# =============================================================================
pn.bookmark("Cover Page")
pn.suppress_footer(page_only=True)
pn.sp(22)

pn.cover_card(
    "JAVA PROGRAMMING (IT-408)",
    "Previous Year Questions & Model Answers",
)
# pn.cover_subtitle(
#     [
#         "UIT-RGPV (Autonomous) Bhopal  |  Semester IV  |  Subject Code: IT-408",
#         "Exam Papers Covered: May-June 2024  |  June 2022  |  July-Dec 2024  |  May-June 2025",
#         "All 5 Questions (CO1-CO5) with Comprehensive Model Answers, Diagrams & Code",
#     ]
# )
pn.sp(8)
pn.rule(pn.get_theme().rl(pn.get_theme().accent), 1.5)
pn.sp(6)

pn.info_table(
    ["Question / CO", "Topic Area", "Sub-Parts Covered"],
    [
        [
            "Q1 -- CO1",
            "Java Fundamentals",
            "javac process, JVM, OOP justification, comments, data types, "
            "type casting, control statements, Java lifecycle, keywords",
        ],
        [
            "Q2 -- CO2",
            "OOP, Classes, Packages, Interfaces, Exceptions, Threads",
            "abstract keyword, garbage collection, inheritance, constructors, "
            "packages, exception handling, polymorphism, threads",
        ],
        [
            "Q3 -- CO3",
            "Applets",
            "Applet class, lifecycle (init/start/stop/destroy), HTML APPLET tag, "
            "status window, parameters, banner applet, graphics methods",
        ],
        [
            "Q4 -- CO4",
            "AWT, Swing, Layout Managers, GUI",
            "Frame vs Panel, layout managers, event listeners, AWT hierarchy, "
            "AWT vs Swing, GridLayout, BorderLayout, multi-threading",
        ],
        [
            "Q5 -- CO5",
            "Event Handling & JDBC",
            "Delegation event model, mouse events, ResultSet, JDBC drivers, "
            "remote database connectivity, exception/constructor/abstract notes",
        ],
    ],
    col_widths=["18%", "30%", "52%"],
)

pn.sp(6)
pn.note(
    "Mark scheme: Part (a) = 3 marks | Part (b) = 4 marks | Part (c) = 4 marks | "
    "Part (d) = 10 marks | Part (e) = 10 marks (alternative). "
    "When the same question appeared in multiple years, ONE comprehensive answer is "
    "provided with all year references noted in the header."
)
pn.br()

# =============================================================================
#  TABLE OF CONTENTS
# =============================================================================
pn.suppress_footer(page_only=True)
pn.toc()

# #############################################################################
#  QUESTION 1 -- CO1: JAVA FUNDAMENTALS
# #############################################################################
pn.part_box("QUESTION 1 -- CO1: JAVA FUNDAMENTALS")

# -----------------------------------------------------------------------------
#  Q1(a) -- 3 Marks
# -----------------------------------------------------------------------------
pn.chap_box(
    "Q1(a) [3 Marks] -- javac Command | JVM | Java as OOP & Platform-Independent Language\n"
    "(May-June 2025 | June 2022 | May-June 2024 | July-Dec 2024)"
)

pn.section("The javac Command & Java Compilation Process")
pn.definition(
    "<b>javac</b> is the Java compiler tool included in the JDK (Java Development Kit). "
    "Its primary function is to translate human-readable Java source code (.java files) "
    "into platform-neutral <b>bytecode</b> (.class files) that can be executed by any "
    "Java Virtual Machine (JVM) on any operating system."
)
pn.bullet(
    [
        "<b>Input:</b> Java source file(s) ending in <code>.java</code> "
        "(e.g., <code>HelloWorld.java</code>).",
        "<b>Output:</b> Compiled bytecode file(s) ending in <code>.class</code> "
        "(e.g., <code>HelloWorld.class</code>).",
        "<b>Syntax:</b> <code>javac HelloWorld.java</code> -- compiles the source file.",
        "<b>Bytecode:</b> Architecture-neutral intermediate code understood only by the JVM, "
        "not the native CPU.",
        "<b>Error Reporting:</b> javac performs syntax checking and reports compile-time "
        "errors (type mismatches, missing semicolons, undeclared variables, etc.).",
    ]
)

pn.section("What is JVM?")
pn.definition(
    "<b>JVM (Java Virtual Machine):</b> An abstract computing machine that provides the "
    "runtime execution environment for Java bytecode. The JVM reads .class bytecode files "
    "and translates them into native machine instructions for the underlying operating system. "
    "It is <b>platform-dependent</b> (a different JVM binary exists for Windows, Linux, "
    "and macOS), but it allows Java programs (compiled to bytecode) to be "
    "<b>platform-independent</b>."
)
pn.bullet(
    [
        "<b>ClassLoader:</b> Loads .class bytecode files into memory.",
        "<b>Bytecode Verifier:</b> Checks bytecode for safety/security before execution.",
        "<b>Interpreter:</b> Reads and executes bytecode instructions line-by-line.",
        "<b>JIT Compiler:</b> Compiles frequently-executed ('hot') bytecode to native code for speed.",
        "<b>Garbage Collector:</b> Automatically manages heap memory -- reclaims unused objects.",
    ]
)

pn.section("Justification: Java is Pure OOP and Platform-Independent")
pn.info_table(
    ["Claim", "Justification"],
    [
        [
            "Java is OOP",
            "Everything in Java is encapsulated inside a class. Java supports all four "
            "OOP pillars: Encapsulation (private + getters/setters), Inheritance (extends), "
            "Polymorphism (overloading + overriding), Abstraction (abstract class/interface). "
            "No code can exist outside a class.",
        ],
        [
            "Platform Independent",
            "javac compiles source code to bytecode (.class) -- not to native machine code. "
            "The same .class file runs on Windows, Linux, and macOS JVMs without recompilation. "
            "This is the WORA (Write Once, Run Anywhere) principle.",
        ],
        [
            "Caveat",
            "The JVM itself is platform-dependent (OS-specific binary), but the Java language "
            "and bytecode are platform-independent.",
        ],
    ],
)
pn.tip(
    "Exam tip for Q1(a): Remember the three-tier: Source (.java) -> javac -> Bytecode (.class) -> "
    "JVM -> Machine Code. JVM is platform-dependent; Java bytecode is platform-independent."
)

# -----------------------------------------------------------------------------
#  Q1(b) -- 4 Marks
# -----------------------------------------------------------------------------
pn.chap_box(
    "Q1(b) [4 Marks] -- Comments in Java | Static Methods | Type Casting | Array Sum\n"
    "(May-June 2025 | June 2022 | May-June 2024 | July-Dec 2024)"
)

pn.section("Comments in Java -- Purpose and Types")
pn.definition(
    "<b>Comments</b> are non-executable statements in Java that are completely ignored "
    "by the compiler (javac). They are used to explain code logic, provide documentation, "
    "temporarily disable code during debugging, and improve maintainability. "
    "Java supports three types of comments."
)
pn.info_table(
    ["Type", "Syntax", "Purpose"],
    [
        [
            "Single-line",
            "// This is a comment",
            "Brief inline explanation on one line. Ignored by compiler from // to end of line.",
        ],
        [
            "Multi-line",
            "/* Comment block */",
            "Longer explanation spanning multiple lines. Everything between /* and */ is ignored.",
        ],
        [
            "Javadoc",
            "/** Documentation */",
            "Processed by the javadoc tool to generate HTML API documentation. Supports tags: "
            "@param, @return, @author, @throws.",
        ],
    ],
)

pn.code_block(
    """
// Single-line comment -- quick inline note
int age = 20;   // age in years

/* Multi-line comment:
   This method calculates the sum of two integers.
   Used in the Calculator class.
*/
int add(int a, int b) { return a + b; }

/**
 * Javadoc comment -- auto-generates HTML documentation.
 * @param radius  the radius of the circle (must be positive)
 * @return        the area of the circle (PI * r^2)
 */
double circleArea(double radius) {
    return Math.PI * radius * radius;
}
""",
    lang="java",
)

pn.section("Static Method -- Definition and Example")
pn.definition(
    "<b>Static method:</b> A method declared with the <code>static</code> keyword that "
    "belongs to the <b>class itself</b>, not to any individual object instance. "
    "Static methods can be called without creating an object: "
    "<code>ClassName.methodName()</code>. They can only access other static members "
    "(static fields/methods) directly."
)

pn.code_block(
    """
// StaticMethodDemo.java
public class MathHelper {

    // Static field -- shared across all instances
    static final double PI = 3.14159;

    // Static method -- no object needed to call
    public static double circleArea(double r) {
        return PI * r * r;   // can access static PI directly
    }

    // Static method -- compute sum of integer array
    public static int arraySum(int[] arr) {
        int sum = 0;
        for (int x : arr) sum += x;
        return sum;
    }

    public static void main(String[] args) {
        // Call static methods WITHOUT creating any object
        System.out.println("Area: " + MathHelper.circleArea(5.0));  // 78.539...

        int[] nums = {10, 20, 30, 40, 50};
        System.out.println("Sum: " + MathHelper.arraySum(nums));   // 150
    }
}
""",
    lang="java",
)

pn.section("Importance of Type Casting -- Casting Various Data Types")
pn.definition(
    "<b>Type Casting:</b> The process of converting a value from one data type to another. "
    "Java supports two forms: (1) <b>Widening (Implicit/Automatic)</b> -- smaller type "
    "automatically promoted to a larger type without data loss. "
    "(2) <b>Narrowing (Explicit/Manual)</b> -- larger type explicitly cast to smaller type; "
    "possible data/precision loss."
)
pn.info_table(
    ["Type", "Direction", "Keyword", "Risk"],
    [
        [
            "Widening",
            "byte->short->int->long->float->double",
            "None (automatic)",
            "No data loss",
        ],
        [
            "Narrowing",
            "double->float->long->int->short->byte",
            "(TargetType) value",
            "Possible data loss",
        ],
    ],
)

pn.code_block(
    """
// TypeCastingDemo.java
public class TypeCastingDemo {
    public static void main(String[] args) {

        // WIDENING (Implicit) -- no cast operator needed
        int    i = 250;
        long   l = i;        // int -> long  (automatic)
        double d = l;        // long -> double (automatic)
        System.out.println("int -> long -> double: " + d);  // 250.0

        // NARROWING (Explicit) -- must write (targetType)
        double pi   = 3.14159;
        int    piInt = (int) pi;   // truncates -- decimal part LOST
        System.out.println("double -> int: " + piInt);       // 3 (not 3.14!)

        // char <-> int conversion
        char c = 'A';
        int  code = (int) c;       // char to int (Unicode value)
        System.out.println("'A' as int: " + code);           // 65

        char back = (char)(code + 1);  // 66 -> 'B'
        System.out.println("66 as char: " + back);           // B

        // byte overflow example
        int bigNum = 300;
        byte b = (byte) bigNum;    // 300 overflows byte range (-128 to 127)
        System.out.println("300 as byte: " + b);             // 44 (overflow!)
    }
}
""",
    lang="java",
)

# -----------------------------------------------------------------------------
#  Q1(c) -- 4 Marks
# -----------------------------------------------------------------------------
pn.chap_box(
    "Q1(c) [4 Marks] -- OOP Benefits | Implicit vs Explicit Type Conversion | JDK & JVM\n"
    "(May-June 2025 | July-Dec 2024 | May-June 2024)"
)

pn.section("Primary Benefits of OOP in Software Development")
pn.bullet(
    [
        "<b>Modularity (Encapsulation):</b> Code is organized into self-contained classes that "
        "bundle data and behavior. Each class can be developed, tested, and maintained "
        "independently, reducing system complexity.",
        "<b>Code Reusability (Inheritance):</b> New classes inherit existing class properties "
        "and methods using <code>extends</code>. This eliminates code duplication and accelerates "
        "development.",
        "<b>Flexibility (Polymorphism):</b> A single interface handles different underlying "
        "implementations. Programs can work with objects of different types through a common "
        "superclass reference, making systems easily extensible.",
        "<b>Data Security (Abstraction):</b> Internal implementation details are hidden from "
        "the user via abstract classes and interfaces. Users interact only with the "
        "public API, reducing accidental misuse.",
        "<b>Maintainability:</b> OOP programs are easier to modify since changes to one class "
        "do not ripple unpredictably through the entire codebase -- especially when well-designed "
        "with low coupling and high cohesion.",
    ]
)

pn.section("JDK and JVM -- Definitions")
pn.info_table(
    ["Component", "Full Form", "Definition", "Contains"],
    [
        [
            "JVM",
            "Java Virtual Machine",
            "Abstract computing machine that runs Java bytecode. Platform-dependent -- "
            "different implementations for Windows, Linux, macOS.",
            "ClassLoader, Bytecode Verifier, Interpreter, JIT Compiler, Garbage Collector",
        ],
        [
            "JDK",
            "Java Development Kit",
            "Complete software development environment for writing, compiling, and debugging "
            "Java programs. Superset of JRE.",
            "JRE + javac (compiler) + jdb (debugger) + jar (archiver) + javadoc (doc generator)",
        ],
    ],
)

pn.section("Implicit Type Conversion vs Explicit Type Casting")
pn.info_table(
    ["Property", "Implicit (Widening)", "Explicit (Narrowing)"],
    [
        [
            "Also Called",
            "Automatic / Widening conversion",
            "Manual / Narrowing / Casting",
        ],
        ["Direction", "Small -> Large data type", "Large -> Small data type"],
        [
            "Syntax Required",
            "None -- compiler handles automatically",
            "(TargetType) expression",
        ],
        [
            "Data Loss Risk",
            "None -- no data lost",
            "Possible -- truncation or overflow",
        ],
        [
            "Example",
            "int i = 10; double d = i;  // 10.0",
            "double d = 9.9; int i = (int)d;  // 9",
        ],
    ],
)

pn.code_block(
    """
// TypeConversionExample.java
public class TypeConversion {
    public static void main(String[] args) {

        // IMPLICIT (Widening) -- Java promotes automatically
        byte   b = 42;
        short  s = b;        // byte -> short (no cast needed)
        int    i = s;        // short -> int
        long   l = i;        // int -> long
        float  f = l;        // long -> float
        double d = f;        // float -> double
        System.out.println("Widened value: " + d);  // 42.0

        // EXPLICIT (Narrowing) -- programmer must explicitly cast
        double salary  = 75000.99;
        int    rounded = (int) salary;   // fractional part discarded
        System.out.println("Salary truncated: " + rounded); // 75000

        // char and int interconversion
        char grade = 'A';
        int  ascii = grade;           // implicit: char -> int
        char next  = (char)(ascii+1); // explicit: int -> char
        System.out.println("Next grade: " + next); // B

        // Type promotion in expressions
        byte x = 10, y = 20;
        // byte z = x + y;    // ERROR! x+y promoted to int in expressions
        byte z = (byte)(x + y);  // explicit cast required
        System.out.println("Byte sum: " + z);  // 30
    }
}
""",
    lang="java",
)

# -----------------------------------------------------------------------------
#  Q1(d) -- 10 Marks
# -----------------------------------------------------------------------------
pn.chap_box(
    "Q1(d) [10 Marks] -- Control Statements in Java | Calculator | Data Types Demo\n"
    "(May-June 2025 | June 2022 | July-Dec 2024 | May-June 2024)"
)

pn.section("Control Statements in Java -- Overview")
pn.definition(
    "<b>Control Statements</b> determine the flow of execution in a Java program. "
    "Without them, code executes sequentially from top to bottom. Control statements "
    "are categorized into three groups: <b>Selection</b> (conditional branching), "
    "<b>Iteration</b> (loops), and <b>Jump</b> (break, continue, return)."
)

pn.section("1. Selection Statements -- if, if-else, nested if, switch")
pn.code_block(
    """
// ControlStatementsDemo.java -- PART 1: Selection Statements
public class ControlDemo {

    // -- if-else -------------------------------------------------
    static void gradeChecker(int marks) {
        if (marks >= 90) {
            System.out.println("Grade: A (Distinction)");
        } else if (marks >= 75) {
            System.out.println("Grade: B (First Class)");
        } else if (marks >= 60) {
            System.out.println("Grade: C (Second Class)");
        } else if (marks >= 40) {
            System.out.println("Grade: D (Pass)");
        } else {
            System.out.println("Grade: F (Fail)");
        }
    }

    // -- switch statement ----------------------------------------
    static void calculator(int a, int b, char op) {
        switch (op) {
            case '+': System.out.println("Sum     : " + (a + b)); break;
            case '-': System.out.println("Difference: " + (a - b)); break;
            case '*': System.out.println("Product : " + (a * b)); break;
            case '/':
                if (b != 0)
                    System.out.println("Quotient: " + (a / b));
                else
                    System.out.println("Error: Division by zero!");
                break;
            case '%': System.out.println("Modulus : " + (a % b)); break;
            default : System.out.println("Invalid operator!");
        }
    }
""",
    lang="java",
)

pn.section("2. Iteration (Loop) Statements -- while, do-while, for, enhanced for")
pn.code_block(
    """
    // -- while loop ----------------------------------------------
    // Execute as long as condition is true; checks condition BEFORE each iteration
    static void printWhile() {
        System.out.print("while: ");
        int i = 1;
        while (i <= 5) {
            System.out.print(i + " ");
            i++;
        }
        System.out.println();
    }

    // -- do-while loop -------------------------------------------
    // Executes body AT LEAST ONCE; checks condition AFTER each iteration
    static void printDoWhile() {
        System.out.print("do-while: ");
        int i = 1;
        do {
            System.out.print(i + " ");
            i++;
        } while (i <= 5);
        System.out.println();
    }

    // -- for loop ------------------------------------------------
    // Most compact; initialization, condition, update in one line
    static void printFor() {
        System.out.print("for: ");
        for (int i = 1; i <= 5; i++) {
            System.out.print(i + " ");
        }
        System.out.println();
    }

    // -- Fibonacci using while loop -------------------------------
    static void fibonacci(int n) {
        System.out.print("Fibonacci (" + n + " terms): ");
        int a = 0, b = 1, count = 0;
        while (count < n) {
            System.out.print(a + " ");
            int temp = a + b;
            a = b;
            b = temp;
            count++;
        }
        System.out.println();
    }

    // -- enhanced for (for-each) ---------------------------------
    static void sumArray(int[] arr) {
        int sum = 0;
        for (int x : arr) sum += x;
        System.out.println("Array sum: " + sum);
    }
""",
    lang="java",
)

pn.section("3. Jump Statements -- break, continue, return")
pn.code_block(
    """
    // -- break statement -----------------------------------------
    // Exits the nearest enclosing loop or switch
    static void breakDemo() {
        System.out.print("break demo: ");
        for (int i = 1; i <= 10; i++) {
            if (i == 6) break;   // exit loop when i reaches 6
            System.out.print(i + " ");
        }
        System.out.println();   // prints: 1 2 3 4 5
    }

    // -- continue statement --------------------------------------
    // Skips the rest of the current iteration and continues with next
    static void continueDemo() {
        System.out.print("continue (skip evens): ");
        for (int i = 1; i <= 10; i++) {
            if (i % 2 == 0) continue;  // skip even numbers
            System.out.print(i + " ");
        }
        System.out.println();   // prints: 1 3 5 7 9
    }

    // -- return statement ----------------------------------------
    // Exits the current method and optionally returns a value
    static int factorial(int n) {
        if (n < 0) return -1;   // early return for invalid input
        if (n == 0 || n == 1) return 1;
        return n * factorial(n - 1);  // recursive return
    }

    // -- main method ---------------------------------------------
    public static void main(String[] args) {
        gradeChecker(85);        // Grade: B
        calculator(10, 3, '/');  // Quotient: 3
        printWhile();
        printDoWhile();
        printFor();
        fibonacci(8);            // 0 1 1 2 3 5 8 13
        sumArray(new int[]{10, 20, 30, 40, 50});
        breakDemo();
        continueDemo();
        System.out.println("5! = " + factorial(5));  // 120
    }
}
""",
    lang="java",
)

pn.section("Java Data Types Demonstration Program")
pn.code_block(
    """
// DataTypesDemo.java -- Demonstrates all 8 primitive Java data types
public class DataTypesDemo {
    public static void main(String[] args) {

        // Integer types
        byte  byteVal  = 127;             // 8-bit: -128 to 127
        short shortVal = 32767;           // 16-bit: -32768 to 32767
        int   intVal   = 2_147_483_647;   // 32-bit (underscores allowed in Java 7+)
        long  longVal  = 9_223_372_036L;  // 64-bit, L suffix required

        // Floating-point types
        float  floatVal  = 3.14159f;      // 32-bit IEEE 754, f suffix required
        double doubleVal = 2.718281828;   // 64-bit (default for decimal literals)

        // Character type
        char charVal = 'J';               // 16-bit Unicode character

        // Boolean type
        boolean boolVal = true;           // only true or false

        System.out.printf("byte:    %d%n",   byteVal);
        System.out.printf("short:   %d%n",   shortVal);
        System.out.printf("int:     %d%n",   intVal);
        System.out.printf("long:    %d%n",   longVal);
        System.out.printf("float:   %.5f%n", floatVal);
        System.out.printf("double:  %.9f%n", doubleVal);
        System.out.printf("char:    %c%n",   charVal);
        System.out.printf("boolean: %b%n",   boolVal);

        // B.Tech Marksheet using control statements
        System.out.println("\n=== B.Tech Semester Marksheet ===");
        String name = "Arjun Sharma";
        int[] marks = {85, 72, 90, 68, 55};
        String[] subjects = {"Maths", "Physics", "Java", "DBMS", "OS"};
        int total = 0;
        for (int i = 0; i < marks.length; i++) {
            String grade;
            if      (marks[i] >= 90) grade = "A+";
            else if (marks[i] >= 80) grade = "A";
            else if (marks[i] >= 70) grade = "B";
            else if (marks[i] >= 60) grade = "C";
            else if (marks[i] >= 50) grade = "D";
            else                     grade = "F";
            System.out.printf("%-10s: %3d  Grade: %s%n", subjects[i], marks[i], grade);
            total += marks[i];
        }
        double avg = (double) total / marks.length;
        System.out.printf("Total: %d | Average: %.2f%n", total, avg);
        System.out.println(avg >= 60 ? "Result: PASS" : "Result: FAIL");
    }
}
""",
    lang="java",
)

pn.tip(
    "Control Statement exam tip: Know the THREE categories -- Selection (if/switch), "
    "Iteration (while/do-while/for), Jump (break/continue/return). "
    "do-while executes MINIMUM ONCE even if condition is false. "
    "break exits the loop; continue skips to the next iteration."
)

# -----------------------------------------------------------------------------
#  Q1(e) -- 10 Marks
# -----------------------------------------------------------------------------
pn.chap_box(
    "Q1(e) [10 Marks] -- Complete Java Program Lifecycle | final, static, this Keywords | OOP Features\n"
    "(May-June 2025 | July-Dec 2024 | June 2022 | May-June 2024)"
)

pn.section("Complete Lifecycle of a Java Program (Source to Execution)")
pn.body(
    "The journey of a Java program from the programmer's text editor to actual execution "
    "on the CPU involves five major phases, each with distinct tools and responsibilities."
)

pn.info_table(
    ["Phase", "Tool / Actor", "Input", "Output"],
    [
        [
            "1. Authoring",
            "Programmer / IDE",
            "Idea / Requirements",
            "ClassName.java (source file)",
        ],
        [
            "2. Compilation",
            "javac compiler",
            "ClassName.java",
            "ClassName.class (bytecode)",
        ],
        [
            "3. Class Loading",
            "JVM ClassLoader",
            "ClassName.class",
            "Loaded class in JVM memory",
        ],
        [
            "4. Bytecode Verification",
            "JVM Verifier",
            "Loaded bytecode",
            "Verified safe bytecode",
        ],
        [
            "5. Execution",
            "JVM Interpreter + JIT",
            "Verified bytecode",
            "Program output on OS",
        ],
    ],
)

net_lifecycle = pd.NetworkDiagram(
    width=pn.CW,
    height=260,
    theme=diag_theme,
    caption="Fig 1.1: Complete Java Program Lifecycle -- Source Code to Machine Execution",
)
# Row 1 (top): write -> compile -> bytecode
net_lifecycle.node("src", "HelloWorld.java\n(Source Code)", x=65, y=80, kind="host")
net_lifecycle.node("javac", "javac\n(Compiler)", x=210, y=80, kind="server")
net_lifecycle.node("bc", "HelloWorld.class\n(Bytecode)", x=370, y=80, kind="storage")
# Row 2 (bottom): classloader -> JVM exec -> output
net_lifecycle.node("cl", "JVM ClassLoader\n+ Verifier", x=130, y=185, kind="generic")
net_lifecycle.node(
    "exec", "Interpreter / JIT\n+ GC + Memory", x=290, y=185, kind="server"
)
net_lifecycle.node("out", "Program Output\n(OS / Console)", x=415, y=185, kind="cloud")

net_lifecycle.link("src", "javac", bidirectional=False)
net_lifecycle.link("javac", "bc", bidirectional=False)
net_lifecycle.link("bc", "cl", bidirectional=False, label="load")
net_lifecycle.link("cl", "exec", bidirectional=False)
net_lifecycle.link("exec", "out", bidirectional=False)
pn.story.extend(net_lifecycle.as_flowable())

pn.section("Role of final, static, and this Keywords")
pn.info_table(
    ["Keyword", "Role / Purpose", "Usage Context"],
    [
        [
            "final",
            "Makes entities immutable/non-overridable. "
            "final variable = constant (cannot reassign). "
            "final method = cannot be overridden by subclass. "
            "final class = cannot be extended (e.g., java.lang.String).",
            "Variables, methods, classes",
        ],
        [
            "static",
            "Makes a member belong to the CLASS rather than an object instance. "
            "static variable = shared by all objects. "
            "static method = callable without creating object. "
            "static block = runs once when class is loaded.",
            "Variables, methods, blocks, nested classes",
        ],
        [
            "this",
            "A reference to the CURRENT object. "
            "Disambiguates instance variables from local variables with same name. "
            "this() in constructor = calls another constructor in same class (chaining). "
            "Can be returned from method for fluent/builder pattern.",
            "Instance methods, constructors",
        ],
    ],
)

pn.code_block(
    """
// KeywordsDemo.java -- demonstrates final, static, and this in one program
public class BankAccount {

    // static field -- shared by ALL BankAccount objects
    static int totalAccounts = 0;
    static final String BANK_NAME = "UIT Bank";  // final static = class-level constant

    // Instance fields
    private final int accountNumber;   // final instance field -- set once in constructor
    private String    holderName;
    private double    balance;

    // CONSTRUCTOR -- uses 'this' to disambiguate and static field
    BankAccount(String holderName, double initialDeposit) {
        totalAccounts++;                        // static -- increment for each new account
        this.accountNumber = totalAccounts;     // final -- set exactly once
        this.holderName    = holderName;        // this.field vs local parameter
        this.balance       = initialDeposit;
    }

    // Chained constructor using this()
    BankAccount(String holderName) {
        this(holderName, 0.0);  // delegate to 2-arg constructor
    }

    // static method -- can be called as BankAccount.getBankName()
    static String getBankName() {
        return BANK_NAME;  // can only access static members
    }

    void deposit(double amount) {
        this.balance += amount;
    }

    void display() {
        System.out.printf("[%s] Account #%d | %s | Balance: %.2f%n",
            BANK_NAME, accountNumber, holderName, balance);
    }

    public static void main(String[] args) {
        System.out.println("Bank: " + BankAccount.getBankName());

        BankAccount a1 = new BankAccount("Priya", 5000.0);
        BankAccount a2 = new BankAccount("Rahul");
        BankAccount a3 = new BankAccount("Divya", 15000.0);

        a1.deposit(2500.0);
        a1.display();
        a2.display();
        a3.display();

        System.out.println("Total accounts opened: " + BankAccount.totalAccounts);
        // a1.accountNumber = 99;  // COMPILE ERROR: final cannot be reassigned
    }
}
""",
    lang="java",
)

pn.section("OOP Features in Java -- Comprehensive Examples")
pn.body(
    "Java implements all four OOP pillars. Below is a demonstration showing "
    "encapsulation, inheritance, polymorphism, and abstraction working together."
)
pn.code_block(
    """
// OOPFeaturesDemo.java -- All four OOP pillars in one example

// ABSTRACTION -- abstract class hides internal details
abstract class Animal {
    private String name;   // ENCAPSULATION -- private data

    Animal(String name) { this.name = name; }

    // Public getter -- controlled access to private field
    public String getName() { return name; }

    // Abstract method -- subclasses MUST override
    abstract void speak();

    // Concrete shared method
    void breathe() { System.out.println(name + " breathes air."); }
}

// INHERITANCE -- Dog inherits from Animal
class Dog extends Animal {
    Dog(String name) { super(name); }

    @Override  // POLYMORPHISM -- runtime method overriding
    public void speak() { System.out.println(getName() + " says: Woof!"); }
}

// INHERITANCE -- Cat inherits from Animal
class Cat extends Animal {
    Cat(String name) { super(name); }

    @Override  // POLYMORPHISM -- different implementation, same method name
    public void speak() { System.out.println(getName() + " says: Meow!"); }
}

public class OOPFeaturesDemo {
    public static void main(String[] args) {
        // POLYMORPHISM -- Animal reference holds Dog/Cat objects
        Animal[] animals = { new Dog("Rex"), new Cat("Whiskers"), new Dog("Bruno") };

        for (Animal a : animals) {
            a.speak();     // dynamic dispatch -- correct method called at runtime
            a.breathe();
        }

        // ENCAPSULATION -- can only access 'name' through public getter
        System.out.println("First animal: " + animals[0].getName());
        // animals[0].name = "Hacked";  // COMPILE ERROR: name is private
    }
}
""",
    lang="java",
)

pn.tip(
    "Q1(e) exam tip: Java Lifecycle = Write -> Compile (javac) -> Load -> Verify -> Execute. "
    "final = constant/non-overridable/non-extendable. "
    "static = class-level (shared, no object needed). "
    "this = current object reference. "
    "OOP pillars: Encapsulation + Inheritance + Polymorphism + Abstraction."
)
pn.br()

# #############################################################################
#  QUESTION 2 -- CO2: OOP, CLASSES, PACKAGES, INTERFACES, EXCEPTIONS, THREADS
# #############################################################################
pn.part_box(
    "QUESTION 2 -- CO2: OOP, CLASSES, PACKAGES, INTERFACES, EXCEPTIONS & THREADS"
)

# -----------------------------------------------------------------------------
#  Q2(a) -- 3 Marks
# -----------------------------------------------------------------------------
pn.chap_box(
    "Q2(a) [3 Marks] -- abstract Keyword | Garbage Collection | Class and Object\n"
    "(May-June 2025 | June 2022 | July-Dec 2024 | May-June 2024)"
)

pn.section("The abstract Keyword -- Cannot be Instantiated")
pn.definition(
    "The keyword that declares a class that <b>cannot be instantiated</b> and may contain "
    "methods without implementation (abstract methods) is <code><b>abstract</b></code>. "
    "An <b>abstract class</b> serves as an incomplete blueprint. It can have both fully "
    "implemented (concrete) methods and body-less (abstract) methods. Subclasses that "
    "extend it must provide implementations for all abstract methods, or they must also "
    "be declared abstract."
)
pn.code_block(
    """
abstract class Shape {           // cannot do: new Shape()
    abstract double area();      // no body -- subclass must implement
    void printInfo() {           // concrete method -- has body
        System.out.println("Area = " + area());
    }
}
class Circle extends Shape {
    double r;
    Circle(double r) { this.r = r; }
    @Override
    double area() { return Math.PI * r * r; }  // must implement abstract method
}
""",
    lang="java",
)

pn.section("Garbage Collection in Java")
pn.definition(
    "<b>Garbage Collection (GC):</b> Java's automatic memory management mechanism. "
    "The JVM's Garbage Collector runs as a background daemon thread and automatically "
    "identifies heap objects that have no active references pointing to them (unreachable "
    "objects) and reclaims their memory. This eliminates the need for manual "
    "<code>free()</code> calls (as required in C/C++)."
)
pn.bullet(
    [
        "<b>When eligible:</b> Object's reference set to null, goes out of scope, or is overwritten.",
        "<b>System.gc():</b> Hints JVM to run GC -- not guaranteed to execute immediately.",
        "<b>finalize():</b> Called by GC before reclaiming -- deprecated in Java 9+.",
        "<b>Algorithms:</b> Mark-and-Sweep, Generational GC (Young/Old Generation).",
    ]
)

pn.section("Demonstrating Class and Object in Java")
pn.code_block(
    """
// ClassAndObjectDemo.java
class Student {                    // CLASS -- blueprint/template
    String name;                   // instance variable (field)
    int    rollNo;
    double marks;

    // Method -- behavior of the object
    void display() {
        System.out.printf("Roll: %d | Name: %-15s | Marks: %.1f%n",
                          rollNo, name, marks);
    }
}

public class ClassAndObjectDemo {
    public static void main(String[] args) {
        // Creating OBJECTS (instances) from the class blueprint
        Student s1 = new Student();  // s1 is a reference; new Student() = heap object
        s1.name   = "Priya Sharma";
        s1.rollNo = 101;
        s1.marks  = 88.5;

        Student s2 = new Student();  // second independent object
        s2.name   = "Rahul Verma";
        s2.rollNo = 102;
        s2.marks  = 75.0;

        s1.display();  // Roll: 101 | Name: Priya Sharma    | Marks: 88.5
        s2.display();  // Roll: 102 | Name: Rahul Verma     | Marks: 75.0
    }
}
""",
    lang="java",
)

# -----------------------------------------------------------------------------
#  Q2(b) -- 4 Marks
# -----------------------------------------------------------------------------
pn.chap_box(
    "Q2(b) [4 Marks] -- Inheritance in Java | Packages (mypackage) | Constructors | Garbage Collection\n"
    "(May-June 2025 | July-Dec 2024 | June 2022 | May-June 2024)"
)

pn.section("Core Concept of Inheritance in Java")
pn.definition(
    "<b>Inheritance:</b> A fundamental OOP mechanism by which a new class (subclass/child class) "
    "acquires the properties (fields) and behaviors (methods) of an existing class "
    "(superclass/parent class). The <code><b>extends</b></code> keyword establishes the "
    "inheritance relationship. Inheritance promotes <b>code reusability</b> and establishes "
    "an <b>IS-A relationship</b> between classes."
)
pn.bullet(
    [
        "<b>Single Inheritance:</b> One subclass extends one superclass (A extends B).",
        "<b>Multilevel Inheritance:</b> Chain of inheritance (A -> B -> C).",
        "<b>Hierarchical Inheritance:</b> Multiple subclasses extend one superclass.",
        "<b>super keyword:</b> Refers to the parent class -- used to call parent constructor "
        "(<code>super()</code>) or parent method (<code>super.methodName()</code>).",
        "<b>Method Overriding:</b> Subclass provides its own implementation of a parent method "
        "-- same signature, @Override annotation recommended.",
    ]
)

pn.section("Constructors -- Definition and Need")
pn.definition(
    "<b>Constructor:</b> A special block of code that is automatically invoked when an "
    "object is created using <code>new</code>. It initializes the object's state. "
    "A constructor MUST have the same name as the class and has NO return type (not even void). "
    "<b>Why needed?</b> Without constructors, all fields would have default values (0, null, false) "
    "and objects could not be created in a meaningful initial state."
)

pn.section("Creating Package mypackage with Classes Hello and Farewell")
pn.code_block(
    """
// -- File: mypackage/Hello.java ----------------------------------------------
package mypackage;   // STEP 1: Declare the package (first statement in file)

public class Hello {

    private String personName;

    // Default constructor
    public Hello() {
        this.personName = "World";
    }

    // Parameterized constructor
    public Hello(String name) {
        this.personName = name;
    }

    // greet() method as required
    public void greet() {
        System.out.println("Hello, " + personName + "! Welcome to UIT-RGPV.");
    }

    // Static utility method
    public static void greetAll() {
        System.out.println("Hello, everyone! Welcome to Java Programming.");
    }
}

// -- File: mypackage/Farewell.java ------------------------------------------
package mypackage;

public class Farewell {

    private String personName;

    public Farewell(String name) {
        this.personName = name;
    }

    public void sayBye() {
        System.out.println("Goodbye, " + personName + "! Have a great day.");
    }
}

// -- File: PackageDemo.java (in parent directory, outside mypackage) ---------
import mypackage.Hello;           // STEP 2: Import class from package
import mypackage.Farewell;

public class PackageDemo {
    public static void main(String[] args) {

        // Using Hello class with default constructor
        Hello h1 = new Hello();
        h1.greet();                      // Hello, World! ...

        // Using Hello with parameterized constructor
        Hello h2 = new Hello("Priya");
        h2.greet();                      // Hello, Priya! ...

        // Static method -- no object needed
        Hello.greetAll();

        // Using Farewell class
        Farewell f = new Farewell("Rahul");
        f.sayBye();                      // Goodbye, Rahul! ...
    }
}

// COMPILE AND RUN STEPS:
// 1. Ensure directory structure:  PackageDemo.java  and  mypackage/Hello.java  mypackage/Farewell.java
// 2. javac mypackage/Hello.java mypackage/Farewell.java
// 3. javac PackageDemo.java
// 4. java PackageDemo
""",
    lang="java",
)

pn.tip(
    "Package exam tips: 'package' statement MUST be the first line (before imports). "
    "Class accessing another package must import it. "
    "Directory structure must match package hierarchy. "
    "public members are accessible outside the package."
)

# -----------------------------------------------------------------------------
#  Q2(c) -- 4 Marks
# -----------------------------------------------------------------------------
pn.chap_box(
    "Q2(c) [4 Marks] -- Exception Handling Goal | Constructors Demo | Interfaces vs Classes | Packages\n"
    "(May-June 2025 | July-Dec 2024 | June 2022 | May-June 2024)"
)

pn.section("Main Goal of Exception Handling")
pn.definition(
    "<b>Exception Handling:</b> The main goal is to <b>maintain normal program flow</b> "
    "even when runtime errors occur, and to provide a structured mechanism to detect, "
    "report, and recover from unexpected runtime conditions (exceptions) without crashing "
    "the program. Java uses try-catch-finally blocks with throw/throws keywords to achieve "
    "robust, fault-tolerant programs."
)
pn.bullet(
    [
        "<b>try block:</b> Contains code that might throw an exception.",
        "<b>catch block:</b> Handles the specific exception type thrown.",
        "<b>finally block:</b> Always executes (cleanup code) -- even if exception occurs.",
        "<b>throw:</b> Manually throw an exception object.",
        "<b>throws:</b> Declares checked exceptions that a method may throw.",
    ]
)

pn.section("Parameterized and Default Constructors -- Demonstration")
pn.code_block(
    """
// ConstructorTypesDemo.java
class Rectangle {

    double length;
    double width;

    // -- DEFAULT CONSTRUCTOR (no parameters) ------------------------------
    // Called when: Rectangle r = new Rectangle();
    // Purpose: Initialize with default/zero values
    Rectangle() {
        this.length = 1.0;   // default 1x1 unit rectangle
        this.width  = 1.0;
        System.out.println("Default constructor: 1x1 rectangle created.");
    }

    // -- PARAMETERIZED CONSTRUCTOR ----------------------------------------
    // Called when: Rectangle r = new Rectangle(5.0, 3.0);
    // Purpose: Initialize with caller-specified values
    Rectangle(double length, double width) {
        this.length = length;
        this.width  = width;
        System.out.println("Parameterized constructor: " + length + "x" + width);
    }

    // -- COPY CONSTRUCTOR -------------------------------------------------
    Rectangle(Rectangle other) {
        this.length = other.length;
        this.width  = other.width;
        System.out.println("Copy constructor: copied " + length + "x" + width);
    }

    double area()      { return length * width; }
    double perimeter() { return 2 * (length + width); }

    void display() {
        System.out.printf("  Length=%.1f  Width=%.1f  Area=%.1f  Perimeter=%.1f%n",
                           length, width, area(), perimeter());
    }
}

public class ConstructorTypesDemo {
    public static void main(String[] args) {
        Rectangle r1 = new Rectangle();           // default
        r1.display();

        Rectangle r2 = new Rectangle(8.0, 5.0);  // parameterized
        r2.display();

        Rectangle r3 = new Rectangle(r2);         // copy
        r3.display();
        r3.length = 100.0;   // modifying r3 does NOT affect r2
        System.out.println("r2 length unchanged: " + r2.length);
    }
}
""",
    lang="java",
)

pn.section("Four Similarities Between Interfaces and Classes")
pn.info_table(
    ["#", "Similarity", "Description"],
    [
        [
            "1",
            "Both are Reference Types",
            "Both Class and Interface names can be used as reference variable types. "
            "e.g., List<String> list = new ArrayList<>(); (List is an interface used as reference type)",
        ],
        [
            "2",
            "Both define method signatures",
            "Both can declare methods. Classes provide implementations; interfaces provide "
            "default/static methods (Java 8+) plus abstract method declarations.",
        ],
        [
            "3",
            "Both can have constants",
            "Both can define constant fields. Interface fields are implicitly "
            "public static final. Class fields can be explicitly declared final static.",
        ],
        [
            "4",
            "Both support inheritance hierarchy",
            "Classes extend one class; interfaces can extend multiple interfaces. "
            "Both participate in Java's type hierarchy rooted at java.lang.Object.",
        ],
    ],
)

pn.section("Creating a Package in Java -- Step-by-Step")
pn.bullet(
    [
        "<b>Step 1:</b> Add <code>package packagename;</code> as the very first statement in the Java source file.",
        "<b>Step 2:</b> Create a directory with the SAME name as the package (case-sensitive).",
        "<b>Step 3:</b> Save the .java file inside that directory.",
        "<b>Step 4:</b> Compile from the parent directory: <code>javac packagename/ClassName.java</code>",
        "<b>Step 5:</b> In the calling program, import using: <code>import packagename.ClassName;</code> or <code>import packagename.*;</code>",
        "<b>Step 6:</b> Compile and run the calling program from the parent directory: <code>java CallingClass</code>",
    ]
)

# -----------------------------------------------------------------------------
#  Q2(d) -- 10 Marks
# -----------------------------------------------------------------------------
pn.chap_box(
    "Q2(d) [10 Marks] -- Advantages of Packages | Inheritance Types | Multiple Inheritance Workaround\n"
    "(May-June 2025 | June 2022 | May-June 2024 | July-Dec 2024)"
)

pn.section("Advantages of Packages in Java")
pn.bullet(
    [
        "<b>Naming Conflict Prevention:</b> Two classes can have the same name in different packages. "
        "e.g., <code>java.util.Date</code> and <code>java.sql.Date</code> coexist without conflict.",
        "<b>Code Organization:</b> Related classes are grouped logically. e.g., all I/O classes "
        "in <code>java.io</code>, all collections in <code>java.util</code>.",
        "<b>Access Control:</b> Package-level (default) access allows classes in the same package "
        "to share internals while hiding them from other packages.",
        "<b>Reusability:</b> Packaged classes can be easily imported and reused across projects. "
        "JAR files bundle packages for distribution.",
        "<b>Maintainability:</b> Separating concerns into packages makes large codebases easier "
        "to navigate and maintain.",
    ]
)

pn.code_block(
    """
// Package organization demo -- showing how packages prevent naming conflicts
// -------------------------------------------------------------------------
// college/academic/Student.java
package college.academic;
public class Student {
    private String name;
    private String major;
    public Student(String name, String major) {
        this.name = name;  this.major = major;
    }
    public void display() {
        System.out.println("[Academic] Student: " + name + " | Major: " + major);
    }
}

// college/sports/Student.java  -- SAME class name, different package!
package college.sports;
public class Student {
    private String name;
    private String sport;
    public Student(String name, String sport) {
        this.name = name;  this.sport = sport;
    }
    public void display() {
        System.out.println("[Sports]   Student: " + name + " | Sport: " + sport);
    }
}

// Main.java (demonstrates package access control)
import college.academic.Student;                // Specific import
// import college.sports.Student; // would conflict -- use fully qualified name

public class Main {
    public static void main(String[] args) {
        Student acad = new Student("Priya", "Computer Science");
        acad.display();

        // Access sports Student via fully qualified name to avoid conflict
        college.sports.Student sports = new college.sports.Student("Rahul", "Cricket");
        sports.display();
    }
}
""",
    lang="java",
)

pn.section("Types of Inheritance in Java")

net_inh = pd.NetworkDiagram(
    width=pn.CW,
    height=370,
    theme=diag_theme,
    caption="Fig 2.1: Types of Inheritance supported in Java (Multiple inheritance via Interface only)",
)
# --- Column 1: Single + Multilevel chain ---
# A at top, B shifted LEFT and below, C1 further below -- staircase left layout
net_inh.node("A", "Class A\n(Parent)", x=70, y=60, kind="server")
net_inh.node("B", "Class B\n(Child of A)", x=40, y=190, kind="database")
net_inh.node("C1", "Class C\n(Child of B)", x=70, y=320, kind="database")

# --- Column 2: Hierarchical -- D at top, E (left) and F (right) below ---
net_inh.node("D", "Class D\n(Parent)", x=235, y=60, kind="server")
net_inh.node("E", "Class E\n(Child 1)", x=165, y=190, kind="database")
net_inh.node("F", "Class F\n(Child 2)", x=305, y=190, kind="database")

# --- Column 3: Multiple via Interfaces -- IA and IB at top, G below ---
net_inh.node("IA", "Interface A", x=375, y=60, kind="generic")
net_inh.node("IB", "Interface B", x=435, y=60, kind="generic")
net_inh.node("G", "Class G\nimplements\nA, B", x=405, y=210, kind="database")

net_inh.link("A", "B", label="Single")
net_inh.link("B", "C1", label="Multilevel")
net_inh.link("D", "E", label="Hierarchical")
net_inh.link("D", "F", label="Hierarchical")
net_inh.link("IA", "G", label="implements")
net_inh.link("IB", "G", label="implements")
pn.story.extend(net_inh.as_flowable())

pn.info_table(
    ["Inheritance Type", "Java Support", "Description & Example"],
    [
        [
            "Single",
            "YES (extends)",
            "One subclass inherits one superclass. class Dog extends Animal {}",
        ],
        [
            "Multilevel",
            "YES (extends chain)",
            "Chain: A -> B -> C. class C extends B {} where B extends A {}",
        ],
        [
            "Hierarchical",
            "YES",
            "Multiple subclasses inherit one superclass. class Dog extends Animal, class Cat extends Animal.",
        ],
        [
            "Multiple (via classes)",
            "NO -- not supported",
            "Java does NOT allow class C extends A, B {}. Causes Diamond Problem ambiguity.",
        ],
        [
            "Multiple (via interfaces)",
            "YES (implements)",
            "class Liger implements Lion, Tiger {}. Interface default methods handle ambiguity.",
        ],
        [
            "Hybrid",
            "Partial (via interfaces)",
            "Combination of types. Supported only through interfaces to avoid diamond problem.",
        ],
    ],
)

pn.section("Why Multiple Inheritance is Excluded -- The Diamond Problem")
pn.body(
    "Java deliberately excludes multiple class inheritance to avoid the "
    "<b>Diamond Problem</b>: if class C inherits from both A and B, and both A and B "
    "override the same method from a common ancestor, the JVM cannot determine which "
    "version of the method class C should inherit. "
    "The solution is to use <b>interfaces</b> -- a class can implement multiple interfaces."
)

pn.code_block(
    """
// MultipleInheritanceViaInterfaces.java
// Demonstrating Lion, Tiger, Liger example (interface-based multiple inheritance)

interface Lion {
    default void roar()  { System.out.println("Lion: ROARR!"); }
    void hunt();          // abstract method
}

interface Tiger {
    default void roar()  { System.out.println("Tiger: ROOAARR!"); }
    void swim();          // abstract method
}

// Liger IMPLEMENTS both Lion and Tiger
class Liger implements Lion, Tiger {

    // MUST override roar() because BOTH Lion and Tiger have default roar()
    // -- compiler forces resolution of the ambiguity
    @Override
    public void roar() {
        Lion.super.roar();    // explicitly call Lion's version
        Tiger.super.roar();   // also call Tiger's version (Liger has both abilities!)
        System.out.println("Liger: ROOOOARRR! (Hybrid roar)");
    }

    @Override
    public void hunt() { System.out.println("Liger: Hunting like a lion."); }

    @Override
    public void swim() { System.out.println("Liger: Swimming like a tiger."); }
}

// Polymorphism via multiple interfaces
public class MultipleInheritanceDemo {
    public static void main(String[] args) {
        Liger liger = new Liger();
        liger.roar();   // calls overridden method
        liger.hunt();
        liger.swim();

        Lion  l = liger;   // Liger IS-A Lion
        Tiger t = liger;   // Liger IS-A Tiger
        l.hunt();
        t.swim();
    }
}
""",
    lang="java",
)

# -----------------------------------------------------------------------------
#  Q2(e) -- 10 Marks
# -----------------------------------------------------------------------------
pn.chap_box(
    "Q2(e) [10 Marks] -- Student Class Design | Threads (Thread & Runnable) | Exception Handling | Polymorphism\n"
    "(May-June 2025 | July-Dec 2024 | June 2022 | May-June 2024)"
)

pn.section("Student Class with Default and Parameterized Constructors")
pn.code_block(
    """
// Student.java -- Complete Student class with both constructor types
public class Student {

    // Instance variables (fields)
    private String name;
    private String studentId;
    private String major;
    private double cgpa;

    // -- DEFAULT CONSTRUCTOR ----------------------------------------------
    public Student() {
        this.name      = "Unknown";
        this.studentId = "S000";
        this.major     = "Undeclared";
        this.cgpa      = 0.0;
        System.out.println("[Default Constructor] Student object created with defaults.");
    }

    // -- PARAMETERIZED CONSTRUCTOR ----------------------------------------
    public Student(String name, String studentId, String major, double cgpa) {
        this.name      = name;
        this.studentId = studentId;
        this.major     = major;
        this.cgpa      = cgpa;
        System.out.println("[Parameterized Constructor] Student: " + name + " created.");
    }

    // Getters and Setters (Encapsulation)
    public String getName()      { return name; }
    public String getStudentId() { return studentId; }
    public String getMajor()     { return major; }
    public double getCgpa()      { return cgpa; }

    public void setMajor(String major) { this.major = major; }
    public void setCgpa(double cgpa)   {
        if (cgpa >= 0.0 && cgpa <= 10.0) this.cgpa = cgpa;
        else System.out.println("Invalid CGPA value.");
    }

    public void display() {
        System.out.printf("ID: %-6s | Name: %-20s | Major: %-25s | CGPA: %.2f%n",
                           studentId, name, major, cgpa);
    }

    public static void main(String[] args) {
        // Declare and create using DEFAULT constructor
        Student s1 = new Student();
        s1.display();

        // Modify via setters
        s1.setMajor("Computer Science");
        s1.setCgpa(7.5);

        // Declare and create using PARAMETERIZED constructor
        Student s2 = new Student("Priya Sharma", "S101", "Information Technology", 8.75);
        Student s3 = new Student("Rahul Verma",  "S102", "Electronics Engineering",  7.20);

        System.out.println("\\n=== Student Records ===");
        s1.display();
        s2.display();
        s3.display();
    }
}
""",
    lang="java",
)

pn.section("Exception Handling -- Comprehensive Demonstration")
pn.code_block(
    """
// ExceptionHandlingDemo.java
public class ExceptionHandlingDemo {

    // Custom (user-defined) exception
    static class InsufficientFundsException extends Exception {
        double shortfall;
        InsufficientFundsException(double shortfall) {
            super("Insufficient funds! Short by: " + shortfall);
            this.shortfall = shortfall;
        }
    }

    static double balance = 5000.0;

    // Method declares checked exception with 'throws'
    static void withdraw(double amount) throws InsufficientFundsException {
        if (amount > balance) {
            throw new InsufficientFundsException(amount - balance); // throw exception
        }
        balance -= amount;
        System.out.println("Withdrawn: " + amount + " | Remaining: " + balance);
    }

    public static void main(String[] args) {

        // --- Handling Arithmetic Exception ---
        try {
            int result = 100 / 0;   // throws ArithmeticException
        } catch (ArithmeticException e) {
            System.out.println("Caught: " + e.getMessage());  // / by zero
        } finally {
            System.out.println("Finally always runs (cleanup here).");
        }

        // --- Handling ArrayIndexOutOfBounds ---
        int[] arr = {10, 20, 30};
        try {
            System.out.println(arr[5]);   // index 5 doesn't exist
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Array error: " + e.getMessage());
        }

        // --- Handling custom exception ---
        try {
            withdraw(3000.0);   // OK
            withdraw(3000.0);   // will fail -- only 2000 left
        } catch (InsufficientFundsException e) {
            System.out.println("Bank error: " + e.getMessage());
            System.out.println("Need extra: " + e.shortfall);
        }

        // --- Multiple catch blocks ---
        try {
            String s = null;
            s.length();   // NullPointerException
        } catch (NullPointerException e) {
            System.out.println("Null error: " + e.getClass().getSimpleName());
        } catch (Exception e) {
            System.out.println("Generic error: " + e.getMessage());
        }
    }
}
""",
    lang="java",
)

pn.section("Two Threads -- Thread Class vs Runnable Interface")
pn.code_block(
    """
// ThreadsDemo.java -- Two threads simultaneously: one via Thread, one via Runnable

// Method 1: Extending Thread class
class CountdownThread extends Thread {
    String name;
    CountdownThread(String name) {
        this.name = name;
        setName(name);  // set thread name
    }
    @Override
    public void run() {
        for (int i = 5; i >= 1; i--) {
            System.out.println("[" + name + "] Count: " + i);
            try { Thread.sleep(400); } catch (InterruptedException e) { return; }
        }
        System.out.println("[" + name + "] Countdown complete!");
    }
}

// Method 2: Implementing Runnable interface
class MessagePrinter implements Runnable {
    String message;
    MessagePrinter(String message) { this.message = message; }

    @Override
    public void run() {
        for (int i = 1; i <= 5; i++) {
            System.out.println("[Runnable] " + message + " (" + i + ")");
            try { Thread.sleep(300); } catch (InterruptedException e) { return; }
        }
    }
}

public class ThreadsDemo {
    public static void main(String[] args) throws InterruptedException {
        System.out.println("Starting two threads simultaneously...");

        // Thread 1: extends Thread
        CountdownThread t1 = new CountdownThread("CountdownThread");

        // Thread 2: implements Runnable (passed to Thread constructor)
        MessagePrinter printer = new MessagePrinter("Hello from Runnable!");
        Thread t2 = new Thread(printer, "RunnableThread");

        // Start both threads -- they run CONCURRENTLY
        t1.start();
        t2.start();

        // Wait for both to complete before main continues
        t1.join();
        t2.join();

        System.out.println("Both threads completed. Main thread exits.");
    }
}
""",
    lang="java",
)

pn.section("Polymorphism -- Types and Demonstration")
pn.code_block(
    """
// PolymorphismDemo.java -- Compile-time (Overloading) and Runtime (Overriding)

class Calculator {
    // COMPILE-TIME POLYMORPHISM (Method Overloading)
    int    add(int a, int b)          { return a + b; }
    double add(double a, double b)    { return a + b; }
    int    add(int a, int b, int c)   { return a + b + c; }
    String add(String a, String b)    { return a + b; }  // string concatenation
}

class Shape {
    double area() { return 0; }   // base implementation
    String name()  { return "Shape"; }
}
class Circle extends Shape {
    double radius;
    Circle(double r) { this.radius = r; }
    @Override double area() { return Math.PI * radius * radius; }
    @Override String name()  { return "Circle(r=" + radius + ")"; }
}
class Rectangle extends Shape {
    double w, h;
    Rectangle(double w, double h) { this.w = w; this.h = h; }
    @Override double area() { return w * h; }
    @Override String name()  { return "Rectangle(" + w + "x" + h + ")"; }
}

public class PolymorphismDemo {
    public static void main(String[] args) {
        Calculator c = new Calculator();
        System.out.println(c.add(3, 4));         // int overload -> 7
        System.out.println(c.add(1.5, 2.5));     // double overload -> 4.0
        System.out.println(c.add("Java", "!"));  // String overload -> Java!

        // RUNTIME POLYMORPHISM (Method Overriding)
        Shape[] shapes = { new Circle(5), new Rectangle(4, 6), new Circle(3) };
        for (Shape s : shapes) {
            // JVM decides at RUNTIME which area() to call based on actual object type
            System.out.printf("%s -> area = %.2f%n", s.name(), s.area());
        }
    }
}
""",
    lang="java",
)

pn.tip(
    "Thread exam tip: Two ways to create threads -- (1) extend Thread and override run(); "
    "(2) implement Runnable and pass to Thread constructor. "
    "Runnable is preferred -- it doesn't use up Java's single inheritance slot. "
    "Call start() NOT run() to launch a thread (run() just calls the method directly)."
)
pn.br()

# #############################################################################
#  QUESTION 3 -- CO3: APPLETS
# #############################################################################
pn.part_box("QUESTION 3 -- CO3: JAVA APPLETS")

# -----------------------------------------------------------------------------
#  Q3(a) -- 3 Marks
# -----------------------------------------------------------------------------
pn.chap_box(
    "Q3(a) [3 Marks] -- Applet Initialization Phase | <APPLET> Tag | Local vs Remote Applet | Applet Class\n"
    "(May-June 2025 | July-Dec 2024 | June 2022 | May-June 2024)"
)

pn.section("Purpose of Applet Initialization Phase (init())")
pn.definition(
    "<b>Applet Initialization Phase:</b> The phase triggered by the browser/appletviewer "
    "calling the <code>init()</code> method exactly <b>ONCE</b> when the applet class is "
    "first loaded into memory. It is the applet's equivalent of a constructor. "
    "Its purpose is to perform all one-time setup tasks before the applet starts running."
)
pn.bullet(
    [
        "<b>Initialize instance variables</b> -- set counters, strings, booleans to starting values.",
        '<b>Read HTML parameters</b> -- call <code>getParameter("name")</code> to read <code>&lt;param&gt;</code> values.',
        "<b>Create and add UI components</b> -- Buttons, TextFields, Labels to the applet panel.",
        "<b>Register event listeners</b> -- attach listeners to UI components.",
        "<b>Load resources</b> -- <code>getImage()</code>, <code>getAudioClip()</code> for images/sounds.",
        "<b>Set visual properties</b> -- <code>setBackground()</code>, <code>setFont()</code>.",
    ]
)

pn.section("Applet Class -- Description")
pn.definition(
    "<b>java.applet.Applet</b> is the base class that all Java applets must extend. "
    "It inherits from <code>java.awt.Panel -> Container -> Component -> Object</code>. "
    "This inheritance gives applets an automatic graphical panel and access to all "
    "AWT drawing and component facilities. The Applet class provides the four lifecycle "
    "methods (<code>init, start, stop, destroy</code>), the <code>paint(Graphics)</code> "
    "hook, and utility methods like <code>getParameter(), showStatus(), getImage()</code>."
)

pn.section("Local Applet vs Remote Applet")
pn.info_table(
    ["Property", "Local Applet", "Remote Applet"],
    [
        [
            "Location",
            "Stored on the same machine running the browser",
            "Stored on a web server accessible via the internet",
        ],
        [
            "Access Method",
            "File path on local filesystem",
            "HTTP URL pointing to a web server",
        ],
        [
            "APPLET Tag",
            'code="MyApplet.class" (no codebase needed)',
            'codebase="http://server.com/applets/" code="MyApplet.class"',
        ],
        [
            "Speed",
            "Fast -- no network download needed",
            "Slower -- must download .class file over network",
        ],
        ["Use Case", "Development and testing", "Production deployment on websites"],
    ],
)

pn.section("Role and Significance of the <APPLET> Tag")
pn.definition(
    "The <code>&lt;APPLET&gt;</code> HTML tag is the mechanism by which an applet is "
    "embedded into a web page and launched by the browser. When the browser encounters "
    "this tag, it downloads the specified .class file, starts the JVM plugin, "
    "instantiates the applet, and begins the lifecycle."
)
pn.code_block(
    """
<!-- LocalApplet.html -->
<html>
  <body>
    <h2>My Java Applet</h2>
    <!-- Required attributes: code, width, height -->
    <applet code="WelcomeApplet.class"    <!-- .class filename -->
            width="400"                    <!-- applet panel width in pixels -->
            height="200"                   <!-- applet panel height in pixels -->
            codebase="applets/"            <!-- optional: subdirectory with .class -->
            name="myApplet"               <!-- optional: for JS/applet communication -->
            alt="Browser must support Java applets">
      <!-- param tags pass values to getParameter() -->
      <param name="message" value="Welcome to Java Programming!">
      <param name="color"   value="blue">
    </applet>
  </body>
</html>
""",
    lang="html",
)

# -----------------------------------------------------------------------------
#  Q3(b) -- 4 Marks
# -----------------------------------------------------------------------------
pn.chap_box(
    "Q3(b) [4 Marks] -- Events in Applet Architecture | Date/Time Applet | HTML APPLET Tag | Parameters\n"
    "(May-June 2025 | July-Dec 2024 | June 2022 | May-June 2024)"
)

pn.section("Two Types of Events Used by Applet Architecture")
pn.info_table(
    ["Event Type", "Description", "Example Methods"],
    [
        [
            "Lifecycle Events",
            "Triggered by the browser/appletviewer to control the applet's lifecycle. "
            "These are NOT user-initiated -- the browser calls them automatically based "
            "on page visibility.",
            "init(), start(), stop(), destroy()",
        ],
        [
            "User Interface Events",
            "Triggered by user interactions with the applet -- mouse movements, key presses, "
            "button clicks. The applet listens for these via the Delegation Event Model.",
            "mouseClicked(), keyPressed(), actionPerformed(), paint()",
        ],
    ],
)

pn.section("Applet Displaying Current Date and Time + HTML File")
pn.code_block(
    """
// DateTimeApplet.java
import java.applet.Applet;
import java.awt.*;
import java.util.Date;

public class DateTimeApplet extends Applet implements Runnable {

    Thread timer;
    Date   currentDateTime;
    Font   boldFont;

    @Override
    public void init() {
        setBackground(Color.DARK_GRAY);
        boldFont = new Font("Courier New", Font.BOLD, 18);
        currentDateTime = new Date();
    }

    @Override
    public void start() {
        timer = new Thread(this);
        timer.start();  // start background thread to update time
    }

    @Override
    public void run() {
        while (Thread.currentThread() == timer) {
            currentDateTime = new Date();  // update to current time
            repaint();                     // schedule a repaint
            try { Thread.sleep(1000); }    // update every 1 second
            catch (InterruptedException e) { break; }
        }
    }

    @Override
    public void stop() {
        timer = null;   // setting to null stops the while loop check
    }

    @Override
    public void paint(Graphics g) {
        g.setFont(boldFont);

        // Draw title
        g.setColor(Color.CYAN);
        g.drawString("Current Date & Time", 30, 50);

        // Draw separator line
        g.setColor(Color.GRAY);
        g.drawLine(30, 60, 370, 60);

        // Draw date/time
        g.setColor(Color.YELLOW);
        g.drawString(currentDateTime.toString(), 30, 100);

        // Draw border
        g.setColor(Color.GREEN);
        g.drawRect(10, 10, getWidth() - 20, getHeight() - 20);
    }
}
""",
    lang="java",
)
pn.code_block(
    """
<!-- DateTimeApplet.html -->
<html>
  <head><title>Date & Time Applet</title></head>
  <body style="background:#222">
    <h2 style="color:white">Java Date & Time Applet</h2>
    <applet code="DateTimeApplet.class"
            width="420"
            height="130"
            alt="Displays current date and time, updated every second">
      Your browser does not support Java applets.
    </applet>
    <p style="color:gray">Compile: javac DateTimeApplet.java<br>
       Run: appletviewer DateTimeApplet.html</p>
  </body>
</html>
""",
    lang="html",
)

pn.section("Passing Parameters to Applets")
pn.code_block(
    """
// ParameterizedGreetingApplet.java
import java.applet.Applet;
import java.awt.*;

public class ParameterizedGreetingApplet extends Applet {

    String message;
    String bgColorName;
    int    fontSize;
    Color  bgColor;

    @Override
    public void init() {
        // Read HTML <param> values using getParameter()
        // ALWAYS check for null -- param may not exist in HTML
        message = getParameter("message");
        if (message == null) message = "Hello, World!";  // default value

        bgColorName = getParameter("bgcolor");
        if (bgColorName == null) bgColorName = "blue";

        String fontSizeParam = getParameter("fontsize");
        fontSize = (fontSizeParam != null) ? Integer.parseInt(fontSizeParam) : 16;

        // Map color name to Color object
        switch (bgColorName.toLowerCase()) {
            case "red":    bgColor = Color.RED;     break;
            case "green":  bgColor = Color.GREEN;   break;
            case "yellow": bgColor = Color.YELLOW;  break;
            default:       bgColor = Color.BLUE;
        }
        setBackground(bgColor);
    }

    @Override
    public void paint(Graphics g) {
        g.setFont(new Font("Arial", Font.BOLD, fontSize));
        g.setColor(Color.WHITE);
        g.drawString(message, 30, 60);
        showStatus("Message: " + message + " | BG: " + bgColorName);
    }
}
""",
    lang="java",
)
pn.code_block(
    """
<!-- ParameterizedGreetingApplet.html -->
<html>
  <body>
    <applet code="ParameterizedGreetingApplet.class" width="400" height="100">
      <param name="message"  value="Welcome to Java Programming!">
      <param name="bgcolor"  value="green">
      <param name="fontsize" value="20">
    </applet>
  </body>
</html>
""",
    lang="html",
)

# -----------------------------------------------------------------------------
#  Q3(c) -- 4 Marks
# -----------------------------------------------------------------------------
pn.chap_box(
    "Q3(c) [4 Marks] -- Role of Window in Applet | Status Window | Applet vs Application | Local vs Remote\n"
    "(May-June 2025 | July-Dec 2024 | June 2022 | May-June 2024)"
)

pn.section("Role of a Window in an Applet")
pn.body(
    "In an applet, the <b>window</b> (the applet panel embedded in the browser) serves as "
    "the visible display surface. Its role includes:"
)
pn.bullet(
    [
        "<b>Rendering Surface:</b> The window is the Graphics context on which all drawing operations "
        "(drawString, drawOval, drawImage, etc.) are performed via the paint() method.",
        "<b>Event Container:</b> The window receives and dispatches all user events -- "
        "mouse clicks, key presses, scroll events -- to registered listeners.",
        "<b>Layout Container:</b> Being a Panel subclass, the window can contain AWT UI "
        "components like Button, TextField, Label using layout managers.",
        "<b>Size Boundary:</b> The window defines the drawable area dimensions (set by "
        "width/height in the <applet> tag). getWidth() and getHeight() return these dimensions.",
    ]
)

pn.section("Purpose of the Status Window in Applets")
pn.body(
    "The <b>Status Window</b> (or Status Bar) is the text bar at the bottom of the browser "
    "window. Applets can display informational messages in the status bar using:"
)
pn.code_block(
    """
// StatusWindowDemo.java
import java.applet.Applet;
import java.awt.*;
import java.awt.event.*;

public class StatusWindowDemo extends Applet implements MouseListener {

    @Override
    public void init() {
        addMouseListener(this);
        showStatus("StatusWindowDemo loaded. Move mouse over applet.");
    }

    @Override
    public void paint(Graphics g) {
        g.setColor(Color.DARK_GRAY);
        g.drawString("Hover / click in this applet panel.", 30, 60);
        g.drawString("Watch the browser status bar below!", 30, 90);
    }

    // Mouse events update the status bar
    @Override
    public void mouseEntered(MouseEvent e) {
        showStatus("Mouse entered the applet at: " + e.getX() + ", " + e.getY());
    }

    @Override
    public void mouseExited(MouseEvent e)  { showStatus("Mouse left the applet area."); }

    @Override
    public void mouseClicked(MouseEvent e) {
        showStatus("Clicked at: (" + e.getX() + ", " + e.getY() + ") -- Button: " + e.getButton());
    }

    @Override public void mousePressed(MouseEvent e)  {}
    @Override public void mouseReleased(MouseEvent e) {}
}
""",
    lang="java",
)

pn.section("How Applets Differ from Application Programs")
pn.info_table(
    ["Feature", "Java Applet", "Java Application"],
    [
        [
            "Entry Point",
            "No main(). Browser calls init() -> start()",
            "public static void main(String[] args)",
        ],
        [
            "Launch",
            "Embedded in HTML page, loaded by browser",
            "Command line: java ClassName",
        ],
        [
            "GUI",
            "Inherits Panel automatically (from Applet class)",
            "Must create Frame/JFrame manually",
        ],
        [
            "File Access",
            "Sandboxed -- cannot access local filesystem (security)",
            "Full access to filesystem, network, OS",
        ],
        ["Network", "Can only connect back to originating server", "No restrictions"],
        [
            "Deployment",
            "Requires web server hosting HTML + .class files",
            "Distributed as .jar or .class files",
        ],
        [
            "Status (2026)",
            "Deprecated (Java 9) and removed (Java 17)",
            "Standard and actively used",
        ],
    ],
)

# -----------------------------------------------------------------------------
#  Q3(d) -- 10 Marks
# -----------------------------------------------------------------------------
pn.chap_box(
    "Q3(d) [10 Marks] -- Applet Lifecycle with Diagram and Code\n"
    "(May-June 2025 | July-Dec 2024 | June 2022 | May-June 2024)"
)

pn.section("Applet Lifecycle -- The Four Phase Methods")
pn.definition(
    "<b>Applet Lifecycle:</b> The defined sequence of states and transitions that an applet "
    "passes through from the moment it is loaded by the browser until it is destroyed. "
    "The browser (or appletviewer) controls this lifecycle by calling four special "
    "lifecycle methods in a prescribed order."
)

pn.info_table(
    ["Method", "Called When", "Purpose", "Frequency"],
    [
        [
            "init()",
            "Applet class is first loaded into browser memory",
            "One-time setup: initialize variables, read params, create UI, register listeners, load resources",
            "EXACTLY ONCE per lifetime",
        ],
        [
            "start()",
            "Immediately after init() AND each time user returns to the page",
            "Begin/resume execution: start threads, resume animation, resume audio",
            "MULTIPLE TIMES (each page visit)",
        ],
        [
            "stop()",
            "User navigates AWAY from page OR minimizes the browser window",
            "Pause execution: stop/null threads, pause animation, mute audio (saves CPU)",
            "MULTIPLE TIMES (each page leave)",
        ],
        [
            "destroy()",
            "Browser tab is closed OR browser is shutting down",
            "Final permanent cleanup: close streams, release ALL resources, stop ALL threads permanently",
            "EXACTLY ONCE per lifetime",
        ],
    ],
)

pn.section("Applet Lifecycle State Diagram")

sm = pd.StateMachine(
    width=pn.CW,
    height=240,
    caption="Fig 3.1: Applet Lifecycle State Transitions -- init, start, stop, destroy",
    theme=diag_theme,
)
sm.state("loaded", "LOADED", initial=True)
sm.state("initialized", "INITIALIZED")
sm.state("running", "RUNNING")
sm.state("idle", "STOPPED/IDLE")
sm.state("destroyed", "DESTROYED", accepting=True)
sm.transition("loaded", "initialized", label="browser calls init()")
sm.transition("initialized", "running", label="browser calls start()")
sm.transition("running", "idle", label="user leaves page\nbrowser calls stop()")
sm.transition("idle", "running", label="user returns\nbrowser calls start()")
sm.transition("idle", "destroyed", label="tab closed\nbrowser calls destroy()")
sm.transition("running", "destroyed", label="direct close\nstop() + destroy()")
pn.story.extend(sm.as_flowable())

pn.section("Complete Lifecycle Demonstration Code")
pn.code_block(
    """
// LifecycleDemoApplet.java -- All four lifecycle methods demonstrated
import java.applet.Applet;
import java.awt.*;

public class LifecycleDemoApplet extends Applet implements Runnable {

    Thread animThread;       // animation thread
    String currentState;     // track current phase for display
    int    startCount  = 0;  // how many times start() was called
    int    stopCount   = 0;  // how many times stop() was called
    int    tickCounter = 0;  // incremented by background thread
    Font   headerFont, bodyFont;

    // -- PHASE 1: init() -----------------------------------------------------
    // Called ONCE: applet class loaded; do one-time initialization here
    @Override
    public void init() {
        currentState = "INITIALIZED";
        headerFont = new Font("Arial", Font.BOLD, 16);
        bodyFont   = new Font("Courier", Font.PLAIN, 12);
        setBackground(new Color(30, 30, 50));    // dark background
        showStatus("Applet initialized -- ready to start.");
        System.out.println("[Lifecycle] init() called once.");
    }

    // -- PHASE 2: start() ----------------------------------------------------
    // Called after init() AND every time user returns to the page
    @Override
    public void start() {
        startCount++;
        currentState = "RUNNING (start #" + startCount + ")";
        animThread   = new Thread(this);
        animThread.start();   // begin/resume animation thread
        showStatus("Applet started -- thread running.");
        System.out.println("[Lifecycle] start() called (visit #" + startCount + ").");
    }

    // -- ANIMATION THREAD ----------------------------------------------------
    @Override
    public void run() {
        while (Thread.currentThread() == animThread) {
            tickCounter++;
            repaint();   // trigger paint() to refresh display
            try { Thread.sleep(500); }
            catch (InterruptedException e) { break; }
        }
    }

    // -- PHASE 3: stop() -----------------------------------------------------
    // Called each time user leaves the page -- PAUSE resources here
    @Override
    public void stop() {
        stopCount++;
        currentState = "STOPPED (stop #" + stopCount + ")";
        animThread   = null;   // setting to null makes run() while-check fail --> thread ends
        showStatus("Applet stopped -- thread paused.");
        System.out.println("[Lifecycle] stop() called (leave #" + stopCount + ").");
        repaint();
    }

    // -- PHASE 4: destroy() --------------------------------------------------
    // Called ONCE: browser tab permanently closed -- final cleanup
    @Override
    public void destroy() {
        animThread   = null;
        currentState = "DESTROYED";
        System.out.println("[Lifecycle] destroy() called -- final cleanup.");
    }

    // -- DISPLAY (paint) ------------------------------------------------------
    @Override
    public void paint(Graphics g) {
        g.setFont(headerFont);
        g.setColor(Color.CYAN);
        g.drawString("Applet Lifecycle Demonstrator", 20, 40);

        g.setColor(Color.LIGHT_GRAY);
        g.drawLine(20, 50, getWidth() - 20, 50);

        g.setFont(bodyFont);
        g.setColor(Color.YELLOW);
        g.drawString("Current State : " + currentState, 20, 80);

        g.setColor(Color.WHITE);
        g.drawString("start() calls : " + startCount, 20, 110);
        g.drawString("stop()  calls : " + stopCount, 20, 130);
        g.drawString("Tick Counter  : " + tickCounter, 20, 150);

        g.setColor(Color.GREEN);
        g.drawString("Lifecycle: init->start->[stop->start]*->stop->destroy", 20, 185);

        // Border
        g.setColor(Color.BLUE);
        g.drawRect(5, 5, getWidth() - 10, getHeight() - 10);
    }
}
""",
    lang="java",
)

pn.tip(
    "Lifecycle order to MEMORIZE: init() -> start() -> [stop() -> start()] * -> stop() -> destroy(). "
    "init() and destroy() called EXACTLY ONCE. "
    "start() and stop() called MULTIPLE TIMES. "
    "Always set thread to null in stop() -- checking against null in run() makes it pause. "
    "Never put infinite loops in init() -- it would block the browser!"
)

# -----------------------------------------------------------------------------
#  Q3(e) -- 10 Marks
# -----------------------------------------------------------------------------
pn.chap_box(
    "Q3(e) [10 Marks] -- Banner Applet | Passing Parameters | Graphics Methods (drawOval, drawRect, drawLine)\n"
    "(May-June 2025 | July-Dec 2024 | June 2022 | May-June 2024)"
)

pn.section("Scrolling Banner Applet -- 'Welcome to Java Programming'")
pn.code_block(
    """
// BannerApplet.java -- Scrolling text banner applet
import java.applet.Applet;
import java.awt.*;

public class BannerApplet extends Applet implements Runnable {

    Thread   bannerThread;
    String   message;       // text to scroll (read from param)
    int      xPos;          // current horizontal position of text
    int      textWidth;     // pixel width of the message string
    Color    textColor;
    Font     bannerFont;

    @Override
    public void init() {
        // Read HTML parameters (with defaults if not provided)
        message = getParameter("msg");
        if (message == null) message = "Welcome to Java Programming!   ";

        String colorParam = getParameter("textcolor");
        textColor = (colorParam != null && colorParam.equals("yellow"))
                    ? Color.YELLOW : Color.GREEN;

        bannerFont = new Font("Arial", Font.BOLD, 22);
        setBackground(Color.BLACK);

        // Calculate text width for proper scrolling reset
        FontMetrics fm = getFontMetrics(bannerFont);
        textWidth = fm.stringWidth(message);

        xPos = getWidth();   // start off-screen to the right
    }

    @Override
    public void start() {
        bannerThread = new Thread(this);
        bannerThread.start();
    }

    @Override
    public void run() {
        while (Thread.currentThread() == bannerThread) {
            xPos -= 2;   // scroll left by 2 pixels per frame
            // Reset: when text has fully scrolled off the left edge
            if (xPos < -textWidth) {
                xPos = getWidth();   // restart from right edge
            }
            repaint();
            try { Thread.sleep(30); }   // ~33 fps
            catch (InterruptedException e) { break; }
        }
    }

    @Override
    public void stop() {
        bannerThread = null;
    }

    // Override update() to prevent white flash (flicker fix)
    @Override
    public void update(Graphics g) {
        paint(g);   // skip default clear -- we handle background in paint()
    }

    @Override
    public void paint(Graphics g) {
        // Redraw background manually (faster than letting update() clear)
        g.setColor(Color.BLACK);
        g.fillRect(0, 0, getWidth(), getHeight());

        // Draw border
        g.setColor(Color.DARK_GRAY);
        g.drawRect(2, 2, getWidth() - 4, getHeight() - 4);

        // Draw scrolling text at current position
        g.setFont(bannerFont);
        g.setColor(textColor);
        g.drawString(message, xPos, getHeight() / 2 + 8);
    }
}
""",
    lang="java",
)
pn.code_block(
    """
<!-- BannerApplet.html -->
<html>
  <body style="background:#111">
    <h3 style="color:white">Java Scrolling Banner Applet</h3>
    <applet code="BannerApplet.class" width="500" height="60">
      <param name="msg"       value="Welcome to Java Programming!   ">
      <param name="textcolor" value="yellow">
    </applet>
  </body>
</html>
""",
    lang="html",
)

pn.section("Graphics Methods -- drawOval, drawRect, drawLine, fillOval")
pn.code_block(
    """
// GraphicsMethodsApplet.java -- demonstrates drawOval, drawRect, drawLine, fillOval
import java.applet.Applet;
import java.awt.*;

public class GraphicsMethodsApplet extends Applet {

    @Override
    public void init() {
        setBackground(Color.WHITE);
    }

    @Override
    public void paint(Graphics g) {

        // -- drawLine(x1, y1, x2, y2) --------------------------------------
        // Draws a straight line from (x1,y1) to (x2,y2)
        g.setColor(Color.BLACK);
        g.drawLine(10, 20, 390, 20);         // horizontal divider line
        g.drawLine(200, 30, 200, 270);       // vertical divider

        // -- drawRect(x, y, width, height) ---------------------------------
        // Draws the outline of a rectangle; (x,y) = top-left corner
        g.setColor(Color.BLUE);
        g.drawRect(20, 40, 150, 100);        // outline only -- hollow

        // Filled rectangle using fillRect
        g.setColor(new Color(0, 100, 255, 100)); // semi-transparent blue
        g.fillRect(25, 45, 140, 90);         // filled blue rectangle

        // Label
        g.setColor(Color.BLACK);
        g.drawString("drawRect + fillRect", 25, 165);

        // -- drawOval(x, y, width, height) ---------------------------------
        // Draws an oval inscribed in the bounding rectangle
        g.setColor(Color.RED);
        g.drawOval(220, 40, 150, 100);       // hollow oval/ellipse

        // -- fillOval(x, y, width, height) ---------------------------------
        // Draws a FILLED oval (solid)
        g.setColor(new Color(255, 100, 0, 150));  // semi-transparent orange
        g.fillOval(225, 45, 140, 90);        // filled oval

        g.setColor(Color.BLACK);
        g.drawString("drawOval + fillOval", 225, 165);

        // -- Circle (oval with equal width and height) ----------------------
        g.setColor(Color.GREEN);
        g.fillOval(80, 185, 80, 80);         // filled circle (r=40)
        g.setColor(Color.DARK_GRAY);
        g.drawOval(80, 185, 80, 80);         // outline over fill

        g.setColor(Color.MAGENTA);
        g.drawOval(260, 185, 100, 60);       // ellipse
        g.fillOval(263, 188, 94, 54);        // filled ellipse (slightly inset)

        // Labels
        g.setColor(Color.BLACK);
        g.drawString("fillOval (circle)", 70, 285);
        g.drawString("Ellipse", 275, 285);
    }
}
""",
    lang="java",
)

pn.section("Disadvantages of Applets")
pn.bullet(
    [
        "<b>Browser Plugin Required:</b> Needs Java browser plugin (NPAPI) which most modern browsers have removed.",
        "<b>Security Sandboxing:</b> Cannot access local file system or unrestricted network -- limits functionality.",
        "<b>Slow Download:</b> .class files must be downloaded over the network before execution.",
        "<b>Platform Inconsistency:</b> Rendering differences across different JVM versions and operating systems.",
        "<b>Deprecated:</b> Officially deprecated in Java 9 and completely removed in Java 17.",
        "<b>Poor Mobile Support:</b> Never worked on mobile browsers (iOS, Android).",
    ]
)

pn.tip(
    "Banner applet tip: The key is 'xPos -= 2' in run(), then check 'if (xPos < -textWidth) xPos = getWidth()'. "
    "Override update() with just 'paint(g)' to prevent flickering. "
    "Always stop the thread in stop() by setting it to null."
)
pn.br()

# #############################################################################
#  QUESTION 4 -- CO4: AWT, SWING, LAYOUT MANAGERS, GUI
# #############################################################################
pn.part_box("QUESTION 4 -- CO4: AWT, SWING, LAYOUT MANAGERS & GUI")

# -----------------------------------------------------------------------------
#  Q4(a) -- 3 Marks
# -----------------------------------------------------------------------------
pn.chap_box(
    "Q4(a) [3 Marks] -- Frame vs Panel | AWT Classes for GUI | Event | Need for GUI\n"
    "(May-June 2025 | July-Dec 2024 | June 2022 | May-June 2024)"
)

pn.section("Frame vs Panel in AWT")
pn.info_table(
    ["Property", "Frame", "Panel"],
    [
        ["Class", "java.awt.Frame", "java.awt.Panel"],
        ["Parent", "extends Window -> Container", "extends Container -> Component"],
        [
            "Top-Level Window",
            "YES -- has title bar, minimize/maximize/close buttons",
            "NO -- must be placed inside another container",
        ],
        [
            "Standalone Use",
            "Can exist independently as the main application window",
            "Must be embedded inside a Frame or another Container",
        ],
        ["Default Layout", "BorderLayout", "FlowLayout"],
        [
            "Visibility",
            "set setVisible(true) to show",
            "Visible when parent container is shown",
        ],
        [
            "Usage",
            "Main application window",
            "Sub-section / panel grouping inside a Frame",
        ],
    ],
)

pn.section("What is an Event?")
pn.definition(
    "<b>Event:</b> An object that encapsulates information about a user action or system "
    "notification that occurred on a GUI component. Examples include mouse clicks, key presses, "
    "button activations, window operations, and scrollbar adjustments. "
    "In Java AWT/Swing, events are represented by classes like "
    "<code>ActionEvent, MouseEvent, KeyEvent, WindowEvent</code>, all extending "
    "<code>java.awt.AWTEvent</code>."
)

pn.section("Need for GUI-Based Applications")
pn.bullet(
    [
        "<b>User-Friendliness:</b> Graphical interfaces are intuitive -- users can interact via mouse clicks and visual elements without memorizing commands.",
        "<b>Productivity:</b> Visual tools (buttons, menus, dialogs) let users accomplish tasks faster than command-line interfaces.",
        "<b>Accessibility:</b> GUI applications serve a much wider audience, including non-technical users.",
        "<b>Visual Feedback:</b> Immediate visual response (color changes, progress bars, dialogs) makes applications feel responsive.",
        "<b>Industry Standard:</b> All major commercial applications (MS Office, browsers, IDEs) use GUI for competitive usability.",
    ]
)

# -----------------------------------------------------------------------------
#  Q4(b) -- 4 Marks
# -----------------------------------------------------------------------------
pn.chap_box(
    "Q4(b) [4 Marks] -- Three AWT Layout Managers | Component/Container/Panel/Frame | AWT vs Swing\n"
    "(May-June 2025 | July-Dec 2024 | June 2022 | May-June 2024)"
)

pn.section("Three Layout Managers in AWT and Their Purposes")
pn.info_table(
    ["Layout Manager", "Class", "How it Works", "Best Use Case"],
    [
        [
            "FlowLayout",
            "java.awt.FlowLayout",
            "Arranges components left-to-right in a row, wrapping to the next row when the row is full. Default layout for Panel and Applet.",
            "Simple toolbars, button rows, horizontally arranged controls.",
        ],
        [
            "BorderLayout",
            "java.awt.BorderLayout",
            "Divides container into 5 regions: NORTH, SOUTH, EAST, WEST, CENTER. Each region can hold one component. CENTER expands to fill remaining space.",
            "Main application window with menu bar (NORTH), status bar (SOUTH), side panels (EAST/WEST), main content (CENTER).",
        ],
        [
            "GridLayout",
            "java.awt.GridLayout",
            "Divides container into equal-sized rectangular cells in a grid (rows x columns). Each cell holds exactly one component.",
            "Calculator buttons, forms with aligned labels and fields, spreadsheet-like interfaces.",
        ],
    ],
)

pn.section("Difference Between Component, Container, Panel, and Frame")
pn.info_table(
    ["Class", "Hierarchy Level", "Description", "Examples"],
    [
        [
            "Component",
            "Base (java.awt.Component)",
            "Root of the AWT hierarchy. Every visible GUI element is a Component. Provides paint(), repaint(), setSize(), setBackground(), event listener registration.",
            "Abstract base -- Button, Label, TextField, Canvas all extend Component",
        ],
        [
            "Container",
            "Mid-level (extends Component)",
            "A Component that can HOLD other Components. Has add(Component) and setLayout(LayoutManager) methods.",
            "Abstract base for Panel, Frame, Dialog, ScrollPane",
        ],
        [
            "Panel",
            "Concrete (extends Container)",
            "A lightweight, non-window Container. Has no title bar or border. Used to group components into sub-sections inside a Frame. Default layout: FlowLayout.",
            "Used inside Frame to organize sections",
        ],
        [
            "Frame",
            "Top-Level (extends Window -> Container)",
            "A top-level window with title bar, resizable border, and OS window buttons (minimize, maximize, close). The main application window.",
            'new Frame("My App") -- the outer window',
        ],
    ],
)

pn.section("AWT vs Swing")
pn.info_table(
    ["Feature", "AWT (Abstract Window Toolkit)", "Swing"],
    [
        ["Package", "java.awt", "javax.swing"],
        [
            "Type",
            "Heavyweight -- uses native OS widgets",
            "Lightweight -- draws its own widgets",
        ],
        [
            "Platform Consistency",
            "Looks different on each OS (uses native controls)",
            "Consistent look across all OS (pluggable LAF)",
        ],
        [
            "Performance",
            "Faster (delegates to OS for rendering)",
            "Slightly slower (Java paints every pixel)",
        ],
        [
            "Components",
            "Button, TextField, Checkbox, List (native)",
            "JButton, JTextField, JCheckBox, JList (Java-painted)",
        ],
        [
            "Look and Feel",
            "Platform native only",
            "Multiple LAFs: Metal, Nimbus, Windows, GTK, etc.",
        ],
        [
            "Functionality",
            "Basic -- limited features",
            "Rich -- JTable, JTree, JScrollPane, JTabbedPane",
        ],
        ["MVC Architecture", "No", "Yes -- Model-View-Controller for tables, lists"],
    ],
)

# -----------------------------------------------------------------------------
#  Q4(c) -- 4 Marks
# -----------------------------------------------------------------------------
pn.chap_box(
    "Q4(c) [4 Marks] -- Event Listeners | GridLayout vs BorderLayout | AWT Controls | Container/Panel/Frame\n"
    "(May-June 2025 | July-Dec 2024 | June 2022 | May-June 2024)"
)

pn.section("Event Listeners in Java -- Handling User Interactions")
pn.info_table(
    ["Listener Interface", "Method(s) to Implement", "Used For"],
    [
        [
            "ActionListener",
            "actionPerformed(ActionEvent e)",
            "Button clicks, menu selection, TextField Enter key",
        ],
        [
            "MouseListener",
            "mouseClicked, mousePressed, mouseReleased, mouseEntered, mouseExited (5 methods)",
            "Mouse click events on any component",
        ],
        [
            "MouseMotionListener",
            "mouseMoved, mouseDragged (2 methods)",
            "Tracking mouse movement and drag operations",
        ],
        [
            "KeyListener",
            "keyPressed, keyReleased, keyTyped (3 methods)",
            "Keyboard input on focused component",
        ],
        [
            "WindowListener",
            "windowClosing, windowOpened, etc. (7 methods)",
            "Frame open/close/minimize/maximize",
        ],
        [
            "ItemListener",
            "itemStateChanged(ItemEvent e)",
            "Checkbox toggle, Choice/List selection",
        ],
        [
            "TextListener",
            "textValueChanged(TextEvent e)",
            "Each character change in TextField/TextArea",
        ],
    ],
)

pn.section("GridLayout vs BorderLayout")
pn.info_table(
    ["Property", "GridLayout(rows, cols)", "BorderLayout()"],
    [
        [
            "Cell Division",
            "Divides into equal rows x columns cells",
            "Divides into 5 named regions",
        ],
        [
            "Cell Size",
            "ALL cells are equal size",
            "CENTER fills remaining space; edges can have preferred size",
        ],
        [
            "Regions",
            "row x col numbered cells",
            "NORTH, SOUTH, EAST, WEST, CENTER (named constants)",
        ],
        ["Components per Cell", "Exactly one", "Exactly one per region (5 total max)"],
        [
            "add() Syntax",
            "container.add(btn) -- added in order",
            "container.add(btn, BorderLayout.NORTH)",
        ],
        ["Use Case", "Calculator keypad, form grid", "Main app window with sections"],
        [
            "Resize Behavior",
            "All cells grow/shrink equally",
            "CENTER grows; NORTH/SOUTH grow horizontally only",
        ],
    ],
)

pn.section("AWT Controls -- Types and Usage")
pn.info_table(
    ["AWT Control", "Class", "Description"],
    [
        [
            "Button",
            "java.awt.Button",
            "Clickable push button. Fires ActionEvent on click. Registered with addActionListener().",
        ],
        [
            "Label",
            "java.awt.Label",
            "Non-editable display text. Alignment: LEFT, RIGHT, CENTER.",
        ],
        [
            "TextField",
            "java.awt.TextField",
            "Single-line text input. Fires ActionEvent on Enter. Access text via getText()/setText().",
        ],
        [
            "TextArea",
            "java.awt.TextArea",
            "Multi-line scrollable text input. Good for larger text blocks.",
        ],
        [
            "Checkbox",
            "java.awt.Checkbox",
            "Toggle on/off control. ItemEvent on state change. isState() to query.",
        ],
        [
            "Choice",
            "java.awt.Choice",
            "Drop-down list selection. add() to add items. getSelectedItem() to query.",
        ],
        [
            "List",
            "java.awt.List",
            "Scrollable item list. Supports single/multiple selection.",
        ],
        [
            "Scrollbar",
            "java.awt.Scrollbar",
            "Horizontal or vertical slider. AdjustmentEvent on movement.",
        ],
        [
            "Canvas",
            "java.awt.Canvas",
            "Blank drawing surface for custom graphics via paint(Graphics).",
        ],
    ],
)

# -----------------------------------------------------------------------------
#  Q4(d) -- 10 Marks
# -----------------------------------------------------------------------------
pn.chap_box(
    "Q4(d) [10 Marks] -- GridLayout Setup | AWT vs Swing Differences | AWT Event Hierarchy | AWT Windows & Buttons\n"
    "(May-June 2025 | July-Dec 2024 | June 2022 | May-June 2024)"
)

pn.section("AWT Component Class Hierarchy")

stack_awt = pd.LayeredStack(
    width=pn.CW * 0.8,
    height=200,
    theme=diag_theme,
    caption="Fig 4.1: AWT Component Hierarchy -- inheritance chain from Object to Frame",
)
stack_awt.layer("java.lang.Object", sublabel="Root of all Java classes")
stack_awt.layer(
    "java.awt.Component",
    sublabel="All GUI elements: setSize, paint, repaint, add/removeXxxListener",
)
stack_awt.layer(
    "java.awt.Container",
    sublabel="Holds child components: add(Component), setLayout(LayoutManager)",
)
stack_awt.layer(
    "java.awt.Panel / Window",
    sublabel="Panel = lightweight container  |  Window = top-level OS window",
)
stack_awt.layer(
    "java.awt.Frame / Applet / Dialog",
    sublabel="Frame = main app window  |  Applet = browser panel  |  Dialog = modal window",
)
pn.story.extend(stack_awt.as_flowable())

pn.section("Setting Up a Grid Layout -- Calculator Keypad Example")
pn.code_block(
    """
// GridLayoutCalculator.java -- Grid layout for calculator keypad
import java.awt.*;
import java.awt.event.*;

public class GridLayoutCalculator extends Frame implements ActionListener {

    TextField display;
    String currentInput = "";

    String[] buttonLabels = {
        "7", "8", "9", "/",
        "4", "5", "6", "*",
        "1", "2", "3", "-",
        "0", "C", "=", "+"
    };

    public GridLayoutCalculator() {
        super("Calculator -- GridLayout Demo");
        setSize(300, 380);

        // STEP 1: Create display TextField (spans top)
        display = new TextField("0");
        display.setFont(new Font("Courier", Font.BOLD, 20));
        display.setEditable(false);
        display.setBackground(Color.BLACK);
        display.setForeground(Color.GREEN);

        // STEP 2: Create panel with 4x4 GridLayout for buttons
        Panel btnPanel = new Panel();
        // GridLayout(rows=4, cols=4, hgap=4, vgap=4) -- 4 rows, 4 columns, 4px gaps
        btnPanel.setLayout(new GridLayout(4, 4, 4, 4));
        btnPanel.setBackground(Color.DARK_GRAY);

        // STEP 3: Add buttons to panel (filled in row-major order)
        for (String label : buttonLabels) {
            Button btn = new Button(label);
            btn.setFont(new Font("Arial", Font.BOLD, 16));
            btn.setBackground(label.matches("[0-9]") ? Color.GRAY : Color.ORANGE);
            btn.setForeground(Color.WHITE);
            btn.addActionListener(this);
            btnPanel.add(btn);  // added in GridLayout order: left-to-right, top-to-bottom
        }

        // STEP 4: Use BorderLayout for main frame
        setLayout(new BorderLayout(5, 5));
        add(display, BorderLayout.NORTH);    // display at top
        add(btnPanel, BorderLayout.CENTER);  // keypad fills center

        // Window close handler
        addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent e) { dispose(); System.exit(0); }
        });
        setVisible(true);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        String cmd = e.getActionCommand();
        switch (cmd) {
            case "C": currentInput = ""; display.setText("0"); break;
            case "=":
                try {
                    // Simple eval (for demo -- real calculator needs parser)
                    double result = eval(currentInput);
                    display.setText(String.valueOf(result));
                    currentInput = String.valueOf(result);
                } catch (Exception ex) { display.setText("Error"); currentInput = ""; }
                break;
            default:
                currentInput += cmd;
                display.setText(currentInput);
        }
    }

    // Very simple expression evaluator for single operation (demo)
    double eval(String expr) {
        if (expr.contains("+")) {
            String[] p = expr.split("\\+"); return Double.parseDouble(p[0]) + Double.parseDouble(p[1]);
        } else if (expr.contains("-")) {
            String[] p = expr.split("-"); return Double.parseDouble(p[0]) - Double.parseDouble(p[1]);
        } else if (expr.contains("*")) {
            String[] p = expr.split("\\*"); return Double.parseDouble(p[0]) * Double.parseDouble(p[1]);
        } else if (expr.contains("/")) {
            String[] p = expr.split("/"); return Double.parseDouble(p[0]) / Double.parseDouble(p[1]);
        }
        return Double.parseDouble(expr);
    }

    public static void main(String[] args) { new GridLayoutCalculator(); }
}
""",
    lang="java",
)

pn.section("Java AWT Program -- One Window with Two Buttons")
pn.code_block(
    """
// TwoButtonsAWT.java -- AWT window with two buttons as required
import java.awt.*;
import java.awt.event.*;

public class TwoButtonsAWT extends Frame implements ActionListener {

    Label  statusLabel;
    Button btnHello;
    Button btnBye;
    int    clickCount = 0;

    public TwoButtonsAWT() {
        super("UIT-RGPV -- AWT Two Buttons Demo");  // Frame title
        setSize(400, 250);
        setLayout(new FlowLayout(FlowLayout.CENTER, 20, 30));

        // Create two buttons
        btnHello = new Button("Say Hello");
        btnBye   = new Button("Say Goodbye");

        // Style the buttons
        btnHello.setFont(new Font("Arial", Font.BOLD, 14));
        btnHello.setBackground(Color.BLUE);
        btnHello.setForeground(Color.WHITE);
        btnHello.setPreferredSize(new Dimension(130, 40));

        btnBye.setFont(new Font("Arial", Font.BOLD, 14));
        btnBye.setBackground(Color.RED);
        btnBye.setForeground(Color.WHITE);
        btnBye.setPreferredSize(new Dimension(130, 40));

        // Status label to show result
        statusLabel = new Label("Click a button!", Label.CENTER);
        statusLabel.setFont(new Font("Courier", Font.BOLD, 16));
        statusLabel.setPreferredSize(new Dimension(360, 30));

        // Register ActionListeners (Delegation Event Model)
        btnHello.addActionListener(this);
        btnBye.addActionListener(this);

        // Add components to frame
        add(btnHello);
        add(btnBye);
        add(statusLabel);

        // Handle window close button
        addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent e) { dispose(); System.exit(0); }
        });

        setVisible(true);   // make window visible
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        clickCount++;
        if (e.getSource() == btnHello) {
            statusLabel.setText("Hello! (Click #" + clickCount + ")");
            statusLabel.setForeground(Color.BLUE);
        } else if (e.getSource() == btnBye) {
            statusLabel.setText("Goodbye! (Click #" + clickCount + ")");
            statusLabel.setForeground(Color.RED);
        }
    }

    public static void main(String[] args) {
        new TwoButtonsAWT();
    }
}
""",
    lang="java",
)

pn.section("AWT Event Hierarchy -- Explained")
pn.body(
    "The AWT event system is organized as a class hierarchy. All event objects extend "
    "<code>java.util.EventObject</code> and carry the source component reference. "
    "AWT-specific events further extend <code>java.awt.AWTEvent</code>."
)
pn.info_table(
    ["Event Category", "Event Class", "Fired By", "Listener Interface"],
    [
        [
            "Semantic Events",
            "ActionEvent",
            "Button, MenuItem, TextField, List",
            "ActionListener",
        ],
        ["Semantic Events", "ItemEvent", "Checkbox, Choice, List", "ItemListener"],
        ["Semantic Events", "TextEvent", "TextField, TextArea", "TextListener"],
        ["Semantic Events", "AdjustmentEvent", "Scrollbar", "AdjustmentListener"],
        [
            "Low-level Events",
            "MouseEvent",
            "Any Component (click/move/drag)",
            "MouseListener, MouseMotionListener",
        ],
        ["Low-level Events", "KeyEvent", "Any Component (key press)", "KeyListener"],
        [
            "Low-level Events",
            "WindowEvent",
            "Frame (open/close/minimize)",
            "WindowListener",
        ],
        [
            "Low-level Events",
            "FocusEvent",
            "Any Component (focus gain/loss)",
            "FocusListener",
        ],
        [
            "Low-level Events",
            "ComponentEvent",
            "Any Component (move/resize/show)",
            "ComponentListener",
        ],
    ],
)

# -----------------------------------------------------------------------------
#  Q4(e) -- 10 Marks
# -----------------------------------------------------------------------------
pn.chap_box(
    "Q4(e) [10 Marks] -- Multi-Threaded Programming | Swing JFrame with Button | AWT Controls & Layouts\n"
    "(May-June 2025 | July-Dec 2024 | June 2022 | May-June 2024)"
)

pn.section("Multi-Threaded Programming in Java -- Complete Example")
pn.definition(
    "<b>Multithreading:</b> The ability of a Java program to execute multiple threads "
    "(lightweight processes) concurrently within the same JVM process. Each thread has its "
    "own program counter, stack, and local variables, but shares the heap and static data "
    "with other threads. Java provides two ways to create threads: extending "
    "<code>Thread</code> or implementing <code>Runnable</code>."
)
pn.code_block(
    """
// MultiThreadDemo.java -- Producer-Consumer multithreading example
import java.util.LinkedList;
import java.util.Queue;

// Shared bounded buffer (thread-safe with synchronized)
class SharedBuffer {
    Queue<Integer> buffer = new LinkedList<>();
    int capacity;

    SharedBuffer(int cap) { this.capacity = cap; }

    // Producer adds items -- waits if buffer is full
    synchronized void produce(int item) throws InterruptedException {
        while (buffer.size() == capacity) {
            System.out.println("[Producer] Buffer full. Waiting...");
            wait();    // release lock and wait
        }
        buffer.add(item);
        System.out.println("[Producer] Produced: " + item + " | Buffer: " + buffer);
        notifyAll();  // wake up waiting consumer
    }

    // Consumer removes items -- waits if buffer is empty
    synchronized int consume() throws InterruptedException {
        while (buffer.isEmpty()) {
            System.out.println("[Consumer] Buffer empty. Waiting...");
            wait();
        }
        int item = buffer.poll();
        System.out.println("[Consumer] Consumed: " + item + " | Buffer: " + buffer);
        notifyAll();  // wake up waiting producer
        return item;
    }
}

class Producer extends Thread {
    SharedBuffer buf;
    Producer(SharedBuffer b) { buf = b; }
    @Override
    public void run() {
        for (int i = 1; i <= 8; i++) {
            try {
                buf.produce(i);
                Thread.sleep(200);  // simulate production time
            } catch (InterruptedException e) { break; }
        }
    }
}

class Consumer extends Thread {
    SharedBuffer buf;
    Consumer(SharedBuffer b) { buf = b; }
    @Override
    public void run() {
        for (int i = 0; i < 8; i++) {
            try {
                buf.consume();
                Thread.sleep(500);  // consumer slower than producer
            } catch (InterruptedException e) { break; }
        }
    }
}

public class MultiThreadDemo {
    public static void main(String[] args) throws InterruptedException {
        SharedBuffer buffer = new SharedBuffer(3);  // max 3 items
        Thread p = new Producer(buffer);
        Thread c = new Consumer(buffer);
        p.start();
        c.start();
        p.join();
        c.join();
        System.out.println("Producer-Consumer demo complete.");
    }
}
""",
    lang="java",
)

pn.section("Swing Program -- JFrame with Label and Button (Click to Update)")
pn.code_block(
    """
// SwingLabelButtonDemo.java -- JFrame with JLabel and JButton
// When button is clicked, label text updates
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class SwingLabelButtonDemo extends JFrame implements ActionListener {

    JLabel  statusLabel;
    JButton updateButton;
    JButton resetButton;
    int     clickCount = 0;

    public SwingLabelButtonDemo() {
        super("Swing JFrame Demo -- IT408");
        setSize(420, 200);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);   // auto-exit on close
        setLayout(new BorderLayout(10, 10));

        // -- JLabel at top (CENTER) ------------------------------------------
        statusLabel = new JLabel("Click the button below to update me!", JLabel.CENTER);
        statusLabel.setFont(new Font("Arial", Font.BOLD, 16));
        statusLabel.setForeground(Color.DARK_GRAY);
        statusLabel.setBorder(BorderFactory.createLineBorder(Color.GRAY, 2));
        statusLabel.setPreferredSize(new Dimension(400, 60));

        // -- Button Panel at bottom (SOUTH) ----------------------------------
        JPanel btnPanel = new JPanel(new FlowLayout(FlowLayout.CENTER, 20, 10));

        updateButton = new JButton("Update Label");
        updateButton.setFont(new Font("Arial", Font.BOLD, 14));
        updateButton.setBackground(new Color(0, 120, 210));
        updateButton.setForeground(Color.WHITE);
        updateButton.setFocusPainted(false);

        resetButton = new JButton("Reset");
        resetButton.setFont(new Font("Arial", Font.BOLD, 14));
        resetButton.setBackground(new Color(200, 50, 50));
        resetButton.setForeground(Color.WHITE);
        resetButton.setFocusPainted(false);

        updateButton.addActionListener(this);
        resetButton.addActionListener(this);

        btnPanel.add(updateButton);
        btnPanel.add(resetButton);

        add(statusLabel, BorderLayout.CENTER);
        add(btnPanel,    BorderLayout.SOUTH);
        add(new JLabel("  UIT-RGPV IT-408 Swing Demo  ", JLabel.CENTER), BorderLayout.NORTH);

        setLocationRelativeTo(null);   // center on screen
        setVisible(true);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == updateButton) {
            clickCount++;
            statusLabel.setText("Button clicked " + clickCount + " time(s)! -- Java Swing");
            statusLabel.setForeground(new Color(0, 100, 200));
        } else if (e.getSource() == resetButton) {
            clickCount = 0;
            statusLabel.setText("Label reset. Click Update again.");
            statusLabel.setForeground(Color.DARK_GRAY);
        }
    }

    public static void main(String[] args) {
        // Swing components must be created on the Event Dispatch Thread (EDT)
        SwingUtilities.invokeLater(() -> new SwingLabelButtonDemo());
    }
}
""",
    lang="java",
)

pn.tip(
    "AWT vs Swing key difference: AWT uses native OS controls (heavyweight); "
    "Swing paints its own controls (lightweight, consistent appearance). "
    "Swing is preferred because it offers richer components (JTable, JTree, JTabbedPane), "
    "pluggable Look and Feel, and consistent cross-platform appearance. "
    "Always create Swing GUIs on the Event Dispatch Thread using SwingUtilities.invokeLater()."
)
pn.br()

# #############################################################################
#  QUESTION 5 -- CO5: EVENT HANDLING & JDBC
# #############################################################################
pn.part_box("QUESTION 5 -- CO5: EVENT HANDLING & JDBC DATABASE CONNECTIVITY")

# -----------------------------------------------------------------------------
#  Q5(a) -- 3 Marks
# -----------------------------------------------------------------------------
pn.chap_box(
    "Q5(a) [3 Marks] -- Window/AWT Event | Delegation Event Model Components | Event Handling | Two Mechanisms\n"
    "(May-June 2025 | July-Dec 2024 | June 2022 | May-June 2024)"
)

pn.section("Purpose of the WindowEvent in Java")
pn.definition(
    "<b>WindowEvent (java.awt.event.WindowEvent):</b> Generated by a Frame or Window "
    "when a window-level operation occurs -- such as the user clicking the close button, "
    "minimizing, maximizing, or restoring the window. The most commonly handled method "
    "is <code>windowClosing()</code> which is triggered when the user clicks the X button. "
    "Without handling this event (or setting <code>EXIT_ON_CLOSE</code> in Swing), "
    "clicking X would NOT close the application."
)
pn.info_table(
    ["WindowListener Method", "Purpose"],
    [
        [
            "windowOpened(e)",
            "Called when window is first shown (after setVisible(true))",
        ],
        [
            "windowClosing(e)",
            "Called when user clicks the X button -- use to call dispose() and System.exit()",
        ],
        ["windowClosed(e)", "Called after window is disposed/destroyed"],
        ["windowIconified(e)", "Called when window is minimized to taskbar"],
        ["windowDeiconified(e)", "Called when window is restored from taskbar"],
        ["windowActivated(e)", "Called when window gains focus"],
        ["windowDeactivated(e)", "Called when window loses focus"],
    ],
)

pn.section("Key Components of the Delegation Event Model")
pn.definition(
    "<b>Delegation Event Model:</b> Introduced in Java 1.1. An event handling architecture "
    "where events generated by a source component are <i>delegated</i> to a separate "
    "listener object for processing. The three key components are:"
)
pn.bullet(
    [
        "<b>Event Source:</b> The GUI component that generates the event "
        "(e.g., Button, TextField, Frame). It maintains a list of registered listeners "
        "and notifies them when an event occurs.",
        "<b>Event Object:</b> An object encapsulating all information about the event -- "
        "the source component, timestamp, type, and event-specific data "
        "(e.g., ActionEvent, MouseEvent, KeyEvent).",
        "<b>Event Listener:</b> An object implementing a listener interface "
        "(e.g., ActionListener, MouseListener) that is registered with the source "
        "and whose callback method is invoked when the event fires.",
    ]
)

pn.section("Two Event Handling Mechanisms in Java")
pn.info_table(
    ["Mechanism", "Java Version", "Approach", "Limitation"],
    [
        [
            "Old Model (Inheritance-based)",
            "Java 1.0",
            "The component itself handled events by overriding action() or handleEvent() methods. "
            "Every event bubbled up through the component hierarchy regardless of interest.",
            "Tight coupling -- component and handler merged. ALL events processed even if unneeded. "
            "Hard to maintain for large GUIs.",
        ],
        [
            "New Model (Delegation)",
            "Java 1.1+",
            "Events delegated from source to separate registered listener objects. "
            "Only interested listeners receive events (efficient). "
            "Source and handler are separate classes (loose coupling).",
            "None -- this is the standard and correct approach.",
        ],
    ],
)

# -----------------------------------------------------------------------------
#  Q5(b) -- 4 Marks
# -----------------------------------------------------------------------------
pn.chap_box(
    "Q5(b) [4 Marks] -- Two Event Types in Delegation Model | JDBC-ODBC Bridge | Mouse Event Class\n"
    "(May-June 2025 | July-Dec 2024 | June 2022 | May-June 2024)"
)

pn.section("Two Types of Events in the Delegation Model")
pn.info_table(
    ["Event Category", "Description", "Examples"],
    [
        [
            "Semantic Events",
            "Higher-level events representing a meaningful action (what the user intended). "
            "They abstract away the low-level input mechanism and focus on the logical action. "
            "These are the events you usually handle in application code.",
            "ActionEvent (button click / Enter key), ItemEvent (checkbox toggle), "
            "TextEvent (text changed), AdjustmentEvent (scrollbar moved)",
        ],
        [
            "Low-level Events",
            "Lower-level events representing raw input device interactions. "
            "They are the foundation from which semantic events are derived. "
            "Handle these when you need granular control over input.",
            "MouseEvent (click/move/drag/enter/exit), KeyEvent (key press/release), "
            "FocusEvent (focus gained/lost), WindowEvent (open/close/minimize), "
            "ComponentEvent (resize/move/show/hide)",
        ],
    ],
)

pn.section("Role of JDBC-ODBC Bridge")
pn.definition(
    "<b>JDBC-ODBC Bridge (Type 1 Driver):</b> One of four JDBC driver types, the bridge "
    "provides connectivity between JDBC (Java Database Connectivity) API calls and "
    "the ODBC (Open Database Connectivity) standard. It translates JDBC method calls "
    "into ODBC function calls, which then communicate with the database. "
    "<b>The bridge was removed in Java 8.</b> It was useful for connecting to "
    "databases that only had ODBC drivers (e.g., Microsoft Access, Excel via DSN)."
)
pn.bullet(
    [
        "<b>Architecture:</b> Java App -> JDBC API -> JDBC-ODBC Bridge Driver -> ODBC Driver -> Database",
        "<b>Platform:</b> Windows-only (ODBC is a Windows technology).",
        "<b>Performance:</b> Slowest of the four types -- multiple translation layers.",
        "<b>Modern Alternative:</b> Use Type 4 (Pure Java Thin Driver) like MySQL Connector/J for direct JDBC-to-DB connectivity.",
    ]
)

pn.section("The Mouse Event Class -- Complete Demonstration")
pn.code_block(
    """
// MouseEventClassDemo.java -- Demonstrates all MouseEvent methods
import java.awt.*;
import java.awt.event.*;

public class MouseEventClassDemo extends Frame
        implements MouseListener, MouseMotionListener {

    String eventInfo  = "No event yet";
    int    mouseX = 0, mouseY = 0;
    int    clickCount = 0;
    boolean dragging  = false;

    public MouseEventClassDemo() {
        super("MouseEvent Demo -- IT408 CO5");
        setSize(500, 350);
        setBackground(Color.WHITE);

        // Register both listener types on the frame
        addMouseListener(this);
        addMouseMotionListener(this);

        addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent e) { dispose(); System.exit(0); }
        });
        setVisible(true);
    }

    @Override
    public void paint(Graphics g) {
        g.setFont(new Font("Courier", Font.BOLD, 13));
        g.setColor(Color.DARK_GRAY);
        g.drawString("Mouse Position: (" + mouseX + ", " + mouseY + ")", 20, 60);
        g.drawString("Last Event:     " + eventInfo, 20, 85);
        g.drawString("Total Clicks:   " + clickCount, 20, 110);
        g.drawString("Dragging:       " + (dragging ? "YES" : "NO"), 20, 135);

        // Show a cross-hair at mouse position
        g.setColor(Color.RED);
        g.drawLine(mouseX - 10, mouseY, mouseX + 10, mouseY);
        g.drawLine(mouseX, mouseY - 10, mouseX, mouseY + 10);
        g.drawOval(mouseX - 5, mouseY - 5, 10, 10);
    }

    // -- MouseListener -- 5 methods ------------------------------------------
    @Override
    public void mouseClicked(MouseEvent e) {
        clickCount++;
        mouseX = e.getX();
        mouseY = e.getY();
        eventInfo = "CLICKED (count=" + e.getClickCount() + ", button=" + e.getButton() + ")";
        repaint();
    }

    @Override
    public void mousePressed(MouseEvent e) {
        eventInfo = "PRESSED at (" + e.getX() + "," + e.getY() + ")";
        repaint();
    }

    @Override
    public void mouseReleased(MouseEvent e) {
        dragging  = false;
        eventInfo = "RELEASED at (" + e.getX() + "," + e.getY() + ")";
        repaint();
    }

    @Override
    public void mouseEntered(MouseEvent e) {
        eventInfo = "ENTERED applet area";
        repaint();
    }

    @Override
    public void mouseExited(MouseEvent e)  {
        eventInfo = "EXITED applet area";
        repaint();
    }

    // -- MouseMotionListener -- 2 methods ------------------------------------
    @Override
    public void mouseMoved(MouseEvent e) {
        mouseX = e.getX();
        mouseY = e.getY();
        eventInfo = "MOVED";
        repaint();
    }

    @Override
    public void mouseDragged(MouseEvent e) {
        mouseX    = e.getX();
        mouseY    = e.getY();
        dragging  = true;
        eventInfo = "DRAGGING";
        repaint();
    }

    public static void main(String[] args) { new MouseEventClassDemo(); }
}
""",
    lang="java",
)

# -----------------------------------------------------------------------------
#  Q5(c) -- 4 Marks
# -----------------------------------------------------------------------------
pn.chap_box(
    "Q5(c) [4 Marks] -- ResultSet Object | Comparing Event Models | Delegation Event Model | Advantages\n"
    "(May-June 2025 | July-Dec 2024 | June 2022 | May-June 2024)"
)

pn.section("ResultSet Object and How It Is Used")
pn.definition(
    "<b>ResultSet (java.sql.ResultSet):</b> An object that represents the tabular "
    "result set of a SQL query executed via JDBC. It acts as a cursor that points to "
    "rows of data returned by a SELECT statement. Initially the cursor is positioned "
    "<b>BEFORE the first row</b>. You call <code>next()</code> to advance the cursor "
    "one row forward and retrieve data from columns using type-specific getter methods."
)
pn.info_table(
    ["ResultSet Method", "Return Type", "Description"],
    [
        [
            "next()",
            "boolean",
            "Moves cursor to next row. Returns true if row exists, false if no more rows.",
        ],
        ["getString(columnName/Index)", "String", "Returns column value as String."],
        ["getInt(columnName/Index)", "int", "Returns column value as int."],
        ["getDouble(columnName/Index)", "double", "Returns column value as double."],
        ["getBoolean(columnName/Index)", "boolean", "Returns column value as boolean."],
        ["getDate(columnName)", "java.sql.Date", "Returns column value as SQL Date."],
        ["previous()", "boolean", "Moves cursor backward (scrollable ResultSet)."],
        [
            "first() / last()",
            "boolean",
            "Jump to first / last row (scrollable ResultSet).",
        ],
        ["absolute(int n)", "boolean", "Jump to row number n (scrollable ResultSet)."],
        [
            "getMetaData()",
            "ResultSetMetaData",
            "Get column names, types, and count of the result set.",
        ],
        [
            "close()",
            "void",
            "Releases ResultSet resources. Always call in finally block.",
        ],
    ],
)
pn.code_block(
    """
// ResultSet usage example
ResultSet rs = stmt.executeQuery("SELECT id, name, marks FROM students");
while (rs.next()) {                          // iterate rows
    int    id    = rs.getInt("id");          // get int column by name
    String name  = rs.getString("name");     // get String column by name
    double marks = rs.getDouble("marks");    // get double column by name
    System.out.printf("ID: %d | Name: %-15s | Marks: %.1f%n", id, name, marks);
}
rs.close();
""",
    lang="java",
)

pn.section("Delegation Event Model -- Advantages")
pn.bullet(
    [
        "<b>Separation of Concerns:</b> Event source and event handler are separate classes. "
        "The Button doesn't need to know how its click is processed.",
        "<b>Multiple Handlers per Source:</b> One component can have multiple listeners registered "
        "(e.g., a button can trigger both a UI update AND a database save).",
        "<b>One Handler for Multiple Sources:</b> A single listener can handle events from "
        "multiple components (checking <code>e.getSource()</code>).",
        "<b>Efficiency:</b> Only listeners explicitly registered receive events -- no "
        "unnecessary event bubbling to every component.",
        "<b>Flexibility:</b> Listeners can be added/removed at runtime using "
        "<code>addXxxListener()</code> and <code>removeXxxListener()</code>.",
        "<b>Testability:</b> Listener classes can be unit-tested independently of the GUI components.",
    ]
)

pn.section("Comparing Old (Inheritance) vs New (Delegation) Event Model")
pn.info_table(
    ["Criterion", "Old Model (Java 1.0)", "New Delegation Model (Java 1.1+)"],
    [
        [
            "Who handles events",
            "The component itself (by subclassing)",
            "Separate listener objects",
        ],
        [
            "Method overridden",
            "action() or handleEvent()",
            "Listener interface methods (e.g., actionPerformed)",
        ],
        [
            "Coupling",
            "Tight -- source and handler merged",
            "Loose -- source and handler separated",
        ],
        [
            "Efficiency",
            "Poor -- ALL events bubble up",
            "Good -- only interested listeners notified",
        ],
        [
            "Flexibility",
            "Low -- can't add/remove handlers",
            "High -- dynamic registration/deregistration",
        ],
        [
            "Multiple handlers",
            "Not possible",
            "Multiple listeners per source supported",
        ],
    ],
)

# -----------------------------------------------------------------------------
#  Q5(d) -- 10 Marks
# -----------------------------------------------------------------------------
pn.chap_box(
    "Q5(d) [10 Marks] -- JDBC Remote Database Connection | ActionListener AWT Program | JDBC Driver Types\n"
    "(May-June 2025 | July-Dec 2024 | June 2022 | May-June 2024)"
)

pn.section("JDBC Architecture -- Overview")

net_jdbc = pd.NetworkDiagram(
    width=pn.CW,
    height=240,
    theme=diag_theme,
    caption="Fig 5.1: JDBC Architecture -- Java Application to Remote Database",
)
# 5 nodes spread evenly across two rows to fit within page width
# Row 1: App -> JDBC API -> DriverManager
net_jdbc.node("app", "Java Application\n(Your Code)", x=70, y=90, kind="host")
net_jdbc.node("api", "JDBC API\n(java.sql.*)", x=210, y=90, kind="server")
net_jdbc.node("dm", "DriverManager\n(loads drivers)", x=360, y=90, kind="server")
# Row 2: Driver -> Remote DB
net_jdbc.node("drv", "JDBC Driver\n(Type 4 / Thin)", x=210, y=185, kind="generic")
net_jdbc.node("db", "Remote Database\n(MySQL/Oracle)", x=360, y=185, kind="database")

net_jdbc.link("app", "api", bidirectional=False, label="calls")
net_jdbc.link("api", "dm", bidirectional=False, label="delegates")
net_jdbc.link("dm", "drv", bidirectional=False, label="loads")
net_jdbc.link("drv", "db", bidirectional=True, label="SQL / Results")
pn.story.extend(net_jdbc.as_flowable())

pn.section("Four Types of JDBC Drivers")
pn.info_table(
    ["Type", "Name", "Mechanism", "Use Case"],
    [
        [
            "Type 1",
            "JDBC-ODBC Bridge",
            "Translates JDBC to ODBC calls. Removed in Java 8.",
            "Legacy Windows databases (deprecated)",
        ],
        [
            "Type 2",
            "Native API Driver",
            "Uses native DB client library (C/C++). Partially Java.",
            "Oracle OCI driver, DB2 legacy",
        ],
        [
            "Type 3",
            "Network Protocol Driver",
            "Pure Java. Translates JDBC to DB-independent middleware protocol.",
            "Multi-database middleware servers",
        ],
        [
            "Type 4",
            "Thin Driver (Pure Java)",
            "Pure Java. Translates JDBC calls directly to DB network protocol (e.g., MySQL Wire Protocol).",
            "Recommended: MySQL Connector/J, PostgreSQL JDBC, Oracle JDBC Thin",
        ],
    ],
)

pn.section("JDBC Connection Process -- Step by Step")
pn.bullet(
    [
        '<b>Step 1 -- Load Driver:</b> <code>Class.forName("com.mysql.cj.jdbc.Driver")</code> -- registers the driver with DriverManager. (Optional in JDBC 4.0+ -- auto-loaded via ServiceLoader.)',
        "<b>Step 2 -- Get Connection:</b> <code>Connection con = DriverManager.getConnection(url, user, password)</code>",
        "<b>Step 3 -- Create Statement:</b> <code>Statement stmt = con.createStatement()</code> for static SQL.",
        "<b>Step 4 -- Execute Query:</b> <code>ResultSet rs = stmt.executeQuery(sql)</code> for SELECT; <code>stmt.executeUpdate(sql)</code> for INSERT/UPDATE/DELETE.",
        "<b>Step 5 -- Process Results:</b> Iterate <code>rs</code> with <code>while(rs.next())</code> and get values with <code>rs.getString(), rs.getInt()</code>.",
        "<b>Step 6 -- Close Resources:</b> Always close in finally: <code>rs.close(); stmt.close(); con.close();</code>",
    ]
)

pn.section("Complete Java Program -- Connect to Remote MySQL Database")
pn.code_block(
    """
// JDBCRemoteConnection.java -- Connect to remote MySQL database using JDBC
// Required: MySQL Connector/J JAR in classpath
// Compile: javac -cp mysql-connector-j-8.x.x.jar JDBCRemoteConnection.java
// Run:     java  -cp .;mysql-connector-j-8.x.x.jar JDBCRemoteConnection

import java.sql.*;

public class JDBCRemoteConnection {

    // -- Connection parameters ------------------------------------------------
    // Format: jdbc:mysql://<host>:<port>/<database>?params
    static final String DB_URL  = "jdbc:mysql://192.168.1.100:3306/college_db"
                                + "?useSSL=true&serverTimezone=UTC";
    static final String DB_USER = "admin_user";
    static final String DB_PASS = "SecurePass@2024";

    public static void main(String[] args) {

        Connection con  = null;
        Statement  stmt = null;
        ResultSet  rs   = null;

        try {
            // STEP 1: Load JDBC driver (optional in JDBC 4.0+ but good practice)
            Class.forName("com.mysql.cj.jdbc.Driver");
            System.out.println("Driver loaded successfully.");

            // STEP 2: Establish connection to remote database
            con = DriverManager.getConnection(DB_URL, DB_USER, DB_PASS);
            System.out.println("Connected to remote database: " + con.getCatalog());

            // STEP 3: Create Statement object
            stmt = con.createStatement();

            // -- INSERT (executeUpdate) ----------------------------------------
            int inserted = stmt.executeUpdate(
                "INSERT INTO students (name, rollno, marks) " +
                "VALUES ('Priya Sharma', 101, 88.5)"
            );
            System.out.println("Rows inserted: " + inserted);

            // -- SELECT (executeQuery) -----------------------------------------
            rs = stmt.executeQuery(
                "SELECT id, name, rollno, marks FROM students ORDER BY marks DESC"
            );

            System.out.println("\n=== Student Records (sorted by marks) ===");
            System.out.printf("%-5s %-20s %-8s %-8s%n", "ID", "Name", "RollNo", "Marks");
            System.out.println("-".repeat(45));

            // STEP 5: Process ResultSet row by row
            while (rs.next()) {
                int    id     = rs.getInt("id");
                String name   = rs.getString("name");
                int    rollno = rs.getInt("rollno");
                double marks  = rs.getDouble("marks");
                System.out.printf("%-5d %-20s %-8d %-8.1f%n", id, name, rollno, marks);
            }

            // -- PreparedStatement (prevents SQL Injection) --------------------
            System.out.println("\nUsing PreparedStatement (safe for user input):");
            PreparedStatement pstmt = con.prepareStatement(
                "SELECT name, marks FROM students WHERE marks > ?"
            );
            pstmt.setDouble(1, 75.0);   // set parameter -- avoids SQL injection
            ResultSet rs2 = pstmt.executeQuery();
            while (rs2.next()) {
                System.out.println("  " + rs2.getString("name") +
                                   " -- " + rs2.getDouble("marks"));
            }
            rs2.close();
            pstmt.close();

        } catch (ClassNotFoundException e) {
            System.err.println("Driver not found: " + e.getMessage());
            System.err.println("Ensure MySQL Connector/J JAR is in classpath.");
        } catch (SQLException e) {
            System.err.println("SQL Error [" + e.getErrorCode() + "]: " + e.getMessage());
            System.err.println("SQLState: " + e.getSQLState());
        } finally {
            // STEP 6: Always close resources in reverse order (ResultSet -> Stmt -> Con)
            try {
                if (rs   != null) rs.close();
                if (stmt != null) stmt.close();
                if (con  != null) con.close();
                System.out.println("\nDatabase connection closed cleanly.");
            } catch (SQLException e) {
                System.err.println("Error closing resources: " + e.getMessage());
            }
        }
    }
}
""",
    lang="java",
)

pn.section("ActionListener Program -- Handling Button Click Events in AWT")
pn.code_block(
    """
// ActionListenerDemo.java -- ActionListener for button click events
import java.awt.*;
import java.awt.event.*;

public class ActionListenerDemo extends Frame implements ActionListener {

    // Components
    Button   btnAdd, btnClear, btnExit;
    TextField tfName, tfScore;
    TextArea  taResults;
    Label     lblStatus;
    int       totalStudents = 0;
    double    totalMarks    = 0;

    public ActionListenerDemo() {
        super("ActionListener Demo -- Student Score Tracker");
        setSize(500, 400);
        setLayout(new BorderLayout(8, 8));

        // -- Input Panel (NORTH) ----------------------------------------------
        Panel inputPanel = new Panel(new GridLayout(2, 2, 5, 5));
        inputPanel.add(new Label("Student Name:"));
        tfName  = new TextField(20);
        inputPanel.add(tfName);
        inputPanel.add(new Label("Score (0-100):"));
        tfScore = new TextField(5);
        inputPanel.add(tfScore);

        // -- Button Panel -----------------------------------------------------
        Panel btnPanel = new Panel(new FlowLayout(FlowLayout.CENTER, 10, 5));
        btnAdd   = new Button("Add Student");
        btnClear = new Button("Clear All");
        btnExit  = new Button("Exit");

        // Register THIS class as ActionListener for all buttons
        btnAdd.addActionListener(this);
        btnClear.addActionListener(this);
        btnExit.addActionListener(this);

        btnPanel.add(btnAdd);
        btnPanel.add(btnClear);
        btnPanel.add(btnExit);

        // -- Results Display (CENTER) -----------------------------------------
        taResults = new TextArea("=== Student Records ===\n", 10, 50,
                                  TextArea.SCROLLBARS_VERTICAL_ONLY);
        taResults.setFont(new Font("Courier", Font.PLAIN, 12));
        taResults.setEditable(false);

        // -- Status Bar (SOUTH) -----------------------------------------------
        lblStatus = new Label("Ready. Enter student name and score.", Label.CENTER);
        lblStatus.setBackground(Color.LIGHT_GRAY);

        // Assemble layout
        Panel northPanel = new Panel(new BorderLayout());
        northPanel.add(inputPanel, BorderLayout.CENTER);
        northPanel.add(btnPanel,   BorderLayout.SOUTH);

        add(northPanel,  BorderLayout.NORTH);
        add(taResults,   BorderLayout.CENTER);
        add(lblStatus,   BorderLayout.SOUTH);

        addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent e) { System.exit(0); }
        });
        setVisible(true);
    }

    // -- ActionListener callback ----------------------------------------------
    @Override
    public void actionPerformed(ActionEvent e) {
        Object src = e.getSource();   // identify which component fired

        if (src == btnAdd) {
            String name  = tfName.getText().trim();
            String scoreText = tfScore.getText().trim();

            if (name.isEmpty() || scoreText.isEmpty()) {
                lblStatus.setText("Error: Name and Score cannot be empty!");
                return;
            }
            try {
                double score = Double.parseDouble(scoreText);
                if (score < 0 || score > 100) { lblStatus.setText("Score must be 0-100!"); return; }
                totalStudents++;
                totalMarks += score;
                String grade = score >= 90 ? "A+" : score >= 80 ? "A" : score >= 70 ? "B"
                             : score >= 60 ? "C"  : score >= 50 ? "D" : "F";
                taResults.append(String.format("#%d %-20s Score: %5.1f  Grade: %s%n",
                                               totalStudents, name, score, grade));
                taResults.append(String.format("    Avg so far: %.2f (%d students)%n",
                                               totalMarks / totalStudents, totalStudents));
                lblStatus.setText("Added: " + name + " | Score: " + score);
                tfName.setText(""); tfScore.setText(""); tfName.requestFocus();
            } catch (NumberFormatException ex) {
                lblStatus.setText("Invalid score -- enter a number (e.g. 75.5)");
            }
        } else if (src == btnClear) {
            taResults.setText("=== Student Records ===\n");
            totalStudents = 0; totalMarks = 0;
            lblStatus.setText("All records cleared.");
        } else if (src == btnExit) {
            dispose(); System.exit(0);
        }
    }

    public static void main(String[] args) { new ActionListenerDemo(); }
}
""",
    lang="java",
)

pn.tip(
    "JDBC exam tip: The 6 steps are: Load Driver -> getConnection -> createStatement -> "
    "executeQuery/Update -> process ResultSet -> close resources. "
    "Type 4 (Pure Java Thin Driver) is the recommended driver type today. "
    "Always close resources in finally block or use try-with-resources. "
    "Use PreparedStatement for parameterized queries to prevent SQL injection."
)

# -----------------------------------------------------------------------------
#  Q5(e) -- 10 Marks
# -----------------------------------------------------------------------------
pn.chap_box(
    "Q5(e) [10 Marks] -- Short Notes: Exception Handling | Constructor | Access Specifiers | Abstract Class\n"
    "(May-June 2025 | May-June 2024 -- SAME QUESTION | July-Dec 2024 JDBC | June 2022 JDBC SQL)"
)

pn.section("Short Note (a): Exception Handling in Java")
pn.definition(
    "<b>Exception Handling</b> is Java's structured mechanism for detecting, reporting, "
    "and recovering from runtime errors (exceptions) without abnormal program termination. "
    "An <b>exception</b> is an abnormal condition that disrupts normal program flow. "
    "Java's exception hierarchy has <code>Throwable</code> as root, with two branches: "
    "<code>Error</code> (JVM-level, unrecoverable) and <code>Exception</code> (program-level)."
)
pn.info_table(
    ["Keyword", "Purpose"],
    [
        [
            "try",
            "Encloses code that might throw an exception. Must have at least one catch or finally.",
        ],
        [
            "catch (ExType e)",
            "Catches and handles a specific exception type. Multiple catch blocks allowed (most specific first).",
        ],
        [
            "finally",
            "Always executes -- whether exception occurred or not. Used for cleanup (close files, DB connections).",
        ],
        [
            "throw",
            'Manually throw an exception: throw new IllegalArgumentException("msg")',
        ],
        [
            "throws",
            "Declares checked exceptions a method may throw: public void read() throws IOException",
        ],
    ],
)
pn.code_block(
    """
// Exception types
try {
    int[] arr = new int[5];
    arr[10] = 100;                    // ArrayIndexOutOfBoundsException (unchecked)
} catch (ArrayIndexOutOfBoundsException e) {
    System.out.println("Caught: " + e.getMessage());
} finally {
    System.out.println("Cleanup in finally.");
}

// Checked exception (must be handled or declared)
try {
    java.io.FileReader fr = new java.io.FileReader("data.txt");  // may throw FileNotFoundException
} catch (java.io.FileNotFoundException e) {
    System.out.println("File not found: " + e.getMessage());
}
""",
    lang="java",
)

pn.section("Short Note (b): Constructors in Java")
pn.definition(
    "<b>Constructor</b> is a special method that is automatically invoked when an object "
    "is created using <code>new</code>. It initializes the newly created object's state. "
    "Key rules: (1) Name must match class name. (2) No return type (not even void). "
    "(3) Multiple constructors allowed (constructor overloading). "
    "(4) If no constructor is written, Java provides a default no-arg constructor automatically -- "
    "but only if you define ZERO constructors."
)
pn.info_table(
    ["Type", "Description", "Example"],
    [
        [
            "Default (no-arg)",
            "No parameters. Java auto-provides if you write none.",
            'Book() { title="Unknown"; }',
        ],
        [
            "Parameterized",
            "Takes arguments to set initial field values.",
            "Book(String t, double p) { title=t; price=p; }",
        ],
        [
            "Copy Constructor",
            "Accepts object of same class; copies all fields.",
            "Book(Book other) { this.title=other.title; }",
        ],
    ],
)

pn.section("Short Note (c): Access Specifiers in Java")
pn.definition(
    "<b>Access Specifiers</b> (Access Modifiers) control the visibility and accessibility "
    "of classes, methods, and variables. Java has four levels of access control."
)
pn.info_table(
    ["Specifier", "Same Class", "Same Package", "Subclass (diff pkg)", "Other Package"],
    [
        ["private", "YES", "NO", "NO", "NO"],
        ["(default)", "YES", "YES", "NO", "NO"],
        ["protected", "YES", "YES", "YES", "NO"],
        ["public", "YES", "YES", "YES", "YES"],
    ],
)
pn.bullet(
    [
        "<b>private:</b> Most restrictive. Used for data hiding (encapsulation). Fields should typically be private.",
        "<b>default (package-private):</b> No modifier written. Visible within the same package only.",
        "<b>protected:</b> Like default, but also accessible to subclasses in other packages.",
        "<b>public:</b> No restrictions. Accessible from anywhere.",
    ]
)

pn.section("Short Note (d): Abstract Class in Java")
pn.definition(
    "<b>Abstract Class</b> is a class declared with the <code>abstract</code> keyword that "
    "<b>cannot be instantiated</b> directly (cannot do <code>new AbstractClass()</code>). "
    "It serves as an incomplete blueprint: it can define common concrete methods "
    "AND declare abstract methods (body-less methods) that concrete subclasses MUST implement. "
    "Abstract classes enable the <b>Template Method</b> design pattern."
)
pn.info_table(
    ["Property", "Abstract Class", "Interface"],
    [
        ["Instantiation", "Cannot be instantiated", "Cannot be instantiated"],
        [
            "Methods",
            "Can have concrete + abstract methods",
            "All methods abstract by default (Java 7); default/static allowed (Java 8+)",
        ],
        ["Fields", "Can have instance variables", "Only public static final constants"],
        [
            "Constructor",
            "CAN have constructors (called via super())",
            "Cannot have constructors",
        ],
        [
            "Inheritance",
            "Single -- extends one abstract class",
            "Multiple -- class can implement many interfaces",
        ],
        [
            "Access Modifiers",
            "Methods can be any access level",
            "All methods implicitly public",
        ],
    ],
)
pn.code_block(
    """
// Abstract class example
abstract class Vehicle {
    int speed;                              // instance variable -- allowed
    Vehicle(int speed) { this.speed = speed; }   // constructor -- allowed

    abstract void fuel();                   // abstract method -- subclass MUST implement
    void describe() {                       // concrete method -- inherited as-is
        System.out.println("Speed: " + speed + " km/h");
    }
}

class Car extends Vehicle {
    Car(int s) { super(s); }
    @Override
    void fuel() { System.out.println("Car uses petrol/diesel."); }
}

class ElectricBike extends Vehicle {
    ElectricBike(int s) { super(s); }
    @Override
    void fuel() { System.out.println("Electric bike uses lithium battery."); }
}

// Vehicle v = new Vehicle(100);  // COMPILE ERROR -- cannot instantiate abstract class
Vehicle v1 = new Car(120);         // OK -- concrete subclass reference
Vehicle v2 = new ElectricBike(80);
v1.fuel(); v1.describe();
v2.fuel(); v2.describe();
""",
    lang="java",
)

pn.section("Q5(e) Alternative: Executing SQL Statements and Processing Results in JDBC")
pn.code_block(
    """
// JDBCSQLExecutionDemo.java -- Complete SQL execution and ResultSet processing
import java.sql.*;

public class JDBCSQLExecutionDemo {

    public static void main(String[] args) throws Exception {
        // Connect to local MySQL (change host/db for remote)
        String url  = "jdbc:mysql://localhost:3306/college_db?useSSL=false&serverTimezone=UTC";
        Connection con  = DriverManager.getConnection(url, "root", "password");
        Statement  stmt = con.createStatement(
            ResultSet.TYPE_SCROLL_INSENSITIVE,   // scrollable -- can go forward/backward
            ResultSet.CONCUR_READ_ONLY
        );

        // -- CREATE TABLE ---------------------------------------------------
        stmt.executeUpdate(
            "CREATE TABLE IF NOT EXISTS students " +
            "(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), marks DOUBLE)"
        );

        // -- INSERT rows ---------------------------------------------------
        stmt.executeUpdate("INSERT INTO students (name, marks) VALUES ('Alice', 92.5)");
        stmt.executeUpdate("INSERT INTO students (name, marks) VALUES ('Bob', 78.0)");
        stmt.executeUpdate("INSERT INTO students (name, marks) VALUES ('Carol', 85.5)");
        System.out.println("3 records inserted.");

        // -- SELECT and process ResultSet ----------------------------------
        ResultSet rs = stmt.executeQuery("SELECT * FROM students ORDER BY marks DESC");

        // Get metadata (column info)
        ResultSetMetaData meta = rs.getMetaData();
        int cols = meta.getColumnCount();
        System.out.print("Columns: ");
        for (int c = 1; c <= cols; c++) System.out.print(meta.getColumnName(c) + " | ");
        System.out.println();

        // Iterate forward through rows
        System.out.println("\n=== All Students (Best to Worst) ===");
        while (rs.next()) {
            System.out.printf("ID:%-3d  Name:%-10s  Marks:%.1f%n",
                rs.getInt(1), rs.getString(2), rs.getDouble(3));
        }

        // Scroll back to first row (TYPE_SCROLL_INSENSITIVE)
        rs.first();
        System.out.println("\nTop student: " + rs.getString("name") + " (" + rs.getDouble("marks") + ")");

        // -- UPDATE --------------------------------------------------------
        int updated = stmt.executeUpdate("UPDATE students SET marks=95.0 WHERE name='Alice'");
        System.out.println("\nRows updated: " + updated);

        // -- DELETE --------------------------------------------------------
        int deleted = stmt.executeUpdate("DELETE FROM students WHERE marks < 80");
        System.out.println("Rows deleted: " + deleted);

        // Final SELECT
        rs = stmt.executeQuery("SELECT * FROM students");
        System.out.println("\n=== Remaining Records ===");
        while (rs.next())
            System.out.printf("ID:%-3d  %s  %.1f%n", rs.getInt(1), rs.getString(2), rs.getDouble(3));

        rs.close(); stmt.close(); con.close();
    }
}
""",
    lang="java",
)

pn.section("Delegation Event Model -- Sequence Diagram")

seq = pd.SequenceDiagram(
    width=pn.CW,
    height=260,
    caption="Fig 5.2: Delegation Event Model -- User Action to Listener Callback Flow",
    theme=diag_theme,
)
seq.actor("src", "Button\n(Source)")
seq.actor("edt", "AWT Event\nDispatch Thread")
seq.actor("lst", "ActionListener\n(Handler)")
seq.message("src", "edt", "actionPerformed event fired")
seq.divider("loop [for each registered listener]")
seq.message("edt", "edt", "look up registered listeners")
seq.message("edt", "lst", "actionPerformed(ActionEvent e)")
seq.message("lst", "edt", "update label / do logic")
seq.divider("end loop")
pn.story.extend(seq.as_flowable())

pn.tip(
    "Q5(e) Short Note memory aid: "
    "Exception = try-catch-finally-throw-throws. "
    "Constructor = same name as class, no return type, called by 'new'. "
    "Access = private(class) < default(package) < protected(+subclass) < public(everywhere). "
    "Abstract = cannot instantiate, has abstract methods, subclass MUST implement all."
)
pn.br()

# =============================================================================
#  BUILD THE PDF
# =============================================================================
pn.build_doc("Java_PYQ_Answers.pdf")
