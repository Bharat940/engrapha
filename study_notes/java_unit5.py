"""
Java Programming (IT408) -- Unit V Notes
UIT-RGPV (Autonomous) Bhopal | Semester IV
Complete exam notes: Event Handling (Delegation Model) and JDBC.
Run: python java_unit5_notes.py
Output: Java_Unit5_Notes.pdf
"""

from __future__ import annotations

import paperforge_notes as pn
import paperforge_diagrams as pd

# =============================================================================
#  THEME & GLOBAL FOOTER SETUP
#  Using OCEAN_DARK -- teal accent on deep navy background
#  Distinct from Unit I (Catppuccin Mocha), II (Midnight Dark),
#  III (Forest Dark), IV (Sunset Dark)
# =============================================================================
pn.set_story([])
pn.set_theme(pn.OCEAN_DARK)

pn.set_global_footer(
    left="Java Programming (IT408) -- Unit V",
    right="UIT-RGPV (Autonomous) Bhopal",
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
    "JAVA PROGRAMMING",
    "Unit V -- Event Handling & JDBC Database Connectivity",
)
pn.cover_subtitle(
    [
        "Subject Code: IT408  |  UIT-RGPV (Autonomous) Bhopal  |  Semester IV",
        "Complete Exam Notes: Delegation Event Model, Event Sources, Listeners,",
        "Mouse & Key Events, JDBC Architecture, Drivers, ResultSet, and Remote DB",
    ]
)
pn.sp(10)
pn.rule(pn.get_theme().rl(pn.get_theme().accent), 1.5)
pn.sp(8)

pn.info_table(
    ["Section", "Syllabus Topics Covered"],
    [
        [
            "5.1 Event Handling Overview",
            "Two mechanisms: old (action-based) vs new (delegation model)",
        ],
        [
            "5.2 The Delegation Event Model",
            "Event source, event object, listener interface, registration",
        ],
        [
            "5.3 Events & Event Classes",
            "EventObject hierarchy, ActionEvent, MouseEvent, KeyEvent, WindowEvent",
        ],
        [
            "5.4 Event Sources",
            "Components that generate events: Button, TextField, Frame, Canvas",
        ],
        [
            "5.5 Event Listeners",
            "Listener interfaces, Adapter classes, single vs multi-method interfaces",
        ],
        [
            "5.6 Mouse Events",
            "MouseEvent, MouseListener, MouseMotionListener -- all methods with code",
        ],
        [
            "5.7 Key Events",
            "KeyEvent, KeyListener -- keyPressed, keyReleased, keyTyped with VK codes",
        ],
        [
            "5.8 Other Event Classes",
            "ItemEvent, TextEvent, AdjustmentEvent, FocusEvent, ComponentEvent",
        ],
        [
            "5.9 JDBC Introduction",
            "JDBC-ODBC bridge, connectivity model, types of drivers",
        ],
        [
            "5.10 JDBC Architecture",
            "DriverManager, Connection, Statement, ResultSet, PreparedStatement",
        ],
        [
            "5.11 Navigating ResultSet",
            "next(), previous(), first(), last(), absolute(), relative(), getXxx()",
        ],
        [
            "5.12 JDBC Exceptions",
            "SQLException, SQLWarning, BatchUpdateException -- handling and getMessage()",
        ],
        [
            "5.13 Remote Database",
            "Connecting to remote DB, connection strings, SSL, connection pooling",
        ],
        [
            "5.14 Exam Questions",
            "20+ exam questions with detailed answers covering all Unit V topics",
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
pn.part_box("UNIT V -- EVENT HANDLING & JDBC DATABASE CONNECTIVITY")

# =============================================================================
#  5.1  EVENT HANDLING OVERVIEW
# =============================================================================
pn.chap_box("5.1  Event Handling Overview")
pn.section("What is Event Handling?")
pn.definition(
    "<b>Event Handling:</b> The mechanism by which a Java program detects and responds "
    "to user actions or system notifications -- such as mouse clicks, key presses, "
    "button activations, window operations, or scrollbar adjustments. "
    "Without event handling, a GUI program would be a static display with no interactivity. "
    "Java AWT and Swing use an <b>event-driven programming model</b> where execution is "
    "driven by events rather than top-to-bottom sequential flow."
)

pn.section("Two Event Handling Mechanisms in Java")
pn.info_table(
    ["Mechanism", "Java Version", "How it Works", "Drawbacks / Why Replaced"],
    [
        [
            "Old (Inheritance-based) Model",
            "Java 1.0",
            "Components extended and overrode action() and handleEvent() methods inside the component class itself. The component both generated and handled events.",
            "Violated separation of concerns. Required subclassing AWT components. Inefficient -- ALL events bubbled up even if unhandled. Unmaintainable for large GUIs.",
        ],
        [
            "New (Delegation) Model",
            "Java 1.1+",
            "Events are generated by a source component and DELEGATED to separate listener objects that are registered with the source. Source and handler are cleanly separated.",
            "None -- this is the current and correct model used in all modern Java GUI programming (AWT, Swing, JavaFX all use delegation).",
        ],
    ],
)

pn.code_block(
    """
// OLD Model (Java 1.0) -- DO NOT USE, shown for context only
// The component itself handled its own events via overriding
public class OldStyleFrame extends java.awt.Frame {
    @Override
    public boolean action(java.awt.Event e, Object arg) {
        // All events came here regardless of source or type
        // Had to manually check event.target and arg to determine what happened
        if (e.target instanceof java.awt.Button) {
            System.out.println("Button: " + arg);
        }
        return true;  // event consumed
    }
}

// NEW Delegation Model (Java 1.1+) -- CORRECT approach
// Event source (Button) delegates to a separate listener object
import java.awt.*;
import java.awt.event.*;

Button btn = new Button("Click Me");
btn.addActionListener(new ActionListener() {    // listener registered with source
    public void actionPerformed(ActionEvent e) { // called when event occurs
        System.out.println("Button clicked: " + e.getActionCommand());
    }
});
""",
    lang="java",
)
pn.br()

# =============================================================================
#  5.2  THE DELEGATION EVENT MODEL
# =============================================================================
pn.chap_box("5.2  The Delegation Event Model")
pn.section("Three Pillars of the Delegation Model")
pn.definition(
    "<b>Delegation Event Model:</b> The event handling architecture introduced in "
    "Java 1.1 and used in all modern Java GUI toolkits. It is built on three core concepts: "
    "(1) <b>Event Source:</b> The component that generates (fires) an event when the user interacts with it. "
    "(2) <b>Event Object:</b> An object created by the source that encapsulates all information about the event (type, timestamp, source component, state). "
    "(3) <b>Event Listener:</b> An object (implementing a listener interface) that is registered with the source and whose callback method is invoked when the event occurs."
)

pn.info_table(
    ["Concept", "Description", "Example"],
    [
        [
            "Event Source",
            "The AWT/Swing component that generates events. It maintains a list of registered listeners.",
            "Button, TextField, Frame, Canvas, Scrollbar",
        ],
        [
            "Event Object",
            "An instance of a class extending java.util.EventObject. Contains: source component, event type, timestamp, and event-specific data.",
            "ActionEvent, MouseEvent, KeyEvent, WindowEvent, ItemEvent",
        ],
        [
            "Event Listener",
            "An interface defining callback methods. Classes implement the interface and provide method bodies.",
            "ActionListener, MouseListener, KeyListener, WindowListener",
        ],
        [
            "Registration",
            "Calling addXxxListener(listener) on the source component. The source stores the listener reference.",
            "button.addActionListener(myListener)",
        ],
        [
            "Dispatch",
            "When the event occurs, the AWT Event Dispatch Thread calls the appropriate listener method.",
            "actionPerformed(e), mouseClicked(e), keyPressed(e)",
        ],
    ],
)

pn.section("Step-by-Step Event Flow")
pn.bullet(
    [
        "<b>Step 1 (User Action):</b> User clicks a Button. The OS detects the mouse click and sends it to the JVM.",
        "<b>Step 2 (Event Creation):</b> The AWT event thread creates an ActionEvent object containing the source (Button), action command (button label), and timestamp.",
        "<b>Step 3 (Dispatch):</b> The AWT event thread looks up the registered ActionListeners for this Button.",
        "<b>Step 4 (Callback):</b> For each registered ActionListener, the thread calls listener.actionPerformed(event).",
        "<b>Step 5 (Handler Executes):</b> Your actionPerformed() method body runs, updating the UI or performing business logic.",
        "<b>Step 6 (Return):</b> Control returns to the AWT event thread, which processes the next event in the queue.",
    ]
)

# Sequence diagram of the delegation flow
seq_del = pd.SequenceDiagram(
    width=pn.CW,
    height=300,
    theme=diag_theme,
    caption="Fig 5.1: Delegation Event Model -- user action to listener callback sequence",
)
seq_del.actor("user", "User")
seq_del.actor("button", "Button\n(Source)")
seq_del.actor("awtthread", "AWT Event\nDispatch Thread")
seq_del.actor("listener", "ActionListener\n(Handler)")

seq_del.message("user", "button", "mouse click", arrow="solid")
seq_del.message("button", "awtthread", "create ActionEvent", arrow="solid")
seq_del.activate("awtthread")
seq_del.divider("loop [for each registered listener]")
seq_del.message("awtthread", "awtthread", "look up listener", arrow="solid")
seq_del.message("awtthread", "listener", "actionPerformed(event)", arrow="solid")
seq_del.activate("listener")
seq_del.message("listener", "listener", "update\nlabel /\ndo logic", arrow="solid")
seq_del.message("listener", "awtthread", "return (done)", arrow="dashed")
seq_del.deactivate("listener")
seq_del.divider("end loop")
seq_del.deactivate("awtthread")
pn.story.extend(seq_del.as_flowable())

pn.section("Complete Delegation Model Example")
pn.code_block(
    """
// DelegationModelDemo.java -- shows all three roles: source, event, listener
import java.awt.*;
import java.awt.event.*;

// ---- ROLE 3: The Listener -- a separate class from the Frame ----
class MyButtonListener implements ActionListener {
    private Label outputLabel;              // reference to the label to update

    MyButtonListener(Label lbl) {
        this.outputLabel = lbl;             // injected via constructor
    }

    // actionPerformed() is the CALLBACK invoked by AWT when button is clicked
    @Override
    public void actionPerformed(ActionEvent e) {
        // ActionEvent carries: source, action command, modifiers, timestamp
        String command = e.getActionCommand();    // button's label text
        long   when    = e.getWhen();             // millisecond timestamp
        outputLabel.setText("'" + command + "' clicked at ms=" + when);
    }
}

// ---- ROLE 1: The Source Container ----
public class DelegationModelDemo extends Frame {

    public DelegationModelDemo() {
        super("Delegation Model Demo");
        setSize(450, 180);
        setLayout(new FlowLayout(FlowLayout.CENTER, 15, 20));

        // ---- Event Source: Button ----
        Button btnSave   = new Button("Save");
        Button btnDelete = new Button("Delete");
        Button btnCancel = new Button("Cancel");
        Label  lblResult = new Label("No button pressed yet.", Label.CENTER);
        lblResult.setPreferredSize(new Dimension(400, 25));

        // ---- ROLE 3: Create the listener objects ----
        MyButtonListener listener = new MyButtonListener(lblResult);

        // ---- REGISTRATION: addActionListener connects source to listener ----
        btnSave.addActionListener(listener);    // same listener handles all three
        btnDelete.addActionListener(listener);
        btnCancel.addActionListener(listener);  // delegation: button delegates to listener

        add(btnSave); add(btnDelete); add(btnCancel); add(lblResult);

        addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent e) { dispose(); System.exit(0); }
        });
        setVisible(true);
    }

    public static void main(String[] args) { new DelegationModelDemo(); }
}
""",
    lang="java",
)
pn.br()

# =============================================================================
#  5.3  EVENTS AND EVENT CLASSES
# =============================================================================
pn.chap_box("5.3  Events and Event Classes")
pn.section("The Event Class Hierarchy")
pn.body(
    "All Java event objects inherit from <code>java.util.EventObject</code>, "
    "which stores the event source and provides <code>getSource()</code>. "
    "AWT events further extend <code>java.awt.AWTEvent</code>, "
    "which adds an event ID integer identifying the specific event type."
)

# Class diagram showing event hierarchy
cd_events = pd.ClassDiagram(
    width=pn.CW,
    height=270,
    theme=diag_theme,
    caption="Fig 5.2: Java AWT Event class hierarchy -- from EventObject to specific event types",
    class_w=140,
)
cd_events.uml_class(
    "EventObject",
    "java.util.EventObject",
    methods=["+ getSource(): Object"],
)
cd_events.uml_class(
    "AWTEvent",
    "java.awt.AWTEvent",
    methods=["+ getID(): int", "+ paramString(): String"],
)
cd_events.uml_class(
    "ComponentEvent",
    "ComponentEvent",
    methods=["+ getComponent(): Component"],
)
cd_events.uml_class(
    "ActionEvent",
    "ActionEvent",
    methods=[
        "+ getActionCommand(): String",
        "+ getModifiers(): int",
        "+ getWhen(): long",
    ],
)
cd_events.uml_class(
    "ItemEvent",
    "ItemEvent",
    methods=["+ getItem(): Object", "+ getStateChange(): int"],
)
cd_events.uml_class(
    "AdjustEvent",
    "AdjustmentEvent",
    methods=["+ getValue(): int", "+ getAdjustmentType(): int"],
)
cd_events.uml_class(
    "InputEvent",
    "InputEvent",
    methods=["+ getModifiers(): int", "+ getWhen(): long", "+ isShiftDown(): boolean"],
)
cd_events.uml_class(
    "MouseEvent",
    "MouseEvent",
    methods=[
        "+ getX(): int",
        "+ getY(): int",
        "+ getClickCount(): int",
        "+ getButton(): int",
    ],
)
cd_events.uml_class(
    "KeyEvent",
    "KeyEvent",
    methods=["+ getKeyCode(): int", "+ getKeyChar(): char", "+ getKeyText(code)"],
)
cd_events.relate("AWTEvent", "EventObject", kind="inheritance")
cd_events.relate("ComponentEvent", "AWTEvent", kind="inheritance")
cd_events.relate("ActionEvent", "AWTEvent", kind="inheritance")
cd_events.relate("ItemEvent", "AWTEvent", kind="inheritance")
cd_events.relate("AdjustEvent", "AWTEvent", kind="inheritance")
cd_events.relate("InputEvent", "ComponentEvent", kind="inheritance")
cd_events.relate("MouseEvent", "InputEvent", kind="inheritance")
cd_events.relate("KeyEvent", "InputEvent", kind="inheritance")
pn.story.extend(cd_events.as_flowable())

pn.section("Key Event Classes and Their Information")
pn.info_table(
    ["Event Class", "Package", "Generated By", "Key Methods"],
    [
        [
            "ActionEvent",
            "java.awt.event",
            "Button click, MenuItem select, TextField Enter key, List double-click",
            "getActionCommand(), getModifiers(), getWhen(), getSource()",
        ],
        [
            "MouseEvent",
            "java.awt.event",
            "Mouse click, press, release, enter, exit, move, drag",
            "getX(), getY(), getClickCount(), getButton(), getPoint(), isPopupTrigger()",
        ],
        [
            "KeyEvent",
            "java.awt.event",
            "Key press, release, type on keyboard-focused component",
            "getKeyCode(), getKeyChar(), getKeyText(), isShiftDown(), isControlDown(), isAltDown()",
        ],
        [
            "WindowEvent",
            "java.awt.event",
            "Frame open, close, minimize, maximize, activate, deactivate",
            "getWindow(), getNewState(), getOldState()",
        ],
        [
            "ItemEvent",
            "java.awt.event",
            "Checkbox toggle, Choice/List selection change",
            "getItem(), getItemSelectable(), getStateChange() (SELECTED/DESELECTED)",
        ],
        [
            "TextEvent",
            "java.awt.event",
            "TextField or TextArea content change (every character)",
            "getSource() (cast to TextComponent to call getText())",
        ],
        [
            "AdjustmentEvent",
            "java.awt.event",
            "Scrollbar position change",
            "getValue(), getAdjustmentType() (UNIT_INCREMENT, TRACK, etc.)",
        ],
        [
            "FocusEvent",
            "java.awt.event",
            "Component gains or loses keyboard focus",
            "isTemporary(), getOppositeComponent()",
        ],
        [
            "ComponentEvent",
            "java.awt.event",
            "Component moved, resized, shown, hidden",
            "getComponent()",
        ],
    ],
)
pn.br()

# =============================================================================
#  5.4  EVENT SOURCES
# =============================================================================
pn.chap_box("5.4  Event Sources")
pn.section("What is an Event Source?")
pn.definition(
    "<b>Event Source:</b> Any AWT or Swing component that can generate events. "
    "A source maintains a list of registered listeners and fires event objects "
    "to all registered listeners when the triggering action occurs. "
    "Every source provides <code>addXxxListener()</code> and <code>removeXxxListener()</code> "
    "methods for each type of event it can fire."
)

pn.info_table(
    ["Event Source", "Events It Generates", "Registration Method"],
    [
        ["Button", "ActionEvent (on click)", "addActionListener(ActionListener l)"],
        [
            "TextField",
            "ActionEvent (Enter key), TextEvent (content change)",
            "addActionListener(), addTextListener()",
        ],
        ["TextArea", "TextEvent (content change)", "addTextListener(TextListener l)"],
        ["Checkbox", "ItemEvent (state toggle)", "addItemListener(ItemListener l)"],
        ["Choice", "ItemEvent (selection change)", "addItemListener(ItemListener l)"],
        [
            "List",
            "ActionEvent (double-click), ItemEvent (single-click selection)",
            "addActionListener(), addItemListener()",
        ],
        [
            "Scrollbar",
            "AdjustmentEvent (position change)",
            "addAdjustmentListener(AdjustmentListener l)",
        ],
        [
            "Frame / Window",
            "WindowEvent (open/close/minimize/restore)",
            "addWindowListener(WindowListener l)",
        ],
        [
            "Any Component",
            "MouseEvent (click/move/drag)",
            "addMouseListener(), addMouseMotionListener()",
        ],
        [
            "Any Component",
            "KeyEvent (press/release/type)",
            "addKeyListener(KeyListener l)",
        ],
        [
            "Any Component",
            "FocusEvent (gain/lose focus)",
            "addFocusListener(FocusListener l)",
        ],
        [
            "Any Component",
            "ComponentEvent (move/resize/show/hide)",
            "addComponentListener(ComponentListener l)",
        ],
    ],
)
pn.br()

# =============================================================================
#  5.5  EVENT LISTENERS AND ADAPTERS
# =============================================================================
pn.chap_box("5.5  Event Listeners and Adapter Classes")
pn.section("Listener Interfaces")
pn.definition(
    "<b>Event Listener:</b> An interface that declares one or more callback methods "
    "that the AWT runtime calls when the corresponding event occurs. "
    "To handle events, a class must implement the listener interface and provide "
    "bodies for ALL declared methods. The class instance is then registered with "
    "the event source using <code>addXxxListener()</code>."
)

pn.info_table(
    ["Listener Interface", "Methods (callbacks)", "Adapter Class"],
    [
        [
            "ActionListener",
            "actionPerformed(ActionEvent e)",
            "None (1 method -- no adapter needed)",
        ],
        [
            "MouseListener",
            "mouseClicked, mousePressed, mouseReleased, mouseEntered, mouseExited (5 methods)",
            "MouseAdapter",
        ],
        [
            "MouseMotionListener",
            "mouseMoved, mouseDragged (2 methods)",
            "MouseMotionAdapter",
        ],
        ["KeyListener", "keyPressed, keyReleased, keyTyped (3 methods)", "KeyAdapter"],
        [
            "WindowListener",
            "windowOpened, windowClosing, windowClosed, windowIconified, windowDeiconified, windowActivated, windowDeactivated (7 methods)",
            "WindowAdapter",
        ],
        [
            "ItemListener",
            "itemStateChanged(ItemEvent e) (1 method)",
            "None (1 method -- no adapter needed)",
        ],
        [
            "TextListener",
            "textValueChanged(TextEvent e) (1 method)",
            "None (1 method -- no adapter needed)",
        ],
        [
            "AdjustmentListener",
            "adjustmentValueChanged(AdjustmentEvent e) (1 method)",
            "None (1 method -- no adapter needed)",
        ],
        ["FocusListener", "focusGained, focusLost (2 methods)", "FocusAdapter"],
        [
            "ComponentListener",
            "componentMoved, componentResized, componentShown, componentHidden (4 methods)",
            "ComponentAdapter",
        ],
    ],
)

pn.section("Why Adapter Classes Exist")
pn.definition(
    "<b>Adapter Class:</b> A convenience class that implements a listener interface "
    "with empty (no-op) method bodies for all methods. "
    "When a listener interface has multiple methods but you only need to handle one or two, "
    "you extend the Adapter class and override ONLY the methods you need "
    "-- instead of implementing all methods (most of which would be empty anyway). "
    "For example, <code>WindowAdapter</code> implements all 7 WindowListener methods "
    "with empty bodies. You extend it and override only <code>windowClosing()</code>."
)

pn.code_block(
    """
// PROBLEM: WindowListener requires ALL 7 methods -- tedious when you only need one
class MyWindowListener implements WindowListener {
    public void windowClosing(WindowEvent e)     { System.exit(0); }  // only this matters
    public void windowOpened(WindowEvent e)      {}  // forced empty implementations
    public void windowClosed(WindowEvent e)      {}
    public void windowIconified(WindowEvent e)   {}
    public void windowDeiconified(WindowEvent e) {}
    public void windowActivated(WindowEvent e)   {}
    public void windowDeactivated(WindowEvent e) {}
}

// SOLUTION: Use WindowAdapter -- extend and override only what you need
frame.addWindowListener(new WindowAdapter() {
    @Override
    public void windowClosing(WindowEvent e) {
        frame.dispose();
        System.exit(0);   // only override the one method you actually need
    }
});

// ANONYMOUS INNER CLASS example for MouseAdapter:
canvas.addMouseListener(new MouseAdapter() {
    @Override
    public void mouseClicked(MouseEvent e) {
        // Only handle click -- the other 4 MouseListener methods are inherited empty
        System.out.println("Clicked at: " + e.getX() + ", " + e.getY());
    }
    // mousePressed, mouseReleased, mouseEntered, mouseExited
    // are all inherited from MouseAdapter with empty bodies
});
""",
    lang="java",
)
pn.br()

# =============================================================================
#  5.6  MOUSE EVENTS
# =============================================================================
pn.chap_box("5.6  The Mouse Event Class")
pn.section("MouseEvent Class -- Complete Reference")
pn.definition(
    "<b>MouseEvent:</b> Represents a mouse action that occurred on a component. "
    "It extends <code>InputEvent</code> and carries the mouse coordinates, "
    "the button that was pressed, and the click count. "
    "Mouse events are split across TWO listener interfaces: "
    "<code>MouseListener</code> (click, press, release, enter, exit) and "
    "<code>MouseMotionListener</code> (move, drag)."
)

pn.info_table(
    ["MouseEvent Method", "Return Type", "Description"],
    [
        [
            "getX()",
            "int",
            "X coordinate of the mouse cursor in the component's coordinate space (pixels from left edge).",
        ],
        [
            "getY()",
            "int",
            "Y coordinate of the mouse cursor (pixels from top edge of component).",
        ],
        [
            "getPoint()",
            "Point",
            "Returns the (x, y) position as a java.awt.Point object.",
        ],
        [
            "getClickCount()",
            "int",
            "Number of consecutive mouse clicks in rapid succession. 2 = double-click.",
        ],
        [
            "getButton()",
            "int",
            "Which button was pressed: MouseEvent.BUTTON1 (left), BUTTON2 (middle), BUTTON3 (right).",
        ],
        [
            "isPopupTrigger()",
            "boolean",
            "True if this event is the platform-specific trigger for showing a popup menu (right-click on Windows/Linux).",
        ],
        [
            "isShiftDown()",
            "boolean",
            "True if Shift key was held when the mouse event occurred.",
        ],
        [
            "isControlDown()",
            "boolean",
            "True if Ctrl key was held when the mouse event occurred.",
        ],
        [
            "isAltDown()",
            "boolean",
            "True if Alt key was held when the mouse event occurred.",
        ],
        [
            "getModifiers()",
            "int",
            "Bitmask of all modifier keys and mouse buttons held during the event.",
        ],
        [
            "getSource()",
            "Object",
            "Inherited from EventObject. Returns the component that fired the event.",
        ],
    ],
)

pn.section("MouseListener Interface -- All Five Methods")
pn.info_table(
    ["MouseListener Method", "When Invoked"],
    [
        [
            "mouseClicked(MouseEvent e)",
            "Mouse button is pressed AND released over the same component (full click). NOT called for drags.",
        ],
        [
            "mousePressed(MouseEvent e)",
            "Mouse button is pressed DOWN (finger touches mouse button). Fires immediately on press.",
        ],
        [
            "mouseReleased(MouseEvent e)",
            "Mouse button is released (finger lifts). Fires even if mouse moved since press.",
        ],
        [
            "mouseEntered(MouseEvent e)",
            "Mouse cursor moves INTO the component's bounds from outside.",
        ],
        [
            "mouseExited(MouseEvent e)",
            "Mouse cursor moves OUT OF the component's bounds to outside.",
        ],
    ],
)

pn.section("MouseMotionListener Interface -- Two Methods")
pn.info_table(
    ["MouseMotionListener Method", "When Invoked"],
    [
        [
            "mouseMoved(MouseEvent e)",
            "Mouse cursor moves within the component WITHOUT any button pressed. Fires continuously.",
        ],
        [
            "mouseDragged(MouseEvent e)",
            "Mouse cursor moves within the component WITH a button pressed (drag gesture). Fires continuously during drag.",
        ],
    ],
)

pn.section("Complete Mouse Event Demo")
pn.code_block(
    """
// MouseEventDemo.java -- All mouse events demonstrated with visual feedback
import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;

public class MouseEventDemo extends Frame
        implements MouseListener, MouseMotionListener {

    // Fields to track mouse state
    int mouseX = 0, mouseY = 0;       // current cursor position
    int clickX = -1, clickY = -1;     // last click position
    String lastEvent = "Move the mouse...";
    boolean mouseInside = false;      // true when cursor is inside canvas area
    int clickCount = 0;
    ArrayList<int[]> clickPoints = new ArrayList<>();  // all click positions

    public MouseEventDemo() {
        super("Mouse Event Demo -- IT408 Unit V");
        setSize(550, 400);
        setBackground(Color.WHITE);

        // Register BOTH mouse listener interfaces on the Frame itself
        addMouseListener(this);
        addMouseMotionListener(this);

        addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent e) { dispose(); System.exit(0); }
        });
        setVisible(true);
    }

    // ---- Paint method draws the visual state ----
    @Override
    public void paint(Graphics g) {
        Insets ins = getInsets();
        int ox = ins.left + 5;
        int oy = ins.top  + 5;

        // Background indicator: green if mouse inside, light gray if outside
        g.setColor(mouseInside ? new Color(200, 255, 200) : new Color(240, 240, 240));
        g.fillRect(ox, oy, getWidth()-ins.left-ins.right-10, getHeight()-ins.top-ins.bottom-10);

        // Border
        g.setColor(Color.GRAY);
        g.drawRect(ox, oy, getWidth()-ins.left-ins.right-10, getHeight()-ins.top-ins.bottom-10);

        // Current event label
        g.setFont(new Font("Arial", Font.BOLD, 14));
        g.setColor(Color.DARK_GRAY);
        g.drawString("Event: " + lastEvent, ox+10, oy+30);

        // Mouse position readout
        g.setFont(new Font("Courier New", Font.PLAIN, 12));
        g.setColor(Color.BLUE);
        g.drawString("Mouse: X=" + mouseX + "  Y=" + mouseY, ox+10, oy+55);
        g.drawString("Total Clicks: " + clickCount, ox+10, oy+75);

        // Draw small crosshair at current position
        g.setColor(Color.RED);
        g.drawLine(mouseX-10, mouseY, mouseX+10, mouseY);
        g.drawLine(mouseX, mouseY-10, mouseX, mouseY+10);

        // Draw all previous click points as blue circles
        g.setColor(Color.BLUE);
        for (int[] p : clickPoints) {
            g.fillOval(p[0]-4, p[1]-4, 8, 8);
        }

        // Draw last click point larger in red
        if (clickX >= 0) {
            g.setColor(Color.RED);
            g.fillOval(clickX-6, clickY-6, 12, 12);
            g.setColor(Color.BLACK);
            g.drawString("(" + clickX + "," + clickY + ")", clickX+8, clickY-5);
        }
    }

    // ============ MouseListener: 5 callback methods ============
    @Override
    public void mouseClicked(MouseEvent e) {
        clickX = e.getX();
        clickY = e.getY();
        clickCount++;
        clickPoints.add(new int[]{clickX, clickY});
        lastEvent = "CLICKED (button=" + e.getButton() + ", clicks=" + e.getClickCount() + ")";
        // Detect double-click
        if (e.getClickCount() == 2) lastEvent = "DOUBLE-CLICK at (" + clickX + "," + clickY + ")";
        repaint();
    }

    @Override
    public void mousePressed(MouseEvent e) {
        lastEvent = "PRESSED (button=" + e.getButton() + ") at (" + e.getX() + "," + e.getY() + ")";
        repaint();
    }

    @Override
    public void mouseReleased(MouseEvent e) {
        lastEvent = "RELEASED at (" + e.getX() + "," + e.getY() + ")";
        repaint();
    }

    @Override
    public void mouseEntered(MouseEvent e) {
        mouseInside = true;
        lastEvent = "ENTERED the component";
        repaint();
    }

    @Override
    public void mouseExited(MouseEvent e) {
        mouseInside = false;
        lastEvent = "EXITED the component";
        repaint();
    }

    // ============ MouseMotionListener: 2 callback methods ============
    @Override
    public void mouseMoved(MouseEvent e) {
        mouseX = e.getX();
        mouseY = e.getY();
        lastEvent = "MOVED";
        repaint();
    }

    @Override
    public void mouseDragged(MouseEvent e) {
        mouseX = e.getX();
        mouseY = e.getY();
        lastEvent = "DRAGGED (button held)";
        repaint();
    }

    public static void main(String[] args) { new MouseEventDemo(); }
}
""",
    lang="java",
)
pn.br()

# =============================================================================
#  5.7  KEY EVENTS
# =============================================================================
pn.chap_box("5.7  Key Events")
pn.section("KeyEvent Class -- Complete Reference")
pn.definition(
    "<b>KeyEvent:</b> Represents a keyboard event generated when the user presses "
    "or releases a key on a keyboard-focused component. "
    "It extends <code>InputEvent</code>. "
    "Key events are handled by the <code>KeyListener</code> interface. "
    "The component that receives key events must have keyboard focus -- "
    "use <code>component.requestFocus()</code> to programmatically give focus."
)

pn.info_table(
    ["KeyListener Method", "When Invoked", "Key Data Available"],
    [
        [
            "keyPressed(KeyEvent e)",
            "Any key is pressed down. Fires for ALL keys including function keys, arrows, and modifiers.",
            "getKeyCode() returns VK_XXX integer. getKeyText() returns string like 'F1', 'Enter', 'Left'.",
        ],
        [
            "keyReleased(KeyEvent e)",
            "Any key is released after being pressed. Also fires for ALL keys.",
            "getKeyCode() returns VK_XXX integer. getKeyText() returns text name.",
        ],
        [
            "keyTyped(KeyEvent e)",
            "A printable character key is typed (press + release). Does NOT fire for non-character keys like F1, Arrows, Ctrl.",
            "getKeyChar() returns the actual char value ('a', 'A', '5', '@'). getKeyCode() returns UNDEFINED.",
        ],
    ],
)

pn.section("Virtual Key Codes (VK_ Constants)")
pn.body(
    "Key codes are integer constants defined in the <code>KeyEvent</code> class. "
    "They identify physical keys regardless of shift/caps state. "
    "Use them in <code>keyPressed()</code> and <code>keyReleased()</code> to detect special keys."
)
pn.info_table(
    ["Key", "VK Constant", "Key", "VK Constant"],
    [
        ["Enter", "KeyEvent.VK_ENTER", "Escape", "KeyEvent.VK_ESCAPE"],
        ["Space", "KeyEvent.VK_SPACE", "Backspace", "KeyEvent.VK_BACK_SPACE"],
        ["Tab", "KeyEvent.VK_TAB", "Delete", "KeyEvent.VK_DELETE"],
        ["Up Arrow", "KeyEvent.VK_UP", "Down Arrow", "KeyEvent.VK_DOWN"],
        ["Left Arrow", "KeyEvent.VK_LEFT", "Right Arrow", "KeyEvent.VK_RIGHT"],
        ["F1 - F12", "VK_F1 through VK_F12", "Home / End", "VK_HOME / VK_END"],
        ["Ctrl", "KeyEvent.VK_CONTROL", "Shift", "KeyEvent.VK_SHIFT"],
        ["Alt", "KeyEvent.VK_ALT", "Caps Lock", "KeyEvent.VK_CAPS_LOCK"],
        [
            "A-Z (letter)",
            "KeyEvent.VK_A ... VK_Z",
            "0-9 (digit)",
            "KeyEvent.VK_0 ... VK_9",
        ],
    ],
)

pn.section("KeyEvent Demo")
pn.code_block(
    """
// KeyEventDemo.java -- demonstrates all three KeyListener methods
import java.awt.*;
import java.awt.event.*;

public class KeyEventDemo extends Frame implements KeyListener {

    TextArea taDisplay;    // shows key event info
    TextField txtInput;    // keyboard focus target

    public KeyEventDemo() {
        super("Key Event Demo -- IT408 Unit V");
        setSize(500, 380);
        setLayout(new BorderLayout(5, 5));

        // ---- TextArea to show key event information ----
        taDisplay = new TextArea("Press keys in the field below...\n", 12, 55);
        taDisplay.setEditable(false);
        taDisplay.setFont(new Font("Courier New", Font.PLAIN, 12));
        add(taDisplay, BorderLayout.CENTER);

        // ---- TextField as the keyboard focus target ----
        Label lbl = new Label("Type here (keyboard focus):", Label.LEFT);
        txtInput = new TextField(40);
        txtInput.setFont(new Font("Arial", Font.PLAIN, 14));

        // Register KeyListener on the TextField
        txtInput.addKeyListener(this);

        Panel southPanel = new Panel(new FlowLayout(FlowLayout.LEFT));
        southPanel.add(lbl);
        southPanel.add(txtInput);
        add(southPanel, BorderLayout.SOUTH);

        addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent e) { dispose(); System.exit(0); }
        });
        setVisible(true);
        txtInput.requestFocus();  // give keyboard focus to the input field
    }

    // ---- keyPressed: fires for ALL keys including special keys ----
    @Override
    public void keyPressed(KeyEvent e) {
        int    code = e.getKeyCode();           // VK_XXX integer
        String text = KeyEvent.getKeyText(code); // human-readable name

        // Detect modifier key combinations
        String mods = "";
        if (e.isControlDown()) mods += "Ctrl+";
        if (e.isShiftDown())   mods += "Shift+";
        if (e.isAltDown())     mods += "Alt+";

        taDisplay.append("[PRESSED]  KeyCode=" + code + "  Name='" + mods + text + "'\n");

        // Handle special key actions
        if (code == KeyEvent.VK_ESCAPE) {
            txtInput.setText("");           // Escape clears the input field
            taDisplay.append("  >> Escape pressed: input field cleared\n");
        }
        if (code == KeyEvent.VK_ENTER) {
            taDisplay.append("  >> Enter pressed: '" + txtInput.getText() + "'\n");
        }
        // Ctrl+A = Select All (common shortcut)
        if (e.isControlDown() && code == KeyEvent.VK_A) {
            txtInput.selectAll();
            taDisplay.append("  >> Ctrl+A: selected all text\n");
        }
    }

    // ---- keyReleased: fires when key is released ----
    @Override
    public void keyReleased(KeyEvent e) {
        taDisplay.append("[RELEASED] KeyCode=" + e.getKeyCode()
                      + "  Name='" + KeyEvent.getKeyText(e.getKeyCode()) + "'\n");
    }

    // ---- keyTyped: fires ONLY for printable character keys ----
    @Override
    public void keyTyped(KeyEvent e) {
        char ch = e.getKeyChar();   // the actual character typed ('a', 'A', '1', '@')
        taDisplay.append("[TYPED]    KeyChar='" + ch
                      + "'  char value=" + (int)ch + "\n");

        // Example: block non-digit input in a numeric field
        if (!Character.isDigit(ch) && ch != KeyEvent.VK_BACK_SPACE) {
            // e.consume() cancels the character so it doesn't appear in the field
            // (Uncomment to enable input validation):
            // e.consume();
            // taDisplay.append("  >> Non-digit blocked!\n");
        }
    }

    public static void main(String[] args) { new KeyEventDemo(); }
}
""",
    lang="java",
)
pn.br()

# =============================================================================
#  5.8  OTHER EVENT CLASSES
# =============================================================================
pn.chap_box("5.8  Other AWT Event Classes")
pn.section("ItemEvent -- Checkbox and Choice Changes")
pn.code_block(
    """
// ItemEvent fires when Checkbox state changes or Choice/List selection changes
import java.awt.*;
import java.awt.event.*;

public class ItemEventDemo extends Frame implements ItemListener {
    Checkbox chkBold, chkItalic;
    Choice colorChoice;
    Label  lblSample;

    public ItemEventDemo() {
        super("ItemEvent Demo");
        setSize(380, 200);
        setLayout(new FlowLayout(FlowLayout.CENTER, 15, 15));

        chkBold   = new Checkbox("Bold",   false);
        chkItalic = new Checkbox("Italic", false);
        colorChoice = new Choice();
        colorChoice.add("Black"); colorChoice.add("Red");
        colorChoice.add("Blue");  colorChoice.add("Green");
        lblSample = new Label("Sample Text", Label.CENTER);
        lblSample.setFont(new Font("Arial", Font.PLAIN, 18));
        lblSample.setPreferredSize(new Dimension(300, 35));

        // Register ItemListener on checkboxes and choice
        chkBold.addItemListener(this);
        chkItalic.addItemListener(this);
        colorChoice.addItemListener(this);

        add(chkBold); add(chkItalic); add(colorChoice); add(lblSample);
        addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent e) { dispose(); System.exit(0); }
        });
        setVisible(true);
    }

    @Override
    public void itemStateChanged(ItemEvent e) {
        // Determine new font style from checkbox states
        int style = Font.PLAIN;
        if (chkBold.getState())   style |= Font.BOLD;
        if (chkItalic.getState()) style |= Font.ITALIC;
        lblSample.setFont(new Font("Arial", style, 18));

        // Determine color from Choice
        String col = colorChoice.getSelectedItem();
        if (col.equals("Red"))   lblSample.setForeground(Color.RED);
        else if (col.equals("Blue"))  lblSample.setForeground(Color.BLUE);
        else if (col.equals("Green")) lblSample.setForeground(Color.GREEN);
        else lblSample.setForeground(Color.BLACK);

        // ItemEvent.getStateChange() returns SELECTED or DESELECTED
        String action = (e.getStateChange() == ItemEvent.SELECTED) ? "SELECTED" : "DESELECTED";
        System.out.println("ItemEvent: " + e.getItem() + " -> " + action);
    }

    public static void main(String[] args) { new ItemEventDemo(); }
}
""",
    lang="java",
)

pn.section("TextEvent, AdjustmentEvent, FocusEvent")
pn.code_block(
    """
// TextEvent fires on every character change in TextField/TextArea
textField.addTextListener(new TextListener() {
    @Override
    public void textValueChanged(TextEvent e) {
        // e.getSource() gives the TextComponent that changed
        TextField tf = (TextField) e.getSource();
        System.out.println("Text changed: '" + tf.getText() + "'  length=" + tf.getText().length());

        // Real use case: live character counter, input validation, autocomplete trigger
        lblCharCount.setText("Characters: " + tf.getText().length());
    }
});

// AdjustmentEvent fires when Scrollbar position changes
scrollbar.addAdjustmentListener(new AdjustmentListener() {
    @Override
    public void adjustmentValueChanged(AdjustmentEvent e) {
        int value = e.getValue();              // current scrollbar position
        int type  = e.getAdjustmentType();     // UNIT_INCREMENT, BLOCK_INCREMENT, TRACK
        System.out.println("Scrollbar value=" + value + "  type=" + type);
    }
});

// FocusEvent fires when a component gains or loses keyboard focus
textField.addFocusListener(new FocusAdapter() {
    @Override
    public void focusGained(FocusEvent e) {
        textField.setBackground(new Color(255, 255, 200));  // highlight on focus
        System.out.println("Focus GAINED by: " + ((Component)e.getSource()).getName());
    }
    @Override
    public void focusLost(FocusEvent e) {
        textField.setBackground(Color.WHITE);               // restore on focus loss
        System.out.println("Focus LOST: " + (e.isTemporary() ? "temporary" : "permanent"));
    }
});
""",
    lang="java",
)
pn.br()

# =============================================================================
#  5.9  JDBC INTRODUCTION
# =============================================================================
pn.part_box("UNIT V -- JDBC: JAVA DATABASE CONNECTIVITY")
pn.chap_box("5.9  Introduction to JDBC")
pn.section("What is JDBC?")
pn.definition(
    "<b>JDBC (Java Database Connectivity):</b> A Java API (Application Programming Interface) "
    "that defines how Java programs communicate with relational databases. "
    "Located in the <code>java.sql</code> package (core) and <code>javax.sql</code> (extensions), "
    "JDBC provides a standard interface so that the same Java code can work with "
    "different database systems (MySQL, Oracle, PostgreSQL, SQLite, MS Access) "
    "by simply changing the database driver -- the Java code itself stays the same. "
    "This database-independence is JDBC's most important feature."
)

pn.section("Why JDBC? The Database Independence Problem")
pn.body(
    "Every database system (MySQL, Oracle, PostgreSQL) has its own proprietary "
    "network protocol, query format, and communication API. Without JDBC, "
    "a Java program written for MySQL would have to be completely rewritten for Oracle. "
    "JDBC defines a standard set of interfaces; each database vendor writes a "
    "<b>JDBC Driver</b> that implements these interfaces for their specific database. "
    "Your Java code targets the JDBC interfaces; the driver handles the vendor specifics."
)

pn.section("JDBC Driver Types")
pn.info_table(
    ["Type", "Name", "How It Works", "Use Today"],
    [
        [
            "Type 1",
            "JDBC-ODBC Bridge Driver",
            "Translates JDBC calls to ODBC (Windows API), then ODBC calls the database. Requires ODBC driver installed. Very slow -- two translation layers.",
            "DEPRECATED -- removed from Java 8. Shown only for historical/exam context.",
        ],
        [
            "Type 2",
            "Native API Driver",
            "Translates JDBC calls to database-specific client library (C/C++ native code). Faster than Type 1 but requires native library on each client machine.",
            "Still used for some enterprise databases (Oracle OCI). Limited portability.",
        ],
        [
            "Type 3",
            "Network Protocol Driver",
            "Pure Java driver that sends JDBC calls to a middleware server over a generic network protocol. Middleware translates to DB-specific protocol.",
            "Used in three-tier enterprise architectures. Rarely seen in practice today.",
        ],
        [
            "Type 4",
            "Thin / Pure Java Driver",
            "Pure Java driver that directly implements the database's native network protocol. No native libraries, no middleware. Most portable and fastest.",
            "THE STANDARD today. MySQL Connector/J, PostgreSQL JDBC, SQLite JDBC are all Type 4.",
        ],
    ],
)

pn.note(
    "For the IT408 exam: The JDBC-ODBC bridge (Type 1) is mentioned in the syllabus for historical context. "
    "It required <code>Class.forName('sun.jdbc.odbc.JdbcOdbcDriver')</code> and was removed in Java 8. "
    "All modern applications use Type 4 drivers. "
    "The Type 4 driver for MySQL is <code>com.mysql.cj.jdbc.Driver</code> (MySQL Connector/J)."
)
pn.br()

# =============================================================================
#  5.10  JDBC ARCHITECTURE & THE CONNECTIVITY MODEL
# =============================================================================
pn.chap_box("5.10  JDBC Architecture & Connectivity Model")
pn.section("The JDBC Connectivity Model")
pn.body(
    "JDBC uses a layered architecture. Your Java application works with the "
    "JDBC API (interfaces in java.sql). The DriverManager selects the appropriate "
    "driver. The driver communicates with the actual database server."
)

# Network diagram showing JDBC architecture
net_jdbc = pd.NetworkDiagram(
    width=530,
    height=240,
    theme=diag_theme,
    caption="Fig 5.3: JDBC Architecture -- Java App to DriverManager to Driver to Database",
)
net_jdbc.node("app", "Java Application\n(Your Code)", x=40, y=120, kind="host")
net_jdbc.node("api", "JDBC API\n(java.sql package)", x=140, y=120, kind="server")
net_jdbc.node("dm", "DriverManager\n(selects driver)", x=240, y=120, kind="generic")
net_jdbc.node("driver", "JDBC Driver\n(vendor-specific)", x=340, y=120, kind="storage")
net_jdbc.node(
    "db", "Database Server\n(MySQL/Oracle/etc.)", x=490, y=120, kind="database"
)

net_jdbc.link("app", "api", label="uses", bidirectional=False)
net_jdbc.link("api", "dm", label="calls", bidirectional=False)
net_jdbc.link("dm", "driver", label="loads", bidirectional=False)
net_jdbc.link("driver", "db", label="TCP/IP\nnative protocol", bidirectional=True)
pn.story.extend(net_jdbc.as_flowable())

pn.section("The DriverManager Class")
pn.definition(
    "<b>DriverManager (java.sql.DriverManager):</b> The JDBC management layer that "
    "maintains a list of registered database drivers and selects the appropriate one "
    "when a connection is requested. "
    "Key method: <code>DriverManager.getConnection(url, user, password)</code> "
    "returns a Connection object to the specified database. "
    "The URL format is driver-specific: "
    "<code>jdbc:mysql://host:port/database</code> for MySQL, "
    "<code>jdbc:oracle:thin:@host:port:sid</code> for Oracle."
)

pn.section("Core JDBC Interfaces in java.sql")
pn.info_table(
    ["Interface / Class", "Role", "Key Methods"],
    [
        [
            "DriverManager (class)",
            "Manages drivers; creates connections. Entry point for JDBC.",
            "getConnection(url, user, pwd) -- returns Connection",
        ],
        [
            "Connection",
            "Represents an open session/transaction with a specific database.",
            "createStatement(), prepareStatement(sql), commit(), rollback(), close(), setAutoCommit(false)",
        ],
        [
            "Statement",
            "Executes a static SQL query against the database. Created from Connection.",
            "executeQuery(sql) -- SELECT; executeUpdate(sql) -- INSERT/UPDATE/DELETE; execute(sql) -- any",
        ],
        [
            "PreparedStatement",
            "Pre-compiled SQL with placeholders (?). Safer (prevents SQL injection) and faster for repeated execution.",
            "setInt(1, val), setString(2, str), executeQuery(), executeUpdate()",
        ],
        [
            "ResultSet",
            "Cursor over the rows returned by a SELECT query. Move with next(). Read with getXxx().",
            "next(), getString(col), getInt(col), getDouble(col), getDate(col), first(), last(), close()",
        ],
        [
            "SQLException (class)",
            "Exception thrown when a JDBC operation fails. Has detailed DB error info.",
            "getMessage(), getSQLState(), getErrorCode(), getNextException()",
        ],
        [
            "CallableStatement",
            "Executes stored procedures defined in the database.",
            "registerOutParameter(), setXxx(), execute()",
        ],
    ],
)

pn.section("The Six Steps of JDBC Programming")
pn.bullet(
    [
        "<b>Step 1 -- Load Driver:</b> Register the JDBC driver class with the JVM. Modern JDBC (4.0+) loads automatically from the JAR using ServiceLoader -- explicit loading is optional but still commonly shown: <code>Class.forName('com.mysql.cj.jdbc.Driver');</code>",
        "<b>Step 2 -- Establish Connection:</b> Call <code>DriverManager.getConnection(url, user, password)</code> to open a Connection to the database.",
        "<b>Step 3 -- Create Statement:</b> Call <code>connection.createStatement()</code> to get a Statement object, or <code>connection.prepareStatement(sql)</code> for PreparedStatement.",
        "<b>Step 4 -- Execute Query:</b> Call <code>statement.executeQuery(sql)</code> for SELECT (returns ResultSet), or <code>statement.executeUpdate(sql)</code> for INSERT/UPDATE/DELETE (returns row count).",
        "<b>Step 5 -- Process ResultSet:</b> Iterate the ResultSet with <code>while(rs.next())</code> and retrieve column values with <code>rs.getString('colName')</code>, <code>rs.getInt('colName')</code>, etc.",
        "<b>Step 6 -- Close Resources:</b> Close in reverse order: <code>rs.close(); stmt.close(); conn.close();</code> Always in a finally block or try-with-resources to prevent resource leaks.",
    ]
)

pn.section("Complete JDBC Program -- All Six Steps")
pn.code_block(
    """
// JDBCDemo.java -- Complete JDBC program demonstrating all 6 steps
// Requires: MySQL Connector/J (mysql-connector-java-x.x.x.jar) in classpath
// Run: javac JDBCDemo.java && java -cp .:mysql-connector-java.jar JDBCDemo
import java.sql.*;

public class JDBCDemo {

    // ---- Database connection parameters ----
    static final String DB_URL  = "jdbc:mysql://localhost:3306/college_db";
    static final String DB_USER = "root";
    static final String DB_PASS = "password123";

    public static void main(String[] args) {

        // ---- Try-with-resources: auto-closes Connection, Statement, ResultSet ----
        // Resources declared in try() are automatically closed even if exception occurs
        try (
            // STEP 1 + 2: Load driver (auto with JDBC 4.0+) and get Connection
            Connection conn = DriverManager.getConnection(DB_URL, DB_USER, DB_PASS);

            // STEP 3: Create a Statement
            Statement stmt = conn.createStatement()
        ) {
            System.out.println("Database connected successfully!");

            // ====================================================
            // INSERT: add a new student record
            // ====================================================
            String insertSQL = "INSERT INTO students (name, branch, marks) "
                             + "VALUES ('Arjun Sharma', 'IT', 88.5)";
            int rowsInserted = stmt.executeUpdate(insertSQL); // returns count of affected rows
            System.out.println("Rows inserted: " + rowsInserted);

            // ====================================================
            // SELECT: query and display all student records
            // STEP 4: Execute SELECT query -- returns ResultSet
            // ====================================================
            String selectSQL = "SELECT id, name, branch, marks FROM students ORDER BY marks DESC";
            try (ResultSet rs = stmt.executeQuery(selectSQL)) {

                System.out.println("\n--- Student Records (sorted by marks) ---");
                System.out.printf("%-5s %-20s %-15s %-8s%n", "ID", "Name", "Branch", "Marks");
                System.out.println("-".repeat(55));

                // STEP 5: Process ResultSet -- rs.next() advances cursor one row
                while (rs.next()) {
                    // Retrieve column values by column name or index (1-based)
                    int    id     = rs.getInt("id");          // retrieve int column
                    String name   = rs.getString("name");     // retrieve String column
                    String branch = rs.getString("branch");
                    double marks  = rs.getDouble("marks");    // retrieve double column
                    System.out.printf("%-5d %-20s %-15s %-8.1f%n", id, name, branch, marks);
                }
                // ResultSet is auto-closed by inner try-with-resources
            }

            // ====================================================
            // UPDATE: modify a record
            // ====================================================
            String updateSQL = "UPDATE students SET marks = 92.0 WHERE name = 'Arjun Sharma'";
            int rowsUpdated = stmt.executeUpdate(updateSQL);
            System.out.println("\nRows updated: " + rowsUpdated);

            // ====================================================
            // DELETE: remove a record
            // ====================================================
            String deleteSQL = "DELETE FROM students WHERE marks < 40.0";
            int rowsDeleted = stmt.executeUpdate(deleteSQL);
            System.out.println("Rows deleted (marks < 40): " + rowsDeleted);

        } catch (SQLException e) {
            // JDBC-specific exception with detailed database error information
            System.err.println("Database error occurred!");
            System.err.println("Message   : " + e.getMessage());
            System.err.println("SQL State : " + e.getSQLState());  // 5-char XOPEN/SQL99 code
            System.err.println("Error Code: " + e.getErrorCode()); // vendor-specific error number
            e.printStackTrace();

        }
        // STEP 6: Connection, Statement, ResultSet are auto-closed by try-with-resources
        System.out.println("Connection closed (try-with-resources).");
    }
}

// ================================================================
// SQL TO CREATE THE TABLE (run in MySQL first)
// ================================================================
/*
CREATE DATABASE college_db;
USE college_db;

CREATE TABLE students (
    id     INT          AUTO_INCREMENT PRIMARY KEY,
    name   VARCHAR(100) NOT NULL,
    branch VARCHAR(50),
    marks  DOUBLE
);

INSERT INTO students (name, branch, marks) VALUES
    ('Priya Patel',  'CS',  92.0),
    ('Rahul Singh',  'EC',  79.5),
    ('Sneha Joshi',  'IT',  95.0),
    ('Rohit Kumar',  'ME',  35.0);
*/
""",
    lang="java",
)
pn.br()

# =============================================================================
#  5.11  NAVIGATING THE RESULT SET
# =============================================================================
pn.chap_box("5.11  Navigating the ResultSet")
pn.section("ResultSet Cursor Navigation")
pn.definition(
    "<b>ResultSet:</b> A table of data (rows and columns) returned by executing a SQL SELECT query. "
    "A ResultSet object maintains a <b>cursor</b> pointing to the current row. "
    "Initially the cursor is positioned BEFORE the first row -- calling <code>next()</code> "
    "moves it to the first row. "
    "By default, a ResultSet is <b>forward-only</b> (TYPE_FORWARD_ONLY) and "
    "<b>read-only</b> (CONCUR_READ_ONLY). "
    "To use navigation methods like <code>previous()</code>, <code>first()</code>, "
    "or <code>absolute()</code>, the ResultSet must be created as TYPE_SCROLL_INSENSITIVE or TYPE_SCROLL_SENSITIVE."
)

pn.section("Creating a Scrollable ResultSet")
pn.code_block(
    """
// Creating a SCROLLABLE ResultSet for bidirectional navigation
// The Statement must be created with scroll type and concurrency flags

// STEP 1: Create statement with scroll and concurrency parameters
Statement stmt = conn.createStatement(
    ResultSet.TYPE_SCROLL_INSENSITIVE,  // can scroll forward AND backward
    ResultSet.CONCUR_READ_ONLY           // cannot update through this ResultSet
);

// Alternative: CONCUR_UPDATABLE allows updating rows via ResultSet methods
// ResultSet.CONCUR_UPDATABLE

// STEP 2: Execute query -- returns scrollable ResultSet
ResultSet rs = stmt.executeQuery("SELECT id, name, marks FROM students");
""",
    lang="java",
)

pn.section("ResultSet Navigation Methods")
pn.info_table(
    ["Method", "Return", "Cursor Moves To"],
    [
        [
            "next()",
            "boolean",
            "Next row. Returns true if valid row; false if past last row. WORKS FOR ALL ResultSet types.",
        ],
        [
            "previous()",
            "boolean",
            "Previous row. Returns false if before first row. Requires SCROLL type.",
        ],
        [
            "first()",
            "boolean",
            "First row. Returns false if ResultSet is empty. Requires SCROLL type.",
        ],
        [
            "last()",
            "boolean",
            "Last row. Returns false if ResultSet is empty. Requires SCROLL type.",
        ],
        [
            "absolute(int n)",
            "boolean",
            "Row number n (1-based). Negative n counts from end: absolute(-1) = last row. Requires SCROLL type.",
        ],
        [
            "relative(int n)",
            "boolean",
            "Moves n rows forward (positive) or backward (negative) from current position. Requires SCROLL type.",
        ],
        [
            "beforeFirst()",
            "void",
            "Positions cursor BEFORE the first row (initial position). Requires SCROLL type.",
        ],
        [
            "afterLast()",
            "void",
            "Positions cursor AFTER the last row. Requires SCROLL type.",
        ],
        ["isFirst()", "boolean", "True if cursor is on the first row."],
        ["isLast()", "boolean", "True if cursor is on the last row."],
        [
            "isBeforeFirst()",
            "boolean",
            "True if cursor is before the first row (initial position).",
        ],
        ["isAfterLast()", "boolean", "True if cursor is after the last row."],
        [
            "getRow()",
            "int",
            "Returns the current row number (1-based). 0 if before first or after last.",
        ],
    ],
)

pn.section("ResultSet Data Retrieval Methods")
pn.info_table(
    ["Method Group", "Methods", "Description"],
    [
        [
            "String columns",
            "getString(colName), getString(colIndex)",
            "Retrieves the column value as a String. Works for VARCHAR, CHAR, TEXT, and most other types.",
        ],
        [
            "Integer columns",
            "getInt(colName), getLong(colName), getShort(colName)",
            "Retrieves integer column values. getInt for INT, getLong for BIGINT.",
        ],
        [
            "Floating-point",
            "getDouble(colName), getFloat(colName)",
            "Retrieves DOUBLE/FLOAT column values as Java double/float.",
        ],
        [
            "Boolean columns",
            "getBoolean(colName)",
            "Retrieves BOOLEAN/TINYINT(1) column. True if value is 'true' or 1.",
        ],
        [
            "Date and Time",
            "getDate(colName), getTime(colName), getTimestamp(colName)",
            "Retrieves SQL DATE, TIME, TIMESTAMP as java.sql.Date, Time, Timestamp.",
        ],
        [
            "Null check",
            "wasNull()",
            "Call AFTER any getXxx() -- returns true if the last column read had a SQL NULL value.",
        ],
        [
            "Metadata",
            "getMetaData(): ResultSetMetaData",
            "Returns column count, column names, and column types. Used for generic table display.",
        ],
        [
            "Column by index",
            "getString(1), getInt(2)",
            "Column indexes are 1-based. Faster than name lookup but fragile if columns reorder.",
        ],
    ],
)

pn.section("Scrollable ResultSet Demo")
pn.code_block(
    """
// ScrollableResultSetDemo.java -- forward, backward, absolute navigation
import java.sql.*;

public class ScrollableResultSetDemo {
    public static void main(String[] args) throws SQLException {
        String url  = "jdbc:mysql://localhost:3306/college_db";
        Connection conn = DriverManager.getConnection(url, "root", "password123");

        // Create SCROLLABLE statement
        Statement stmt = conn.createStatement(
            ResultSet.TYPE_SCROLL_INSENSITIVE,
            ResultSet.CONCUR_READ_ONLY
        );
        ResultSet rs = stmt.executeQuery("SELECT id, name, marks FROM students");

        // ---- Forward navigation (standard) ----
        System.out.println("--- Forward (first to last) ---");
        while (rs.next()) {
            System.out.printf("Row %d: id=%-3d  name=%-20s  marks=%.1f%n",
                rs.getRow(), rs.getInt("id"), rs.getString("name"), rs.getDouble("marks"));
        }

        // ---- Backward navigation ----
        System.out.println("\n--- Backward (last to first) ---");
        rs.afterLast();                           // position after last row
        while (rs.previous()) {                   // move backward
            System.out.printf("Row %d: %s  %.1f%n",
                rs.getRow(), rs.getString("name"), rs.getDouble("marks"));
        }

        // ---- Jump to specific rows ----
        System.out.println("\n--- Absolute positioning ---");
        rs.first();
        System.out.println("First: " + rs.getString("name"));

        rs.last();
        System.out.println("Last:  " + rs.getString("name"));

        rs.absolute(2);                           // jump to row 2 directly
        System.out.println("Row 2: " + rs.getString("name"));

        rs.absolute(-1);                          // -1 = last row
        System.out.println("Row -1 (last): " + rs.getString("name"));

        rs.relative(-1);                          // move back 1 from current
        System.out.println("Relative(-1): " + rs.getString("name"));

        // ---- Metadata: discover column info at runtime ----
        System.out.println("\n--- ResultSetMetaData ---");
        rs.first();
        ResultSetMetaData meta = rs.getMetaData();
        int colCount = meta.getColumnCount();
        System.out.println("Column count: " + colCount);
        for (int i = 1; i <= colCount; i++) {
            System.out.printf("  Col %d: name='%s'  type='%s'  displaySize=%d%n",
                i, meta.getColumnName(i), meta.getColumnTypeName(i), meta.getColumnDisplaySize(i));
        }

        // ALWAYS close in finally or use try-with-resources
        rs.close();
        stmt.close();
        conn.close();
    }
}
""",
    lang="java",
)
pn.br()

# =============================================================================
#  5.12  JDBC EXCEPTION CLASSES
# =============================================================================
pn.chap_box("5.12  JDBC Exception Classes")
pn.section("SQLException -- The Primary JDBC Exception")
pn.definition(
    "<b>SQLException:</b> The primary exception class for all database errors in JDBC. "
    "It extends <code>Exception</code> (checked exception -- must be caught or declared). "
    "SQLException carries three pieces of database error information: "
    "(1) <b>Message:</b> Human-readable description of the error. "
    "(2) <b>SQLState:</b> A 5-character code following the XOPEN or SQL:2003 standard "
    "(e.g., '23000' = integrity constraint violation, '42S02' = table not found). "
    "(3) <b>Vendor Error Code:</b> Database-specific integer error code "
    "(e.g., MySQL error 1062 = Duplicate entry, 1146 = Table doesn't exist). "
    "SQLExceptions can be CHAINED -- each exception can have a 'next exception' "
    "linked via <code>getNextException()</code>."
)

pn.info_table(
    ["JDBC Exception Class", "Extends", "Description"],
    [
        [
            "SQLException",
            "Exception",
            "Base class for ALL JDBC exceptions. Wraps database error code, SQLState, and message. Iterable since Java 6 -- chain with for-each loop.",
        ],
        [
            "SQLWarning",
            "SQLException",
            "Non-fatal conditions reported by the DB (data truncation, deprecated feature use). Attached to Connection, Statement, or ResultSet. Retrieved with getWarnings().",
        ],
        [
            "DataTruncation",
            "SQLWarning",
            "Specifically for data truncation on read or write. Provides getDataSize() (actual data size) and getTransferSize() (bytes transferred).",
        ],
        [
            "BatchUpdateException",
            "SQLException",
            "Thrown during batch execution (executeBatch()). Provides getUpdateCounts() array showing how many rows each batch statement affected before failure.",
        ],
        [
            "SQLTimeoutException",
            "SQLTransientException",
            "Thrown when a query or statement exceeds the timeout set by setQueryTimeout().",
        ],
    ],
)

pn.section("Handling SQLException Properly")
pn.code_block(
    """
// ExceptionHandlingDemo.java -- proper JDBC exception handling
import java.sql.*;

public class ExceptionHandlingDemo {

    static final String URL  = "jdbc:mysql://localhost:3306/college_db";
    static final String USER = "root";
    static final String PASS = "password123";

    public static void main(String[] args) {
        Connection conn = null;
        Statement  stmt = null;
        ResultSet  rs   = null;

        try {
            conn = DriverManager.getConnection(URL, USER, PASS);
            stmt = conn.createStatement();

            // ---- Intentional errors for demonstration ----

            // SCENARIO 1: Table doesn't exist -- causes SQLException
            try {
                rs = stmt.executeQuery("SELECT * FROM nonexistent_table");
            } catch (SQLException e) {
                System.out.println("CAUGHT: Table error");
                System.out.println("  Message   : " + e.getMessage());
                System.out.println("  SQLState  : " + e.getSQLState());     // 42S02 in MySQL
                System.out.println("  Error Code: " + e.getErrorCode());    // 1146 in MySQL
                // CHAIN: iterate through chained exceptions (if any)
                SQLException next = e.getNextException();
                if (next != null) System.out.println("  Chained: " + next.getMessage());
            }

            // SCENARIO 2: Check for SQLWarnings on a successful query
            rs = stmt.executeQuery("SELECT * FROM students");
            SQLWarning warning = stmt.getWarnings();
            while (warning != null) {
                System.out.println("WARNING: " + warning.getMessage()
                                 + " (SQLState=" + warning.getSQLState() + ")");
                warning = warning.getNextWarning();     // warnings are chained too
            }

            // SCENARIO 3: Batch update with BatchUpdateException
            conn.setAutoCommit(false);    // disable auto-commit for batch
            Statement batchStmt = conn.createStatement();
            batchStmt.addBatch("INSERT INTO students(name, branch, marks) VALUES('Batch1','IT',80)");
            batchStmt.addBatch("INSERT INTO students(name, branch, marks) VALUES('Batch2','CS',85)");
            batchStmt.addBatch("INVALID SQL STATEMENT");  // this will fail
            try {
                int[] counts = batchStmt.executeBatch();
                conn.commit();
                for (int i = 0; i < counts.length; i++) {
                    System.out.println("Batch stmt " + (i+1) + " affected: " + counts[i] + " rows");
                }
            } catch (BatchUpdateException bue) {
                System.out.println("BATCH FAILED: " + bue.getMessage());
                int[] updateCounts = bue.getUpdateCounts();
                for (int i = 0; i < updateCounts.length; i++) {
                    System.out.println("  Batch[" + i + "] count: " + updateCounts[i]);
                }
                conn.rollback();   // rollback entire batch on any failure
            }

        } catch (SQLException e) {
            System.err.println("FATAL DB Error: " + e.getMessage());
            // Java 6+: SQLException is Iterable for chained exceptions
            for (Throwable t : e) {
                System.err.println("  -> " + t.getMessage());
            }
        } finally {
            // STEP 6: Always close in finally to guarantee resource release
            // Even if exceptions occurred above, we MUST close these
            try { if (rs   != null) rs.close();   } catch (SQLException e) { e.printStackTrace(); }
            try { if (stmt != null) stmt.close();  } catch (SQLException e) { e.printStackTrace(); }
            try { if (conn != null) conn.close();  } catch (SQLException e) { e.printStackTrace(); }
            System.out.println("Resources closed in finally block.");
        }
    }
}
""",
    lang="java",
)
pn.br()

# =============================================================================
#  5.13  CONNECTING TO REMOTE DATABASE / PREPAREDSTATEMENT
# =============================================================================
pn.chap_box("5.13  Connecting to Remote Database & PreparedStatement")
pn.section("Remote Database Connection")
pn.definition(
    "<b>Remote Database Connection:</b> Connecting to a database server running on "
    "a different machine (not localhost). The JDBC URL changes to include the "
    "remote hostname or IP address. The database server must be configured to "
    "accept remote connections (bind-address=0.0.0.0 in MySQL) and the firewall "
    "must allow traffic on the database port (MySQL default: 3306)."
)

pn.info_table(
    ["Database", "Local URL", "Remote URL Format"],
    [
        [
            "MySQL",
            "jdbc:mysql://localhost:3306/mydb",
            "jdbc:mysql://192.168.1.100:3306/mydb",
        ],
        [
            "MySQL (SSL)",
            "jdbc:mysql://localhost:3306/mydb",
            "jdbc:mysql://remote-host:3306/mydb?useSSL=true&requireSSL=true",
        ],
        [
            "PostgreSQL",
            "jdbc:postgresql://localhost:5432/mydb",
            "jdbc:postgresql://db.example.com:5432/mydb",
        ],
        [
            "Oracle",
            "jdbc:oracle:thin:@localhost:1521:orcl",
            "jdbc:oracle:thin:@10.0.0.1:1521:orcl",
        ],
        [
            "SQLite (file)",
            "jdbc:sqlite:local.db",
            "SQLite is file-based only -- no remote connections",
        ],
        [
            "MS SQL Server",
            "jdbc:sqlserver://localhost:1433;databaseName=mydb",
            "jdbc:sqlserver://192.168.1.50:1433;databaseName=mydb",
        ],
    ],
)

pn.section("PreparedStatement -- Safe Parameterized Queries")
pn.definition(
    "<b>PreparedStatement:</b> A pre-compiled SQL statement with placeholder "
    "parameters represented by <code>?</code>. "
    "It is preferred over Statement for four reasons: "
    "(1) <b>SQL Injection Prevention:</b> Parameters are automatically escaped -- "
    "user input cannot break out of the SQL syntax. "
    "(2) <b>Performance:</b> The SQL is compiled once and cached; executing it "
    "multiple times with different parameters is faster. "
    "(3) <b>Cleaner Code:</b> No string concatenation needed to build SQL. "
    "(4) <b>Type Safety:</b> setInt(), setString(), setDate() handle type conversion "
    "and quoting automatically."
)

pn.code_block(
    """
// PreparedStatementDemo.java -- demonstrates PreparedStatement and remote DB
import java.sql.*;

public class PreparedStatementDemo {

    // ---- Remote MySQL database connection ----
    static final String URL  = "jdbc:mysql://192.168.1.100:3306/college_db"
                             + "?useSSL=false&serverTimezone=UTC";
    static final String USER = "appuser";     // use a restricted user for remote
    static final String PASS = "securePass!"; // never hardcode in production

    public static void main(String[] args) {

        // ---- SQL INJECTION RISK with Statement (NEVER DO THIS with user input) ----
        // String userInput = "' OR '1'='1";    // malicious input
        // String sql = "SELECT * FROM students WHERE name = '" + userInput + "'";
        // This would return ALL rows -- the injected SQL is valid!

        // ---- SAFE: Use PreparedStatement with ? placeholders ----
        String insertSQL = "INSERT INTO students (name, branch, marks) VALUES (?, ?, ?)";
        String selectSQL = "SELECT id, name, branch, marks FROM students WHERE branch = ? AND marks >= ?";
        String updateSQL = "UPDATE students SET marks = ? WHERE id = ?";
        String deleteSQL = "DELETE FROM students WHERE id = ?";

        try (Connection conn = DriverManager.getConnection(URL, USER, PASS)) {

            System.out.println("Connected to remote DB: " + URL);

            // ============ INSERT with PreparedStatement ============
            try (PreparedStatement pstmt = conn.prepareStatement(insertSQL,
                    Statement.RETURN_GENERATED_KEYS)) {  // get auto-generated ID back

                // Set each ? parameter by position (1-based)
                pstmt.setString(1, "Kavya Reddy");     // param 1: name (String)
                pstmt.setString(2, "IT");               // param 2: branch (String)
                pstmt.setDouble(3, 91.5);               // param 3: marks (double)
                int rows = pstmt.executeUpdate();
                System.out.println("Inserted: " + rows + " row(s)");

                // Retrieve auto-generated primary key
                try (ResultSet generatedKeys = pstmt.getGeneratedKeys()) {
                    if (generatedKeys.next()) {
                        System.out.println("New student ID: " + generatedKeys.getInt(1));
                    }
                }

                // Reuse PreparedStatement with different parameters (efficient!)
                pstmt.setString(1, "Vikram Nair");
                pstmt.setString(2, "CS");
                pstmt.setDouble(3, 78.0);
                pstmt.executeUpdate();
                System.out.println("Second insert done.");
            }

            // ============ SELECT with PreparedStatement ============
            try (PreparedStatement pstmt = conn.prepareStatement(selectSQL)) {
                pstmt.setString(1, "IT");    // WHERE branch = 'IT'
                pstmt.setDouble(2, 75.0);    // AND marks >= 75.0
                ResultSet rs = pstmt.executeQuery();

                System.out.println("\n--- IT students with marks >= 75 ---");
                while (rs.next()) {
                    System.out.printf("ID=%-3d  Name=%-20s  Branch=%-5s  Marks=%.1f%n",
                        rs.getInt("id"), rs.getString("name"),
                        rs.getString("branch"), rs.getDouble("marks"));
                }
            }

            // ============ UPDATE with PreparedStatement ============
            try (PreparedStatement pstmt = conn.prepareStatement(updateSQL)) {
                pstmt.setDouble(1, 95.0);   // new marks value
                pstmt.setInt(2, 1);          // WHERE id = 1
                int updated = pstmt.executeUpdate();
                System.out.println("Updated " + updated + " row(s).");
            }

            // ============ TRANSACTION: commit/rollback ============
            conn.setAutoCommit(false);      // begin transaction
            try (PreparedStatement pstmt = conn.prepareStatement(deleteSQL)) {
                pstmt.setInt(1, 99);         // delete student with id=99
                int deleted = pstmt.executeUpdate();
                System.out.println("Deleted: " + deleted + " row(s)");
                conn.commit();               // commit if all operations succeeded
                System.out.println("Transaction committed.");
            } catch (SQLException e) {
                conn.rollback();             // rollback on any error
                System.out.println("Transaction rolled back: " + e.getMessage());
            }

        } catch (SQLException e) {
            System.err.println("DB Error: " + e.getMessage() + " (SQLState: " + e.getSQLState() + ")");
        }
    }
}
""",
    lang="java",
)

pn.section("JDBC Connection Flow Diagram")
fc_jdbc = pd.Flowchart(
    width=pn.CW,
    height=420,
    theme=diag_theme,
    caption="Fig 5.4: Complete JDBC Connection and Query Execution Flow",
)
fc_jdbc.terminal("start", "START: Need database data")
fc_jdbc.process("load", "Step 1: Load JDBC Driver (auto with JDBC 4.0+)")
fc_jdbc.process("connect", "Step 2: DriverManager.getConnection(url, user, pwd)")
fc_jdbc.decision("conn_ok", "Connection established?")
fc_jdbc.process("conn_err", "Handle SQLException: log error, retry or abort")
fc_jdbc.process("stmt", "Step 3: conn.createStatement() or prepareStatement(sql)")
fc_jdbc.process("exec", "Step 4: executeQuery(sql) for SELECT or executeUpdate for DML")
fc_jdbc.decision("select", "Is it a SELECT query?")
fc_jdbc.process("rs", "Step 5: Process ResultSet with while(rs.next())")
fc_jdbc.process("dml", "Step 5: Check int rowCount from executeUpdate()")
fc_jdbc.process("close", "Step 6: rs.close(), stmt.close(), conn.close()")
fc_jdbc.terminal("end", "END: All resources released")

fc_jdbc.edge("start", "load")
fc_jdbc.edge("load", "connect")
fc_jdbc.edge("connect", "conn_ok")
fc_jdbc.edge("conn_ok", "stmt", branch="yes")
fc_jdbc.edge("conn_ok", "conn_err", branch="no")
fc_jdbc.edge("stmt", "exec")
fc_jdbc.edge("exec", "select")
fc_jdbc.edge("select", "rs", branch="yes")
fc_jdbc.edge("select", "dml", branch="no")
fc_jdbc.edge("rs", "close")
fc_jdbc.edge("dml", "close")
fc_jdbc.edge("close", "end")
pn.story.extend(fc_jdbc.as_flowable())
pn.br()

# =============================================================================
#  5.14  EXAM QUESTIONS & ANSWERS
# =============================================================================
pn.part_box("UNIT V -- EXAM QUESTIONS & DETAILED ANSWERS")
pn.chap_box("5.14  Previous-Year Style Exam Questions")

pn.section("2-Mark Questions (Short Answer)")

pn.highlight(
    "<b>Q1. What is the Delegation Event Model in Java?</b><br/>"
    "A: The Delegation Event Model (introduced in Java 1.1) separates event generation "
    "from event handling. An event source (Button, TextField) generates an event object "
    "and delegates (passes) it to registered listener objects. "
    "The listener object (implementing a listener interface like ActionListener) contains the "
    "handler code. This separates UI components from business logic, "
    "enables multiple listeners per source, and improves code maintainability."
)

pn.highlight(
    "<b>Q2. Differentiate between the old and new event handling mechanisms.</b><br/>"
    "A: Old Model (Java 1.0): Component overrides action() or handleEvent(). "
    "Event source and handler are the same object. All events bubble up regardless of interest. "
    "Inefficient for large GUIs. NOT recommended. "
    "New Model (Java 1.1+): Event source delegates to separate listener objects. "
    "Source registers listeners. AWT calls listener callbacks only for registered types. "
    "Clean separation. Current standard."
)

pn.highlight(
    "<b>Q3. What is an Event Listener? Give two examples.</b><br/>"
    "A: An event listener is a Java interface that defines callback method(s) to be invoked "
    "when a specific type of event occurs. A class implements the listener interface and is "
    "registered with a source via addXxxListener(). "
    "Examples: (1) ActionListener -- one method: actionPerformed(ActionEvent e), "
    "handles button clicks and menu selections. "
    "(2) MouseListener -- five methods: mouseClicked, mousePressed, mouseReleased, "
    "mouseEntered, mouseExited, handles all mouse button events."
)

pn.highlight(
    "<b>Q4. What is an Adapter class? Why is it used?</b><br/>"
    "A: An Adapter class implements a listener interface with all methods having "
    "empty (no-op) bodies. It is used when you only need to handle one or two "
    "of the many methods defined in a multi-method listener interface. "
    "Example: WindowAdapter implements all 7 WindowListener methods as empty. "
    "You extend WindowAdapter and override only windowClosing(), saving from writing "
    "6 empty method bodies required if directly implementing WindowListener."
)

pn.highlight(
    "<b>Q5. What is JDBC? What is its main advantage?</b><br/>"
    "A: JDBC (Java Database Connectivity) is a Java API in the java.sql package "
    "that provides a standard way for Java programs to connect to and interact with "
    "relational databases. Its main advantage is <b>database independence</b>: "
    "the same Java code works with different databases (MySQL, Oracle, PostgreSQL) "
    "by simply changing the JDBC driver JAR file and connection URL, "
    "without modifying the application code."
)

pn.highlight(
    "<b>Q6. What is the JDBC-ODBC Bridge? Why is it deprecated?</b><br/>"
    "A: The JDBC-ODBC Bridge (Type 1 driver) translated JDBC calls to ODBC calls "
    "which then communicated with the database. It required an ODBC driver to be "
    "installed on the client machine (Windows-specific) and was very slow due to "
    "two translation layers. It was deprecated in Java 7 and removed in Java 8 "
    "because Type 4 (pure Java) drivers are faster, portable, and cross-platform."
)

pn.highlight(
    "<b>Q7. What is DriverManager in JDBC?</b><br/>"
    "A: DriverManager (java.sql.DriverManager) is the management layer in JDBC that "
    "maintains a list of registered JDBC drivers and selects the appropriate one "
    "when a connection is requested. The key method is: "
    "<code>Connection conn = DriverManager.getConnection(url, user, password);</code> "
    "It searches registered drivers for one that understands the URL format "
    "(e.g., jdbc:mysql:// is handled by the MySQL JDBC driver)."
)

pn.highlight(
    "<b>Q8. What is a PreparedStatement? How does it prevent SQL injection?</b><br/>"
    "A: PreparedStatement is a pre-compiled SQL statement with <code>?</code> placeholders. "
    "Created with <code>conn.prepareStatement(sql)</code> and parameters set with "
    "setInt(), setString(), etc. "
    "SQL Injection prevention: parameters are sent separately from the SQL structure "
    "and the driver handles escaping/quoting automatically. "
    "Even if a user enters <code>' OR '1'='1</code>, it is treated as a literal string "
    "value, NOT as SQL syntax -- the query structure cannot be altered."
)

pn.highlight(
    "<b>Q9. What is a ResultSet? How do you navigate it?</b><br/>"
    "A: ResultSet is a table of data returned by executeQuery(). "
    "It has a cursor initially positioned before the first row. "
    "Navigation: next() moves to next row (returns false when past last row). "
    "For scrollable ResultSet (TYPE_SCROLL_INSENSITIVE): previous(), first(), last(), "
    "absolute(n), relative(n). "
    "Data retrieval: getString('colName'), getInt('colName'), getDouble('colName'). "
    "Always close with rs.close() when done."
)

pn.highlight(
    "<b>Q10. What is SQLException? What information does it carry?</b><br/>"
    "A: SQLException is the primary JDBC exception (extends Exception -- checked). "
    "It carries three pieces of database error information: "
    "(1) getMessage() -- human-readable error description. "
    "(2) getSQLState() -- 5-character XOPEN/SQL standard state code (e.g., '42S02' = table not found). "
    "(3) getErrorCode() -- vendor-specific integer error number (e.g., MySQL 1146 = table not found). "
    "SQLExceptions can be chained (getNextException())."
)

pn.section("5-Mark Questions (Explain with Code)")

pn.highlight(
    "<b>Q11. Explain the delegation event model with a complete code example.</b><br/>"
    "A: Three roles -- Source (Button), Event Object (ActionEvent), Listener (ActionListener). "
    "Source generates event when user clicks. AWT creates ActionEvent with source, command, timestamp. "
    "AWT calls actionPerformed(e) on all registered listeners. "
    "Code: Create Button (source); implement ActionListener (listener); "
    "register with btn.addActionListener(listener); "
    "actionPerformed() gets called with ActionEvent -- read e.getActionCommand(). "
    "See DelegationModelDemo in Section 5.2."
)

pn.highlight(
    "<b>Q12. Write a Java program to handle mouse events -- display coordinates on click, "
    "change color on enter/exit.</b><br/>"
    "A: Implement MouseListener on a Frame or Panel. "
    "In mouseClicked(e): record e.getX(), e.getY(); call repaint() to draw crosshair. "
    "In mouseEntered(e): setBackground(Color.YELLOW); repaint(). "
    "In mouseExited(e): setBackground(Color.WHITE); repaint(). "
    "In paint(g): drawString with coordinates; draw crosshair at click point. "
    "Register with addMouseListener(this). "
    "See MouseEventDemo in Section 5.6 for the complete program."
)

pn.highlight(
    "<b>Q13. Write a Java program to handle keyboard events -- display each key pressed.</b><br/>"
    "A: Implement KeyListener on a Frame (or any focusable component). "
    "keyPressed(e): e.getKeyCode() for VK constant; KeyEvent.getKeyText(code) for name; "
    "check isControlDown(), isShiftDown(); detect Escape, Enter. "
    "keyTyped(e): e.getKeyChar() for the printable character typed. "
    "keyReleased(e): fires when key is lifted. "
    "Call requestFocus() on the component to ensure it receives key events. "
    "See KeyEventDemo in Section 5.7."
)

pn.highlight(
    "<b>Q14. Write a JDBC program to connect to MySQL and perform SELECT, INSERT, UPDATE, DELETE.</b><br/>"
    "A: Step 1: Get connection: DriverManager.getConnection(url, user, password). "
    "Step 2: Create Statement: conn.createStatement(). "
    "Step 3 INSERT: stmt.executeUpdate('INSERT INTO ... VALUES ...'). "
    "Step 4 SELECT: ResultSet rs = stmt.executeQuery('SELECT * FROM ...'); while(rs.next()) { rs.getString(), rs.getInt() }. "
    "Step 5 UPDATE: stmt.executeUpdate('UPDATE ... SET ... WHERE ...'). "
    "Step 6 DELETE: stmt.executeUpdate('DELETE FROM ... WHERE ...'). "
    "Step 7: rs.close(); stmt.close(); conn.close(). "
    "See JDBCDemo in Section 5.10."
)

pn.highlight(
    "<b>Q15. Explain ResultSet navigation methods with a scrollable ResultSet example.</b><br/>"
    "A: Standard (forward only): rs.next() moves to next row. "
    "For scrollable: conn.createStatement(TYPE_SCROLL_INSENSITIVE, CONCUR_READ_ONLY). "
    "Navigation: first() -- first row; last() -- last row; previous() -- back one; "
    "absolute(n) -- jump to row n (n=-1 for last); relative(n) -- move n rows from current; "
    "beforeFirst() -- before row 1; afterLast() -- after last row; getRow() -- current row number. "
    "See ScrollableResultSetDemo in Section 5.11."
)

pn.section("10-Mark Questions (Detailed Programs)")

pn.highlight(
    "<b>Q16. Write a complete Java program demonstrating all mouse and keyboard event "
    "listeners. Show: click coordinates, drag path, key names, Ctrl+key combinations.</b><br/>"
    "A: Combine MouseListener + MouseMotionListener + KeyListener on one Frame. "
    "Mouse: track clicks (coordinates, count), drag (path drawing with ArrayList), "
    "enter/exit (color change). "
    "Key: keyPressed gets VK code + modifier check (Ctrl, Shift, Alt); "
    "keyTyped gets printable char; Escape clears; Enter submits. "
    "Use TextArea or paint() to display event log. "
    "See MouseEventDemo (Sec 5.6) and KeyEventDemo (Sec 5.7) and combine them."
)

pn.highlight(
    "<b>Q17. Explain the Delegation Event Model in detail. "
    "What are Event Sources, Event Objects, and Listeners? "
    "Explain each with an example and diagram.</b><br/>"
    "A: EVENT SOURCE = component that fires events (Button fires ActionEvent). "
    "EVENT OBJECT = instance of EventObject subclass containing all event data "
    "(ActionEvent carries command string, timestamp, modifiers). "
    "EVENT LISTENER = interface with callback methods (ActionListener.actionPerformed). "
    "FLOW: User action -> Source creates EventObject -> AWT dispatches to registered listeners "
    "-> listener.callbackMethod(event) executes. "
    "See Fig 5.1 sequence diagram and DelegationModelDemo code in Sections 5.2-5.4."
)

pn.highlight(
    "<b>Q18. Write a complete JDBC application that: connects to MySQL, "
    "creates a table if not exists, inserts 5 records, displays all records, "
    "searches by name using PreparedStatement, and handles all exceptions.</b><br/>"
    "A: (1) getConnection(url, user, pwd). "
    "(2) executeUpdate CREATE TABLE IF NOT EXISTS. "
    "(3) PreparedStatement for INSERT with 5 sets of setString/setDouble calls. "
    "(4) executeQuery SELECT and while(rs.next()) display. "
    "(5) PreparedStatement for SELECT WHERE name LIKE ? with setString(1, '%Rahul%'). "
    "(6) Catch SQLException: print getMessage(), getSQLState(), getErrorCode(). "
    "(7) Finally block closes all resources. See JDBCDemo and PreparedStatementDemo."
)

pn.highlight(
    "<b>Q19. Explain JDBC exception classes. Write code to handle SQLException, "
    "SQLWarning, and BatchUpdateException. Include transaction management.</b><br/>"
    "A: SQLException: catch(SQLException e) { e.getMessage(), getSQLState(), getErrorCode(), for(Throwable t: e) chain. }. "
    "SQLWarning: conn.getWarnings() or stmt.getWarnings() -- iterate with getNextWarning(). "
    "BatchUpdateException: stmt.addBatch(); then try { executeBatch(); commit(); } "
    "catch (BatchUpdateException b) { getUpdateCounts() array; conn.rollback(); }. "
    "Transaction: conn.setAutoCommit(false); ... conn.commit() or conn.rollback(). "
    "See ExceptionHandlingDemo in Section 5.12."
)

pn.highlight(
    "<b>Q20. Compare the four types of JDBC drivers. Which one is preferred and why? "
    "Write a program to connect to a remote MySQL database and perform CRUD operations.</b><br/>"
    "A: Type 1 (JDBC-ODBC Bridge): deprecated, Windows-only, slow. "
    "Type 2 (Native API): fast but requires native client lib. "
    "Type 3 (Net Protocol): middleware-based, no native lib. "
    "Type 4 (Pure Java/Thin): preferred -- no native libs, cross-platform, direct DB protocol. "
    "Remote URL: jdbc:mysql://192.168.1.100:3306/college_db?useSSL=false. "
    "CRUD: executeUpdate for INSERT/UPDATE/DELETE; executeQuery + ResultSet for SELECT. "
    "Use PreparedStatement for safety. See PreparedStatementDemo in Section 5.13."
)

pn.section("Quick Revision Summary Table")
pn.info_table(
    ["Topic", "Key Exam Points"],
    [
        [
            "Old event model",
            "Java 1.0 -- component overrides action(). All events go to same method. Inefficient. Replaced by delegation.",
        ],
        [
            "New delegation model",
            "Java 1.1+ -- Source fires event to registered Listener. Three roles: Source, EventObject, Listener.",
        ],
        [
            "Event source",
            "Component that generates events. Provides addXxxListener() and removeXxxListener().",
        ],
        [
            "Event object",
            "Carries event data. All extend java.util.EventObject. AWT events extend AWTEvent with getID().",
        ],
        [
            "ActionListener",
            "1 method: actionPerformed(ActionEvent e). e.getActionCommand() = button label. No adapter.",
        ],
        [
            "MouseListener",
            "5 methods: Clicked, Pressed, Released, Entered, Exited. Adapter: MouseAdapter.",
        ],
        [
            "MouseMotionListener",
            "2 methods: mouseMoved, mouseDragged. Adapter: MouseMotionAdapter.",
        ],
        [
            "KeyListener",
            "3 methods: keyPressed, keyReleased, keyTyped. keyTyped only fires for printable chars. Adapter: KeyAdapter.",
        ],
        [
            "KeyEvent VK codes",
            "VK_ENTER, VK_ESCAPE, VK_SPACE, VK_UP/DOWN/LEFT/RIGHT, VK_F1-F12, VK_A-Z, VK_0-9.",
        ],
        [
            "Adapter classes",
            "Implement listener with empty methods. Extend adapter to override only needed methods. WindowAdapter most common.",
        ],
        [
            "JDBC-ODBC bridge",
            "Type 1 driver. Deprecated. Required ODBC driver. Removed in Java 8. Class.forName('sun.jdbc.odbc.JdbcOdbcDriver').",
        ],
        [
            "JDBC driver types",
            "Type 1=ODBC bridge (deprecated), Type 2=Native API, Type 3=Net protocol, Type 4=Pure Java (preferred).",
        ],
        [
            "JDBC 6 steps",
            "1.Load driver 2.getConnection 3.createStatement 4.executeQuery/Update 5.Process ResultSet 6.close all.",
        ],
        [
            "DriverManager",
            "getConnection(url, user, pwd) returns Connection. Selects the correct registered driver from URL prefix.",
        ],
        [
            "Connection URL",
            "jdbc:mysql://host:port/db for MySQL. jdbc:oracle:thin:@host:port:sid for Oracle.",
        ],
        [
            "Statement",
            "executeQuery(sql) returns ResultSet. executeUpdate(sql) returns int rowCount.",
        ],
        [
            "PreparedStatement",
            "conn.prepareStatement(sql with ?). setString/Int/Double(1, val). Prevents SQL injection. Reusable.",
        ],
        [
            "ResultSet",
            "Cursor before first row. next() advances. getString/Int/Double('colName'). Close with rs.close().",
        ],
        [
            "Scrollable ResultSet",
            "TYPE_SCROLL_INSENSITIVE + CONCUR_READ_ONLY. Enables previous(), first(), last(), absolute(n).",
        ],
        [
            "SQLException",
            "getMessage(), getSQLState() (5-char code), getErrorCode() (vendor int). Iterable for chain.",
        ],
        [
            "SQLWarning",
            "Non-fatal. conn.getWarnings() or stmt.getWarnings(). Chain with getNextWarning().",
        ],
        [
            "BatchUpdateException",
            "Extends SQLException. executeBatch() fails. getUpdateCounts() shows per-statement rows.",
        ],
        [
            "Transaction",
            "conn.setAutoCommit(false); ... conn.commit() or conn.rollback() in catch.",
        ],
        [
            "try-with-resources",
            "try(Connection c=...; Statement s=...) { } catches and auto-closes. Recommended for JDBC.",
        ],
    ],
)

pn.tip(
    "Exam must-know programs: "
    "(1) Complete event demo with Button + MouseListener + KeyListener. "
    "(2) JDBC with all CRUD operations (INSERT, SELECT, UPDATE, DELETE). "
    "(3) PreparedStatement with parameterized query. "
    "(4) ResultSet navigation with scrollable type. "
    "Always remember to close ResultSet, Statement, and Connection in that exact order "
    "in a finally block, or use try-with-resources."
)

# =============================================================================
#  BUILD DOCUMENT
# =============================================================================
pn.build_doc("Java_Unit5_Notes.pdf")
print("Generated: Java_Unit5_Notes.pdf")

pn.build_html("java_unit5_html")
print("Generated: java_unit5_html")
