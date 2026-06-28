"""
Engrapha Logo Generator
========================
Generates SVG assets with transparent backgrounds:

  assets/engrapha_icon.svg          — 500×500 square icon  (PyPI / GitHub avatar / favicon)
  assets/engrapha_logo.svg          — 700×200 horizontal wordmark  (README header)
  assets/engrapha_banner.svg        — 1280×640 banner  (GitHub social preview)

  assets/engrapha_icon_black.svg    — ink variant (for light backgrounds)
  assets/engrapha_logo_black.svg
  assets/engrapha_banner_black.svg

Design
------
A single, bold "E". The stem, middle arm, and bottom arm are plain flat
bars. The TOP arm only is shaped like a sharpened pencil: it runs as a
bar, then tapers into a wood-toned cone, ending in a dark graphite point —
the literal writing tool, attached to the letter itself, rather than a
separate icon placed next to it.

  • MAIN     (#2563EB)  The E itself (stem + all three arms)
  • WOOD     (#E8B84B)  Pencil cone, top arm only
  • GRAPHITE (#1F2937)  Pencil tip point, top arm only
  • WHITE    (#F9FAFB)  Wordmark text on dark surfaces
  • INK      (#111827)  Wordmark text on light surfaces

WOOD and GRAPHITE stay fixed regardless of light/dark variant — a pencil's
wood and graphite tones don't invert the way flat brand-color fills might.

All assets have a transparent background so they work on any dark or light
surface.
"""

import os
from reportlab.graphics.shapes import Drawing, Group, Rect, Polygon, String
from reportlab.graphics import renderSVG
from reportlab.lib.colors import HexColor

# ── Palette ───────────────────────────────────────────────────────────────────
MAIN = HexColor("#2563EB")
WOOD = HexColor("#E8B84B")
GRAPHITE = HexColor("#1F2937")
WHITE = HexColor("#F9FAFB")
INK = HexColor("#111827")
TAG_GREY = HexColor("#9CA3AF")

# ── Helpers ───────────────────────────────────────────────────────────────────


def P(pts, fill):
    """Filled polygon, no stroke. pts: list of (x, y) tuples."""
    flat = [coord for point in pts for coord in point]
    p = Polygon(flat)
    p.fillColor = fill
    p.strokeColor = None
    p.strokeWidth = 0
    return p


def R(x, y, w, h, fill):
    r = Rect(x, y, w, h)
    r.fillColor = fill
    r.strokeColor = None
    r.strokeWidth = 0
    return r


def postprocess_svg(path: str) -> None:
    svg = open(path, encoding="utf-8").read()
    svg = svg.replace("fill-rule: evenodd", "fill-rule: nonzero")
    svg = svg.replace('fill-rule="evenodd"', 'fill-rule="nonzero"')
    open(path, "w", encoding="utf-8").write(svg)


# ── Monogram geometry (400×400 local box, Y-up ReportLab coords) ──────────────
# Local geometry is fixed; callers scale/offset via `s`/`ox`/`oy`.


def _draw_mark(g: Group, ox: float, oy: float, s: float, main_color):
    def r(x, y, w, h, c):
        g.add(R(ox + x * s, oy + y * s, w * s, h * s, c))

    def poly(pts, c):
        g.add(P([(ox + x * s, oy + y * s) for x, y in pts], c))

    # Stem
    r(80, 40, 60, 320, main_color)
    # Bottom arm — plain flat bar
    r(80, 40, 190, 64, main_color)
    # Middle arm — plain flat bar, shorter, set low
    r(80, 160, 130, 60, main_color)
    # Top arm — shorter blue bar, then pencil replaces the rest
    r(120, 296, 80, 64, main_color)
    poly([(200, 296), (200, 360), (250, 336), (250, 320)], WOOD)
    poly([(250, 320), (250, 336), (265, 328)], GRAPHITE)


# ── 1. Icon  500 × 500 ────────────────────────────────────────────────────────


def build_icon(main_color=MAIN) -> Drawing:
    W = H = 500.0
    d = Drawing(W, H)
    g = Group()

    mark_size = 340.0
    s = mark_size / 400.0
    ox = (W - mark_size) / 2.0
    oy = (H - mark_size) / 2.0
    _draw_mark(g, ox=ox, oy=oy, s=s, main_color=main_color)

    d.add(g)
    return d


# ── 2. Logo  700 × 200 (horizontal wordmark) ──────────────────────────────────


def build_logo(main_color=MAIN, text_color=None) -> Drawing:
    W, H = 700.0, 200.0
    d = Drawing(W, H)
    g = Group()

    if text_color is None:
        text_color = WHITE

    mark_size = 168.0
    s = mark_size / 400.0
    ox = 20.0
    oy = (H - mark_size) / 2.0
    _draw_mark(g, ox=ox, oy=oy, s=s, main_color=main_color)

    tx = ox + mark_size + 34.0
    fs = 74

    cap_height = fs * 0.717
    ty = H / 2.0 - cap_height / 2.0

    title = String(tx, ty, "Engrapha")
    title.fontName = "Helvetica-Bold"
    title.fontSize = fs
    title.fillColor = text_color
    title.textAnchor = "start"
    g.add(title)

    d.add(g)
    return d


# ── 3. Banner  1280 × 640 ──────────────────────────────────────────────────────


def build_banner(dots: bool = True, main_color=MAIN, text_color=None) -> Drawing:
    W, H = 1280.0, 640.0
    d = Drawing(W, H)
    g = Group()

    if text_color is None:
        text_color = WHITE

    if dots:
        dot_step = 48.0
        dot_r = 1.8
        dot_c = HexColor("#1F2937")
        x = dot_step
        while x < W:
            y = dot_step
            while y < H:
                r = Rect(x - dot_r, y - dot_r, dot_r * 2, dot_r * 2)
                r.fillColor = dot_c
                r.strokeColor = None
                g.add(r)
                y += dot_step
            x += dot_step

    mark_size = 360.0
    s = mark_size / 400.0
    ox = 130.0
    oy = (H - mark_size) / 2.0
    _draw_mark(g, ox=ox, oy=oy, s=s, main_color=main_color)

    tx = ox + mark_size + 70.0
    fs = 130
    tag_fs = 36
    gap = 34.0

    cap_height = fs * 0.717
    tag_cap_height = tag_fs * 0.717

    block_height = cap_height + gap + tag_cap_height
    block_top = H / 2.0 + block_height / 2.0

    ty = block_top - cap_height
    tag_ty = ty - gap - tag_cap_height

    title = String(tx, ty, "Engrapha")
    title.fontName = "Helvetica-Bold"
    title.fontSize = fs
    title.fillColor = text_color
    title.textAnchor = "start"
    g.add(title)

    tag = String(tx, tag_ty, "Technical Publishing for Python")
    tag.fontName = "Helvetica"
    tag.fontSize = tag_fs
    tag.fillColor = TAG_GREY
    tag.textAnchor = "start"
    g.add(tag)

    d.add(g)
    return d


# ── Main ──────────────────────────────────────────────────────────────────────


def generate_assets():
    out = "assets"
    os.makedirs(out, exist_ok=True)

    assets = [
        ("engrapha_icon.svg", build_icon()),
        ("engrapha_logo.svg", build_logo(text_color=WHITE)),
        ("engrapha_banner.svg", build_banner(dots=True, text_color=WHITE)),
    ]

    for name, drawing in assets:
        path = os.path.join(out, name)
        renderSVG.drawToFile(drawing, path)
        postprocess_svg(path)
        print(f"OK {path}")

    assets_black = [
        ("engrapha_icon_black.svg", build_icon()),
        ("engrapha_logo_black.svg", build_logo(text_color=INK)),
        ("engrapha_banner_black.svg", build_banner(dots=False, text_color=INK)),
    ]

    for name, drawing in assets_black:
        path = os.path.join(out, name)
        renderSVG.drawToFile(drawing, path)
        postprocess_svg(path)
        print(f"OK {path}")

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
