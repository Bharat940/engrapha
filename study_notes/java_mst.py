import engrapha_notes as en
import engrapha_diagrams as ed

# -- Setup --------------------------------------------------------------------
en.set_story([])
en.set_theme(en.DARK)
en.set_global_footer(
    left="Java Programming (IT-408) -- MST Answers",
    right="UIT-RGPV (Autonomous) Bhopal",
    show_page_num=True,
)
diag_theme = ed.DiagramTheme.from_notes_theme(en.get_theme())
CW = en.CW

# ============================================================
#  COVER PAGE
# ============================================================
en.suppress_footer(page_only=True)
en.cover_card(
    "Java Programming (IT-408)",
    "Mid-Semester Test -- Compiled Answers",
)
# en.cover_subtitle(
#     [
#         "Department of Information Technology",
#         "UIT-RGPV (Autonomous), Bhopal",
#         "",
#         "MST-I   |  March 2026  |  Max Marks: 30  |  Time: 1 Hr",
#         "MST-II  |  April 2026  |  Max Marks: 30  |  Time: 1 Hr",
#         "MST-III |  May 2026    |  Max Marks: 30  |  Time: 1 Hr",
#     ]
# )

en.sp(16)
en.info_table(
    ["MST Paper", "Date", "Max Marks", "Duration", "Topics Covered"],
    [
        [
            "MST-I",
            "March 2026",
            "30",
            "1 Hour",
            "Java Basics, Loops, Data Types, Threads, Constructors, Packages",
        ],
        [
            "MST-II",
            "April 2026",
            "30",
            "1 Hour",
            "Applets, AWT Forms, AWT Class Hierarchy",
        ],
        [
            "MST-III",
            "May 2026",
            "30",
            "1 Hour",
            "JDBC, Event Handling, Database Queries",
        ],
    ],
)
en.br()

# ============================================================
#  MST-I
# ============================================================
en.bookmark("MST-I")
en.part_box("MST-I -- March 2026")
en.note(
    "Exam Details: MST-I | Date: March 2026 | Max Marks: 30 | Time: 1 Hour | "
    "Attempt ALL questions. Marks are indicated against each question."
)
en.sp(6)

# -- Q1 [3 Marks] -------------------------------------------------------------
en.bookmark("MST-I Q1")
en.chap_box(
    "Q1 [3 Marks] -- Hello World Program & Java Execution Process\n(MST-I, March 2026)"
)

en.section("Hello World Program")
en.body(
    "The classic first Java program demonstrates the fundamental structure of a Java source file: "
    "a <b>class declaration</b>, a <b>main method</b> (the entry point), and output via "
    "<b>System.out.println()</b>."
)
en.code_block(
    """\
// File: HelloWorld.java
public class HelloWorld {
    // main() is the entry point of every Java application
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
""",
    lang="java",
)

en.section("Key Components Explained")
en.bullet(
    [
        "<b>public class HelloWorld</b> -- Every Java program must have at least one class. "
        "The filename must match the class name (HelloWorld.java).",
        "<b>public static void main(String[] args)</b> -- JVM calls this method to start execution. "
        "'static' means no object is needed; 'String[] args' holds command-line arguments.",
        "<b>System.out.println()</b> -- Prints text to the standard output (console) followed by a newline.",
    ]
)

en.section("Java Execution Process")
en.bullet(
    [
        "<b>Step 1 -- Write Source Code:</b> Save the program as HelloWorld.java.",
        "<b>Step 2 -- Compile:</b> Run <b>javac HelloWorld.java</b>. "
        "The Java compiler (javac) converts source code (.java) into bytecode (.class file).",
        "<b>Step 3 -- Run:</b> Run <b>java HelloWorld</b>. "
        "The Java Virtual Machine (JVM) interprets the bytecode and executes the program.",
    ]
)
en.highlight(
    "javac HelloWorld.java  -->  HelloWorld.class  -->  java HelloWorld  -->  Output"
)

en.subsection("Expected Output")
en.code_block(
    """\
$ javac HelloWorld.java
$ java HelloWorld
Hello, World!
""",
    lang="text",
)
en.sp(8)

# -- Q2 [4 Marks] -------------------------------------------------------------
en.bookmark("MST-I Q2")
en.chap_box("Q2 [4 Marks] -- Loops in Java with Examples\n(MST-I, March 2026)")

en.section("Overview")
en.body(
    "Java provides four types of loops to execute a block of code repeatedly: "
    "<b>while</b>, <b>do-while</b>, <b>for</b>, and the enhanced <b>for-each</b> loop."
)

en.subsection("1. while Loop")
en.body(
    "Executes the body <b>as long as</b> the condition is true. The condition is checked <b>before</b> each iteration."
)
en.code_block(
    """\
int i = 1;
while (i <= 5) {
    System.out.println("while: " + i);
    i++;
}
// Output: 1 2 3 4 5
""",
    lang="java",
)

en.subsection("2. do-while Loop")
en.body(
    "Executes the body <b>at least once</b>, then checks the condition. The condition is checked <b>after</b> each iteration."
)
en.code_block(
    """\
int j = 1;
do {
    System.out.println("do-while: " + j);
    j++;
} while (j <= 5);
// Output: 1 2 3 4 5  (body executes at least once even if condition is false)
""",
    lang="java",
)

en.subsection("3. for Loop")
en.body(
    "Best used when the number of iterations is known. Combines initialization, condition, and update in one line."
)
en.code_block(
    """\
for (int k = 1; k <= 5; k++) {
    System.out.println("for: " + k);
}
// Output: 1 2 3 4 5
""",
    lang="java",
)

en.subsection("4. Enhanced for-each Loop")
en.body(
    "Introduced in Java 5. Used to iterate over arrays and collections without using an index."
)
en.code_block(
    """\
int[] numbers = {10, 20, 30, 40, 50};
for (int num : numbers) {
    System.out.println("for-each: " + num);
}
// Output: 10 20 30 40 50
""",
    lang="java",
)

en.info_table(
    ["Loop", "Condition Check", "Minimum Executions", "Best Used For"],
    [
        ["while", "Before iteration", "0", "Unknown iteration count, condition-driven"],
        ["do-while", "After iteration", "1", "Menu-driven programs, must run once"],
        ["for", "Before iteration", "0", "Known iteration count"],
        ["for-each", "Implicit", "0", "Arrays and Collections traversal"],
    ],
)

en.subsection("Expected Output (all four loops combined)")
en.code_block(
    """\
$ java LoopDemo
while: 1
while: 2
while: 3
while: 4
while: 5
do-while: 1
do-while: 2
do-while: 3
do-while: 4
do-while: 5
for: 1
for: 2
for: 3
for: 4
for: 5
for-each: 10
for-each: 20
for-each: 30
for-each: 40
for-each: 50
""",
    lang="text",
)
en.sp(8)

# -- Q3 [8 Marks] -------------------------------------------------------------
en.bookmark("MST-I Q3")
en.chap_box("Q3 [8 Marks] -- Data Types in Java\n(MST-I, March 2026)")

en.section("Introduction")
en.body(
    "Java is a <b>strongly typed language</b> -- every variable must have a declared type. "
    "Java data types are divided into two main categories: <b>Primitive</b> (built-in) and "
    "<b>Non-Primitive</b> (reference) types."
)

en.section("1. Primitive Data Types")
en.body(
    "Java has <b>8 primitive data types</b>. They store actual values directly in memory "
    "(stack), are not objects, and have fixed sizes regardless of platform."
)
en.info_table(
    ["Data Type", "Size", "Range", "Default Value", "Example Literal"],
    [
        ["byte", "1 byte (8 bits)", "-128 to 127", "0", "byte b = 10;"],
        ["short", "2 bytes (16 bits)", "-32,768 to 32,767", "0", "short s = 200;"],
        [
            "int",
            "4 bytes (32 bits)",
            "-2^31 to 2^31-1 (~2.1 billion)",
            "0",
            "int i = 1000;",
        ],
        ["long", "8 bytes (64 bits)", "-2^63 to 2^63-1", "0L", "long l = 9876543210L;"],
        [
            "float",
            "4 bytes (32 bits)",
            "~3.4e-38 to ~3.4e+38 (7 digits)",
            "0.0f",
            "float f = 3.14f;",
        ],
        [
            "double",
            "8 bytes (64 bits)",
            "~1.7e-308 to ~1.7e+308 (15 digits)",
            "0.0d",
            "double d = 3.14159;",
        ],
        [
            "char",
            "2 bytes (16 bits)",
            "0 to 65,535 (Unicode characters)",
            "'\\u0000'",
            "char c = 'A';",
        ],
        [
            "boolean",
            "1 bit (JVM-dep.)",
            "true or false",
            "false",
            "boolean flag = true;",
        ],
    ],
)

en.subsection("Integer Types: byte, short, int, long")
en.body(
    "<b>byte</b>: Smallest integer type. Useful for saving memory in large arrays. "
    "<b>short</b>: Rarely used; saves memory over int. "
    "<b>int</b>: Default integer type for all arithmetic. "
    "<b>long</b>: For very large integers; suffix L required."
)

en.subsection("Floating-Point Types: float, double")
en.body(
    "<b>float</b>: Single-precision; suffix f required. Less precise (7 decimal digits). "
    "<b>double</b>: Default for decimal literals; double-precision (15 decimal digits). "
    "Use double for scientific calculations."
)

en.subsection("char Type")
en.body(
    "<b>char</b>: Stores a single Unicode character (16-bit, unsigned). "
    "Java uses Unicode so char can represent characters from any script worldwide. "
    "char c = 'A'; stores the Unicode value 65."
)

en.subsection("boolean Type")
en.body(
    "<b>boolean</b>: Can only hold <b>true</b> or <b>false</b>. "
    "Used for conditional expressions and flags. Java does NOT allow 0/1 as boolean values (unlike C)."
)

en.section("2. Non-Primitive (Reference) Data Types")
en.body(
    "Non-primitive types store <b>references (addresses)</b> to objects in heap memory, "
    "not the actual values. They include:"
)
en.bullet(
    [
        '<b>String</b> -- A sequence of characters. e.g., String name = "Java";',
        "<b>Arrays</b> -- Fixed-size collection of same-type elements. e.g., int[] arr = new int[5];",
        "<b>Classes</b> -- User-defined blueprints for objects.",
        "<b>Interfaces</b> -- Abstract contracts implemented by classes.",
    ]
)

en.tip(
    "Key Difference: Primitive types are stored on the STACK (faster, fixed size). "
    "Reference types are stored on the HEAP (dynamic size, garbage collected). "
    "Primitive types cannot be null; reference types can be null."
)

en.section("Complete Code Example -- All Primitive Types")
en.code_block(
    """\
public class DataTypesDemo {
    public static void main(String[] args) {

        // Integer types
        byte  b  = 127;
        short s  = 32000;
        int   i  = 2147483647;
        long  l  = 9876543210L;

        // Floating-point types
        float  f  = 3.14f;
        double d  = 3.141592653589793;

        // Character type
        char c = 'J';

        // Boolean type
        boolean flag = true;

        // Non-primitive type
        String str = "Hello Java";
        int[]  arr = {1, 2, 3, 4, 5};

        System.out.println("byte    : " + b);
        System.out.println("short   : " + s);
        System.out.println("int     : " + i);
        System.out.println("long    : " + l);
        System.out.println("float   : " + f);
        System.out.println("double  : " + d);
        System.out.println("char    : " + c);
        System.out.println("boolean : " + flag);
        System.out.println("String  : " + str);
        System.out.println("Array[0]: " + arr[0]);
    }
}
""",
    lang="java",
)

en.subsection("Expected Output")
en.code_block(
    """\
$ java DataTypesDemo
byte    : 127
short   : 32000
int     : 2147483647
long    : 9876543210
float   : 3.14
double  : 3.141592653589793
char    : J
boolean : true
String  : Hello Java
Array[0]: 1
""",
    lang="text",
)
en.sp(8)

# -- Q4 [3 Marks] -------------------------------------------------------------
en.bookmark("MST-I Q4")
en.chap_box("Q4 [3 Marks] -- Multi-Threading in Java\n(MST-I, March 2026)")

en.section("What is Multi-Threading?")
en.body(
    "A <b>thread</b> is the smallest unit of execution within a process. "
    "<b>Multi-threading</b> is the ability of a program to execute multiple threads "
    "simultaneously, allowing concurrent tasks to run within a single program."
)
en.bullet(
    [
        "Improves performance by utilizing multiple CPU cores.",
        "Enables responsive UIs -- background tasks do not freeze the application.",
        "Java has built-in support for threading via the <b>java.lang.Thread</b> class and "
        "the <b>java.lang.Runnable</b> interface.",
    ]
)

en.section("Two Ways to Create a Thread")
en.subsection("Method 1: Extending Thread Class")
en.code_block(
    """\
class MyThread extends Thread {
    public void run() {
        System.out.println("Thread running: " + Thread.currentThread().getName());
    }
}
// Usage:
MyThread t = new MyThread();
t.start();   // calls run() in a new thread
""",
    lang="java",
)

en.subsection("Method 2: Implementing Runnable Interface")
en.code_block(
    """\
class MyTask implements Runnable {
    public void run() {
        System.out.println("Runnable running: " + Thread.currentThread().getName());
    }
}
// Usage:
Thread t = new Thread(new MyTask());
t.start();   // calls run() in a new thread
""",
    lang="java",
)

en.note(
    "Prefer Runnable over extending Thread -- it allows your class to extend another class "
    "(Java supports only single inheritance). Thread states: NEW -> RUNNABLE -> RUNNING -> "
    "BLOCKED/WAITING -> TERMINATED."
)

en.subsection("Expected Output (thread name may vary by OS scheduler)")
en.code_block(
    """\
$ java ThreadDemo
Thread running: Thread-0
Runnable running: Thread-1
""",
    lang="text",
)
en.sp(8)

# -- Q5 [4 Marks] -------------------------------------------------------------
en.bookmark("MST-I Q5")
en.chap_box("Q5 [4 Marks] -- Constructors in Java\n(MST-I, March 2026)")

en.section("What is a Constructor?")
en.body(
    "A <b>constructor</b> is a special method called automatically when an object is created. "
    "It has the <b>same name as the class</b> and <b>no return type</b> (not even void). "
    "Its purpose is to initialize the object's fields."
)

en.subsection("Types of Constructors")
en.bullet(
    [
        "<b>Default Constructor</b> -- No parameters. Provided by JVM if none is defined.",
        "<b>Parameterized Constructor</b> -- Accepts arguments to initialize fields with specific values.",
        "<b>Constructor Overloading</b> -- Multiple constructors with different parameter lists in the same class.",
    ]
)

en.section("Complete Example: Constructor Types")
en.code_block(
    """\
public class Student {
    String name;
    int    age;
    double marks;

    // 1. Default Constructor (no parameters)
    public Student() {
        name  = "Unknown";
        age   = 0;
        marks = 0.0;
        System.out.println("Default constructor called.");
    }

    // 2. Parameterized Constructor (name + age)
    public Student(String name, int age) {
        this.name = name;
        this.age  = age;
        this.marks = 0.0;
        System.out.println("Parameterized constructor called.");
    }

    // 3. Constructor Overloading (name + age + marks)
    public Student(String name, int age, double marks) {
        this.name  = name;
        this.age   = age;
        this.marks = marks;
        System.out.println("Full parameterized constructor called.");
    }

    public void display() {
        System.out.println("Name: " + name + ", Age: " + age + ", Marks: " + marks);
    }

    public static void main(String[] args) {
        Student s1 = new Student();                        // calls default
        Student s2 = new Student("Alice", 20);             // calls 2-param
        Student s3 = new Student("Bob", 21, 92.5);         // calls 3-param

        s1.display();
        s2.display();
        s3.display();
    }
}
""",
    lang="java",
)

en.tip(
    "The keyword 'this' refers to the current object instance. "
    "Using 'this.name = name' distinguishes the field (this.name) from the parameter (name). "
    "Constructors cannot be abstract, static, final, or synchronized."
)

en.subsection("Expected Output")
en.code_block(
    """\
$ java Student
Default constructor called.
Parameterized constructor called.
Full parameterized constructor called.
Name: Unknown, Age: 0, Marks: 0.0
Name: Alice, Age: 20, Marks: 0.0
Name: Bob, Age: 21, Marks: 92.5
""",
    lang="text",
)
en.sp(8)

# -- Q6 [8 Marks] -------------------------------------------------------------
en.bookmark("MST-I Q6")
en.chap_box("Q6 [8 Marks] -- Java Packages: Creation and Usage\n(MST-I, March 2026)")

en.section("What is a Package?")
en.body(
    "A <b>package</b> in Java is a namespace that organizes a set of related classes and interfaces. "
    "Packages serve several purposes:"
)
en.bullet(
    [
        "<b>Avoid Name Conflicts</b> -- Two classes with the same name can coexist in different packages.",
        "<b>Access Control</b> -- Package-private members are accessible only within the same package.",
        "<b>Code Organization</b> -- Groups related classes logically (e.g., java.util, java.io).",
        "<b>Reusability</b> -- Packaged code can be imported and reused across projects.",
    ]
)

en.section("Types of Packages")
en.info_table(
    ["Type", "Description", "Examples"],
    [
        [
            "Built-in (Java API)",
            "Pre-defined packages bundled with JDK",
            "java.lang, java.util, java.io, java.awt, java.sql",
        ],
        [
            "User-defined",
            "Created by the programmer for their application",
            "com.company.project, mypackage",
        ],
    ],
)

en.section("Creating a User-Defined Package")
en.body(
    "Use the <b>package</b> keyword as the <b>first statement</b> in the source file "
    "(before any import statements or class declarations)."
)
en.subsection("Step 1: Create the Package Directory and Source File")
en.body("Create file: <b>mypackage/Greeting.java</b>")
en.code_block(
    """\
// File: mypackage/Greeting.java
package mypackage;                  // package declaration -- MUST be first line

public class Greeting {
    private String message;

    public Greeting(String message) {
        this.message = message;
    }

    public void display() {
        System.out.println("Greeting: " + message);
    }

    // Package-private method (no access modifier)
    void internalHelper() {
        System.out.println("Internal helper -- only visible within mypackage");
    }
}
""",
    lang="java",
)

en.subsection("Step 2: Compile with -d Flag")
en.body(
    "The <b>-d</b> flag tells javac where to place the compiled .class files, "
    "preserving the package directory structure."
)
en.code_block(
    """\
# Compile from the root project directory:
javac -d . mypackage/Greeting.java
# This creates: ./mypackage/Greeting.class
""",
    lang="text",
)

en.subsection("Step 3: Create a Class in Another Package")
en.body("Create file: <b>MainApp.java</b> (in the root/default package)")
en.code_block(
    """\
// File: MainApp.java
import mypackage.Greeting;          // import the specific class

public class MainApp {
    public static void main(String[] args) {
        Greeting g = new Greeting("Hello from mypackage!");
        g.display();

        // g.internalHelper();     // ERROR! package-private, not accessible here
    }
}
""",
    lang="java",
)

en.subsection("Step 4: Compile and Run MainApp")
en.code_block(
    """\
javac MainApp.java
java MainApp
""",
    lang="text",
)

en.subsection("Expected Output")
en.code_block(
    """\
$ java MainApp
Greeting: Hello from mypackage!
""",
    lang="text",
)


en.section("Import Statements")
en.info_table(
    ["Import Syntax", "Effect"],
    [
        [
            "import mypackage.Greeting;",
            "Imports only the Greeting class from mypackage",
        ],
        [
            "import mypackage.*;",
            "Imports ALL public classes from mypackage (not sub-packages)",
        ],
        [
            "(no import, use fully qualified)",
            "Use mypackage.Greeting g = new mypackage.Greeting(...);",
        ],
    ],
)

en.section("Access Control with Packages")
en.info_table(
    [
        "Access Modifier",
        "Same Class",
        "Same Package",
        "Subclass (other pkg)",
        "Other Package",
    ],
    [
        ["public", "Yes", "Yes", "Yes", "Yes"],
        ["protected", "Yes", "Yes", "Yes", "No"],
        ["(default)", "Yes", "Yes", "No", "No"],
        ["private", "Yes", "No", "No", "No"],
    ],
)

en.note(
    "Convention: Package names are written in lowercase and use reverse domain name notation. "
    "e.g., com.rgpv.it408.assignment. The java.lang package is automatically imported in every Java program."
)
en.sp(8)
en.br()

# ============================================================
#  MST-II
# ============================================================
en.bookmark("MST-II")
en.part_box("MST-II -- April 2026")
en.note(
    "Exam Details: MST-II | Date: April 2026 | Max Marks: 30 | Time: 1 Hour | "
    "All 3 questions carry 10 marks each. Attempt ALL questions."
)
en.sp(6)

# -- MST-II Q1 [10 Marks] -----------------------------------------------------
en.bookmark("MST-II Q1")
en.chap_box(
    "Q1 [10 Marks] -- Java Applet: Lifecycle, Execution & Comparison with Standalone Applications\n(MST-II, April 2026)"
)

en.section("What is a Java Applet?")
en.body(
    "A <b>Java Applet</b> is a small Java program designed to run inside a web browser or "
    "the <b>appletviewer</b> tool. Applets extend the <b>java.applet.Applet</b> class "
    "(or <b>javax.swing.JApplet</b> for Swing-based applets). They were historically used "
    "to add dynamic, interactive content to web pages."
)
en.bullet(
    [
        "Applets do NOT have a <b>main()</b> method -- they are controlled by the browser/appletviewer.",
        "They are embedded in HTML using the <b>&lt;applet&gt;</b> tag.",
        "They run in a restricted <b>sandbox</b> (cannot access local file system by default).",
        "Applets are downloaded from a server and executed on the client machine by the JVM plugin.",
    ]
)

en.section("Applet Lifecycle Methods")
en.body(
    "The browser/appletviewer manages the applet lifecycle through four key methods "
    "called in a specific order:"
)
en.info_table(
    ["Method", "Called When", "Purpose"],
    [
        [
            "init()",
            "Applet is first loaded",
            "One-time initialization -- like a constructor. Set up UI, load resources.",
        ],
        [
            "start()",
            "After init() and when page is revisited",
            "Begin or resume execution -- start threads, animations.",
        ],
        [
            "stop()",
            "User leaves the page",
            "Pause execution -- stop threads, animations to save resources.",
        ],
        [
            "destroy()",
            "Applet is permanently removed",
            "Clean up resources -- close files, connections.",
        ],
    ],
)

en.sp(8)

# Applet Lifecycle StateMachine
sm = ed.StateMachine(
    width=CW,
    height=240,
    caption="Fig M2.1: Applet Lifecycle State Machine",
    theme=diag_theme,
)
sm.state("loaded", "LOADED", initial=True)
sm.state("init", "INITIALIZED")
sm.state("running", "RUNNING")
sm.state("idle", "IDLE")
sm.state("destroyed", "DESTROYED")
sm.transition("loaded", "init", label="init()")
sm.transition("init", "running", label="start()")
sm.transition("running", "idle", label="stop()")
sm.transition("idle", "running", label="start()")
sm.transition("idle", "destroyed", label="destroy()")
en.story.extend(sm.as_flowable())

en.sp(8)

en.section("Complete Java Applet Example")
en.code_block(
    """\
import java.applet.Applet;
import java.awt.Graphics;

/*
 * HTML to embed this applet:
 * <applet code="HelloApplet.class" width="400" height="200">
 * </applet>
 *
 * Run with: appletviewer HelloApplet.html
 */
public class HelloApplet extends Applet {

    String message;

    @Override
    public void init() {
        // Called once when applet first loads
        message = "Hello from Java Applet!";
        System.out.println("Applet: init() called");
    }

    @Override
    public void start() {
        // Called after init() and when page is revisited
        System.out.println("Applet: start() called");
    }

    @Override
    public void paint(Graphics g) {
        // Called to render the applet's content
        g.drawString(message, 50, 100);
        g.drawRect(10, 10, 380, 180);
    }

    @Override
    public void stop() {
        // Called when user navigates away from the page
        System.out.println("Applet: stop() called");
    }

    @Override
    public void destroy() {
        // Called just before applet is removed from memory
        System.out.println("Applet: destroy() called");
    }
}
""",
    lang="java",
)

en.subsection("Expected Console Output & GUI Display")
en.code_block(
    """\
-- Console output when loaded and started:
Applet: init() called
Applet: start() called

-- Console output when page is left and applet closed:
Applet: stop() called
Applet: destroy() called

-- GUI Window Display:
[An appletviewer window opens of size 400x200]
[A black rectangle border is drawn from x=10, y=10 to x=390, y=190]
[The text "Hello from Java Applet!" is rendered in black at x=50, y=100]
""",
    lang="text",
)

en.section("Applet vs Standalone Application -- Comparison")
en.info_table(
    ["Feature", "Java Applet", "Standalone Application"],
    [
        [
            "Entry Point",
            "No main(); uses init()/start()/stop()/destroy()",
            "public static void main(String[] args)",
        ],
        [
            "Execution Environment",
            "Browser / appletviewer with JVM plugin",
            "JVM directly (java command)",
        ],
        [
            "GUI Framework",
            "AWT / Swing, rendered in browser window",
            "AWT / Swing / JavaFX, own window",
        ],
        [
            "File System Access",
            "Restricted (sandbox security)",
            "Full access to local file system",
        ],
        [
            "Network Access",
            "Only to the server it was loaded from",
            "Unrestricted network access",
        ],
        [
            "Distribution",
            "Downloaded from web server via HTML",
            "Installed locally or via JAR",
        ],
        [
            "Security",
            "High restrictions (sandbox model)",
            "Runs with full user permissions",
        ],
        [
            "Status (2026)",
            "Deprecated; removed from modern browsers",
            "Standard, widely used",
        ],
        ["Base Class", "Extends java.applet.Applet", "No required base class"],
        [
            "Compilation",
            "javac; needs HTML file to run",
            "javac; run directly with java",
        ],
    ],
)

en.tip(
    "Applets are deprecated as of Java 9 and removed in Java 17. Modern web applications use "
    "JavaScript/HTML5 for browser-based interactivity. For exam purposes, understand the lifecycle "
    "and the key differences from standalone applications."
)
en.sp(8)

# -- MST-II Q2 [10 Marks] -----------------------------------------------------
en.bookmark("MST-II Q2")
en.chap_box(
    "Q2 [10 Marks] -- Student Registration Form using Java AWT\n(MST-II, April 2026)"
)

en.section("AWT Components Used")
en.body(
    "Java's <b>Abstract Window Toolkit (AWT)</b> provides platform-dependent GUI components. "
    "The following components are used in this Student Registration Form:"
)
en.info_table(
    ["AWT Component", "Class", "Purpose"],
    [
        [
            "Frame",
            "java.awt.Frame",
            "Top-level window with title bar, border, and menu bar",
        ],
        ["Label", "java.awt.Label", "Displays non-editable text (field names)"],
        [
            "TextField",
            "java.awt.TextField",
            "Single-line text input field for user input",
        ],
        ["Button", "java.awt.Button", "Clickable button that triggers an action"],
        [
            "Panel",
            "java.awt.Panel",
            "Invisible container to group and layout components",
        ],
        [
            "FlowLayout",
            "java.awt.FlowLayout",
            "Default layout: arranges components left to right",
        ],
        [
            "GridLayout",
            "java.awt.GridLayout",
            "Arranges components in a grid of rows and columns",
        ],
    ],
)

en.section("Complete AWT Student Registration Form")
en.code_block(
    """\
import java.awt.*;
import java.awt.event.*;

public class StudentRegistrationForm extends Frame implements ActionListener {

    // Declare components
    Label  nameLabel, emailLabel, titleLabel;
    TextField nameField, emailField;
    Button submitButton, resetButton;

    public StudentRegistrationForm() {
        // --- Set up the Frame ---
        setTitle("Student Registration Form");
        setSize(400, 250);
        setLayout(new FlowLayout(FlowLayout.LEFT, 20, 15));

        // --- Title Label ---
        titleLabel = new Label("Student Registration Form");
        titleLabel.setFont(new Font("Arial", Font.BOLD, 16));

        // --- Name row ---
        nameLabel = new Label("Name:");
        nameField = new TextField(25);

        // --- Email row ---
        emailLabel = new Label("Email:");
        emailField = new TextField(25);

        // --- Buttons ---
        submitButton = new Button("Submit");
        resetButton  = new Button("Reset");

        // Register ActionListeners
        submitButton.addActionListener(this);
        resetButton.addActionListener(this);

        // --- Add components to Frame ---
        add(titleLabel);
        add(nameLabel);
        add(nameField);
        add(emailLabel);
        add(emailField);
        add(submitButton);
        add(resetButton);

        // Handle window close
        addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent e) {
                System.exit(0);
            }
        });

        setVisible(true);
    }

    // Handle button clicks
    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == submitButton) {
            String name  = nameField.getText().trim();
            String email = emailField.getText().trim();
            if (name.isEmpty() || email.isEmpty()) {
                System.out.println("ERROR: All fields are required!");
            } else {
                System.out.println("Submitted --> Name: " + name + ", Email: " + email);
            }
        } else if (e.getSource() == resetButton) {
            nameField.setText("");
            emailField.setText("");
            System.out.println("Form reset.");
        }
    }

    public static void main(String[] args) {
        new StudentRegistrationForm();
    }
}
""",
    lang="java",
)

en.subsection("Expected Console Output (when buttons are clicked)")
en.code_block(
    """\
-- When Submit is clicked with Name='Arjun' and Email='arjun@college.edu':
Submitted --> Name: Arjun, Email: arjun@college.edu

-- When Submit is clicked with empty fields:
ERROR: All fields are required!

-- When Reset is clicked:
Form reset.

[Note: The AWT Frame window opens with title 'Student Registration Form',
 showing Name/Email fields and Submit/Reset buttons]
""",
    lang="text",
)

en.section("Component Explanations")
en.subsection("Frame")
en.body(
    "<b>Frame</b> is the top-level container (window). It extends Window and provides a title bar, "
    "minimize/maximize/close buttons, and a border. <b>setSize(400, 250)</b> sets width x height in pixels. "
    "<b>setVisible(true)</b> makes the window appear on screen."
)

en.subsection("Label")
en.body(
    "<b>Label</b> displays a static text string. It cannot be edited by the user. "
    "Used here to identify input fields: 'Name:' and 'Email:'."
)

en.subsection("TextField")
en.body(
    "<b>TextField</b> provides a single-line editable text input. The integer argument "
    "to the constructor (e.g., 25) specifies the visible width in columns. "
    '<b>getText()</b> retrieves entered text; <b>setText("")</b> clears it.'
)

en.subsection("Button and ActionListener")
en.body(
    "<b>Button</b> creates a clickable button. When clicked, it fires an <b>ActionEvent</b>. "
    "The form implements <b>ActionListener</b> and overrides <b>actionPerformed()</b> to handle clicks. "
    "<b>e.getSource()</b> identifies which button was clicked."
)

en.tip(
    "For a production application, use GridLayout or GroupLayout for proper alignment of labels and fields. "
    "FlowLayout is used here for simplicity. Swing (JFrame, JLabel, JTextField, JButton) is the modern "
    "alternative to AWT with better look-and-feel and more components."
)
en.sp(8)

# -- MST-II Q3 [10 Marks] -----------------------------------------------------
en.bookmark("MST-II Q3")
en.chap_box(
    "Q3 [10 Marks] -- AWT Class Hierarchy: Component, Container, Panel, Frame\n(MST-II, April 2026)"
)

en.section("AWT Class Hierarchy Overview")
en.body(
    "Java's <b>Abstract Window Toolkit (AWT)</b> is organized as a class hierarchy rooted at "
    "<b>java.awt.Component</b>. Every GUI element is either a Component or a Container "
    "(which can hold other Components). The hierarchy defines how GUI elements are structured, "
    "how they are rendered, and how they interact."
)

en.sp(8)

# AWT LayeredStack Diagram
stack = ed.LayeredStack(
    width=CW, height=220, caption="Fig M2.2: AWT Component Class Hierarchy"
)
stack.layer(
    "Frame (extends Window extends Container)",
    sublabel="Top-level window with title bar and borders",
)
stack.layer(
    "Panel (extends Container)", sublabel="Invisible container to group components"
)
stack.layer(
    "Container (extends Component)",
    sublabel="Can hold other Components -- uses add() method",
)
stack.layer(
    "Component (abstract base class)",
    sublabel="paint(), repaint(), setSize(), setVisible()",
)
en.story.extend(stack.as_flowable())

en.sp(8)

en.section("1. Component (java.awt.Component)")
en.body(
    "<b>Component</b> is the abstract root class of the AWT hierarchy. "
    "Every GUI element -- buttons, labels, text fields, canvases -- extends Component. "
    "It defines the fundamental properties and behaviors all GUI elements share."
)
en.bullet(
    [
        "<b>paint(Graphics g)</b> -- Renders the component. Override to draw custom graphics.",
        "<b>repaint()</b> -- Requests the component to be redrawn by the AWT paint thread.",
        "<b>setSize(int w, int h)</b> -- Sets the width and height of the component.",
        "<b>setLocation(int x, int y)</b> -- Positions the component within its parent.",
        "<b>setVisible(boolean)</b> -- Shows or hides the component.",
        "<b>setBackground(Color)</b> / <b>setForeground(Color)</b> -- Sets background/foreground color.",
        "<b>setFont(Font)</b> -- Sets the display font for the component.",
        "<b>addMouseListener()</b> / <b>addKeyListener()</b> -- Registers event listeners.",
    ]
)

en.section("2. Container (java.awt.Container) -- extends Component")
en.body(
    "<b>Container</b> is a Component that can contain other Components. "
    "It provides the <b>add()</b> and <b>remove()</b> methods and supports layout managers."
)
en.bullet(
    [
        "<b>add(Component c)</b> -- Adds a child component to this container.",
        "<b>remove(Component c)</b> -- Removes a child component.",
        "<b>setLayout(LayoutManager lm)</b> -- Sets the layout manager (FlowLayout, BorderLayout, GridLayout, etc.).",
        "<b>getComponents()</b> -- Returns array of all child components.",
        "Common subclasses: Panel, Window, ScrollPane.",
    ]
)

en.section("3. Panel (java.awt.Panel) -- extends Container")
en.body(
    "<b>Panel</b> is the simplest concrete container. It is a plain, borderless, "
    "invisible rectangle that groups components together. Panels can be nested inside "
    "Frames or other Containers to create complex layouts."
)
en.bullet(
    [
        "Default layout: <b>FlowLayout</b> (components arranged left to right).",
        "Used to group related components (e.g., a row of buttons).",
        "Cannot exist as a standalone window -- must be added to a Frame or Window.",
        "Applet extends Panel (that is why Applets have a graphical surface).",
    ]
)

en.section("4. Frame (java.awt.Frame) -- extends Window extends Container")
en.body(
    "<b>Frame</b> is a top-level window with a title bar, border, and optional menu bar. "
    "It is the main window of an AWT application."
)
en.bullet(
    [
        "Extends <b>Window</b>, which extends <b>Container</b>.",
        "Default layout: <b>BorderLayout</b>.",
        "<b>setTitle(String)</b> -- Sets the window title.",
        "<b>setSize(int, int)</b> -- Sets width and height.",
        "<b>setVisible(true)</b> -- Makes the window visible on screen.",
        "Must handle the window-close event with <b>WindowListener</b> / <b>System.exit(0)</b>.",
    ]
)

en.section("Comparison Table")
en.info_table(
    ["Class", "Extends", "Default Layout", "Standalone Window?", "Primary Purpose"],
    [
        [
            "Component",
            "Object (abstract)",
            "N/A",
            "No",
            "Abstract base: all GUI elements",
        ],
        ["Container", "Component", "N/A", "No", "Can hold child Components"],
        ["Panel", "Container", "FlowLayout", "No", "Group/organize components"],
        [
            "Frame",
            "Window->Container",
            "BorderLayout",
            "Yes",
            "Top-level application window",
        ],
    ],
)

en.section("Code Example: Frame with Panel")
en.code_block(
    """\
import java.awt.*;
import java.awt.event.*;

public class HierarchyDemo {
    public static void main(String[] args) {
        // Frame: top-level window
        Frame frame = new Frame("AWT Hierarchy Demo");
        frame.setSize(400, 300);
        frame.setLayout(new BorderLayout());

        // Panel: groups buttons at the bottom
        Panel buttonPanel = new Panel();          // default FlowLayout
        buttonPanel.setBackground(Color.LIGHT_GRAY);

        Button okBtn     = new Button("OK");
        Button cancelBtn = new Button("Cancel");
        buttonPanel.add(okBtn);
        buttonPanel.add(cancelBtn);

        // Label in the center of the Frame
        Label info = new Label("Component -> Container -> Panel -> Frame", Label.CENTER);

        // Add components to Frame
        frame.add(info,        BorderLayout.CENTER);
        frame.add(buttonPanel, BorderLayout.SOUTH);

        frame.addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent e) { System.exit(0); }
        });
        frame.setVisible(true);
    }
}
""",
    lang="java",
)

en.subsection("Expected Output (console + GUI window)")
en.code_block(
    """\
[A 400x300 AWT window titled 'AWT Hierarchy Demo' opens.]
[CENTER area shows label: 'Component -> Container -> Panel -> Frame']
[SOUTH area shows Panel (light gray) with two buttons: 'OK' and 'Cancel']

-- No console output on launch (window is rendered by AWT paint thread)
-- Closing the window calls System.exit(0)
""",
    lang="text",
)

en.note(
    "The inheritance chain is: Object -> Component -> Container -> Window -> Frame. "
    "Swing (javax.swing) extends AWT: JComponent extends Container, JFrame extends Frame. "
    "In modern Java development, Swing or JavaFX is preferred over AWT."
)
en.sp(8)
en.br()

# ============================================================
#  MST-III
# ============================================================
en.bookmark("MST-III")
en.part_box("MST-III -- May 2026")
en.note(
    "Exam Details: MST-III | Date: May 2026 | Max Marks: 30 | Time: 1 Hour | "
    "All 3 questions carry 10 marks each. Attempt ALL questions."
)
en.sp(6)

# -- MST-III Q1 [10 Marks] -----------------------------------------------------
en.bookmark("MST-III Q1")
en.chap_box(
    "Q1 [10 Marks] -- JDBC: Step-by-Step Database Connection Process\n(MST-III, May 2026)"
)

en.section("What is JDBC?")
en.body(
    "<b>JDBC (Java Database Connectivity)</b> is a Java API that enables Java programs to interact "
    "with relational databases (MySQL, Oracle, PostgreSQL, etc.). It provides a standard interface "
    "so that the same Java code can work with different databases by simply swapping the JDBC driver."
)

en.section("JDBC Architecture")
en.sp(8)

net = ed.NetworkDiagram(
    width=CW, height=240, caption="Fig M3.1: JDBC Architecture", theme=diag_theme
)
net.node("app", "Java Application\n(Your Code)", x=70, y=90, kind="host")
net.node("api", "JDBC API\n(java.sql.*)", x=210, y=90, kind="server")
net.node("dm", "DriverManager\n(loads drivers)", x=360, y=90, kind="server")
net.node("drv", "JDBC Driver\n(Type 4 / Thin)", x=210, y=185, kind="generic")
net.node("db", "Remote Database\n(MySQL/Oracle)", x=360, y=185, kind="database")
net.link("app", "api", bidirectional=False, label="calls")
net.link("api", "dm", bidirectional=False, label="delegates")
net.link("dm", "drv", bidirectional=False, label="loads")
net.link("drv", "db", bidirectional=True, label="SQL / Results")
en.story.extend(net.as_flowable())

en.sp(8)

en.section("6-Step JDBC Connection Process")
en.info_table(
    ["Step", "Action", "Key API / Class"],
    [
        ["1", "Load the JDBC Driver", 'Class.forName("com.mysql.cj.jdbc.Driver")'],
        [
            "2",
            "Establish a Connection",
            "DriverManager.getConnection(url, user, password)",
        ],
        [
            "3",
            "Create a Statement",
            "conn.createStatement() or conn.prepareStatement(sql)",
        ],
        [
            "4",
            "Execute the SQL Query",
            "stmt.executeQuery(sql) or stmt.executeUpdate(sql)",
        ],
        ["5", "Process the ResultSet", "rs.next(), rs.getString(), rs.getInt()"],
        ["6", "Close Resources", "rs.close(), stmt.close(), conn.close()"],
    ],
)

en.subsection("Step 1: Load the JDBC Driver")
en.body(
    "Registers the JDBC driver with the <b>DriverManager</b>. "
    "In modern JDBC (4.0+), this step is automatic via ServiceLoader -- but it is still "
    "shown for completeness in exams."
)
en.code_block(
    """\
Class.forName("com.mysql.cj.jdbc.Driver");  // MySQL Connector/J driver
""",
    lang="java",
)

en.subsection("Step 2: Establish a Connection")
en.body(
    "<b>DriverManager.getConnection()</b> takes a JDBC URL, username, and password "
    "and returns a <b>Connection</b> object representing the database session."
)
en.code_block(
    """\
String url      = "jdbc:mysql://localhost:3306/college_db";
String username = "root";
String password = "password123";
Connection conn = DriverManager.getConnection(url, username, password);
""",
    lang="java",
)

en.subsection("Step 3: Create a Statement")
en.body(
    "<b>Statement</b>: For static SQL. "
    "<b>PreparedStatement</b>: For parameterized/dynamic SQL (prevents SQL injection). "
    "<b>CallableStatement</b>: For stored procedures."
)

en.subsection("Steps 4-6: Execute, Process, Close")
en.body(
    "<b>executeQuery()</b> returns a <b>ResultSet</b> for SELECT statements. "
    "<b>executeUpdate()</b> returns rows affected for INSERT/UPDATE/DELETE. "
    "Always close resources in a finally block or use try-with-resources."
)

en.section("Complete JDBC Code Example -- Remote Database Connection")
en.code_block(
    """\
import java.sql.*;

public class JDBCConnectionDemo {
    public static void main(String[] args) {

        // JDBC URL format: jdbc:mysql://<host>:<port>/<database>
        String url  = "jdbc:mysql://192.168.1.100:3306/college_db" +
                      "?useSSL=false&serverTimezone=UTC";
        String user = "admin";
        String pass = "securePass";

        // try-with-resources ensures all resources are closed automatically
        try (
            Connection conn = DriverManager.getConnection(url, user, pass);
            Statement  stmt = conn.createStatement();
            ResultSet  rs   = stmt.executeQuery("SELECT * FROM students")
        ) {
            System.out.println("Connection established successfully!");

            // Process each row of the ResultSet
            while (rs.next()) {
                int    id      = rs.getInt("id");
                String name    = rs.getString("name");
                double marks   = rs.getDouble("marks");
                System.out.printf("ID: %d | Name: %-20s | Marks: %.2f%n",
                                  id, name, marks);
            }

        } catch (SQLException e) {
            System.err.println("Database error: " + e.getMessage());
            e.printStackTrace();
        }
        // Resources auto-closed by try-with-resources
    }
}
""",
    lang="java",
)

en.subsection("Expected Output")
en.code_block(
    """\
Connection established successfully!
ID: 1 | Name: Alice Sharma         | Marks: 88.50
ID: 2 | Name: Bob Verma            | Marks: 55.00
ID: 3 | Name: Carol Singh          | Marks: 73.20
ID: 4 | Name: David Kumar          | Marks: 45.00
ID: 5 | Name: Eva Patel            | Marks: 92.00
ID: 6 | Name: Frank Gupta          | Marks: 61.50
""",
    lang="text",
)

en.section("Key JDBC API Methods Explained")
en.info_table(
    ["Method", "Class", "Returns", "Description"],
    [
        [
            "DriverManager.getConnection(url,u,p)",
            "DriverManager",
            "Connection",
            "Opens a connection to the database",
        ],
        [
            "conn.createStatement()",
            "Connection",
            "Statement",
            "Creates a Statement for static SQL",
        ],
        [
            "conn.prepareStatement(sql)",
            "Connection",
            "PreparedStatement",
            "Precompiles parameterized SQL",
        ],
        [
            "stmt.executeQuery(sql)",
            "Statement",
            "ResultSet",
            "Executes SELECT; returns result rows",
        ],
        [
            "stmt.executeUpdate(sql)",
            "Statement",
            "int",
            "Executes INSERT/UPDATE/DELETE; returns row count",
        ],
        [
            "rs.next()",
            "ResultSet",
            "boolean",
            "Moves cursor to next row; true if row exists",
        ],
        [
            "rs.getString(colName)",
            "ResultSet",
            "String",
            "Gets String value of named column",
        ],
        ["rs.getInt(colName)", "ResultSet", "int", "Gets int value of named column"],
        ["rs.close()", "ResultSet", "void", "Closes ResultSet, releases resources"],
    ],
)

en.tip(
    "Always use try-with-resources (Java 7+) or a finally block to close Connection, Statement, and ResultSet. "
    "Unclosed connections cause memory leaks and exhaust the database connection pool. "
    "For production code, use a connection pool library like HikariCP or Apache DBCP."
)
en.sp(8)

# -- MST-III Q2 [10 Marks] -----------------------------------------------------
en.bookmark("MST-III Q2")
en.chap_box(
    "Q2 [10 Marks] -- Events, Event Sources, and Event Listeners in Java GUI\n(MST-III, May 2026)"
)

en.section("The Delegation Event Model")
en.body(
    "Java uses the <b>Delegation Event Model</b> (introduced in Java 1.1) for handling GUI events. "
    "In this model, the responsibility of handling an event is <b>delegated</b> from the "
    "event source to a registered listener. This decouples the source from the handler."
)

en.section("Three Pillars of the Delegation Model")
en.info_table(
    ["Pillar", "Description", "Example"],
    [
        [
            "Event Object",
            "Encapsulates information about what happened and where",
            "ActionEvent, MouseEvent, KeyEvent",
        ],
        [
            "Event Source",
            "The GUI component that generates the event when interacted with",
            "Button, TextField, CheckBox",
        ],
        [
            "Event Listener",
            "An object that implements a listener interface and handles the event",
            "ActionListener, MouseListener, KeyListener",
        ],
    ],
)

en.section("Flow of Event Processing")
en.bullet(
    [
        "<b>Step 1 -- Source generates event:</b> User interacts with a GUI component (e.g., clicks a Button).",
        "<b>Step 2 -- Event object created:</b> JVM creates an event object (e.g., ActionEvent) with event details.",
        "<b>Step 3 -- Listeners notified:</b> The AWT Event Dispatch Thread (EDT) calls the appropriate "
        "method on each registered listener.",
        "<b>Step 4 -- Listener handles event:</b> The listener's callback method (e.g., actionPerformed()) "
        "executes the application logic.",
    ]
)

en.sp(8)

# Delegation Event Model Sequence Diagram
seq = ed.SequenceDiagram(
    width=CW,
    height=280,
    caption="Fig M3.2: Delegation Event Model -- Communication Flow",
)
seq.actor("src", "Button\n(Event Source)")
seq.actor("edt", "AWT Event\nDispatch Thread")
seq.actor("lst", "ActionListener\n(Handler)")
seq.message("src", "edt", "User clicks button")
seq.divider("loop [for each registered listener]")
seq.message("edt", "edt", "look up registered listeners")
seq.message("edt", "lst", "actionPerformed(ActionEvent e)")
seq.message("lst", "edt", "update UI / do logic")
seq.divider("end loop")
en.story.extend(seq.as_flowable())

en.sp(8)

en.section("Common Event Types and Listener Interfaces")
en.info_table(
    ["Event Class", "Listener Interface", "Method to Override", "Triggered By"],
    [
        [
            "ActionEvent",
            "ActionListener",
            "actionPerformed(ActionEvent e)",
            "Button click, TextField Enter",
        ],
        [
            "MouseEvent",
            "MouseListener",
            "mouseClicked/Pressed/Released()",
            "Mouse clicks",
        ],
        ["MouseEvent", "MouseMotionListener", "mouseMoved/Dragged()", "Mouse movement"],
        [
            "KeyEvent",
            "KeyListener",
            "keyPressed/Released/Typed()",
            "Keyboard key press",
        ],
        [
            "WindowEvent",
            "WindowListener",
            "windowClosing/Opened()",
            "Window state changes",
        ],
        [
            "ItemEvent",
            "ItemListener",
            "itemStateChanged(ItemEvent e)",
            "Checkbox, Choice selection",
        ],
        [
            "TextEvent",
            "TextListener",
            "textValueChanged(TextEvent e)",
            "TextField text change",
        ],
    ],
)

en.section("Complete ActionListener Example")
en.code_block(
    """\
import java.awt.*;
import java.awt.event.*;

// The class implements ActionListener to handle button events
public class EventDemo extends Frame implements ActionListener {

    Button greetBtn;
    Button clearBtn;
    Label  messageLabel;

    public EventDemo() {
        setTitle("Delegation Event Model Demo");
        setSize(400, 200);
        setLayout(new FlowLayout());

        greetBtn     = new Button("Say Hello");
        clearBtn     = new Button("Clear");
        messageLabel = new Label("Click a button...");

        // REGISTER: Add this object as ActionListener for both buttons
        // This is the "delegation" -- source delegates handling to listener
        greetBtn.addActionListener(this);
        clearBtn.addActionListener(this);

        add(greetBtn);
        add(clearBtn);
        add(messageLabel);

        addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent e) { System.exit(0); }
        });
        setVisible(true);
    }

    // HANDLER: This method is called by EDT when an action event occurs
    @Override
    public void actionPerformed(ActionEvent e) {
        // e.getSource() returns the component that fired the event
        if (e.getSource() == greetBtn) {
            messageLabel.setText("Hello from Delegation Event Model!");
            System.out.println("ActionEvent received from: " + e.getActionCommand());
        } else if (e.getSource() == clearBtn) {
            messageLabel.setText("Click a button...");
        }
    }

    public static void main(String[] args) {
        new EventDemo();
    }
}
""",
    lang="java",
)

en.subsection("Expected Console Output")
en.code_block(
    """\
-- When 'Say Hello' button is clicked:
ActionEvent received from: Say Hello
[Label text changes to: 'Hello from Delegation Event Model!']

-- When 'Clear' button is clicked:
[Label text resets to: 'Click a button...']

-- Lambda / anonymous inner class version:
Button clicked via anonymous inner class!
Lambda listener!
""",
    lang="text",
)

en.section("Anonymous Inner Class Listener (Alternative)")
en.body(
    "Instead of implementing ActionListener in the main class, you can use "
    "an <b>anonymous inner class</b> for cleaner, localized event handling:"
)
en.code_block(
    """\
Button btn = new Button("Click Me");
btn.addActionListener(new ActionListener() {
    @Override
    public void actionPerformed(ActionEvent e) {
        System.out.println("Button clicked via anonymous inner class!");
    }
});

// Java 8+ Lambda expression (even cleaner):
btn.addActionListener(e -> System.out.println("Lambda listener!"));
""",
    lang="java",
)

en.note(
    "The Event Dispatch Thread (EDT) is a special thread managed by AWT/Swing that processes "
    "all GUI events sequentially. Never perform long-running operations on the EDT -- "
    "use SwingWorker or new Thread() for background tasks, then update UI on the EDT "
    "using SwingUtilities.invokeLater()."
)
en.sp(8)

# -- MST-III Q3 [10 Marks] -----------------------------------------------------
en.bookmark("MST-III Q3")
en.chap_box(
    "Q3 [10 Marks] -- JDBC Program: SELECT Query with ResultSet Processing\n(MST-III, May 2026)"
)

en.section("Problem Statement")
en.body(
    "Write a Java program that connects to a MySQL database and executes "
    "<b>SELECT * FROM students WHERE marks &gt; 60</b>, iterates the ResultSet, "
    "and prints the results. Explain each JDBC API method used."
)

en.section("SQL: Create and Populate the Table")
en.body("First, create the database table in MySQL:")
en.code_block(
    """\
-- Run these SQL commands in MySQL before running the Java program

CREATE DATABASE IF NOT EXISTS college_db;
USE college_db;

CREATE TABLE IF NOT EXISTS students (
    id      INT          PRIMARY KEY AUTO_INCREMENT,
    name    VARCHAR(50)  NOT NULL,
    email   VARCHAR(80)  NOT NULL,
    course  VARCHAR(30)  NOT NULL,
    marks   DOUBLE       NOT NULL
);

INSERT INTO students (name, email, course, marks) VALUES
    ('Alice Sharma',  'alice@example.com',  'B.Tech IT', 88.5),
    ('Bob Verma',     'bob@example.com',    'B.Tech CS', 55.0),
    ('Carol Singh',   'carol@example.com',  'B.Tech IT', 73.2),
    ('David Kumar',   'david@example.com',  'B.Tech CS', 45.0),
    ('Eva Patel',     'eva@example.com',    'B.Tech IT', 92.0),
    ('Frank Gupta',   'frank@example.com',  'B.Tech CS', 61.5);
""",
    lang="java",
)

en.section("Complete Java JDBC Program")
en.code_block(
    """\
import java.sql.*;

public class StudentQueryDemo {

    // Database connection constants
    static final String JDBC_URL  = "jdbc:mysql://localhost:3306/college_db"
                                  + "?useSSL=false&serverTimezone=UTC";
    static final String DB_USER   = "root";
    static final String DB_PASS   = "password123";

    public static void main(String[] args) {

        System.out.println("Connecting to database...");
        System.out.println("Query: SELECT * FROM students WHERE marks > 60");
        System.out.println("-----------------------------------------------");

        // try-with-resources: auto-closes conn, stmt, rs when block exits
        try (
            Connection conn = DriverManager.getConnection(JDBC_URL, DB_USER, DB_PASS);
            Statement  stmt = conn.createStatement();
            ResultSet  rs   = stmt.executeQuery(
                                "SELECT * FROM students WHERE marks > 60 ORDER BY marks DESC")
        ) {
            System.out.println("Connection successful! Executing query...");
            System.out.printf("%-5s %-20s %-30s %-15s %-8s%n",
                              "ID", "Name", "Email", "Course", "Marks");
            System.out.println("-----------------------------------------------");

            int rowCount = 0;

            // rs.next() advances cursor to next row; returns false when no more rows
            while (rs.next()) {
                // Retrieve column values by column name
                int    id     = rs.getInt("id");
                String name   = rs.getString("name");
                String email  = rs.getString("email");
                String course = rs.getString("course");
                double marks  = rs.getDouble("marks");

                // Print formatted row
                System.out.printf("%-5d %-20s %-30s %-15s %-8.2f%n",
                                  id, name, email, course, marks);
                rowCount++;
            }

            System.out.println("-----------------------------------------------");
            System.out.println("Total students with marks > 60: " + rowCount);

        } catch (SQLException e) {
            // SQLState and error code help diagnose the database error
            System.err.println("SQL Error   : " + e.getMessage());
            System.err.println("SQL State   : " + e.getSQLState());
            System.err.println("Error Code  : " + e.getErrorCode());
            e.printStackTrace();
        }
        // Connection, Statement, and ResultSet are auto-closed here
        System.out.println("Resources closed. Program complete.");
    }
}
""",
    lang="java",
)

en.section("Expected Output")
en.code_block(
    """\
Connecting to database...
Query: SELECT * FROM students WHERE marks > 60
-----------------------------------------------
Connection successful! Executing query...
ID    Name                 Email                          Course          Marks
-----------------------------------------------
5     Eva Patel            eva@example.com                B.Tech IT       92.00
1     Alice Sharma         alice@example.com              B.Tech IT       88.50
3     Carol Singh          carol@example.com              B.Tech IT       73.20
6     Frank Gupta          frank@example.com              B.Tech CS       61.50
-----------------------------------------------
Total students with marks > 60: 4
Resources closed. Program complete.
""",
    lang="text",
)

en.section("JDBC API Methods -- Detailed Explanation")
en.info_table(
    ["Method Call", "API Class", "Return Type", "What It Does"],
    [
        [
            "DriverManager.getConnection(url, user, pass)",
            "java.sql.DriverManager",
            "Connection",
            "Establishes physical TCP connection to the database server using JDBC URL. "
            "URL format: jdbc:<subprotocol>://<host>:<port>/<db>?params",
        ],
        [
            "conn.createStatement()",
            "java.sql.Connection",
            "Statement",
            "Creates a Statement object for sending static SQL to the database. "
            "For dynamic SQL with parameters, use conn.prepareStatement(sql).",
        ],
        [
            "stmt.executeQuery(String sql)",
            "java.sql.Statement",
            "ResultSet",
            "Executes a SELECT query. Returns a ResultSet containing the query results. "
            "Throws SQLException if query fails or is not a SELECT.",
        ],
        [
            "rs.next()",
            "java.sql.ResultSet",
            "boolean",
            "Advances the cursor to the next row. Returns true if a row exists, "
            "false if past the last row. Must call next() before reading any data.",
        ],
        [
            "rs.getInt(String columnLabel)",
            "java.sql.ResultSet",
            "int",
            "Retrieves the integer value of the named column in the current row.",
        ],
        [
            "rs.getString(String columnLabel)",
            "java.sql.ResultSet",
            "String",
            "Retrieves the String value of the named column in the current row.",
        ],
        [
            "rs.getDouble(String columnLabel)",
            "java.sql.ResultSet",
            "double",
            "Retrieves the double value of the named column in the current row.",
        ],
        [
            "e.getSQLState()",
            "java.sql.SQLException",
            "String",
            "Returns the SQLState code (5-character string) for the error, "
            "defined by SQL standard (e.g., '42000' = syntax error).",
        ],
    ],
)

en.section("Using PreparedStatement -- Safer Query")
en.body(
    "For queries with user-supplied parameters, always use <b>PreparedStatement</b> "
    "to prevent SQL injection attacks:"
)
en.code_block(
    """\
// Safe parameterized query using PreparedStatement
double minimumMarks = 60.0;
String sql = "SELECT * FROM students WHERE marks > ? ORDER BY marks DESC";

try (
    Connection        conn = DriverManager.getConnection(JDBC_URL, DB_USER, DB_PASS);
    PreparedStatement pstmt = conn.prepareStatement(sql)
) {
    pstmt.setDouble(1, minimumMarks);   // Set parameter at position 1
    ResultSet rs = pstmt.executeQuery();

    while (rs.next()) {
        System.out.println(rs.getString("name") + " -> " + rs.getDouble("marks"));
    }
    rs.close();
} catch (SQLException e) {
    e.printStackTrace();
}
""",
    lang="java",
)

en.tip(
    "To run this program: (1) Add mysql-connector-java.jar to your classpath. "
    "e.g., javac -cp .;mysql-connector-j-8.0.33.jar StudentQueryDemo.java "
    "and java -cp .;mysql-connector-j-8.0.33.jar StudentQueryDemo. "
    "(2) Ensure MySQL server is running and college_db database exists. "
    "(3) Replace DB_USER and DB_PASS with your MySQL credentials."
)

# #############################################################################
#  MST-I  --  April 2023  (Jan-June 2023 Session)
# #############################################################################
en.bookmark("MST-I April 2023")
en.part_box("MST-I -- April 2023  (Session: Jan-June 2023)")
en.note(
    "Exam Details: MST-I | Date: April 2023 | Max Marks: 30 | Time: 1 Hour | "
    "Marks: Q1=3m, Q2=4m, Q3=8m (choice), Q4=3m, Q5=4m, Q6=8m (choice)"
)
en.sp(6)

# -- 2023-I Q1 [3 Marks] ------------------------------------------------------
en.bookmark("2023-I Q1")
en.chap_box(
    "Q1 [3 Marks] -- Single-line and Multi-line Comments in Java\n"
    "(MST-I, April 2023)"
)
en.section("Types of Comments in Java")
en.definition(
    "<b>Comments</b> are non-executable statements ignored by the Java compiler (javac). "
    "They improve code readability, serve as documentation, and help in debugging. "
    "Java supports <b>three</b> types of comments."
)
en.info_table(
    ["Type", "Syntax", "Scope", "Purpose"],
    [
        ["Single-line", "// text", "From // to end of line", "Brief inline notes"],
        [
            "Multi-line",
            "/* text */",
            "Everything between /* and */",
            "Longer explanations across multiple lines",
        ],
        [
            "Javadoc",
            "/** text */",
            "Everything between /** and */",
            "API documentation generated by javadoc tool",
        ],
    ],
)
en.code_block(
    """\
public class CommentsDemo {
    public static void main(String[] args) {

        // Single-line comment: prints a greeting
        System.out.println("Hello from Java!");

        /* Multi-line comment:
           This block demonstrates arithmetic.
           Both lines below compute a sum. */
        int a = 10, b = 20;
        int sum = a + b;  // inline single-line comment

        System.out.println("Sum = " + sum);
    }
}
""",
    lang="java",
)
en.subsection("Expected Output")
en.code_block(
    """\
$ java CommentsDemo
Hello from Java!
Sum = 30
""",
    lang="text",
)

# -- 2023-I Q2 [4 Marks] ------------------------------------------------------
en.bookmark("2023-I Q2")
en.chap_box(
    "Q2 [4 Marks] -- Data Types in Java Programming (Categorized)\n"
    "(MST-I, April 2023)"
)
en.note(
    "This question overlaps with Q3 [8 Marks] in MST-I March 2026 which provides a "
    "more comprehensive answer. The categorized overview below is tailored for 4 marks."
)
en.section("Categories of Java Data Types")
en.definition(
    "Java is a <b>strongly typed</b> language. Every variable must be declared with a type. "
    "Data types are divided into two main categories:"
)
en.info_table(
    ["Category", "Subcategory", "Types", "Storage"],
    [
        [
            "Primitive",
            "Integer",
            "byte, short, int, long",
            "Stack (value stored directly)",
        ],
        ["Primitive", "Floating-point", "float, double", "Stack"],
        ["Primitive", "Character", "char", "Stack (16-bit Unicode)"],
        ["Primitive", "Boolean", "boolean", "Stack (true/false only)"],
        [
            "Non-Primitive (Reference)",
            "String",
            "String",
            "Heap (object reference on stack)",
        ],
        ["Non-Primitive (Reference)", "Array", "int[], String[], etc.", "Heap"],
        [
            "Non-Primitive (Reference)",
            "Class / Interface",
            "User-defined types",
            "Heap",
        ],
    ],
)
en.tip(
    "Primitive types are NOT objects (no methods, fixed size). "
    "Non-primitive types are objects stored on the heap. "
    "java.lang.String is immutable -- every modification creates a new object."
)

# -- 2023-I Q3 [8 Marks] -- CHOICE: Card Program OR Project Day ---------------
en.bookmark("2023-I Q3")
en.chap_box(
    "Q3 [8 Marks] -- Card Deck Program (Even/Odd) | OR | Project Day Calculator\n"
    "(MST-I, April 2023 -- Internal Choice)"
)
en.section("Option A: Card Deck -- Even or Odd (Recommended)")
en.definition(
    "Randomly pick a card from a deck of 52 cards. "
    "Number cards: 2-10 (even/odd by value). "
    "Face cards: Ace=1 (odd), Jack=11 (odd), Queen=12 (even), King=13 (odd)."
)
en.code_block(
    """\
import java.util.Random;

public class CardPickDemo {

    public static void main(String[] args) {
        // Standard deck: suits x ranks
        String[] suits = {"Hearts", "Diamonds", "Clubs", "Spades"};
        // Ranks: Ace(1), 2-10, Jack(11), Queen(12), King(13)
        String[] ranks = {
            "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10",
            "Jack", "Queen", "King"
        };

        // Pick a random card from 52
        Random rand  = new Random();
        int suitIdx  = rand.nextInt(4);   // 0-3
        int rankIdx  = rand.nextInt(13);  // 0-12
        int cardValue = rankIdx + 1;      // Ace=1, 2=2, ... King=13

        String suit = suits[suitIdx];
        String rank = ranks[rankIdx];

        System.out.println("Card picked: " + rank + " of " + suit);
        System.out.println("Card value : " + cardValue);

        // Check even or odd using modulo operator
        if (cardValue % 2 == 0) {
            System.out.println("Result     : EVEN card (" + rank + " = " + cardValue + ")");
        } else {
            System.out.println("Result     : ODD card  (" + rank + " = " + cardValue + ")");
        }

        // Special face card classification
        switch (rank) {
            case "Ace"  : System.out.println("[Face card] Ace   = 1  (ODD)");  break;
            case "Jack" : System.out.println("[Face card] Jack  = 11 (ODD)");  break;
            case "Queen": System.out.println("[Face card] Queen = 12 (EVEN)"); break;
            case "King" : System.out.println("[Face card] King  = 13 (ODD)");  break;
            default     : System.out.println("[Number card: " + rank + "]");
        }
    }
}
""",
    lang="java",
)
en.subsection("Sample Output")
en.code_block(
    """\
$ java CardPickDemo
Card picked: Queen of Hearts
Card value : 12
Result     : EVEN card (Queen = 12)
[Face card] Queen = 12 (EVEN)

-- Another run:
Card picked: 7 of Spades
Card value : 7
Result     : ODD card  (7 = 7)
[Number card: 7]
""",
    lang="text",
)

en.section("Option B: Project Day Calculator")
en.definition(
    "You have 30 days. Work only on EVEN days (2,4,6,...30 = 15 days). "
    "Finish 10% work per day. Find when the project is 100% complete."
)
en.code_block(
    """\
public class ProjectDayCalculator {
    public static void main(String[] args) {
        double workCompleted = 0.0;  // percentage
        int    dayFinished   = -1;

        for (int day = 1; day <= 30; day++) {
            if (day % 2 == 0) {          // only even days
                workCompleted += 10.0;   // 10% per even day
                System.out.printf("Day %2d (even): Work done = %.0f%%%n", day, workCompleted);

                if (workCompleted >= 100.0) {
                    dayFinished = day;
                    break;
                }
            }
        }

        if (dayFinished != -1) {
            System.out.println("Project completed on Day: " + dayFinished);
        } else {
            System.out.println("Project NOT completed within 30 days.");
        }
    }
}
""",
    lang="java",
)
en.subsection("Expected Output")
en.code_block(
    """\
Day  2 (even): Work done = 10%
Day  4 (even): Work done = 20%
Day  6 (even): Work done = 30%
Day  8 (even): Work done = 40%
Day 10 (even): Work done = 50%
Day 12 (even): Work done = 60%
Day 14 (even): Work done = 70%
Day 16 (even): Work done = 80%
Day 18 (even): Work done = 90%
Day 20 (even): Work done = 100%
Project completed on Day: 20
""",
    lang="text",
)

# -- 2023-I Q4 [3 Marks] ------------------------------------------------------
en.bookmark("2023-I Q4")
en.chap_box(
    "Q4 [3 Marks] -- Create a Class, Object and Access its Functions\n"
    "(MST-I, April 2023)"
)
en.section("Class and Object in Java")
en.definition(
    "A <b>class</b> is a blueprint (template) that defines attributes (fields) and "
    "behaviors (methods). An <b>object</b> is a concrete instance created from a class "
    "using the <b>new</b> keyword."
)
en.code_block(
    """\
// Define a class
class Car {
    // Fields (attributes)
    String brand;
    int    speed;

    // Constructor
    Car(String brand, int speed) {
        this.brand = brand;
        this.speed = speed;
    }

    // Method (behavior)
    void displayInfo() {
        System.out.println("Brand: " + brand + " | Speed: " + speed + " km/h");
    }

    void accelerate(int increase) {
        speed += increase;
        System.out.println(brand + " accelerated to " + speed + " km/h");
    }
}

public class ClassObjectDemo {
    public static void main(String[] args) {
        // Create objects (instances) using 'new'
        Car car1 = new Car("Toyota", 80);
        Car car2 = new Car("BMW",    120);

        // Access methods using dot operator
        car1.displayInfo();
        car2.displayInfo();
        car1.accelerate(30);
    }
}
""",
    lang="java",
)
en.subsection("Expected Output")
en.code_block(
    """\
Brand: Toyota | Speed: 80 km/h
Brand: BMW    | Speed: 120 km/h
Toyota accelerated to 110 km/h
""",
    lang="text",
)

# -- 2023-I Q5 [4 Marks] ------------------------------------------------------
en.bookmark("2023-I Q5")
en.chap_box("Q5 [4 Marks] -- Class vs Interface Comparison\n" "(MST-I, April 2023)")
en.section("Class and Interface -- Comparison")
en.info_table(
    ["Feature", "Class", "Interface"],
    [
        ["Keyword", "class", "interface"],
        [
            "Instantiation",
            "Can create objects directly: new MyClass()",
            "Cannot instantiate directly (no objects)",
        ],
        [
            "Methods",
            "Can have concrete (implemented) methods",
            "Methods are abstract by default (Java 7); default/static allowed (Java 8+)",
        ],
        [
            "Variables",
            "Can have instance variables (any type)",
            "Variables are implicitly public static final (constants)",
        ],
        ["Constructors", "Has constructors", "No constructors"],
        [
            "Inheritance",
            "Extends ONE class only (single inheritance)",
            "Can implement MULTIPLE interfaces (multiple inheritance)",
        ],
        [
            "Access Modifiers",
            "public, private, protected, default",
            "Methods are public by default",
        ],
        [
            "Usage",
            "Blueprint for real-world objects with state",
            "Defines a CONTRACT that implementing classes must fulfill",
        ],
        [
            "Example",
            "class Dog extends Animal {}",
            "interface Printable { void print(); }",
        ],
    ],
)
en.code_block(
    """\
// Interface example
interface Shape {
    double area();           // abstract by default
    default void describe() {
        System.out.println("I am a shape with area: " + area());
    }
}

// Class implementing the interface
class Circle implements Shape {
    double radius;
    Circle(double r) { this.radius = r; }

    @Override
    public double area() {
        return Math.PI * radius * radius;
    }
}

class Rectangle implements Shape {
    double w, h;
    Rectangle(double w, double h) { this.w = w; this.h = h; }

    @Override
    public double area() { return w * h; }
}

public class InterfaceDemo {
    public static void main(String[] args) {
        Shape c = new Circle(5);
        Shape r = new Rectangle(4, 6);
        c.describe();  // uses default method
        r.describe();
    }
}
""",
    lang="java",
)
en.subsection("Expected Output")
en.code_block(
    """\
I am a shape with area: 78.53981633974483
I am a shape with area: 24.0
""",
    lang="text",
)

# -- 2023-I Q6 [8 Marks] -- CHOICE: Polymorphism OR Inheritance ---------------
en.bookmark("2023-I Q6")
en.chap_box(
    "Q6 [8 Marks] -- Polymorphism | OR | Inheritance with All Types\n"
    "(MST-I, April 2023 -- Internal Choice)"
)
en.section("Option A: Polymorphism in Java (Recommended)")
en.definition(
    "<b>Polymorphism</b> (Greek: 'many forms') means the ability of one entity to take "
    "multiple forms. In Java, polymorphism allows a single method name or operator to "
    "behave differently depending on the context."
)
en.info_table(
    ["Type", "Also Called", "Resolved At", "Mechanism"],
    [
        [
            "Compile-time Polymorphism",
            "Method Overloading / Static Binding",
            "Compile time",
            "Same method name, different parameters",
        ],
        [
            "Runtime Polymorphism",
            "Method Overriding / Dynamic Binding",
            "Runtime (JVM)",
            "Subclass overrides parent method; called via parent reference",
        ],
    ],
)
en.code_block(
    """\
// ============================================================
// COMPILE-TIME POLYMORPHISM -- Method Overloading
// ============================================================
class MathOps {
    // Same name 'add', different parameter types/counts
    int    add(int a, int b)             { return a + b; }
    double add(double a, double b)       { return a + b; }
    int    add(int a, int b, int c)      { return a + b + c; }
}

// ============================================================
// RUNTIME POLYMORPHISM -- Method Overriding
// ============================================================
class Animal {
    void sound() {
        System.out.println("Animal makes a sound");
    }
}

class Dog extends Animal {
    @Override
    void sound() {  // overrides parent method
        System.out.println("Dog says: Woof!");
    }
}

class Cat extends Animal {
    @Override
    void sound() {
        System.out.println("Cat says: Meow!");
    }
}

public class PolymorphismDemo {
    public static void main(String[] args) {

        // Compile-time polymorphism
        MathOps m = new MathOps();
        System.out.println("add(2,3)       = " + m.add(2, 3));
        System.out.println("add(2.5, 3.5)  = " + m.add(2.5, 3.5));
        System.out.println("add(1, 2, 3)   = " + m.add(1, 2, 3));

        // Runtime polymorphism -- parent reference, child object
        Animal a1 = new Dog();  // upcasting
        Animal a2 = new Cat();
        Animal a3 = new Animal();

        a1.sound();  // calls Dog.sound() -- resolved at runtime
        a2.sound();  // calls Cat.sound()
        a3.sound();  // calls Animal.sound()
    }
}
""",
    lang="java",
)
en.subsection("Expected Output")
en.code_block(
    """\
add(2,3)       = 5
add(2.5, 3.5)  = 6.0
add(1, 2, 3)   = 6
Dog says: Woof!
Cat says: Meow!
Animal makes a sound
""",
    lang="text",
)

en.section("Option B: Inheritance -- All Types in Java")
en.definition(
    "<b>Inheritance</b> is an OOP mechanism where a subclass (child class) acquires the "
    "properties and behaviors of a superclass (parent class) using the <b>extends</b> keyword. "
    "Java supports 4 forms of inheritance (NOT multiple class inheritance)."
)
en.info_table(
    ["Type", "Supported?", "Description", "Keyword"],
    [
        ["Single", "YES", "One child extends one parent", "extends"],
        ["Multilevel", "YES", "A -> B -> C chain", "extends (chained)"],
        ["Hierarchical", "YES", "Multiple children extend one parent", "extends"],
        ["Multiple (via class)", "NO", "Diamond problem -- NOT allowed", "N/A"],
        ["Multiple (via interface)", "YES", "class C implements A, B", "implements"],
    ],
)
en.code_block(
    """\
// SINGLE Inheritance
class Vehicle {
    String brand = "Generic";
    void start() { System.out.println(brand + " vehicle started"); }
}
class Car extends Vehicle {
    int doors = 4;
    void honk() { System.out.println("Car honks!"); }
}

// MULTILEVEL Inheritance: Vehicle -> Car -> ElectricCar
class ElectricCar extends Car {
    int batteryPercent = 80;
    void charge() {
        System.out.println("Charging... Battery: " + batteryPercent + "%");
    }
}

// HIERARCHICAL Inheritance: Vehicle is parent of both Car and Truck
class Truck extends Vehicle {
    int payload = 5000;
    void loadCargo() {
        System.out.println("Truck loading " + payload + " kg cargo");
    }
}

// MULTIPLE inheritance via Interface
interface Electric { void charge(); }
interface Hybrid   { void switchFuel(); }
class HybridCar extends Car implements Electric, Hybrid {
    public void charge()     { System.out.println("HybridCar charging battery"); }
    public void switchFuel() { System.out.println("HybridCar switching to petrol"); }
}

public class InheritanceDemo {
    public static void main(String[] args) {
        // Single
        Car car = new Car();
        car.brand = "Toyota";
        car.start();   // inherited from Vehicle
        car.honk();

        // Multilevel
        ElectricCar ev = new ElectricCar();
        ev.brand = "Tesla";
        ev.start();    // from Vehicle
        ev.honk();     // from Car
        ev.charge();   // own method

        // Hierarchical
        Truck truck = new Truck();
        truck.brand = "Tata";
        truck.start();
        truck.loadCargo();

        // Multiple via interface
        HybridCar hc = new HybridCar();
        hc.brand = "Honda";
        hc.start();
        hc.charge();
        hc.switchFuel();
    }
}
""",
    lang="java",
)
en.subsection("Expected Output")
en.code_block(
    """\
Toyota vehicle started
Car honks!
Tesla vehicle started
Car honks!
Charging... Battery: 80%
Tata vehicle started
Truck loading 5000 kg cargo
Honda vehicle started
HybridCar charging battery
HybridCar switching to petrol
""",
    lang="text",
)

en.br()

# #############################################################################
#  MST-II  --  May 2023  (Jan-June 2023 Session)
# #############################################################################
en.bookmark("MST-II May 2023")
en.part_box("MST-II -- May 2023  (Session: Jan-June 2023)")
en.note(
    "Exam Details: MST-II | Date: May 2023 | Max Marks: 30 | Time: 1 Hour | "
    "Marks: Q1=3m, Q2=4m, Q3=8m (choice), Q4=3m, Q5=4m, Q6=8m (choice)"
)
en.sp(6)

# -- 2023-II Q1 [3 Marks] -----------------------------------------------------
en.bookmark("2023-II Q1")
en.chap_box(
    "Q1 [3 Marks] -- Attributes of the <applet> HTML Tag\n" "(MST-II, May 2023)"
)
en.section("The <applet> HTML Tag")
en.definition(
    "The <b>&lt;applet&gt;</b> tag is used to embed a Java applet inside an HTML page. "
    "It was the standard way to run Java applets in browsers (now deprecated). "
    "The tag has several attributes that control how the applet is loaded and displayed."
)
en.info_table(
    ["Attribute", "Required?", "Description", "Example"],
    [
        ["code", "YES", "Name of the compiled .class file", 'code="HelloApplet.class"'],
        ["width", "YES", "Width of the applet display area in pixels", "width=400"],
        ["height", "YES", "Height of the applet display area in pixels", "height=200"],
        [
            "codebase",
            "No",
            "Directory/URL where the .class file is located",
            'codebase="applets/"',
        ],
        [
            "archive",
            "No",
            "JAR file(s) containing the applet and resources",
            'archive="mylib.jar"',
        ],
        [
            "name",
            "No",
            "Name for the applet (for inter-applet communication)",
            'name="myApplet"',
        ],
        [
            "alt",
            "No",
            "Alternate text if browser does not support applets",
            'alt="Java required"',
        ],
        [
            "align",
            "No",
            "Alignment of applet w.r.t. surrounding text",
            'align="middle"',
        ],
        ["hspace", "No", "Horizontal space around the applet in pixels", "hspace=10"],
        ["vspace", "No", "Vertical space around the applet in pixels", "vspace=10"],
        [
            "param",
            "No",
            "Pass parameters to the applet via name/value pairs",
            '<param name="color" value="blue">',
        ],
    ],
)
en.code_block(
    """\
<!-- Complete example of applet tag with common attributes -->
<html>
<body>
  <applet
    code      = "HelloApplet.class"
    codebase  = "."
    width     = "400"
    height    = "200"
    name      = "helloApp"
    alt       = "Java Applet requires JRE plugin"
    hspace    = "5"
    vspace    = "5">
    <param name="message" value="Welcome to Java Applets!">
    Your browser does not support Java Applets.
  </applet>
</body>
</html>
""",
    lang="html",
)

# -- 2023-II Q2 [4 Marks] -----------------------------------------------------
en.bookmark("2023-II Q2")
en.chap_box(
    "Q2 [4 Marks] -- Java Applet: Display 'Hello World' in Web Browser\n"
    "(MST-II, May 2023)"
)
en.section("Hello World Java Applet")
en.definition(
    "An applet extends <b>java.applet.Applet</b> and overrides the <b>paint(Graphics g)</b> "
    "method to draw content. Unlike standalone apps, applets run in a browser or "
    "appletviewer -- there is <b>no main() method</b>."
)
en.code_block(
    """\
import java.applet.Applet;
import java.awt.Graphics;
import java.awt.Font;
import java.awt.Color;

/*
 * HTML file to run this applet (save as HelloApplet.html):
 *
 * <html>
 * <body>
 *   <applet code="HelloApplet.class" width="400" height="150">
 *   </applet>
 * </body>
 * </html>
 *
 * Compile : javac HelloApplet.java
 * Run     : appletviewer HelloApplet.html
 */
public class HelloApplet extends Applet {

    @Override
    public void init() {
        // Set background color (called once when applet loads)
        setBackground(Color.LIGHT_GRAY);
    }

    @Override
    public void paint(Graphics g) {
        // Set font and color for the text
        g.setFont(new Font("Arial", Font.BOLD, 24));
        g.setColor(Color.BLUE);

        // Draw the string at position (x=60, y=80) in the applet window
        g.drawString("Hello World", 60, 80);

        // Draw a decorative rectangle border
        g.setColor(Color.RED);
        g.drawRect(10, 10, 380, 130);
    }
}
""",
    lang="java",
)
en.subsection("Output in appletviewer")
en.code_block(
    """\
[appletviewer opens a window titled 'Applet Viewer: HelloApplet.class']
[Gray background with blue bold text 'Hello World' at position (60,80)]
[Red rectangle border drawn around the applet area]
[Status bar at bottom shows: 'Applet started']
""",
    lang="text",
)

# -- 2023-II Q3 [8 Marks] -- CHOICE: Applet Lifecycle OR init/start/paint/stop
en.bookmark("2023-II Q3")
en.chap_box(
    "Q3 [8 Marks] -- Applet Lifecycle with Example | OR | Applet Methods Explained\n"
    "(MST-II, May 2023 -- Internal Choice)"
)
en.note(
    "This question overlaps with Q1 [10 Marks] MST-II April 2026 which provides a "
    "more comprehensive answer (StateMachine diagram + full code). "
    "The answer below covers the 8-mark version with all method details."
)
en.section("Applet Lifecycle Methods -- Detailed")
en.info_table(
    ["Method", "Called By", "When Called", "Purpose", "Override?"],
    [
        [
            "init()",
            "Browser/appletviewer",
            "Once: when applet is first loaded",
            "One-time initialization; set up UI, load images, initialize variables",
            "Often",
        ],
        [
            "start()",
            "Browser/appletviewer",
            "After init(); again when page is revisited",
            "Begin execution; start threads, begin animations",
            "Often",
        ],
        [
            "paint(Graphics g)",
            "AWT paint thread",
            "When applet needs rendering (first display, resize, expose)",
            "Draw text and graphics using Graphics object",
            "Always",
        ],
        [
            "stop()",
            "Browser/appletviewer",
            "When user navigates away from the page",
            "Pause execution; stop threads/animations",
            "Sometimes",
        ],
        [
            "destroy()",
            "Browser/appletviewer",
            "When applet is permanently removed",
            "Free all resources; close connections",
            "Sometimes",
        ],
    ],
)
en.code_block(
    """\
import java.applet.Applet;
import java.awt.*;

public class LifecycleDemoApplet extends Applet {

    String status = "Applet not started";
    int    paintCount = 0;

    @Override
    public void init() {
        status = "init() called -- Applet initialized";
        setBackground(Color.BLACK);
        setForeground(Color.GREEN);
        System.out.println("[LIFECYCLE] init() called");
    }

    @Override
    public void start() {
        status = "start() called -- Applet running";
        System.out.println("[LIFECYCLE] start() called");
        repaint();  // trigger paint()
    }

    @Override
    public void paint(Graphics g) {
        paintCount++;
        g.setFont(new Font("Courier New", Font.BOLD, 14));
        g.drawString("Status    : " + status,  20, 40);
        g.drawString("Repaints  : " + paintCount, 20, 70);
        g.drawString("Lifecycle : init -> start -> paint -> stop -> destroy", 20, 100);
        System.out.println("[LIFECYCLE] paint() called (repaint #" + paintCount + ")");
    }

    @Override
    public void stop() {
        status = "stop() called -- Applet paused";
        System.out.println("[LIFECYCLE] stop() called");
    }

    @Override
    public void destroy() {
        System.out.println("[LIFECYCLE] destroy() called -- cleanup done");
    }
}
""",
    lang="java",
)
en.subsection("Expected Console Output")
en.code_block(
    """\
[LIFECYCLE] init() called
[LIFECYCLE] start() called
[LIFECYCLE] paint() called (repaint #1)
[LIFECYCLE] paint() called (repaint #2)   <- window resized
[LIFECYCLE] stop() called                 <- user navigated away
[LIFECYCLE] start() called                <- user returned to page
[LIFECYCLE] paint() called (repaint #3)
[LIFECYCLE] stop() called
[LIFECYCLE] destroy() called -- cleanup done
""",
    lang="text",
)

# -- 2023-II Q4 [3 Marks] -----------------------------------------------------
en.bookmark("2023-II Q4")
en.chap_box("Q4 [3 Marks] -- Event Delegation Model\n" "(MST-II, May 2023)")
en.note(
    "This question overlaps with Q2 [10 Marks] MST-III May 2026 which provides a full "
    "answer including SequenceDiagram. Below is a concise 3-mark summary."
)
en.section("Event Delegation Model -- Summary")
en.definition(
    "The <b>Delegation Event Model</b> (introduced in Java 1.1) is the standard Java "
    "mechanism for handling GUI events. Instead of the event source handling its own events, "
    "it <b>delegates</b> (passes) the handling responsibility to a separate <b>listener</b> object."
)
en.bullet(
    [
        "<b>Event Source:</b> The GUI component that generates the event (e.g., Button, TextField).",
        "<b>Event Object:</b> Encapsulates event information (e.g., ActionEvent, MouseEvent, KeyEvent).",
        "<b>Event Listener:</b> An object implementing a listener interface that handles the event "
        "(e.g., ActionListener.actionPerformed(), MouseListener.mouseClicked()).",
    ]
)
en.highlight(
    "Source --> fires Event --> EDT calls --> Listener.handlerMethod() --> handles event"
)
en.tip(
    "Registration: source.addXxxListener(listenerObject). "
    "E.g., button.addActionListener(this). "
    "Advantage: clean separation between source and handler -- promotes loose coupling."
)

# -- 2023-II Q5 [4 Marks] -----------------------------------------------------
en.bookmark("2023-II Q5")
en.chap_box("Q5 [4 Marks] -- AWT vs Swing -- Differentiation\n" "(MST-II, May 2023)")
en.section("AWT vs Swing -- Detailed Comparison")
en.info_table(
    ["Feature", "AWT (Abstract Window Toolkit)", "Swing (javax.swing)"],
    [
        ["Package", "java.awt", "javax.swing"],
        [
            "Type",
            "Heavyweight components (OS-native peers)",
            "Lightweight components (pure Java, no OS peers)",
        ],
        [
            "Look and Feel",
            "Platform-dependent (looks different on Win/Mac/Linux)",
            "Platform-independent (consistent look via Pluggable L&F)",
        ],
        [
            "Performance",
            "Faster for simple apps (native rendering)",
            "Slightly slower but more consistent",
        ],
        [
            "Components",
            "Button, TextField, Label, Frame, Panel",
            "JButton, JTextField, JLabel, JFrame, JPanel (J prefix)",
        ],
        ["MVC Support", "Not built-in", "Built-in Model-View-Controller architecture"],
        [
            "Custom Drawing",
            "Limited via Canvas",
            "Powerful via JPanel + paintComponent()",
        ],
        ["Tooltips", "Not supported", "Supported via setToolTipText()"],
        ["Icons", "Not supported in most components", "Supported (ImageIcon)"],
        ["Double Buffering", "Manual", "Built-in (flicker-free rendering)"],
        ["Preferred for", "Simple legacy apps", "Modern desktop applications"],
    ],
)
en.tip(
    "Rule of thumb: Swing components have 'J' prefix (JButton, JFrame, JLabel). "
    "Swing extends AWT -- JComponent extends Container, JFrame extends Frame. "
    "For new projects, always prefer Swing or JavaFX over AWT."
)

# -- 2023-II Q6 [8 Marks] -- CHOICE: Container/Frame/Window OR Graphics -------
en.bookmark("2023-II Q6")
en.chap_box(
    "Q6 [8 Marks] -- Container, Frame & Window with Examples | OR | Graphic Controls\n"
    "(MST-II, May 2023 -- Internal Choice)"
)
en.section(
    "Option A: Container, Frame and Window -- Explained with Examples (Recommended)"
)
en.definition(
    "In Java AWT, <b>Container</b>, <b>Window</b>, and <b>Frame</b> form part of the "
    "component hierarchy. They define how GUI elements are structured and displayed."
)
en.info_table(
    ["Class", "Extends", "Visible?", "Key Purpose"],
    [
        [
            "Container",
            "Component",
            "No (abstract grouping)",
            "Can hold other Components via add()",
        ],
        [
            "Window",
            "Container",
            "Yes (no title/border)",
            "Standalone window without decorations",
        ],
        [
            "Frame",
            "Window",
            "Yes (with title + border)",
            "Standard application window with title bar",
        ],
        [
            "Dialog",
            "Window",
            "Yes (modal/non-modal)",
            "Pop-up dialog box, attached to a parent Frame",
        ],
        [
            "Panel",
            "Container",
            "No (embedded only)",
            "Groups components; must be added to Frame/Window",
        ],
    ],
)
en.code_block(
    """\
import java.awt.*;
import java.awt.event.*;

public class ContainerFrameDemo {
    public static void main(String[] args) {

        // --- FRAME: top-level window with title bar ---
        Frame frame = new Frame("Container/Frame Demo");
        frame.setSize(500, 350);
        frame.setLayout(new BorderLayout());
        frame.setBackground(Color.WHITE);

        // --- LABEL in CENTER ---
        Label centerLabel = new Label(
            "Frame > Window > Container > Component", Label.CENTER
        );
        centerLabel.setFont(new Font("Arial", Font.BOLD, 14));

        // --- PANEL (Container): groups buttons in SOUTH ---
        Panel buttonPanel = new Panel(new FlowLayout(FlowLayout.CENTER, 10, 5));
        buttonPanel.setBackground(Color.LIGHT_GRAY);

        Button infoBtn  = new Button("Show Info");
        Button exitBtn  = new Button("Exit");
        buttonPanel.add(infoBtn);
        buttonPanel.add(exitBtn);

        // --- PANEL (Container): labels in NORTH ---
        Panel northPanel = new Panel(new FlowLayout(FlowLayout.LEFT));
        northPanel.add(new Label("AWT Hierarchy Demo"));
        northPanel.setBackground(Color.CYAN);

        // Add panels and label to the Frame
        frame.add(northPanel,   BorderLayout.NORTH);
        frame.add(centerLabel,  BorderLayout.CENTER);
        frame.add(buttonPanel,  BorderLayout.SOUTH);

        // Button listeners
        infoBtn.addActionListener(e -> {
            System.out.println("Frame   : top-level window (title + border)");
            System.out.println("Panel   : container grouping buttons");
            System.out.println("Label   : non-editable text component");
            System.out.println("Button  : clickable action trigger");
        });
        exitBtn.addActionListener(e -> System.exit(0));

        frame.addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent e) { System.exit(0); }
        });

        frame.setVisible(true);
    }
}
""",
    lang="java",
)
en.subsection("Expected Console Output (when 'Show Info' button clicked)")
en.code_block(
    """\
[A 500x350 window titled 'Container/Frame Demo' opens]
[NORTH: cyan panel with 'AWT Hierarchy Demo' label]
[CENTER: bold label 'Frame > Window > Container > Component']
[SOUTH: light gray panel with 'Show Info' and 'Exit' buttons]

-- On clicking 'Show Info':
Frame   : top-level window (title + border)
Panel   : container grouping buttons
Label   : non-editable text component
Button  : clickable action trigger
""",
    lang="text",
)

en.section("Option B: Java Program for Various Graphic Controls")
en.code_block(
    """\
import java.applet.Applet;
import java.awt.*;

/*
 * <applet code="GraphicsDemo.class" width="450" height="320"></applet>
 */
public class GraphicsDemo extends Applet {

    @Override
    public void paint(Graphics g) {
        // 1. drawLine -- draws a straight line
        g.setColor(Color.BLACK);
        g.drawLine(20, 30, 200, 30);
        g.drawString("drawLine", 210, 35);

        // 2. drawRect -- draws rectangle outline
        g.setColor(Color.BLUE);
        g.drawRect(20, 50, 120, 60);
        g.drawString("drawRect", 160, 85);

        // 3. fillRect -- draws filled rectangle
        g.setColor(Color.CYAN);
        g.fillRect(20, 130, 120, 50);
        g.setColor(Color.BLACK);
        g.drawString("fillRect", 160, 160);

        // 4. drawOval -- draws oval/circle outline
        g.setColor(Color.RED);
        g.drawOval(20, 200, 100, 70);
        g.drawString("drawOval", 135, 240);

        // 5. fillOval -- draws filled oval/circle
        g.setColor(Color.ORANGE);
        g.fillOval(260, 200, 100, 70);
        g.setColor(Color.BLACK);
        g.drawString("fillOval", 375, 240);

        // 6. drawString -- draws text
        g.setFont(new Font("Arial", Font.BOLD, 16));
        g.setColor(Color.MAGENTA);
        g.drawString("Java Graphics Controls", 80, 300);
    }
}
""",
    lang="java",
)

en.subsection("Expected GUI Display")
en.code_block(
    """\
[An Applet Window of size 450x320 opens rendering the following shapes:]
1. A straight black line from coordinates (20,30) to (200,30), with text
   "drawLine" rendered next to it.
2. A blue outlined rectangle at (20,50) with width 120 and height 60,
   with text "drawRect" rendered next to it.
3. A solid filled cyan rectangle at (20,130) with width 120 and height 50,
   with text "fillRect" rendered next to it.
4. A red outlined oval at (20,200) with width 100 and height 70,
   with text "drawOval" rendered next to it.
5. A solid filled orange oval at (260,200) with width 100 and height 70,
   with text "fillOval" rendered next to it.
6. A large bold magenta heading "Java Graphics Controls" rendered at the
   bottom at coordinates (80,300).
""",
    lang="text",
)

en.subsection("Graphics Methods Reference")
en.info_table(
    ["Method", "Description", "Parameters"],
    [
        [
            "drawLine(x1,y1,x2,y2)",
            "Draws a line from (x1,y1) to (x2,y2)",
            "int x1, y1, x2, y2",
        ],
        [
            "drawRect(x,y,w,h)",
            "Draws rectangle outline",
            "int x, y (top-left), width, height",
        ],
        ["fillRect(x,y,w,h)", "Draws filled rectangle", "int x, y, width, height"],
        [
            "drawOval(x,y,w,h)",
            "Draws oval/circle outline in bounding box",
            "int x, y (bounding box top-left), width, height",
        ],
        ["fillOval(x,y,w,h)", "Draws filled oval/circle", "int x, y, width, height"],
        [
            "drawString(str,x,y)",
            "Draws text at position (x,y)",
            "String text, int x (left), int y (baseline)",
        ],
        [
            "setColor(Color c)",
            "Sets current drawing color",
            "Color constant or new Color(r,g,b)",
        ],
        [
            "setFont(Font f)",
            "Sets current font for drawString",
            "new Font(name, style, size)",
        ],
    ],
)

en.br()

# #############################################################################
#  MST-III  --  May 2023  (Jan-June 2023 Session)
# #############################################################################
en.bookmark("MST-III May 2023")
en.part_box("MST-III -- May 2023  (Session: Jan-June 2023)")
en.note(
    "Exam Details: MST-III | Date: May 2023 | Max Marks: 30 | Time: 1 Hour | "
    "All questions carry equal marks (30 / 5 = 6 marks each)"
)
en.sp(6)

# -- 2023-III Q1 [6 Marks] ----------------------------------------------------
en.bookmark("2023-III Q1")
en.chap_box(
    "Q1 [6 Marks] -- Card Deck: Even or Odd (Random Pick)\n" "(MST-III, May 2023)"
)
en.note(
    "This question is identical to Q3 Option A [8 Marks] in MST-I April 2023. "
    "The 8-mark answer already covers this fully -- see MST-I April 2023 Q3. "
    "Below is the 6-mark version with a focused explanation."
)
en.section("Card Deck Program -- 6 Mark Version")
en.definition(
    "A standard deck has 52 cards: 4 suits x 13 ranks. "
    "Ace=1(odd), 2-10 (even/odd by value), Jack=11(odd), Queen=12(even), King=13(odd). "
    "Use Random to pick a card, then check if its numeric value is even or odd."
)
en.code_block(
    """\
import java.util.Random;

public class CardEvenOdd {
    public static void main(String[] args) {
        String[] ranks = {
            "Ace", "2", "3", "4", "5", "6", "7",
            "8", "9", "10", "Jack", "Queen", "King"
        };
        String[] suits = {"Hearts", "Diamonds", "Clubs", "Spades"};

        Random rand = new Random();
        int rankIdx   = rand.nextInt(13);  // 0-12
        int suitIdx   = rand.nextInt(4);   // 0-3
        int cardValue = rankIdx + 1;       // Ace=1 to King=13

        System.out.println("Card : " + ranks[rankIdx] + " of " + suits[suitIdx]);
        System.out.println("Value: " + cardValue);
        System.out.println("Type : " + (cardValue % 2 == 0 ? "EVEN" : "ODD"));
    }
}
""",
    lang="java",
)
en.subsection("Sample Output")
en.code_block(
    """\
Card : King of Clubs
Value: 13
Type : ODD
""",
    lang="text",
)

# -- 2023-III Q2 [6 Marks] ----------------------------------------------------
en.bookmark("2023-III Q2")
en.chap_box(
    "Q2 [6 Marks] -- Inheritance: Types and Implementation\n" "(MST-III, May 2023)"
)
en.note(
    "This question overlaps with Q6 Option B [8 Marks] in MST-I April 2023 which provides "
    "a more comprehensive answer. The 6-mark version below is more concise."
)
en.section("Types of Inheritance in Java -- 6 Mark Summary")
en.info_table(
    ["Type", "Supported?", "Syntax"],
    [
        ["Single", "YES", "class B extends A {}"],
        ["Multilevel", "YES", "class C extends B {} where B extends A {}"],
        ["Hierarchical", "YES", "class B extends A {} and class C extends A {}"],
        ["Multiple (via class)", "NO -- Diamond Problem", "NOT allowed"],
        ["Multiple (via interface)", "YES", "class C implements A, B {}"],
    ],
)
en.code_block(
    """\
// Single + Multilevel + Hierarchical in one program
class Shape {
    String color = "Red";
    void draw() { System.out.println(color + " shape drawn"); }
}

// Single: Circle extends Shape
class Circle extends Shape {
    double radius;
    Circle(double r) { radius = r; }
    double area() { return Math.PI * radius * radius; }
}

// Multilevel: ColoredCircle extends Circle extends Shape
class ColoredCircle extends Circle {
    ColoredCircle(double r, String c) {
        super(r);
        color = c;
    }
    void display() {
        System.out.printf("%s Circle: area=%.2f%n", color, area());
    }
}

// Hierarchical: Rectangle also extends Shape
class Rectangle extends Shape {
    double w, h;
    Rectangle(double w, double h) { this.w=w; this.h=h; }
    double area() { return w * h; }
}

public class InheritanceTypes {
    public static void main(String[] args) {
        Circle c = new Circle(5);
        c.draw();                          // inherited from Shape
        System.out.printf("Circle area: %.2f%n", c.area());

        ColoredCircle cc = new ColoredCircle(3, "Blue");
        cc.draw();                         // inherited from Shape via Circle
        cc.display();

        Rectangle r = new Rectangle(4, 6);
        r.draw();
        System.out.printf("Rectangle area: %.2f%n", r.area());
    }
}
""",
    lang="java",
)
en.subsection("Expected Output")
en.code_block(
    """\
Red shape drawn
Circle area: 78.54
Blue shape drawn
Blue Circle: area=28.27
Red shape drawn
Rectangle area: 24.00
""",
    lang="text",
)

# -- 2023-III Q3 [6 Marks] ----------------------------------------------------
en.bookmark("2023-III Q3")
en.chap_box("Q3 [6 Marks] -- Applet Lifecycle with Example\n" "(MST-III, May 2023)")
en.note(
    "This question overlaps with Q1 [10 Marks] MST-II April 2026 (most comprehensive) "
    "and Q3 [8 Marks] MST-II May 2023. The 6-mark answer below is concise but complete."
)
en.section("Applet Lifecycle -- 6 Mark Summary")
en.info_table(
    ["Phase", "Method", "Purpose"],
    [
        ["Load", "init()", "Initialize applet once -- setup UI, load resources"],
        [
            "Start",
            "start()",
            "Begin execution -- called after init() and on page return",
        ],
        [
            "Display",
            "paint(Graphics g)",
            "Render content -- called by AWT thread when display needed",
        ],
        ["Stop", "stop()", "Pause when page is left -- stop threads"],
        ["Destroy", "destroy()", "Cleanup when applet is removed -- free memory"],
    ],
)
en.highlight("init() -> start() -> paint()  [ <--> stop() <--> start() ]  -> destroy()")
en.code_block(
    """\
import java.applet.Applet;
import java.awt.Graphics;

public class LifecycleApplet extends Applet {

    @Override
    public void init() {
        System.out.println("init(): Setting up applet...");
    }

    @Override
    public void start() {
        System.out.println("start(): Applet is now running");
    }

    @Override
    public void paint(Graphics g) {
        g.drawString("Applet Lifecycle Demo", 50, 80);
        g.drawString("init -> start -> paint -> stop -> destroy", 30, 110);
        System.out.println("paint(): Rendering applet display");
    }

    @Override
    public void stop() {
        System.out.println("stop(): Applet paused (page left)");
    }

    @Override
    public void destroy() {
        System.out.println("destroy(): Applet cleaned up");
    }
}
""",
    lang="java",
)
en.subsection("Console Output")
en.code_block(
    """\
init(): Setting up applet...
start(): Applet is now running
paint(): Rendering applet display
stop(): Applet paused (page left)
start(): Applet is now running
paint(): Rendering applet display
stop(): Applet paused (page left)
destroy(): Applet cleaned up
""",
    lang="text",
)

# -- 2023-III Q4 [6 Marks] ----------------------------------------------------
en.bookmark("2023-III Q4")
en.chap_box("Q4 [6 Marks] -- AWT vs Swing: Differentiation\n" "(MST-III, May 2023)")
en.note(
    "This question overlaps with Q5 [4 Marks] MST-II May 2023. "
    "The 6-mark version provides an expanded answer."
)
en.section("AWT vs Swing -- 6 Mark Answer")
en.definition(
    "<b>AWT (Abstract Window Toolkit)</b> is Java's original GUI framework using OS-native components. "
    "<b>Swing</b> is a more powerful, platform-independent GUI framework built on top of AWT "
    "with pure-Java (lightweight) components."
)
en.info_table(
    ["Feature", "AWT", "Swing"],
    [
        ["Components", "Heavyweight (OS-native peers)", "Lightweight (pure Java)"],
        ["Look & Feel", "Platform-dependent", "Pluggable, consistent on all platforms"],
        ["Package", "java.awt", "javax.swing"],
        ["Prefix", "Button, Frame, Label", "JButton, JFrame, JLabel"],
        ["MVC", "Not built-in", "Built-in MVC architecture"],
        ["Tooltips", "Not supported", "setToolTipText() supported"],
        ["Icons", "Not supported", "ImageIcon supported"],
        ["Double Buffering", "Manual", "Built-in (no flicker)"],
        ["Tables, Trees", "Not available", "JTable, JTree available"],
        ["Performance", "Faster (native)", "Slightly slower but feature-rich"],
    ],
)
en.code_block(
    """\
import javax.swing.*;   // Swing
import java.awt.*;      // AWT

public class AwtVsSwingDemo {
    public static void main(String[] args) {

        // -- AWT Frame --
        java.awt.Frame awtFrame = new java.awt.Frame("AWT Frame");
        awtFrame.setSize(200, 100);
        awtFrame.add(new java.awt.Button("AWT Button"));
        awtFrame.setVisible(true);

        // -- Swing JFrame --
        JFrame swingFrame = new JFrame("Swing JFrame");
        swingFrame.setSize(200, 100);
        JButton jBtn = new JButton("Swing JButton");
        jBtn.setToolTipText("Hover tooltip -- not in AWT!");
        swingFrame.add(jBtn);
        swingFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        swingFrame.setVisible(true);
    }
}
""",
    lang="java",
)
en.subsection("Output")
en.code_block(
    """\
[Two windows open side by side]
Left : AWT Frame (200x100) with native OS-styled 'AWT Button'
Right: Swing JFrame (200x100) with Java-styled 'Swing JButton'
       (hovering over Swing button shows tooltip: 'Hover tooltip -- not in AWT!')
""",
    lang="text",
)

# -- 2023-III Q5 [6 Marks] ----------------------------------------------------
en.bookmark("2023-III Q5")
en.chap_box(
    "Q5 [6 Marks] -- JDBC Connectivity with a Java Program\n" "(MST-III, May 2023)"
)
en.note(
    "This question overlaps with Q1 [10 Marks] and Q3 [10 Marks] in MST-III May 2026 "
    "which provide the most comprehensive JDBC answers. "
    "The 6-mark version below is a focused, complete JDBC connectivity demonstration."
)
en.section("JDBC Connectivity -- 6 Mark Answer")
en.definition(
    "<b>JDBC (Java Database Connectivity)</b> is a Java API that provides a standard "
    "interface to connect Java programs to relational databases. The 6-step process: "
    "Load Driver -> Get Connection -> Create Statement -> Execute Query -> Process ResultSet -> Close."
)
en.code_block(
    """\
import java.sql.*;

public class JDBCDemo {

    public static void main(String[] args) {

        // Connection parameters for MySQL remote database
        String url  = "jdbc:mysql://localhost:3306/college_db?useSSL=false";
        String user = "root";
        String pass = "password123";

        try {
            // Step 1: Load JDBC Driver (auto in JDBC 4.0+, shown for reference)
            Class.forName("com.mysql.cj.jdbc.Driver");
            System.out.println("Step 1: Driver loaded");

            // Step 2: Establish Connection
            Connection conn = DriverManager.getConnection(url, user, pass);
            System.out.println("Step 2: Connected to database");

            // Step 3: Create Statement
            Statement stmt = conn.createStatement();
            System.out.println("Step 3: Statement created");

            // Step 4: Execute Query
            ResultSet rs = stmt.executeQuery("SELECT id, name, marks FROM students");
            System.out.println("Step 4: Query executed");

            // Step 5: Process ResultSet
            System.out.println("Step 5: Processing results...");
            System.out.println("ID  | Name             | Marks");
            System.out.println("----|------------------|------");
            while (rs.next()) {
                System.out.printf("%-3d | %-16s | %.2f%n",
                    rs.getInt("id"),
                    rs.getString("name"),
                    rs.getDouble("marks"));
            }

            // Step 6: Close Resources
            rs.close();
            stmt.close();
            conn.close();
            System.out.println("Step 6: Resources closed");

        } catch (ClassNotFoundException e) {
            System.err.println("Driver not found: " + e.getMessage());
        } catch (SQLException e) {
            System.err.println("SQL Error: " + e.getMessage());
        }
    }
}
""",
    lang="java",
)
en.subsection("Expected Output")
en.code_block(
    """\
Step 1: Driver loaded
Step 2: Connected to database
Step 3: Statement created
Step 4: Query executed
Step 5: Processing results...
ID  | Name             | Marks
----|------------------|------
1   | Alice Sharma     | 88.50
2   | Bob Verma        | 55.00
3   | Carol Singh      | 73.20
4   | David Kumar      | 45.00
5   | Eva Patel        | 92.00
6   | Frank Gupta      | 61.50
Step 6: Resources closed
""",
    lang="text",
)

# -- Build ---------------------------------------------------------------------
en.build_doc("Java_MST_Answers.pdf")
