"""
Java Programming (IT408) -- Unit II Notes
UIT-RGPV (Autonomous) Bhopal | Semester IV
Complete exam notes with Java syntax highlighting and vector diagrams.
Run: python java_unit2_notes.py
Output: Java_Unit2_Notes.pdf
"""

from __future__ import annotations

import paperforge_notes as pn
import paperforge_diagrams as pd

# =============================================================================
#  THEME & GLOBAL FOOTER SETUP
# =============================================================================
pn.set_story([])
pn.set_theme(pn.MIDNIGHT_DARK)

pn.set_global_footer(
    left="Java Programming (IT408) -- Unit II",
    right="UIT-RGPV (Autonomous) Bhopal",
    show_page_num=True,
)

diag_theme = pd.DiagramTheme.from_notes_theme(pn.get_theme())

# =============================================================================
#  COVER PAGE
# =============================================================================
pn.bookmark("Cover Page")
pn.suppress_footer(page_only=True)
pn.sp(28)

pn.cover_card(
    "JAVA PROGRAMMING",
    "Unit II -- Classes, OOP, Packages, Exceptions & Threads",
)
# pn.cover_subtitle(
#     [
#         "Subject Code: IT408  |  UIT-RGPV (Autonomous) Bhopal  |  Semester IV",
#         "Complete Exam Notes: Class Fundamentals, Inheritance, Packages, Interfaces,",
#         "Exception Handling, and Multithreading with Code Examples and Diagrams",
#     ]
# )
pn.sp(10)
pn.rule(pn.get_theme().rl(pn.get_theme().accent), 1.5)
pn.sp(8)

pn.info_table(
    ["Section", "Syllabus Topics Covered"],
    [
        [
            "2.1 Class Fundamentals",
            "Class syntax, fields, methods, access specifiers, object creation",
        ],
        [
            "2.2 Constructors",
            "Default, parameterized, copy constructors, constructor chaining",
        ],
        [
            "2.3 The this Keyword",
            "Reference to current instance, constructor chaining via this()",
        ],
        [
            "2.4 Method Overloading",
            "Compile-time polymorphism, rules, type promotion in overloading",
        ],
        [
            "2.5 Objects as Parameters",
            "Pass by reference, object arguments, returning objects",
        ],
        [
            "2.6 Garbage Collection",
            "JVM GC, finalize() method, System.gc(), weak references",
        ],
        [
            "2.7 Abstract Classes",
            "abstract keyword, abstract methods, partial implementation",
        ],
        [
            "2.8 Inheritance",
            "extends keyword, super keyword, method overriding, final classes",
        ],
        [
            "2.9 Multilevel Hierarchy",
            "Constructor chaining in hierarchy, super(), toString(), equals()",
        ],
        [
            "2.10 Packages",
            "package declaration, import, CLASSPATH, access across packages",
        ],
        [
            "2.11 Interfaces",
            "interface keyword, implements, default/static methods (Java 8+)",
        ],
        [
            "2.12 Exception Handling",
            "try-catch-finally, throws, throw, checked vs unchecked, custom",
        ],
        [
            "2.13 Multithreading",
            "Thread class, Runnable, lifecycle, synchronization, inter-thread comm",
        ],
        [
            "2.14 Exam Flashcards",
            "High-yield revision cards, core definitions, and key exam focus areas for Unit II",
        ],
    ],
    col_widths=["30%", "70%"],
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
pn.part_box("UNIT II -- JAVA CLASSES, OOP, PACKAGES, EXCEPTIONS & THREADS")

# =============================================================================
#  2.1  CLASS FUNDAMENTALS
# =============================================================================
pn.chap_box("2.1  Class Fundamentals")
pn.section("What is a Class?")
pn.definition(
    "<b>Class:</b> A class is a user-defined data type (blueprint/template) that encapsulates "
    "data (called <i>fields</i> or <i>instance variables</i>) and behavior (called <i>methods</i>). "
    "A class is declared using the <code>class</code> keyword. Objects are instances of a class, "
    "created at runtime using the <code>new</code> keyword. A class by itself consumes no heap memory "
    "-- only objects (instances) consume memory."
)

pn.section("Class Declaration Syntax")
pn.code_block(
    """
// General class syntax
[access_modifier] class ClassName [extends ParentClass] [implements Interface1, ...] {

    // 1. INSTANCE VARIABLES (Fields) -- state of the object
    [access_modifier] [static] [final] dataType fieldName [= initialValue];

    // 2. CONSTRUCTORS -- called when object is created with 'new'
    [access_modifier] ClassName([parameters]) {
        // initialization code
    }

    // 3. METHODS -- behavior of the object
    [access_modifier] [static] returnType methodName([parameters]) {
        // method body
        [return value;]
    }
}
""",
    lang="java",
)

pn.section("Simple Class Example -- Box")
pn.code_block(
    """
// Box.java -- a simple class with fields and methods
public class Box {

    // Instance variables (fields) -- each Box object has its own copy
    double width;
    double height;
    double depth;

    // Method: computes and returns the volume of the box
    double volume() {
        return width * height * depth;
    }

    // Method: displays box dimensions
    void display() {
        System.out.println("Width: " + width + ", Height: " + height + ", Depth: " + depth);
    }
}

// BoxDemo.java -- using the Box class
public class BoxDemo {
    public static void main(String[] args) {
        // 'box1' is a reference variable (stored on stack)
        // 'new Box()' creates the actual object on the heap
        Box box1 = new Box();

        // Accessing instance variables via dot (.) operator
        box1.width  = 10.0;
        box1.height = 5.0;
        box1.depth  = 2.5;

        // Calling methods via reference
        System.out.println("Volume = " + box1.volume()); // 125.0
        box1.display();

        // A second independent object -- has its own width, height, depth
        Box box2 = new Box();
        box2.width = 3.0; box2.height = 3.0; box2.depth = 3.0;
        System.out.println("Box2 Volume = " + box2.volume()); // 27.0
    }
}
""",
    lang="java",
)

pn.section("Access Specifiers")
pn.info_table(
    ["Modifier", "Same Class", "Same Package", "Subclass (Other Pkg)", "Other Package"],
    [
        ["private", "YES", "NO", "NO", "NO"],
        ["(default)", "YES", "YES", "NO", "NO"],
        ["protected", "YES", "YES", "YES", "NO"],
        ["public", "YES", "YES", "YES", "YES"],
    ],
)

pn.note(
    "The <b>default</b> (package-private) access is applied when no modifier is written. "
    "It allows access within the same package only. It is NOT the same as <code>public</code>."
)

pn.section("Memory Model: Stack vs Heap for Objects")

net_mem = pd.NetworkDiagram(
    width=pn.CW,
    height=200,
    theme=diag_theme,
    caption="Fig 2.1: Object memory layout -- reference variable on stack, object on heap",
)
net_mem.node(
    "stack",
    "STACK MEMORY\nbox1 (reference)\nbox2 (reference)",
    x=100,
    y=100,
    kind="storage",
)
net_mem.node(
    "heap1",
    "HEAP: Box Object 1\nwidth=10.0\nheight=5.0\ndepth=2.5",
    x=280,
    y=140,
    kind="database",
)
net_mem.node(
    "heap2",
    "HEAP: Box Object 2\nwidth=3.0\nheight=3.0\ndepth=3.0",
    x=280,
    y=60,
    kind="database",
)
net_mem.node(
    "method",
    "METHOD AREA\nBox.class bytecode\nvolume() method\ndisplay() method",
    x=460,
    y=100,
    kind="server",
)
net_mem.link("stack", "heap1", label="box1 points to")
net_mem.link("stack", "heap2", label="box2 points to")
net_mem.link("heap1", "method", label="shared class")
net_mem.link("heap2", "method", label="shared class")
pn.story.extend(net_mem.as_flowable())
pn.br()

# =============================================================================
#  2.2  CONSTRUCTORS
# =============================================================================
pn.chap_box("2.2  Constructors")
pn.section("What is a Constructor?")
pn.definition(
    "<b>Constructor:</b> A special method that is automatically called when an object is "
    "created using <code>new</code>. A constructor initializes the object's state. "
    "Rules: (1) Constructor name must EXACTLY match the class name. "
    "(2) Constructor has NO return type (not even void). "
    "(3) A class can have multiple constructors (constructor overloading). "
    "(4) If you define no constructor, Java provides a <b>default constructor</b> "
    "(no-argument, zero-initializes fields). Once you define any constructor, the default is no longer provided."
)

pn.section("Types of Constructors")
pn.info_table(
    ["Constructor Type", "Description", "When to Use"],
    [
        [
            "Default (no-arg)",
            "Takes no parameters. Assigns default values to fields.",
            "When all objects start with same initial state.",
        ],
        [
            "Parameterized",
            "Accepts arguments to initialize fields with specific values.",
            "When objects need different initial states at creation.",
        ],
        [
            "Copy Constructor",
            "Takes an object of the same class and copies its fields.",
            "To create a deep copy of an existing object (Java lacks built-in copy constructors unlike C++).",
        ],
    ],
)

pn.code_block(
    """
// ConstructorDemo.java
public class Student {

    String name;
    int rollNo;
    double marks;

    // ---- Default Constructor (no arguments) ----
    Student() {
        name   = "Unknown";
        rollNo = 0;
        marks  = 0.0;
        System.out.println("Default constructor called.");
    }

    // ---- Parameterized Constructor ----
    Student(String n, int r, double m) {
        name   = n;
        rollNo = r;
        marks  = m;
        System.out.println("Parameterized constructor called for: " + name);
    }

    // ---- Copy Constructor ----
    // Accepts an existing Student object and copies its fields
    Student(Student other) {
        this.name   = other.name;
        this.rollNo = other.rollNo;
        this.marks  = other.marks;
        System.out.println("Copy constructor called -- copied: " + name);
    }

    void display() {
        System.out.printf("Roll: %d | Name: %-15s | Marks: %.1f%n", rollNo, name, marks);
    }

    public static void main(String[] args) {
        Student s1 = new Student();                         // Default
        Student s2 = new Student("Arjun", 101, 88.5);      // Parameterized
        Student s3 = new Student(s2);                       // Copy of s2

        s1.display(); // Roll: 0  | Name: Unknown         | Marks: 0.0
        s2.display(); // Roll: 101| Name: Arjun           | Marks: 88.5
        s3.display(); // Roll: 101| Name: Arjun           | Marks: 88.5 (independent copy)

        // Modifying s3 does NOT affect s2 -- they are separate heap objects
        s3.marks = 95.0;
        s2.display(); // Still 88.5
        s3.display(); // Now 95.0
    }
}
""",
    lang="java",
)

pn.tip(
    "Constructor name = Class name. No return type. Called automatically by 'new'. "
    "Java auto-provides default constructor ONLY if you write ZERO constructors. "
    "Constructor overloading = same class, different parameter lists."
)
pn.br()

# =============================================================================
#  2.3  THE this KEYWORD
# =============================================================================
pn.chap_box("2.3  The this Keyword")
pn.section("Uses of this")
pn.definition(
    "<b>this:</b> A reference that always points to the <b>current object</b> -- the object "
    "on which the method or constructor is being invoked. It is implicitly passed to every "
    "instance method and constructor. Three primary uses: "
    "(1) Disambiguate local variables from instance variables when they share the same name. "
    "(2) Pass the current object as an argument to another method. "
    "(3) Call another constructor in the same class using <code>this()</code> -- must be the first statement."
)

pn.code_block(
    """
// ThisKeywordDemo.java
public class Employee {

    String name;
    int    empId;
    double salary;

    // USE 1: Disambiguate -- parameter 'name' shadows field 'name'
    // Without 'this', the assignment would be: name = name (no-op on itself)
    Employee(String name, int empId, double salary) {
        this.name   = name;    // this.name = instance field, name = local parameter
        this.empId  = empId;
        this.salary = salary;
    }

    // USE 2: Constructor chaining with this() -- avoids code duplication
    // This no-arg constructor delegates to the 3-arg constructor above
    Employee() {
        this("Anonymous", 0, 0.0); // MUST be the first statement in the constructor
        System.out.println("No-arg constructor (chained to parameterized).");
    }

    // USE 3: Return current object for method chaining (Builder-style pattern)
    Employee setSalary(double salary) {
        this.salary = salary;
        return this;              // returns the current Employee object
    }

    Employee setName(String name) {
        this.name = name;
        return this;
    }

    void display() {
        System.out.printf("ID: %d | Name: %-12s | Salary: %.2f%n", empId, name, salary);
    }

    public static void main(String[] args) {
        Employee e1 = new Employee("Priya", 201, 55000.0);
        e1.display();

        Employee e2 = new Employee();     // chains to 3-arg constructor
        e2.display();

        // Method chaining via returned 'this'
        new Employee("Ravi", 202, 0).setSalary(72000).setName("Ravi Kumar").display();
    }
}
""",
    lang="java",
)

pn.note(
    "<b>this() call rules:</b> It must be the FIRST statement in a constructor body. "
    "You cannot use both <code>this()</code> and <code>super()</code> in the same constructor "
    "since both require being the first statement."
)
pn.br()

# =============================================================================
#  2.4  METHOD OVERLOADING
# =============================================================================
pn.chap_box("2.4  Method Overloading")
pn.section("Compile-Time Polymorphism")
pn.definition(
    "<b>Method Overloading:</b> Defining multiple methods in the SAME class with the "
    "SAME name but DIFFERENT parameter lists (different number of parameters, or different "
    "parameter types, or different order of parameter types). The compiler selects the "
    "correct method at <b>compile time</b> -- hence called static (compile-time) polymorphism "
    "or <b>early binding</b>. Return type alone is NOT sufficient to differentiate overloaded methods."
)

pn.info_table(
    ["Rule", "Valid Overloading?", "Example"],
    [
        [
            "Different number of parameters",
            "YES -- valid",
            "add(int a) vs add(int a, int b)",
        ],
        [
            "Different parameter types",
            "YES -- valid",
            "add(int a, int b) vs add(double a, double b)",
        ],
        [
            "Different parameter ORDER",
            "YES -- valid",
            "show(int a, double b) vs show(double a, int b)",
        ],
        [
            "Only return type different",
            "NO -- compile error",
            "int get() vs double get()",
        ],
        [
            "Only access modifier different",
            "NO -- compile error",
            "public void m() vs private void m()",
        ],
    ],
)

pn.code_block(
    """
// OverloadDemo.java -- Arithmetic Calculator with overloaded add() methods
public class Calculator {

    // Version 1: add two integers
    int add(int a, int b) {
        System.out.println("int + int");
        return a + b;
    }

    // Version 2: add three integers
    int add(int a, int b, int c) {
        System.out.println("int + int + int");
        return a + b + c;
    }

    // Version 3: add two doubles
    double add(double a, double b) {
        System.out.println("double + double");
        return a + b;
    }

    // Version 4: add an int and a double (parameter ORDER matters for selection)
    double add(int a, double b) {
        System.out.println("int + double");
        return a + b;
    }

    // Version 5: add a double and an int (different order from Version 4)
    double add(double a, int b) {
        System.out.println("double + int");
        return a + b;
    }

    public static void main(String[] args) {
        Calculator c = new Calculator();

        System.out.println(c.add(10, 20));          // calls Version 1 -> 30
        System.out.println(c.add(1, 2, 3));         // calls Version 2 -> 6
        System.out.println(c.add(1.5, 2.5));        // calls Version 3 -> 4.0
        System.out.println(c.add(5, 2.5));          // calls Version 4 -> 7.5
        System.out.println(c.add(3.0, 4));          // calls Version 5 -> 7.0

        // TYPE PROMOTION in overloading:
        // When no exact match, Java WIDENS (promotes) the type automatically.
        // byte -> short -> int -> long -> float -> double
        byte b = 10;
        System.out.println(c.add(b, 20));  // byte promoted to int -> calls Version 1
    }
}
""",
    lang="java",
)

pn.section("Overloading Constructors")
pn.body(
    "Constructor overloading follows the same rules as method overloading. "
    "Different constructors are provided to allow creating objects in multiple ways -- "
    "this is extremely common in the Java standard library (e.g., <code>String</code>, "
    "<code>ArrayList</code>, <code>Scanner</code> all have multiple constructors)."
)
pn.br()

# =============================================================================
#  2.5  OBJECTS AS PARAMETERS & RETURNING OBJECTS
# =============================================================================
pn.chap_box("2.5  Using Objects as Parameters & Returning Objects")
pn.section("Pass by Reference (Objects)")
pn.definition(
    "<b>Java passes object references by value.</b> When you pass an object to a method, "
    "you pass a copy of the <i>reference</i> (memory address), NOT a copy of the object. "
    "This means the method CAN modify the object's fields through the reference. "
    "However, reassigning the reference inside the method does NOT affect the original reference "
    "in the caller -- only the object's contents can be modified."
)

pn.code_block(
    """
// ObjectParamDemo.java
public class Point {
    int x, y;

    Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    // Accepts another Point object as parameter
    // Computes the straight-line distance between this point and 'other'
    double distanceTo(Point other) {
        int dx = this.x - other.x;
        int dy = this.y - other.y;
        return Math.sqrt(dx * dx + dy * dy); // Math.sqrt returns double
    }

    // RETURNING AN OBJECT from a method
    // Creates and returns a new Point that is the midpoint of this and 'other'
    Point midpoint(Point other) {
        int mx = (this.x + other.x) / 2;
        int my = (this.y + other.y) / 2;
        return new Point(mx, my);  // heap allocation returned to caller
    }

    // Demonstrates that modifying object content DOES affect caller's object
    static void shiftRight(Point p, int amount) {
        p.x += amount;  // modifies heap object through the reference -- visible to caller
        // p = new Point(0, 0); // This would NOT affect caller -- only local reference changes
    }

    public static void main(String[] args) {
        Point p1 = new Point(0, 0);
        Point p2 = new Point(3, 4);

        System.out.println("Distance: " + p1.distanceTo(p2));  // 5.0

        Point mid = p1.midpoint(p2);
        System.out.println("Midpoint: (" + mid.x + ", " + mid.y + ")"); // (1, 2)

        System.out.println("p1.x before shift: " + p1.x); // 0
        shiftRight(p1, 10);
        System.out.println("p1.x after shift:  " + p1.x); // 10 (modified!)
    }
}
""",
    lang="java",
)
pn.br()

# =============================================================================
#  2.6  GARBAGE COLLECTION & finalize()
# =============================================================================
pn.chap_box("2.6  Garbage Collection & finalize()")
pn.section("Automatic Memory Management")
pn.definition(
    "<b>Garbage Collection:</b> Java's automatic memory reclamation mechanism. "
    "When an object has no more references pointing to it, it becomes <b>eligible for "
    "garbage collection</b>. The JVM's garbage collector (GC) runs in the background "
    "and reclaims the heap memory of unreferenced objects. The programmer never calls "
    "<code>free()</code> (as in C/C++) -- memory management is automatic."
)
pn.bullet(
    [
        "<b>When is an object eligible for GC?</b> When the reference variable holding it goes out of scope, is set to null, or is reassigned to another object.",
        "<b>System.gc():</b> A hint to the JVM to run garbage collection. Not guaranteed to run immediately -- the JVM may ignore it.",
        "<b>finalize() method:</b> Called by the GC <i>just before</i> reclaiming an object's memory. Used to release non-Java resources (file handles, DB connections). Deprecated in Java 9+ (unreliable -- GC may never call it). Prefer <code>try-with-resources</code> and <code>AutoCloseable</code> instead.",
    ]
)

pn.code_block(
    """
// GarbageCollectionDemo.java
public class ResourceHolder {

    String resourceName;

    ResourceHolder(String name) {
        this.resourceName = name;
        System.out.println("CREATED: " + resourceName);
    }

    // finalize() -- called by GC before reclaiming this object
    // @Override annotation confirms we are overriding Object.finalize()
    @Override
    protected void finalize() throws Throwable {
        System.out.println("FINALIZED (before GC): " + resourceName);
        super.finalize(); // always call super.finalize() in overriding code
    }

    public static void main(String[] args) throws InterruptedException {
        // Create objects
        ResourceHolder r1 = new ResourceHolder("Database Connection");
        ResourceHolder r2 = new ResourceHolder("File Handle");

        // Make r1 and r2 eligible for GC
        r1 = null;  // r1 no longer references the heap object
        r2 = null;  // r2 no longer references the heap object

        // Hint to JVM to perform GC (not guaranteed to run immediately)
        System.gc();

        // Wait briefly to allow GC thread to process (demo only -- NOT recommended in production)
        Thread.sleep(500);

        System.out.println("Main method finishing.");
    }
}

// ====================================================
// OBJECT LIFECYCLE (reference assignment and nulling)
// ====================================================
// Box b = new Box();   // b holds reference --> object alive
// b = null;            // reference removed --> object eligible for GC
// Box c = b;           // before null: c also points to same object
// // Both b and c must be null for GC eligibility
""",
    lang="java",
)

pn.section("Object Lifecycle Flowchart")
fc_gc = pd.Flowchart(
    width=pn.CW,
    height=320,
    theme=diag_theme,
    caption="Fig 2.2: Java Object Lifecycle -- from creation to garbage collection",
)
fc_gc.terminal("start", "START: new ClassName()")
fc_gc.process(
    "alloc", "JVM allocates heap memory; constructor runs; object initialized"
)
fc_gc.process("use", "Object used: methods called, fields accessed via reference")
fc_gc.decision("ref", "Any active reference pointing to the object?")
fc_gc.process("eligible", "Object marked eligible for Garbage Collection")
fc_gc.process("finalize", "GC calls finalize() (if overridden) before reclaiming")
fc_gc.process("reclaim", "JVM reclaims heap memory -- space returned to free pool")
fc_gc.terminal("end", "Object destroyed -- memory available for new allocations")

fc_gc.edge("start", "alloc")
fc_gc.edge("alloc", "use")
fc_gc.edge("use", "ref")
fc_gc.edge("ref", "use", branch="yes")
fc_gc.edge("ref", "eligible", branch="no")
fc_gc.edge("eligible", "finalize")
fc_gc.edge("finalize", "reclaim")
fc_gc.edge("reclaim", "end")
pn.story.extend(fc_gc.as_flowable())
pn.br()

# =============================================================================
#  2.7  ABSTRACT CLASSES
# =============================================================================
pn.chap_box("2.7  Abstract Classes")
pn.section("What is an Abstract Class?")
pn.definition(
    "<b>Abstract Class:</b> A class declared with the <code>abstract</code> keyword that "
    "cannot be instantiated directly (you cannot do <code>new AbstractClass()</code>). "
    "It serves as an <b>incomplete blueprint</b> -- it defines common state and behavior, "
    "and declares <b>abstract methods</b> (methods with no body/implementation) that "
    "subclasses MUST override. Abstract classes enable the Template Method design pattern."
)

pn.info_table(
    ["Property", "Abstract Class", "Concrete Class"],
    [
        ["Instantiation", "CANNOT be instantiated with new", "CAN be instantiated"],
        [
            "Abstract Methods",
            "CAN have abstract methods (body-less)",
            "CANNOT have abstract methods",
        ],
        [
            "Concrete Methods",
            "CAN have fully implemented methods",
            "All methods must be implemented",
        ],
        [
            "Constructors",
            "CAN have constructors (called via super())",
            "CAN have constructors",
        ],
        [
            "Inheritance",
            "Subclass MUST implement all abstract methods",
            "Normal inheritance",
        ],
        [
            "Fields",
            "CAN have instance variables and static fields",
            "CAN have all fields",
        ],
    ],
)

pn.body("<b>Part 1: The Abstract Base Class</b>")
pn.code_block(
    """
// Shape.java -- Abstract Base Class
abstract class Shape {
    String color;

    // Concrete constructor called by subclasses
    Shape(String color) {
        this.color = color;
    }

    // Abstract methods to be implemented by subclasses
    abstract double area();
    abstract double perimeter();

    // Concrete method shared by all shape subclasses
    void displayInfo() {
        System.out.printf("Shape: %-12s | Color: %-8s | Area: %8.2f | Perimeter: %8.2f%n",
                          getClass().getSimpleName(), color, area(), perimeter());
    }
}
""",
    lang="java",
)

pn.body("<b>Part 2: The Concrete Subclasses</b>")
pn.code_block(
    """
// Circle concrete subclass
class Circle extends Shape {
    double radius;

    Circle(String color, double radius) {
        super(color);
        this.radius = radius;
    }

    @Override
    double area() { return Math.PI * radius * radius; }

    @Override
    double perimeter() { return 2 * Math.PI * radius; }
}

// Rectangle concrete subclass
class Rectangle extends Shape {
    double length, width;

    Rectangle(String color, double length, double width) {
        super(color);
        this.length = length;
        this.width  = width;
    }

    @Override
    double area() { return length * width; }

    @Override
    double perimeter() { return 2 * (length + width); }
}

// Triangle concrete subclass
class Triangle extends Shape {
    double a, b, c;

    Triangle(String color, double a, double b, double c) {
        super(color);
        this.a = a; this.b = b; this.c = c;
    }

    @Override
    double area() {
        double s = (a + b + c) / 2.0;
        return Math.sqrt(s * (s-a) * (s-b) * (s-c));
    }

    @Override
    double perimeter() { return a + b + c; }
}
""",
    lang="java",
)

pn.body("<b>Part 3: The Driver Execution Class</b>")
pn.code_block(
    """
// AbstractClassDemo.java -- Main driver class
public class AbstractClassDemo {
    public static void main(String[] args) {
        // Polymorphic array referencing concrete objects
        Shape[] shapes = {
            new Circle("Red",    7.0),
            new Rectangle("Blue", 5.0, 3.0),
            new Triangle("Green", 3.0, 4.0, 5.0),
        };

        for (Shape s : shapes) {
            s.displayInfo(); // invokes dynamic method dispatch
        }
    }
}
""",
    lang="java",
)

pn.section("Abstract Class UML Diagram")
cd_abstract = pd.ClassDiagram(
    width=pn.CW,
    height=200,
    theme=diag_theme,
    caption="Fig 2.3: Abstract Shape hierarchy showing inheritance and method overriding",
    class_w=115,
)
cd_abstract.uml_class(
    "Shape",
    "Shape",
    stereotype="abstract",
    attributes=["# color: String"],
    methods=[
        "+ Shape(color)",
        "<<abstract>> + area(): double",
        "<<abstract>> + perimeter(): double",
        "+ displayInfo(): void",
    ],
)
cd_abstract.uml_class(
    "Circle",
    "Circle",
    attributes=["- radius: double"],
    methods=["+ area(): double", "+ perimeter(): double"],
)
cd_abstract.uml_class(
    "Rectangle",
    "Rectangle",
    attributes=["- length: double", "- width: double"],
    methods=["+ area(): double", "+ perimeter(): double"],
)
cd_abstract.uml_class(
    "Triangle",
    "Triangle",
    attributes=["- a,b,c: double"],
    methods=["+ area(): double", "+ perimeter(): double"],
)
cd_abstract.relate("Circle", "Shape", kind="inheritance")
cd_abstract.relate("Rectangle", "Shape", kind="inheritance")
cd_abstract.relate("Triangle", "Shape", kind="inheritance")
pn.story.extend(cd_abstract.as_flowable())
pn.br()

# =============================================================================
#  2.8  INHERITANCE
# =============================================================================
pn.chap_box("2.8  Inheritance")
pn.section("What is Inheritance?")
pn.definition(
    "<b>Inheritance:</b> A mechanism by which a new class (called <b>subclass</b>, "
    "child class, or derived class) acquires the properties (fields) and behaviors "
    "(methods) of an existing class (called <b>superclass</b>, parent class, or base class). "
    "Declared using the <code>extends</code> keyword. Java supports <b>single inheritance</b> "
    "only (one direct parent class), but supports <b>multilevel</b> and <b>hierarchical</b> "
    "inheritance. Multiple inheritance (two parents) is NOT supported in Java via classes "
    "(to avoid the diamond problem) but IS achievable via interfaces."
)

pn.info_table(
    ["Inheritance Type", "Description", "Java Support"],
    [
        ["Single", "One subclass extends one superclass.", "YES -- via extends"],
        [
            "Multilevel",
            "A extends B, B extends C (chain of inheritance).",
            "YES -- via extends chain",
        ],
        [
            "Hierarchical",
            "Multiple subclasses extend the same superclass.",
            "YES -- via extends",
        ],
        [
            "Multiple",
            "One subclass extends two or more superclasses.",
            "NO for classes; YES for interfaces via implements",
        ],
        [
            "Hybrid",
            "Combination of multiple and hierarchical.",
            "Partial -- through interfaces",
        ],
    ],
)

pn.section("The super Keyword and Method Overriding")
pn.body("<b>Part 1: The Base Superclass</b>")
pn.code_block(
    """
// Animal.java -- Base Superclass
class Animal {
    String name;
    int    age;

    // Superclass constructor
    Animal(String name, int age) {
        this.name = name;
        this.age  = age;
        System.out.println("Animal constructor: " + name);
    }

    void speak() {
        System.out.println(name + " makes a generic sound.");
    }

    void showInfo() {
        System.out.println("Name: " + name + " | Age: " + age);
    }
}
""",
    lang="java",
)

pn.body("<b>Part 2: The Inherited Subclasses</b>")
pn.code_block(
    """
// Dog subclass extending Animal
class Dog extends Animal {
    String breed;

    // Subclass constructor calls superclass constructor via super()
    Dog(String name, int age, String breed) {
        super(name, age);      // calls Animal(name, age)
        this.breed = breed;
        System.out.println("Dog constructor: " + breed);
    }

    // Overriding the speak() method
    @Override
    void speak() {
        System.out.println(name + " says: WOOF!");
    }

    // Call superclass method using super prefix
    void speakBoth() {
        super.speak();  // Animal's speak()
        this.speak();   // Dog's speak()
    }

    @Override
    void showInfo() {
        super.showInfo();      // invoke parent's implementation
        System.out.println("Breed: " + breed);
    }
}

// GuideDog multilevel subclass extending Dog
class GuideDog extends Dog {
    String owner;

    GuideDog(String name, int age, String breed, String owner) {
        super(name, age, breed);  // calls Dog(name, age, breed)
        this.owner = owner;
        System.out.println("GuideDog constructor: assigned to " + owner);
    }

    @Override
    void speak() {
        System.out.println(name + " (guide dog) says: quiet woof.");
    }
}
""",
    lang="java",
)

pn.body("<b>Part 3: The Driver Execution Class</b>")
pn.code_block(
    """
// InheritanceDemo.java -- Main driver execution class
public class InheritanceDemo {
    public static void main(String[] args) {
        // Constructor chaining execution: GuideDog -> Dog -> Animal
        GuideDog gd = new GuideDog("Buddy", 3, "Labrador", "Alice");
        gd.speak();      // invokes GuideDog's speak()
        gd.showInfo();   // invokes Dog's showInfo()

        System.out.println("---");
        // Polymorphism: parent reference holds subclass object
        Animal a = new Dog("Rex", 5, "Shepherd");
        a.speak(); // invokes Dog's speak() via dynamic method dispatch
    }
}
""",
    lang="java",
)

pn.section("Rules of Method Overriding")
pn.info_table(
    ["Rule", "Detail"],
    [
        [
            "Same Signature",
            "Method name, parameter list, and return type must be identical (covariant return type allowed since Java 5).",
        ],
        [
            "Access Cannot Narrow",
            "Overriding method access must be equal or MORE permissive (e.g., protected -> public is OK; public -> private is NOT).",
        ],
        [
            "Cannot Override static",
            "Static methods are hidden (shadowed), not overridden. Dynamic dispatch doesn't apply.",
        ],
        [
            "Cannot Override final",
            "A method declared final in the superclass cannot be overridden.",
        ],
        [
            "Cannot Override private",
            "Private methods are not visible to subclasses; they can be re-declared (not overriding).",
        ],
        [
            "Exceptions",
            "Cannot throw new checked exceptions not in parent; CAN throw unchecked (RuntimeException).",
        ],
    ],
)

pn.section("Inheritance Hierarchy Diagram")
cd_inherit = pd.ClassDiagram(
    width=pn.CW,
    height=230,
    theme=diag_theme,
    caption="Fig 2.4: Multilevel + Hierarchical inheritance -- Animal hierarchy",
    class_w=120,
)
cd_inherit.uml_class(
    "Animal",
    "Animal",
    attributes=["# name: String", "# age: int"],
    methods=["+ Animal(name, age)", "+ speak(): void", "+ showInfo(): void"],
)
cd_inherit.uml_class(
    "Dog",
    "Dog",
    attributes=["- breed: String"],
    methods=["+ Dog(name, age, breed)", "+ speak(): void", "+ showInfo(): void"],
)
cd_inherit.uml_class(
    "Cat",
    "Cat",
    attributes=["- indoor: boolean"],
    methods=["+ Cat(name, age, indoor)", "+ speak(): void"],
)
cd_inherit.uml_class(
    "GuideDog", "GuideDog", attributes=["- owner: String"], methods=["+ speak(): void"]
)
cd_inherit.relate("Dog", "Animal", kind="inheritance")
cd_inherit.relate("Cat", "Animal", kind="inheritance")
cd_inherit.relate("GuideDog", "Dog", kind="inheritance")
pn.story.extend(cd_inherit.as_flowable())
pn.br()

# =============================================================================
#  2.9  MULTILEVEL HIERARCHY & CONSTRUCTOR CHAINING
# =============================================================================
pn.chap_box("2.9  Multilevel Hierarchy & Constructor Chaining")
pn.section("Constructor Call Order in Inheritance")
pn.definition(
    "<b>Constructor Chaining:</b> In a class hierarchy, constructors are called from "
    "the TOP of the hierarchy (root superclass) DOWN to the most derived subclass. "
    "This ensures that parent class state is fully initialized before child class "
    "initialization adds or overrides state. Each constructor calls <code>super()</code> "
    "explicitly, or the compiler inserts an implicit <code>super()</code> call if none is written."
)

pn.code_block(
    """
// ConstructorChainDemo.java -- Constructor order in multilevel hierarchy
class A {
    int a;
    A(int a) {
        this.a = a;
        System.out.println("Constructor A: a=" + a);
    }
}

class B extends A {
    int b;
    B(int a, int b) {
        super(a);          // explicitly call A's constructor FIRST
        this.b = b;
        System.out.println("Constructor B: b=" + b);
    }
}

class C extends B {
    int c;
    C(int a, int b, int c) {
        super(a, b);       // call B's constructor, which calls A's
        this.c = c;
        System.out.println("Constructor C: c=" + c);
    }

    void show() {
        System.out.println("a=" + a + ", b=" + b + ", c=" + c);
    }
}

public class ConstructorChainDemo {
    public static void main(String[] args) {
        C obj = new C(1, 2, 3);
        // Output order:
        // Constructor A: a=1   (top of chain runs FIRST)
        // Constructor B: b=2
        // Constructor C: c=3   (bottom of chain runs LAST)
        obj.show();        // a=1, b=2, c=3
    }
}
""",
    lang="java",
)

pn.section("Constructor Chain Sequence Diagram")
seq_chain = pd.SequenceDiagram(
    width=pn.CW,
    height=260,
    theme=diag_theme,
    caption="Fig 2.5: Constructor chaining sequence in multilevel hierarchy A -> B -> C",
)
seq_chain.actor("main", "main()")
seq_chain.actor("C_ctor", "C(a,b,c)")
seq_chain.actor("B_ctor", "B(a,b)")
seq_chain.actor("A_ctor", "A(a)")
seq_chain.message("main", "C_ctor", "new C(1,2,3)", arrow="solid")
seq_chain.activate("C_ctor")
seq_chain.message("C_ctor", "B_ctor", "super(a, b)", arrow="solid")
seq_chain.activate("B_ctor")
seq_chain.message("B_ctor", "A_ctor", "super(a)", arrow="solid")
seq_chain.activate("A_ctor")
seq_chain.message("A_ctor", "B_ctor", "A initialized", arrow="dashed")
seq_chain.deactivate("A_ctor")
seq_chain.message("B_ctor", "C_ctor", "B initialized", arrow="dashed")
seq_chain.deactivate("B_ctor")
seq_chain.message("C_ctor", "main", "C initialized; object ready", arrow="dashed")
seq_chain.deactivate("C_ctor")
pn.story.extend(seq_chain.as_flowable())
pn.br()

# =============================================================================
#  2.10  PACKAGES
# =============================================================================
pn.chap_box("2.10  Packages & Import")
pn.section("What is a Package?")
pn.definition(
    "<b>Package:</b> A namespace that groups related classes and interfaces together. "
    "Packages serve two purposes: (1) <b>Namespace management</b> -- prevents naming conflicts "
    "between classes in different packages (e.g., <code>java.util.Date</code> vs "
    "<code>java.sql.Date</code>). "
    "(2) <b>Access control</b> -- package-private (default access) members are accessible "
    "only within the same package. "
    "Packages map to directory structures on the file system."
)

pn.info_table(
    ["Type", "Syntax", "Description"],
    [
        [
            "Package declaration",
            "package com.company.project;",
            "FIRST statement in .java file (before imports). Declares which package this class belongs to.",
        ],
        [
            "Single type import",
            "import java.util.ArrayList;",
            "Imports exactly one class from a package.",
        ],
        [
            "Wildcard import",
            "import java.util.*;",
            "Imports ALL public classes in the package (does NOT include sub-packages).",
        ],
        [
            "Static import",
            "import static java.lang.Math.*;",
            "Imports static members, allowing usage without class prefix (e.g., sqrt() instead of Math.sqrt()).",
        ],
        [
            "java.lang",
            "(automatic)",
            "The java.lang package (String, Math, System, Object, Thread...) is imported automatically in every Java file.",
        ],
    ],
)

pn.code_block(
    """
// File: com/shapes/Circle.java
package com.shapes;         // MUST be first non-comment statement

public class Circle {
    private double radius;

    public Circle(double radius) { this.radius = radius; }

    public double area() { return Math.PI * radius * radius; }

    // toString() is overriding Object.toString() -- auto-called in string contexts
    @Override
    public String toString() {
        return "Circle[radius=" + radius + "]";
    }
}

// ================================================================
// File: com/main/Main.java
package com.main;

// Fully-qualified import to avoid ambiguity
import com.shapes.Circle;
import static java.lang.Math.PI;   // static import -- can use PI directly

public class Main {
    public static void main(String[] args) {
        Circle c = new Circle(5.0);
        System.out.println(c);              // calls c.toString() automatically
        System.out.println("Area = " + c.area());
        System.out.println("PI value: " + PI); // static import -- no Math. prefix
    }
}

// ================================================================
// COMPILING AND RUNNING WITH PACKAGES (command line):
//   javac -d . com/shapes/Circle.java      // compile; -d . places .class in correct dir
//   javac -d . com/main/Main.java
//   java com.main.Main                     // fully qualified class name to run
""",
    lang="java",
)

pn.section("Key Standard Packages")
pn.info_table(
    ["Package", "Contents (selected)"],
    [
        [
            "java.lang",
            "String, Math, System, Object, Thread, Runnable, Integer, Exception (auto-imported)",
        ],
        [
            "java.util",
            "ArrayList, LinkedList, HashMap, HashSet, Scanner, Date, Arrays, Collections",
        ],
        [
            "java.io",
            "File, FileInputStream, FileOutputStream, BufferedReader, PrintWriter, Serializable",
        ],
        ["java.net", "Socket, ServerSocket, URL, HttpURLConnection"],
        [
            "java.sql",
            "Connection, Statement, PreparedStatement, ResultSet, DriverManager",
        ],
        ["javax.swing", "JFrame, JPanel, JButton, JLabel, JTextField, JTable"],
        [
            "java.awt",
            "Frame, Panel, Button, Color, Graphics, Font, FlowLayout, GridLayout",
        ],
    ],
)
pn.br()

# =============================================================================
#  2.11  INTERFACES
# =============================================================================
pn.chap_box("2.11  Interfaces")
pn.section("What is an Interface?")
pn.definition(
    "<b>Interface:</b> A completely abstract type (prior to Java 8) that declares a set "
    "of methods a class MUST implement. Interfaces define a <b>contract</b> -- any class "
    "that implements the interface must provide concrete bodies for all its abstract methods. "
    "Since Java 8, interfaces can also contain <code>default</code> (with body) and "
    "<code>static</code> methods. Since Java 9, they can contain <code>private</code> methods. "
    "A class implements an interface using the <code>implements</code> keyword. "
    "A class can implement MULTIPLE interfaces (solving the multiple inheritance limitation)."
)

pn.info_table(
    ["Feature", "Abstract Class", "Interface"],
    [
        ["Keyword", "abstract class", "interface"],
        ["Implements keyword", "extends (subclass)", "implements (any class)"],
        [
            "Multiple inheritance",
            "NO (single extends only)",
            "YES (implements Interface1, Interface2)",
        ],
        ["Constructors", "YES", "NO"],
        [
            "Instance variables",
            "YES (any access modifier)",
            "NO (only public static final constants)",
        ],
        [
            "Method implementation",
            "YES (can have concrete methods)",
            "YES since Java 8 (default, static methods)",
        ],
        ["Access of methods", "Any modifier", "Always public (even if not stated)"],
        [
            "Use when",
            "Related classes share common code",
            "Unrelated classes need to share behavior",
        ],
    ],
)

pn.body("<b>Part 1: The Interface Contracts</b>")
pn.code_block(
    """
// Printable.java and Saveable.java -- Interface contracts
interface Printable {
    // Implicitly public abstract method
    void print();

    // Default method (Java 8+) providing utility implementation
    default void printBorder() {
        System.out.println("==============================================");
    }

    // Static method (Java 8+) callable on interface name directly
    static void help() {
        System.out.println("Printable: implement print() to show content.");
    }
}

interface Saveable {
    void save(String filename);
    void load(String filename);
}
""",
    lang="java",
)

pn.body("<b>Part 2: Implementing the Interfaces</b>")
pn.code_block(
    """
// DocumentReport implements Printable and Saveable (multiple inheritance of behavior)
class DocumentReport implements Printable, Saveable {
    String content;

    DocumentReport(String content) {
        this.content = content;
    }

    // Must override and implement all abstract methods from interfaces
    @Override
    public void print() {
        printBorder();                          // invoke default implementation
        System.out.println("DOCUMENT: " + content);
        printBorder();
    }

    @Override
    public void save(String filename) {
        System.out.println("Saving to: " + filename);
    }

    @Override
    public void load(String filename) {
        System.out.println("Loading from: " + filename);
    }
}
""",
    lang="java",
)

pn.body("<b>Part 3: The Driver Execution Class</b>")
pn.code_block(
    """
// InterfaceDemo.java -- Main driver execution class
public class InterfaceDemo {
    public static void main(String[] args) {
        DocumentReport doc = new DocumentReport("Annual Report Q4 2026");
        doc.print();
        doc.save("report_q4.pdf");

        // Interface reference holding class object (polymorphism)
        Printable p = doc;
        p.print();

        Printable.help();   // invoke static interface method
    }
}
""",
    lang="java",
)

pn.section("Interface vs Abstract Class UML")
cd_iface = pd.ClassDiagram(
    width=pn.CW,
    height=210,
    theme=diag_theme,
    caption="Fig 2.6: Interface implementation -- class implements multiple interfaces",
    class_w=120,
)
cd_iface.uml_class(
    "Printable",
    "Printable",
    stereotype="interface",
    methods=["+ print(): void", "default printBorder(): void"],
)
cd_iface.uml_class(
    "Saveable",
    "Saveable",
    stereotype="interface",
    methods=["+ save(f): void", "+ load(f): void"],
)
cd_iface.uml_class(
    "DocumentReport",
    "DocumentReport",
    attributes=["- content: String"],
    methods=["+ print(): void", "+ save(f): void", "+ load(f): void"],
)
cd_iface.relate("DocumentReport", "Printable", kind="realization")
cd_iface.relate("DocumentReport", "Saveable", kind="realization")
pn.story.extend(cd_iface.as_flowable())
pn.br()

# =============================================================================
#  2.12  EXCEPTION HANDLING
# =============================================================================
pn.chap_box("2.12  Exception Handling")
pn.section("What is an Exception?")
pn.definition(
    "<b>Exception:</b> An event that disrupts the normal flow of a program's execution. "
    "When an error occurs inside a method, the JVM creates an exception object containing "
    "information about the error (type, message, stack trace) and <b>throws</b> it. "
    "If the exception is not caught, it propagates up the call stack and eventually "
    "terminates the program. Java exception handling uses five keywords: "
    "<code>try</code>, <code>catch</code>, <code>finally</code>, <code>throw</code>, <code>throws</code>."
)

pn.section("Exception Hierarchy")
cd_exc = pd.ClassDiagram(
    width=pn.CW,
    height=240,
    theme=diag_theme,
    caption="Fig 2.7: Java Exception class hierarchy",
    class_w=130,
)
cd_exc.uml_class(
    "Throwable",
    "Throwable",
    stereotype="class",
    methods=["+ getMessage()", "+ printStackTrace()"],
)
cd_exc.uml_class(
    "Error",
    "Error",
    stereotype="class",
    methods=["-- JVM errors --", "OutOfMemoryError", "StackOverflowError"],
)
cd_exc.uml_class(
    "Exception", "Exception", stereotype="class", methods=["-- Base of all checked"]
)
cd_exc.uml_class(
    "RuntimeException",
    "RuntimeException",
    stereotype="class",
    methods=["-- Unchecked exceptions"],
)
cd_exc.uml_class(
    "Checked",
    "IOException\nSQLException\nFileNotFoundException",
    stereotype="class",
    methods=[],
)
cd_exc.uml_class(
    "Unchecked",
    "NullPointerException\nArrayIndexOutOfBounds\nArithmeticException",
    stereotype="class",
    methods=[],
)
cd_exc.relate("Error", "Throwable", kind="inheritance")
cd_exc.relate("Exception", "Throwable", kind="inheritance")
cd_exc.relate("RuntimeException", "Exception", kind="inheritance")
cd_exc.relate("Checked", "Exception", kind="inheritance")
cd_exc.relate("Unchecked", "RuntimeException", kind="inheritance")
pn.story.extend(cd_exc.as_flowable())

pn.section("Checked vs Unchecked Exceptions")
pn.info_table(
    ["Feature", "Checked Exceptions", "Unchecked (Runtime) Exceptions"],
    [
        [
            "Inheritance",
            "Extend Exception (not RuntimeException)",
            "Extend RuntimeException",
        ],
        [
            "Compiler enforcement",
            "MUST be caught or declared with throws",
            "Optional -- compiler does NOT require handling",
        ],
        [
            "When they occur",
            "External failures: file not found, network down, DB error",
            "Programming bugs: null pointer, wrong index, divide by zero",
        ],
        [
            "Examples",
            "IOException, SQLException, FileNotFoundException, ClassNotFoundException",
            "NullPointerException, ArrayIndexOutOfBoundsException, ArithmeticException, ClassCastException",
        ],
        [
            "Best practice",
            "Catch and recover, or propagate with throws",
            "Fix the code bug rather than catching",
        ],
    ],
)

pn.body("<b>Part 1: Custom Exception & Domain Logic</b>")
pn.code_block(
    """
// BankAccount.java -- Custom exception and class declaration
class InsufficientFundsException extends Exception {
    double amount;

    InsufficientFundsException(double amount) {
        super("Insufficient funds: need " + amount + " more.");
        this.amount = amount;
    }
}

class BankAccount {
    private String owner;
    private double balance;

    BankAccount(String owner, double balance) {
        this.owner   = owner;
        this.balance = balance;
    }

    // Method throws checked exception -- callers must handle or propagate
    void withdraw(double amount) throws InsufficientFundsException {
        if (amount <= 0) {
            throw new IllegalArgumentException("Withdrawal amount must be positive.");
        }
        if (amount > balance) {
            throw new InsufficientFundsException(amount - balance);
        }
        balance -= amount;
        System.out.printf("%s withdrew: %.2f | New balance: %.2f%n", owner, amount, balance);
    }

    double getBalance() { return balance; }
}
""",
    lang="java",
)

pn.body("<b>Part 2: Basic Exception Handling (try-catch-finally)</b>")
pn.code_block(
    """
// TryCatchFinallyDemo.java -- Demo try-catch-finally
public class TryCatchFinallyDemo {
    public static void main(String[] args) {
        BankAccount acc = new BankAccount("Rahul", 5000.0);

        try {
            acc.withdraw(1000.0);  // succeeds
            acc.withdraw(8000.0);  // throws checked exception
            System.out.println("This line is NEVER reached.");

        } catch (InsufficientFundsException e) {
            System.out.println("CAUGHT: " + e.getMessage());
            System.out.println("Shortfall: " + e.amount);

        } catch (IllegalArgumentException e) {
            System.out.println("Bad input: " + e.getMessage());

        } finally {
            // Always executes -- ideal for resource/state cleanup
            System.out.println("FINALLY: Balance = " + acc.getBalance());
        }
    }
}
""",
    lang="java",
)

pn.body("<b>Part 3: Multi-Catch and Try-With-Resources (Java 7+)</b>")
pn.code_block(
    """
// ExceptionFeaturesDemo.java -- Multi-catch & Try-with-resources
import java.io.*;

public class ExceptionFeaturesDemo {
    public static void main(String[] args) {
        // 1. Multi-catch (pipe symbol syntax)
        try {
            int[] arr = {1, 2, 3};
            System.out.println(arr[5]);       // ArrayIndexOutOfBoundsException
        } catch (ArrayIndexOutOfBoundsException | NullPointerException e) {
            System.out.println("Multi-catch: " + e.getClass().getSimpleName());
        }

        // 2. Try-with-resources: automatically closes resources
        try (BufferedReader br = new BufferedReader(new StringReader("line1\\nline2"))) {
            System.out.println(br.readLine()); // line1
        } catch (IOException e) {
            System.out.println("IO Error: " + e.getMessage());
        }
    }
}
""",
    lang="java",
)

pn.section("Exception Propagation Flow")
fc_exc = pd.Flowchart(
    width=pn.CW,
    height=310,
    theme=diag_theme,
    caption="Fig 2.8: Exception propagation and catch block selection",
)
fc_exc.terminal("start", "Method throws exception", x=150, y=450)
fc_exc.decision("try", "Is throwing code inside a try block?", x=150, y=370)
fc_exc.decision("catch", "Does a matching catch block exist?", x=150, y=280)
fc_exc.process("handle", "Execute matching catch block; handle exception", x=80, y=190)
fc_exc.process("finally_r", "Execute finally block (if any)", x=150, y=100)
fc_exc.terminal("resume", "Program continues after try-catch-finally", x=150, y=20)
fc_exc.process(
    "propagate", "Unwind stack: exception passes to calling method", x=360, y=370
)
fc_exc.decision("caller", "Does calling method have matching catch?", x=360, y=280)
fc_exc.process(
    "jvm", "JVM catches it: print stack trace; terminate thread", x=360, y=190
)

fc_exc.edge("start", "try")
fc_exc.edge("try", "catch", branch="yes")
fc_exc.edge("try", "propagate", branch="no")
fc_exc.edge("catch", "handle", branch="yes")
fc_exc.edge("catch", "finally_r", branch="no")
fc_exc.edge("handle", "finally_r")
fc_exc.edge("finally_r", "resume")
fc_exc.edge("propagate", "caller")
fc_exc.edge("caller", "handle", branch="yes")
fc_exc.edge("caller", "jvm", branch="no")
pn.story.extend(fc_exc.as_flowable())

pn.tip(
    "try: wraps risky code. catch: handles specific exception types. "
    "finally: ALWAYS runs (cleanup). throw: manually throw an exception. "
    "throws: declares that a method may propagate a checked exception. "
    "Unchecked (RuntimeException) need not be declared or caught."
)
pn.br()

# =============================================================================
#  2.13  MULTITHREADING
# =============================================================================
pn.chap_box("2.13  Multithreading")
pn.section("What is a Thread?")
pn.definition(
    "<b>Thread:</b> The smallest unit of execution within a process. A Java program "
    "starts with one thread -- the <b>main thread</b> -- which runs the <code>main()</code> "
    "method. Creating additional threads allows the program to perform concurrent tasks. "
    "<b>Multithreading</b> is executing multiple threads simultaneously within one process, "
    "sharing the same process memory. Java has built-in thread support via the "
    "<code>java.lang.Thread</code> class and the <code>java.lang.Runnable</code> interface."
)

pn.section("Two Ways to Create a Thread")
pn.info_table(
    ["Method", "How", "When to Use", "Limitation"],
    [
        [
            "Extend Thread",
            "class MyThread extends Thread { public void run(){...} }",
            "Simple threads with no other inheritance needed.",
            "Cannot extend any other class (Java has single inheritance).",
        ],
        [
            "Implement Runnable",
            "class MyTask implements Runnable { public void run(){...} }",
            "When class already extends another class, or for better OOP design.",
            "More verbose -- must wrap in Thread: new Thread(task).start()",
        ],
    ],
)

pn.body("<b>Method 1: Extending the Thread Class</b>")
pn.code_block(
    """
// CounterThread.java -- Extending Thread class
class CounterThread extends Thread {
    private String threadName;
    private int start, end;

    CounterThread(String name, int start, int end) {
        super(name);            // sets the thread's name
        this.threadName = name;
        this.start = start;
        this.end   = end;
    }

    // run() contains code to execute in the new thread
    @Override
    public void run() {
        for (int i = start; i <= end; i++) {
            System.out.printf("[Thread: %-12s] count = %d%n", threadName, i);
            try {
                Thread.sleep(100); // pause 100ms
            } catch (InterruptedException e) {
                System.out.println(threadName + " was interrupted.");
                Thread.currentThread().interrupt(); // restore interrupt status
            }
        }
    }
}
""",
    lang="java",
)

pn.body("<b>Method 2: Implementing the Runnable Interface (Preferred)</b>")
pn.code_block(
    """
// PrintTask.java -- Implementing Runnable interface
class PrintTask implements Runnable {
    private String message;
    private int repetitions;

    PrintTask(String message, int reps) {
        this.message    = message;
        this.repetitions = reps;
    }

    @Override
    public void run() {
        for (int i = 1; i <= repetitions; i++) {
            System.out.printf("[Runnable] %s -- iteration %d%n", message, i);
            try { 
                Thread.sleep(150); 
            } catch (InterruptedException e) { 
                Thread.currentThread().interrupt(); 
            }
        }
    }
}
""",
    lang="java",
)

pn.body("<b>Driver Execution: Starting and Joining Threads</b>")
pn.code_block(
    """
// MultithreadingDemo.java -- Driver class
public class MultithreadingDemo {
    public static void main(String[] args) throws InterruptedException {
        System.out.println("Main thread starting.");

        // Instantiate thread objects (Method 1)
        CounterThread t1 = new CounterThread("Alpha", 1, 5);
        CounterThread t2 = new CounterThread("Beta",  1, 5);

        // Instantiate runnable task wrapped in a Thread (Method 2)
        Thread t3 = new Thread(new PrintTask("Hello from Runnable", 4), "Gamma");

        // start() creates a new OS-level execution thread and invokes run()
        t1.start();
        t2.start();
        t3.start();

        // join() blocks caller (main) thread until target thread completes
        t1.join();
        t2.join();
        t3.join();

        System.out.println("Main thread finished. All threads joined.");
    }
}
""",
    lang="java",
)

pn.section("Thread Lifecycle")

sm_thread = pd.StateMachine(
    width=pn.CW,
    height=240,
    theme=diag_theme,
    caption="Fig 2.9: Java Thread State Lifecycle",
)
sm_thread.state("new", "NEW", initial=True)
sm_thread.state("runnable", "RUNNABLE")
sm_thread.state("running", "RUNNING")
sm_thread.state("blocked", "BLOCKED /\nWAITING /\nTIMED_WAIT")
sm_thread.state("dead", "TERMINATED", accepting=True)

sm_thread.transition("new", "runnable", label="start()", pill=True)
sm_thread.transition("runnable", "running", label="scheduler picks\nthread", pill=True)
sm_thread.transition(
    "running", "runnable", label="yield() /\ntime slice over", pill=True
)
sm_thread.transition("running", "blocked", label="sleep() / wait() /\nI/O", pill=True)
sm_thread.transition(
    "blocked", "runnable", label="sleep ends /\nnotify() /\nI/O done", pill=True
)
sm_thread.transition("running", "dead", label="run() returns /\nexception", pill=True)
pn.story.extend(sm_thread.as_flowable())

pn.section("Synchronization -- Preventing Race Conditions")
pn.definition(
    "<b>Race Condition:</b> When two or more threads access shared data simultaneously and "
    "at least one of them modifies it, the result depends on the unpredictable order of "
    "thread execution. This leads to <b>data inconsistency</b>. "
    "<b>Synchronization</b> uses the <code>synchronized</code> keyword to create a "
    "<b>monitor lock (mutex)</b>: only one thread can execute a synchronized method or "
    "block on the same object at a time. Other threads must wait until the lock is released."
)

pn.body("<b>Part 1: Shared Resource with Synchronized Methods</b>")
pn.code_block(
    """
// BankAccount.java -- Shared account structure showing lock synchronization
class BankAccount {
    private double balance;
    private String name;

    BankAccount(String name, double balance) {
        this.name = name;
        this.balance = balance;
    }

    // UNSAFE: race condition possible without synchronization
    void unsafeDeposit(double amount) {
        double temp = balance;  // read current balance
        temp += amount;         // add amount locally
        balance = temp;         // write back
    }

    // SAFE: synchronized keyword locks access on the 'this' object
    synchronized void deposit(double amount) {
        balance += amount;   // atomic write relative to other threads
        System.out.printf("[%s] Deposited %.2f | Balance: %.2f%n", name, amount, balance);
    }

    synchronized void withdraw(double amount) {
        if (balance >= amount) {
            balance -= amount;
            System.out.printf("[%s] Withdrew  %.2f | Balance: %.2f%n", name, amount, balance);
        } else {
            System.out.printf("[%s] Insufficient funds (requested %.2f, have %.2f)%n",
                               name, amount, balance);
        }
    }

    synchronized double getBalance() { return balance; }
}
""",
    lang="java",
)

pn.body("<b>Part 2: Multi-Thread Access Driver Class</b>")
pn.code_block(
    """
// SynchronizationDemo.java -- Runnable thread task and driver execution
class DepositThread implements Runnable {
    BankAccount account;
    double amount;
    int times;

    DepositThread(BankAccount acc, double amt, int n) {
        account = acc; amount = amt; times = n;
    }

    @Override
    public void run() {
        for (int i = 0; i < times; i++) {
            account.deposit(amount);
        }
    }
}

public class SynchronizationDemo {
    public static void main(String[] args) throws InterruptedException {
        BankAccount sharedAccount = new BankAccount("Shared", 0.0);

        // Threads competing for the lock of the shared bank account instance
        Thread t1 = new Thread(new DepositThread(sharedAccount, 100.0, 5), "T1");
        Thread t2 = new Thread(new DepositThread(sharedAccount, 200.0, 5), "T2");

        t1.start(); t2.start();
        t1.join();  t2.join();

        System.out.println("Final Balance: " + sharedAccount.getBalance());
    }
}
""",
    lang="java",
)

pn.section("Inter-Thread Communication: wait() and notify()")
pn.definition(
    "<b>Inter-thread Communication:</b> Allows threads to coordinate execution. "
    "Three methods defined in <code>Object</code> (not Thread) and usable only inside "
    "synchronized blocks: "
    "<code>wait()</code> -- releases the lock and suspends the calling thread until another thread "
    "calls <code>notify()</code> or <code>notifyAll()</code> on the same object. "
    "<code>notify()</code> -- wakes up ONE thread waiting on this object's monitor. "
    "<code>notifyAll()</code> -- wakes ALL threads waiting on this object's monitor."
)

pn.code_block(
    """
// ProducerConsumerDemo.java -- Classic inter-thread communication pattern
class SharedBuffer {
    private int data = -1;
    private boolean produced = false;   // flag: is data ready for consumer?

    // Producer calls this -- generates data and notifies consumer
    synchronized void produce(int value) throws InterruptedException {
        while (produced) {
            wait(); // wait until consumer has consumed the previous item
        }
        this.data = value;
        produced = true;
        System.out.println("PRODUCED: " + value);
        notify(); // wake up the consumer thread
    }

    // Consumer calls this -- waits for data, then consumes it
    synchronized int consume() throws InterruptedException {
        while (!produced) {
            wait(); // wait until producer has put something in
        }
        produced = false;
        System.out.println("CONSUMED: " + data);
        notify(); // wake up the producer thread
        return data;
    }
}

public class ProducerConsumerDemo {
    public static void main(String[] args) {
        SharedBuffer buffer = new SharedBuffer();

        Thread producer = new Thread(() -> {
            try {
                for (int i = 1; i <= 5; i++) {
                    buffer.produce(i);
                    Thread.sleep(50);
                }
            } catch (InterruptedException e) { Thread.currentThread().interrupt(); }
        }, "Producer");

        Thread consumer = new Thread(() -> {
            try {
                for (int i = 1; i <= 5; i++) {
                    buffer.consume();
                    Thread.sleep(100);
                }
            } catch (InterruptedException e) { Thread.currentThread().interrupt(); }
        }, "Consumer");

        producer.start();
        consumer.start();
    }
}
""",
    lang="java",
)

pn.section("Thread Priority and Daemon Threads")
pn.info_table(
    ["Concept", "Description", "API"],
    [
        [
            "Thread Priority",
            "Hints to scheduler about relative importance. Range 1 (MIN_PRIORITY) to 10 (MAX_PRIORITY). Default = 5 (NORM_PRIORITY). Higher priority runs more often but not guaranteed.",
            "thread.setPriority(Thread.MAX_PRIORITY)",
        ],
        [
            "Daemon Thread",
            "Background service thread (e.g., GC). JVM exits when ONLY daemon threads are left -- does not wait for daemons to finish. Must be set BEFORE start().",
            "thread.setDaemon(true); thread.start();",
        ],
        [
            "Thread Name",
            "Each thread has a name (default Thread-0, Thread-1...). Useful for debugging.",
            'thread.setName("WorkerThread")',
        ],
        ["Thread ID", "Unique long identifier assigned by JVM.", "thread.getId()"],
        [
            "Current Thread",
            "Get reference to currently executing thread.",
            "Thread.currentThread()",
        ],
    ],
)
pn.br()

# =============================================================================
#  QUICK REVISION SUMMARY
# =============================================================================
pn.chap_box("Unit II -- Quick Revision Exam Flashcards")
pn.section("Key Points by Topic")

pn.highlight(
    "<b>Q: What is the difference between method overloading and method overriding?</b><br/>"
    "A: Overloading: same class, same name, different parameters -- resolved at compile time (static polymorphism). "
    "Overriding: subclass redefines parent's method with identical signature -- resolved at runtime (dynamic polymorphism)."
)
pn.highlight(
    "<b>Q: What is the role of the super keyword?</b><br/>"
    "A: Two uses: (1) <code>super.method()</code> -- calls the overridden method from the parent class. "
    "(2) <code>super(args)</code> -- calls the parent class constructor. super() must be the first statement "
    "in a constructor."
)
pn.highlight(
    "<b>Q: What is the difference between an abstract class and an interface?</b><br/>"
    "A: Abstract class can have instance variables, constructors, and concrete methods; "
    "only single inheritance. Interface has only constants and abstract methods (prior Java 8); "
    "a class can implement multiple interfaces."
)
pn.highlight(
    "<b>Q: Checked vs unchecked exceptions?</b><br/>"
    "A: Checked (IOException, SQLException) must be caught or declared -- compiler enforces. "
    "Unchecked (NullPointerException, ArrayIndexOutOfBoundsException) are programming bugs -- "
    "compiler does not require handling. Both extend Throwable via Exception."
)
pn.highlight(
    "<b>Q: What happens if you call run() instead of start()?</b><br/>"
    "A: Calling run() directly executes the run() body in the CURRENT thread -- no new thread is created. "
    "Only start() creates a new OS thread and invokes run() concurrently."
)
pn.highlight(
    "<b>Q: What is synchronization and why is it needed?</b><br/>"
    "A: When multiple threads access shared mutable data, a race condition can produce inconsistent results. "
    "Synchronized methods/blocks use a mutex (monitor lock) so only one thread executes them at a time on a given object, "
    "ensuring thread safety."
)
pn.highlight(
    "<b>Q: What does finally always do?</b><br/>"
    "A: The finally block ALWAYS executes -- whether an exception is thrown or not, "
    "whether it is caught or not. The only exception: System.exit() or JVM crash. "
    "Used for mandatory cleanup (close files, DB connections, release locks)."
)

pn.section("Unit II Exam Blueprint")
pn.info_table(
    ["Marks", "Expected Questions"],
    [
        [
            "2 marks",
            "Define constructor. What is this keyword? Difference between interface and abstract class. What is synchronization?",
        ],
        [
            "5 marks",
            "Explain constructor overloading with example. Explain method overriding vs overloading. Explain exception hierarchy. Explain thread lifecycle with diagram.",
        ],
        [
            "10 marks",
            "Explain inheritance with multilevel example and UML diagram. Explain exception handling (try-catch-finally-throw-throws) with code. Explain multithreading with producer-consumer example. Explain abstract class vs interface with code and diagram.",
        ],
    ],
)

pn.note(
    "Practice writing: (1) a full inheritance chain with super, (2) a try-catch-finally with custom exception, "
    "(3) a thread using Runnable with synchronized method. These are the most frequently asked 10-mark questions."
)

# =============================================================================
#  BUILD DOCUMENT
# =============================================================================
pn.build_doc("Java_Unit2_Notes.pdf")
print("Generated: Java_Unit2_Notes.pdf")
