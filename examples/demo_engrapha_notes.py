from __future__ import annotations

import engrapha_diagrams as ed
import engrapha_notes as en


def main() -> None:
    en.set_story([])
    en.set_theme(en.CATPPUCCIN_MOCHA)
    en.set_global_footer(left="engrapha Notes", right="API Demo", show_page_num=True)

    en.bookmark("Cover Page")
    en.suppress_footer(page_only=True)
    en.cover_card(
        "engrapha Notes",
        "Themed blocks, code, formulas, references, and diagrams",
        cover_theme="catppuccin",
        author="Bharat Dangi",
        date="June 2026",
        ornament="dots",
        tags=["Theming", "Components", "Catppuccin Mocha"],
    )
    en.br()

    en.suppress_footer(page_only=True)
    en.toc()

    en.part_box("Unit I: Layout Helpers")
    en.chap_box("1.1 Core Blocks")
    en.section("Body, Definitions, and Callouts")
    en.body("engrapha uses semantic helper functions so notes scripts stay readable and maintainable.")
    en.definition("<b>Semantic Block:</b> A helper that expresses document meaning instead of canvas coordinates.")
    en.tip("Use diagrams near the explanation they support.")
    en.warning("Keep table and diagram labels concise to avoid cramped layouts.")
    en.important("Themes propagate to notes and diagrams through the active theme object.")

    en.section("Question and Answer Blocks")
    en.question("Explain the purpose of a listener in Java event handling.")
    en.answer("A listener receives callback methods when a registered event source fires an event.")
    en.mcq(
        "Which JDBC object represents tabular query output?",
        ["Connection", "Statement", "ResultSet", "DriverManager"],
        correct_index=2,
    )

    en.section("Code Blocks")
    en.code_block(
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
        theme=en.DRACULA,
    )

    en.section("Formula and Reference Features")
    en.label("sec_formula")
    en.body(f"Inline formulas are supported, for example {en.formula('E = mc^2')}.")
    en.formula_block(r"\int_a^b f(x)\,dx")
    en.body(f"This paragraph references the formula section on page {en.ref('sec_formula')}.")
    en.body(f"Index entries can be attached inline{en.index_entry('Formula')}.")

    en.section("Native Diagram Embedding")
    theme = ed.DiagramTheme.from_notes_theme(en.get_theme())
    fc = ed.Flowchart(width=en.CW, height=210, theme=theme, caption="Fig 1: Notes Build Pipeline")
    fc.terminal("start", "Markdown or Python")
    fc.process("notes", "engrapha_notes")
    fc.process("diagrams", "engrapha_diagrams")
    fc.terminal("pdf", "PDF, HTML, PPTX")
    fc.edge("start", "notes")
    fc.edge("notes", "diagrams")
    fc.edge("diagrams", "pdf")
    en.story.extend(fc.as_flowable())

    en.section("Revision Cards and Flashcards")
    en.revision_card("Event Handling", ["Source creates an event object.", "Listener callback handles it.", "Registration connects source to listener."])
    en.flashcard("What is JDBC?", "Java Database Connectivity.")

    en.part_box("Document Index")
    en.print_index()

    en.build_doc("demo_engrapha_notes.pdf")
    print("Generated: demo_engrapha_notes.pdf")


if __name__ == "__main__":
    main()
