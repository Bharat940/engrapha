# Diagram: AWS Cloud

AWS diagrams render vector-native AWS resource icons on top of the standard ArchitectureDiagram layout. All auto-layout and orthogonal routing from `ArchitectureDiagram` is inherited.

## Minimal example

```python
import engrapha_notes as en
import engrapha_diagrams as ed

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

## Node types

| Method | Kind | Visual |
| ------ | ---- | ------ |
| `ec2(name, label)` | compute/server | server blade chassis |
| `rds(name, label)` | database | multi-disc cylinder |
| `s3(name, label)` | storage | trapezoidal bucket |
| `lambda_fn(name, label)` | function | lambda (λ) symbol |
| `sqs(name, label)` | queue | stadium with slot markers |

Use `connect(...)` inherited from `ArchitectureDiagram` for routed edges.

## Orientation

Pass `orientation="vertical"` to stack tiers bottom-to-top instead of the default horizontal left-to-right.

## Auto layout

Nodes are auto-positioned when added without x, y. Only specify coordinates if needed.

## Next

- [Architecture](architecture.md)
- [C4 Container](c4.md)

