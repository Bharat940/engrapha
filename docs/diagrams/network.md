# Diagram: Network

Network topology diagrams render hosts, switches, routers, clouds, firewalls, databases, wireless points, and more. Presets for `bus`, `star`, `ring`, `mesh`, and `tree` topologies are included.

## Minimal example

```python
import paperforge_notes as pn
import paperforge_diagrams as pd

net = pd.NetworkDiagram(width=500, height=220, caption="Fig 8: LAN")

net.node("inet",  "Internet",   x=50,  y=110, kind="cloud")
net.node("fw",    "Firewall",   x=160, y=110, kind="firewall")
net.node("sw",    "Core Switch",x=270, y=110, kind="switch")
net.node("srv",   "Web Server", x=380, y=150, kind="server")
net.node("db",    "Database",   x=380, y=70,  kind="database")

net.link("inet", "fw")
net.link("fw",   "sw")
net.link("sw",   "srv")
net.link("sw",   "db")

pn.add(net.as_flowable())
```

## Node kinds

| Kind | Shape |
| ---- | ----- |
| `host` / `server` / `firewall` / `database` / `load_balancer` / `storage` / `custom` | Rectangle |
| `router` | Hexagon |
| `switch` | Octagon |
| `hub` / `generic` | Circle |
| `cloud` | Cloud (path) |
| `wireless` | Antenna |
| `printer` | Printer |
| `mobile` | Phone |
| `text` | (no shape, label only) |

## Topology presets

```python
net.star_topology(
    center_id="sw",
    center_label="Core Switch",
    spoke_ids=["h1", "h2", "h3"],
)

net.bus_topology(node_ids=["n1", "n2", "n3"])
net.ring_topology(node_ids=["r1", "r2", "r3", "r4"])
net.mesh_topology(node_ids=["m1", "m2", "m3", "m4"])
net.tree_topology(parent_child_map={"root": ["a", "b"]})
```

## Labels

Set `label_pos="auto"` (default) for smart placement above or below. Override with:

```python
net.node("sw", "Label", label_pos="right")
```

## Links

```python
net.link("sw", "srv", label="Gi0/1", bidirectional=True)
```

Bidirectional links draw a single line. `bidirectional=False` adds an arrowhead.

## Custom node drawers

```python
def my_drawer(diagram, cx, cy, w, h, fill, stroke):
    diagram._add(diagram.S.rounded_rect(
        cx - w/2, cy - h/2, w, h,
        rx=3, fill=fill, stroke=stroke
    ))

net.node("id", "Label", kind="custom", custom_draw=my_drawer)
```

## Next

- [Architecture](architecture.md)
- [Stack](stack.md)
