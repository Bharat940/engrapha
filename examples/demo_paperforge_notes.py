from __future__ import annotations

import paperforge_diagrams as pd
import paperforge_notes as pn


def main() -> None:
    pn.set_story([])
    pn.set_theme(pn.CATPPUCCIN_MOCHA)
    pn.set_global_footer(left="PaperForge Notes", right="API Demo", show_page_num=True)

    pn.bookmark("Cover Page")
    pn.suppress_footer(page_only=True)
    pn.cover_card(
        "PaperForge Notes",
        "Themed blocks, code, formulas, references, and diagrams",
        cover_theme="catppuccin",
        author="Bharat Dangi",
        date="June 2026",
        ornament="dots",
        tags=["Theming", "Components", "Catppuccin Mocha"],
    )
    pn.br()

    pn.suppress_footer(page_only=True)
    pn.toc()

    pn.part_box("Unit I: Layout Helpers")
    pn.chap_box("1.1 Core Blocks")
    pn.section("Body, Definitions, and Callouts")
    pn.body("PaperForge uses semantic helper functions so notes scripts stay readable and maintainable.")
    pn.definition("<b>Semantic Block:</b> A helper that expresses document meaning instead of canvas coordinates.")
    pn.tip("Use diagrams near the explanation they support.")
    pn.warning("Keep table and diagram labels concise to avoid cramped layouts.")
    pn.important("Themes propagate to notes and diagrams through the active theme object.")

    pn.section("Question and Answer Blocks")
    pn.question("Explain the purpose of a listener in Java event handling.")
    pn.answer("A listener receives callback methods when a registered event source fires an event.")
    pn.mcq(
        "Which JDBC object represents tabular query output?",
        ["Connection", "Statement", "ResultSet", "DriverManager"],
        correct_index=2,
    )

    pn.section("Code Blocks")
    pn.code_block(
        """
import java.awt.event.*;

class SaveHandler implements ActionListener {
    @Override
    public void actionPerformed(ActionEvent event) {
        System.out.println(event.getActionCommand());
    }
}
""",
        lang="java",
        theme=pn.DRACULA,
    )

    pn.section("Formula and Reference Features")
    pn.label("sec_formula")
    pn.body(f"Inline formulas are supported, for example {pn.formula('E = mc^2')}.")
    pn.formula_block(r"\int_a^b f(x)\,dx")
    pn.body(f"This paragraph references the formula section on page {pn.ref('sec_formula')}.")
    pn.body(f"Index entries can be attached inline{pn.index_entry('Formula')}.")

    pn.section("Native Diagram Embedding")
    theme = pd.DiagramTheme.from_notes_theme(pn.get_theme())
    fc = pd.Flowchart(width=pn.CW, height=210, theme=theme, caption="Fig 1: Notes Build Pipeline")
    fc.terminal("start", "Markdown or Python")
    fc.process("notes", "paperforge_notes")
    fc.process("diagrams", "paperforge_diagrams")
    fc.terminal("pdf", "PDF, HTML, PPTX")
    fc.edge("start", "notes")
    fc.edge("notes", "diagrams")
    fc.edge("diagrams", "pdf")
    pn.story.extend(fc.as_flowable())

    pn.section("Revision Cards and Flashcards")
    pn.revision_card("Event Handling", ["Source creates an event object.", "Listener callback handles it.", "Registration connects source to listener."])
    pn.flashcard("What is JDBC?", "Java Database Connectivity.")

    pn.part_box("Document Index")
    pn.print_index()

    pn.build_doc("demo_paperforge_notes.pdf")
    print("Generated: demo_paperforge_notes.pdf")


if __name__ == "__main__":
    main()
