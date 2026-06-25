"""
shapes.py -- Low-level vector primitive builders for paperforge_diagrams.

All functions return reportlab.graphics.shapes objects (or Groups of them).
None of these functions have side effects; they are pure builders.

Known limitation: reportlab String does not support multi-line text natively.
Use multiline_label() which stacks individual String objects.

Known limitation: arrowheads on Line are not natively supported.
Use arrow_line() which composes a Line with a Polygon triangle tip.
"""

from __future__ import annotations

import math
from typing import Literal, cast

from reportlab.graphics.shapes import (
    Circle,
    Ellipse,
    Group,
    Line,
    Path,
    Polygon,
    Rect,
    String,
)
from reportlab.lib.colors import Color, HexColor
from reportlab.pdfbase.pdfmetrics import stringWidth

# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------


def _hex(color: str | Color | None) -> Color | None:
    if color is None:
        return None
    if isinstance(color, Color):
        return color
    if isinstance(color, str):
        if color.lower() == "none":
            return None
        return HexColor(color)
    return color


def _angle_point(
    cx: float, cy: float, r: float, angle_deg: float
) -> tuple[float, float]:
    """Return the point on a circle at the given angle (degrees, 0 = right)."""
    rad = math.radians(angle_deg)
    return cx + r * math.cos(rad), cy + r * math.sin(rad)


def _normalize(dx: float, dy: float) -> tuple[float, float]:
    """Return unit vector for (dx, dy), or (1, 0) if zero length."""
    length = math.hypot(dx, dy)
    if length < 1e-9:
        return 1.0, 0.0
    return dx / length, dy / length


# ---------------------------------------------------------------------------
# Basic shapes
# ---------------------------------------------------------------------------


def rounded_rect(
    x: float,
    y: float,
    w: float,
    h: float,
    rx: float = 4.0,
    fill: str = "#161b22",
    stroke: str = "#38bdf8",
    stroke_width: float = 1.5,
) -> Rect:
    """Axis-aligned rectangle with optional rounded corners."""
    r = Rect(x, y, w, h)
    r.fillColor = _hex(fill)
    r.strokeColor = _hex(stroke)
    r.strokeWidth = stroke_width
    r.rx = rx
    r.ry = rx
    return r


def plain_rect(
    x: float,
    y: float,
    w: float,
    h: float,
    fill: str = "#161b22",
    stroke: str = "#38bdf8",
    stroke_width: float = 1.5,
) -> Rect:
    """Sharp-cornered rectangle."""
    r = Rect(x, y, w, h)
    r.fillColor = _hex(fill)
    r.strokeColor = _hex(stroke)
    r.strokeWidth = stroke_width
    return r


def diamond(
    cx: float,
    cy: float,
    w: float,
    h: float,
    fill: str = "#1e1040",
    stroke: str = "#a855f7",
    stroke_width: float = 1.8,
) -> Polygon:
    """Four-point diamond centered at (cx, cy)."""
    half_w = w / 2
    half_h = h / 2
    points = [
        cx,
        cy + half_h,
        cx + half_w,
        cy,
        cx,
        cy - half_h,
        cx - half_w,
        cy,
    ]
    p = Polygon(points)
    p.fillColor = _hex(fill)
    p.strokeColor = _hex(stroke)
    p.strokeWidth = stroke_width
    return p


def polygon(
    points: list[float],
    fill: str = "#1e293b",
    stroke: str = "#475569",
    stroke_width: float = 1.5,
) -> Polygon:
    """Polygon with arbitrary points list [x1, y1, x2, y2, ...]."""
    p = Polygon(points)
    p.fillColor = _hex(fill)
    p.strokeColor = _hex(stroke)
    p.strokeWidth = stroke_width
    return p


def oval(
    cx: float,
    cy: float,
    rx: float,
    ry: float,
    fill: str = "#1e293b",
    stroke: str = "#475569",
    stroke_width: float = 1.5,
    dashed: bool = False,
) -> Ellipse:
    """Ellipse centered at (cx, cy) with semi-axes rx, ry."""
    e = Ellipse(cx, cy, rx, ry)
    e.fillColor = _hex(fill)
    e.strokeColor = _hex(stroke)
    e.strokeWidth = stroke_width
    if dashed:
        e.strokeDashArray = [4, 3]
    return e


ellipse = oval


def circle(
    cx: float,
    cy: float,
    r: float,
    fill: str = "#161b22",
    stroke: str = "#38bdf8",
    stroke_width: float = 1.5,
) -> Circle:
    """Circle centered at (cx, cy) with radius r."""
    c = Circle(cx, cy, r)
    c.fillColor = _hex(fill)
    c.strokeColor = _hex(stroke)
    c.strokeWidth = stroke_width
    return c


def double_oval(
    cx: float,
    cy: float,
    rx: float,
    ry: float,
    fill: str = "#1e1a40",
    stroke: str = "#818cf8",
    stroke_width: float = 1.3,
    gap: float = 2.5,
) -> Group:
    """Two concentric ellipses -- represents a multivalued attribute."""
    outer = oval(cx, cy, rx, ry, fill=fill, stroke=stroke, stroke_width=stroke_width)
    inner = oval(cx, cy, rx - gap, ry - gap, fill=fill, stroke=stroke, stroke_width=0.9)
    g = Group()
    g.add(outer)
    g.add(inner)
    return g


def double_circle(
    cx: float,
    cy: float,
    r: float,
    fill: str = "#0b2848",
    stroke: str = "#34d399",
    stroke_width: float = 1.5,
    gap: float = 2.5,
) -> Group:
    """Two concentric circles -- represents an accepting state."""
    outer = circle(cx, cy, r, fill=fill, stroke=stroke, stroke_width=stroke_width)
    inner = circle(cx, cy, r - gap, fill=fill, stroke=stroke, stroke_width=stroke_width)
    g = Group()
    g.add(outer)
    g.add(inner)
    return g


def stadium(
    x: float,
    y: float,
    w: float,
    h: float,
    fill: str = "#042a1a",
    stroke: str = "#34d399",
    stroke_width: float = 1.5,
) -> Rect:
    """Pill / stadium shape (rounded rect with radius = h/2). Used for terminal nodes."""
    return rounded_rect(
        x, y, w, h, rx=h / 2, fill=fill, stroke=stroke, stroke_width=stroke_width
    )


def hexagon(
    cx: float,
    cy: float,
    r: float,
    fill: str = "#0b2848",
    stroke: str = "#38bdf8",
    stroke_width: float = 1.5,
) -> Polygon:
    """Regular hexagon centered at (cx, cy). Used for router nodes."""
    points: list[float] = []
    for i in range(6):
        px, py = _angle_point(cx, cy, r, 60 * i + 30)
        points += [px, py]
    p = Polygon(points)
    p.fillColor = _hex(fill)
    p.strokeColor = _hex(stroke)
    p.strokeWidth = stroke_width
    return p


def octagon(
    cx: float,
    cy: float,
    r: float,
    fill: str = "#0b2848",
    stroke: str = "#38bdf8",
    stroke_width: float = 1.5,
) -> Polygon:
    """Regular octagon centered at (cx, cy). Used for switch nodes."""
    points: list[float] = []
    for i in range(8):
        px, py = _angle_point(cx, cy, r, 45 * i + 22.5)
        points += [px, py]
    p = Polygon(points)
    p.fillColor = _hex(fill)
    p.strokeColor = _hex(stroke)
    p.strokeWidth = stroke_width
    return p


def parallelogram(
    x: float,
    y: float,
    w: float,
    h: float,
    skew: float = 10.0,
    fill: str = "#1c1917",
    stroke: str = "#fb923c",
    stroke_width: float = 1.5,
) -> Polygon:
    """Parallelogram shifted right by skew at the top. Used for I/O boxes."""
    points = [
        x + skew,
        y + h,
        x + w + skew,
        y + h,
        x + w,
        y,
        x,
        y,
    ]
    p = Polygon(points)
    p.fillColor = _hex(fill)
    p.strokeColor = _hex(stroke)
    p.strokeWidth = stroke_width
    return p


def cylinder(
    x: float,
    y: float,
    w: float,
    h: float,
    fill: str = "#0b2848",
    stroke: str = "#38bdf8",
    stroke_width: float = 1.5,
) -> Group:
    """
    Cylinder shape for database nodes.
    Drawn as a rectangle body with an ellipse top and bottom.
    """
    ry = h * 0.12
    rx = w / 2
    cx = x + rx
    body = plain_rect(
        x, y + ry, w, h - ry * 2, fill=fill, stroke=stroke, stroke_width=stroke_width
    )
    top = oval(
        cx, y + h - ry, rx, ry, fill=fill, stroke=stroke, stroke_width=stroke_width
    )
    bottom = oval(
        cx, y + ry, rx, ry, fill=fill, stroke=stroke, stroke_width=stroke_width
    )
    g = Group()
    g.add(body)
    g.add(bottom)
    g.add(top)
    return g


def cloud(
    cx: float,
    cy: float,
    w: float,
    h: float,
    fill: str = "#161b22",
    stroke: str = "#38bdf8",
    stroke_width: float = 1.3,
) -> Group:
    """
    Unified cloud shape using a Path with bezier curves.
    Used for internet/cloud nodes in network diagrams.
    """
    rx = w / 2.0
    ry = h / 2.0

    p = Path()
    p.fillColor = _hex(fill)
    p.strokeColor = _hex(stroke)
    p.strokeWidth = stroke_width

    sx = cx - rx * 0.6
    sy = cy - ry * 0.4
    p.moveTo(sx, sy)

    # Flat bottom line
    p.lineTo(cx + rx * 0.6, cy - ry * 0.4)

    # Bottom-right bubble
    p.curveTo(
        cx + rx * 0.9, cy - ry * 0.4, cx + rx, cy - ry * 0.2, cx + rx, cy + ry * 0.05
    )

    # Top-right bubble
    p.curveTo(
        cx + rx * 1.05,
        cy + ry * 0.4,
        cx + rx * 0.6,
        cy + ry * 0.7,
        cx + rx * 0.3,
        cy + ry * 0.5,
    )

    # Top center bubble
    p.curveTo(
        cx + rx * 0.1,
        cy + ry * 0.9,
        cx - rx * 0.1,
        cy + ry * 0.9,
        cx - rx * 0.3,
        cy + ry * 0.5,
    )

    # Top-left bubble
    p.curveTo(
        cx - rx * 0.6,
        cy + ry * 0.7,
        cx - rx * 1.05,
        cy + ry * 0.4,
        cx - rx,
        cy + ry * 0.05,
    )

    # Bottom-left bubble
    p.curveTo(cx - rx, cy - ry * 0.2, cx - rx * 0.9, cy - ry * 0.4, sx, sy)

    p.closePath()

    g = Group()
    g.add(p)
    return g


# ---------------------------------------------------------------------------
# Lines and arrows
# ---------------------------------------------------------------------------


def solid_line(
    x1: float,
    y1: float,
    x2: float,
    y2: float,
    color: str = "#334155",
    width: float = 1.5,
) -> Line:
    """Simple solid line segment."""
    ln = Line(x1, y1, x2, y2)
    ln.strokeColor = _hex(color)
    ln.strokeWidth = width
    return ln


def dashed_line(
    x1: float,
    y1: float,
    x2: float,
    y2: float,
    color: str = "#475569",
    width: float = 1.2,
    dash: tuple[float, float] = (4.0, 3.0),
) -> Line:
    """Dashed line segment."""
    ln = Line(x1, y1, x2, y2)
    ln.strokeColor = _hex(color)
    ln.strokeWidth = width
    ln.strokeDashArray = list(dash)
    return ln


def double_line(
    x1: float,
    y1: float,
    x2: float,
    y2: float,
    color: str = "#38bdf8",
    width: float = 1.4,
    gap: float = 2.5,
) -> Group:
    """
    Two parallel lines representing total participation in ER diagrams.
    Lines are offset perpendicularly by gap/2 on each side.
    """
    dx, dy = x2 - x1, y2 - y1
    ux, uy = _normalize(-dy, dx)  # perpendicular unit vector
    off = gap / 2
    l1 = solid_line(
        x1 + ux * off,
        y1 + uy * off,
        x2 + ux * off,
        y2 + uy * off,
        color=color,
        width=width,
    )
    l2 = solid_line(
        x1 - ux * off,
        y1 - uy * off,
        x2 - ux * off,
        y2 - uy * off,
        color=color,
        width=width,
    )
    g = Group()
    g.add(l1)
    g.add(l2)
    return g


def _arrowhead_polygon(
    tip_x: float,
    tip_y: float,
    dx: float,
    dy: float,
    size: float,
    filled: bool,
    color: str,
) -> Polygon:
    """
    Filled or open arrowhead triangle at (tip_x, tip_y) pointing in (dx, dy) direction.
    """
    ux, uy = _normalize(dx, dy)
    px, py = -uy, ux  # perpendicular
    half = size * 0.35
    base_x = tip_x - ux * size
    base_y = tip_y - uy * size
    points = [
        tip_x,
        tip_y,
        base_x + px * half,
        base_y + py * half,
        base_x - px * half,
        base_y - py * half,
    ]
    poly = Polygon(points)
    poly.strokeColor = _hex(color)
    poly.strokeWidth = 1.0
    poly.fillColor = _hex(color) if filled else None
    return poly


def arrow_line(
    x1: float,
    y1: float,
    x2: float,
    y2: float,
    color: str = "#334155",
    width: float = 1.4,
    arrow_end: bool = True,
    arrow_start: bool = False,
    dashed: bool = False,
    filled_head: bool = True,
    arrow_size: float = 8.0,
) -> Group:
    """
    Line with optional arrowheads. Arrowhead is a filled or open triangle polygon.
    Line is shortened to avoid bleeding inside arrowheads.
    """
    dx, dy = x2 - x1, y2 - y1
    dist = math.hypot(dx, dy)
    ux, uy = _normalize(dx, dy)

    lx1, ly1 = x1, y1
    lx2, ly2 = x2, y2

    required_space = (arrow_size if arrow_start else 0.0) + (
        arrow_size if arrow_end else 0.0
    )
    if dist > required_space:
        if arrow_start:
            lx1 += ux * arrow_size
            ly1 += uy * arrow_size
        if arrow_end:
            lx2 -= ux * arrow_size
            ly2 -= uy * arrow_size
    else:
        lx1, ly1 = (x1 + x2) / 2, (y1 + y2) / 2
        lx2, ly2 = lx1, ly1

    g = Group()
    if dashed:
        ln = dashed_line(lx1, ly1, lx2, ly2, color=color, width=width)
    else:
        ln = solid_line(lx1, ly1, lx2, ly2, color=color, width=width)
    g.add(ln)
    if arrow_end:
        g.add(_arrowhead_polygon(x2, y2, dx, dy, arrow_size, filled_head, color))
    if arrow_start:
        g.add(_arrowhead_polygon(x1, y1, -dx, -dy, arrow_size, filled_head, color))
    return g


def open_diamond_head(
    tip_x: float,
    tip_y: float,
    dx: float,
    dy: float,
    size: float,
    color: str,
) -> Polygon:
    """Open diamond arrowhead for UML aggregation."""
    ux, uy = _normalize(dx, dy)
    px, py = -uy, ux
    half = size * 0.30
    mid_x = tip_x - ux * size
    mid_y = tip_y - uy * size
    back_x = tip_x - ux * size * 2
    back_y = tip_y - uy * size * 2
    points = [
        tip_x,
        tip_y,
        mid_x + px * half,
        mid_y + py * half,
        back_x,
        back_y,
        mid_x - px * half,
        mid_y - py * half,
    ]
    poly = Polygon(points)
    poly.strokeColor = _hex(color)
    poly.strokeWidth = 1.1
    poly.fillColor = None
    return poly


def filled_diamond_head(
    tip_x: float,
    tip_y: float,
    dx: float,
    dy: float,
    size: float,
    color: str,
) -> Polygon:
    """Filled diamond arrowhead for UML composition."""
    ux, uy = _normalize(dx, dy)
    px, py = -uy, ux
    half = size * 0.30
    mid_x = tip_x - ux * size
    mid_y = tip_y - uy * size
    back_x = tip_x - ux * size * 2
    back_y = tip_y - uy * size * 2
    points = [
        tip_x,
        tip_y,
        mid_x + px * half,
        mid_y + py * half,
        back_x,
        back_y,
        mid_x - px * half,
        mid_y - py * half,
    ]
    poly = Polygon(points)
    poly.strokeColor = _hex(color)
    poly.strokeWidth = 1.1
    poly.fillColor = _hex(color)
    return poly


def self_loop_path(
    cx: float,
    cy: float,
    r: float,
    offset: float = 20.0,
    color: str = "#334155",
    width: float = 1.4,
) -> Path:
    """
    Cubic bezier self-loop above a circle state node.
    Returns a Path object.
    """
    sx, sy = cx, cy + r  # start (top of circle)
    ex, ey = cx + r * 0.5, cy + r  # end (upper-right of circle)
    c1x = sx - offset
    c1y = sy + offset * 1.5
    c2x = ex + offset
    c2y = ey + offset * 1.5
    p = Path()
    p.moveTo(sx, sy)
    p.curveTo(c1x, c1y, c2x, c2y, ex, ey)
    p.fillColor = None
    p.strokeColor = _hex(color)
    p.strokeWidth = width
    return p


# ---------------------------------------------------------------------------
# Text labels
# ---------------------------------------------------------------------------


def label(
    x: float,
    y: float,
    text: str,
    font: str = "Helvetica",
    size: float = 9.0,
    color: str = "#e2e8f0",
    anchor: Literal["start", "middle", "end"] = "middle",
) -> String:
    """Single-line text string."""
    s = String(x, y, text)
    s.fontName = font
    s.fontSize = size
    s.fillColor = _hex(color)
    s.textAnchor = anchor
    return s


def text_width(text: str, font: str = "Helvetica", size: float = 9.0) -> float:
    """Measure a label using ReportLab's active font metrics."""
    return cast(float, stringWidth(text, font, size))


def wrap_text(
    text: str,
    max_width: float,
    font: str = "Helvetica",
    size: float = 9.0,
) -> list[str]:
    """Wrap label text to a measured width, including long unbroken tokens."""
    if max_width <= 0:
        raise ValueError("max_width must be positive")

    lines: list[str] = []
    for paragraph in text.splitlines() or [""]:
        words = paragraph.split()
        if not words:
            lines.append("")
            continue

        current = ""
        for word in words:
            candidate = f"{current} {word}".strip()
            if current and text_width(candidate, font, size) <= max_width:
                current = candidate
                continue
            if current:
                lines.append(current)
                current = ""
            if text_width(word, font, size) <= max_width:
                current = word
                continue

            fragment = ""
            for char in word:
                candidate = fragment + char
                if fragment and text_width(candidate, font, size) > max_width:
                    lines.append(fragment)
                    fragment = char
                else:
                    fragment = candidate
            current = fragment

        if current:
            lines.append(current)
    return lines or [""]


def multiline_label(
    x: float,
    y: float,
    lines: list[str],
    font: str = "Helvetica",
    size: float = 9.0,
    color: str = "#e2e8f0",
    line_height: float = 11.0,
    anchor: Literal["start", "middle", "end"] = "middle",
) -> Group:
    """
    Stack of String objects simulating multi-line text.
    Lines are drawn top-to-bottom; y is the baseline of the topmost line.
    """
    g = Group()
    for i, line in enumerate(lines):
        s = label(
            x,
            y - i * line_height,
            line,
            font=font,
            size=size,
            color=color,
            anchor=anchor,
        )
        g.add(s)
    return g


def centered_wrapped_label(
    x: float,
    y: float,
    text: str,
    max_width: float,
    font: str = "Helvetica",
    size: float = 9.0,
    color: str = "#e2e8f0",
    line_height: float | None = None,
    anchor: Literal["start", "middle", "end"] = "middle",
) -> Group:
    """Draw measured wrapped text vertically centered around the supplied point."""
    lines = wrap_text(text, max_width, font=font, size=size)
    lh = line_height if line_height is not None else size * 1.2
    first_baseline = y + (len(lines) - 1) * lh / 2.0 - size * 0.35
    return multiline_label(
        x,
        first_baseline,
        lines,
        font=font,
        size=size,
        color=color,
        line_height=lh,
        anchor=anchor,
    )


def pill_label(
    x: float,
    y: float,
    text: str,
    font: str = "Helvetica-Oblique",
    size: float = 7.0,
    text_color: str = "#e2e8f0",
    bg_color: str = "#1e293b",
    border_color: str = "#38bdf8",
    pad_x: float = 3.5,
    pad_y: float = 2.0,
) -> Group:
    """
    Text label with a rounded-rect background pill.
    Designed for edge/link labels so they are clearly visible
    regardless of surrounding line colors or diagram backgrounds.
    Supports multi-line text strings separated by newlines.
    """
    lines = text.splitlines() or [""]
    line_widths = [text_width(line, font, size) for line in lines]
    tw = max(line_widths)
    half_w = tw / 2.0 + pad_x

    lh = size * 1.2
    pill_h = size + (len(lines) - 1) * lh + pad_y * 2
    rx = (size + pad_y * 2) / 2.0

    bg = rounded_rect(
        x - half_w,
        y - size * 0.2 - pad_y - (len(lines) - 1) * lh / 2.0,
        half_w * 2,
        pill_h,
        rx=rx,
        fill=bg_color,
        stroke=border_color,
        stroke_width=0.7,
    )

    g = Group()
    g.add(bg)

    first_baseline = y + (len(lines) - 1) * lh / 2.0
    for i, line in enumerate(lines):
        txt_y = first_baseline - i * lh
        txt = label(
            x, txt_y, line, font=font, size=size, color=text_color, anchor="middle"
        )
        g.add(txt)

    return g


def underlined_label(
    x: float,
    y: float,
    text: str,
    font: str = "Helvetica-Bold",
    size: float = 9.0,
    color: str = "#6ee7b7",
) -> Group:
    """
    Text with an underline (for primary key attributes).
    The underline width is estimated from character count.
    """
    g = Group()
    s = label(x, y, text, font=font, size=size, color=color, anchor="middle")
    g.add(s)
    char_width = size * 0.55
    half_w = len(text) * char_width / 2
    ul = solid_line(x - half_w, y - 2.0, x + half_w, y - 2.0, color=color, width=0.9)
    g.add(ul)
    return g


def badge(
    cx: float,
    cy: float,
    text: str,
    bg: str = "#0f172a",
    fg: str = "#f87171",
    border: str = "#ef4444",
    radius: float = 7.0,
    font: str = "Helvetica-Bold",
    size: float = 9.0,
) -> Group:
    """
    Small rounded rectangle badge -- used for cardinality labels (1, N, M).
    """
    char_width = size * 0.65
    half_w = max(len(text) * char_width / 2 + 3, radius)
    x = cx - half_w
    y = cy - radius
    w = half_w * 2
    h = radius * 2
    g = Group()
    bg_rect = rounded_rect(
        x, y, w, h, rx=radius, fill=bg, stroke=border, stroke_width=0.9
    )
    g.add(bg_rect)
    txt = label(
        cx, cy - size * 0.35, text, font=font, size=size, color=fg, anchor="middle"
    )
    g.add(txt)
    return g


def divider_line(
    x: float,
    y: float,
    w: float,
    color: str = "#334155",
    width: float = 0.7,
) -> Line:
    """Horizontal separator used inside class diagram sections."""
    return solid_line(x, y, x + w, y, color=color, width=width)


def double_border_rect(
    x: float,
    y: float,
    w: float,
    h: float,
    fill: str = "#0b2848",
    stroke: str = "#38bdf8",
    stroke_width: float = 1.5,
    gap: float = 3.0,
) -> Group:
    """Rectangle with a concentric inner rectangle -- weak entity or identifying relationship."""
    g = Group()
    outer = plain_rect(x, y, w, h, fill=fill, stroke=stroke, stroke_width=stroke_width)
    inner = plain_rect(
        x + gap,
        y + gap,
        w - gap * 2,
        h - gap * 2,
        fill=fill,
        stroke=stroke,
        stroke_width=0.9,
    )
    g.add(outer)
    g.add(inner)
    return g


def initial_state_marker(
    target_x: float,
    target_y: float,
    direction: Literal["right", "left", "up", "down"] = "right",
    r: float = 5.0,
    color: str = "#38bdf8",
    arrow_len: float = 18.0,
) -> Group:
    """Filled circle with an arrow -- marks the initial state in state machines."""
    g = Group()
    offsets: dict[str, tuple[float, float]] = {
        "right": (-arrow_len - r * 2, 0),
        "left": (arrow_len + r * 2, 0),
        "up": (0, -arrow_len - r * 2),
        "down": (0, arrow_len + r * 2),
    }
    ox, oy = offsets[direction]
    dot_cx = target_x + ox
    dot_cy = target_y + oy
    dot = Circle(dot_cx, dot_cy, r)
    dot.fillColor = _hex(color)
    dot.strokeColor = _hex(color)
    dot.strokeWidth = 1.0
    g.add(dot)
    arrow = arrow_line(dot_cx, dot_cy, target_x, target_y, color=color, arrow_size=7.0)
    g.add(arrow)
    return g


def rack_lines(
    x: float,
    y: float,
    w: float,
    h: float,
    color: str = "#334155",
    count: int = 3,
) -> Group:
    """Horizontal dashes inside a server node to suggest rack units."""
    g = Group()
    spacing = h / (count + 1)
    for i in range(1, count + 1):
        ly = y + spacing * i
        ln = dashed_line(
            x + 4, ly, x + w - 4, ly, color=color, width=0.6, dash=(3.0, 3.0)
        )
        g.add(ln)
    return g


# ---------------------------------------------------------------------------
# Contrast color helpers for dynamic node labels and environmental adaptivity
# ---------------------------------------------------------------------------


def is_light_color(color: str | Color | None) -> bool:
    """Return True if the color is light, False if it is dark."""
    if color is None:
        return False
    if isinstance(color, Color):
        try:
            r, g, b = color.red * 255, color.green * 255, color.blue * 255
            luma = 0.299 * r + 0.587 * g + 0.114 * b
            return bool(luma > 150)
        except AttributeError:
            return False
    if isinstance(color, str):
        if color.lower() == "none":
            return True
        hex_str = color.lstrip("#")
        if len(hex_str) == 3:
            hex_str = "".join(c * 2 for c in hex_str)
        if len(hex_str) != 6:
            return False
        try:
            r = int(hex_str[0:2], 16)
            g = int(hex_str[2:4], 16)
            b = int(hex_str[4:6], 16)
            luma = 0.299 * r + 0.587 * g + 0.114 * b
            return bool(luma > 150)
        except ValueError:
            return False
    return False


def get_contrast_color(
    bg_color: str | Color | None, light_fg: str = "#e2e8f0", dark_fg: str = "#0f172a"
) -> str:
    """Choose light_fg or dark_fg depending on background brightness."""
    return dark_fg if is_light_color(bg_color) else light_fg
