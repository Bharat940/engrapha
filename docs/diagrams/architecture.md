# Diagrams: Architecture, C4, and AWS

Three closely related diagram types: `ArchitectureDiagram`, `C4ContainerDiagram`, and `AWSDiagram`. All share the same auto-layout engine and orthogonal-routing connections.

## ArchitectureDiagram

Draws 4-tier topology: clients, services, databases, and queues.

```python
import engrapha_notes as en
import engrapha_diagrams as ed

arch = ed.ArchitectureDiagram(
    width=450, height=220,
    caption="Fig 9: Web App Architecture",
    orientation="horizontal",  # "vertical"
)

arch.client("web", "Web Client")
arch.service("api", "Gateway API")
arch.service("auth", "Auth Service")
arch.database("db", "PostgreSQL")
arch.queue("q", "Job Queue")

arch.connect("web",  "api",  "HTTPS")
arch.connect("api",  "auth", "gRPC")
arch.connect("api",  "db",   "TCP/5432")
arch.connect("api",  "q",    "AMQP")
arch.connect("auth", "db",   "TCP/5432")

en.add(arch.as_flowable())
en.build_doc("arch.pdf")
```

### Orientation

With `orientation="vertical"` the tiers stack bottom-to-top. Clients at the bottom, databases at the top.

## C4ContainerDiagram

System and Container nodes arranged on a grid with relationship lines:

```python
c4 = ed.C4ContainerDiagram(
    width=420, height=220,
    caption="Fig 10: C4 Container View",
)

c4.system("user", "Customer")
c4.container("spa",  "SPA (React)", "Provides UI")
c4.container("api",  "API (Go)",    "Business logic")
c4.container("db",   "Postgres",    "Order data")

c4.relate("user", "spa", "Uses")
c4.relate("spa", "api", "Makes API calls")
c4.relate("api", "db", "Reads / Writes")

en.add(c4.as_flowable())
```

Systems render in darker surface tones; containers render with lighter backgrounds.

## AWSDiagram

AWS-specific vector icons on top of the ArchitectureDiagram layout:

```python
aws = ed.AWSDiagram(
    width=450, height=220,
    caption="Fig 11: AWS Stack",
    orientation="horizontal",
)

aws.ec2("app",    "EC2 App")
aws.rds("db",     "RDS PostgreSQL")
aws.s3("assets",  "S3 Storage")
aws.lambda_fn("fn", "Handler")
aws.sqs("queue",  "Job Queue")

aws.connect("app", "db",     "SQL Connection")
aws.connect("app", "assets", "Uploads")
aws.connect("app", "fn",     "Invoke")
aws.connect("app", "queue",  "Events")

en.add(aws.as_flowable())
```

### Node types

| Method | Kind | Visual |
| ------ | ---- | ------ |
| `ec2(name, label)` | compute/server | server blade |
| `rds(name, label)` | database | cylinder |
| `s3(name, label)` | storage | trapezoidal bucket |
| `lambda_fn(name, label)` | function | lambda (λ) symbol |
| `sqs(name, label)` | queue | stadium with slot markers |

## Auto layout

All three handle auto-positioning when nodes are added without x, y coordinates. Only specify coordinates if the auto-layout is unsatisfactory.

## Next

- [C4 Container](c4.md)
- [AWS Cloud](cloud.md)

