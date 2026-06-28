import engrapha_notes as en
import engrapha_diagrams as ed

theme = ed.DiagramTheme.from_notes_theme(en.get_theme())

en.chap_box("2.2 Second Sub-Chapter")
en.section("Included Diagram Chapter")
en.body(
    "This second chapter focuses on vector diagrams loaded via include_chapter()."
)
en.definition("<b>Term:</b> Don't mix <i>stories.py</i> with direct <i>story</i> access unless necessary.")
en.important("Use en.add(flowable) or en.story.extend(flowables) to append diagrams.")

en.section("Layered Stack")
stack = ed.LayeredStack(
    width=300, height=160, theme=theme, caption="Fig 1: Application Layers"
)
stack.layer("Presentation")
stack.layer("Application")
stack.layer("Transport")
stack.layer("Network")
en.story.extend(stack.as_flowable())

en.section("Network Topology")
net = ed.NetworkDiagram(
    width=en.CW, height=140, theme=theme, caption="Fig 2: Simple Topology"
)
net.node("sw", "Switch", kind="switch")
net.node("a", "Host A", kind="host")
net.node("b", "Host B", kind="host")
net.link("sw", "a")
net.link("sw", "b")
en.story.extend(net.as_flowable())
