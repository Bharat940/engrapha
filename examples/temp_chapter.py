import engrapha_notes as en
import engrapha_diagrams as ed

theme = ed.DiagramTheme.from_notes_theme(en.get_theme())

en.chap_box("2.1 First Sub-Chapter")
en.section("Included Python Chapter")
en.body(
    "This section was loaded dynamically from temp_chapter.py. "
    "Modular compilation lets you split content across multiple files."
)
en.tip("Keep files small and focused for maintainable note projects.")
en.bullet([
    "Each chapter file stays self-contained.",
    "Shared theme config flows through the parent script.",
])
en.code_block(
    "result = [i*i for i in range(10)]",
    lang="python",
    theme=en.DRACULA,
)

en.section("Embedded Diagram")
fc = ed.Flowchart(
    width=en.CW, height=150, theme=theme, caption="Fig 1: Included Flowchart"
)
fc.terminal("s", "START")
fc.process("load", "Load Chapter")
fc.terminal("e", "END")
fc.edge("s", "load")
fc.edge("load", "e")
en.story.extend(fc.as_flowable())
