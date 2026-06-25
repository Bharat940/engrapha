"""
Java Programming (IT408) -- Unit IV Notes
UIT-RGPV (Autonomous) Bhopal | Semester IV
Complete exam notes: AWT, Frame Windows, Controls, Layout Managers, Swing, Servlet.
Run: python java_unit4_notes.py
Output: Java_Unit4_Notes.pdf
"""

from __future__ import annotations

import paperforge_notes as pn
import paperforge_diagrams as pd

# =============================================================================
#  THEME & GLOBAL FOOTER SETUP
#  Using SUNSET_DARK -- warm orange accent on deep midnight-purple background
#  Distinct from Unit I (Catppuccin Mocha), II (Midnight Dark), III (Forest Dark)
# =============================================================================
pn.set_story([])
pn.set_theme(pn.SUNSET_DARK)

pn.set_global_footer(
    left="Java Programming (IT408) -- Unit IV",
    right="UIT-RGPV (Autonomous) Bhopal",
    show_page_num=True,
)

# Sync diagram theme with active notes theme
diag_theme = pd.DiagramTheme.from_notes_theme(pn.get_theme())

# =============================================================================
#  COVER PAGE
# =============================================================================
pn.bookmark("Cover Page")
pn.suppress_footer(page_only=True)
pn.sp(26)

pn.cover_card(
    "JAVA PROGRAMMING",
    "Unit IV -- AWT, GUI Controls, Layout Managers, Swing & Servlet",
)
pn.cover_subtitle(
    [
        "Subject Code: IT408  |  UIT-RGPV (Autonomous) Bhopal  |  Semester IV",
        "Complete Exam Notes: AWT Hierarchy, Frame, Controls, Layouts, Menus,",
        "Introduction to Swing Components and Java Servlets with Code Examples",
    ]
)
pn.sp(10)
pn.rule(pn.get_theme().rl(pn.get_theme().accent), 1.5)
pn.sp(8)

pn.info_table(
    ["Section", "Syllabus Topics Covered"],
    [
        [
            "4.1 Introducing the AWT",
            "What is AWT, java.awt package, AWT vs Swing, component hierarchy",
        ],
        [
            "4.2 AWT Class Hierarchy",
            "Component, Container, Window, Panel, Frame -- roles and hierarchy",
        ],
        [
            "4.3 Window Fundamentals",
            "Component, Container, Panel, Frame class details and relationships",
        ],
        [
            "4.4 Working with Frame Windows",
            "Creating frames, setSize, setVisible, WindowListener, close handling",
        ],
        [
            "4.5 Graphics and Text in AWT",
            "Graphics class in Frame, drawString, drawRect, setFont, setColor",
        ],
        [
            "4.6 Handling Events in a Frame",
            "ActionListener, WindowAdapter, inner class, anonymous class",
        ],
        [
            "4.7 AWT Controls",
            "Button, Label, TextField, TextArea, Checkbox, CheckboxGroup, Choice, List, Scrollbar",
        ],
        [
            "4.8 Layout Managers",
            "FlowLayout, BorderLayout, GridLayout, CardLayout, GridBagLayout overview",
        ],
        [
            "4.9 Menus in AWT",
            "MenuBar, Menu, MenuItem, CheckboxMenuItem, PopupMenu, event handling",
        ],
        [
            "4.10 Introduction to Swing",
            "JFrame, JPanel, JButton, JLabel, JTextField, JTable -- Swing vs AWT",
        ],
        [
            "4.11 Introduction to Servlets",
            "Servlet lifecycle, HttpServlet, doGet, doPost, HttpServletRequest/Response",
        ],
        [
            "4.12 Exam Questions",
            "20+ exam-style questions with detailed answers covering all topics",
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
pn.part_box("UNIT IV -- AWT, GUI PROGRAMMING, SWING & SERVLET")

# =============================================================================
#  4.1  INTRODUCING THE AWT
# =============================================================================
pn.chap_box("4.1  Introducing the AWT")
pn.section("What is the Abstract Window Toolkit?")
pn.definition(
    "<b>AWT (Abstract Window Toolkit):</b> Java's original platform-independent "
    "windowing, graphics, and user-interface widget toolkit, introduced in Java 1.0. "
    "Located in the <code>java.awt</code> package, AWT provides classes for creating "
    "graphical user interfaces (GUIs) with windows, buttons, text fields, menus, "
    "and layout managers. "
    "AWT components are <b>heavyweight</b> -- each component is a thin wrapper around "
    "a native operating-system UI control (a Windows HWND, a macOS NSView, etc.). "
    "This means AWT GUIs look and behave like native OS applications, but may differ "
    "slightly across platforms."
)

pn.section("AWT vs Swing -- Key Differences")
pn.info_table(
    ["Feature", "AWT", "Swing"],
    [
        ["Package", "java.awt", "javax.swing"],
        [
            "Component weight",
            "Heavyweight -- wraps native OS widgets",
            "Lightweight -- drawn entirely by Java 2D",
        ],
        [
            "Look & Feel",
            "Native OS look (platform-dependent)",
            "Pluggable Look & Feel (consistent across OS)",
        ],
        [
            "Component prefix",
            "Button, TextField, Checkbox...",
            "JButton, JTextField, JCheckBox...",
        ],
        [
            "Rich components",
            "Limited set (basic controls only)",
            "Rich set: JTable, JTree, JTabbedPane, JSlider...",
        ],
        [
            "Threading model",
            "Single-threaded (AWT Event Thread)",
            "Single-threaded (Swing EDT -- same model)",
        ],
        ["MVC architecture", "Not enforced", "Built around Model-View-Controller"],
        [
            "Performance",
            "Delegates to OS -- very fast for basics",
            "Pure Java paint -- slightly slower but richer",
        ],
        [
            "When introduced",
            "Java 1.0 (1995)",
            "Java 1.2 (1998), default GUI toolkit since then",
        ],
    ],
)

pn.note(
    "In the IT408 syllabus, AWT (Unit IV) is taught first because it is the foundation "
    "of all Java GUI programming. Swing components extend AWT containers. "
    "Understanding AWT Component, Container, Frame, and LayoutManager is mandatory "
    "before studying Swing effectively."
)
pn.br()

# =============================================================================
#  4.2  AWT CLASS HIERARCHY
# =============================================================================
pn.chap_box("4.2  AWT Class Hierarchy")
pn.section("The Complete AWT Component Tree")
pn.body(
    "Every AWT visual element inherits from <code>java.awt.Component</code>. "
    "Understanding this hierarchy is essential for knowing which methods are "
    "available at each level and how containers hold other components."
)

# UML class diagram showing the full AWT hierarchy
cd_awt = pd.ClassDiagram(
    width=pn.CW,
    height=260,
    theme=diag_theme,
    caption="Fig 4.1: AWT Class Hierarchy -- Component to Frame to Applet",
    class_w=130,
)
cd_awt.uml_class(
    "Object",
    "java.lang.Object",
    methods=["+ equals(), toString()"],
)
cd_awt.uml_class(
    "Component",
    "java.awt.Component",
    methods=[
        "+ paint(g), repaint()",
        "+ setSize(), setVisible()",
        "+ setBackground(), setForeground()",
        "+ addMouseListener(), addKeyListener()",
    ],
)
cd_awt.uml_class(
    "Container",
    "java.awt.Container",
    methods=["+ add(Component)", "+ setLayout(LayoutManager)", "+ remove(Component)"],
)
cd_awt.uml_class(
    "Window",
    "java.awt.Window",
    methods=["+ pack(), show()", "+ addWindowListener()"],
)
cd_awt.uml_class(
    "Panel",
    "java.awt.Panel",
    methods=["+ Panel()"],
)
cd_awt.uml_class(
    "Frame",
    "java.awt.Frame",
    methods=["+ setTitle(String)", "+ setMenuBar(MenuBar)", "+ setIconImage(Image)"],
)
cd_awt.uml_class(
    "Dialog",
    "java.awt.Dialog",
    methods=["+ setModal(boolean)", "+ setTitle(String)"],
)
cd_awt.uml_class(
    "Applet",
    "java.applet.Applet",
    methods=["+ init(), start()", "+ stop(), destroy()"],
)
cd_awt.relate("Component", "Object", kind="inheritance")
cd_awt.relate("Container", "Component", kind="inheritance")
cd_awt.relate("Window", "Container", kind="inheritance")
cd_awt.relate("Panel", "Container", kind="inheritance")
cd_awt.relate("Frame", "Window", kind="inheritance")
cd_awt.relate("Dialog", "Window", kind="inheritance")
cd_awt.relate("Applet", "Panel", kind="inheritance")
pn.story.extend(cd_awt.as_flowable())

pn.section("Key Classes in the AWT Hierarchy")
pn.info_table(
    ["Class", "Package", "Description"],
    [
        [
            "Component",
            "java.awt",
            "Root of all AWT visual elements. Provides methods for painting, event handling, size, position, color, and font.",
        ],
        [
            "Container",
            "java.awt",
            "A Component that can hold other Components. Manages child layout using a LayoutManager.",
        ],
        [
            "Panel",
            "java.awt",
            "Simplest concrete Container. Used as a drawing area or to group components. Has no title bar or borders.",
        ],
        [
            "Window",
            "java.awt",
            "A top-level Container that has NO title bar, menu bar, or border. Parent of Frame and Dialog.",
        ],
        [
            "Frame",
            "java.awt",
            "Top-level windowed container WITH title bar, minimize/maximize/close buttons, and optional MenuBar. Most common AWT top-level container.",
        ],
        [
            "Dialog",
            "java.awt",
            "A secondary window, modal or modeless. Requires a parent Frame. Used for file choosers, alerts, input prompts.",
        ],
        [
            "Applet",
            "java.applet",
            "Extends Panel -- thus an AWT Container. Embedded in browser instead of being a top-level window.",
        ],
    ],
)
pn.br()

# =============================================================================
#  4.3  WINDOW FUNDAMENTALS -- COMPONENT, CONTAINER, PANEL, FRAME
# =============================================================================
pn.chap_box("4.3  Window Fundamentals")
pn.section("The Component Class")
pn.definition(
    "<b>Component:</b> The abstract superclass of all AWT UI elements. "
    "Every button, label, text field, panel, and frame is a Component. "
    "It provides the fundamental infrastructure for display and interaction: "
    "painting on screen, receiving events, and managing visual properties. "
    "You cannot instantiate Component directly -- you use one of its subclasses."
)
pn.info_table(
    ["Component Method", "Description"],
    [
        ["setSize(int w, int h)", "Sets the component's pixel width and height."],
        [
            "setLocation(int x, int y)",
            "Sets the component's top-left position relative to its parent.",
        ],
        [
            "setBounds(int x, int y, int w, int h)",
            "Sets position and size in one call.",
        ],
        [
            "setVisible(boolean b)",
            "Shows (true) or hides (false) the component. New frames are hidden by default.",
        ],
        [
            "setEnabled(boolean b)",
            "Enables (true) or disables (false) interaction with the component.",
        ],
        ["setBackground(Color c)", "Sets the background fill color of the component."],
        ["setForeground(Color c)", "Sets the text/drawing color of the component."],
        ["setFont(Font f)", "Sets the font used for text in this component."],
        [
            "getWidth() / getHeight()",
            "Returns the current pixel width or height of the component.",
        ],
        [
            "repaint()",
            "Requests that the component be redrawn by calling update() -> paint().",
        ],
        [
            "paint(Graphics g)",
            "Override to custom-draw the component. Called by AWT automatically.",
        ],
        [
            "addMouseListener(l)",
            "Registers a MouseListener for click/press/release/enter/exit events.",
        ],
        ["addKeyListener(l)", "Registers a KeyListener for keyboard events."],
    ],
)

pn.section("The Container Class")
pn.definition(
    "<b>Container:</b> A Component that can contain other Components. "
    "When you call <code>add(Component)</code> on a Container, the component becomes "
    "a child and is positioned according to the Container's <code>LayoutManager</code>. "
    "Containers can be nested: a Panel inside a Frame, a Panel inside another Panel."
)
pn.code_block(
    """
// Container usage -- adding components to a Panel
import java.awt.*;

public class ContainerDemo {
    public static void main(String[] args) {
        Frame f = new Frame("Container Demo");

        // Panel is a lightweight Container -- used to group components
        Panel p = new Panel();
        p.setLayout(new FlowLayout());   // arrange children left-to-right

        // Add AWT controls to the Panel
        p.add(new Label("Name:"));
        p.add(new TextField(15));
        p.add(new Button("Submit"));

        // Add the Panel to the Frame
        f.add(p);           // Frame's default layout is BorderLayout
        f.setSize(350, 150);
        f.setVisible(true);
    }
}
""",
    lang="java",
)

pn.section("The Panel Class")
pn.definition(
    "<b>Panel:</b> The simplest concrete Container. It has no title bar, "
    "borders, or window chrome -- it is just a rectangular area that can "
    "hold and arrange other components. Panels are used to: "
    "(1) Group a set of related controls together. "
    "(2) Create regions within a Frame (e.g., a top toolbar panel and a center content panel). "
    "(3) Serve as the drawing surface in an Applet. "
    "Default layout manager: FlowLayout."
)

pn.section("The Frame Class")
pn.definition(
    "<b>Frame:</b> A top-level application window with a title bar, "
    "system-provided minimize/maximize/close buttons, optional menu bar, "
    "and a resizable border. It is the most commonly used AWT container for "
    "standalone GUI applications. Default layout manager: BorderLayout. "
    "A Frame is NOT visible by default -- you must call <code>setVisible(true)</code>."
)
pn.info_table(
    ["Frame Method", "Description"],
    [
        [
            "Frame(String title)",
            "Constructor -- creates a Frame with the given title bar text.",
        ],
        ["setTitle(String title)", "Changes the title bar text after creation."],
        ["setSize(int w, int h)", "Sets the frame's width and height in pixels."],
        [
            "setVisible(boolean b)",
            "Shows (true) or hides (false) the frame. Must call setVisible(true) to see the window.",
        ],
        [
            "setResizable(boolean b)",
            "Allows (true) or prevents (false) user resizing of the window.",
        ],
        ["setMenuBar(MenuBar mb)", "Attaches a MenuBar to the frame's top edge."],
        [
            "setIconImage(Image img)",
            "Sets the icon shown in the taskbar and title bar.",
        ],
        [
            "pack()",
            "Resizes the frame to the preferred size of its components. Use after adding all components.",
        ],
        [
            "dispose()",
            "Destroys the frame's native resources and removes it from screen.",
        ],
        [
            "setLocationRelativeTo(null)",
            "Centers the frame on screen (pass null for screen center).",
        ],
    ],
)
pn.br()

# =============================================================================
#  4.4  WORKING WITH FRAME WINDOWS
# =============================================================================
pn.chap_box("4.4  Working with Frame Windows")
pn.section("Creating a Frame -- Three Approaches")

pn.body("<b>Approach 1: Directly Instantiate Frame</b>")
pn.code_block(
    """
// DirectFrameDemo.java -- simplest way to create a Frame window
import java.awt.*;
import java.awt.event.*;

public class DirectFrameDemo {
    public static void main(String[] args) {
        // Create a Frame with a title
        Frame f = new Frame("My First AWT Window");

        // Set window size: width=400, height=300 pixels
        f.setSize(400, 300);

        // Center on screen by passing null to setLocationRelativeTo
        f.setLocationRelativeTo(null);

        // Set background color
        f.setBackground(Color.LIGHT_GRAY);

        // CRITICAL: A Frame starts invisible -- must call setVisible(true)
        f.setVisible(true);

        // ---- Handle window close button (X) ----
        // Without this, clicking X does NOT close the application!
        f.addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosing(WindowEvent e) {
                f.dispose();         // release native window resources
                System.exit(0);      // terminate the JVM
            }
        });
    }
}
""",
    lang="java",
)

pn.body("<b>Approach 2: Extend Frame (Recommended for OOP design)</b>")
pn.code_block(
    """
// ExtendFrameDemo.java -- extend Frame for reusable window classes
import java.awt.*;
import java.awt.event.*;

// Extending Frame is the OOP-friendly approach
// All Frame methods are available directly (no need for f.xxx())
public class ExtendFrameDemo extends Frame {

    // ---- Declare UI components as instance fields ----
    Button btnOK, btnCancel;
    Label  lblMessage;
    TextField txtInput;

    // Constructor -- build the entire UI here
    public ExtendFrameDemo(String title) {
        super(title);               // call Frame(String) constructor

        // ---- Configure the Frame ----
        setSize(400, 250);
        setBackground(new Color(240, 240, 255));
        setLayout(new FlowLayout(FlowLayout.CENTER, 10, 20));

        // ---- Create and add components ----
        lblMessage = new Label("Enter your name:");
        txtInput   = new TextField(20);
        btnOK      = new Button("OK");
        btnCancel  = new Button("Cancel");

        add(lblMessage);
        add(txtInput);
        add(btnOK);
        add(btnCancel);

        // ---- Event handler for OK button ----
        btnOK.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String name = txtInput.getText().trim();
                lblMessage.setText("Hello, " + name + "!");
            }
        });

        // ---- Event handler for Cancel button ----
        btnCancel.addActionListener(e -> {
            txtInput.setText("");           // Java 8+ lambda syntax
            lblMessage.setText("Enter your name:");
        });

        // ---- Window close handler ----
        addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosing(WindowEvent e) {
                dispose();
                System.exit(0);
            }
        });

        // ---- Show the window ----
        setVisible(true);
    }

    // main() creates an instance of our custom Frame subclass
    public static void main(String[] args) {
        new ExtendFrameDemo("Extended Frame Demo");
    }
}
""",
    lang="java",
)

pn.section("WindowListener and WindowAdapter")
pn.definition(
    "<b>WindowListener:</b> An interface with 7 callback methods for window events. "
    "You must implement ALL 7 methods even if you only need one. "
    "<b>WindowAdapter:</b> A convenience adapter class that provides empty "
    "implementations of all 7 WindowListener methods. Extend WindowAdapter and "
    "override only the methods you need -- this is the standard approach."
)
pn.info_table(
    ["WindowListener Method", "Triggered When"],
    [
        [
            "windowOpened(WindowEvent e)",
            "Window is first made visible (after setVisible(true)).",
        ],
        [
            "windowClosing(WindowEvent e)",
            "User clicks the X button. This is where you call dispose() and System.exit(0).",
        ],
        [
            "windowClosed(WindowEvent e)",
            "Window has been closed (after dispose() is called).",
        ],
        ["windowIconified(WindowEvent e)", "Window is minimized to taskbar icon."],
        ["windowDeiconified(WindowEvent e)", "Window is restored from taskbar icon."],
        [
            "windowActivated(WindowEvent e)",
            "Window gains focus (becomes the foreground window).",
        ],
        ["windowDeactivated(WindowEvent e)", "Window loses focus."],
    ],
)
pn.br()

# =============================================================================
#  4.5  GRAPHICS AND TEXT IN AWT
# =============================================================================
pn.chap_box("4.5  Graphics and Text in AWT Frame")
pn.section("Drawing in a Frame using paint()")
pn.body(
    "Unlike an Applet where AWT automatically calls paint(Graphics g), "
    "in a Frame you override paint() directly to draw custom graphics. "
    "The Graphics object is provided by the AWT system. "
    "Everything drawn inside paint() appears within the Frame's client area "
    "(below the title bar)."
)

pn.code_block(
    """
// GraphicsFrameDemo.java -- Drawing text, shapes, and colors in a Frame
import java.awt.*;
import java.awt.event.*;

public class GraphicsFrameDemo extends Frame {

    public GraphicsFrameDemo() {
        super("Graphics in Frame -- IT408 Unit IV");
        setSize(520, 420);
        setBackground(Color.WHITE);
        addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent e) { dispose(); System.exit(0); }
        });
        setVisible(true);
    }

    // Override paint() to draw custom graphics
    // Note: In a Frame, paint() includes the title bar area in its coordinate space
    // Use getInsets() to find the title bar offset if positioning precisely
    @Override
    public void paint(Graphics g) {
        Insets ins = getInsets();   // title bar + border thickness
        int ox = ins.left;          // x offset for usable area
        int oy = ins.top;           // y offset for usable area

        // ---- 1. TEXT with different fonts ----
        g.setFont(new Font("Arial", Font.BOLD, 18));
        g.setColor(Color.DARK_GRAY);
        g.drawString("AWT Graphics in Frame Window", ox + 60, oy + 30);

        g.setFont(new Font("Courier New", Font.PLAIN, 12));
        g.setColor(Color.BLUE);
        g.drawString("Font.PLAIN Courier, size 12", ox + 20, oy + 60);

        g.setFont(new Font("Times New Roman", Font.ITALIC, 14));
        g.setColor(Color.RED);
        g.drawString("Font.ITALIC Times New Roman, size 14", ox + 20, oy + 85);

        // ---- 2. LINES ----
        g.setColor(Color.BLACK);
        g.drawLine(ox + 20, oy + 100, ox + 480, oy + 100);     // horizontal separator

        // ---- 3. RECTANGLES (outline and filled) ----
        g.setColor(Color.BLUE);
        g.drawRect(ox + 20, oy + 115, 100, 60);                // outline rectangle
        g.setColor(new Color(200, 200, 255));
        g.fillRect(ox + 140, oy + 115, 100, 60);               // filled rectangle
        g.setColor(Color.BLACK);
        g.setFont(new Font("Arial", Font.PLAIN, 10));
        g.drawString("drawRect", ox + 35, oy + 190);
        g.drawString("fillRect", ox + 155, oy + 190);

        // ---- 4. OVALS AND CIRCLES ----
        g.setColor(Color.RED);
        g.drawOval(ox + 260, oy + 115, 80, 60);               // oval outline
        g.setColor(new Color(255, 200, 200));
        g.fillOval(ox + 360, oy + 115, 70, 70);               // filled circle
        g.setColor(Color.BLACK);
        g.drawString("drawOval", ox + 267, oy + 190);
        g.drawString("fillOval", ox + 370, oy + 195);

        // ---- 5. ARC ----
        g.setColor(Color.GREEN);
        g.drawArc(ox + 20, oy + 210, 120, 80, 0, 270);        // 270-degree arc
        g.setColor(Color.BLACK);
        g.drawString("drawArc (270 deg)", ox + 20, oy + 305);

        // ---- 6. POLYGON (triangle) ----
        int[] xs = { ox + 200, ox + 250, ox + 300 };
        int[] ys = { oy + 290, oy + 210, oy + 290 };
        g.setColor(new Color(100, 180, 100));
        g.fillPolygon(xs, ys, 3);
        g.setColor(Color.BLACK);
        g.drawString("fillPolygon (triangle)", ox + 185, oy + 310);

        // ---- 7. ROUND RECTANGLE ----
        g.setColor(Color.MAGENTA);
        g.drawRoundRect(ox + 350, oy + 210, 120, 70, 25, 25); // rounded corners
        g.setColor(Color.BLACK);
        g.drawString("drawRoundRect", ox + 355, oy + 300);

        // ---- 8. COLOR SWATCHES ----
        Color[] palette = { Color.RED, Color.ORANGE, Color.YELLOW,
                            Color.GREEN, Color.BLUE, Color.MAGENTA };
        for (int i = 0; i < palette.length; i++) {
            g.setColor(palette[i]);
            g.fillRect(ox + 20 + i * 75, oy + 325, 60, 30);
        }
        g.setColor(Color.BLACK);
        g.drawString("AWT Color palette swatches", ox + 120, oy + 380);
    }

    public static void main(String[] args) {
        new GraphicsFrameDemo();
    }
}
""",
    lang="java",
)

pn.tip(
    "In a Frame, use getInsets() to find the exact height of the title bar. "
    "This prevents drawing underneath the title. "
    "getInsets().top is the title bar height in pixels. "
    "Always add getInsets() offsets to x,y coordinates in paint()."
)
pn.br()

# =============================================================================
#  4.6  HANDLING EVENTS IN A FRAME WINDOW
# =============================================================================
pn.chap_box("4.6  Handling Events in a Frame Window")
pn.section("Event Handling in AWT -- Overview")
pn.definition(
    "<b>Event Handling:</b> The mechanism by which a program responds to user actions "
    "(button clicks, key presses, mouse movement, window operations). "
    "In modern AWT (Java 1.1+), the <b>Delegation Event Model</b> is used: "
    "a component (event source) fires an event object; "
    "one or more registered listener objects receive and handle the event. "
    "This separates the UI component from the business logic that handles it."
)

pn.section("Common AWT Event Listeners")
pn.info_table(
    ["Listener Interface", "Event Type", "Key Methods", "Adapter Class"],
    [
        [
            "ActionListener",
            "Button click, menu item select, Return key in TextField",
            "actionPerformed(ActionEvent e)",
            "None (single method)",
        ],
        [
            "WindowListener",
            "Frame open/close/minimize/restore/activate",
            "windowClosing, windowOpened, windowClosed...",
            "WindowAdapter",
        ],
        [
            "MouseListener",
            "Click, press, release, enter, exit",
            "mouseClicked, mousePressed, mouseReleased, mouseEntered, mouseExited",
            "MouseAdapter",
        ],
        [
            "MouseMotionListener",
            "Move, drag",
            "mouseMoved, mouseDragged",
            "MouseMotionAdapter",
        ],
        [
            "KeyListener",
            "Key pressed/released/typed",
            "keyPressed, keyReleased, keyTyped",
            "KeyAdapter",
        ],
        [
            "ItemListener",
            "Checkbox/Choice/List selection change",
            "itemStateChanged(ItemEvent e)",
            "None (single method)",
        ],
        [
            "TextListener",
            "Text field/area content change",
            "textValueChanged(TextEvent e)",
            "None (single method)",
        ],
        [
            "AdjustmentListener",
            "Scrollbar position change",
            "adjustmentValueChanged(AdjustmentEvent e)",
            "None (single method)",
        ],
        [
            "FocusListener",
            "Component gains/loses keyboard focus",
            "focusGained, focusLost",
            "FocusAdapter",
        ],
    ],
)

pn.section("Four Ways to Handle Events")
pn.body("<b>Method 1: Named inner class (most readable, classic approach)</b>")
pn.code_block(
    """
// Method 1: Named inner class listener -- classic and most readable approach
import java.awt.*;
import java.awt.event.*;

public class InnerClassEventDemo extends Frame {

    Button btnClick;
    Label  lblStatus;

    // ---- Named inner class: ButtonHandler ----
    // Placed inside the outer class, has access to all outer fields
    class ButtonHandler implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            lblStatus.setText("Button was clicked at " + e.getWhen() + " ms!");
        }
    }

    public InnerClassEventDemo() {
        super("Inner Class Event Demo");
        setSize(420, 180);
        setLayout(new FlowLayout(FlowLayout.CENTER, 15, 25));

        btnClick  = new Button("Click Me!");
        lblStatus = new Label("Waiting for click...", Label.CENTER);
        lblStatus.setPreferredSize(new Dimension(350, 30));

        // Register the inner class listener with the button
        btnClick.addActionListener(new ButtonHandler());

        add(btnClick);
        add(lblStatus);

        addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent e) { dispose(); System.exit(0); }
        });
        setVisible(true);
    }

    public static void main(String[] args) { new InnerClassEventDemo(); }
}
""",
    lang="java",
)

pn.body("<b>Method 2: Anonymous inner class (most common in practice)</b>")
pn.code_block(
    """
// Method 2: Anonymous inner class listener -- most common in AWT code
// The listener is defined exactly where it is registered
btnClick.addActionListener(new ActionListener() {
    @Override
    public void actionPerformed(ActionEvent e) {
        lblStatus.setText("Clicked! Source: " + ((Button)e.getSource()).getLabel());
    }
});
""",
    lang="java",
)

pn.body(
    "<b>Method 3: Lambda expression (Java 8+, only for single-method interfaces)</b>"
)
pn.code_block(
    """
// Method 3: Lambda -- compact syntax for single-method (functional) interfaces
// ActionListener has exactly one method (actionPerformed), so lambdas work
btnClick.addActionListener(e -> lblStatus.setText("Lambda handler called!"));

// WindowAdapter with lambda (must still use anonymous class for adapters)
addWindowListener(new WindowAdapter() {
    public void windowClosing(WindowEvent e) { System.exit(0); }
});
""",
    lang="java",
)

pn.body("<b>Method 4: The outer class implements the listener (self-registration)</b>")
pn.code_block(
    """
// Method 4: Frame itself implements ActionListener
// 'this' is passed as the listener -- clean but mixes concerns for large UIs
import java.awt.*;
import java.awt.event.*;

public class SelfHandlerDemo extends Frame implements ActionListener, WindowListener {

    Button btnA, btnB;
    Label  lblOut;

    public SelfHandlerDemo() {
        super("Self Handler Demo");
        setSize(380, 160);
        setLayout(new FlowLayout());

        btnA  = new Button("Button A");
        btnB  = new Button("Button B");
        lblOut = new Label("Press a button.", Label.CENTER);

        // Register 'this' as the listener for both buttons
        btnA.addActionListener(this);
        btnB.addActionListener(this);
        this.addWindowListener(this);

        add(btnA); add(btnB); add(lblOut);
        setVisible(true);
    }

    // Single actionPerformed handles events from BOTH buttons
    // Use e.getActionCommand() or e.getSource() to distinguish
    @Override
    public void actionPerformed(ActionEvent e) {
        String cmd = e.getActionCommand();   // returns button label text
        if (cmd.equals("Button A")) lblOut.setText("Button A was pressed!");
        else if (cmd.equals("Button B")) lblOut.setText("Button B was pressed!");
    }

    // WindowListener implementation -- implement all 7 methods (even if empty)
    @Override public void windowClosing(WindowEvent e) { dispose(); System.exit(0); }
    @Override public void windowOpened(WindowEvent e)  {}
    @Override public void windowClosed(WindowEvent e)  {}
    @Override public void windowIconified(WindowEvent e)   {}
    @Override public void windowDeiconified(WindowEvent e) {}
    @Override public void windowActivated(WindowEvent e)   {}
    @Override public void windowDeactivated(WindowEvent e) {}

    public static void main(String[] args) { new SelfHandlerDemo(); }
}
""",
    lang="java",
)

pn.section("Event Delegation Model Flow")
fc_event = pd.Flowchart(
    width=pn.CW,
    height=280,
    theme=diag_theme,
    caption="Fig 4.2: AWT Delegation Event Model -- source generates event, listener handles it",
)
fc_event.terminal("user", "User Action (click button, press key, move mouse)")
fc_event.process(
    "source", "Event Source (Button, TextField, Frame) generates EventObject"
)
fc_event.process(
    "dispatch", "AWT Event Dispatch Thread delivers EventObject to registered listeners"
)
fc_event.decision("listeners", "Are listeners registered for this event type?")
fc_event.process(
    "call", "AWT calls listener method (actionPerformed, mouseClicked, etc.)"
)
fc_event.process(
    "handler", "Listener handler code executes (update UI, business logic)"
)
fc_event.terminal("done", "Event handling complete -- UI updated")
fc_event.process("ignore", "Event is silently discarded (no listener registered)")

fc_event.edge("user", "source")
fc_event.edge("source", "dispatch")
fc_event.edge("dispatch", "listeners")
fc_event.edge("listeners", "call", branch="yes")
fc_event.edge("listeners", "ignore", branch="no")
fc_event.edge("call", "handler")
fc_event.edge("handler", "done")
pn.story.extend(fc_event.as_flowable())
pn.br()

# =============================================================================
#  4.7  AWT CONTROLS
# =============================================================================
pn.chap_box("4.7  AWT Controls")
pn.section("Overview of AWT Controls")
pn.body(
    "AWT provides a set of ready-made UI controls (also called widgets or components). "
    "Each control is a class in <code>java.awt</code>. They are all subclasses of "
    "<code>Component</code> and can be added to any Container."
)

pn.info_table(
    ["Control Class", "Description", "Key Methods / Properties"],
    [
        [
            "Button",
            "A push button with a text label. Fires ActionEvent on click.",
            "new Button(label); addActionListener(); getLabel(); setLabel()",
        ],
        [
            "Label",
            "Non-interactive text display. Cannot be clicked or edited.",
            "new Label(text, alignment); setText(); getText(); Label.CENTER / LEFT / RIGHT",
        ],
        [
            "TextField",
            "Single-line editable text input box.",
            "new TextField(columns); getText(); setText(); setEchoChar('*') for password",
        ],
        [
            "TextArea",
            "Multi-line scrollable text editing area.",
            "new TextArea(rows, cols); getText(); setText(); append(str); setEditable(false)",
        ],
        [
            "Checkbox",
            "A toggle button with checked/unchecked state and a label.",
            "new Checkbox(label, state); getState(); setState(true/false); addItemListener()",
        ],
        [
            "CheckboxGroup",
            "Groups multiple Checkboxes into a radio-button group (one selected at a time).",
            "new CheckboxGroup(); new Checkbox(label, group, state); getSelectedCheckbox()",
        ],
        [
            "Choice",
            "A drop-down selection list (combo box).",
            "new Choice(); add(item); getSelectedItem(); getSelectedIndex(); addItemListener()",
        ],
        [
            "List",
            "A scrollable list showing multiple items; supports single/multiple selection.",
            "new List(rows, multiSelect); add(item); getSelectedItem(); getSelectedItems()",
        ],
        [
            "Scrollbar",
            "A horizontal or vertical scroll slider.",
            "new Scrollbar(orientation, value, visible, min, max); getValue(); addAdjustmentListener()",
        ],
        [
            "Canvas",
            "A blank component for custom drawing. Override paint().",
            "new Canvas(); override paint(Graphics g); repaint()",
        ],
    ],
)

pn.section("Complete AWT Controls Demo")
pn.code_block(
    """
// AWTControlsDemo.java -- demonstrates Button, Label, TextField, Checkbox, Choice, List
import java.awt.*;
import java.awt.event.*;

public class AWTControlsDemo extends Frame implements ActionListener, ItemListener {

    // ---- Declare all controls ----
    Label  lblName, lblGender, lblCourse, lblResult;
    TextField txtName;
    Checkbox  chkMale, chkFemale;
    CheckboxGroup genderGroup;
    Choice    choiceCourse;   // drop-down list
    List      listSkills;     // multi-select scrollable list
    Button    btnSubmit, btnClear;
    TextArea  taOutput;

    public AWTControlsDemo() {
        super("AWT Controls Demo -- IT408");
        setSize(500, 500);
        setLayout(new FlowLayout(FlowLayout.LEFT, 10, 8));
        setBackground(new Color(245, 245, 255));

        // ---- Labels ----
        lblName   = new Label("Student Name:");
        lblGender = new Label("Gender:");
        lblCourse = new Label("Course:");
        lblResult = new Label("Result will appear here.", Label.CENTER);

        // ---- TextField: single-line text input ----
        txtName = new TextField(25);

        // ---- CheckboxGroup: radio buttons for gender ----
        genderGroup = new CheckboxGroup();
        chkMale   = new Checkbox("Male",   genderGroup, true);  // default selected
        chkFemale = new Checkbox("Female", genderGroup, false);

        // ---- Choice: drop-down for course selection ----
        choiceCourse = new Choice();
        choiceCourse.add("Information Technology");
        choiceCourse.add("Computer Science");
        choiceCourse.add("Electronics");
        choiceCourse.add("Mechanical");

        // ---- List: multi-select skill list ----
        listSkills = new List(4, true);  // 4 visible rows, multiselect=true
        listSkills.add("Java Programming");
        listSkills.add("Python");
        listSkills.add("Web Development");
        listSkills.add("Database (SQL)");
        listSkills.add("Machine Learning");

        // ---- Buttons ----
        btnSubmit = new Button("Submit Form");
        btnClear  = new Button("Clear");

        // ---- TextArea for output display ----
        taOutput = new TextArea(6, 45);
        taOutput.setEditable(false);        // read-only output area
        taOutput.setBackground(Color.WHITE);
        taOutput.setFont(new Font("Courier New", Font.PLAIN, 12));

        // ---- Register event listeners ----
        btnSubmit.addActionListener(this);
        btnClear.addActionListener(this);
        choiceCourse.addItemListener(this);

        // ---- Add all controls to the Frame ----
        add(lblName);   add(txtName);
        add(lblGender); add(chkMale); add(chkFemale);
        add(new Label("Course:"));  add(choiceCourse);
        add(new Label("Skills (multi-select):")); add(listSkills);
        add(btnSubmit); add(btnClear);
        add(new Label("Output:")); add(taOutput);

        addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent e) { dispose(); System.exit(0); }
        });
        setVisible(true);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == btnSubmit) {
            // Collect all field values
            String name    = txtName.getText().trim();
            String gender  = genderGroup.getSelectedCheckbox().getLabel();
            String course  = choiceCourse.getSelectedItem();
            String[] skills = listSkills.getSelectedItems(); // returns String[]

            StringBuilder sb = new StringBuilder();
            sb.append("Name   : ").append(name).append("\n");
            sb.append("Gender : ").append(gender).append("\n");
            sb.append("Course : ").append(course).append("\n");
            sb.append("Skills : ");
            for (String s : skills) sb.append(s).append(", ");
            sb.append("\n--- Form Submitted Successfully ---");
            taOutput.setText(sb.toString());

        } else if (e.getSource() == btnClear) {
            // Reset all fields to defaults
            txtName.setText("");
            genderGroup.setSelectedCheckbox(chkMale);
            choiceCourse.select(0);
            listSkills.deselectAll();
            taOutput.setText("");
        }
    }

    @Override
    public void itemStateChanged(ItemEvent e) {
        // Called when Choice selection changes
        if (e.getSource() == choiceCourse) {
            taOutput.append("Course changed to: " + choiceCourse.getSelectedItem() + "\n");
        }
    }

    public static void main(String[] args) { new AWTControlsDemo(); }
}
""",
    lang="java",
)

pn.section("Scrollbar Control")
pn.code_block(
    """
// ScrollbarDemo.java -- AWT Scrollbar with AdjustmentListener
import java.awt.*;
import java.awt.event.*;

public class ScrollbarDemo extends Frame implements AdjustmentListener {

    Scrollbar hBar, vBar;
    Label lblValue;

    public ScrollbarDemo() {
        super("Scrollbar Demo");
        setSize(400, 200);
        setLayout(new FlowLayout());

        // Scrollbar(orientation, initialValue, visibleAmount, min, max)
        // HORIZONTAL = 0, VERTICAL = 1
        hBar = new Scrollbar(Scrollbar.HORIZONTAL, 50, 10, 0, 200);
        vBar = new Scrollbar(Scrollbar.VERTICAL,   50, 10, 0, 200);
        lblValue = new Label("H=50  V=50", Label.CENTER);
        lblValue.setPreferredSize(new Dimension(350, 30));

        hBar.addAdjustmentListener(this);
        vBar.addAdjustmentListener(this);

        add(new Label("Horizontal:")); add(hBar);
        add(new Label("Vertical:"));  add(vBar);
        add(lblValue);

        addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent e) { dispose(); System.exit(0); }
        });
        setVisible(true);
    }

    @Override
    public void adjustmentValueChanged(AdjustmentEvent e) {
        // Called whenever either scrollbar moves
        lblValue.setText("H=" + hBar.getValue() + "  V=" + vBar.getValue());
    }

    public static void main(String[] args) { new ScrollbarDemo(); }
}
""",
    lang="java",
)
pn.br()

# =============================================================================
#  4.8  LAYOUT MANAGERS
# =============================================================================
pn.chap_box("4.8  Layout Managers")
pn.section("What is a Layout Manager?")
pn.definition(
    "<b>Layout Manager:</b> An object that implements the <code>java.awt.LayoutManager</code> "
    "interface and controls the size and position of components inside a Container. "
    "Instead of placing components at absolute pixel coordinates (which breaks when the "
    "window is resized or rendered on a different screen DPI), a LayoutManager "
    "automatically repositions and resizes components based on rules. "
    "You set a layout manager with <code>container.setLayout(new XxxLayout())</code>. "
    "Passing <code>null</code> to setLayout() enables absolute positioning."
)

pn.info_table(
    ["Layout Manager", "Default for", "How it Arranges Components"],
    [
        [
            "FlowLayout",
            "Panel, Applet",
            "Left-to-right, top-to-bottom. New row when row fills. Like words in a paragraph.",
        ],
        [
            "BorderLayout",
            "Frame, Dialog, Window",
            "Five regions: NORTH (top), SOUTH (bottom), EAST (right), WEST (left), CENTER (middle, gets all extra space).",
        ],
        [
            "GridLayout",
            "None",
            "Equal-size grid of rows and columns. All cells same width and height.",
        ],
        [
            "CardLayout",
            "None",
            "Stacks components like cards; only one visible at a time. Used for wizard/tab-like panels.",
        ],
        [
            "GridBagLayout",
            "None",
            "Most powerful and complex. Each cell can span multiple rows/columns; cells have individual weights.",
        ],
        [
            "null (Absolute)",
            "None",
            "No manager -- use setBounds(x,y,w,h) for each component. Breaks on resize.",
        ],
    ],
)

pn.section("FlowLayout")
pn.code_block(
    """
// FlowLayout: components flow left-to-right, then wrap to next row
// Constructor: new FlowLayout(alignment, hgap, vgap)
// alignment: FlowLayout.LEFT, CENTER (default), RIGHT, LEADING, TRAILING
// hgap: horizontal gap between components (default 5px)
// vgap: vertical gap between rows (default 5px)

Panel p = new Panel();
p.setLayout(new FlowLayout(FlowLayout.LEFT, 10, 8)); // left-align, 10px hgap, 8px vgap

p.add(new Button("One"));
p.add(new Button("Two"));
p.add(new Button("Three"));
p.add(new Button("Four"));
// Components are placed left-to-right; when row fills, wraps to next row
""",
    lang="java",
)

pn.section("BorderLayout")
pn.code_block(
    """
// BorderLayout: five regions -- NORTH, SOUTH, EAST, WEST, CENTER
// Constructor: new BorderLayout(hgap, vgap)
// CENTER gets all remaining space after NORTH/SOUTH/EAST/WEST are sized

Frame f = new Frame("BorderLayout Demo");
f.setLayout(new BorderLayout(5, 5));  // 5px gaps between regions

f.add(new Button("NORTH"),  BorderLayout.NORTH);   // top strip
f.add(new Button("SOUTH"),  BorderLayout.SOUTH);   // bottom strip
f.add(new Button("EAST"),   BorderLayout.EAST);    // right strip
f.add(new Button("WEST"),   BorderLayout.WEST);    // left strip
f.add(new TextArea(),       BorderLayout.CENTER);  // fills remaining middle area

// KEY: If you add a component WITHOUT specifying a region, it goes to CENTER
// Only one component can occupy each region (last one added wins)
""",
    lang="java",
)

pn.section("GridLayout")
pn.code_block(
    """
// GridLayout: creates a grid where all cells are EXACTLY the same size
// Constructor: new GridLayout(rows, cols, hgap, vgap)
// Components fill the grid left-to-right, top-to-bottom

Panel calcPanel = new Panel();
calcPanel.setLayout(new GridLayout(4, 3, 5, 5));  // 4 rows, 3 columns, 5px gaps

// Add 12 calculator buttons (fills 4x3 grid)
String[] keys = {"7","8","9","4","5","6","1","2","3","0",".","="};
for (String k : keys) {
    calcPanel.add(new Button(k));
}

// KEY: All cells are equal size regardless of component preferred size
// Rows and cols are exact -- if rows=0, auto-calculate based on column count
""",
    lang="java",
)

pn.section("Full Layout Manager Demo")
pn.code_block(
    """
// LayoutDemo.java -- demonstrates FlowLayout, BorderLayout, and GridLayout together
import java.awt.*;
import java.awt.event.*;

public class LayoutDemo extends Frame {

    public LayoutDemo() {
        super("Layout Manager Demo -- IT408");
        setSize(500, 400);

        // Frame uses BorderLayout by default
        // ---- NORTH: Toolbar panel with FlowLayout ----
        Panel northPanel = new Panel(new FlowLayout(FlowLayout.LEFT, 5, 5));
        northPanel.setBackground(new Color(200, 220, 255));
        northPanel.add(new Button("New"));
        northPanel.add(new Button("Open"));
        northPanel.add(new Button("Save"));
        northPanel.add(new TextField("Search...", 15));
        northPanel.add(new Button("Find"));
        add(northPanel, BorderLayout.NORTH);

        // ---- CENTER: GridLayout for a form ----
        Panel centerPanel = new Panel(new GridLayout(4, 2, 8, 8));
        centerPanel.setBackground(new Color(240, 240, 240));
        centerPanel.add(new Label("First Name:", Label.RIGHT));
        centerPanel.add(new TextField(20));
        centerPanel.add(new Label("Last Name:",  Label.RIGHT));
        centerPanel.add(new TextField(20));
        centerPanel.add(new Label("Email:",      Label.RIGHT));
        centerPanel.add(new TextField(20));
        centerPanel.add(new Label("Branch:",     Label.RIGHT));
        Choice c = new Choice();
        c.add("IT"); c.add("CS"); c.add("EC");
        centerPanel.add(c);
        add(centerPanel, BorderLayout.CENTER);

        // ---- SOUTH: Button bar ----
        Panel southPanel = new Panel(new FlowLayout(FlowLayout.RIGHT));
        southPanel.setBackground(new Color(220, 220, 220));
        southPanel.add(new Button("Submit"));
        southPanel.add(new Button("Reset"));
        southPanel.add(new Button("Cancel"));
        add(southPanel, BorderLayout.SOUTH);

        // ---- WEST: Navigation list ----
        List navList = new List(6, false);
        navList.add("Profile");
        navList.add("Courses");
        navList.add("Results");
        navList.add("Library");
        navList.add("Events");
        add(navList, BorderLayout.WEST);

        addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent e) { dispose(); System.exit(0); }
        });
        setVisible(true);
    }

    public static void main(String[] args) { new LayoutDemo(); }
}
""",
    lang="java",
)

pn.section("Layout Manager Comparison Diagram")
# Layered stack showing layout manager characteristics
stack_layout = pd.LayeredStack(
    width=pn.CW,
    height=200,
    theme=diag_theme,
    caption="Fig 4.3: Layout Manager selection guide -- from simplest to most powerful",
)
stack_layout.layer(
    "FlowLayout", sublabel="Simplest. Left-to-right wrap. Default for Panel and Applet."
)
stack_layout.layer(
    "GridLayout", sublabel="Uniform grid. All cells equal size. Good for keypads/forms."
)
stack_layout.layer(
    "BorderLayout",
    sublabel="5 regions (N,S,E,W,C). Default for Frame/Dialog. Most practical.",
)
stack_layout.layer(
    "CardLayout",
    sublabel="One panel visible at a time. Good for wizards/tab switching.",
)
stack_layout.layer(
    "GridBagLayout",
    sublabel="Most powerful. Rows, cols, spans, weights. Complex to configure.",
)
pn.story.extend(stack_layout.as_flowable())
pn.br()

# =============================================================================
#  4.9  MENUS IN AWT
# =============================================================================
pn.chap_box("4.9  Menus in AWT")
pn.section("AWT Menu Hierarchy")
pn.definition(
    "<b>Menu System:</b> AWT provides a complete menu infrastructure. "
    "A <code>MenuBar</code> is attached to a Frame. "
    "Each <code>Menu</code> is added to the MenuBar (File, Edit, Help...). "
    "Each <code>MenuItem</code> is added to a Menu (New, Open, Save...). "
    "Menus can be nested (a MenuItem can itself be a Menu -- creating submenus). "
    "A separator line is added with <code>menu.addSeparator()</code>."
)

pn.info_table(
    ["Menu Class", "Description"],
    [
        [
            "MenuBar",
            "The horizontal bar attached to a Frame. Contains Menu objects. Added via frame.setMenuBar(menuBar).",
        ],
        [
            "Menu",
            "A single pull-down menu (File, Edit, View...). Added to MenuBar or another Menu (submenu).",
        ],
        [
            "MenuItem",
            "A clickable entry within a Menu. Fires ActionEvent when selected.",
        ],
        [
            "CheckboxMenuItem",
            "A MenuItem that can be checked/unchecked. Fires ItemEvent. Use for toggleable options (like View > Toolbar).",
        ],
        [
            "PopupMenu",
            "A context menu that appears at a specific position (on right-click). Added to a component, shown with show(component, x, y).",
        ],
    ],
)

pn.code_block(
    """
// MenuDemo.java -- Complete menu bar with File, Edit, Help menus and event handling
import java.awt.*;
import java.awt.event.*;

public class MenuDemo extends Frame implements ActionListener, ItemListener {

    TextArea taEditor;            // main content area
    CheckboxMenuItem miWordWrap;  // toggle option in View menu

    public MenuDemo() {
        super("AWT Menu Demo -- IT408");
        setSize(600, 400);

        // ============ 1. Create the MenuBar ============
        MenuBar menuBar = new MenuBar();

        // ============ 2. Create File Menu ============
        Menu menuFile = new Menu("File");
        MenuItem miNew    = new MenuItem("New",    new MenuShortcut('N')); // Ctrl+N
        MenuItem miOpen   = new MenuItem("Open",   new MenuShortcut('O'));
        MenuItem miSave   = new MenuItem("Save",   new MenuShortcut('S'));
        MenuItem miSaveAs = new MenuItem("Save As...");
        MenuItem miExit   = new MenuItem("Exit");

        menuFile.add(miNew);
        menuFile.add(miOpen);
        menuFile.add(miSave);
        menuFile.add(miSaveAs);
        menuFile.addSeparator();                    // horizontal separator line
        menuFile.add(miExit);

        // ============ 3. Create Edit Menu ============
        Menu menuEdit = new Menu("Edit");
        MenuItem miCut   = new MenuItem("Cut",   new MenuShortcut('X'));
        MenuItem miCopy  = new MenuItem("Copy",  new MenuShortcut('C'));
        MenuItem miPaste = new MenuItem("Paste", new MenuShortcut('V'));
        MenuItem miSelAll= new MenuItem("Select All", new MenuShortcut('A'));

        menuEdit.add(miCut);
        menuEdit.add(miCopy);
        menuEdit.add(miPaste);
        menuEdit.addSeparator();
        menuEdit.add(miSelAll);

        // ============ 4. Create View Menu with submenu ============
        Menu menuView = new Menu("View");
        miWordWrap = new CheckboxMenuItem("Word Wrap", false);  // starts unchecked
        Menu menuZoom = new Menu("Zoom");                        // SUBMENU
        menuZoom.add(new MenuItem("25%"));
        menuZoom.add(new MenuItem("50%"));
        menuZoom.add(new MenuItem("100%"));
        menuZoom.add(new MenuItem("200%"));

        menuView.add(miWordWrap);
        menuView.addSeparator();
        menuView.add(menuZoom);         // submenu added as a Menu object

        // ============ 5. Create Help Menu ============
        Menu menuHelp = new Menu("Help");
        menuHelp.add(new MenuItem("Help Contents"));
        menuHelp.addSeparator();
        menuHelp.add(new MenuItem("About"));
        menuBar.setHelpMenu(menuHelp);  // setHelpMenu positions it at the right end

        // ============ 6. Assemble MenuBar ============
        menuBar.add(menuFile);
        menuBar.add(menuEdit);
        menuBar.add(menuView);
        // menuHelp is already added via setHelpMenu

        // ============ 7. Attach MenuBar to Frame ============
        setMenuBar(menuBar);

        // ============ 8. Register ActionListeners ============
        miNew.addActionListener(this);
        miOpen.addActionListener(this);
        miSave.addActionListener(this);
        miExit.addActionListener(this);
        miCut.addActionListener(this);
        miCopy.addActionListener(this);
        miPaste.addActionListener(this);
        miWordWrap.addItemListener(this);   // CheckboxMenuItem uses ItemListener

        // ============ 9. Main content area ============
        taEditor = new TextArea("Type here...", 15, 60, TextArea.SCROLLBARS_VERTICAL_ONLY);
        add(taEditor, BorderLayout.CENTER);

        addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent e) { dispose(); System.exit(0); }
        });
        setVisible(true);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        String cmd = e.getActionCommand();
        switch (cmd) {
            case "New":   taEditor.setText(""); break;
            case "Save":  System.out.println("Save triggered: " + taEditor.getText().length() + " chars"); break;
            case "Exit":  dispose(); System.exit(0); break;
            case "Cut":   System.out.println("Cut selected text"); break;
            case "Copy":  System.out.println("Copy selected text"); break;
            case "Paste": System.out.println("Paste clipboard text"); break;
            default:      System.out.println("Menu item: " + cmd); break;
        }
    }

    @Override
    public void itemStateChanged(ItemEvent e) {
        // Called when CheckboxMenuItem is toggled
        if (e.getSource() == miWordWrap) {
            boolean wrapOn = miWordWrap.getState();
            System.out.println("Word Wrap is now: " + (wrapOn ? "ON" : "OFF"));
        }
    }

    public static void main(String[] args) { new MenuDemo(); }
}
""",
    lang="java",
)
pn.br()

# =============================================================================
#  4.10  INTRODUCTION TO SWING
# =============================================================================
pn.chap_box("4.10  Introduction to Swing")
pn.section("What is Swing?")
pn.definition(
    "<b>Swing:</b> A GUI widget toolkit introduced in Java 1.2 as part of the "
    "Java Foundation Classes (JFC). Swing is built on top of AWT but provides "
    "<b>lightweight</b> components (drawn entirely in Java, not OS native widgets). "
    "All Swing components are in the <code>javax.swing</code> package and are "
    "prefixed with 'J' (JButton, JLabel, JTextField). "
    "Swing is the standard GUI toolkit for Java desktop applications. "
    "It follows the <b>Model-View-Controller (MVC)</b> design pattern internally."
)

pn.section("Swing Component Equivalents")
pn.info_table(
    ["AWT Control", "Swing Equivalent", "Key Improvements in Swing Version"],
    [
        [
            "Button",
            "JButton",
            "Supports icons (ImageIcon), HTML text in label, keyboard mnemonics.",
        ],
        [
            "Label",
            "JLabel",
            "Supports icons, HTML text, vertical/horizontal alignment.",
        ],
        [
            "TextField",
            "JTextField",
            "Same basic function; JFormattedTextField for format validation.",
        ],
        [
            "TextArea",
            "JTextArea",
            "Wrap in JScrollPane for scrollbars; supports undo/redo.",
        ],
        ["Checkbox", "JCheckBox", "Supports icons; JCheckBoxMenuItem for menus."],
        [
            "CheckboxGroup (radio)",
            "JRadioButton + ButtonGroup",
            "JRadioButton in ButtonGroup -- cleaner API.",
        ],
        [
            "Choice (combo box)",
            "JComboBox",
            "Editable or non-editable; supports generic type in Java 5+.",
        ],
        [
            "List",
            "JList",
            "Strongly typed generic; wrap in JScrollPane; supports custom renderers.",
        ],
        [
            "Scrollbar",
            "JScrollBar",
            "Rarely used directly; JScrollPane wraps components automatically.",
        ],
        [
            "Frame",
            "JFrame",
            "setDefaultCloseOperation() replaces WindowAdapter; uses content pane.",
        ],
        ["Dialog", "JDialog", "Same improvements as JFrame."],
        [
            "Panel",
            "JPanel",
            "Double-buffered by default; supports borders via setBorder().",
        ],
        [
            "MenuBar/Menu/MenuItem",
            "JMenuBar/JMenu/JMenuItem",
            "Supports icons, keyboard shortcuts (KeyStrokes), look and feel.",
        ],
        [
            "None",
            "JTable",
            "Full spreadsheet-like grid with sortable columns and custom cell renderers.",
        ],
        [
            "None",
            "JTree",
            "Hierarchical tree display for file systems, XML, org charts.",
        ],
        ["None", "JTabbedPane", "Multi-tab interface for switching between views."],
        ["None", "JSlider", "Visual slider with tick marks and labels."],
        ["None", "JProgressBar", "Animated progress indicator."],
    ],
)

pn.section("Key Differences: Creating a Frame in AWT vs Swing")
pn.code_block(
    """
// ============================================================
// AWT Frame (java.awt.Frame) -- Unit IV reference
// ============================================================
import java.awt.*;
import java.awt.event.*;

public class AWTFrameExample extends Frame {
    public AWTFrameExample() {
        super("AWT Frame");
        setSize(400, 250);
        setLayout(new FlowLayout());

        add(new Button("AWT Button"));
        add(new TextField("AWT TextField", 15));
        add(new Label("AWT Label"));

        // Must handle window close explicitly
        addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent e) { dispose(); System.exit(0); }
        });
        setVisible(true);
    }
    public static void main(String[] args) { new AWTFrameExample(); }
}

// ============================================================
// Swing JFrame (javax.swing.JFrame) -- modern equivalent
// ============================================================
import javax.swing.*;
import java.awt.*;

public class SwingFrameExample extends JFrame {
    public SwingFrameExample() {
        super("Swing JFrame");
        setSize(400, 250);

        // Swing: use getContentPane() to add components
        // (or setLayout directly since Java 5 -- Swing forwards automatically)
        Container cp = getContentPane();
        cp.setLayout(new FlowLayout());

        cp.add(new JButton("Swing JButton"));
        cp.add(new JTextField("Swing JTextField", 15));
        cp.add(new JLabel("Swing JLabel with Icon support"));

        // Swing: setDefaultCloseOperation replaces WindowAdapter for closing
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        setVisible(true);
    }
    public static void main(String[] args) {
        // Swing rule: always create GUI on the Event Dispatch Thread
        SwingUtilities.invokeLater(() -> new SwingFrameExample());
    }
}
""",
    lang="java",
)

pn.section("Key Swing Components Demo")
pn.code_block(
    """
// SwingComponentsDemo.java -- JButton, JLabel, JTextField, JComboBox, JTable
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class SwingComponentsDemo extends JFrame {

    public SwingComponentsDemo() {
        super("Swing Components Demo -- IT408");
        setSize(600, 450);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // JPanel with GridLayout for form fields
        JPanel formPanel = new JPanel(new GridLayout(4, 2, 8, 8));
        formPanel.setBorder(BorderFactory.createTitledBorder("Student Details"));

        formPanel.add(new JLabel("Name:"));
        JTextField txtName = new JTextField(20);
        formPanel.add(txtName);

        formPanel.add(new JLabel("Branch:"));
        JComboBox<String> comboBranch = new JComboBox<>(
            new String[]{"Information Technology", "Computer Science", "Electronics"}
        );
        formPanel.add(comboBranch);

        formPanel.add(new JLabel("Semester:"));
        JSpinner spinSemester = new JSpinner(new SpinnerNumberModel(4, 1, 8, 1));
        formPanel.add(spinSemester);

        formPanel.add(new JLabel("Active:"));
        JCheckBox chkActive = new JCheckBox("Currently Enrolled", true);
        formPanel.add(chkActive);

        // JTable for displaying tabular data
        String[] colNames = {"Roll No.", "Name", "Branch", "Marks"};
        Object[][] data = {
            {"001", "Arjun Sharma",  "IT",  "88.5"},
            {"002", "Priya Patel",   "CS",  "92.0"},
            {"003", "Rahul Singh",   "EC",  "79.5"},
            {"004", "Sneha Joshi",   "IT",  "95.0"},
        };
        JTable table = new JTable(data, colNames);
        JScrollPane tableScroll = new JScrollPane(table);  // JScrollPane adds scrollbars
        tableScroll.setBorder(BorderFactory.createTitledBorder("Student Records"));

        // JButton with ActionListener (lambda)
        JButton btnSubmit = new JButton("Submit");
        btnSubmit.addActionListener(e -> {
            JOptionPane.showMessageDialog(
                this,                                      // parent component
                "Name: " + txtName.getText() + "\nBranch: " + comboBranch.getSelectedItem(),
                "Submitted",                               // dialog title
                JOptionPane.INFORMATION_MESSAGE            // icon type
            );
        });

        // Assemble layout using BorderLayout (JFrame default)
        add(formPanel, BorderLayout.NORTH);
        add(tableScroll, BorderLayout.CENTER);
        add(btnSubmit, BorderLayout.SOUTH);

        setVisible(true);
    }

    public static void main(String[] args) {
        // Always use SwingUtilities.invokeLater for thread safety
        SwingUtilities.invokeLater(() -> new SwingComponentsDemo());
    }
}
""",
    lang="java",
)

pn.tip(
    "Swing thread rule: always create and modify Swing components on the Event Dispatch Thread (EDT). "
    "Use SwingUtilities.invokeLater(() -> { ... }) in main() to ensure this. "
    "AWT and Swing components should NEVER be mixed in the same container."
)
pn.br()

# =============================================================================
#  4.11  INTRODUCTION TO SERVLETS
# =============================================================================
pn.chap_box("4.11  Introduction to Servlets")
pn.section("What is a Java Servlet?")
pn.definition(
    "<b>Servlet:</b> A Java class that runs on a web server and handles HTTP requests "
    "from web browsers or other HTTP clients. Servlets are the server-side counterpart "
    "to Applets (which run on the client). They extend "
    "<code>javax.servlet.http.HttpServlet</code> and override "
    "<code>doGet()</code> or <code>doPost()</code> to handle GET/POST requests. "
    "Servlets run inside a <b>Servlet Container</b> (also called a web container), "
    "such as Apache Tomcat, Jetty, or GlassFish. "
    "The container manages the servlet lifecycle: loading, instantiation, request "
    "dispatching, and unloading."
)

pn.section("Servlet vs Applet vs Application")
pn.info_table(
    ["Feature", "Java Applet", "Java Servlet", "Standalone Application"],
    [
        ["Runs on", "Client browser", "Web server (Tomcat/Jetty)", "Local JVM"],
        [
            "Extends",
            "java.applet.Applet",
            "javax.servlet.http.HttpServlet",
            "No required parent",
        ],
        ["Entry point", "init(), start()", "doGet(), doPost()", "main()"],
        [
            "Triggered by",
            "Browser loading HTML page",
            "HTTP request from browser",
            "User/OS/scheduler",
        ],
        [
            "Output",
            "Draws on browser panel (AWT)",
            "Sends HTML/JSON to browser",
            "Console/Swing window",
        ],
        [
            "Security",
            "Sandboxed -- limited",
            "Full server access",
            "Full system access",
        ],
        [
            "Status",
            "Deprecated (Java 17)",
            "Widely used (Spring Boot uses it)",
            "Standard",
        ],
    ],
)

pn.section("Servlet Lifecycle")
pn.definition(
    "<b>Servlet Lifecycle:</b> Managed by the Servlet Container. Three phases: "
    "(1) <b>init(ServletConfig):</b> Called ONCE when the servlet is first loaded. "
    "Initialize resources (DB connections, config reading). "
    "(2) <b>service(HttpServletRequest, HttpServletResponse):</b> Called for EVERY "
    "incoming HTTP request. The container calls service(), which dispatches to "
    "doGet() or doPost() based on the HTTP method. "
    "(3) <b>destroy():</b> Called ONCE before the servlet is unloaded. "
    "Release resources."
)

# Servlet lifecycle state machine
sm_servlet = pd.StateMachine(
    width=pn.CW,
    height=200,
    theme=diag_theme,
    caption="Fig 4.4: Servlet Lifecycle -- init, service (doGet/doPost), destroy",
)
sm_servlet.state("loaded", "CLASS LOADED\nby container", initial=True)
sm_servlet.state("init", "INITIALIZED\n(init() done)")
sm_servlet.state("ready", "READY\n(awaiting requests)")
sm_servlet.state("serving", "SERVING\n(service() running)")
sm_servlet.state("destroyed", "DESTROYED\n(destroy() done)", accepting=True)

sm_servlet.transition("loaded", "init", label="container calls\ninit()")
sm_servlet.transition("init", "ready", label="ready for\nrequests")
sm_servlet.transition("ready", "serving", label="HTTP request\narrives")
sm_servlet.transition("serving", "ready", label="response sent\nto client")
sm_servlet.transition("ready", "destroyed", label="server shutdown\nor undeploy")
pn.story.extend(sm_servlet.as_flowable())

pn.section("A Complete Servlet Example")
pn.code_block(
    """
// HelloServlet.java -- A minimal but complete HTTP Servlet
// Requires: javax.servlet-api.jar in classpath (provided by Tomcat/Jetty)
import javax.servlet.*;
import javax.servlet.http.*;
import java.io.*;

// @WebServlet annotation maps URL pattern to this servlet (Servlet 3.0+)
// Alternatively, configure in web.xml (older approach)
@WebServlet("/hello")          // this servlet handles requests to /hello
public class HelloServlet extends HttpServlet {

    // ================================================================
    // LIFECYCLE METHOD 1: init() -- called ONCE when servlet loads
    // ================================================================
    @Override
    public void init(ServletConfig config) throws ServletException {
        super.init(config);       // MUST call super.init() to initialize ServletConfig
        System.out.println("[SERVLET] init() called -- servlet loaded.");
        // Read initialization parameters from web.xml:
        // String dbUrl = config.getInitParameter("dbUrl");
    }

    // ================================================================
    // LIFECYCLE METHOD 2a: doGet() -- handles HTTP GET requests
    // Called when user types URL in browser or clicks a link
    // ================================================================
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        // Read query parameters from the URL (?name=Rahul&branch=IT)
        String name   = request.getParameter("name");    // reads ?name=Rahul
        String branch = request.getParameter("branch");  // reads ?branch=IT

        // Provide defaults for missing parameters
        if (name   == null) name   = "World";
        if (branch == null) branch = "Unknown";

        // ---- Build the HTTP response ----
        response.setContentType("text/html; charset=UTF-8"); // MIME type
        response.setStatus(HttpServletResponse.SC_OK);        // 200 OK

        // Get a Writer to send HTML content back to the browser
        PrintWriter out = response.getWriter();

        // Write HTML output
        out.println("<!DOCTYPE html>");
        out.println("<html><head><title>Hello Servlet</title></head>");
        out.println("<body>");
        out.println("<h1>Hello, " + name + "!</h1>");
        out.println("<p>Branch: <b>" + branch + "</b></p>");
        out.println("<p>Handled by: HelloServlet (doGet)</p>");
        out.println("<p><a href='/hello?name=Arjun&branch=IT'>Click here (GET)</a></p>");
        out.println("</body></html>");
        // PrintWriter is automatically closed by the container after doGet() returns
    }

    // ================================================================
    // LIFECYCLE METHOD 2b: doPost() -- handles HTTP POST requests
    // Called when an HTML form submits with method="post"
    // ================================================================
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        // Read form fields sent in the POST body (NOT visible in URL)
        String username = request.getParameter("username");
        String password = request.getParameter("password");

        response.setContentType("text/html; charset=UTF-8");
        PrintWriter out = response.getWriter();
        out.println("<html><body>");

        // Simple authentication check (use hashed passwords in real code!)
        if ("admin".equals(username) && "password123".equals(password)) {
            // Store user in session (persists across requests)
            HttpSession session = request.getSession();
            session.setAttribute("loggedInUser", username);
            out.println("<h2>Login successful! Welcome, " + username + "!</h2>");
        } else {
            out.println("<h2>Login failed! Invalid username or password.</h2>");
            out.println("<a href='/login.html'>Try again</a>");
        }

        out.println("</body></html>");
    }

    // ================================================================
    // LIFECYCLE METHOD 3: destroy() -- called ONCE when servlet unloads
    // ================================================================
    @Override
    public void destroy() {
        System.out.println("[SERVLET] destroy() called -- releasing resources.");
        // Close DB connections, thread pools, file handles here
        super.destroy();
    }
}

// ================================================================
// CORRESPONDING HTML FORM (login.html) to trigger doPost()
// ================================================================
/*
<html>
<body>
  <h2>Student Login</h2>
  <form action="/hello" method="post">
    Username: <input type="text"     name="username"><br>
    Password: <input type="password" name="password"><br>
    <input type="submit" value="Login">
  </form>
</body>
</html>
*/
""",
    lang="java",
)

pn.section("Servlet Request and Response Objects")
pn.info_table(
    ["Object / Method", "Description"],
    [
        [
            "HttpServletRequest request",
            "Represents the incoming HTTP request. Provides access to parameters, headers, session, and body.",
        ],
        [
            "request.getParameter(name)",
            "Returns query string or form body parameter value as String. Returns null if not present.",
        ],
        [
            "request.getParameterMap()",
            "Returns all parameters as Map<String, String[]>.",
        ],
        [
            "request.getSession()",
            "Returns the HttpSession associated with this client (creates one if none exists).",
        ],
        [
            "request.getHeader(name)",
            "Returns a specific HTTP request header value (e.g., User-Agent, Content-Type).",
        ],
        [
            "request.getMethod()",
            "Returns HTTP method as String: 'GET', 'POST', 'PUT', 'DELETE', etc.",
        ],
        [
            "request.getRequestURI()",
            "Returns the URL path after the host (e.g., /hello?name=Rahul).",
        ],
        [
            "HttpServletResponse response",
            "Represents the outgoing HTTP response being built for the client.",
        ],
        [
            "response.setContentType(mime)",
            "Sets the MIME type of the response (e.g., 'text/html', 'application/json').",
        ],
        [
            "response.setStatus(code)",
            "Sets the HTTP status code (200 OK, 404 Not Found, 500 Internal Server Error).",
        ],
        [
            "response.getWriter()",
            "Returns a PrintWriter for writing text response body.",
        ],
        [
            "response.getOutputStream()",
            "Returns a ServletOutputStream for writing binary response (images, PDFs).",
        ],
        [
            "response.sendRedirect(url)",
            "Sends HTTP 302 redirect to the client, causing browser to request a new URL.",
        ],
        [
            "response.addCookie(cookie)",
            "Adds a cookie to the response to be stored on the client.",
        ],
    ],
)

pn.section("web.xml -- Servlet Deployment Descriptor (Traditional)")
pn.code_block(
    """
<!-- web.xml -- Place in WEB-INF/ directory of the web application -->
<!-- This is the traditional (pre-Servlet-3.0) way to configure servlets -->
<!-- With Servlet 3.0+, @WebServlet annotation replaces this file -->

<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="http://java.sun.com/xml/ns/javaee" version="3.0">

    <!-- Servlet declaration -->
    <servlet>
        <servlet-name>HelloServlet</servlet-name>
        <servlet-class>HelloServlet</servlet-class>
        <!-- Initialization parameters read by init() via getInitParameter() -->
        <init-param>
            <param-name>dbUrl</param-name>
            <param-value>jdbc:mysql://localhost/mydb</param-value>
        </init-param>
        <!-- load-on-startup: positive integer means load at server startup -->
        <load-on-startup>1</load-on-startup>
    </servlet>

    <!-- URL mapping: requests to /hello are dispatched to HelloServlet -->
    <servlet-mapping>
        <servlet-name>HelloServlet</servlet-name>
        <url-pattern>/hello</url-pattern>
    </servlet-mapping>

    <!-- Welcome files shown when root URL is accessed -->
    <welcome-file-list>
        <welcome-file>index.html</welcome-file>
        <welcome-file>index.jsp</welcome-file>
    </welcome-file-list>

</web-app>

<!-- DEPLOYMENT STRUCTURE:
     WebApp/
       |-- WEB-INF/
       |     |-- web.xml              (deployment descriptor)
       |     |-- classes/             (compiled .class files)
       |     |     |-- HelloServlet.class
       |     |-- lib/                 (JAR dependencies)
       |-- index.html
       |-- login.html
-->
""",
    lang="java",
)

pn.section("Servlet Architecture Diagram")
net_servlet = pd.NetworkDiagram(
    width=pn.CW,
    height=260,
    theme=diag_theme,
    caption="Fig 4.5: Servlet Architecture -- browser sends HTTP request, container dispatches to servlet",
)
net_servlet.node("browser", "Web Browser\n(Client)", x=60, y=130, kind="host")
net_servlet.node("http", "HTTP Request\n(GET/POST)", x=170, y=130, kind="generic")
net_servlet.node(
    "container", "Servlet Container\n(Tomcat)", x=290, y=130, kind="server"
)
net_servlet.node(
    "servlet", "HelloServlet\n(doGet/doPost)", x=400, y=80, kind="database"
)
net_servlet.node("db", "Database\n(JDBC/MySQL)", x=400, y=185, kind="database")
net_servlet.node("response", "HTTP Response\n(HTML/JSON)", x=170, y=50, kind="storage")

net_servlet.link("browser", "http", label="sends request", bidirectional=False)
net_servlet.link("http", "container", label="routes to", bidirectional=False)
net_servlet.link("container", "servlet", label="init/service", bidirectional=False)
net_servlet.link("servlet", "db", label="JDBC query", bidirectional=True)
net_servlet.link("servlet", "response", label="generates HTML", bidirectional=False)
net_servlet.link("response", "browser", label="sends back", bidirectional=False)
pn.story.extend(net_servlet.as_flowable())
pn.br()

# =============================================================================
#  4.12  EXAM QUESTIONS & ANSWERS
# =============================================================================
pn.part_box("UNIT IV -- EXAM QUESTIONS & DETAILED ANSWERS")
pn.chap_box("4.12  Previous-Year Style Exam Questions")

pn.section("2-Mark Questions (Short Answer)")

pn.highlight(
    "<b>Q1. What is AWT? Which package does it belong to?</b><br/>"
    "A: AWT (Abstract Window Toolkit) is Java's original GUI toolkit for creating "
    "platform-independent graphical user interfaces. It is in the <code>java.awt</code> package. "
    "AWT provides classes for windows, buttons, text fields, menus, layout managers, "
    "graphics, and event handling. AWT components are heavyweight -- each wraps a native OS widget."
)

pn.highlight(
    "<b>Q2. What is the difference between AWT and Swing?</b><br/>"
    "A: AWT is in java.awt; components are heavyweight (native OS widgets). "
    "Swing is in javax.swing; components are lightweight (drawn by Java 2D). "
    "Swing has more components (JTable, JTree, JTabbedPane), supports pluggable Look and Feel, "
    "and is consistent across platforms. AWT components match the OS look exactly. "
    "Swing components are prefixed with 'J': JButton instead of Button."
)

pn.highlight(
    "<b>Q3. What is a Frame? How do you create one?</b><br/>"
    "A: Frame (java.awt.Frame) is a top-level AWT container with a title bar, "
    "minimize/maximize/close buttons, and an optional menu bar. "
    "Create: <code>Frame f = new Frame('Title');</code> "
    "Then: <code>f.setSize(400, 300); f.setVisible(true);</code> "
    "Must handle window close: <code>f.addWindowListener(new WindowAdapter() { "
    "public void windowClosing(WindowEvent e) { f.dispose(); System.exit(0); } });</code>"
)

pn.highlight(
    "<b>Q4. Explain the difference between FlowLayout and BorderLayout.</b><br/>"
    "A: FlowLayout places components left-to-right and wraps to the next row when the "
    "row is full (like words in a paragraph). It is the default layout for Panel. "
    "BorderLayout divides the container into 5 regions: NORTH, SOUTH, EAST, WEST, CENTER. "
    "Only one component per region. CENTER gets all remaining space. "
    "BorderLayout is the default for Frame and Dialog."
)

pn.highlight(
    "<b>Q5. What is GridLayout? When is it useful?</b><br/>"
    "A: GridLayout arranges components in a grid of equal-sized cells. "
    "All cells are the same width and height regardless of component preferred size. "
    "Created with <code>new GridLayout(rows, cols, hgap, vgap)</code>. "
    "Useful when you need uniform-sized cells: calculator keypads, form label/field pairs, "
    "or icon grids. Components fill cells left-to-right, top-to-bottom."
)

pn.highlight(
    "<b>Q6. What is a MenuBar in AWT? Explain its structure.</b><br/>"
    "A: A MenuBar is the horizontal bar attached to a Frame's top edge via setMenuBar(). "
    "Structure: MenuBar contains Menu objects (File, Edit, Help). "
    "Each Menu contains MenuItem objects (New, Open, Save) and sub-menus. "
    "CheckboxMenuItem is a toggleable MenuItem. "
    "addSeparator() adds a horizontal line separator between items."
)

pn.highlight(
    "<b>Q7. What is a Servlet? How does it differ from an Applet?</b><br/>"
    "A: A Servlet is a Java class that runs on a web server and handles HTTP requests. "
    "An Applet runs on the client (browser) side. "
    "Servlet extends HttpServlet; Applet extends Applet. "
    "Servlet has no GUI -- it generates HTML text responses; Applet displays graphics. "
    "Servlet is server-side; Applet is client-side. "
    "Servlets are actively used; Applets are deprecated."
)

pn.highlight(
    "<b>Q8. What are the lifecycle methods of a Servlet?</b><br/>"
    "A: Three lifecycle methods managed by the container: "
    "(1) init(ServletConfig): Called ONCE when servlet loads. Initialize resources. "
    "(2) service(HttpServletRequest, HttpServletResponse): Called for EVERY request. "
    "Dispatches to doGet() or doPost() based on HTTP method. "
    "(3) destroy(): Called ONCE before servlet unloads. Release resources. "
    "Order: init() -> service() [multiple times] -> destroy()."
)

pn.highlight(
    "<b>Q9. What is the difference between doGet() and doPost() in a Servlet?</b><br/>"
    "A: doGet() handles HTTP GET requests -- parameters appear in URL query string "
    "(visible, bookmarkable, max ~2000 chars, not for sensitive data). "
    "doPost() handles HTTP POST requests -- parameters sent in request body "
    "(not visible in URL, no size limit, safe for passwords and large data). "
    "Both receive HttpServletRequest and HttpServletResponse objects."
)

pn.highlight(
    "<b>Q10. What is a Layout Manager? Why is it preferred over absolute positioning?</b><br/>"
    "A: A LayoutManager controls automatic positioning and sizing of components inside a Container. "
    "It is preferred over absolute positioning (setBounds) because it: "
    "adapts to different screen sizes and resolutions, "
    "adjusts when the window is resized, "
    "works correctly across different operating systems with different font metrics, "
    "and handles component preferred sizes automatically."
)

pn.section("5-Mark Questions (Explain with Code)")

pn.highlight(
    "<b>Q11. Explain the AWT Component hierarchy with a diagram.</b><br/>"
    "A: Root: java.lang.Object -> java.awt.Component (all UI elements) -> "
    "java.awt.Container (holds other components) -> java.awt.Window (top-level with no title) -> "
    "java.awt.Frame (has title, menu, close buttons) and java.awt.Dialog (secondary window). "
    "Also: Container -> Panel (simple container, Applet's parent). "
    "See Fig 4.1 for the complete UML hierarchy diagram."
)

pn.highlight(
    "<b>Q12. Write a Java program to create a Frame with buttons and handle button click events.</b><br/>"
    "A: Extend Frame; declare Button and Label fields; set layout (FlowLayout); "
    "create buttons; add ActionListener via addActionListener(); "
    "in actionPerformed() update the label text; add WindowAdapter for close; "
    "call setVisible(true). See ExtendFrameDemo in Section 4.4 for the full code."
)

pn.highlight(
    "<b>Q13. Write an AWT program demonstrating FlowLayout, BorderLayout, and GridLayout.</b><br/>"
    "A: (1) FlowLayout: panel.setLayout(new FlowLayout(FlowLayout.LEFT)); add buttons. "
    "(2) BorderLayout: frame.setLayout(new BorderLayout()); frame.add(component, BorderLayout.NORTH/SOUTH/EAST/WEST/CENTER). "
    "(3) GridLayout: panel.setLayout(new GridLayout(rows, cols)); add equal-sized cells. "
    "See LayoutDemo in Section 4.8 for a combined example."
)

pn.highlight(
    "<b>Q14. Explain AWT controls with code: Button, TextField, Checkbox, Choice, List.</b><br/>"
    "A: Button: new Button('label'); add ActionListener. "
    "TextField: new TextField(columns); getText(); setText(). "
    "Checkbox: new Checkbox('label', state); getState(); ItemListener. "
    "CheckboxGroup: groups Checkboxes into radio buttons; getSelectedCheckbox(). "
    "Choice: new Choice(); add(item); getSelectedItem(); ItemListener. "
    "List: new List(rows, multiSelect); add(item); getSelectedItems(). "
    "See AWTControlsDemo in Section 4.7 for the full demo."
)

pn.highlight(
    "<b>Q15. Write a Servlet that handles a student login form.</b><br/>"
    "A: HTML form with action='/login' method='post' containing username and password fields. "
    "Servlet extends HttpServlet; doPost() reads request.getParameter('username') and 'password'. "
    "Check credentials; if valid: create session with request.getSession(); "
    "response.getWriter() prints success HTML; else prints failure HTML. "
    "See HelloServlet Section 4.11 for the complete code including web.xml."
)

pn.section("10-Mark Questions (Detailed Programs)")

pn.highlight(
    "<b>Q16. Write a complete AWT application for a Student Registration Form with "
    "at least 6 different controls, layout managers, and event handling.</b><br/>"
    "A: Use BorderLayout for Frame. NORTH: Title Label. "
    "CENTER: GridLayout Panel with Label+TextField for Name/Roll/Email, "
    "CheckboxGroup for Gender (Male/Female), Choice for Branch, "
    "List for subjects (multi-select), Checkbox for Hostel accommodation. "
    "SOUTH: FlowLayout Panel with Submit and Reset buttons. "
    "ActionListener: Submit reads all fields, Reset clears them. "
    "WindowAdapter for close. See AWTControlsDemo in Section 4.7."
)

pn.highlight(
    "<b>Q17. Write an AWT program to create a Menu Bar with File, Edit, and View menus. "
    "Add items including CheckboxMenuItem and submenus. Handle all menu events.</b><br/>"
    "A: Create MenuBar; add Menu('File'), Menu('Edit'), Menu('View'). "
    "File: New, Open, Save, separator, Exit. Edit: Cut, Copy, Paste. "
    "View: CheckboxMenuItem('Word Wrap'), Menu('Zoom') submenu. "
    "setMenuBar(menuBar) on Frame. ActionListener for MenuItems; "
    "ItemListener for CheckboxMenuItem. See MenuDemo in Section 4.9."
)

pn.highlight(
    "<b>Q18. Compare Swing and AWT. Write a Swing program showing JFrame, JButton, "
    "JLabel, JTextField, and JTable.</b><br/>"
    "A: AWT = heavyweight, OS native, java.awt. "
    "Swing = lightweight, pure Java, javax.swing, pluggable L&F, more components. "
    "Swing JFrame: setDefaultCloseOperation(EXIT_ON_CLOSE) instead of WindowAdapter. "
    "Add components to getContentPane(). JTable(data[][], colNames[]) wrapped in JScrollPane. "
    "SwingUtilities.invokeLater() for thread safety. See SwingComponentsDemo Section 4.10."
)

pn.highlight(
    "<b>Q19. Explain the Servlet lifecycle and write a Servlet to handle HTTP GET and POST "
    "requests. Include the web.xml configuration.</b><br/>"
    "A: Lifecycle: init() [once] -> service() [per request -> doGet/doPost] -> destroy() [once]. "
    "doGet(): read URL params via request.getParameter(); write HTML via response.getWriter(). "
    "doPost(): read form body params; set session attribute; redirect or display result. "
    "web.xml: servlet-name, servlet-class, url-pattern; or use @WebServlet('/path') annotation. "
    "See HelloServlet Section 4.11 for complete code + web.xml."
)

pn.highlight(
    "<b>Q20. Write an AWT program demonstrating all four event handling approaches: "
    "named inner class, anonymous inner class, lambda, and self-implementing listener. "
    "Use Button, TextField, and Label components.</b><br/>"
    "A: (1) Named inner class: class ButtonHandler implements ActionListener { actionPerformed... }. "
    "(2) Anonymous inner class: btnX.addActionListener(new ActionListener() { actionPerformed... }). "
    "(3) Lambda (Java 8+): btnX.addActionListener(e -> lblResult.setText(txtInput.getText())). "
    "(4) Self-implementing: class MyFrame extends Frame implements ActionListener { actionPerformed... }. "
    "See all four methods in Section 4.6 with complete code."
)

pn.section("Quick Revision Summary Table")
pn.info_table(
    ["Topic", "Key Exam Points"],
    [
        [
            "AWT package",
            "java.awt -- Abstract Window Toolkit. Heavyweight (native OS widgets).",
        ],
        [
            "Swing package",
            "javax.swing -- Lightweight, pure Java. Prefix J. JFrame, JButton, JLabel.",
        ],
        [
            "Component hierarchy",
            "Object -> Component -> Container -> Window -> Frame. Panel -> Applet.",
        ],
        [
            "Frame methods",
            "setSize(), setVisible(true), setTitle(), setMenuBar(), setLayout(), pack(), dispose(), setLocationRelativeTo(null).",
        ],
        [
            "FlowLayout",
            "Default for Panel. Left-to-right, wraps rows. new FlowLayout(align, hgap, vgap).",
        ],
        [
            "BorderLayout",
            "Default for Frame. 5 regions: NORTH,SOUTH,EAST,WEST,CENTER. add(comp, BorderLayout.X).",
        ],
        [
            "GridLayout",
            "Equal-size cells. new GridLayout(rows, cols, hgap, vgap). Calculator/form grids.",
        ],
        [
            "WindowAdapter",
            "Extends WindowAdapter, override windowClosing() to call dispose() + System.exit(0).",
        ],
        [
            "ActionListener",
            "Handles button clicks. actionPerformed(ActionEvent e). e.getActionCommand() for label.",
        ],
        ["Button", "new Button('label'); addActionListener(); getLabel(); setLabel()."],
        [
            "TextField",
            "new TextField(columns); getText(); setText(); setEchoChar('*') for password.",
        ],
        [
            "Checkbox + Group",
            "new CheckboxGroup(); new Checkbox('Male', group, true); getSelectedCheckbox().getLabel().",
        ],
        [
            "Choice",
            "new Choice(); add(item); getSelectedItem(); getSelectedIndex(); addItemListener().",
        ],
        [
            "List",
            "new List(rows, multiSelect=true); add(); getSelectedItems() returns String[].",
        ],
        [
            "MenuBar structure",
            "setMenuBar(new MenuBar()) on Frame. MenuBar -> Menu -> MenuItem. addSeparator(). CheckboxMenuItem uses ItemListener.",
        ],
        [
            "Servlet lifecycle",
            "init() [once] -> service()/doGet()/doPost() [per request] -> destroy() [once].",
        ],
        [
            "doGet vs doPost",
            "doGet: params in URL, visible, bookmarkable. doPost: params in body, hidden, no size limit.",
        ],
        [
            "HttpServletRequest",
            "request.getParameter(name), getSession(), getMethod(), getHeader(name).",
        ],
        [
            "HttpServletResponse",
            "response.setContentType(), getWriter(), setStatus(), sendRedirect().",
        ],
        [
            "web.xml role",
            "Deployment descriptor: maps URL patterns to servlet classes. Replaced by @WebServlet in Servlet 3.0+.",
        ],
        [
            "Swing JFrame close",
            "setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE) -- replaces WindowAdapter.",
        ],
        [
            "SwingUtilities rule",
            "Always create/modify Swing UI on EDT: SwingUtilities.invokeLater(() -> new MyFrame()).",
        ],
    ],
)

pn.note(
    "For exam: Always show the import statements in AWT programs. "
    "Always add a WindowAdapter/WindowListener to handle the close button. "
    "For Servlet questions, always show the HTML form AND the Servlet class. "
    "Exam questions frequently ask for programs combining multiple controls with layout managers -- "
    "practice writing a complete Frame extending class with constructor-built UI."
)

# =============================================================================
#  BUILD DOCUMENT
# =============================================================================
pn.build_doc("Java_Unit4_Notes.pdf")
print("Generated: Java_Unit4_Notes.pdf")
