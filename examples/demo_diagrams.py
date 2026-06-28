"""
demo_diagrams.py — engrapha Diagrams showcase.

Each figure is a realistic, non-trivial example designed to show off the
depth of the corresponding builder.  Run with the project venv:

    .venv/Scripts/python examples/demo_diagrams.py
"""

from __future__ import annotations

import engrapha_diagrams as ed
import engrapha_notes as en


def add_diagram(diagram: ed.DiagramBase) -> None:
    """Append one diagram and a small spacer to the active notes story."""
    en.story.extend(diagram.as_flowable())
    en.sp(10)


def main() -> None:
    en.set_story([])
    en.set_theme(en.DARK)
    en.set_global_footer(left="engrapha Diagrams", right="Showcase", show_page_num=True)

    theme = ed.DiagramTheme.from_notes_theme(en.get_theme())

    en.cover_card(
        "engrapha Diagrams", "A comprehensive showcase of every diagram builder"
    )
    en.br()
    en.toc()

    # =========================================================================
    en.part_box("Core Flow & Logic")
    # =========================================================================

    # ── Fig 1: Flowchart ─────────────────────────────────────────────────────
    en.section("Flowchart")
    fc = ed.Flowchart(
        width=en.CW,
        height=520,
        theme=theme,
        caption="Fig 1: User Authentication & Password Reset Flow",
    )
    fc.terminal("start", "START")
    fc.io_box("input", "Enter Username\n& Password")
    fc.predefined("lookup", "DB Lookup\nUser Record")
    fc.decision("found", "User\nFound?")
    fc.decision("locked", "Account\nLocked?")
    fc.process("verify", "Verify Password\nHash (bcrypt)")
    fc.decision("valid", "Password\nValid?")
    fc.predefined("log_fail", "Log Failed\nAttempt")
    fc.decision("max_fail", "≥ 5 Failed\nAttempts?")
    fc.process("lock", "Lock Account\n& Notify User")
    fc.process("reset_counter", "Reset Fail\nCounter")
    fc.predefined("issue_token", "Issue JWT\nSession Token")
    fc.io_box("dashboard", "Redirect to\nDashboard")
    fc.terminal("end", "END")
    fc.process("err_user", "Show: User\nNot Found")
    fc.process("err_locked", "Show: Account\nLocked")

    fc.edge("start", "input")
    fc.edge("input", "lookup")
    fc.edge("lookup", "found")
    fc.edge("found", "locked", branch="yes")
    fc.edge("found", "err_user", branch="no")
    fc.edge("err_user", "end")
    fc.edge("locked", "err_locked", branch="yes")
    fc.edge("locked", "verify", branch="no")
    fc.edge("err_locked", "end")
    fc.edge("verify", "valid")
    fc.edge("valid", "reset_counter", branch="yes")
    fc.edge("valid", "log_fail", branch="no")
    fc.edge("log_fail", "max_fail")
    fc.edge("max_fail", "lock", branch="yes")
    fc.edge("max_fail", "input", branch="no", orthogonal=True)
    fc.edge("lock", "end")
    fc.edge("reset_counter", "issue_token")
    fc.edge("issue_token", "dashboard")
    fc.edge("dashboard", "end")
    add_diagram(fc)

    # ── Fig 2: Sequence Diagram ───────────────────────────────────────────────
    en.section("Sequence Diagram")
    seq = ed.SequenceDiagram(
        width=en.CW,
        height=320,
        theme=theme,
        caption="Fig 2: Microservice Order Checkout Flow",
    )
    seq.actor("browser", "Browser")
    seq.actor("gateway", "API Gateway")
    seq.actor("order", "Order Svc")
    seq.actor("inventory", "Inventory Svc")
    seq.actor("db", "Orders DB")
    seq.actor("payment", "Payment Svc")

    seq.message("browser", "gateway", "POST /checkout")
    seq.activate("gateway")
    seq.message("gateway", "order", "createOrder(cart)")
    seq.activate("order")
    seq.message("order", "inventory", "reserveItems(cart)")
    seq.activate("inventory")
    seq.message("inventory", "order", "reserved: OK", arrow="dashed")
    seq.deactivate("inventory")
    seq.message("order", "db", "INSERT order")
    seq.activate("db")
    seq.message("db", "order", "order_id: 4821", arrow="dashed")
    seq.deactivate("db")
    seq.divider("Payment Processing")
    seq.message("order", "payment", "charge(card, amount)")
    seq.activate("payment")
    seq.message("payment", "payment", "retry on timeout")
    seq.message("payment", "order", "txn_id: px_9f2a", arrow="dashed")
    seq.deactivate("payment")
    seq.message("order", "gateway", "201 Created {order_id}", arrow="dashed")
    seq.deactivate("order")
    seq.message("gateway", "browser", "200 OK {receipt}", arrow="dashed")
    seq.deactivate("gateway")
    add_diagram(seq)

    # ── Fig 3: Class Diagram ──────────────────────────────────────────────────
    en.section("Class Diagram")
    cd = ed.ClassDiagram(
        width=en.CW,
        height=300,
        theme=theme,
        caption="Fig 3: E-Commerce Domain Model",
    )
    cd.uml_class(
        "product",
        "Product",
        attributes=["- id: UUID", "- name: String", "- price: Decimal", "- stock: int"],
        methods=["+ getPrice(): Decimal", "+ isAvailable(): bool"],
    )
    cd.uml_class(
        "digital",
        "DigitalProduct",
        stereotype="entity",
        attributes=["- downloadUrl: URL", "- licenseKey: String"],
        methods=["+ generateKey(): String"],
    )
    cd.uml_class(
        "physical",
        "PhysicalProduct",
        stereotype="entity",
        attributes=["- weight: float", "- dimensions: Tuple"],
        methods=["+ shippingCost(): Decimal"],
    )
    cd.uml_class(
        "cart",
        "ShoppingCart",
        attributes=["- sessionId: String", "- createdAt: DateTime"],
        methods=[
            "+ addItem(p): void",
            "+ totalPrice(): Decimal",
            "+ checkout(): Order",
        ],
    )
    cd.uml_class(
        "cartitem",
        "CartItem",
        attributes=["- quantity: int", "- unitPrice: Decimal"],
        methods=["+ subtotal(): Decimal"],
    )
    cd.uml_class(
        "order",
        "Order",
        attributes=["- orderId: UUID", "- status: OrderStatus", "- placedAt: DateTime"],
        methods=["+ cancel(): void", "+ ship(): void"],
    )
    cd.uml_class(
        "irepo",
        "IProductRepository",
        stereotype="interface",
        methods=[
            "+ findById(id): Product",
            "+ search(q): List[Product]",
            "+ save(p): void",
        ],
    )
    cd.relate("digital", "product", kind="inheritance")
    cd.relate("physical", "product", kind="inheritance")
    cd.relate("cart", "cartitem", kind="composition", from_mult="1", to_mult="*")
    cd.relate("cartitem", "product", kind="association", from_mult="*", to_mult="1")
    cd.relate("cart", "order", kind="dependency", label="creates")
    cd.relate("digital", "irepo", kind="realization")
    cd.relate("physical", "irepo", kind="realization")
    add_diagram(cd)

    # ── Fig 4: ER Diagram ─────────────────────────────────────────────────────
    en.section("ER Diagram")
    er = ed.ERDiagram(
        width=en.CW,
        height=300,
        theme=theme,
        caption="Fig 4: Hospital Management ER Model",
    )
    # Entities
    er.entity("PATIENT")
    er.entity("DOCTOR")
    er.entity("DEPARTMENT")
    er.entity("PRESCRIPTION", weak=True)

    # Relationships
    er.relationship("TREATS")
    er.relationship("WORKS_IN")
    er.relationship("ISSUED_TO", identifying=True)

    # Attributes for PATIENT
    er.entity_attributes(
        "PATIENT",
        [
            ("Patient_ID", {"pk": True}),
            "Name",
            "DOB",
            ("Phone", {"multivalued": True}),
        ],
    )
    # Attributes for DOCTOR
    er.entity_attributes(
        "DOCTOR",
        [
            ("Doctor_ID", {"pk": True}),
            "Specialty",
        ],
    )
    # Attributes for DEPARTMENT
    er.entity_attributes(
        "DEPARTMENT",
        [
            ("Dept_ID", {"pk": True}),
            "Name",
        ],
    )
    # Attribute on TREATS relationship
    er.attribute("Diagnosis", parent="TREATS")
    er.attribute("Visit_Date", parent="TREATS")

    # Connections
    er.connect("PATIENT", "TREATS", card_from="M", card_to="N", total_from=True)
    er.connect("DOCTOR", "TREATS", card_from="1", card_to="N")
    er.connect("DOCTOR", "WORKS_IN", card_from="N", card_to="1", total_from=True)
    er.connect("DEPARTMENT", "WORKS_IN", card_from="1", card_to="N")
    er.connect("PATIENT", "ISSUED_TO", card_from="1", card_to="N")
    er.connect("PRESCRIPTION", "ISSUED_TO", card_from="N", card_to="1", total_from=True)
    add_diagram(er)

    # ── Fig 5: State Machine ──────────────────────────────────────────────────
    en.section("State Machine")
    sm = ed.StateMachine(
        width=en.CW,
        height=270,
        theme=theme,
        caption="Fig 5: E-Commerce Order Lifecycle",
    )
    sm.state("pending", "Pending\nPayment", initial=True)
    sm.state("confirmed", "Confirmed")
    sm.state("picking", "Picking\n& Packing")
    sm.state("shipped", "Shipped")
    sm.state("out", "Out for\nDelivery")
    sm.state("delivered", "Delivered", accepting=True)
    sm.state("cancelled", "Cancelled", accepting=True)
    sm.state("refunded", "Refunded", accepting=True)

    sm.transition("pending", "confirmed", label="payment_ok")
    sm.transition("pending", "cancelled", label="timeout / cancel")
    sm.transition("confirmed", "picking", label="warehouse_assigned")
    sm.transition("confirmed", "cancelled", label="cancel_request")
    sm.transition("picking", "shipped", label="dispatched")
    sm.transition("shipped", "out", label="arrived_local_hub")
    sm.transition("out", "delivered", label="signed_off")
    sm.transition("out", "shipped", label="failed_delivery")
    sm.transition("delivered", "refunded", label="return_approved")
    sm.transition("cancelled", "refunded", label="refund_issued")
    add_diagram(sm)

    # =========================================================================
    en.part_box("Network & Infrastructure")
    # =========================================================================

    # ── Fig 6: Network Diagram (Tree Topology) ────────────────────────────────
    en.section("Network Diagram")
    net = ed.NetworkDiagram(
        width=en.CW,
        height=260,
        theme=theme,
        caption="Fig 6: Enterprise Campus Network (Tree Topology)",
    )
    net.tree_topology(
        parent_child_map={
            "core": ["dist_a", "dist_b"],
            "dist_a": ["access_1", "access_2"],
            "dist_b": ["access_3", "access_4"],
            "access_1": ["server_farm", "wifi_a"],
            "access_3": ["wifi_b", "printer_bay"],
        },
        node_labels={
            "core": "Core Router",
            "dist_a": "Distribution A",
            "dist_b": "Distribution B",
            "access_1": "Access SW-1",
            "access_2": "Access SW-2",
            "access_3": "Access SW-3",
            "access_4": "Access SW-4",
            "server_farm": "Server Farm",
            "wifi_a": "WiFi AP-A",
            "wifi_b": "WiFi AP-B",
            "printer_bay": "Print Server",
        },
        node_kinds={
            "core": "router",
            "dist_a": "switch",
            "dist_b": "switch",
            "access_1": "switch",
            "access_2": "switch",
            "access_3": "switch",
            "access_4": "switch",
            "server_farm": "server",
            "wifi_a": "wireless",
            "wifi_b": "wireless",
            "printer_bay": "printer",
        },
    )
    add_diagram(net)

    # ── Fig 7: Network — Star (DMZ) ───────────────────────────────────────────
    en.section("Network — Star Topology (DMZ)")
    dmz = ed.NetworkDiagram(
        width=en.CW,
        height=240,
        theme=theme,
        caption="Fig 7: DMZ Network — Firewall-Centric Star",
    )
    dmz.star_topology(
        center_id="fw",
        center_label="Next-Gen\nFirewall",
        center_kind="firewall",
        spoke_ids=["internet", "lb", "waf", "ids", "dmz_db"],
        spoke_labels=["Internet", "Load\nBalancer", "WAF", "IDS/IPS", "DMZ DB"],
        spoke_kind="generic",
    )
    # Override kinds for richer icons
    for nid, kind in [
        ("internet", "cloud"),
        ("lb", "load_balancer"),
        ("dmz_db", "database"),
    ]:
        dmz._node_index[nid].kind = kind  # type: ignore[assignment]
    add_diagram(dmz)

    # ── Fig 8: Web Deployment — Linear Chain ─────────────────────────────────
    en.section("Network — Web Deployment (Linear Chain)")
    web = ed.NetworkDiagram(
        width=en.CW,
        height=200,
        theme=theme,
        caption="Fig 8: Production Web Deployment",
    )
    web.node("internet", "Internet", kind="cloud")
    web.node("fw", "Firewall", kind="firewall", label_pos="left")
    web.node("lb", "Load Balancer", kind="load_balancer", label_pos="left")
    web.node("api1", "API Server 1", kind="server")
    web.node("api2", "API Server 2", kind="server")
    web.node("cache", "Redis Cache", kind="storage")
    web.node("db", "Primary DB", kind="database", label_pos="right")
    web.node("replica", "DB Replica", kind="database")

    web.link("internet", "fw")
    web.link("fw", "lb")
    web.link("lb", "api1")
    web.link("lb", "api2")
    web.link("api1", "cache")
    web.link("api2", "cache")
    web.link("api1", "db")
    web.link("api2", "db")
    web.link("db", "replica", label="replication")
    add_diagram(web)

    # =========================================================================
    en.part_box("Architecture & Cloud")
    # =========================================================================

    # ── Fig 9: Architecture Diagram ───────────────────────────────────────────
    en.section("Architecture Diagram")
    arch = ed.ArchitectureDiagram(
        width=en.CW,
        height=350,
        theme=theme,
        caption="Fig 9: Real-Time Analytics Platform",
        orientation="vertical",
    )
    arch.client("mobile", "Mobile App")
    arch.client("web", "Web App")
    arch.service("gateway", "API Gateway")
    arch.service("ingest", "Ingest Service")
    arch.service("stream", "Stream Processor")
    arch.service("notif", "Notification Svc")
    arch.database("kafka", "Kafka")
    arch.database("clickhouse", "ClickHouse")
    arch.database("pg", "PostgreSQL")
    arch.queue("queue", "Task Queue")

    arch.connect("mobile", "gateway", "HTTPS")
    arch.connect("web", "gateway", "HTTPS")
    arch.connect("gateway", "ingest", "gRPC")
    arch.connect("ingest", "kafka", "produce", label_pos="start")
    arch.connect("kafka", "stream", "consume")
    arch.connect("stream", "clickhouse", "batch write")
    arch.connect("gateway", "pg", "SQL", label_pos="end")
    arch.connect("stream", "queue", "events")
    arch.connect("queue", "notif", "push")
    add_diagram(arch)

    # ── Fig 10: C4 Container Diagram ─────────────────────────────────────────
    en.section("C4 Container Diagram")
    c4 = ed.C4ContainerDiagram(
        width=en.CW,
        height=260,
        theme=theme,
        caption="Fig 10: SaaS Platform — C4 Container View",
    )
    c4.system("idp", "Identity Provider (Auth0)")
    c4.system("cdn", "CDN / Edge Network")
    c4.container("spa", "React SPA", "TypeScript / Vite")
    c4.container("bff", "BFF API", "Node.js / Express")
    c4.container("core", "Core API", "Python / FastAPI")
    c4.container("worker", "Background Worker")
    c4.container("db", "PostgreSQL v16")
    c4.container("redis", "Redis v7")
    c4.container("storage", "Object Storage")

    c4.relate("spa", "bff", "API calls (HTTPS/JSON)")
    c4.relate("bff", "idp", "validate tokens (OIDC)")
    c4.relate("bff", "core", "delegates (gRPC)")
    c4.relate("core", "db", "reads/writes (SQL)")
    c4.relate("core", "redis", "cache & pub/sub")
    c4.relate("redis", "worker", "task dispatch")
    c4.relate("worker", "db", "writes (SQL)")
    c4.relate("worker", "storage", "upload artefacts")
    c4.relate("spa", "cdn", "static assets")
    add_diagram(c4)

    # ── Fig 11: AWS Diagram ────────────────────────────────────────────────────
    en.section("AWS Diagram")
    aws = ed.AWSDiagram(
        width=en.CW,
        height=300,
        theme=theme,
        caption="Fig 11: Serverless Media Processing Pipeline",
    )
    aws.s3("raw", "S3 Raw Bucket")
    aws.lambda_fn("trigger", "Trigger Lambda")
    aws.sqs("queue", "Processing Queue")
    aws.lambda_fn("process", "Processor Lambda")
    aws.ec2("transcode", "Transcode Fleet")
    aws.s3("cdn_bucket", "S3 CDN Bucket")
    aws.rds("meta", "RDS Metadata")

    aws.connect("raw", "trigger", "s3:PutObject")
    aws.connect("trigger", "queue", "enqueue job")
    aws.connect("queue", "process", "trigger")
    aws.connect("process", "transcode", "dispatch task")
    aws.connect("transcode", "cdn_bucket", "upload result")
    aws.connect("process", "meta", "write metadata")
    aws.connect("cdn_bucket", "meta", "register URL")
    add_diagram(aws)

    # =========================================================================
    en.part_box("Data & Schema")
    # =========================================================================

    # ── Fig 12: Schema Diagram ────────────────────────────────────────────────
    en.section("Database Schema")
    schema = ed.SchemaDiagram(
        width=en.CW,
        height=280,
        theme=theme,
        caption="Fig 12: Multi-Tenant SaaS Database Schema",
    )
    schema.table(
        "tenants",
        [
            ("id", "UUID", {"pk": True}),
            ("name", "VARCHAR(120)", {}),
            ("plan", "VARCHAR(32)", {}),
            ("created_at", "TIMESTAMPTZ", {}),
        ],
    )
    schema.table(
        "users",
        [
            ("id", "UUID", {"pk": True}),
            ("tenant_id", "UUID", {"fk": True}),
            ("email", "VARCHAR(255)", {"unique": True}),
            ("role", "VARCHAR(32)", {}),
            ("last_login", "TIMESTAMPTZ", {"nullable": True}),
        ],
    )
    schema.table(
        "projects",
        [
            ("id", "UUID", {"pk": True}),
            ("tenant_id", "UUID", {"fk": True}),
            ("owner_id", "UUID", {"fk": True}),
            ("name", "VARCHAR(120)", {}),
            ("archived", "BOOLEAN", {}),
        ],
    )
    schema.table(
        "tasks",
        [
            ("id", "UUID", {"pk": True}),
            ("project_id", "UUID", {"fk": True}),
            ("assignee_id", "UUID", {"fk": True, "nullable": True}),
            ("title", "VARCHAR(255)", {}),
            ("status", "VARCHAR(32)", {}),
            ("due_date", "DATE", {"nullable": True}),
        ],
    )
    schema.table(
        "audit_log",
        [
            ("id", "BIGSERIAL", {"pk": True}),
            ("tenant_id", "UUID", {"fk": True}),
            ("actor_id", "UUID", {"fk": True}),
            ("action", "VARCHAR(64)", {}),
            ("payload", "JSONB", {"nullable": True}),
            ("created_at", "TIMESTAMPTZ", {}),
        ],
    )

    schema.relation("users", "tenant_id", "tenants", "id")
    schema.relation("projects", "tenant_id", "tenants", "id")
    schema.relation("projects", "owner_id", "users", "id")
    schema.relation("tasks", "project_id", "projects", "id")
    schema.relation("tasks", "assignee_id", "users", "id")
    schema.relation("audit_log", "tenant_id", "tenants", "id")
    schema.relation("audit_log", "actor_id", "users", "id")
    add_diagram(schema)

    # =========================================================================
    en.part_box("Timing & Version Control")
    # =========================================================================

    # ── Fig 13: Timing Diagram ────────────────────────────────────────────────
    en.section("Timing Diagram")
    td = ed.TimingDiagram(
        width=en.CW,
        height=240,
        theme=theme,
        caption="Fig 13: Full-Duplex SPI Bus — 4-Signal Timing",
    )
    td.clock("SCLK", period=20.0, cycles=10)
    td.signal(
        "CS_N",
        transitions=[
            (0, 1),
            (10, 0),
            (210, 1),
        ],
    )
    td.signal(
        "MOSI",
        transitions=[
            (0, 0),
            (10, 1),
            (30, 0),
            (50, 1),
            (70, 1),
            (90, 0),
            (110, 1),
            (130, 0),
            (150, 1),
            (170, 0),
            (190, 1),
            (210, 0),
        ],
    )
    td.signal(
        "MISO",
        transitions=[
            (0, 0),
            (20, 1),
            (40, 0),
            (60, 0),
            (80, 1),
            (100, 1),
            (120, 0),
            (140, 1),
            (160, 0),
            (180, 1),
            (200, 0),
            (210, 0),
        ],
    )
    add_diagram(td)

    # ── Fig 14: Git Branch Flow ───────────────────────────────────────────────
    en.section("Git Diagram")
    git = ed.GitDiagram(
        width=en.CW,
        height=270,
        theme=theme,
        caption="Fig 14: Feature-Branch Git Flow with Hotfix",
    )
    git.commit("main", "initial")
    git.branch("main", "develop")
    git.commit("develop", "setup CI")
    git.branch("develop", "feature/auth")
    git.commit("feature/auth", "add login")
    git.commit("feature/auth", "add OAuth")
    git.commit("develop", "fix linting")
    git.merge("feature/auth", "develop", "merge auth")
    git.branch("develop", "feature/payments")
    git.commit("feature/payments", "stripe integration")
    git.branch("main", "hotfix/xss")
    git.commit("hotfix/xss", "sanitise inputs")
    git.merge("hotfix/xss", "main", "hotfix merge")
    git.commit("main", "v1.0.1")
    git.merge("hotfix/xss", "develop", "back-merge")
    git.commit("feature/payments", "add webhooks")
    git.merge("feature/payments", "develop", "merge payments")
    git.merge("develop", "main", "release")
    git.commit("main", "v1.1.0 release")
    add_diagram(git)

    # ── Fig 15: Layered Stack ─────────────────────────────────────────────────
    en.section("Layered Stack")
    stack = ed.LayeredStack(
        width=en.CW,
        height=280,
        theme=theme,
        caption="Fig 15: Modern Full-Stack Application Architecture",
    )
    stack.layer(
        "Presentation Layer", sublabel="React SPA · Next.js SSR · Mobile (React Native)"
    )
    stack.layer(
        "API Gateway Layer", sublabel="Rate limiting · Auth (JWT/OIDC) · Load Balancing"
    )
    stack.layer("Application Services", sublabel="FastAPI · gRPC · GraphQL · WebSocket")
    stack.layer(
        "Domain / Business Logic", sublabel="DDD Aggregates · CQRS · Event Sourcing"
    )
    stack.layer("Data Access Layer", sublabel="SQLAlchemy ORM · Redis Client · S3 SDK")
    stack.layer("Infrastructure", sublabel="PostgreSQL 16 · Redis 7 · Kafka · S3 / CDN")
    stack.layer(
        "Observability", sublabel="OpenTelemetry · Prometheus · Grafana · Sentry"
    )
    add_diagram(stack)

    en.build_doc("demo_diagrams.pdf")
    print("Generated: demo_diagrams.pdf")


if __name__ == "__main__":
    main()
