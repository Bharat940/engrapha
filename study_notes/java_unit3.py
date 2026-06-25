"""
Java Programming (IT408) -- Unit III Notes
UIT-RGPV (Autonomous) Bhopal | Semester IV
Complete exam notes on Java Applets with diagrams, code examples, and exam questions.
Run: python java_unit3_notes.py
Output: Java_Unit3_Notes.pdf
"""

from __future__ import annotations

import paperforge_notes as pn
import paperforge_diagrams as pd

# =============================================================================
#  THEME & GLOBAL FOOTER SETUP
#  Using FOREST_DARK theme -- green accent on dark charcoal
#  Different from Unit I (Catppuccin Mocha) and Unit II (Midnight Dark)
# =============================================================================
pn.set_story([])
pn.set_theme(pn.FOREST_DARK)

pn.set_global_footer(
    left="Java Programming (IT408) -- Unit III",
    right="UIT-RGPV (Autonomous) Bhopal",
    show_page_num=True,
)

# Sync diagram theme with notes theme
diag_theme = pd.DiagramTheme.from_notes_theme(pn.get_theme())

# =============================================================================
#  COVER PAGE
# =============================================================================
pn.bookmark("Cover Page")
pn.suppress_footer(page_only=True)
pn.sp(26)

pn.cover_card(
    "JAVA PROGRAMMING",
    "Unit III -- The Applet Class & Applet Programming",
)
pn.cover_subtitle(
    [
        "Subject Code: IT408  |  UIT-RGPV (Autonomous) Bhopal  |  Semester IV",
        "Complete Exam Notes: Applet Basics, Lifecycle, Architecture, HTML Tag,",
        "Display Methods, Banner Applet, Status Window, Parameters, and Exam Questions",
    ]
)
pn.sp(10)
pn.rule(pn.get_theme().rl(pn.get_theme().accent), 1.5)
pn.sp(8)

pn.info_table(
    ["Section", "Syllabus Topics Covered"],
    [
        [
            "3.1 Applet Basics",
            "What is an Applet, Applet vs Application, History, java.applet package",
        ],
        [
            "3.2 The Applet Class",
            "Class hierarchy, Applet class methods, AppletContext, AudioClip",
        ],
        [
            "3.3 Applet Architecture",
            "Browser-JVM-Applet interaction, event-driven model, paint/repaint",
        ],
        [
            "3.4 Initialization & Termination",
            "Lifecycle: init, start, stop, destroy -- full sequence with diagram",
        ],
        [
            "3.5 Simple Display Methods",
            "Graphics class, drawString, drawRect, drawOval, setColor, setFont",
        ],
        [
            "3.6 Simple Banner Applet",
            "Scrolling text using Thread, run(), sleep(), repaint(), update()",
        ],
        [
            "3.7 Using the Status Window",
            "showStatus() method, browser status bar usage with mouse events",
        ],
        [
            "3.8 The HTML APPLET Tag",
            "code, width, height, codebase, archive, name, alt attributes",
        ],
        [
            "3.9 Passing Parameters",
            "HTML param tag, getParameter(), null checking, type conversion",
        ],
        [
            "3.10 Improving the Banner",
            "Speed/color via params, pause/resume, multi-ad rotation, flicker fix",
        ],
        [
            "3.11 Exam Questions",
            "20 exam-style questions with detailed answers covering all topics",
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
pn.part_box("UNIT III -- THE APPLET CLASS & APPLET PROGRAMMING")

# =============================================================================
#  3.1  APPLET BASICS
# =============================================================================
pn.chap_box("3.1  Applet Basics")
pn.section("What is a Java Applet?")
pn.definition(
    "<b>Applet:</b> A small Java program designed to be embedded inside a web page "
    "and executed by a Java-enabled web browser or the <code>appletviewer</code> tool. "
    "Applets are downloaded over the internet along with the HTML page and run on the "
    "client machine inside the browser's JVM. Unlike standalone applications, an applet "
    "has NO <code>main()</code> method -- instead, the browser controls its lifecycle "
    "through special lifecycle methods: <code>init()</code>, <code>start()</code>, "
    "<code>stop()</code>, and <code>destroy()</code>. "
    "Applets are declared <b>deprecated since Java 9</b> and <b>removed in Java 17</b>."
)

pn.section("Applet vs Java Application -- Key Differences")
pn.info_table(
    ["Feature", "Java Applet", "Standalone Java Application"],
    [
        [
            "Entry Point",
            "No main(); uses init(), start() lifecycle methods",
            "public static void main(String[] args) required",
        ],
        [
            "Execution Host",
            "Runs inside a web browser or appletviewer",
            "Runs directly on JVM via java command",
        ],
        [
            "GUI",
            "Automatically has a graphical panel inside browser window",
            "Must create GUI manually (Swing/AWT) or use console",
        ],
        [
            "Security",
            "Sandboxed -- cannot access local file system, network freely",
            "Full access to system resources, files, network",
        ],
        [
            "HTML",
            "Requires <applet> or <object> tag in HTML to launch",
            "No HTML required -- launched from command line",
        ],
        [
            "Superclass",
            "Must extend java.applet.Applet (or JApplet)",
            "No required superclass",
        ],
        [
            "Deployment",
            "Downloaded from web server and cached on client",
            "Distributed as .jar or .class files",
        ],
        ["Status (2026)", "Deprecated and removed (Java 17+)", "Standard and current"],
    ],
)

pn.section("Brief History and Context")
pn.bullet(
    [
        "<b>1995:</b> Java 1.0 introduced Applets as the defining feature for interactive web content.",
        "<b>1996-2000:</b> Peak popularity -- animations, games, and interactive forms used Applets widely.",
        "<b>2010-2015:</b> HTML5, CSS3, and JavaScript improvements began replacing Applet use cases. Chrome, Firefox dropped plugin support.",
        "<b>2017:</b> Java 9 officially marked Applets as <code>@Deprecated</code> for removal.",
        "<b>2021:</b> Java 17 removed the <code>java.applet</code> package and appletviewer tool entirely.",
        "<b>Modern Alternatives:</b> HTML5 Canvas, WebGL, JavaScript frameworks (React, Angular), and JavaFX for desktop apps.",
    ]
)

pn.note(
    "Despite being deprecated, Java Applets remain a core topic in the IT408 syllabus at UIT-RGPV. "
    "All exam questions should be answered using the classic <code>java.applet.Applet</code> API "
    "with AWT Graphics. Use <code>appletviewer</code> to test applet code on your local machine."
)
pn.br()

# =============================================================================
#  3.2  THE APPLET CLASS
# =============================================================================
pn.chap_box("3.2  The Applet Class")
pn.section("Class Hierarchy")
pn.body(
    "Every applet must directly or indirectly extend the <code>java.applet.Applet</code> class. "
    "This class itself inherits from the AWT component hierarchy, which is why an applet "
    "automatically has a visual panel and can use Graphics drawing methods."
)

pn.section("Key Methods of the Applet Class")
pn.info_table(
    ["Method", "Return Type", "Description"],
    [
        [
            "init()",
            "void",
            "Called once when applet loads. Override for one-time setup: initialize variables, create UI components, load images.",
        ],
        [
            "start()",
            "void",
            "Called after init() and whenever user returns to page. Override to start/resume threads.",
        ],
        [
            "stop()",
            "void",
            "Called when user leaves page. Override to pause threads and save CPU.",
        ],
        [
            "destroy()",
            "void",
            "Called once before applet is removed from memory. Override for final cleanup.",
        ],
        [
            "paint(Graphics g)",
            "void",
            "Called by AWT to draw the applet. Override to draw text, shapes, images.",
        ],
        [
            "repaint()",
            "void",
            "Schedules a repaint (calls update() -> paint()). Call when data changes.",
        ],
        [
            "update(Graphics g)",
            "void",
            "Default clears background then calls paint(). Override to prevent flicker.",
        ],
        [
            "getParameter(name)",
            "String",
            "Reads a <param> value from HTML. Returns null if not found.",
        ],
        [
            "showStatus(msg)",
            "void",
            "Displays message in browser's status bar at bottom.",
        ],
        [
            "getAppletContext()",
            "AppletContext",
            "Returns the AppletContext for inter-applet communication.",
        ],
        [
            "getImage(URL, name)",
            "Image",
            "Loads an image from the given URL for display.",
        ],
        [
            "getAudioClip(URL)",
            "AudioClip",
            "Loads an audio clip from the given URL for playback.",
        ],
        ["getWidth()", "int", "Returns current applet panel width in pixels."],
        ["getHeight()", "int", "Returns current applet panel height in pixels."],
        [
            "getCodeBase()",
            "URL",
            "Returns URL of the directory containing the applet's .class file.",
        ],
        [
            "getDocumentBase()",
            "URL",
            "Returns URL of the HTML document that contains the applet.",
        ],
    ],
)

# UML class diagram showing Applet hierarchy
cd_hier = pd.ClassDiagram(
    width=pn.CW,
    height=None,
    theme=diag_theme,
    caption="Fig 3.1: Java Applet class inheritance hierarchy",
    class_w=140,
)
cd_hier.uml_class(
    "Object",
    "java.lang.Object",
    methods=["+ toString(): String", "+ equals(obj): boolean"],
)
cd_hier.uml_class(
    "Component",
    "java.awt.Component",
    methods=[
        "+ paint(g: Graphics): void",
        "+ repaint(): void",
        "+ setBackground(c): void",
    ],
)
cd_hier.uml_class(
    "Container",
    "java.awt.Container",
    methods=["+ add(comp): void", "+ setLayout(lm): void"],
)
cd_hier.uml_class(
    "Panel",
    "java.awt.Panel",
    methods=["+ Panel()"],
)
cd_hier.uml_class(
    "Applet",
    "java.applet.Applet",
    methods=[
        "+ init(): void",
        "+ start(): void",
        "+ stop(): void",
        "+ destroy(): void",
        "+ getParameter(name): String",
        "+ showStatus(msg): void",
    ],
)
cd_hier.uml_class(
    "MyApplet",
    "MyApplet (Your Class)",
    methods=["+ init(): void", "+ paint(g): void"],
)
cd_hier.relate("Component", "Object", kind="inheritance")
cd_hier.relate("Container", "Component", kind="inheritance")
cd_hier.relate("Panel", "Container", kind="inheritance")
cd_hier.relate("Applet", "Panel", kind="inheritance")
cd_hier.relate("MyApplet", "Applet", kind="inheritance")
pn.story.extend(cd_hier.as_flowable())

pn.section("Minimal Applet Structure")
pn.code_block(
    """
// MinimalApplet.java -- The bare minimum structure of every Java applet
// Step 1: Import required packages
import java.applet.Applet;   // contains the Applet base class
import java.awt.Graphics;    // contains Graphics drawing context

// Step 2: Class must extend Applet (required -- not optional)
// The 'public' modifier is required for the browser to access the class
public class MinimalApplet extends Applet {

    // Step 3: Override lifecycle methods as needed
    // init() -- called ONCE when applet loads into browser memory
    @Override
    public void init() {
        // One-time initialization: set background, load resources, etc.
        setBackground(java.awt.Color.WHITE);
    }

    // Step 4: Override paint() to draw content
    // 'g' is the Graphics object provided by the AWT system
    @Override
    public void paint(Graphics g) {
        // drawString(text, x, y) -- x=left edge, y=baseline of text
        g.drawString("Minimal Java Applet is running!", 30, 60);
    }

    // NOTE: start(), stop(), destroy() are inherited from Applet
    // with empty bodies -- only override them if your applet needs them
}

// =====================================================
// CORRESPONDING HTML FILE (save as MinimalApplet.html)
// =====================================================
// <html>
// <body>
//   <applet code="MinimalApplet.class" width="350" height="120">
//     Browser does not support Java applets.
//   </applet>
// </body>
// </html>
//
// TO COMPILE AND RUN:
//   javac MinimalApplet.java
//   appletviewer MinimalApplet.html
""",
    lang="java",
)
pn.br()

# =============================================================================
#  3.3  APPLET ARCHITECTURE
# =============================================================================
pn.chap_box("3.3  Applet Architecture")
pn.section("Browser-JVM-Applet Interaction")
pn.definition(
    "<b>Applet Architecture:</b> The structural design describing how a web browser, "
    "the Java Virtual Machine (JVM), and the applet code interact. "
    "When a browser encounters the <code>&lt;applet&gt;</code> tag in an HTML page, "
    "it downloads the compiled <code>.class</code> file from the web server, "
    "starts an embedded JVM (Java Plugin), creates an instance of the applet class, "
    "and invokes the lifecycle methods in sequence to initialize, run, and terminate the applet."
)

# Network diagram showing the full applet architecture
net_arch = pd.NetworkDiagram(
    width=pn.CW,
    height=320,
    theme=diag_theme,
    caption="Fig 3.2: Complete Applet Architecture -- browser downloads, JVM runs, AWT renders",
)
net_arch.node("user", "Client Machine", x=60, y=250, kind="host")
net_arch.node("browser", "Web Browser", x=230, y=250, kind="server")
net_arch.node("websvr", "Web Server\nHTML + class", x=420, y=250, kind="cloud")
net_arch.node("jvm", "JVM Plugin\ninside browser", x=230, y=155, kind="generic")
net_arch.node("applet", "Applet Instance", x=135, y=60, kind="database")
net_arch.node("awt", "AWT Rendering\nGraphics engine", x=325, y=60, kind="storage")

net_arch.link("user", "browser", label="opens URL")
net_arch.link("browser", "websvr", label="GET files")
net_arch.link("browser", "jvm", label="loads plugin")
net_arch.link("jvm", "applet", label="creates object")
net_arch.link("applet", "awt", label="paint(g)")
pn.story.extend(net_arch.as_flowable())

pn.section("Event-Driven Model")
pn.body(
    "Applets follow an <b>event-driven programming model</b> -- rather than running sequentially "
    "from top to bottom like a script, an applet sits idle waiting for events. "
    "Events can be triggered by the browser (lifecycle events), by the user (mouse clicks, "
    "key presses), or by internal timers (threads calling repaint). "
    "The AWT system dispatches events to registered listener methods."
)
pn.bullet(
    [
        "<b>Lifecycle Events:</b> Triggered by browser -- init, start, stop, destroy called automatically.",
        "<b>Paint Events:</b> Triggered by AWT when applet needs to redraw -- calls update() -> paint().",
        "<b>Mouse Events:</b> Triggered by user -- mouseClicked, mouseMoved, mouseDragged, etc.",
        "<b>Key Events:</b> Triggered by keyboard input -- keyPressed, keyReleased, keyTyped.",
        "<b>Action Events:</b> Triggered by UI controls -- button clicks, menu selections.",
        "<b>Timer Events:</b> Triggered by a Thread using sleep() + repaint() to animate content.",
    ]
)

pn.section("The paint() and repaint() Relationship")
pn.body(
    "Understanding the difference between <code>paint()</code>, <code>update()</code>, "
    "and <code>repaint()</code> is critical for writing smooth applets."
)
pn.info_table(
    ["Method", "Who Calls It", "What It Does"],
    [
        [
            "paint(Graphics g)",
            "AWT system -- you should NOT call it directly",
            "Draws the applet content. Receives a Graphics context. Override this to draw.",
        ],
        [
            "repaint()",
            "You call this in your code when data changes",
            "Requests AWT to schedule a redraw. AWT calls update() -> paint() on the next paint cycle.",
        ],
        [
            "update(Graphics g)",
            "AWT calls this after repaint(); default clears screen then calls paint()",
            "Default implementation clears entire background then calls paint(). Override to prevent screen flash/flicker in animations.",
        ],
    ],
)

pn.code_block(
    """
// FlickerFix.java -- Override update() to prevent flickering in animations
public class FlickerFix extends java.applet.Applet implements Runnable {

    int x = 0;

    public void start() {
        new Thread(this).start();
    }

    public void run() {
        while (true) {
            x += 2;                          // advance position
            if (x > getWidth()) x = 0;       // wrap around
            repaint();                        // schedule redraw
            try { Thread.sleep(30); } catch (InterruptedException e) { break; }
        }
    }

    // Override update() to draw WITHOUT clearing first (prevents white flash)
    @Override
    public void update(java.awt.Graphics g) {
        // Manually fill only the needed area instead of wiping entire screen
        g.setColor(getBackground());
        g.fillRect(0, 0, getWidth(), getHeight());
        paint(g);  // now draw the new frame on the clean background
    }

    @Override
    public void paint(java.awt.Graphics g) {
        g.setColor(java.awt.Color.RED);
        g.fillOval(x, 40, 30, 30);           // draw moving ball
    }
}
""",
    lang="java",
)
pn.br()

# =============================================================================
#  3.4  APPLET LIFECYCLE -- INIT, START, STOP, DESTROY
# =============================================================================
pn.chap_box("3.4  Applet Initialization and Termination")
pn.section("The Four Lifecycle Methods")
pn.definition(
    "<b>Applet Lifecycle:</b> The sequence of states and transitions an applet goes through "
    "from the moment it is first loaded into the browser to the moment it is permanently "
    "removed from memory. The browser (or appletviewer) controls this lifecycle by calling "
    "four special methods in a defined order. Understanding this sequence is essential for "
    "writing correct applets that properly initialize, run, pause, and clean up."
)

pn.info_table(
    ["Method", "Called When", "Purpose", "Call Frequency"],
    [
        [
            "init()",
            "Applet class loaded into memory for the first time",
            "One-time setup: initialize variables, create UI components, register event listeners, load images/audio. Equivalent to a constructor.",
            "EXACTLY ONCE per applet lifetime",
        ],
        [
            "start()",
            "Immediately after init(); also every time user navigates BACK to the page",
            "Begin or resume execution: start background threads, resume animation, resume audio playback.",
            "MULTIPLE TIMES (once per page visit)",
        ],
        [
            "stop()",
            "User navigates AWAY from page (browser leaves) OR minimizes window",
            "Pause execution: stop threads, pause animation, mute audio to save CPU while not visible.",
            "MULTIPLE TIMES (once per page leave)",
        ],
        [
            "destroy()",
            "Browser closes tab permanently OR applet is being removed from memory",
            "Final cleanup: close files, release streams, stop all threads permanently.",
            "EXACTLY ONCE per applet lifetime",
        ],
    ],
)

pn.section("Complete Lifecycle State Diagram")

# State machine showing full applet lifecycle
sm_life = pd.StateMachine(
    width=pn.CW,
    height=250,
    theme=diag_theme,
    caption="Fig 3.3: Applet lifecycle state transitions -- init, start, stop, destroy",
)
sm_life.state("loaded", "LOADED", initial=True)
sm_life.state("init", "INITIALIZED")
sm_life.state("running", "RUNNING")
sm_life.state("stopped", "STOPPED")
sm_life.state("destroyed", "DESTROYED", accepting=True)

sm_life.transition("loaded", "init", label="browser calls\ninit()")
sm_life.transition("init", "running", label="browser calls\nstart()")
sm_life.transition("running", "stopped", label="user leaves page\nbrowser calls stop()")
sm_life.transition("stopped", "running", label="user returns\nbrowser calls start()")
sm_life.transition("stopped", "destroyed", label="tab closed\nbrowser calls\ndestroy()")
sm_life.transition(
    "running", "destroyed", label="direct close\ncalls stop() +\ndestroy()"
)
pn.story.extend(sm_life.as_flowable())

pn.section("Lifecycle in Code -- Full Demonstration")
pn.code_block(
    """
// LifecycleDemo.java -- Demonstrates all four lifecycle methods
import java.applet.Applet;
import java.awt.*;

public class LifecycleDemo extends Applet {

    // Instance variable to track current lifecycle state for display
    String currentState = "Not yet started";
    int initCount = 0, startCount = 0, stopCount = 0;

    // STEP 1: init() -- called ONCE when applet class is first loaded
    @Override
    public void init() {
        initCount++;
        currentState = "INITIALIZED (init called " + initCount + " time)";
        setBackground(Color.LIGHT_GRAY);
        setFont(new Font("Arial", Font.BOLD, 14));

        // init() is the right place to:
        // - Set applet size preference: resize(300, 200)
        // - Read HTML parameters: getParameter("name")
        // - Create and add UI components (buttons, text fields)
        // - Register event listeners
        // - Load images: getImage(getCodeBase(), "logo.png")

        System.out.println("[LIFECYCLE] init() called.");
        repaint();
    }

    // STEP 2: start() -- called after init() AND every return visit
    @Override
    public void start() {
        startCount++;
        currentState = "RUNNING (start called " + startCount + " times)";

        // start() is the right place to:
        // - Create and start background threads
        // - Begin animation loops
        // - Resume audio playback

        System.out.println("[LIFECYCLE] start() called.");
        repaint();
    }

    // STEP 3: stop() -- called every time user leaves the page
    @Override
    public void stop() {
        stopCount++;
        currentState = "STOPPED (stop called " + stopCount + " times)";

        // stop() is the right place to:
        // - Interrupt/null background threads to pause animation
        // - Pause or mute audio
        // - Save state that should persist across revisits

        System.out.println("[LIFECYCLE] stop() called.");
    }

    // STEP 4: destroy() -- called ONCE when applet is removed
    @Override
    public void destroy() {
        currentState = "DESTROYED -- applet terminated";

        // destroy() is the right place to:
        // - Close file streams and network connections
        // - Stop ALL threads permanently
        // - Release native resources (images, audio)
        // - Perform any final state persistence

        System.out.println("[LIFECYCLE] destroy() called.");
        repaint();
    }

    // paint() -- draws the current state on the applet panel
    @Override
    public void paint(Graphics g) {
        // Draw state information for visual tracking
        g.setColor(Color.DARK_GRAY);
        g.drawRect(10, 10, getWidth()-20, getHeight()-20);

        g.setColor(Color.BLUE);
        g.drawString("Current State:", 20, 50);
        g.setColor(Color.RED);
        g.drawString(currentState, 20, 80);

        g.setColor(Color.BLACK);
        g.drawString("init() count:    " + initCount, 20, 120);
        g.drawString("start() count:   " + startCount, 20, 145);
        g.drawString("stop() count:    " + stopCount, 20, 170);
        g.drawString("Lifecycle order: init -> start -> [stop -> start] -> stop -> destroy", 20, 205);
    }
}
""",
    lang="java",
)

pn.section("Lifecycle Sequence Diagram")
# Sequence diagram showing browser-to-applet calls
seq_life = pd.SequenceDiagram(
    width=pn.CW,
    height=310,
    theme=diag_theme,
    caption="Fig 3.4: Browser calling applet lifecycle methods in sequence",
)
seq_life.actor("browser", "Web Browser")
seq_life.actor("jvm", "JVM / Plugin")
seq_life.actor("applet", "AppletInstance")

seq_life.message("browser", "jvm", "load .class file from server", arrow="solid")
seq_life.message("jvm", "applet", "new AppletClass()", arrow="solid")
seq_life.activate("applet")
seq_life.message("jvm", "applet", "init()", arrow="solid")
seq_life.message("applet", "jvm", "one-time setup done", arrow="dashed")
seq_life.message("jvm", "applet", "start()", arrow="solid")
seq_life.message("applet", "jvm", "execution started", arrow="dashed")

seq_life.divider("User Leaves Page")
seq_life.message("browser", "jvm", "page hidden / navigated away", arrow="solid")
seq_life.message("jvm", "applet", "stop()", arrow="solid")
seq_life.message("applet", "jvm", "threads paused", arrow="dashed")

seq_life.divider("User Returns to Page")
seq_life.message("browser", "jvm", "page visible again", arrow="solid")
seq_life.message("jvm", "applet", "start()", arrow="solid")

seq_life.divider("Browser Tab Closed")
seq_life.message("browser", "jvm", "tab/window closed", arrow="solid")
seq_life.message("jvm", "applet", "stop()", arrow="solid")
seq_life.message("jvm", "applet", "destroy()", arrow="solid")
seq_life.deactivate("applet")
pn.story.extend(seq_life.as_flowable())

pn.tip(
    "Lifecycle order: init() -> start() -> [stop() -> start()] -> stop() -> destroy(). "
    "init() and destroy() are called EXACTLY ONCE each. "
    "start() and stop() can be called MULTIPLE TIMES. "
    "Always stop threads in stop() and set them to null to allow restart in start()."
)
pn.br()

# =============================================================================
#  3.5  SIMPLE APPLET DISPLAY METHODS
# =============================================================================
pn.chap_box("3.5  Simple Applet Display Methods")
pn.section("The Graphics Class")
pn.definition(
    "<b>Graphics (java.awt.Graphics):</b> The abstract base class for all "
    "graphics contexts. A Graphics object provides the drawing tools to render "
    "text, shapes, images, and colors onto a component's screen area. "
    "It is automatically passed as a parameter to the <code>paint(Graphics g)</code> "
    "method. Every drawing operation uses the current <b>color</b> (set via setColor()) "
    "and <b>font</b> (set via setFont()). The coordinate system has origin (0,0) at "
    "the <b>top-left corner</b>, with x increasing rightward and y increasing downward."
)

pn.section("Coordinate System")
pn.body(
    "Java's AWT coordinate system places the origin at the TOP-LEFT corner of the applet panel. "
    "X increases to the RIGHT. Y increases DOWNWARD. "
    "This is different from standard mathematical coordinates where Y increases upward."
)

pn.code_block(
    """
// Coordinate System Reference:
// =============================================
//  (0,0) -----> x increases rightward
//    |
//    |  (50,30) = 50 pixels right, 30 pixels down
//    |
//    v  y increases downward
//
// drawString("Text", 50, 80) = text starts at x=50, baseline at y=80
// drawRect(10, 10, 100, 50)  = rectangle top-left at (10,10), width=100, height=50
// drawOval(20, 20, 80, 80)   = oval in bounding box at (20,20), 80x80 pixels
""",
    lang="java",
)

pn.section("Complete Graphics Method Reference")
pn.info_table(
    ["Method", "Syntax / Signature", "Description"],
    [
        [
            "setColor()",
            "g.setColor(Color c)",
            "Sets the current drawing color. Applies to all subsequent draw/fill calls. e.g. g.setColor(Color.RED)",
        ],
        [
            "setFont()",
            "g.setFont(Font f)",
            "Sets font for drawString(). e.g. g.setFont(new Font('Arial', Font.BOLD, 16))",
        ],
        [
            "drawString()",
            "g.drawString(String str, int x, int y)",
            "Draws text string starting at position (x,y). y is the text baseline -- characters descend below y.",
        ],
        [
            "drawLine()",
            "g.drawLine(int x1, int y1, int x2, int y2)",
            "Draws a straight line from (x1,y1) to (x2,y2).",
        ],
        [
            "drawRect()",
            "g.drawRect(int x, int y, int w, int h)",
            "Draws outline of rectangle. (x,y) is top-left corner; w=width, h=height.",
        ],
        [
            "fillRect()",
            "g.fillRect(int x, int y, int w, int h)",
            "Draws SOLID filled rectangle. Same parameters as drawRect().",
        ],
        [
            "clearRect()",
            "g.clearRect(int x, int y, int w, int h)",
            "Fills rectangle with current background color (effectively erasing).",
        ],
        [
            "drawRoundRect()",
            "g.drawRoundRect(x, y, w, h, arcW, arcH)",
            "Rectangle with rounded corners. arcW, arcH control corner arc size.",
        ],
        [
            "drawOval()",
            "g.drawOval(int x, int y, int w, int h)",
            "Draws oval inscribed in bounding box at (x,y) with width w, height h. Use equal w,h for a circle.",
        ],
        [
            "fillOval()",
            "g.fillOval(int x, int y, int w, int h)",
            "Draws SOLID filled oval/circle.",
        ],
        [
            "drawArc()",
            "g.drawArc(x, y, w, h, startAngle, arcAngle)",
            "Draws arc (part of oval). Angles in degrees, counterclockwise from 3 o'clock.",
        ],
        [
            "drawPolygon()",
            "g.drawPolygon(int[] xPts, int[] yPts, int n)",
            "Draws closed polygon. xPts[] and yPts[] are arrays of vertex coordinates; n = point count.",
        ],
        [
            "fillPolygon()",
            "g.fillPolygon(int[] xPts, int[] yPts, int n)",
            "Draws SOLID filled polygon.",
        ],
        [
            "drawImage()",
            "g.drawImage(Image img, int x, int y, this)",
            "Draws an Image at (x,y). 4th arg is an ImageObserver (usually 'this').",
        ],
        ["getColor()", "g.getColor(): Color", "Returns the current drawing color."],
        [
            "getFont()",
            "g.getFont(): Font",
            "Returns the current font being used for drawString().",
        ],
    ],
)

pn.section("Graphics Demo -- Shapes and Colors")
pn.code_block(
    """
// GraphicsDemo.java -- Demonstrates all major drawing methods
import java.applet.Applet;
import java.awt.*;
/*
 * <applet code="GraphicsDemo.class" width="500" height="380"></applet>
 */
public class GraphicsDemo extends Applet {

    @Override
    public void init() {
        setBackground(Color.WHITE);
    }

    @Override
    public void paint(Graphics g) {

        // ---- 1. FONT AND TEXT ----
        g.setFont(new Font("Arial", Font.BOLD, 16));
        g.setColor(Color.DARK_GRAY);
        g.drawString("Java Graphics Demo -- IT408 Unit III", 80, 30);

        // ---- 2. LINES ----
        g.setColor(Color.BLACK);
        g.drawLine(20, 50, 480, 50);                   // horizontal rule

        // ---- 3. RECTANGLES ----
        g.setColor(Color.BLUE);
        g.drawRect(20, 60, 100, 60);                   // outline rectangle
        g.setFont(new Font("Arial", Font.PLAIN, 10));
        g.drawString("drawRect()", 30, 135);

        g.setColor(Color.CYAN);
        g.fillRect(140, 60, 100, 60);                  // solid filled rectangle
        g.setColor(Color.BLACK);
        g.drawString("fillRect()", 160, 135);

        g.setColor(Color.GREEN);
        g.drawRoundRect(260, 60, 100, 60, 20, 20);     // rounded corners
        g.drawString("drawRoundRect()", 265, 135);

        // ---- 4. OVALS AND CIRCLES ----
        g.setColor(Color.RED);
        g.drawOval(20, 150, 100, 60);                  // oval (ellipse)
        g.drawString("drawOval()", 35, 225);

        g.setColor(Color.MAGENTA);
        g.fillOval(140, 150, 80, 80);                  // solid circle
        g.setColor(Color.BLACK);
        g.drawString("fillOval()", 157, 245);

        // ---- 5. ARC ----
        g.setColor(Color.ORANGE);
        g.drawArc(260, 150, 100, 80, 0, 270);          // 270-degree arc
        g.setColor(Color.BLACK);
        g.drawString("drawArc(270 deg)", 258, 245);

        // ---- 6. POLYGON (triangle) ----
        int[] xPts = { 380, 420, 460 };
        int[] yPts = { 230, 150, 230 };
        g.setColor(Color.GREEN);
        g.fillPolygon(xPts, yPts, 3);                  // filled triangle
        g.setColor(Color.BLACK);
        g.drawString("fillPolygon()", 375, 250);

        // ---- 7. COLOR DEMONSTRATION ----
        Color[] palette = {
            Color.RED, Color.ORANGE, Color.YELLOW,
            Color.GREEN, Color.BLUE, Color.MAGENTA
        };
        for (int i = 0; i < palette.length; i++) {
            g.setColor(palette[i]);
            g.fillRect(20 + i * 75, 265, 60, 30);     // color swatches
        }
        g.setColor(Color.BLACK);
        g.drawString("Color swatches: RED, ORANGE, YELLOW, GREEN, BLUE, MAGENTA", 20, 320);

        // ---- 8. CUSTOM RGB COLOR ----
        // new Color(red, green, blue) -- each 0..255
        g.setColor(new Color(128, 0, 128));  // dark purple
        g.setFont(new Font("Arial", Font.BOLD, 14));
        g.drawString("Custom RGB Color: new Color(128, 0, 128)", 20, 355);
    }
}
""",
    lang="java",
)

pn.section("The Font Class")
pn.info_table(
    ["Font Style Constant", "Value", "Appearance"],
    [
        ["Font.PLAIN", "0", "Normal weight, normal style text"],
        ["Font.BOLD", "1", "Heavy/bold weight text"],
        ["Font.ITALIC", "2", "Italicized/slanted text"],
        ["Font.BOLD + Font.ITALIC", "3", "Bold and italic combined"],
    ],
)
pn.code_block(
    """
// Font creation syntax:
//   new Font(String name, int style, int size)
//
// Examples:
Font plainFont  = new Font("Arial",       Font.PLAIN,         12);
Font boldFont   = new Font("Helvetica",   Font.BOLD,          16);
Font italicFont = new Font("Times New Roman", Font.ITALIC,    14);
Font bothFont   = new Font("Courier New", Font.BOLD + Font.ITALIC, 18);

// Apply font before drawing text:
g.setFont(boldFont);
g.drawString("Bold text at size 16", 30, 50);
""",
    lang="java",
)
pn.br()

# =============================================================================
#  3.6  SIMPLE BANNER APPLET
# =============================================================================
pn.chap_box("3.6  Simple Banner Applet")
pn.section("What is a Banner Applet?")
pn.definition(
    "<b>Banner Applet:</b> An applet that continuously scrolls text horizontally "
    "across the screen -- like a news ticker or advertising marquee. "
    "It is the classic example of combining <b>threads</b> (for continuous animation) "
    "with <b>applet display methods</b> (for drawing). "
    "The key technique is using a background Thread that repeatedly moves the text "
    "position and calls <code>repaint()</code> at regular intervals using <code>Thread.sleep()</code>."
)

pn.section("How the Banner Works -- Key Concepts")
pn.bullet(
    [
        "<b>Thread:</b> A separate thread of execution that runs the scrolling loop in the background while the applet stays responsive. The applet implements Runnable and passes itself to a new Thread.",
        "<b>xPos variable:</b> Tracks the current horizontal position of the message. Starts at the right edge (getWidth()) and decreases each iteration to move text leftward.",
        "<b>repaint():</b> Called inside the thread loop to request the AWT system redraw the applet. The AWT event thread then calls update() -> paint().",
        "<b>Thread.sleep(ms):</b> Pauses the thread for the given milliseconds. Controls animation speed -- smaller value = faster scrolling.",
        "<b>update() override:</b> Overriding update(Graphics g) to manually fill the background (instead of AWT auto-clearing) prevents the visual flickering (white flash between frames) caused by the default AWT erase-then-draw behavior.",
    ]
)

# Banner Applet Flowchart
fc_banner = pd.Flowchart(
    width=pn.CW,
    height=540,
    theme=diag_theme,
    caption="Fig 3.5: Banner Applet execution flow -- init, start, thread loop, repaint",
)
fc_banner.terminal("begin", "Browser loads applet class", x=250, y=500)
fc_banner.process(
    "init", "init(): set background, set xPos = applet width", x=250, y=440
)
fc_banner.process(
    "start", "start(): create new Thread(this); thread.start()", x=250, y=380
)
fc_banner.decision("run", "Is thread active?", x=250, y=320)
fc_banner.process("move", "xPos -= scrollSpeed (shift text leftward)", x=250, y=260)
fc_banner.decision("wrap", "xPos < -(message width)?", x=250, y=200)
fc_banner.process("reset", "xPos = getWidth() (reset to right edge)", x=440, y=200)
fc_banner.process("repaint", "repaint() called -- AWT schedules paint", x=250, y=120)
fc_banner.process("paint", "paint(g): clear background, drawString", x=250, y=50)
fc_banner.process("sleep", "Thread.sleep(50ms) -- pause", x=60, y=50)
fc_banner.terminal("stop", "stop(): set thread = null -- loop exits", x=440, y=320)

fc_banner.edge("begin", "init")
fc_banner.edge("init", "start")
fc_banner.edge("start", "run")
fc_banner.edge("run", "move", branch="yes")
fc_banner.edge("run", "stop", branch="no")
fc_banner.edge("move", "wrap")
fc_banner.edge("wrap", "reset", branch="yes")
fc_banner.edge("wrap", "repaint", branch="no")
fc_banner.edge("reset", "repaint")
fc_banner.edge("repaint", "paint")
fc_banner.edge("paint", "sleep")
fc_banner.edge("sleep", "run", orthogonal=True)
pn.story.extend(fc_banner.as_flowable())

pn.section("Simple Banner Applet Code")
pn.code_block(
    """
// SimpleBannerApplet.java -- Classic scrolling text banner
import java.applet.Applet;
import java.awt.*;
/*
 * <applet code="SimpleBannerApplet.class" width="450" height="100"></applet>
 */
public class SimpleBannerApplet extends Applet implements Runnable {

    // The text to scroll across the screen
    String message = "  *** Welcome to Java Applet Banner -- IT408 UIT-RGPV! ***  ";

    // Thread reference -- nulling it in stop() signals run() to exit
    Thread scrollThread;

    // Current x-position of the message (pixels from left edge)
    int xPos;

    // ----------------------------------------------------------------
    // init() -- one-time setup
    // ----------------------------------------------------------------
    @Override
    public void init() {
        setBackground(Color.BLACK);
        // Message starts just beyond the RIGHT edge of the applet
        xPos = getWidth();
    }

    // ----------------------------------------------------------------
    // start() -- create and launch the scrolling thread
    // ----------------------------------------------------------------
    @Override
    public void start() {
        // Create a new thread that will call our run() method
        scrollThread = new Thread(this);
        scrollThread.start();  // start() launches the thread; calls run()
    }

    // ----------------------------------------------------------------
    // run() -- the scrolling loop (runs on the background thread)
    // ----------------------------------------------------------------
    @Override
    public void run() {
        // Keep scrolling while our thread reference is still valid
        // When stop() nulls 'scrollThread', Thread.currentThread() != scrollThread
        while (Thread.currentThread() == scrollThread) {
            xPos -= 3;   // move 3 pixels to the left each frame

            // When text has completely scrolled off the LEFT edge, reset to right
            // message.length() * 8 estimates pixel width of message text
            if (xPos < -(message.length() * 8)) {
                xPos = getWidth();  // reset: start from right edge again
            }

            repaint();  // request a screen refresh (calls update -> paint)

            try {
                Thread.sleep(50);  // wait 50ms between frames (approx 20 FPS)
            } catch (InterruptedException e) {
                return;  // thread was interrupted -- exit gracefully
            }
        }
    }

    // ----------------------------------------------------------------
    // stop() -- null the thread reference to stop the scrolling loop
    // ----------------------------------------------------------------
    @Override
    public void stop() {
        scrollThread = null;  // signals run() loop to exit at next iteration
    }

    // ----------------------------------------------------------------
    // paint() -- draw the scrolling message at current position
    // ----------------------------------------------------------------
    @Override
    public void paint(Graphics g) {
        // Set font for the banner text
        g.setFont(new Font("Arial", Font.BOLD, 20));
        // Set text color (bright yellow on black background)
        g.setColor(Color.YELLOW);
        // Draw message at current x position, vertically centered
        g.drawString(message, xPos, 55);
    }

    // ----------------------------------------------------------------
    // update() -- OVERRIDE to prevent flickering
    // Default AWT update() erases whole screen then calls paint()
    // This causes a visible white flash between frames
    // Our override manually clears only what's needed before paint()
    // ----------------------------------------------------------------
    @Override
    public void update(Graphics g) {
        // Fill with background color (avoids white-flash flicker)
        g.setColor(getBackground());  // get applet's background color
        g.fillRect(0, 0, getWidth(), getHeight());  // clear entire panel
        paint(g);  // then draw the new frame
    }
}
""",
    lang="java",
)
pn.br()

# =============================================================================
#  3.7  USING THE STATUS WINDOW
# =============================================================================
pn.chap_box("3.7  Using the Status Window")
pn.section("What is the Status Window?")
pn.definition(
    "<b>Status Window (Status Bar):</b> The narrow strip at the very bottom of a "
    "web browser or AppletViewer window that displays short informational messages. "
    "An applet can write to this area using the <code>showStatus(String message)</code> "
    "method inherited from the <code>Applet</code> class. "
    "It is commonly used for: displaying mouse coordinates, showing hover hints, "
    "reporting progress of a background operation, or showing keyboard shortcut reminders. "
    "The status message is temporary and may be overwritten by the browser itself."
)

pn.bullet(
    [
        "<b>Syntax:</b> <code>showStatus(String message)</code> -- no return value.",
        "<b>Where it appears:</b> Bottom of the browser window or AppletViewer tool bar.",
        "<b>Thread-safe:</b> Can be called from any thread (e.g., from inside run()).",
        "<b>Transient:</b> Browser may overwrite with its own status messages (e.g., hover URL).",
        "<b>No size limit enforced:</b> Very long strings may be truncated by the browser.",
    ]
)

pn.code_block(
    """
// StatusWindowDemo.java -- Show mouse position and lifecycle info in status bar
import java.applet.Applet;
import java.awt.*;
import java.awt.event.*;
/*
 * <applet code="StatusWindowDemo.class" width="400" height="250"></applet>
 */
public class StatusWindowDemo extends Applet
        implements MouseMotionListener, MouseListener {

    int mouseX = -1, mouseY = -1;
    String lastEvent = "None";
    int clickCount = 0;

    @Override
    public void init() {
        setBackground(Color.LIGHT_GRAY);
        // Register this applet as listener for both mouse position and click events
        addMouseMotionListener(this);
        addMouseListener(this);
        // Show initial hint in browser status bar
        showStatus("Move your mouse over the applet to see coordinates!");
    }

    @Override
    public void paint(Graphics g) {
        g.setFont(new Font("Arial", Font.BOLD, 14));
        g.setColor(Color.DARK_GRAY);
        g.drawString("Mouse X: " + mouseX + "   Mouse Y: " + mouseY, 30, 60);
        g.drawString("Last Event: " + lastEvent, 30, 90);
        g.drawString("Click Count: " + clickCount, 30, 120);
        g.setFont(new Font("Arial", Font.PLAIN, 12));
        g.setColor(Color.GRAY);
        g.drawString("(Check browser status bar at the bottom of the window)", 20, 165);
        g.drawString("showStatus() writes to that area.", 20, 185);
    }

    // MouseMotionListener -- fires continuously as mouse moves
    @Override
    public void mouseMoved(MouseEvent e) {
        mouseX = e.getX();
        mouseY = e.getY();
        lastEvent = "MOVED";
        // Display coordinates in the browser status bar
        showStatus("Mouse position: X=" + mouseX + ", Y=" + mouseY);
        repaint();
    }

    @Override
    public void mouseDragged(MouseEvent e) {
        mouseX = e.getX();
        mouseY = e.getY();
        lastEvent = "DRAGGED";
        showStatus("Dragging at: X=" + mouseX + ", Y=" + mouseY);
        repaint();
    }

    // MouseListener -- fires on click, press, release, enter, exit
    @Override
    public void mouseClicked(MouseEvent e) {
        clickCount++;
        lastEvent = "CLICKED at (" + e.getX() + ", " + e.getY() + ")";
        showStatus("Click #" + clickCount + " at X=" + e.getX() + " Y=" + e.getY());
        repaint();
    }

    @Override public void mousePressed(MouseEvent e)  { lastEvent = "PRESSED";  repaint(); }
    @Override public void mouseReleased(MouseEvent e) { lastEvent = "RELEASED"; repaint(); }
    @Override public void mouseEntered(MouseEvent e)  {
        showStatus("Mouse entered the applet area.");
    }
    @Override public void mouseExited(MouseEvent e)   {
        showStatus("Mouse left the applet area.");
    }
}
""",
    lang="java",
)
pn.br()

# =============================================================================
#  3.8  THE HTML APPLET TAG
# =============================================================================
pn.chap_box("3.8  The HTML APPLET Tag")
pn.section("APPLET Tag Syntax and Attributes")
pn.definition(
    "<b>The &lt;applet&gt; Tag:</b> An HTML element that embeds a Java applet "
    "inside a web page. The browser reads this tag to determine which .class file "
    "to download, what size panel to allocate, where to find the files, and what "
    "parameters to pass to the applet. The <code>code</code>, <code>width</code>, "
    "and <code>height</code> attributes are REQUIRED; all others are optional."
)

pn.info_table(
    ["Attribute", "Required?", "Description", "Example"],
    [
        [
            "code",
            "YES",
            "Name of the compiled .class file containing the Applet subclass. Include .class extension.",
            'code="MyApplet.class"',
        ],
        ["width", "YES", "Width of the applet display panel in pixels.", 'width="400"'],
        [
            "height",
            "YES",
            "Height of the applet display panel in pixels.",
            'height="300"',
        ],
        [
            "codebase",
            "No",
            "URL or directory path where the .class file is located. If omitted, defaults to same directory as the HTML file.",
            'codebase="applets/"',
        ],
        [
            "archive",
            "No",
            "Comma-separated list of JAR files to download. The browser downloads and caches these before loading the applet.",
            'archive="app.jar, libs.jar"',
        ],
        [
            "name",
            "No",
            "A name identifier for this applet. Used by JavaScript or other applets on the same page to reference this applet.",
            'name="clockApplet"',
        ],
        [
            "alt",
            "No",
            "Alternate text shown when the browser cannot run Java (no plugin installed). Good accessibility practice.",
            'alt="Java required to view this."',
        ],
        [
            "align",
            "No",
            "Alignment of the applet panel within the surrounding HTML text flow.",
            'align="middle"',
        ],
        [
            "hspace",
            "No",
            "Horizontal spacing (pixels) between the applet panel and surrounding HTML content.",
            'hspace="10"',
        ],
        [
            "vspace",
            "No",
            "Vertical spacing (pixels) between the applet panel and surrounding HTML content.",
            'vspace="10"',
        ],
        [
            "<param>",
            "No (child)",
            "Child tag for passing named string parameters into the applet. Read using getParameter(name) inside the applet.",
            '<param name="speed" value="5">',
        ],
    ],
)

pn.section("Complete HTML Example with All Attributes")
pn.code_block(
    """
<!-- BannerPage.html -- Full HTML page embedding an applet with all attributes -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Java Applet Demo -- IT408</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f0f0f0; }
        h1   { color: navy; }
    </style>
</head>
<body>
    <h1>Java Banner Applet Demo</h1>
    <p>The animated banner applet is displayed below:</p>

    <!--
        APPLET TAG: Embeds the Java applet into the page
        Required attributes: code, width, height
        Optional: codebase, archive, name, alt, align
    -->
    <applet
        code="ColoredBannerApplet.class"
        codebase="classes/"
        width="500"
        height="100"
        name="bannerApplet"
        alt="Java applet not supported. Please install Java Runtime."
        align="center"
        hspace="10"
        vspace="5">

        <!--
            PARAM TAGS: Pass named string values to the applet
            These are read inside the applet using getParameter("paramName")
            ALL param values are strings -- applet must convert if needed
        -->
        <param name="message" value="Welcome to UIT-RGPV IT408 Java Programming!">
        <param name="speed"   value="5">
        <param name="color"   value="yellow">
        <param name="font"    value="Arial">
        <param name="size"    value="20">
        <!-- Text shown if browser cannot display Java applets -->
        Your browser does not support Java applets.
        Please install the Java Runtime Environment to view this content.
        Alternatively, run: <code>appletviewer BannerPage.html</code>
    </applet>

    <p><em>To run locally: compile the .java file, then run appletviewer BannerPage.html</em></p>
</body>
</html>

<!--
    COMMAND LINE USAGE:
    javac ColoredBannerApplet.java    (compile to .class)
    appletviewer BannerPage.html      (run in applet viewer)
-->
""",
    lang="java",
)

pn.section("Alternative: Embedding Applet Tag in Java Source File")
pn.code_block(
    """
// You can also embed the HTML applet tag as a comment in the Java source file
// Then appletviewer can be run directly on the .java file

import java.applet.Applet;
import java.awt.*;

/*
 * APPLET TAG COMMENT -- appletviewer reads this when you run:
 *   appletviewer QuickApplet.java
 * <applet code="QuickApplet.class" width="350" height="150">
 *   <param name="message" value="Hello from embedded tag!">
 * </applet>
 */
public class QuickApplet extends Applet {
    String msg;
    public void init() {
        msg = getParameter("message");
        if (msg == null) msg = "No message parameter found.";
    }
    public void paint(Graphics g) {
        g.drawString(msg, 30, 75);
    }
}

// Run with:
//   javac QuickApplet.java
//   appletviewer QuickApplet.java    (reads the /* <applet> */ comment)
""",
    lang="java",
)
pn.br()

# =============================================================================
#  3.9  PASSING PARAMETERS TO APPLETS
# =============================================================================
pn.chap_box("3.9  Passing Parameters to Applets")
pn.section("The getParameter() Method")
pn.definition(
    "<b>Passing Parameters:</b> HTML <code>&lt;param&gt;</code> tags inside the "
    "<code>&lt;applet&gt;</code> block allow the HTML author to pass "
    "configuration data to the applet without recompiling the Java code. "
    "Inside the applet, the <code>getParameter(String name)</code> method "
    "(inherited from <code>Applet</code>) reads these values. "
    "<b>Important:</b> getParameter() ALWAYS returns a String (or null if not found). "
    "The applet must parse numeric values using <code>Integer.parseInt()</code>, "
    "<code>Double.parseDouble()</code>, etc."
)

pn.info_table(
    ["Step", "HTML Side (in .html file)", "Java Side (in applet init())"],
    [
        ["1. Declare param", '<param name="fontSize" value="18">', "--"],
        ["2. Read param", "--", 'String s = getParameter("fontSize");'],
        ["3. Check null", "--", 'if (s == null) s = "14"; // default fallback'],
        ["4. Parse type", "--", "int size = Integer.parseInt(s); // String -> int"],
        ["5. Use value", "--", 'g.setFont(new Font("Arial", Font.PLAIN, size));'],
    ],
)

pn.code_block(
    """
// ParameterDemo.java -- Complete parameter reading demonstration
import java.applet.Applet;
import java.awt.*;
/*
 * <applet code="ParameterDemo.class" width="420" height="220">
 *   <param name="name"       value="Rahul Sharma">
 *   <param name="branch"     value="Information Technology">
 *   <param name="year"       value="4">
 *   <param name="marks"      value="87.5">
 *   <param name="bgColor"    value="lightblue">
 *   <param name="textSize"   value="16">
 * </applet>
 */
public class ParameterDemo extends Applet {

    // Declare fields to hold parameter values (read in init, used in paint)
    String name, branch;
    int year, textSize;
    double marks;
    Color bgColor;

    @Override
    public void init() {
        // ---- String parameters (getParameter returns String or null) ----
        name = getParameter("name");
        if (name == null) name = "Unknown Student";  // always provide default!

        branch = getParameter("branch");
        if (branch == null) branch = "Unknown Branch";

        // ---- Integer parameter: parse String -> int ----
        String yearStr = getParameter("year");
        if (yearStr != null) {
            try {
                year = Integer.parseInt(yearStr);       // "4" -> 4
            } catch (NumberFormatException e) {
                year = 1;  // fallback if HTML has non-numeric value
            }
        } else {
            year = 1;
        }

        // ---- Double/float parameter: parse String -> double ----
        String marksStr = getParameter("marks");
        if (marksStr != null) {
            try {
                marks = Double.parseDouble(marksStr);   // "87.5" -> 87.5
            } catch (NumberFormatException e) {
                marks = 0.0;
            }
        } else {
            marks = 0.0;
        }

        // ---- Color parameter: map String name to Color object ----
        String colorStr = getParameter("bgColor");
        if (colorStr == null)              bgColor = Color.WHITE;
        else if (colorStr.equals("lightblue"))  bgColor = new Color(173, 216, 230);
        else if (colorStr.equals("yellow"))     bgColor = Color.YELLOW;
        else if (colorStr.equals("pink"))       bgColor = Color.PINK;
        else                               bgColor = Color.WHITE;
        setBackground(bgColor);

        // ---- Font size parameter ----
        String sizeStr = getParameter("textSize");
        textSize = (sizeStr != null) ? Integer.parseInt(sizeStr) : 14;
    }

    @Override
    public void paint(Graphics g) {
        g.setFont(new Font("Arial", Font.BOLD, textSize));
        g.setColor(Color.DARK_GRAY);
        g.drawString("Student Information (from HTML Parameters):", 20, 40);

        g.setFont(new Font("Arial", Font.PLAIN, textSize));
        g.setColor(Color.BLUE);
        g.drawString("Name   : " + name,          30, 75);
        g.drawString("Branch : " + branch,        30, 105);
        g.drawString("Year   : " + year + " Year", 30, 135);
        g.drawString("Marks  : " + marks + "%",   30, 165);
    }
}
""",
    lang="java",
)

# Parameter Reading Flow
fc_param = pd.Flowchart(
    width=pn.CW,
    height=500,
    theme=diag_theme,
    caption="Fig 3.6: Parameter reading flow -- HTML to applet via getParameter()",
)
fc_param.terminal("html", "HTML: <param name='speed' value='5'>", x=250, y=460)
fc_param.process("init", "Applet init(): call getParameter('speed')", x=250, y=400)
fc_param.decision("null", "Is returned value null?", x=250, y=340)
fc_param.process("default", "Use default value (e.g. speed = 3)", x=60, y=340)
fc_param.process(
    "parse", "Parse String to needed type (Integer.parseInt)", x=250, y=260
)
fc_param.decision("valid", "Is parsed value valid (no Exception)?", x=250, y=180)
fc_param.process("error", "Use safe default on parse error", x=440, y=180)
fc_param.process("use", "Assign to field; use in paint() or start()", x=250, y=90)
fc_param.terminal("done", "Applet configured from HTML params", x=250, y=30)

fc_param.edge("html", "init")
fc_param.edge("init", "null")
fc_param.edge("null", "default", branch="yes")
fc_param.edge("null", "parse", branch="no")
fc_param.edge("parse", "valid")
fc_param.edge("valid", "use", branch="yes")
fc_param.edge("valid", "error", branch="no")
fc_param.edge("default", "use", orthogonal=True)
fc_param.edge("error", "use", orthogonal=True)
fc_param.edge("use", "done")
pn.story.extend(fc_param.as_flowable())
pn.br()

# =============================================================================
#  3.10  IMPROVING THE BANNER APPLET
# =============================================================================
pn.chap_box("3.10  Improving the Banner Applet")
pn.section("Enhancements Over the Simple Banner")
pn.bullet(
    [
        "<b>Configurable via HTML params:</b> Speed, text color, font size, and message text are all controlled by HTML &lt;param&gt; tags -- no recompilation needed.",
        "<b>Pause/Resume on mouse click:</b> MouseListener toggles a boolean flag. The thread loop checks the flag -- if paused, it skips the scroll and repaint, saving CPU.",
        "<b>Multiple rotating advertisements:</b> An array of messages rotates automatically when each message completes a full scroll, making it useful for ad banners.",
        "<b>Flicker prevention:</b> Override update(Graphics g) to fill background with the applet's background color before calling paint(g), eliminating the white-flash flicker seen in the simple version.",
        "<b>Color cycle:</b> Each advertisement uses a different text color from a colors array, matching the message index.",
    ]
)

pn.section("Improved Banner Applet -- Full Code")
pn.code_block(
    """
// ImprovedBannerApplet.java -- Full-featured banner with all improvements
import java.applet.Applet;
import java.awt.*;
import java.awt.event.*;
/*
 * <applet code="ImprovedBannerApplet.class" width="500" height="100">
 *   <param name="speed"   value="4">
 *   <param name="color"   value="yellow">
 *   <param name="size"    value="22">
 * </applet>
 */
public class ImprovedBannerApplet extends Applet
        implements Runnable, MouseListener {

    // ---- Configuration (read from HTML params in init()) ----
    int   scrollSpeed;   // pixels to move per frame
    Color textColor;     // color of scrolling text
    int   fontSize;      // font size for message

    // ---- Multiple rotating ad messages ----
    String[] messages = {
        "  *** Welcome to Java Applet Programming -- IT408! ***  ",
        "  *** UIT-RGPV Bhopal -- Semester IV -- Unit III ***  ",
        "  *** Applets: init -> start -> stop -> destroy ***  ",
    };

    // ---- Per-message colors (cycles with messages array) ----
    Color[] colors = { Color.YELLOW, Color.CYAN, Color.GREEN };

    int currentMsg = 0;  // index of currently scrolling message
    int xPos;            // current horizontal text position

    Thread scrollThread; // background animation thread
    boolean paused = false; // pause/resume toggle (mouse click)

    @Override
    public void init() {
        setBackground(Color.BLACK);
        xPos = getWidth();

        // ---- Read HTML parameters with defaults ----
        String speedStr = getParameter("speed");
        scrollSpeed = (speedStr != null) ? Integer.parseInt(speedStr) : 3;

        String colorStr = getParameter("color");
        if (colorStr == null)             textColor = Color.YELLOW;
        else if (colorStr.equals("yellow")) textColor = Color.YELLOW;
        else if (colorStr.equals("cyan"))   textColor = Color.CYAN;
        else if (colorStr.equals("green"))  textColor = Color.GREEN;
        else if (colorStr.equals("red"))    textColor = Color.RED;
        else                              textColor = Color.WHITE;

        String sizeStr = getParameter("size");
        fontSize = (sizeStr != null) ? Integer.parseInt(sizeStr) : 20;

        // Register mouse listener for pause/resume feature
        addMouseListener(this);
        showStatus("Click banner to pause/resume scrolling.");
    }

    @Override
    public void start() {
        scrollThread = new Thread(this);
        scrollThread.start();
    }

    // ---- run() -- scrolling animation loop (background thread) ----
    @Override
    public void run() {
        while (Thread.currentThread() == scrollThread) {
            if (!paused) {
                // Advance text position leftward by scrollSpeed pixels
                xPos -= scrollSpeed;

                // When message exits left edge, advance to next message
                if (xPos < -(messages[currentMsg].length() * (fontSize / 2 + 2))) {
                    xPos = getWidth();  // reset to right edge
                    currentMsg = (currentMsg + 1) % messages.length; // rotate
                }

                repaint();  // request screen refresh
            }

            try {
                Thread.sleep(40);   // ~25 FPS animation rate
            } catch (InterruptedException e) {
                return;
            }
        }
    }

    @Override
    public void stop() {
        scrollThread = null;  // stops the run() loop gracefully
    }

    @Override
    public void paint(Graphics g) {
        // Choose color for current message
        g.setColor(colors[currentMsg % colors.length]);
        g.setFont(new Font("Arial", Font.BOLD, fontSize));

        // Draw scrolling message at current xPos
        g.drawString(messages[currentMsg], xPos, 55);

        // Show PAUSED indicator when animation is frozen
        if (paused) {
            g.setFont(new Font("Arial", Font.PLAIN, 11));
            g.setColor(Color.RED);
            g.drawString("[ PAUSED -- click to resume ]", 150, 85);
        }
    }

    // ---- Override update() to eliminate flicker ----
    @Override
    public void update(Graphics g) {
        // Fill background manually before painting new frame
        g.setColor(getBackground()); // use applet's own background color
        g.fillRect(0, 0, getWidth(), getHeight());
        paint(g);  // draw new frame on cleared background
    }

    // ---- MouseListener: toggle pause/resume on click ----
    @Override
    public void mouseClicked(MouseEvent e) {
        paused = !paused;
        showStatus(paused ? "Banner PAUSED. Click to resume." : "Banner RESUMED.");
        repaint();  // refresh to show/hide PAUSED label
    }

    // Unused MouseListener methods (must implement all interface methods)
    @Override public void mousePressed(MouseEvent e)  {}
    @Override public void mouseReleased(MouseEvent e) {}
    @Override public void mouseEntered(MouseEvent e)  {}
    @Override public void mouseExited(MouseEvent e)   {}
}
""",
    lang="java",
)

pn.section("Comparison: Simple vs Improved Banner")
pn.info_table(
    ["Feature", "Simple Banner", "Improved Banner"],
    [
        [
            "Text source",
            "Hardcoded String in source code",
            "HTML <param name='...'>  or multiple messages array",
        ],
        ["Scroll speed", "Fixed (3 pixels/frame)", "Configurable via HTML speed param"],
        [
            "Text color",
            "Fixed (Color.YELLOW)",
            "Configurable via HTML color param; cycles with messages",
        ],
        [
            "Pause/Resume",
            "No pause feature",
            "Click anywhere on applet to pause; click again to resume",
        ],
        [
            "Multiple messages",
            "Single message loops",
            "Array of messages rotates automatically",
        ],
        [
            "Flicker",
            "May flicker (default update() clears screen)",
            "Flicker-free: override update() to clear manually before paint",
        ],
        ["Status bar", "Not used", "showStatus() shows pause/resume hints"],
    ],
)
pn.br()

# =============================================================================
#  3.11  EXAM QUESTIONS WITH ANSWERS
# =============================================================================
pn.part_box("UNIT III -- EXAM QUESTIONS & DETAILED ANSWERS")
pn.chap_box("3.11  Previous-Year Style Exam Questions")

pn.section("2-Mark Questions (Short Answer)")

pn.highlight(
    "<b>Q1. Define Java Applet. How is it different from a Java Application?</b><br/>"
    "A: A Java Applet is a small Java program embedded in a web page and executed by a "
    "Java-enabled browser. Unlike a standalone application, an applet has no main() method; "
    "its lifecycle is controlled by the browser through init(), start(), stop(), and destroy(). "
    "An application runs independently via the java command; an applet requires an HTML page "
    "and browser/appletviewer. Applications have full system access; applets run in a security sandbox."
)

pn.highlight(
    "<b>Q2. What package contains the Applet class? Write its full class hierarchy.</b><br/>"
    "A: The Applet class is in the <code>java.applet</code> package. "
    "Hierarchy: java.lang.Object -> java.awt.Component -> java.awt.Container -> "
    "java.awt.Panel -> java.applet.Applet. "
    "This hierarchy means every applet is also an AWT Panel, giving it a graphical display area."
)

pn.highlight(
    "<b>Q3. What is the role of the paint() method in an applet?</b><br/>"
    "A: paint(Graphics g) is responsible for drawing the applet's visual output on screen. "
    "It is called by the AWT system whenever the applet needs to be rendered: on first display, "
    "after resize, after being uncovered by another window, or after repaint() is called. "
    "Never call paint() directly -- use repaint() to schedule a redraw. "
    "The Graphics object 'g' provides all drawing tools (drawString, drawRect, setColor, etc.)."
)

pn.highlight(
    "<b>Q4. Differentiate between init() and start() in an applet.</b><br/>"
    "A: init() is called EXACTLY ONCE when the applet class is first loaded -- it performs "
    "one-time initialization (set background, initialize variables, add listeners). "
    "start() is called after init() AND every time the user returns to the page -- it "
    "begins or resumes execution (start threads, resume animation). "
    "Key difference: init() = once only; start() = multiple times per applet lifetime."
)

pn.highlight(
    "<b>Q5. What is the purpose of showStatus() in an applet?</b><br/>"
    "A: showStatus(String message) displays a short text message in the status bar "
    "(the strip at the very bottom of the browser or AppletViewer window). "
    "It is used for showing mouse coordinates, hover hints, progress messages, or "
    "any informational text that should appear below the applet without occupying applet space. "
    "The message may be overwritten by browser's own status messages."
)

pn.highlight(
    "<b>Q6. What is the HTML tag for embedding a Java applet? Name three of its attributes.</b><br/>"
    "A: The HTML tag is &lt;applet&gt;. Three key attributes: "
    "(1) <b>code</b> -- name of the compiled .class file (required). "
    "(2) <b>width</b> -- width of applet panel in pixels (required). "
    "(3) <b>height</b> -- height of applet panel in pixels (required). "
    "Other attributes: codebase (directory of .class file), archive (JAR file), "
    "name (identifier for applet), alt (text if Java not supported)."
)

pn.highlight(
    "<b>Q7. How are parameters passed to an applet from HTML?</b><br/>"
    "A: Parameters are passed using &lt;param&gt; child tags inside the &lt;applet&gt; tag: "
    "<code>&lt;param name='speed' value='5'&gt;</code>. "
    "Inside the applet, getParameter('speed') reads the value as a String. "
    "If the param is not defined in HTML, getParameter() returns null -- always check for null "
    "and provide a default. Parse to int/double using Integer.parseInt() or Double.parseDouble()."
)

pn.highlight(
    "<b>Q8. Why is update() overridden in a banner applet?</b><br/>"
    "A: The default AWT update() method erases the entire applet panel with the background color "
    "before calling paint(). In animations this causes a visible white-flash flicker between frames. "
    "By overriding update(Graphics g) to manually fill the background and then call paint(), "
    "we control exactly what gets erased, eliminating the flicker and producing smooth animation."
)

pn.highlight(
    "<b>Q9. What is the difference between repaint() and paint()?</b><br/>"
    "A: paint(Graphics g) is the actual drawing method -- you override it and draw in it; "
    "never call it directly. repaint() is a request method -- you call it when your data changes "
    "to tell AWT 'please schedule a redraw'. AWT then calls update() -> paint() on its own event thread. "
    "Direct calls to paint() are dangerous because they may not have a valid Graphics context."
)

pn.highlight(
    "<b>Q10. What is AppletViewer and when is it used?</b><br/>"
    "A: AppletViewer is a command-line tool included in the JDK that simulates the browser "
    "environment for testing applets locally without needing a browser with Java plugin. "
    "Usage: <code>appletviewer MyApplet.html</code> or <code>appletviewer MyApplet.java</code> "
    "(if the .java file contains an &lt;applet&gt; comment). "
    "It was the standard way to test and debug applets before browser plugins became obsolete."
)

pn.section("5-Mark Questions (Explain with Code/Diagram)")

pn.highlight(
    "<b>Q11. Explain the complete lifecycle of a Java Applet with a diagram.</b><br/>"
    "A: The Java Applet lifecycle consists of four methods called by the browser in sequence:<br/>"
    "<b>1. init():</b> Called once when applet loads. One-time setup (variables, UI, listeners).<br/>"
    "<b>2. start():</b> Called after init(); also each time user returns to the page. Starts threads.<br/>"
    "<b>3. stop():</b> Called when user leaves page. Pauses threads to save CPU. May be called multiple times.<br/>"
    "<b>4. destroy():</b> Called once when applet is removed from memory. Final cleanup.<br/>"
    "Order: Page Load -> init() -> start() -> [stop() -> start() repeated] -> stop() -> destroy(). "
    "See Fig 3.3 and Fig 3.4 for the state machine and sequence diagrams."
)

pn.highlight(
    "<b>Q12. Write a Java Applet to draw a rectangle, oval, and display text with different colors.</b><br/>"
    "A: See GraphicsDemo code in Section 3.5. Key points: "
    "(1) import java.applet.Applet; import java.awt.*; "
    "(2) extend Applet; "
    "(3) override paint(Graphics g); "
    "(4) use g.setColor(Color.X) before each draw call; "
    "(5) g.drawRect(x,y,w,h) for rectangle, g.drawOval(x,y,w,h) for oval, g.drawString(text,x,y) for text. "
    "HTML: &lt;applet code='GraphicsDemo.class' width='400' height='300'&gt;&lt;/applet&gt;"
)

pn.highlight(
    "<b>Q13. Explain the Simple Banner Applet with Runnable thread. Write its code.</b><br/>"
    "A: A banner applet scrolls text using a background Thread. "
    "The class implements both Applet and Runnable. "
    "In init(): set background, set xPos=getWidth(). "
    "In start(): create scrollThread = new Thread(this); scrollThread.start(). "
    "In run(): loop while thread is valid; decrement xPos by speed; reset when off-screen; call repaint(); sleep(50ms). "
    "In stop(): scrollThread = null (exits loop). "
    "Override update(g) to prevent flicker. "
    "See the complete SimpleBannerApplet code in Section 3.6."
)

pn.highlight(
    "<b>Q14. Explain the HTML APPLET tag with all its attributes and a complete example.</b><br/>"
    "A: The &lt;applet&gt; tag embeds Java applets. Required: code (class file name), width, height. "
    "Optional: codebase (class directory), archive (JAR files), name (applet identifier), "
    "alt (fallback text), align, hspace, vspace. "
    "Child &lt;param&gt; tags pass named string parameters: &lt;param name='x' value='y'&gt;. "
    "Example: &lt;applet code='Banner.class' width='400' height='100'&gt; "
    "&lt;param name='speed' value='5'&gt; &lt;/applet&gt;. "
    "See Section 3.8 for the complete HTML file example."
)

pn.highlight(
    "<b>Q15. How do you pass and read parameters in an applet? Write a program to display student info from HTML parameters.</b><br/>"
    "A: HTML side: use &lt;param name='name' value='Rahul'&gt; inside &lt;applet&gt; block. "
    "Java side (in init()): String name = getParameter('name'); if(name==null) name='Unknown'; "
    "For int: int x = Integer.parseInt(getParameter('x')); "
    "For double: double d = Double.parseDouble(getParameter('d')); "
    "Always check for null before parsing. Use the values in paint(). "
    "See complete ParameterDemo code in Section 3.9."
)

pn.section("10-Mark Questions (Detailed Programs)")

pn.highlight(
    "<b>Q16. Write a complete Java Applet program for a scrolling banner. "
    "Include HTML file. Add pause/resume on mouse click and configurable speed/color via parameters.</b><br/>"
    "A: See the ImprovedBannerApplet code in Section 3.10 -- it covers ALL these requirements: "
    "(1) Scrolling text with Thread and sleep(). "
    "(2) Multiple rotating messages with color cycling. "
    "(3) Mouse click toggles paused boolean; thread skips repaint when paused. "
    "(4) HTML params: speed, color, size read in init() with defaults. "
    "(5) update() override prevents flicker. "
    "(6) showStatus() for pause/resume hints. "
    "HTML: code='ImprovedBannerApplet.class' with &lt;param name='speed' value='4'&gt; etc."
)

pn.highlight(
    "<b>Q17. Write an applet that draws various geometric shapes (rectangle, circle, line, polygon) "
    "with filled and unfilled versions, using multiple colors.</b><br/>"
    "A: See GraphicsDemo in Section 3.5 for the complete implementation. "
    "Key AWT Graphics methods: drawRect vs fillRect, drawOval vs fillOval, "
    "drawLine, drawPolygon vs fillPolygon, drawArc, drawRoundRect. "
    "Color usage: g.setColor(Color.X) before each operation. "
    "Custom RGB: new Color(r, g, b) where r, g, b are 0-255 integers. "
    "Font: new Font('Arial', Font.BOLD, 16) set via g.setFont()."
)

pn.highlight(
    "<b>Q18. Explain Applet Architecture. Describe how a browser, JVM, and the applet class interact "
    "from page load to execution.</b><br/>"
    "A: (1) User opens HTML page in browser. "
    "(2) Browser parses HTML and finds &lt;applet code='X.class'&gt; tag. "
    "(3) Browser sends HTTP GET request to web server; server returns X.class bytecode. "
    "(4) Browser activates Java Plugin (embedded JVM). "
    "(5) JVM class loader loads and verifies X.class bytecode. "
    "(6) JVM instantiates the Applet subclass (calls no-arg constructor). "
    "(7) JVM calls init() -- one-time setup. "
    "(8) JVM calls start() -- begin execution. "
    "(9) AWT calls paint(Graphics g) to render first frame. "
    "(10) Applet now runs; responds to lifecycle and user events. "
    "See Fig 3.2 for the complete architecture diagram."
)

pn.highlight(
    "<b>Q19. Write an applet that displays mouse click coordinates and draws a marker at each click position. "
    "Also use the Status Window to show current mouse position.</b><br/>"
    "A: (1) Implement MouseListener and MouseMotionListener. "
    "(2) In init(): addMouseListener(this); addMouseMotionListener(this); showStatus('Click anywhere!'). "
    "(3) In mouseClicked(MouseEvent e): record e.getX(), e.getY(); add to list; repaint(); showStatus(coords). "
    "(4) In mouseMoved(MouseEvent e): showStatus('Mouse at X=' + e.getX() + ' Y=' + e.getY()). "
    "(5) In paint(Graphics g): for each recorded point, draw fillOval(x-5, y-5, 10, 10) in red. "
    "See StatusWindowDemo in Section 3.7 and MouseCoordApplet in the reference examples."
)

pn.highlight(
    "<b>Q20. Compare Java Applet, Java Application, and Java Servlet. "
    "Why are Applets deprecated? What are the modern alternatives?</b><br/>"
    "A: <b>Applet:</b> Client-side, runs in browser, sandboxed, extends Applet, no main(). "
    "<b>Application:</b> Standalone, runs via java command, full system access, has main(). "
    "<b>Servlet:</b> Server-side, runs in Tomcat/Jetty, extends HttpServlet, handles HTTP requests. "
    "<b>Deprecation reasons:</b> Browser plugins (NPAPI) removed by all major browsers 2015-2017; "
    "security vulnerabilities; slow load (full JVM download); no mobile support; HTML5+JS does same things better. "
    "<b>Modern alternatives:</b> HTML5 Canvas + JavaScript for browser animations; "
    "JavaFX for desktop GUI; Spring Boot / Servlets for web backend; React/Angular for web UI."
)

pn.section("Assignment Question Bank Coverage")
assignment_questions = [
    (
        "Q1. What is a Java Applet? How is it different from a standalone Java application?",
        "An applet is embedded in HTML and controlled by init(), start(), stop(), and destroy(); an application runs directly from main(). Applets are sandboxed and browser/appletviewer hosted, while applications have normal JVM process access.",
    ),
    (
        "Q2. Explain the Applet class. Which package contains it?",
        "The class is <code>java.applet.Applet</code>. It extends Panel through the AWT hierarchy and provides lifecycle, parameter, status, image, and audio helper methods.",
    ),
    (
        "Q3. Describe the applet lifecycle methods: init(), start(), stop(), destroy().",
        "init() runs once for setup; start() runs after init and on revisits; stop() pauses execution when the page is left; destroy() runs once for final cleanup.",
    ),
    (
        "Q4. Explain Applet Architecture with a diagram.",
        "Browser reads the HTML applet tag, downloads class files from the web server, starts the JVM plugin, creates the applet object, and AWT calls paint() for rendering. See Fig 3.2.",
    ),
    (
        "Q5. What is the role of the paint() method in an applet?",
        "paint(Graphics g) renders applet output. It is called by AWT on first display, resize, uncover, or repaint(); use the Graphics object for drawString(), drawRect(), drawOval(), colors, and fonts.",
    ),
    (
        "Q6. Differentiate between init() and start(), and stop() and destroy().",
        "init() is one-time setup, start() can run many times; stop() temporarily pauses resources, destroy() permanently releases them before removal.",
    ),
    (
        "Q7. What are simple applet display methods? Explain drawString(), drawRect(), drawOval().",
        "drawString(text, x, y) writes text at a baseline, drawRect(x, y, w, h) outlines a rectangle, and drawOval(x, y, w, h) outlines an oval or circle inside a bounding box.",
    ),
    (
        "Q8. What is the Status Window in an applet?",
        "The status window is the browser or AppletViewer status bar. Use showStatus(message) to display brief messages such as mouse position, progress, or hints.",
    ),
    (
        "Q9. Explain the HTML &lt;applet&gt; tag and its attributes.",
        "The applet tag embeds a class file in HTML. Required attributes are code, width, and height; common optional attributes include codebase, archive, name, alt, align, hspace, and vspace.",
    ),
    (
        "Q10. How are parameters passed to an applet using HTML?",
        "Use child &lt;param name='key' value='value'&gt; tags inside &lt;applet&gt;. Java reads them with getParameter('key') and must check for null before parsing.",
    ),
    (
        'Q11. Write a simple applet to display "Welcome to Java Applet Programming".',
        "Extend Applet, override paint(Graphics g), set a font/color if needed, and call g.drawString('Welcome to Java Applet Programming', x, y).",
    ),
    (
        "Q12. Create an applet that draws a rectangle, circle, and line.",
        "In paint(), call g.drawRect(...), g.drawOval(...), and g.drawLine(...), optionally setting different colors before each shape. See GraphicsDemo in Section 3.5.",
    ),
    (
        "Q13. Write an applet to display multiple messages using paint().",
        "Override paint() and call drawString() multiple times at different y coordinates, changing color or font between lines for readability.",
    ),
    (
        "Q14. Create an applet to display Name, Class, Roll Number.",
        "Store the values as strings and draw them in paint() with aligned labels such as Name, Class, and Roll No. The same pattern is used in parameter-display examples.",
    ),
    (
        "Q15. Write an applet that changes background color.",
        "Call setBackground(Color.X) in init(), then draw foreground text in paint() with a contrasting color.",
    ),
    (
        "Q16. Create a Simple Banner Applet with scrolling text.",
        "Implement Runnable, create/start a thread in start(), update x position in run(), call repaint(), and draw the message in paint(). See Section 3.6.",
    ),
    (
        "Q17. Modify the banner applet to change text color and adjust scrolling speed.",
        "Read color and speed from HTML parameters in init(), parse speed with a default value, map color strings to Color constants, and use them in the banner loop.",
    ),
    (
        "Q18. Create an applet that uses Status Window to display messages.",
        "Add mouse or motion listeners and call showStatus() inside event methods, for example showStatus('Mouse at X=' + e.getX()).",
    ),
    (
        "Q19. Write an HTML file to execute an applet using &lt;applet&gt; tag.",
        "Place &lt;applet code='WelcomeApplet.class' width='400' height='150'&gt; fallback text &lt;/applet&gt; in an HTML body, then run it with appletviewer.",
    ),
    (
        "Q20. Create an applet that reads parameters from HTML and displays them.",
        "Use &lt;param&gt; tags for values such as name, branch, and year; read them with getParameter(), apply defaults for null, and draw them in paint().",
    ),
    (
        "Q21. Improve the banner applet: add pause/resume feature using mouse click events.",
        "Implement MouseListener, keep a boolean paused flag, toggle it in mouseClicked(), and skip x-position updates in run() while paused. The improved banner in Section 3.10 covers this.",
    ),
    (
        "Q22. Create an applet to display current system time with live update.",
        "Use a background thread that formats new Date() every second, stores the formatted time string, calls repaint(), and draws the time in paint().",
    ),
    (
        "Q23. Develop an applet using parameters like text and color.",
        "Read text and color parameters in init(); choose a default when absent, map color names to Color constants, then draw the text using that color.",
    ),
    (
        "Q24. Create an applet that shows mouse click coordinates.",
        "Implement MouseListener, store e.getX() and e.getY() in mouseClicked(), increment a counter if needed, and repaint a marker plus coordinate text.",
    ),
    (
        "Q25. Design a simple drawing applet using mouse.",
        "Implement MouseMotionListener, collect points during mouseDragged(), and repaint them as small filled ovals or connected strokes.",
    ),
    (
        "Q26. Explain initialization and termination of an applet with code.",
        "Initialization is handled by init() and start(); termination is handled by stop() and destroy(). Use init() for setup, stop() to pause threads, and destroy() for final cleanup.",
    ),
    (
        "Q27. Write a complete applet program with corresponding HTML file.",
        "A complete answer includes imports, an Applet subclass, init()/paint() or event methods, plus an HTML file containing the applet tag with code, width, and height.",
    ),
    (
        "Q28. Create an applet that displays shapes based on user input.",
        "Use AWT controls such as Button, implement ActionListener, store the selected shape in actionPerformed(), and draw the chosen shape in paint().",
    ),
    (
        "Q29. Design a digital banner advertisement applet.",
        "Use a string array of ads, a thread-driven x position, rotating currentAd index, colorful text, and repaint() for continuous scrolling.",
    ),
    (
        "Q30. Build an animated applet using threads.",
        "Use a Runnable thread to update animation state such as ball position, reverse direction at boundaries, sleep briefly, and repaint the frame.",
    ),
    (
        "Q31. Compare Applet, Servlet, and Java Application.",
        "Applet is client-side and browser hosted; Servlet is server-side and responds to HTTP; Application is standalone and starts from main().",
    ),
    (
        "Q32. Why are Java Applets deprecated?",
        "They depended on browser plugins, created security risk, loaded slowly, lacked mobile support, and were replaced by HTML5, JavaScript, and modern web frameworks.",
    ),
    (
        "Q33. Suggest modern alternatives to Applets.",
        "Use HTML5 Canvas, WebGL, JavaScript frameworks, Progressive Web Apps, JavaFX for desktop GUI, or Java backends such as Servlets and Spring Boot.",
    ),
]

for question, answer in assignment_questions:
    pn.highlight(f"<b>{question}</b><br/>A: {answer}")

pn.section("Quick Revision Summary Table")
pn.info_table(
    ["Topic", "Key Exam Point"],
    [
        [
            "Applet class package",
            "java.applet.Applet -- hierarchy: Object -> Component -> Container -> Panel -> Applet",
        ],
        [
            "init() call count",
            "Exactly ONCE per applet lifetime -- one-time setup only",
        ],
        [
            "start() call count",
            "MULTIPLE times -- after init() and each time page is revisited",
        ],
        [
            "stop() call count",
            "MULTIPLE times -- each time user navigates away from page",
        ],
        [
            "destroy() call count",
            "Exactly ONCE -- when applet is permanently removed from memory",
        ],
        [
            "paint() trigger",
            "Called by AWT: on first display, after repaint(), after resize, after uncover",
        ],
        [
            "repaint() vs paint()",
            "repaint() = request a redraw (you call this); paint() = actual drawing (AWT calls this)",
        ],
        [
            "update() override reason",
            "Prevent flicker in animation by manually clearing background before paint()",
        ],
        [
            "getParameter() return",
            "Always returns String or null -- parse int with Integer.parseInt(), double with Double.parseDouble()",
        ],
        [
            "HTML required attrs",
            "code (class name), width, height -- all three are mandatory",
        ],
        [
            "showStatus() target",
            "Browser's status bar at the very bottom of the browser window",
        ],
        [
            "Flicker fix technique",
            "Override update(Graphics g): fill background then call paint(g)",
        ],
        [
            "Thread in banner",
            "Implements Runnable; scrollThread = new Thread(this); scrollThread.start()",
        ],
        [
            "Stopping thread safely",
            "In stop(): scrollThread = null; run() checks Thread.currentThread() == scrollThread",
        ],
        [
            "Applet deprecated",
            "Java 9 deprecated; Java 17 removed. All major browsers dropped Java plugin 2015-2017.",
        ],
        [
            "Modern alternatives",
            "HTML5 Canvas+JS, JavaFX (desktop), Spring Boot (web), React/Angular (UI)",
        ],
        [
            "appletviewer usage",
            "appletviewer MyApplet.html OR appletviewer MyApplet.java (with embedded <applet> comment)",
        ],
        [
            "Coordinate origin",
            "Top-left corner is (0,0); x increases right; y increases DOWN (opposite to math)",
        ],
    ],
)

pn.note(
    "For exam: Always write the APPLET TAG COMMENT in your code when asked to write an applet program. "
    "Always show the corresponding HTML file. "
    "Always override both start() and stop() when using threads (null the thread in stop()). "
    "These three habits earn full marks in 10-mark applet questions."
)

# =============================================================================
#  BUILD DOCUMENT
# =============================================================================
pn.build_doc("Java_Unit3_Notes.pdf")
print("Generated: Java_Unit3_Notes.pdf")
