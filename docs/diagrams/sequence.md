# Diagram: Sequence

A UML sequence diagram maps ordered message arrows over lifelines. Each actor is placed left-to-right at the top. A dashed lifeline drops down. Activation bars, activity dividers, and notes can be layered in.

## Minimal example

```python
import engrapha_notes as en
import engrapha_diagrams as ed

seq = ed.SequenceDiagram(width=400, height=220, caption="Fig 2: TCP Handshake")

seq.actor("cl", "Client")
seq.actor("srv", "Server")

seq.message("cl", "srv", "SYN")
seq.activate("srv")
seq.divider("Internal processing")
seq.message("srv", "cl", "SYN-ACK", arrow="dashed")
seq.deactivate("srv")

en.add(seq.as_flowable())
en.build_doc("seq.pdf")
```

## Arrow styles

```python
seq.message(src, dst, "data", arrow="solid")          # default
seq.message(src, dst, "data", arrow="dashed")
seq.message(src, dst, "data", arrow="solid_open")     # open triangle
seq.message(src, dst, "data", arrow="dashed_open")    # open, dashed
```

## Self-messages

`from_id == to_id` renders as a small loop above the lifeline:

```python
seq.message("srv", "srv", "retry(3)")
```

## Activation bars

Wrap activity in `activate / deactivate`:

```python
seq.activate("db")
seq.message("app", "db", "SELECT ...")
seq.deactivate("db")
```

## Divider

Insert a time-divider label across the width of the canvas:

```python
seq.divider("— Authentication —")
```


## Auto layout

Nodes are evenly spaced automatically. Override x, y only when you need manual control. When left as `None`, each actor is evenly distributed:

```python
seq.actor("a", "Alpha")
seq.actor("b", "Beta")
seq.actor("c", "Gamma")
```

If you want multi-column alignment, just specify explicit coordinates:

```python
seq.actor("a", "Alpha", x=120, y=200)
seq.actor("b", "Beta", x=280, y=200)
```

## Parameters reference

| Parameter | Default | Purpose |
| -------- | ------ | ------- |
| `width` | `400` | Canvas width |
| `height` | `200` | Canvas height |
| `theme` | — | Vector theme |
| `row_height` | auto | Vertical spacing |
| `actor_margin_top` | `20` | Top margin |
| `margin` | `120` | Side margins |
| `arrow` | `"solid"` | `solid`, `dashed`, `solid_open`, `dashed_open` |

## Next

- [ER and Schema](er.md)
- [Architecture](architecture.md)

