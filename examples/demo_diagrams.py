from __future__ import annotations

import paperforge_diagrams as pd
import paperforge_notes as pn


def add_diagram(diagram: pd.DiagramBase) -> None:
    """Append one diagram and a small spacer to the active notes story."""
    pn.story.extend(diagram.as_flowable())
    pn.sp(10)


def main() -> None:
    pn.set_story([])
    pn.set_theme(pn.DARK)
    pn.set_global_footer(left="PaperForge Diagrams", right="Demo", show_page_num=True)

    theme = pd.DiagramTheme.from_notes_theme(pn.get_theme())

    pn.cover_card("PaperForge Diagrams", "Vector-native ReportLab diagram reference")
    # pn.cover_subtitle("Flowchart, sequence, class, ER, state, timing, network, and architecture examples")
    pn.br()
    pn.toc()

    pn.part_box("Core Diagram Builders")

    pn.section("Flowchart")
    fc = pd.Flowchart(width=pn.CW, height=250, theme=theme, caption="Fig 1: Request Validation Flow")
    fc.terminal("start", "START")
    fc.process("read", "Read Request")
    fc.decision("valid", "Valid Input?")
    fc.process("save", "Save Record")
    fc.terminal("end", "END")
    fc.edge("start", "read")
    fc.edge("read", "valid")
    fc.edge("valid", "save", branch="yes")
    fc.edge("valid", "read", branch="no", orthogonal=True)
    fc.edge("save", "end")
    add_diagram(fc)

    pn.section("Sequence Diagram")
    seq = pd.SequenceDiagram(width=pn.CW, height=260, theme=theme, caption="Fig 2: Login Sequence")
    seq.actor("user", "User")
    seq.actor("web", "Web App")
    seq.actor("auth", "Auth Service")
    seq.message("user", "web", "Submit credentials")
    seq.activate("web")
    seq.message("web", "auth", "Validate")
    seq.activate("auth")
    seq.message("auth", "web", "Token")
    seq.deactivate("auth")
    seq.message("web", "user", "Dashboard")
    seq.deactivate("web")
    add_diagram(seq)

    pn.section("Class Diagram")
    cd = pd.ClassDiagram(width=pn.CW, height=260, theme=theme, caption="Fig 3: Repository Classes")
    cd.uml_class("repo", "UserRepository", stereotype="interface", methods=["+ findById(id): User", "+ save(user): void"])
    cd.uml_class("sql", "SqlUserRepository", attributes=["- connection: Connection"], methods=["+ findById(id): User", "+ save(user): void"])
    cd.relate("sql", "repo", kind="realization")
    add_diagram(cd)

    pn.section("ER Diagram")
    er = pd.ERDiagram(width=pn.CW, height=250, theme=theme, caption="Fig 4: Enrollment ER Model")
    er.entity("STUDENT")
    er.relationship("ENROLLS")
    er.entity("COURSE")
    er.entity_attributes("STUDENT", [("Student_ID", {"pk": True}), "Name"])
    er.entity_attributes("COURSE", [("Course_ID", {"pk": True}), "Title"])
    er.attribute("Grade", parent="ENROLLS")
    er.connect("STUDENT", "ENROLLS", card_from="1", card_to="N")
    er.connect("COURSE", "ENROLLS", card_from="1", card_to="N")
    add_diagram(er)

    pn.section("Network Diagram")
    net = pd.NetworkDiagram(width=pn.CW, height=240, theme=theme, caption="Fig 5: Web Deployment")
    net.node("internet", "Internet", kind="cloud")
    net.node("fw", "Firewall", kind="firewall")
    net.node("lb", "Load Balancer", kind="load_balancer")
    net.node("api", "API Server", kind="server")
    net.node("db", "Database", kind="database")
    net.link("internet", "fw")
    net.link("fw", "lb")
    net.link("lb", "api")
    net.link("api", "db")
    add_diagram(net)

    pn.section("State Machine")
    sm = pd.StateMachine(width=pn.CW, height=210, theme=theme, caption="Fig 6: Order State Machine")
    sm.state("new", "New", initial=True)
    sm.state("paid", "Paid")
    sm.state("packed", "Packed")
    sm.state("done", "Delivered", accepting=True)
    sm.transition("new", "paid", label="payment")
    sm.transition("paid", "packed", label="pack")
    sm.transition("packed", "done", label="ship")
    add_diagram(sm)

    pn.section("Timing Diagram")
    td = pd.TimingDiagram(width=pn.CW, height=190, theme=theme, caption="Fig 7: SPI Timing")
    td.clock("SCLK", period=20.0, cycles=8)
    td.signal("CS", transitions=[(0, 1), (5, 0), (165, 1)])
    td.signal("MOSI", transitions=[(0, 0), (20, 1), (60, 0), (120, 1)])
    add_diagram(td)

    pn.section("Layered Stack")
    stack = pd.LayeredStack(width=pn.CW, height=250, theme=theme, caption="Fig 8: TCP/IP Stack")
    stack.layer("Application", sublabel="HTTP, DNS, SMTP")
    stack.layer("Transport", sublabel="TCP, UDP")
    stack.layer("Internet", sublabel="IP, ICMP")
    stack.layer("Network Access", sublabel="Ethernet, Wi-Fi")
    add_diagram(stack)

    pn.part_box("Newer Builders")

    pn.section("Schema, Architecture, C4, Git, and AWS")
    schema = pd.SchemaDiagram(width=pn.CW, height=230, theme=theme, caption="Fig 9: Database Schema")
    schema.table("users", [("id", "INT", {"pk": True}), ("email", "VARCHAR", {})])
    schema.table("orders", [("id", "INT", {"pk": True}), ("user_id", "INT", {"fk": True})])
    schema.relation("orders", "user_id", "users", "id")
    add_diagram(schema)

    arch = pd.ArchitectureDiagram(width=pn.CW, height=220, theme=theme, caption="Fig 10: Service Architecture")
    arch.client("web", "Web App")
    arch.service("api", "Auth API")
    arch.database("db", "Postgres")
    arch.queue("queue", "Job Queue")
    arch.connect("web", "api", "HTTPS")
    arch.connect("api", "db", "SQL")
    arch.connect("api", "queue", "events")
    add_diagram(arch)

    c4 = pd.C4ContainerDiagram(width=pn.CW, height=220, theme=theme, caption="Fig 11: C4 Container View")
    c4.system("shop", "Shop System")
    c4.container("api", "Spring Boot", "Business API")
    c4.container("db", "PostgreSQL", "Stores orders")
    c4.relate("shop", "api", "uses")
    c4.relate("api", "db", "reads and writes")
    add_diagram(c4)

    git = pd.GitDiagram(width=pn.CW, height=180, theme=theme, caption="Fig 12: Git Branch Flow")
    git.commit("main", "init")
    git.branch("main", "feature")
    git.commit("feature", "login")
    git.merge("feature", "main", "merge")
    add_diagram(git)

    aws = pd.AWSDiagram(width=pn.CW, height=220, theme=theme, caption="Fig 13: AWS Service Sketch")
    aws.ec2("app", "EC2 App")
    aws.rds("db", "RDS DB")
    aws.s3("assets", "S3 Assets")
    aws.connect("app", "db", "SQL")
    aws.connect("app", "assets", "objects")
    add_diagram(aws)

    pn.build_doc("demo_diagrams.pdf")
    print("Generated: demo_diagrams.pdf")


if __name__ == "__main__":
    main()
