from __future__ import annotations

import paperforge_diagrams as pd
import paperforge_notes as pn


def main() -> None:
    pn.set_story([])
    pn.set_theme(pn.TEXTBOOK)
    pn.set_global_footer(
        left="PaperForge Comprehensive Demo", right="Reference", show_page_num=True
    )

    theme = pd.DiagramTheme.from_notes_theme(pn.get_theme())

    # Premium cover page with new publishing framework
    pn.bookmark("Cover Page")
    pn.suppress_footer(page_only=True)
    
    pn.cover_card(
        "PaperForge Comprehensive Demo",
        "One source exported to PDF, HTML, PPTX, and flashcards",
        cover_theme="diagram",
        bg_svg="C:\\Dev\\notes\\asset_images\\paper-and-pen-svgrepo-com.svg",
        banner_svg="assets/paperforge_banner_black.svg",
        banner_width=420.0,
        logo_svg="assets/paperforge_icon_black.svg",
        logo_width=80.0,
        author="Bharat Dangi",
        date="June 2026",
        tags=["Documentation", "Reference", "2026 Edition"],
    )
    pn.br()

    pn.suppress_footer(page_only=True)
    pn.toc()

    # UNIT 1
    pn.part_box(
        "Unit I: Document Authoring",
        subtitle="Modern typography and clean layout helpers",
        topics=["Themed Content & Core Blocks", "Math & Educational Components", "Tables, Code & Images"],
    )
    pn.chap_box("1.1 Themed Content")
    pn.section("Semantic Notes")
    pn.body(
        "This demo combines all PaperForge features in a compact reference document."
    )
    pn.definition(
        "<b>PaperForge:</b> A Python authoring toolkit for notes and vector diagrams."
    )

    pn.section("Callouts & Admonitions")
    pn.tip("Tip callout helps point out useful information.")
    pn.note("Note callout adds general side information.")
    pn.important("Important callout for key takeaways.")
    pn.warning("Warning callout when something requires attention.")

    pn.chap_box("1.2 Educational Features")
    pn.section("Math and Theorems")
    pn.body(
        f"Inline math {pn.formula(r'E = mc^2')} works perfectly. Block math is below:"
    )
    pn.formula_block(r"\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}")
    pn.theorem(
        "Pythagorean Theorem: In a right-angled triangle, the square of the hypotenuse is equal to the sum of the squares of the other two sides."
    )
    pn.proof(
        "By using similar triangles or algebraic expansion of (a+b)^2 = c^2 + 4(ab/2), we obtain a^2 + b^2 = c^2."
    )

    pn.section("Q&A and MCQ")
    pn.question("What is the main advantage of Platypus Flowables?")
    pn.answer("They handle pagination automatically across multiple pages.")
    pn.mcq(
        "Which of these is a Python web framework?",
        ["React", "Django", "Angular", "Vue"],
        correct_index=1,
    )

    pn.section("Tables and Code")
    pn.info_table(
        ["Feature", "Purpose"],
        [
            ["Themes", "Apply a consistent visual system."],
            ["Code Blocks", "Render readable source snippets."],
            ["Diagrams", "Keep technical figures vector-native."],
            ["Exports", "Generate PDF, HTML, PPTX, and flashcards."],
        ],
    )
    pn.code_block(
        """
import paperforge_notes as pn

pn.set_theme(pn.OCEAN_DARK)
pn.section("Topic")
pn.body("Write explanation here.")
pn.build_doc("notes.pdf")
""",
        lang="python",
    )

    pn.section("Images (Local, Remote & Fallbacks)")
    pn.body("Here is a local image from the project's assets folder:")
    pn.image(
        "asset_images/von_neumann.png",
        caption="Fig 1: Von Neumann Architecture (Local System)",
        link="https://en.wikipedia.org/wiki/Von_Neumann_architecture"
    )

    pn.body("Here is a remote image that falls back to a working URL because the primary path is broken:")
    pn.image(
        "broken_url.png",
        fallbacks=["https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png"],
        caption="Fig 2: Google Logo (Resolved via Fallback URL)",
        link="https://www.google.com"
    )

    pn.body("Here is a broken image path demonstrating the default styled placeholder fallback box:")
    pn.image(
        "invalid_path_example.png",
        caption="Fig 3: Non-existent Image (Renders Default Placeholder)",
        width=150,
        height=100
    )
    pn.br()

    # UNIT 2
    pn.part_box(
        "Unit II: Diagram Coverage",
        subtitle="Native vector drawing API",
        topics=["Flowcharts & Decisions", "Architecture & Blocks", "Timing & Signal Transitions"],
    )

    pn.chap_box("2.1 Core Workflows")
    pn.section("Flowchart")
    fc = pd.Flowchart(
        width=pn.CW, height=300, theme=theme, caption="Fig 1: Compile Workflow"
    )
    fc.terminal("start", "START")
    fc.process("parse", "Parse Source")
    fc.decision("check", "Valid?")
    fc.process("render", "Render Flowables")
    fc.terminal("done", "DONE")
    fc.edge("start", "parse")
    fc.edge("parse", "check")
    fc.edge("check", "render", label="Yes")
    fc.edge("check", "parse", label="No")
    fc.edge("render", "done")
    pn.story.extend(fc.as_flowable())

    pn.section("State Machine")
    sm = pd.StateMachine(
        width=pn.CW, height=180, theme=theme, caption="Fig 2: Simple Parser State"
    )
    sm.state("idle", "Idle", initial=True)
    sm.state("read", "Reading")
    sm.state("end", "End", accepting=True)
    sm.transition("idle", "read", "char")
    sm.transition("read", "read", "char")
    sm.transition("read", "end", "EOF")
    pn.story.extend(sm.as_flowable())

    pn.chap_box("2.2 Software Architecture")
    pn.section("Architecture")
    arch = pd.ArchitectureDiagram(
        width=pn.CW, height=220, theme=theme, caption="Fig 3: Authoring Platform"
    )
    arch.client("author", "Author")
    arch.service("notes", "Notes Engine")
    arch.service("diagrams", "Diagram Engine")
    arch.database("outputs", "Generated Files")
    arch.connect("author", "notes", "writes")
    arch.connect("notes", "diagrams", "embeds")
    arch.connect("diagrams", "outputs", "exports")
    pn.story.extend(arch.as_flowable())

    pn.section("Network Diagram")
    net = pd.NetworkDiagram(
        width=pn.CW, height=150, theme=theme, caption="Fig 4: Cloud Layout"
    )
    net.node("r1", "Core Router", kind="router")
    net.node("s1", "Switch A", kind="switch", label_pos="left")
    net.node("srv1", "Web Server", kind="server", label_pos="right")
    net.node("db1", "Primary DB", kind="database")
    net.link("r1", "s1")
    net.link("s1", "srv1")
    net.link("srv1", "db1")
    pn.story.extend(net.as_flowable())

    pn.chap_box("2.3 Data and Models")
    pn.section("Sequence Diagram")
    seq = pd.SequenceDiagram(
        width=pn.CW, height=200, theme=theme, caption="Fig 5: HTTP Request"
    )
    seq.actor("u", "User")
    seq.actor("s", "Server")
    seq.message("u", "s", "GET /api/data")
    seq.activate("s")
    seq.message("s", "u", "200 OK", arrow="dashed")
    seq.deactivate("s")
    pn.story.extend(seq.as_flowable())

    pn.section("Class Diagram")
    cd = pd.ClassDiagram(
        width=pn.CW, height=240, theme=theme, caption="Fig 6: Inheritance"
    )
    cd.uml_class(
        "Shape", "Shape", attributes=["+ x: float", "+ y: float"], methods=["+ draw()"]
    )
    cd.uml_class(
        "Circle", "Circle", attributes=["+ radius: float"], methods=["+ draw()"]
    )
    cd.uml_class("Square", "Square", attributes=["+ side: float"], methods=["+ draw()"])
    cd.relate("Circle", "Shape", kind="inheritance")
    cd.relate("Square", "Shape", kind="inheritance")
    pn.story.extend(cd.as_flowable())

    pn.section("ER Diagram")
    er = pd.ERDiagram(
        width=pn.CW, height=200, theme=theme, caption="Fig 7: User Orders"
    )
    er.entity("User", x=100, y=100)
    er.entity("Order", x=400, y=100)
    er.attribute("ID", "User", pk=True)
    er.attribute("Name", "User")
    er.attribute("Order_ID", "Order", pk=True)
    er.attribute("Total", "Order")
    er.relationship("places", x=250, y=100)
    er.connect("User", "places", "1", "1")
    er.connect("places", "Order", "N", "N")
    pn.story.extend(er.as_flowable())

    pn.chap_box("2.4 Advanced Technical")
    pn.section("Layered Stack")
    stack = pd.LayeredStack(
        width=300, height=180, theme=theme, caption="Fig 8: Software Layers"
    )
    stack.layer("UI Layer")
    stack.layer("Service Layer")
    stack.layer("Data Access Layer")
    stack.layer("Database")
    pn.story.extend(stack.as_flowable())

    pn.section("Timing Diagram")
    td = pd.TimingDiagram(
        width=pn.CW, height=150, theme=theme, caption="Fig 9: Clock Signal"
    )
    td.clock("CLK", period=1.0, cycles=8)
    td.signal("DATA", transitions=[(0, 0), (2.0, 1), (4.0, 0), (6.0, 1)])
    pn.story.extend(td.as_flowable())
    pn.br()

    # UNIT 3
    pn.part_box(
        "Unit III: Study Features",
        subtitle="Cross-referencing and interactive aids",
        topics=["Labels & Target Referencing", "Flashcards & Revision Checklists", "Document Indexes"],
    )
    pn.chap_box("3.1 References and Flashcards")
    pn.section("Cross References")
    pn.label("sec_study")
    pn.body(
        f"Cross references resolve during multi-pass PDF builds. This section is page {pn.ref('sec_study')}."
    )
    pn.body(
        f"Index entries are collected for final review{pn.index_entry('Cross Reference')}."
    )

    pn.flashcard(
        "What does as_flowable() return?",
        "A list of Platypus flowables containing the diagram.",
    )
    pn.flashcard(
        "Why use vector diagrams?",
        "They remain crisp in PDF and avoid external rendering tools.",
    )
    pn.revision_card(
        "PaperForge Checklist",
        ["Run package tests.", "Compile target notes.", "Inspect generated outputs."],
    )

    pn.part_box(
        "Document Index",
        subtitle="Alphabetical keyword catalog",
    )
    pn.print_index()

    # COVER STYLE SHOWCASE
    pn.br()
    pn.bookmark("Hero Cover Style")
    pn.suppress_footer(page_only=True)
    pn.cover_card(
        "Hero Architecture",
        "Bold, solid background fill with a clean edge stripe",
        cover_theme="hero",
        author="Bharat Dangi",
        date="June 2026",
    )
    
    pn.br()
    pn.bookmark("Book Cover Style")
    pn.suppress_footer(page_only=True)
    pn.cover_card(
        "Book Architecture",
        "Classic textbook split layout with dual background tones",
        cover_theme="book",
        author="Bharat Dangi",
        date="June 2026",
    )
    
    pn.br()
    pn.bookmark("Academic Modern Cover Style")
    pn.suppress_footer(page_only=True)
    pn.cover_card(
        "Academic Modern Architecture",
        "Clean left edge dual-stripe bounding the whole page",
        cover_theme="academic_modern",
        author="Bharat Dangi",
        date="June 2026",
    )

    # OUTPUTS
    pn.build_doc("demo_comprehensive.pdf")
    pn.build_html("demo_comprehensive_html")
    pn.build_pptx("demo_comprehensive.pptx")
    pn.build_split_doc(
        "demo_comprehensive.pdf", split_by="part", reset_page_numbers=True
    )

    print("Generated: demo_comprehensive.pdf")
    print("Generated: demo_comprehensive_html")
    print("Generated: demo_comprehensive.pptx")


if __name__ == "__main__":
    main()
