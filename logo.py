"""
PaperForge Logo Generator
=========================
Generates SVG assets with transparent backgrounds:

  assets/paperforge_icon.svg    — 500×500 square icon  (PyPI / GitHub avatar / favicon)
  assets/paperforge_logo.svg    — 700×200 horizontal wordmark  (README header)
  assets/paperforge_banner.svg  — 1280×640 banner  (GitHub social preview)

Design
------
A PF monogram where P and F share one vertical backbone stem.
  • WHITE (#F9FAFB)  P-bowl  → Paper / document / content
  • BLUE  (#2563EB)  F-arms  → Forge / flow / diagram output

All assets have a transparent background so they work on any dark or light surface.
The icon variant adds a rounded square container for contexts that need one.
"""

import os
import re
from reportlab.graphics.shapes import Drawing, Group, Rect, Polygon, String, Line
from reportlab.graphics import renderSVG
from reportlab.lib.colors import HexColor

# ── Palette ───────────────────────────────────────────────────────────────────
BLUE = HexColor("#2563EB")  # F-arms   — forge / flow
WHITE = HexColor("#F9FAFB")  # P-bowl   — paper / content
INK = HexColor("#111827")  # container bg (icon only, not banner/logo)
FOLD = HexColor("#1E3A8A")  # dog-ear shadow

# ── Helpers ───────────────────────────────────────────────────────────────────


def R(x, y, w, h, color):
    """Stroke-less filled rectangle."""
    r = Rect(x, y, w, h)
    r.fillColor = color
    r.strokeColor = None
    r.strokeWidth = 0
    return r


def P(pts, fill):
    """Filled polygon, no stroke."""
    p = Polygon(pts)
    p.fillColor = fill
    p.strokeColor = None
    p.strokeWidth = 0
    return p


def postprocess_svg(path: str) -> None:
    """
    ReportLab SVG renderer writes fill-rule:evenodd on the root <g>.
    This can cause the P counter (negative space) to accidentally punch through
    shapes beneath it.  We switch it to nonzero so our solid rects stack cleanly.
    Also ensures no stray white background rect sneaks in.
    """
    svg = open(path, encoding="utf-8").read()
    svg = svg.replace("fill-rule: evenodd", "fill-rule: nonzero")
    svg = svg.replace('fill-rule="evenodd"', 'fill-rule="nonzero"')
    open(path, "w", encoding="utf-8").write(svg)


# ── Monogram geometry (500×500 canvas, Y-up ReportLab coords) ─────────────────

_MX = 155  # monogram left edge
_SW = 40  # stem width
_MY = 100  # monogram bottom (Shifted down to make room for the F)
_MH = 290  # monogram height (→ top remains exactly at 390)


def _monogram(g: Group, ox: float, oy: float, s: float):
    """
    Draw the PF monogram into group g.
    ox, oy = origin offset (bottom-left of monogram in drawing coords)
    s      = uniform scale factor
    """

    def rr(x, y, w, h, c):
        g.add(R(ox + x * s, oy + y * s, w * s, h * s, c))

    # Stem
    rr(_MX, _MY, _SW, _MH, WHITE)

    # P – top bar
    rr(_MX + _SW, 355, 115, 35, WHITE)

    # P – right post (Height adjusted to meet the newly shifted mid-bar)
    rr(_MX + _SW + 80, 270, 35, 85, WHITE)

    # P – mid bar (Shifted UP 5px to y=235)
    rr(_MX + _SW, 235, 115, 35, WHITE)

    # ── Increased Negative Space ──
    # F – upper arm (Shifted DOWN 10px to y=160).
    # This creates a massive 40px gap between the top of this arm and the bottom of the P!
    rr(_MX + _SW, 160, 150, 35, BLUE)

    # F – lower arm (Shifted DOWN 10px to y=100).
    # Maintains the exact 25px internal gap between the two blue F arms.
    rr(_MX + _SW, 100, 90, 35, BLUE)


# ── 1. Icon  500 × 500 ────────────────────────────────────────────────────────


def build_icon() -> Drawing:
    W = H = 500.0
    d = Drawing(W, H)
    g = Group()

    _monogram(g, ox=17.5, oy=5.0, s=1.0)

    d.add(g)
    return d


def build_logo() -> Drawing:
    W, H = 700.0, 200.0
    d = Drawing(W, H)
    g = Group()

    s = 0.45
    _monogram(g, ox=0.0, oy=10.0, s=s)

    tx = 180.0
    fs = 76

    cap_height = fs * 0.72
    ty = (H - cap_height) / 2.0

    title = String(tx, ty, "PaperForge")
    title.fontName = "Helvetica-Bold"
    title.fontSize = fs
    title.fillColor = WHITE
    title.textAnchor = "start"
    g.add(title)

    d.add(g)
    return d


def build_banner(dots: bool = True) -> Drawing:
    W, H = 1280.0, 640.0
    d = Drawing(W, H)
    g = Group()

    if dots:
        dot_step = 48.0
        dot_r = 1.8
        dot_c = HexColor("#1F2937")
        x = dot_step
        while x < W:
            y = dot_step
            while y < H:
                dot = R(x - dot_r, y - dot_r, dot_r * 2, dot_r * 2, dot_c)
                g.add(dot)
                y += dot_step
            x += dot_step

    s = 1.17
    _monogram(g, ox=20.0, oy=33.0, s=s)

    tx = 460.0
    ty = 340.0
    fs = 140

    title = String(tx, ty, "PaperForge")
    title.fontName = "Helvetica-Bold"
    title.fontSize = fs
    title.fillColor = WHITE
    title.textAnchor = "start"
    g.add(title)

    tag = String(tx, ty - 182.0, "Technical Publishing for Python")
    tag.fontName = "Helvetica"
    tag.fontSize = 42
    tag.fillColor = HexColor("#9CA3AF")
    tag.textAnchor = "start"
    g.add(tag)

    d.add(g)
    return d


# ── Main ──────────────────────────────────────────────────────────────────────


def generate_assets():
    out = "assets"
    os.makedirs(out, exist_ok=True)

    global WHITE
    original_white = WHITE

    # Generate White variants
    assets = [
        ("paperforge_icon.svg", build_icon()),
        ("paperforge_logo.svg", build_logo()),
        ("paperforge_banner.svg", build_banner()),
    ]

    for name, drawing in assets:
        path = os.path.join(out, name)
        renderSVG.drawToFile(drawing, path)
        postprocess_svg(path)
        print(f"OK {path}")

    # Generate Black variants
    WHITE = HexColor("#111827")  # INK color (black)
    assets_black = [
        ("paperforge_icon_black.svg", build_icon()),
        ("paperforge_logo_black.svg", build_logo()),
        ("paperforge_banner_black.svg", build_banner(dots=False)),
    ]

    for name, drawing in assets_black:
        path = os.path.join(out, name)
        renderSVG.drawToFile(drawing, path)
        postprocess_svg(path)
        print(f"OK {path}")

    WHITE = original_white

    print()
    print("Tip — PNG export (requires cairosvg):")
    print("  pip install cairosvg")
    print('  python -c "')
    print("  import cairosvg, glob")
    print("  for f in glob.glob('assets/*.svg'):")
    print("      cairosvg.svg2png(url=f, write_to=f.replace('.svg', '.png'), scale=2)")
    print('  "')


if __name__ == "__main__":
    generate_assets()
