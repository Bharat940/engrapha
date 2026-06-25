"""
demo_themes.py -- Generates demo_themes.pdf showing preset themes, custom themes, and templates.

Each theme gets its own page showing headings, body text, tip, note, definition,
info table, frame format, packet format, a flowchart, and a layered stack.

Run:
    python demo_themes.py
"""

from __future__ import annotations

import paperforge_notes as pn
import paperforge_diagrams as pd

# Clear story list
pn.set_story([])

# Generate Table of Contents page
pn.toc()
pn.suppress_footer(page_only=True)

# Render all preset themes, one page per theme
for idx, theme in enumerate(pn.ALL_THEMES):
    # Set the active theme
    pn.set_theme(theme)
    pn.footer(
        left=f"Theme: {theme.name}",
        right="PaperForge Themes Showcase",
        show_page_num=True,
    )

    # Showcase heading
    pn.part_box(f"Theme: {theme.name}")

    pn.section("1. Content Helpers")
    pn.body(
        f"This page demonstrates the <b>{theme.name}</b> theme. "
        "All helper functions retrieve the active theme dynamically at render-time. "
        "Body text is styled using <i>Helvetica</i> for clear readability."
    )

    pn.bullet(
        [
            "Bullet points automatically match the theme's text color.",
            "The bullet character itself uses the accent color.",
        ]
    )

    pn.definition(
        "<b>Definition:</b> The boundary box uses the theme's primary accent color."
    )
    pn.tip("This is an exam tip callout box in green.")
    pn.note("This is a note callout box in yellow.")

    pn.sp(4)
    pn.section("2. Tables and Monospace Code")
    pn.info_table(
        ["Field Name", "Theme Default Hex", "Purpose"],
        [
            ["bg", theme.bg, "Canvas and page background"],
            ["accent", theme.accent, "Headers, rules, borders, and main strokes"],
            ["accent2", theme.accent2, "Secondary nodes, decisions, relations"],
            ["text", theme.text, "Primary body text color"],
        ],
    )

    # Demonstrate Dracula syntax highlighting theme override on preset pages
    pn.code_block(
        f"""
// Active Theme Configuration: {theme.name}
#define ACCENT "{theme.accent}"
#define BG     "{theme.bg}"
void init_theme() {{
    print("Theme applied successfully!");
}}
""",
        lang="c",
        theme=pn.DRACULA,
    )

    pn.sp(4)
    pn.section("3. Frame & Packet Formats")
    pn.frame_format(
        "Sample Header Frame Layout",
        [
            ("PREAMBLE", "7B"),
            ("SFD", "1B"),
            ("HEADER", "20B"),
            ("PAYLOAD", "Var"),
            ("FCS", "4B"),
        ],
    )

    pn.packet_format(
        "UDP Segment Format (8 bytes)",
        [
            ("Source Port", 16),
            ("Destination Port", 16),
            ("Length", 16),
            ("Checksum", 16),
        ],
        bit_ruler=True,
    )

    pn.sp(4)
    pn.section("4. Theme-Compatible Vector Diagrams", bookmark=False)

    # Get the matching DiagramTheme from NotesTheme
    diag_theme = pd.DiagramTheme.from_notes_theme(theme)

    # Star spoke kind
    net = pd.NetworkDiagram(
        width=pn.CW, height=180, theme=diag_theme, caption="Star Topology in Theme"
    )
    net.star_topology(
        "sw", "Core Switch", ["Host-A", "Host-B", "Host-C"], spoke_kind="host"
    )
    for flowable in net.as_flowable():
        pn.add(flowable)

    # Simple flowchart
    fc = pd.Flowchart(
        width=pn.CW, height=140, theme=diag_theme, caption="GCD Flowchart in Theme"
    )
    fc.terminal("s", "START")
    fc.process("p", "A = A - B")
    fc.decision("d", "A == B?")
    fc.terminal("e", "END")
    fc.edge("s", "p")
    fc.edge("p", "d")
    fc.edge("d", "e", branch="yes")
    fc.edge("d", "p", branch="no", orthogonal=True)
    for flowable in fc.as_flowable():
        pn.add(flowable)

    pn.br()

# 9. Custom Theme built via ThemeBuilder
custom_theme = (
    pn.ThemeBuilder()
    .set_colors(bg="#0b0f19", surface="#151d30", accent="#ff007f")
    .set_fonts(body_font="Helvetica", heading_font="Helvetica-Bold", size_body=10.5)
    .set_borders(thickness=1.5, color="#ff007f")
    .set_header_footer(show_headers=True, divider_thickness=0.8)
    .build()
)

pn.set_theme(custom_theme)
pn.footer(
    left="Custom ThemeBuilder Design",
    right="Pink Cyberpunk Theme Showcase",
    show_page_num=True,
)
pn.part_box("Custom ThemeBuilder Showcase")
pn.body(
    "This page showcases a custom theme built dynamically using the <b>ThemeBuilder</b> API. "
    "Notice the cyberpunk pink accent, custom background, and custom borders."
)
pn.code_block(
    """
# Python code block styled with Monokai
def build_custom_theme():
    builder = pn.ThemeBuilder()
    builder.set_colors(bg="#0b0f19", accent="#ff007f")
    return builder.build()
""",
    lang="python",
    theme=pn.MONOKAI,
)

pn.br()

# 10. EngineeringNotes Template Showcase
pn.EngineeringNotes(dark=True)
pn.footer(
    left="Engineering Notes Layout",
    right="Technical Notebook Template",
    show_page_num=True,
)
pn.part_box("EngineeringNotes Template")
pn.body(
    "This page uses the prebuilt <b>EngineeringNotes</b> template, optimized for formulas, "
    "equations, code blocks, and diagrams."
)
pn.tip("Use this template for technical documentations and textbook compilation.")

pn.br()

# 11. QuestionBank Template Showcase
pn.QuestionBank(dark=False)
pn.footer(
    left="Question Bank Layout (Light)",
    right="Academic Exam template",
    show_page_num=True,
)
pn.part_box("QuestionBank Template")
pn.body(
    "This page demonstrates the <b>QuestionBank</b> template in light mode. "
    "It uses a serif font (Times-Roman) and compact layout margins to fit exam questions."
)
pn.note(f"Footnotes can also be resolved dynamically in the margins{pn.footnote('Footnote resolved inside the bottom margin area of the QuestionBank template page.')}.")

# 12. Print-Ready Layout Showcase (Double Page Borders, 3-Column Headers/Footers, Style Overrides)
print_showcase_theme = pn.LIGHT.copy_with(
    name="Print Showcase Theme",
    body_font="Times-Roman",
    heading_font="Times-Bold",
    double_page_border=True,
    page_border_margin=15.0,
    page_border_gap=3.0,
    show_headers=True,
)
pn.set_theme(print_showcase_theme)

# Set 3-column header and footer
pn.set_global_header(
    left="PaperForge Showcase",
    center="Semester – IV",
    right="Session: Jan-June 2026",
    y_offset=0.8,
    line_y_offset=0.85,
)
pn.set_global_footer(
    left="Name: Jane Doe",
    center="Enrollment no: 0101IT999999",
    show_page_num=True,
)

# Start a new page for the print template
pn.br()

pn.part_box("Advanced Print Layout Template")
pn.body(
    "This page showcases PaperForge's advanced layout settings tailored for academic assignments and exams. "
    "Features shown on this page include:"
)
pn.bullet(
    [
        "<b>Double concentric page borders:</b> A premium border styling suited for print media.",
        "<b>Three-column running header & footer:</b> Left, centered, and right elements (including dynamic enrollment info).",
        "<b>Adjustable vertical offsets:</b> Fine-tune header text spacing relative to the borders and text content.",
        "<b>Component-level style overrides:</b> Modify fonts and border properties for specific components inline."
    ]
)

# Style override showcase
pn.qbox(
    "Sample Question with Accent Red Override",
    font_name="Times-Bold",
    font_size=12,
    text_color="#ff0000",
    bg_color="#ffffff",
    border_color="#000000"
)
pn.body("This question box uses inline component overrides for its font name, text color, and border color.")

# Build the document
pn.build_doc("demo_themes.pdf")
print("Generated: demo_themes.pdf")
