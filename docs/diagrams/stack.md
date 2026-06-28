# Diagram: Layered Stack

LayeredStack draws horizontal layers and dividers. Ideal for OSI/TCP-IP stacks, memory hierarchies, and any stacked software structure.

## Minimal example

```python
import engrapha_notes as en
import engrapha_diagrams as ed

stack = ed.LayeredStack(
    width=300, height=260,
    caption="Fig 12: OSI Reference Model",
)

stack.layer("Layer 7: Application",  sublabel="HTTP, FTP, SMTP, DNS")
stack.layer("Layer 6: Presentation", sublabel="SSL/TLS, JPEG, MPEG")
stack.layer("Layer 5: Session",      sublabel="NetBIOS, RPC")
stack.divider()                     # thicker separator after Session

stack.layer("Layer 4: Transport",  sublabel="TCP, UDP")
stack.layer("Layer 3: Network",    sublabel="IP, ICMP, ARP")
stack.layer("Layer 2: Data Link",  sublabel="Ethernet, PPP, HDLC")
stack.layer("Layer 1: Physical",   sublabel="Cables, Fiber, Radio")

en.add(stack.as_flowable())
```

## Layer colors

If you do not specify `fill`, the theme cycles through `stack_colors`:

```python
stack.layer("Custom", sublabel="...", fill="#22d3ee")
stack.layer("Other",  sublabel="...", stroke="#fbbf24")
```

## Dividers

`divider()` draws a thicker separator after the most recently added layer:

```python
stack.layer("Transport")
stack.divider()     # ← thicker rule here
stack.layer("Network")
```

## Scale behavior

If the total layer height exceeds the canvas minus margins, stacking scales uniformly to fit.

## Parameters reference

| Parameter | Default | Purpose |
| --------- | ------- | ------- |
| `width` | depends | Canvas width |
| `height` | depends | Canvas height |
| `theme` | — | Color mapping |
| `margin` | `12.0` | Horizontal padding |
| `layer_h` | `30.0` | Default layer height (scales if needed) |
| `corner_radius` | `5.0` | Rounded top corners |

## Next

- [Timing](timing.md)
- [Git](git.md)

