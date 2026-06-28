"""
Computer Architecture IT-404 -- Autonomous Examination, June 2022
Previous Year Questions & Answers
UIT-RGPV (Autonomous) Bhopal | Semester IV
Run: python ca_pyq.py
Output: CA_PYQ_Answers.pdf
"""

from __future__ import annotations

import sys

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.platypus import (
    Paragraph,
    Table,
    TableStyle,
)

import engrapha_diagrams as ed
import engrapha_notes as en
from engrapha_notes import (
    COVER_H1,
    COVER_H2,
    COVER_SUB,
    add,
    body,
    br,
    build_doc,
    bullet,
    chap_box,
    code_block,
    definition,
    info_table,
    note,
    packet_format,
    part_box,
    rule,
    section,
    sp,
    story,
)

PAGE_W, PAGE_H = A4
PM = 1.8 * cm
CW = PAGE_W - 2 * PM

# -- Color palette & Theme configuration ---------------------------------------
theme_name = "midnight_dark"
for arg in sys.argv[1:]:
    if arg.startswith("--theme="):
        theme_name = arg.split("=")[1].lower()
    elif arg == "--light":
        theme_name = "light"

theme_map = {
    "dark": en.DARK,
    "light": en.LIGHT,
    "ocean_dark": en.OCEAN_DARK,
    "forest_dark": en.FOREST_DARK,
    "sunset_dark": en.SUNSET_DARK,
    "midnight_dark": en.MIDNIGHT_DARK,
    "ocean_light": en.OCEAN_LIGHT,
    "sepia": en.SEPIA,
}

active_theme = theme_map.get(theme_name, en.MIDNIGHT_DARK)
en.set_story([])
en.set_theme(active_theme)
print(f"Using theme: {active_theme.name}")

diag_theme = ed.DiagramTheme.from_notes_theme(en.get_theme())


# =============================================================================
#  CUSTOM CPU DIAGRAM DRAWING HELPERS
# =============================================================================
def intersect_segments(p1, p2, p3, p4):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4
    denom = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1)
    if abs(denom) < 1e-9:
        return None
    ua = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / denom
    ub = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / denom
    if 0.0 <= ua <= 1.0 and 0.0 <= ub <= 1.0:
        return x1 + ua * (x2 - x1), y1 + ua * (y2 - y1)
    return None


def clip_polygon(poly_points, cx, cy, tx, ty):
    from engrapha_diagrams.layout import edge_clip_rect

    p1 = (cx, cy)
    p2 = (tx, ty)
    n = len(poly_points) // 2
    for i in range(n):
        p3 = (poly_points[2 * i], poly_points[2 * i + 1])
        next_idx = (i + 1) % n
        p4 = (poly_points[2 * next_idx], poly_points[2 * next_idx + 1])
        pt = intersect_segments(p1, p2, p3, p4)
        if pt is not None:
            return pt
    return edge_clip_rect(cx, cy, 56.0, 28.0, tx, ty)


def clip_alu(cx, cy, w, h, tx, ty):
    pts = [
        cx - w / 2,
        cy + h / 2,
        cx - w / 6,
        cy + h / 2,
        cx,
        cy + h / 6,
        cx + w / 6,
        cy + h / 2,
        cx + w / 2,
        cy + h / 2,
        cx + w / 4,
        cy - h / 2,
        cx - w / 4,
        cy - h / 2,
    ]
    return clip_polygon(pts, cx, cy, tx, ty)


def clip_mux_custom(cx, cy, w, h, tx, ty):
    W = 70.0
    H = 60.0
    pts = [
        cx - W / 2, cy + H / 2,
        cx + W / 2, cy + H / 2,
        cx + W / 4, cy - H / 2,
        cx - W / 4, cy - H / 2,
    ]
    return clip_polygon(pts, cx, cy, tx, ty)


def clip_input(cx, cy, w, h, tx, ty):
    skew = 6.0
    pts = [
        cx - w / 2 + skew,
        cy + h / 2,
        cx + w / 2 + skew,
        cy + h / 2,
        cx + w / 2,
        cy - h / 2,
        cx - w / 2,
        cy - h / 2,
    ]
    return clip_polygon(pts, cx, cy, tx, ty)


def draw_alu(diag, cx, cy, w, h, fill, stroke):
    import engrapha_diagrams.shapes as S

    pts = [
        cx - w / 2,
        cy + h / 2,
        cx - w / 6,
        cy + h / 2,
        cx,
        cy + h / 6,
        cx + w / 6,
        cy + h / 2,
        cx + w / 2,
        cy + h / 2,
        cx + w / 4,
        cy - h / 2,
        cx - w / 4,
        cy - h / 2,
    ]
    diag._add(S.polygon(pts, fill=fill, stroke=stroke, stroke_width=1.5))


def draw_register(diag, cx, cy, w, h, fill, stroke):
    import engrapha_diagrams.shapes as S

    diag._add(
        S.rounded_rect(
            cx - w / 2,
            cy - h / 2,
            w,
            h,
            rx=3,
            fill=fill,
            stroke=stroke,
            stroke_width=1.5,
        )
    )
    for i in range(1, 4):
        x = cx - w / 2 + i * (w / 4)
        diag._add(S.solid_line(x, cy - h / 2, x, cy + h / 2, color=stroke, width=0.8))


def draw_nothing(diag, cx, cy, w, h, fill, stroke):
    pass


def clip_none(cx, cy, w, h, tx, ty):
    return cx, cy


def draw_fa_labeled(diag, cx, cy, w, h, fill, stroke):
    import engrapha_diagrams.shapes as S

    W = 70.0
    H = 50.0
    diag._add(
        S.rounded_rect(
            cx - W / 2,
            cy - H / 2,
            W,
            H,
            rx=4,
            fill=fill,
            stroke=stroke,
            stroke_width=1.5,
        )
    )
    diag._add(
        S.label(
            cx,
            cy + 4,
            "Full Adder",
            font="Helvetica-Bold",
            size=9.0,
            color=diag_theme.node_text,
            anchor="middle",
        )
    )
    diag._add(
        S.label(
            cx,
            cy - 6,
            "(FA_i)",
            font="Helvetica",
            size=8.0,
            color=diag_theme.node_text,
            anchor="middle",
        )
    )


def clip_fa_custom(cx, cy, w, h, tx, ty):
    from engrapha_diagrams.layout import edge_clip_rect

    W = 70.0
    H = 50.0
    return edge_clip_rect(cx, cy, W, H, tx, ty)


def draw_block_80x40(diag, cx, cy, w, h, fill, stroke):
    import engrapha_diagrams.shapes as S

    diag._add(
        S.rounded_rect(
            cx - 40,
            cy - 20,
            80,
            40,
            rx=3,
            fill=fill,
            stroke=stroke,
            stroke_width=1.5,
        )
    )


def clip_block_80x40(cx, cy, w, h, tx, ty):
    from engrapha_diagrams.layout import edge_clip_rect

    return edge_clip_rect(cx, cy, 80.0, 40.0, tx, ty)


def draw_cu(diag, cx, cy, w, h, fill, stroke):
    import engrapha_diagrams.shapes as S

    diag._add(
        S.rounded_rect(
            cx - w / 2,
            cy - h / 2,
            w,
            h,
            rx=4,
            fill=fill,
            stroke=stroke,
            stroke_width=1.5,
        )
    )
    diag._add(
        S.solid_line(
            cx - w / 2, cy - h / 6, cx + w / 2, cy - h / 6, color=stroke, width=1.0
        )
    )
    for i in range(1, 6):
        x = cx - w / 2 + i * (w / 6)
        diag._add(S.solid_line(x, cy - h / 2, x, cy - h / 6, color=stroke, width=0.6))


def draw_mux_labeled(diag, cx, cy, w, h, fill, stroke):
    import engrapha_diagrams.shapes as S
    W = 70.0
    H = 60.0
    pts = [
        cx - W / 2, cy + H / 2,
        cx + W / 2, cy + H / 2,
        cx + W / 4, cy - H / 2,
        cx - W / 4, cy - H / 2,
    ]
    diag._add(S.polygon(pts, fill=fill, stroke=stroke, stroke_width=1.5))
    diag._add(
        S.label(
            cx,
            cy + 2,
            "4x1 MUX",
            font="Helvetica-Bold",
            size=9.0,
            color=diag_theme.node_text,
            anchor="middle",
        )
    )

    # 4 input lines and labels
    y_offsets = [18, 6, -6, -18]
    borders = [-31.5, -28.0, -24.5, -21.0]
    labels = ["B_i", "B_i'", "0", "1"]
    for y_off, border_x, lbl in zip(y_offsets, borders, labels, strict=False):
        diag._add(S.solid_line(cx - 55, cy + y_off, cx + border_x, cy + y_off, color=stroke, width=1.0))
        diag._add(
            S.label(
                cx - 59,
                cy + y_off - 3.0,
                lbl,
                font="Helvetica",
                size=8.0,
                color=diag_theme.node_text,
                anchor="end",
            )
        )

    # select index numbers inside the MUX
    select_indices = ["0", "1", "2", "3"]
    for y_off, border_x, idx in zip(y_offsets, borders, select_indices, strict=False):
        diag._add(
            S.label(
                cx + border_x + 3.0,
                cy + y_off - 3.0,
                idx,
                font="Helvetica",
                size=7.0,
                color=diag_theme.node_text,
                anchor="start",
            )
        )


def draw_input(diag, cx, cy, w, h, fill, stroke):
    import engrapha_diagrams.shapes as S

    diag._add(
        S.parallelogram(
            cx - w / 2,
            cy - h / 2,
            w,
            h,
            skew=6.0,
            fill=fill,
            stroke=stroke,
            stroke_width=1.5,
        )
    )
    diag._add(
        S.solid_line(cx - w / 2 + 2, cy, cx + w / 2 + 2, cy, color=stroke, width=0.6)
    )
    for i in range(1, 5):
        x1 = cx - w / 2 + i * (w / 5)
        x2 = x1 + 3.0
        diag._add(S.solid_line(x1, cy - h / 2, x2, cy + h / 2, color=stroke, width=0.6))


def draw_output(diag, cx, cy, w, h, fill, stroke):
    import engrapha_diagrams.shapes as S

    diag._add(
        S.rounded_rect(
            cx - w / 2,
            cy - h / 6,
            w,
            h * 2 / 3,
            rx=3,
            fill=fill,
            stroke=stroke,
            stroke_width=1.5,
        )
    )
    diag._add(
        S.plain_rect(
            cx - w / 2 + 3,
            cy - h / 6 + 3,
            w - 6,
            h * 2 / 3 - 6,
            fill=fill,
            stroke=stroke,
            stroke_width=0.6,
        )
    )
    diag._add(
        S.solid_line(
            cx - w / 4, cy - h / 2, cx + w / 4, cy - h / 2, color=stroke, width=1.5
        )
    )
    diag._add(S.solid_line(cx, cy - h / 6, cx, cy - h / 2, color=stroke, width=1.5))


def draw_register_swap(diag, cx, cy, w, h, fill, stroke):
    import engrapha_diagrams.shapes as S
    mid_x = CW / 2
    r1_cx = mid_x - 90
    r2_cx = mid_x + 90
    ry = 115

    # Register colors and text
    r_fill = diag_theme.node_fill
    r_stroke = diag_theme.node_stroke

    # R1
    diag._add(S.rounded_rect(r1_cx - 35, ry - 20, 70, 40, rx=3, fill=r_fill, stroke=r_stroke, stroke_width=1.5))
    diag._add(S.label(r1_cx, ry + 2, "Register R1", font="Helvetica-Bold", size=9.0, color=diag_theme.node_text, anchor="middle"))
    diag._add(S.label(r1_cx, ry - 8, "(n bits)", font="Helvetica", size=7.5, color=diag_theme.node_text, anchor="middle"))

    # R2
    diag._add(S.rounded_rect(r2_cx - 35, ry - 20, 70, 40, rx=3, fill=r_fill, stroke=r_stroke, stroke_width=1.5))
    diag._add(S.label(r2_cx, ry + 2, "Register R2", font="Helvetica-Bold", size=9.0, color=diag_theme.node_text, anchor="middle"))
    diag._add(S.label(r2_cx, ry - 8, "(n bits)", font="Helvetica", size=7.5, color=diag_theme.node_text, anchor="middle"))

    # Control logic yT2
    ctrl_cx = mid_x
    ctrl_cy = 40
    diag._add(S.rounded_rect(ctrl_cx - 45, ctrl_cy - 15, 90, 30, rx=3, fill=r_fill, stroke=r_stroke, stroke_width=1.5))
    diag._add(S.multiline_label(ctrl_cx, ctrl_cy + 4.5, ["Control Logic", "(yT2)"], font="Helvetica-Bold", size=8.5, color=diag_theme.node_text, line_height=10.0, anchor="middle"))

    # Color codes for wires
    path_r1_to_r2_color = active_theme.accent       # Indigo: #818cf8
    path_r2_to_r1_color = active_theme.accent2      # Lavender: #c4b5fd
    ctrl_color = active_theme.green                 # Green: #34d399
    clk_color = active_theme.yellow                 # Yellow: #fbbf24

    # 1. Swap paths (R1 -> R2 path and R2 -> R1 path)
    # R1 -> R2 path: (r1_cx + 35, ry + 8) -> (mid_x - 30, ry + 8) -> (mid_x + 30, ry - 8) -> (r2_cx - 35, ry - 8)
    diag._add(S.solid_line(r1_cx + 35, ry + 8, mid_x - 30, ry + 8, color=path_r1_to_r2_color, width=1.5))
    diag._add(S.solid_line(mid_x - 30, ry + 8, mid_x + 30, ry - 8, color=path_r1_to_r2_color, width=1.5))
    diag._add(S.arrow_line(mid_x + 30, ry - 8, r2_cx - 35, ry - 8, color=path_r1_to_r2_color, width=1.5, arrow_end=True))
    diag._add(S.label(mid_x - 50, ry + 13, "R1 Out", font="Helvetica-Bold", size=8.0, color=path_r1_to_r2_color, anchor="middle"))

    # R2 -> R1 path: (r2_cx - 35, ry + 8) -> (mid_x + 30, ry + 8) -> (mid_x - 30, ry - 8) -> (r1_cx + 35, ry - 8)
    # We break the diagonal line to leave an 8px gap in the middle (where it crosses mid_x, ry) to show it's non-connecting.
    diag._add(S.solid_line(r2_cx - 35, ry + 8, mid_x + 30, ry + 8, color=path_r2_to_r1_color, width=1.5))
    diag._add(S.solid_line(mid_x + 30, ry + 8, mid_x + 4, ry + 1, color=path_r2_to_r1_color, width=1.5))
    # (Gap at middle)
    diag._add(S.solid_line(mid_x - 4, ry - 1, mid_x - 30, ry - 8, color=path_r2_to_r1_color, width=1.5))
    diag._add(S.arrow_line(mid_x - 30, ry - 8, r1_cx + 35, ry - 8, color=path_r2_to_r1_color, width=1.5, arrow_end=True))
    diag._add(S.label(mid_x + 50, ry + 13, "R2 Out", font="Helvetica-Bold", size=8.0, color=path_r2_to_r1_color, anchor="middle"))

    # Clock wiring (clk_y = 62)
    clk_y = 62
    diag._add(S.label(r1_cx - 52, clk_y - 3, "CLK", font="Helvetica-Bold", size=8.0, color=clk_color, anchor="end"))
    diag._add(S.solid_line(r1_cx - 45, clk_y, r2_cx + 10, clk_y, color=clk_color, width=1.2))
    diag._add(S.arrow_line(r1_cx + 10, clk_y, r1_cx + 10, ry - 20, color=clk_color, width=1.2, arrow_end=True))
    diag._add(S.arrow_line(r2_cx + 10, clk_y, r2_cx + 10, ry - 20, color=clk_color, width=1.2, arrow_end=True))

    # Clock dynamic triangle indicators
    diag._add(S.polygon([r1_cx + 5, ry - 20, r1_cx + 10, ry - 15, r1_cx + 15, ry - 20], fill="none", stroke=clk_color, stroke_width=1.0))
    diag._add(S.polygon([r2_cx + 5, ry - 20, r2_cx + 10, ry - 15, r2_cx + 15, ry - 20], fill="none", stroke=clk_color, stroke_width=1.0))

    # Clock T-junction dot at (r1_cx + 10, clk_y) where signal splits
    diag._add(S.circle(r1_cx + 10, clk_y, 2.5, fill=clk_color, stroke=clk_color))

    # Load control wiring
    # Vertical load control wire from (mid_x, 55) to (mid_x, 75).
    # It crosses clk_y = 62, so we add a 5px gap around y = 62.
    diag._add(S.solid_line(ctrl_cx, ctrl_cy + 15, ctrl_cx, clk_y - 2.5, color=ctrl_color, width=1.2))
    diag._add(S.solid_line(ctrl_cx, clk_y + 2.5, ctrl_cx, 75, color=ctrl_color, width=1.2))

    # Horizontal load line and vertical feeds to registers
    diag._add(S.solid_line(r1_cx - 10, 75, r2_cx - 10, 75, color=ctrl_color, width=1.2))
    diag._add(S.arrow_line(r1_cx - 10, 75, r1_cx - 10, ry - 20, color=ctrl_color, width=1.2, arrow_end=True))
    diag._add(S.arrow_line(r2_cx - 10, 75, r2_cx - 10, ry - 20, color=ctrl_color, width=1.2, arrow_end=True))
    diag._add(S.label(r1_cx - 15, ry - 28, "LD", font="Helvetica-Bold", size=8.0, color=ctrl_color, anchor="end"))
    diag._add(S.label(r2_cx - 15, ry - 28, "LD", font="Helvetica-Bold", size=8.0, color=ctrl_color, anchor="end"))
    diag._add(S.label(ctrl_cx + 10, ctrl_cy + 18, "yT2", font="Helvetica-Bold", size=8.0, color=ctrl_color, anchor="start"))

    # Load T-junction dot at (mid_x, 75) where load signal splits
    diag._add(S.circle(mid_x, 75, 2.5, fill=ctrl_color, stroke=ctrl_color))


def draw_associative_mapping(diag, cx, cy, w, h, fill, stroke):
    import engrapha_diagrams.shapes as S
    mid_x = CW / 2

    # CPU Address fields
    addr_y = 160
    diag._add(S.rounded_rect(mid_x - 110, addr_y, 110, 22, rx=2, fill=fill, stroke=stroke, stroke_width=1.5))
    diag._add(S.label(mid_x - 55, addr_y + 6, "Tag (15 bits)", font="Helvetica-Bold", size=8.5, color=diag_theme.node_text, anchor="middle"))

    diag._add(S.rounded_rect(mid_x, addr_y, 70, 22, rx=2, fill=fill, stroke=stroke, stroke_width=1.5))
    diag._add(S.label(mid_x + 35, addr_y + 6, "Word (5 bits)", font="Helvetica-Bold", size=8.5, color=diag_theme.node_text, anchor="middle"))
    diag._add(S.label(mid_x - 120, addr_y + 6, "CPU Address:", font="Helvetica-Bold", size=9.0, color=diag_theme.node_text, anchor="end"))

    # Cache memory table
    cache_y = 40
    cache_x = mid_x - 120
    col1_w = 90
    col2_w = 120
    row_h = 16

    # Headers
    diag._add(S.plain_rect(cache_x, cache_y + 4 * row_h, col1_w, 18, fill=fill, stroke=stroke, stroke_width=1.5))
    diag._add(S.plain_rect(cache_x + col1_w, cache_y + 4 * row_h, col2_w, 18, fill=fill, stroke=stroke, stroke_width=1.5))
    diag._add(S.label(cache_x + col1_w / 2, cache_y + 4 * row_h + 4, "Tag Memory", font="Helvetica-Bold", size=8.0, color=diag_theme.node_text, anchor="middle"))
    diag._add(S.label(cache_x + col1_w + col2_w / 2, cache_y + 4 * row_h + 4, "Data Memory", font="Helvetica-Bold", size=8.0, color=diag_theme.node_text, anchor="middle"))

    # Rows
    for idx, label in enumerate(["Line 0", "Line 1", "...", "Line 511"]):
        ry = cache_y + (3 - idx) * row_h
        if idx == 2:
            diag._add(S.dashed_line(cache_x, ry + row_h / 2, cache_x + col1_w + col2_w, ry + row_h / 2, color=stroke, width=0.8))
            continue
        diag._add(S.plain_rect(cache_x, ry, col1_w, row_h, fill=fill, stroke=stroke, stroke_width=1.0))
        diag._add(S.plain_rect(cache_x + col1_w, ry, col2_w, row_h, fill=fill, stroke=stroke, stroke_width=1.0))

        diag._add(S.label(cache_x - 5, ry + 3, label, font="Helvetica", size=7.0, color=diag_theme.node_text, anchor="end"))
        diag._add(S.label(cache_x + col1_w / 2, ry + 3, f"Tag {idx if idx < 2 else '511'}", font="Helvetica", size=7.5, color=diag_theme.node_text, anchor="middle"))
        diag._add(S.label(cache_x + col1_w + col2_w / 2, ry + 3, f"Data Block {idx if idx < 2 else '511'}", font="Helvetica", size=7.5, color=diag_theme.node_text, anchor="middle"))

    # Parallel tag comparisons
    tag_out_x = mid_x - 55
    diag._add(S.solid_line(tag_out_x, addr_y, tag_out_x, cache_y + 4 * row_h + 10, color=stroke, width=1.0))
    cam_x = cache_x + col1_w / 2
    diag._add(S.solid_line(tag_out_x, cache_y + 4 * row_h + 10, cam_x, cache_y + 4 * row_h + 10, color=stroke, width=1.0))
    diag._add(S.arrow_line(cam_x, cache_y + 4 * row_h + 10, cam_x, cache_y + 4 * row_h, color=stroke, width=1.0, arrow_end=True))

    for idx in [0, 1, 3]:
        ry = cache_y + (3 - idx) * row_h
        diag._add(S.arrow_line(cache_x + 5, ry + row_h / 2, cache_x + col1_w - 5, ry + row_h / 2, color=active_theme.accent, width=1.0, arrow_end=True, dashed=True))

    diag._add(S.label(cache_x + col1_w / 2, cache_y - 12, "Parallel Tag Comparison (CAM Search)", font="Helvetica-Oblique", size=7.5, color=active_theme.accent, anchor="middle"))

    # Word selection offset
    word_out_x = mid_x + 35
    diag._add(S.arrow_line(word_out_x, addr_y, word_out_x, cache_y + 4 * row_h, color=stroke, width=1.0, arrow_end=True))
    diag._add(S.label(word_out_x + 4, cache_y + 4 * row_h + 10, "Selects Word", font="Helvetica", size=7.5, color=diag_theme.node_text, anchor="start"))


def draw_daisy_chain(diag, cx, cy, w, h, fill, stroke):
    import engrapha_diagrams.shapes as S

    # We will draw within a canvas of width CW and height 130
    mid_y = 65

    # CPU Block
    cpu_x = 45
    cpu_w = 60
    cpu_h = 70
    diag._add(S.rounded_rect(cpu_x - cpu_w/2, mid_y - cpu_h/2, cpu_w, cpu_h, rx=4, fill=fill, stroke=stroke, stroke_width=1.5))
    diag._add(S.label(cpu_x, mid_y + 4, "CPU", font="Helvetica-Bold", size=10.0, color=diag_theme.node_text, anchor="middle"))

    # Device Blocks
    dev_w = 65
    dev_h = 60
    dev_y = mid_y
    dev_x_coords = [150, 260, 370]
    for idx, dx in enumerate(dev_x_coords, 1):
        diag._add(S.rounded_rect(dx - dev_w/2, dev_y - dev_h/2, dev_w, dev_h, rx=3, fill=fill, stroke=stroke, stroke_width=1.5))
        diag._add(S.label(dx, dev_y + 4, f"Device {idx}", font="Helvetica-Bold", size=9.0, color=diag_theme.node_text, anchor="middle"))

    # Data Bus at top (y = 115)
    bus_y = 115
    diag._add(S.solid_line(20, bus_y, 410, bus_y, color=stroke, width=2.0))
    diag._add(S.label(30, bus_y + 4, "Data Bus", font="Helvetica-Bold", size=8.0, color=diag_theme.node_text, anchor="start"))

    # Connect CPU and Devices to Data Bus
    # CPU to Data Bus
    diag._add(S.arrow_line(cpu_x, mid_y + cpu_h/2, cpu_x, bus_y, color=stroke, width=1.2, arrow_end=True, arrow_start=True))
    # Devices to Data Bus
    for dx in dev_x_coords:
        diag._add(S.arrow_line(dx, dev_y + dev_h/2, dx, bus_y, color=stroke, width=1.2, arrow_end=True))

    # INTA Daisy Chain (Priority Out -> Priority In)
    # CPU INTA output is at (75, 65)
    chain_color = active_theme.accent

    # CPU to Dev 1
    diag._add(S.arrow_line(cpu_x + cpu_w/2, mid_y, 150 - dev_w/2, mid_y, color=chain_color, width=1.5, arrow_end=True))
    diag._add(S.label(cpu_x + cpu_w/2 + 5, mid_y + 4, "INTA", font="Helvetica", size=7.0, color=diag_theme.node_text, anchor="start"))
    diag._add(S.label(150 - dev_w/2 - 2, mid_y + 4, "PI", font="Helvetica", size=7.0, color=diag_theme.node_text, anchor="end"))

    # Dev 1 to Dev 2
    diag._add(S.arrow_line(150 + dev_w/2, mid_y, 260 - dev_w/2, mid_y, color=chain_color, width=1.5, arrow_end=True))
    diag._add(S.label(150 + dev_w/2 + 2, mid_y + 4, "PO", font="Helvetica", size=7.0, color=diag_theme.node_text, anchor="start"))
    diag._add(S.label(260 - dev_w/2 - 2, mid_y + 4, "PI", font="Helvetica", size=7.0, color=diag_theme.node_text, anchor="end"))

    # Dev 2 to Dev 3
    diag._add(S.arrow_line(260 + dev_w/2, mid_y, 370 - dev_w/2, mid_y, color=chain_color, width=1.5, arrow_end=True))
    diag._add(S.label(260 + dev_w/2 + 2, mid_y + 4, "PO", font="Helvetica", size=7.0, color=diag_theme.node_text, anchor="start"))
    diag._add(S.label(370 - dev_w/2 - 2, mid_y + 4, "PI", font="Helvetica", size=7.0, color=diag_theme.node_text, anchor="end"))

    # Dev 3 PO line going right
    diag._add(S.solid_line(370 + dev_w/2, mid_y, 420, mid_y, color=chain_color, width=1.5))
    diag._add(S.label(370 + dev_w/2 + 2, mid_y + 4, "PO", font="Helvetica", size=7.0, color=diag_theme.node_text, anchor="start"))

    # INT Interrupt Request Line at bottom (y = 22)
    int_color = active_theme.red
    int_y = 22
    diag._add(S.solid_line(35, int_y, 370, int_y, color=int_color, width=1.2))
    # CPU INT input is at (45, 30)
    diag._add(S.arrow_line(cpu_x, int_y, cpu_x, mid_y - cpu_h/2, color=int_color, width=1.2, arrow_end=True))
    diag._add(S.label(cpu_x + 3, mid_y - cpu_h/2 + 4, "INT", font="Helvetica-Bold", size=7.5, color=diag_theme.node_text, anchor="start"))

    # Connect Devices to INT line
    for dx in dev_x_coords:
        diag._add(S.solid_line(dx, dev_y - dev_h/2, dx, int_y, color=int_color, width=1.2))

    # Draw T-junction dots
    for dx in dev_x_coords:
        diag._add(S.circle(dx, int_y, 2.0, fill=int_color, stroke=int_color))

    diag._add(S.label(30, int_y - 8, "Interrupt Request (INT) Line", font="Helvetica-Bold", size=7.5, color=diag_theme.node_text, anchor="start"))


# =============================================================================
#  COVER PAGE
# =============================================================================
en.bookmark("Cover Page")
sp(20)
t = Table(
    [
        [Paragraph("COMPUTER ARCHITECTURE", COVER_H1)],
        [Paragraph("IT-404  |  Autonomous Exam Solutions", COVER_H2)],
    ],
    colWidths=[CW],
)
t.setStyle(
    TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, -1), active_theme.rl(active_theme.surface)),
            ("TOPPADDING", (0, 0), (-1, -1), 24),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 24),
            ("LEFTPADDING", (0, 0), (-1, -1), 20),
            ("RIGHTPADDING", (0, 0), (-1, -1), 20),
            ("BOX", (0, 0), (-1, -1), 2.5, active_theme.rl(active_theme.accent)),
        ]
    )
)
add(t)
sp(14)
add(Paragraph("B.E./B.Tech. IV Semester (UIT) Autonomous", COVER_H2))
add(Paragraph("Examinations: June 2022, May/June 2023 &amp; June 2024 -- Solutions", COVER_SUB))
add(Paragraph("Time: Three Hours  |  Maximum Marks: 105", COVER_SUB))
sp(10)
rule(active_theme.rl(active_theme.accent), 1.5)
sp(8)

note(
    "<b>Exam Schema & Guidelines:</b><br/>"
    "1. Attempt all questions. All subparts of a question should be answered at one place.<br/>"
    "2. Parts <b>a</b>, <b>b</b>, and <b>c</b> of each question are <b>compulsory</b>, with allotted marks of <b>3, 4, and 4</b> respectively.<br/>"
    "3. Parts <b>d</b> and <b>e</b> represent an <b>internal choice</b>, with allotted marks of <b>10</b>. "
    "To provide complete coverage, both choice parts have been fully solved in these notes."
)

info_table(
    ["Question", "Marks Scheme", "Topic &amp; CO Coverage Summary"],
    [
        [
            "Question 1 (CO1)",
            "3 + 4 + 4 + 10 = 21 Marks",
            "Von Neumann Model, Instruction Execution Cycle, Registers Classification, RTL &amp; Register Swap logic, Arithmetic Circuit, Shift Micro-operations, Registers function (AC, MAR, MBR, IR, PC)",
        ],
        [
            "Question 2 (CO2)",
            "3 + 4 + 4 + 10 = 21 Marks",
            "IEEE 754 float layout &amp; conversion, Control Units (Hardwired vs Microprogrammed), 2's Complement Addition/Subtraction &amp; Overflow checks, Booth's Multiplication, Signed Representation &amp; Ranges",
        ],
        [
            "Question 3 (CO3)",
            "3 + 4 + 4 + 10 = 21 Marks",
            "Stack Micro-operations, Addressing Modes (Implied, Immediate, Relative, Index, Direct, Indirect), Infix to Postfix Algorithm &amp; RPN Conversion, Data Transfer (DMA)",
        ],
        [
            "Question 4 (CO4)",
            "3 + 4 + 4 + 10 = 21 Marks",
            "Memory Capacity &amp; Address lines, SRAM vs DRAM, Memory Hierarchy, Chip count calculations, Cache hit ratio, Average Cache Access Time (Serial/Parallel), Page Replacement (FIFO, LRU, Optimal), Cache Mapping Techniques (Associative)",
        ],
        [
            "Question 5 (CO5)",
            "3 + 4 + 4 + 10 = 21 Marks",
            "Pipelining &amp; Throughput, Speedup Factor derivation &amp; calculations, Space-Time Diagrams (6 segments, 8 tasks), Pipeline Hazards (Structural, Data, Control), Multiprocessor characteristics, Parallel processing techniques",
        ],
    ],
)
br()


# =============================================================================
#  QUESTION 1: CO1
# =============================================================================
part_box("QUESTION 1 -- CO1 FUNDAMENTALS")

# -- Q1 (a) --
chap_box(
    "Q1. a) Draw Von-Neumann model of computer and describe its subsystems. [3 Marks] (June 2022)\n"
    "[AND]\n"
    "Q1. a) Discuss \"Von Neumann bottleneck limitation\" of Von Neumann model. What are the ways to overcome this? [3 Marks] (June 2023)"
)
section("The Stored-Program Concept")
definition(
    "<b>Von Neumann Architecture:</b> A standard computer design model proposed by John von Neumann "
    "in 1945 where <b>both instruction code and program data share the same physical memory space</b> "
    "and are accessed using a single communication bus. The system executes instructions sequentially "
    "via a central controller."
)

section("Subsystems of the Von Neumann Model")
bullet(
    [
        "<b>1. Memory Unit:</b> A unified storage space that holds both executable instructions and binary data. "
        "It is organized as addressable locations accessed via address and data buses.",
        "<b>2. Arithmetic Logic Unit (ALU):</b> The processor core that performs all numerical calculations (addition, "
        "subtraction) and bitwise logic operations (AND, OR, XOR, shifts). Operates combinationally.",
        "<b>3. Control Unit (CU):</b> Coordinates all hardware operations. It fetches instructions from memory, decodes "
        "the instruction opcodes, and issues control signals to direct the datapath components.",
        "<b>4. Input Subsystem:</b> Interfaces external devices (keyboard, mouse) to feed digital data into the processor.",
        "<b>5. Output Subsystem:</b> Displays or exports computed results to user peripherals (displays, printers).",
    ]
)

section("Von Neumann Subsystems Diagram")
net_vn = ed.NetworkDiagram(
    width=CW,
    height=240,
    theme=diag_theme,
    caption="Fig 1.1: Von Neumann Subsystem Architecture block diagram",
)
net_vn.node("cu", "Control Unit\n(CU)", x=175, y=55, kind="custom", custom_draw=draw_cu)
net_vn.node(
    "alu",
    "Arithmetic Logic\nUnit (ALU)",
    x=345,
    y=55,
    kind="custom",
    custom_draw=draw_alu,
    custom_clip=clip_alu,
)
net_vn.node(
    "input",
    "Input Subsystem",
    x=65,
    y=135,
    kind="custom",
    custom_draw=draw_input,
    custom_clip=clip_input,
)
net_vn.node(
    "output",
    "Output Subsystem",
    x=450,
    y=135,
    kind="custom",
    custom_draw=draw_output,
)
net_vn.node("mem", "Memory Unit\n(Code + Data)", x=255, y=200, kind="database")

net_vn.link("input", "alu", label="Data")
net_vn.link("alu", "output", label="Data")
net_vn.link("alu", "mem", label="Data")
net_vn.link("mem", "cu", label="Instr/Ctrl", bidirectional=True)
net_vn.link("cu", "alu", label="Control")
net_vn.link("cu", "input", label="Control")
net_vn.link("cu", "output", label="Control")
story.extend(net_vn.as_flowable())

section("The Von Neumann Bottleneck Limitation")
body(
    "The <b>Von Neumann Bottleneck</b> refers to the throughput limitation caused by the shared single physical path (bus) "
    "for both instruction fetch and data read/write operations. Because the CPU speed is orders of magnitude faster than "
    "memory speed, the processor remains idle (waiting for memory access) during bus conflicts, creating a primary system bottleneck."
)

section("Ways to Overcome the Von Neumann Bottleneck")
bullet(
    [
        "<b>1. Cache Memory:</b> Placing a high-speed, small SRAM cache close to the processor to hold recently accessed "
        "instructions and data, reducing references to the slower main memory.",
        "<b>2. Harvard Architecture:</b> Separating physical memory spaces and data/instruction buses (e.g., L1 Cache is split "
        "into L1 Instruction Cache and L1 Data Cache), enabling concurrent instruction fetch and data transfers.",
        "<b>3. Pipelining & Out-of-Order Execution:</b> Overlapping instruction cycles and executing independent instructions "
        "while others wait for memory inputs.",
        "<b>4. Memory Interleaving:</b> Accessing multiple memory modules simultaneously to achieve higher bandwidth.",
        "<b>5. Processing-in-Memory (PIM):</b> Integrating execution logic directly inside memory modules to process data "
        "in-place, bypassing the transfer buses entirely.",
    ]
)
sp(10)

# -- Q1 (a) 2024 --
chap_box(
    "Q1. a) With the help of a suitable diagram explain the process of execution of an instruction in a computer. What do you mean by Fetch, decode and Execute cycle? [3 Marks] (June 2024)"
)
section("The Instruction Cycle (Fetch-Decode-Execute)")
body(
    "The <b>Instruction Cycle</b> is the fundamental process by which a computer's central processing unit (CPU) "
    "retrieves a program instruction from its memory, determines what actions the instruction requires, and "
    "carries out those actions. This cycle is repeated continuously from bootstrap to shutdown."
)
bullet(
    [
        "<b>1. Fetch Cycle:</b> The CPU fetches the instruction from the memory address pointed to by the Program Counter (PC). "
        "The instruction opcode is loaded into the Instruction Register (IR), and the PC is incremented to point to the next instruction.",
        "<b>2. Decode Cycle:</b> The Control Unit (CU) interprets the instruction stored in the IR. It decodes the operation code (opcode) "
        "to determine the hardware signals needed. It also determines the addressing mode and fetches any operands from memory if required.",
        "<b>3. Execute Cycle:</b> The CPU executes the decoded instruction. This may involve performing arithmetic/logic operations in the ALU, "
        "manipulating registers, jumping to a different memory address, or transferring data between memory and I/O modules.",
    ]
)

section("Instruction Cycle Flowchart")
fc_fde = ed.Flowchart(
    width=CW,
    height=280,
    theme=diag_theme,
    caption="Fig 1.1b: Sequential Flowchart of the Fetch-Decode-Execute Cycle",
)
fc_fde.terminal("start", "START")
fc_fde.process("fetch", "FETCH: IR <- M[PC]; PC <- PC + 1")
fc_fde.process("decode", "DECODE: Decode Opcode & Address Mode")
fc_fde.decision("indirect", "Indirect Address?")
fc_fde.process("fetch_op", "FETCH OPERAND: EA <- M[ADR]")
fc_fde.process("exec", "EXECUTE: Perform Operation")
fc_fde.terminal("next", "Next Instruction Loop")

fc_fde.edge("start", "fetch")
fc_fde.edge("fetch", "decode")
fc_fde.edge("decode", "indirect")
fc_fde.edge("indirect", "fetch_op", branch="Yes")
fc_fde.edge("indirect", "exec", branch="No")
fc_fde.edge("fetch_op", "exec")
fc_fde.edge("exec", "next")
fc_fde.edge("next", "fetch", orthogonal=True)
story.extend(fc_fde.as_flowable())
sp(10)

# -- Q1 (b) --
chap_box(
    "Q1. b) Classify various computer registers into two broad classes. Elaborate with suitable examples. [4 Marks]"
)
section("Classification of CPU Registers")
body(
    "Internal CPU registers are high-speed temporary storage cells implemented using D-type flip-flops. "
    "They are classified into two broad categories based on their programmer visibility:"
)

info_table(
    ["Register Class", "Definition & Purpose", "Examples & Function"],
    [
        [
            "User-Visible Registers\n(General-Purpose)",
            "Registers that can be directly referenced and manipulated by the programmer "
            "using machine instructions (assembly). They are used to hold temporary operands, "
            "address pointers, and loop counters.",
            "<b>• General Purpose (GPRs):</b> R0, R1, EAX, EBX - hold operands.\n"
            "<b>• Accumulator (AC):</b> Holds intermediate arithmetic results.\n"
            "<b>• Index Register (XR):</b> Used for address calculations.\n"
            "<b>• Base Register (BR):</b> Holds segment base addresses.",
        ],
        [
            "Control and Status Registers\n(User-Invisible)",
            "Registers used internally by the CPU control unit to manage instruction execution, "
            "control the memory interface, and store machine state. They cannot be modified "
            "directly by ordinary user-level software.",
            "<b>• Program Counter (PC):</b> Holds address of the next instruction.\n"
            "<b>• Instruction Register (IR):</b> Holds the current instruction opcode.\n"
            "<b>• Memory Address Register (MAR):</b> Holds the address being accessed.\n"
            "<b>• Memory Data Register (MDR):</b> Holds data read from or written to memory.\n"
            "<b>• Program Status Word (PSW):</b> Holds ALU flags (Z, N, C, V).",
        ],
    ],
    col_widths=[150, 180, 163],
)
sp(10)

# -- Q1 (b) 2024 --
chap_box(
    "Q1. b) Explain the term Register Transfer Language (RTL). Describe the following micro-operation and draw block diagram for it:\n yT2: R2 <- R1, R1 <- R2\n[4 Marks] (June 2024)\n"
    "[AND]\n"
    "Q1. b) Explain following RTL statements:\n R: MDR <- M[MAR]\n W: M[MAR] <- MDR\n[4 Marks] (June 2023)"
)
section("Register Transfer Language (RTL)")
definition(
    "<b>Register Transfer Language (RTL):</b> A symbolic notation system used to describe the "
    "micro-operations, data transfers, and control signals that occur between the internal registers "
    "of a digital system. It defines the datapath connections and conditions at the hardware level."
)

section("Micro-operation Description: yT2: R2 <- R1, R1 <- R2")
body(
    "The statement is a conditional simultaneous register swap operation controlled by the Boolean function <b>P = yT<sub>2</sub></b>. "
    "It has the following hardware implications:"
)
bullet(
    [
        "<b>Control Condition:</b> When yT<sub>2</sub> = 1, control logic asserts the Load (LD) inputs of both registers R1 and R2.",
        "<b>Simultaneous Transfer:</b> At the next positive clock edge (CLK), register R1 receives the content of register R2, "
        "and register R2 receives the content of register R1 in parallel. This is made possible because registers are built using "
        "edge-triggered flip-flops that sample their inputs before changing their outputs, avoiding data hazards.",
    ]
)

section("Register Swap Hardware Schematic Block Diagram")
net_swap = ed.NetworkDiagram(
    width=CW,
    height=170,
    theme=diag_theme,
    caption="Fig 1.2b: Hardware implementation of simultaneous swap yT2: R2 <- R1, R1 <- R2",
)
net_swap.node("swap_circ", "", x=CW/2, y=85, kind="custom", custom_draw=draw_register_swap)
story.extend(net_swap.as_flowable())
sp(10)

section("Memory Transfer RTL Statements (June 2023)")
body(
    "The two RTL statements describe memory data transfers controlled by control variables <b>R</b> (Read) and <b>W</b> (Write):"
)
bullet(
    [
        "<b>1. Memory Read Operation (R: MDR &larr; M[MAR]):</b> When control condition R = 1, "
        "the content of the memory word at the address specified by the Memory Address Register (MAR) is fetched "
        "and loaded into the Memory Data Register (MDR). This is an input data transfer from external memory to the CPU.",
        "<b>2. Memory Write Operation (W: M[MAR] &larr; MDR):</b> When control condition W = 1, "
        "the content currently held in the Memory Data Register (MDR) is written into the memory location "
        "specified by the address in the Memory Address Register (MAR). This is an output data transfer from the CPU to external memory.",
    ]
)
sp(10)

# -- Q1 (c) --
chap_box(
    "Q1. c) Draw the block diagram for the hardware that implements the following statements:\n x + y'z: AR <- AR + BR\nwhere AR and BR are two n-bit registers and x, y, and z are control variables. Include the logic gates for the control function. [4 Marks]"
)
section("Hardware Logic Analysis")
body(
    "To implement the conditional register transfer, we define a control signal <b>P = x + y'z</b>. "
    "When <b>P = 1</b>, the load enable input (LD) of register AR is asserted, causing the output of "
    "the binary adder (AR + BR) to be loaded into AR on the next positive clock edge. When P = 0, the LD input "
    "is deasserted, and AR retains its state."
)

bullet(
    [
        "<b>NOT Gate:</b> Inverts control variable y to produce y'.",
        "<b>AND Gate:</b> Combines y' and z to produce the product term y'z.",
        "<b>OR Gate:</b> Combines x and y'z to generate the final control signal P = x + y'z.",
        "<b>Binary Adder:</b> An n-bit combinational adder that continually computes the sum of the AR and BR outputs.",
        "<b>Clock (CLK):</b> Synchronously triggers the register update when LD (P) is active.",
    ]
)

section("Hardware Control Logic Schematic Diagram")
net_ctrl = ed.NetworkDiagram(
    width=CW,
    height=190,
    theme=diag_theme,
    caption="Fig 1.2: Logic control circuit and datapath for x + y'z: AR <- AR + BR",
)
net_ctrl.node(
    "br", "Register BR\n(n bits)", x=90, y=130, kind="custom", custom_draw=draw_register
)
net_ctrl.node(
    "ar",
    "Register AR\n(n bits)",
    x=270,
    y=130,
    kind="custom",
    custom_draw=draw_register,
)
net_ctrl.node(
    "adder",
    "n-bit Binary Adder",
    x=180,
    y=60,
    kind="custom",
    custom_draw=draw_block_80x40,
    custom_clip=clip_block_80x40,
)
net_ctrl.node(
    "ctrl",
    "Control Logic\n(P = x + y'z)",
    x=380,
    y=130,
    kind="custom",
    custom_draw=draw_block_80x40,
    custom_clip=clip_block_80x40,
)

net_ctrl.link("br", "adder", label="Data Out")
net_ctrl.link("ar", "adder", label="Data Out")
net_ctrl.link("adder", "ar", label="Sum (to Data In)", bidirectional=False)
net_ctrl.link("ctrl", "ar", label="Load (LD)", bidirectional=False)
story.extend(net_ctrl.as_flowable())
sp(10)

# -- Q1 (c) 2024 --
chap_box(
    "Q1. c) What do you mean by Arithmetic shift micro operation? Give a suitable example for it. [4 Marks] (June 2024)"
)
section("Arithmetic Shift Micro-operations")
definition(
    "<b>Arithmetic Shift:</b> A shift micro-operation that shifts signed binary numbers in a register "
    "left or right, while preserving the sign of the number in the most significant bit (MSB) position. "
    "It multiplies or divides the signed integer by 2."
)
bullet(
    [
        "<b>Arithmetic Shift Right (asr):</b> Shifts all bits right. The MSB (sign bit) is duplicated and "
        "copied into the next bit position to preserve the sign. The LSB is discarded. (Equivalent to division by 2).",
        "<b>Arithmetic Shift Left (asl):</b> Shifts all bits left. A 0 is inserted in the vacated LSB position. "
        "The MSB (sign bit) is shifted out. This can cause a signed overflow if the sign of the number changes.",
    ]
)

section("Detailed Numerical Example")
body(
    "Let register R contain the 8-bit signed value: <b>-6 = 1111 1010<sub>2</sub></b> (in 2's complement form):"
)
info_table(
    ["Operation", "Visual Bit Trace (MSB -> LSB)", "Result Value", "Mathematical Effect"],
    [
        [
            "Initial State",
            "[1] 1 1 1   1 0 1 0",
            "-6",
            "-",
        ],
        [
            "Arithmetic Shift Right (asr)",
            "<b>[1] [1]</b> 1 1   1 1 0 1  (LSB 0 discarded)",
            "-3",
            "Divides by 2: -6 / 2 = -3 (Correct)",
        ],
        [
            "Arithmetic Shift Left (asl)",
            "<b>[1]</b> 1 1 1   0 1 0 <b>0</b>  (MSB 1 shifted out)",
            "-12",
            "Multiplies by 2: -6 &times; 2 = -12 (Correct, no overflow)",
        ],
    ],
)
sp(10)

# -- Q1 (d) --
chap_box(
    "Q1. d) Build a 4 bit arithmetic circuit which can perform all the arithmetic operations on data stored in two registers. Write its function table. [10 Marks]"
)
section("Arithmetic Circuit Design")
body(
    "A 4-bit arithmetic circuit is built using 4 Full Adders (FA) connected in cascade, "
    "with their secondary inputs (Y_i) selected by a multiplexer at each stage. "
    "By controlling the inputs to the multiplexers, different arithmetic micro-operations "
    "are realized. The core operation of the adder circuit is <b>D = A + Y + Cin</b>."
)

section("Multiplexer Selection Logic")
body(
    "For each bit stage <i>i</i>, input A_i is connected directly to the Full Adder. Input B_i is "
    "passed to a 4-to-1 Multiplexer controlled by select lines S1 and S0. The MUX output Y_i is selected as:"
)
bullet(
    [
        "<b>S1S0 = 00:</b> Y_i = B_i (Pass B)",
        "<b>S1S0 = 01:</b> Y_i = B_i' (Pass 1's complement of B)",
        "<b>S1S0 = 10:</b> Y_i = 0 (Pass zero)",
        "<b>S1S0 = 11:</b> Y_i = 1 (in binary, equivalent to all 1s or -1 in 2's complement)",
    ]
)

section("Arithmetic Circuit Function Table")
info_table(
    [
        "S1",
        "S0",
        "Cin",
        "Y Input",
        "Result Equation (D = A + Y + Cin)",
        "Operation Implemented",
    ],
    [
        ["0", "0", "0", "B", "D = A + B", "Addition"],
        ["0", "0", "1", "B", "D = A + B + 1", "Add with Carry"],
        ["0", "1", "0", "B'", "D = A + B'", "Add 1's complement of B"],
        ["0", "1", "1", "B'", "D = A + B' + 1 = A - B", "Subtraction (2's complement)"],
        ["1", "0", "0", "0", "D = A", "Transfer A"],
        ["1", "0", "1", "0", "D = A + 1", "Increment A"],
        ["1", "1", "0", "-1 (all 1s)", "D = A - 1", "Decrement A"],
        ["1", "1", "1", "-1 (all 1s)", "D = A - 1 + 1 = A", "Transfer A (with offset)"],
    ],
)

section("Arithmetic Circuit Stage Diagram")
net_arith = ed.NetworkDiagram(
    width=CW,
    height=200,
    theme=diag_theme,
    caption="Fig 1.3: Single Stage (Stage i) of the 4-bit Arithmetic Circuit",
)
# Nodes representing multiplexer and adder
net_arith.node(
    "mux",
    "",
    x=145,
    y=100,
    kind="custom",
    custom_draw=draw_mux_labeled,
    custom_clip=clip_mux_custom,
)
net_arith.node(
    "fa",
    "",
    x=265,
    y=100,
    kind="custom",
    custom_draw=draw_fa_labeled,
    custom_clip=clip_fa_custom,
)

# Input and output pins represented as text-only ports
net_arith.node(
    "sel", "Select Lines\n(S_1, S_0)", x=145, y=40, kind="text", label_pos="below"
)
net_arith.node("ai", "Input A_i", x=265, y=160, kind="text", label_pos="above")
net_arith.node("cin", "Carry In (C_i)", x=265, y=40, kind="text", label_pos="below")
net_arith.node("di", "Output D_i", x=355, y=100, kind="text", label_pos="right")
net_arith.node("cout", "Carry Out (C_i+1)", x=355, y=40, kind="text", label_pos="right")

# Links connecting the components
net_arith.link("sel", "mux")
net_arith.link("mux", "fa", label="Y_i")
net_arith.link("ai", "fa")
net_arith.link("cin", "fa")
net_arith.link("fa", "di")
net_arith.link("fa", "cout")
story.extend(net_arith.as_flowable())
sp(10)

# -- Q1 (d) 2024 --
chap_box(
    "Q1. d) Give a classification of shift micro-operations. An 8-bit register contains the binary value 1001 1100. What is the register value after an arithmetic shift right? Starting from the initial number 1001 1100, determine the register value after an arithmetic shift left, and state whether there is an overflow. [10 Marks] (June 2024)\n"
    "[AND]\n"
    "Q1. e) What do you mean by Shift micro-operation? Classify shift micro-operations. Give suitable example for each class. [10 Marks] (May/June 2023)"
)
section("Classification of Shift Micro-operations")
definition(
    "<b>Shift Micro-operations:</b> Operations that shift the binary information stored in a register "
    "either to the left or to the right. They are used for serial data transfer, bit manipulation, "
    "and signed/unsigned arithmetic operations."
)
body(
    "Shift micro-operations are classified into three primary classes:"
)
info_table(
    ["Shift Type", "Operations", "Behavior of Ends", "Applications"],
    [
        [
            "Logical Shift",
            "shl, shr",
            "Inserts 0 into the vacated end. Discards the bit shifted out.",
            "Unsigned arithmetic, bit clearing.",
        ],
        [
            "Circular Shift",
            "cil, cir",
            "Wraps the shifted-out bit around to enter the opposite vacated end. No bits are lost.",
            "Bit rotation, serial communication.",
        ],
        [
            "Arithmetic Shift",
            "asl, asr",
            "Right shift preserves MSB (sign bit). Left shift inserts 0 in LSB and checks for sign changes (overflow).",
            "Signed integer multiplication/division by 2.",
        ],
    ],
)

section("Numerical Problems with 8-bit Value: 1001 1100")
body(
    "Let register R contain the 8-bit signed value <b>R = 1001 1100<sub>2</sub></b> (equivalent to -100 in 2's complement)."
)
bullet(
    [
        "<b>1. Arithmetic Shift Right (asr):</b><br/>"
        "All bits shift right. The sign bit (MSB, which is 1) is replicated and copied into the MSB position. "
        "The LSB (0) is discarded.<br/>"
        "• Initial: <b>1</b>001 1100<br/>"
        "• After ASR: <b>1100 1110</b> (equivalent to -50 in 2's complement).",
        "<b>2. Arithmetic Shift Left (asl):</b><br/>"
        "All bits shift left. The MSB (1) is shifted out, and a 0 is inserted into the vacated LSB position.<br/>"
        "• Initial: <b>1</b>001 1100<br/>"
        "• After ASL: <b>0011 1000</b> (equivalent to +56 in 2's complement).",
        "<b>3. Overflow Check:</b><br/>"
        "An overflow occurs in ASL if the sign bit changes during the shift.<br/>"
        "• Sign bit before shift: <b>R<sub>7</sub> = 1</b> (negative number).<br/>"
        "• Sign bit after shift: <b>R<sub>7</sub>' = 0</b> (positive number).<br/>"
        "• Overflow formula: <b>V = R<sub>7</sub> XOR R<sub>6</sub> = 1 XOR 0 = 1</b>. "
        "Since V = 1, an <b>overflow has occurred</b>. The value +56 is mathematically incorrect because the "
        "ideal result -200 cannot fit in an 8-bit signed register (which is limited to [-128, +127]).",
    ]
)
sp(10)

# -- Q1 (d) 2023 --
chap_box(
    "Q1. d) The eight bit registers AR, BR, CR and DR initially have the following values:\n"
    " AR=11110010\n"
    " BR=11111111\n"
    " CR=10111001\n"
    " DR=11101010\n"
    "Determine the 8 bit values in each register after the execution of the following sequence of micro-operations?\n"
    " AR <- AR + BR\n"
    " CR <- CR ^ DR, BR <- BR + 1\n"
    " AR <- AR - CR\n"
    "[10 Marks] (May/June 2023)"
)
section("Register Execution Trace Analysis")
body(
    "We track the values in registers AR, BR, CR, and DR step-by-step. The registers are 8-bit, "
    "meaning any overflow or carry bit beyond the 8th bit (MSB) is discarded."
)

section("Initial State")
bullet(
    [
        "<b>AR</b> = 11110010 &sub; 242<sub>10</sub>",
        "<b>BR</b> = 11111111 &sub; 255<sub>10</sub>",
        "<b>CR</b> = 10111001 &sub; 185<sub>10</sub>",
        "<b>DR</b> = 11101010 &sub; 234<sub>10</sub>",
    ]
)

section("Step 1: AR &larr; AR + BR")
body(
    "We add the binary values of AR and BR: <br/>"
    "&nbsp;&nbsp;&nbsp;&nbsp;1111 0010 (AR)<br/>"
    "&nbsp;&nbsp;+ 1111 1111 (BR)<br/>"
    "&nbsp;&nbsp;-----------<br/>"
    "&nbsp;1 1111 0001 (Sum = 497<sub>10</sub>)<br/>"
    "Since AR is an 8-bit register, the carry out (1) is discarded. AR becomes <b>11110001</b> (241<sub>10</sub>)."
)

section("Step 2: CR &larr; CR ^ DR, BR &larr; BR + 1")
body(
    "These two micro-operations occur simultaneously in parallel (as denoted by the comma):"
)
bullet(
    [
        "<b>CR &larr; CR ^ DR (Bitwise XOR):</b><br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;1011 1001 (CR)<br/>"
        "&nbsp;&nbsp;^ 1110 1010 (DR)<br/>"
        "&nbsp;&nbsp;-----------<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;0101 0011 (Result = 83<sub>10</sub>)<br/>"
        "So CR becomes <b>01010011</b>.",
        "<b>BR &larr; BR + 1 (Increment):</b><br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;1111 1111 (BR)<br/>"
        "&nbsp;&nbsp;+ 0000 0001 (1)<br/>"
        "&nbsp;&nbsp;-----------<br/>"
        "&nbsp;1 0000 0000 (Result = 256<sub>10</sub>)<br/>"
        "Discarding the 9th bit (carry), BR becomes <b>00000000</b>.",
    ]
)

section("Step 3: AR &larr; AR - CR")
body(
    "Subtraction is performed using 2's complement arithmetic: <b>AR &larr; AR + (2's complement of CR)</b>.<br/>"
    "• CR = 01010011<br/>"
    "• 1's complement of CR = 10101100<br/>"
    "• 2's complement of CR = 10101101 (equivalent to -83 in 2's complement)<br/>"
    "Now we add AR and the 2's complement of CR:<br/>"
    "&nbsp;&nbsp;&nbsp;&nbsp;1111 0001 (AR)<br/>"
    "&nbsp;&nbsp;+ 1010 1101 (2's complement of CR)<br/>"
    "&nbsp;&nbsp;-----------<br/>"
    "&nbsp;1 1001 1110 (Sum = 158<sub>10</sub>)<br/>"
    "Discarding the carry out (1), AR becomes <b>10011110</b>."
)

section("Final Values in Registers")
info_table(
    ["Register", "Binary Value (8-bit)", "Decimal Equivalent", "Status / Notes"],
    [
        ["AR", "10011110", "158", "Modified in Step 1 and Step 3."],
        ["BR", "00000000", "0", "Incremented in Step 2 (overflowed to 0)."],
        ["CR", "01010011", "83", "Modified via bitwise XOR in Step 2."],
        ["DR", "11101010", "234", "Unchanged throughout the sequence."],
    ]
)
sp(10)

# -- Q1 (e) --
chap_box(
    "Q1. e) [OR] Starting from an initial value of R1 = 11011101, determine the sequence of binary values in R after a logical shift-left, followed by a circular shift-right, followed by a logical shift-right and a circular shift-left. [10 Marks]"
)
section("Step-by-Step Binary Shift Trace")
body(
    "Let us trace the bit transformations of register R (8-bit) starting from the initial value <b>R1 = 11011101</b>."
)

info_table(
    [
        "Step",
        "Shift Operation",
        "Calculation Details & Bit Shift",
        "New Value of R",
        "Carry (Out)",
    ],
    [
        [
            "Initial",
            "-",
            "Starting binary pattern in register R.",
            "<b>1101 1101</b>",
            "-",
        ],
        [
            "1",
            "Logical Shift-Left (shl)",
            "All bits shift left. The MSB (1) is discarded. The vacated LSB position is filled with 0.",
            "<b>1011 1010</b>",
            "1",
        ],
        [
            "2",
            "Circular Shift-Right (cir)",
            "All bits shift right. The LSB (0) wraps around and enters the MSB position. No bits lost.",
            "<b>0101 1101</b>",
            "0",
        ],
        [
            "3",
            "Logical Shift-Right (shr)",
            "All bits shift right. The LSB (1) is discarded. The vacated MSB position is filled with 0.",
            "<b>0010 1110</b>",
            "1",
        ],
        [
            "4",
            "Circular Shift-Left (cil)",
            "All bits shift left. The MSB (0) wraps around and enters the LSB position. No bits lost.",
            "<b>0101 1100</b>",
            "0",
        ],
    ],
    col_widths=[50, 140, 173, 90, 40],
)
sp(10)

# -- Q1 (e) 2024 --
chap_box(
    "Q1. e) [OR] Discuss the function of following computer registers:\n i) Program counter\n ii) Accumulator\n iii) MAR\n iv) MBR\n v) Instruction register\n[10 Marks] (June 2024)\n"
    "[AND]\n"
    "Q1. c) Write the uses of AC, MAR and MDR registers. [4 Marks] (June 2023)"
)
section("Functional Roles of Key CPU Registers")
info_table(
    ["Register Name", "Abbr.", "Primary Functions", "Interfacing &amp; Datapath Context"],
    [
        [
            "Program Counter",
            "PC",
            "Holds the memory address of the next instruction to be fetched and executed. It manages sequential execution flow.",
            "Feeds MAR during instruction fetch. Increments automatically by 1 (or instruction length) after each fetch.",
        ],
        [
            "Accumulator",
            "AC",
            "Serves as the primary general-purpose register that holds intermediate operands and execution results of ALU operations.",
            "Connected directly to one input of the ALU and receives the final output from the ALU.",
        ],
        [
            "Memory Address Register",
            "MAR",
            "Holds the physical address in memory that is currently being accessed for a read or write operation.",
            "Connected to the address bus lines. Loaded from PC (during fetch) or Instruction Address field (during execution).",
        ],
        [
            "Memory Buffer Register",
            "MBR",
            "Holds the data word read from memory or the data word ready to be written to memory. (Also known as Memory Data Register - MDR).",
            "Connected to the data bus lines. Acts as a high-speed buffer between the slow main memory and fast CPU.",
        ],
        [
            "Instruction Register",
            "IR",
            "Holds the opcode and operands of the instruction currently being decoded and executed by the control unit.",
            "Loaded from MBR during instruction fetch. Its output feeds the instruction decoder in the Control Unit.",
        ],
    ],
    col_widths=[110, 45, 200, 138],
)
br()


# =============================================================================
#  QUESTION 2: CO2
# =============================================================================
part_box("QUESTION 2 -- CO2 DATA REPRESENTATION & CONTROL")

# -- Q2 (a) 2023 --
chap_box(
    "Q2. a) Define the terms Micro-program, Micro-instruction and Micro-operation ?\n"
    "[3 Marks] (May/June 2023)"
)
section("Definitions of Microprogramming Concepts")
definition(
    "<b>1. Micro-operation:</b> An elementary hardware operation performed on data stored in one or "
    "more registers during a single clock pulse (e.g., addition, shifting, loading, clearing). Micro-operations "
    "are the low-level building blocks of instruction execution."
)
definition(
    "<b>2. Micro-instruction:</b> A control word stored in the control memory (ROM) that specifies one or "
    "more micro-operations to be executed simultaneously. It also contains bits to determine the address of "
    "the next micro-instruction."
)
definition(
    "<b>3. Micro-program:</b> A sequence of micro-instructions that coordinates the execution of a machine-language "
    "instruction (like ADD, SUB, etc.) or handles system events (like interrupts). It acts as software control "
    "for the hardware datapath."
)
sp(10)

# -- Q2 (a) --
chap_box(
    "Q2. a) Find the decimal value of exponent in excess 127 form, in IEEE 754 single precision representation of a binary number (1101 0000.0001)<sub>2</sub>. [3 Marks]"
)
section("IEEE 754 Conversion Process")
body(
    "We are given the fractional binary value: <b>(1101 0000.0001)<sub>2</sub></b>. Let us represent this in IEEE 754 format."
)
bullet(
    [
        "<b>Step 1: Normalize the binary number.</b><br/>"
        "Shift the radix point to the left so that there is exactly one non-zero digit to its left:<br/>"
        "1101 0000.0001 = <b>1.101000000001<sub>2</sub> × 2<sup>7</sup></b> (shifted left by 7 places)",
        "<b>Step 2: Identify the actual exponent.</b><br/>"
        "The actual exponent <i>e</i> is <b>7</b>.",
        "<b>Step 3: Calculate the biased exponent (excess-127).</b><br/>"
        "IEEE 754 single-precision format uses a bias of 127 for the exponent.<br/>"
        "Biased Exponent = <i>e</i> + Bias = 7 + 127 = <b>134</b>.",
        "<b>Step 4: Express in binary.</b><br/>"
        "The biased exponent 134 in 8-bit binary is <b>10000110<sub>2</sub></b>.",
    ]
)

packet_format(
    "IEEE 754 Single Precision Field Layout for (1101 0000.0001)<sub>2</sub>",
    [
        ("S", 1),
        ("Exponent (E)", 8),
        ("Mantissa (M)", 23),
    ],
)
body(
    "<b>Field Values for this representation:</b><br/>"
    "• <b>Sign (S):</b> 0 (representing positive value)<br/>"
    "• <b>Exponent (E):</b> 134 (binary 10000110)<br/>"
    "• <b>Mantissa (M):</b> 10100000000100000000000 (fractional part, padded to 23 bits)"
)

# -- Q2 (b) / Q2 (a) [OVERLAPPED] --
chap_box(
    "Q2. b) Compare hardwired and micro-programmed control units. [4 Marks] (June 2022)\n"
    "[AND]\n"
    "Q2. a) Differentiate Hardwired and micro-programmed control units. [3 Marks] (June 2024)\n"
    "[AND]\n"
    "Q2. b) Differentiate hardwired and micro programmed control units. [4 Marks] (May/June 2023)"
)
section("Comparison Table")
info_table(
    ["Property", "Hardwired Control Unit", "Micro-programmed Control Unit"],
    [
        [
            "Implementation",
            "Built using logic gates, flip-flops, and combinational hardware decoders.",
            "Built using control memory (ROM) where microprograms are stored.",
        ],
        [
            "Operating Speed",
            "Very fast, since control signals are generated via logic propagation delays.",
            "Slower, as every instruction requires fetching microinstructions from ROM.",
        ],
        [
            "Design Flexibility",
            "Very rigid. Any modification requires physical rewiring and redesigning the board.",
            "Highly flexible. Modifications can be done by simply updating the microcode in ROM.",
        ],
        [
            "Complexity",
            "Increases drastically with larger instruction sets (leads to unmanageable gates).",
            "Structured and systematic. Easily handles complex and large instruction sets.",
        ],
        [
            "Instruction Architecture",
            "Mainly used in RISC (Reduced Instruction Set Computer) processors.",
            "Mainly used in CISC (Complex Instruction Set Computer) processors.",
        ],
    ],
)
sp(10)

# -- Q2 (c) --
chap_box(
    "Q2. c) Add two numbers 5 and 4 in 2's complement format. Assume four bit registers are used. Check for overflow. [4 Marks]"
)
section("2's Complement Addition & Overflow Analysis")
body(
    "In a 4-bit signed register, the range of representable numbers using 2's complement is "
    "[-2<sup>3</sup>, 2<sup>3</sup> - 1] = <b>[-8, +7]</b>."
)
bullet(
    [
        "<b>Representing +5 in 4-bit:</b> 0101<sub>2</sub>",
        "<b>Representing +4 in 4-bit:</b> 0100<sub>2</sub>",
    ]
)

section("Binary Addition Steps")
code_block("""
   Carry-in:   1 0 0 0
   Operand A:   0 1 0 1   (+5)
   Operand B: + 0 1 0 0   (+4)
   ---------------------
   Sum:         1 0 0 1
   Carry-out:   0
""")

section("Overflow Verification Methods")
bullet(
    [
        "<b>Method 1: Sign Discrepancy.</b> We added two positive numbers (MSBs = 0) and "
        "obtained a negative result (MSB = 1, which represents -7 in 2's complement). This sign inversion "
        "proves that a signed overflow has occurred.",
        "<b>Method 2: Carry XOR.</b> The carry-in to the sign bit (MSB) is <b>C<sub>in</sub> = 1</b> (from Bit 2 addition). "
        "The carry-out of the sign bit is <b>C<sub>out</sub> = 0</b>.<br/>"
        "Overflow Flag V = C<sub>in</sub> XOR C<sub>out</sub> = 1 XOR 0 = <b>1</b>. Since V = 1, overflow is asserted.",
        "<b>Mathematical Reason:</b> The algebraic sum is +9, but the maximum positive number representable in "
        "a 4-bit signed register is +7. Thus, +9 exceeds the limit, causing the bit to spill into the sign position.",
    ]
)
sp(10)

# -- Q2 (c) 2024 --
chap_box(
    "Q2. c) Explain the process of 2's complement method of subtraction with a suitable example. [4 Marks] (June 2024)"
)
section("2's Complement Subtraction Method")
body(
    "Subtraction of two signed binary numbers in 2's complement representation is accomplished through "
    "addition. To perform <b>A - B</b>:"
)
bullet(
    [
        "<b>Step 1:</b> Find the 2's complement of the subtrahend B (invert all bits of B and add 1). This yields -B.",
        "<b>Step 2:</b> Add this 2's complement value to the minuend A, i.e. compute <b>S = A + (2's complement of B)</b>.",
        "<b>Step 3:</b> Inspect the carry-out (C<sub>out</sub>) from the sign bit position:<br/>"
        "• <b>If C<sub>out</sub> = 1:</b> The result is positive. Discard the carry-out; the sum is the correct magnitude.<br/>"
        "• <b>If C<sub>out</sub> = 0:</b> The result is negative and is in its 2's complement form. To find its decimal value, "
        "take the 2's complement of the sum and prefix a negative sign.",
    ]
)

section("Subtraction Examples using 6-bit registers")
bullet(
    [
        "<b>Example 1: Subtract 4 from 9 (Positive Result: 9 - 4 = +5)</b><br/>"
        "Minuend A = +9 = 001001<sub>2</sub> | Subtrahend B = +4 = 000100<sub>2</sub><br/>"
        "• 2's complement of B (+4): 111011<sub>2</sub> + 1 = 111100<sub>2</sub> (-4)<br/>"
        "• Add: 001001 + 111100 = <b>(1) 000101<sub>2</sub></b><br/>"
        "• Analysis: Carry-out is 1. Discard it. Result is 000101<sub>2</sub> = <b>+5</b>. (Correct)",
        "<b>Example 2: Subtract 9 from 4 (Negative Result: 4 - 9 = -5)</b><br/>"
        "Minuend A = +4 = 000100<sub>2</sub> | Subtrahend B = +9 = 001001<sub>2</sub><br/>"
        "• 2's complement of B (+9): 110110<sub>2</sub> + 1 = 110111<sub>2</sub> (-9)<br/>"
        "• Add: 000100 + 110111 = <b>(0) 111011<sub>2</sub></b><br/>"
        "• Analysis: Carry-out is 0. Result is negative and is stored as 111011. Its magnitude is "
        "2's complement of 111011 = 000100 + 1 = 000101<sub>2</sub> = 5. So the result is <b>-5</b>. (Correct)",
    ]
)
sp(10)

# -- Q2 (d) --
chap_box(
    "Q2. d) Use BOOTH method to multiply two numbers +7 and +3. Also write steps of multiplication. [10 Marks] (June 2022)\n"
    "[AND]\n"
    "Q2. e) Show the step by step procedure of multiplication when following two numbers is multiplied by Booth method. (+15) X (-13). [10 Marks] (May/June 2023)"
)
section("Booth's Multiplication Principles")
body(
    "Booth's algorithm multiplies signed integers in 2's complement format by scanning pairs "
    "of multiplier bits (Q<sub>0</sub>, Q<sub>-1</sub>) and performing additions/subtractions followed by arithmetic right shifts. "
    "We use 5-bit registers to prevent overflow since the product (+21) requires 6 bits."
)
bullet(
    [
        "<b>Multiplicand (M):</b> +7 = 00111<sub>2</sub>",
        "<b>Negative Multiplicand (-M):</b> -7 = 11001<sub>2</sub> (2's complement of M)",
        "<b>Multiplier (Q):</b> +3 = 00011<sub>2</sub>",
        "<b>Initial Accumulator (A):</b> 00000<sub>2</sub>",
        "<b>Initial Carry bit (Q<sub>-1</sub>):</b> 0",
        "<b>Initial Step Count:</b> n = 5",
    ]
)

section("Booth's Multiplication Trace Table")
info_table(
    [
        "Cycle",
        "Q0 Q-1",
        "Operation performed",
        "Accumulator (A)",
        "Multiplier (Q)",
        "Q-1",
        "Count",
    ],
    [
        ["0", "-", "Initial State", "00000", "00011", "0", "5"],
        [
            "1",
            "1 0",
            "A <- A - M (Subtract)",
            "11001\n11100",
            "00011\n10001",
            "0\n1",
            "4",
        ],
        ["2", "1 1", "No-op (Arithmetic Shift Right)", "11110", "01000", "1", "3"],
        [
            "3",
            "0 1",
            "A <- A + M (Add)\nArithmetic Shift Right",
            "00101\n00010",
            "01000\n10100",
            "1\n0",
            "2",
        ],
        ["4", "0 0", "No-op (Arithmetic Shift Right)", "00001", "01010", "0", "1"],
        ["5", "0 0", "No-op (Arithmetic Shift Right)", "00000", "10101", "0", "0"],
    ],
)

section("Verification of Result")
body(
    "The 10-bit binary product is stored in the register pair (A, Q) = <b>00000 10101</b>.<br/>"
    "Converting 0000010101<sub>2</sub> to decimal: 16 + 4 + 1 = <b>+21</b>. The result is correct (+7 × +3 = +21)."
)
sp(10)

section("Booth's Multiplication Trace for (+15) X (-13) (May/June 2023)")
body(
    "We multiply the two signed numbers: Multiplicand <b>M = +15</b> and Multiplier <b>Q = -13</b>. "
    "To represent +15 and -13 without overflow, we use 6-bit registers (allowing values in [-32, +31]):"
)
bullet(
    [
        "<b>Multiplicand (M):</b> +15 = 001111<sub>2</sub>",
        "<b>Negative Multiplicand (-M):</b> -15 = 110001<sub>2</sub> (2's complement of M)",
        "<b>Multiplier (Q):</b> -13 = 110011<sub>2</sub>",
        "<b>Initial Accumulator (A):</b> 000000<sub>2</sub>",
        "<b>Initial Carry bit (Q<sub>-1</sub>):</b> 0",
        "<b>Initial Step Count:</b> n = 6",
    ]
)

info_table(
    [
        "Cycle",
        "Q0 Q-1",
        "Operation performed",
        "Accumulator (A)",
        "Multiplier (Q)",
        "Q-1",
        "Count",
    ],
    [
        ["0", "-", "Initial State", "000000", "110011", "0", "6"],
        [
            "1",
            "1 0",
            "A &larr; A - M (Subtract M)\nArithmetic Shift Right",
            "110001\n111000",
            "110011\n111001",
            "0\n1",
            "5",
        ],
        [
            "2",
            "1 1",
            "No-op (Arithmetic Shift Right)",
            "111100",
            "011100",
            "1",
            "4",
        ],
        [
            "3",
            "0 1",
            "A &larr; A + M (Add M)\nArithmetic Shift Right",
            "001011\n000101",
            "011100\n101110",
            "1\n0",
            "3",
        ],
        [
            "4",
            "0 0",
            "No-op (Arithmetic Shift Right)",
            "000010",
            "110111",
            "0",
            "2",
        ],
        [
            "5",
            "1 0",
            "A &larr; A - M (Subtract M)\nArithmetic Shift Right",
            "110011\n111001",
            "110111\n111011",
            "0\n1",
            "1",
        ],
        [
            "6",
            "1 1",
            "No-op (Arithmetic Shift Right)",
            "111100",
            "111101",
            "1",
            "0",
        ],
    ],
)

section("Result Verification for (+15) X (-13)")
body(
    "The 12-bit binary product is stored in the register pair (A, Q) = <b>111100111101</b>.<br/>"
    "• MSB is 1, so the result is negative.<br/>"
    "• Taking the 2's complement of 111100111101:<br/>"
    "&nbsp;&nbsp;1's complement = 000011000010<br/>"
    "&nbsp;&nbsp;2's complement = 000011000011 = 128 + 64 + 2 + 1 = <b>+195</b>.<br/>"
    "Therefore, the product is <b>-195</b>. This is correct since (+15) &times; (-13) = <b>-195</b>."
)
sp(10)

# -- Q2 (d) --


chap_box(
    "Q2. d) Discuss IEEE representations of floating point numbers. Convert the decimal (32.75)10 in single precision IEEE format. [10 Marks] (June 2024)\n"
    "[AND]\n"
    "Q2. d) How to represent fractional numbers in computer? Discuss IEEE 32-bit single precision format. Convert the decimal (32.75)10 in single precision IEEE format. [10 Marks] (May/June 2023)"
)
section("Representation of Fractional Numbers in Computers")
body(
    "Computers typically represent fractional/real numbers in two primary formats:"
)
bullet(
    [
        "<b>1. Fixed-Point Representation:</b> A specific number of bits is allocated for the integer part "
        "and a specific number of bits for the fractional part. The binary point is assumed to be at a fixed position. "
        "It is simple to implement but has a very limited range of representable numbers (e.g., Q-formats).",
        "<b>2. Floating-Point Representation:</b> The binary point is allowed to float to accommodate very large or "
        "very small numbers. It represents numbers in a scientific notation format: <b>M &times; R<sup>E</sup></b> "
        "(where M is mantissa, R is radix/base, and E is exponent). This is standardized internationally by the IEEE 754 standard.",
    ]
)

section("IEEE 754 Floating Point Representations")
body(
    "The IEEE 754 standard is the most widely used specification for representing real numbers in binary format. "
    "It defines two primary formats based on word size:"
)
bullet(
    [
        "<b>1. Single Precision (32-bit):</b> Consists of 1 sign bit (S), 8 biased exponent bits (E), and 23 fraction/mantissa bits (M). "
        "The exponent bias is <b>127</b>. Formula: <b>V = (-1)<sup>S</sup> &times; 1.M &times; 2<sup>E - 127</sup></b>.",
        "<b>2. Double Precision (64-bit):</b> Consists of 1 sign bit (S), 11 biased exponent bits (E), and 52 fraction/mantissa bits (M). "
        "The exponent bias is <b>1023</b>. Formula: <b>V = (-1)<sup>S</sup> &times; 1.M &times; 2<sup>E - 1023</sup></b>.",
    ]
)

packet_format(
    "IEEE 754 Single-Precision Standard fields mapping",
    [
        ("S", 1),
        ("Biased Exponent (8 bits)", 8),
        ("Fraction / Mantissa (23 bits)", 23),
    ],
)

section("Conversion of (32.75)10 into Single Precision Format")
bullet(
    [
        "<b>Step 1: Sign bit detection.</b> Since the number is positive, <b>S = 0</b>.",
        "<b>Step 2: Convert to binary.</b><br/>"
        "• Integer part: 32 = 100000<sub>2</sub><br/>"
        "• Fractional part: 0.75 = 0.5 + 0.25 = 2<sup>-1</sup> + 2<sup>-2</sup> = 0.11<sub>2</sub><br/>"
        "• Combined binary value: <b>100000.11<sub>2</sub></b>",
        "<b>Step 3: Normalize the binary value.</b> Shift the radix point left by 5 positions so there is exactly "
        "one non-zero digit to the left of the point:<br/>"
        "100000.11 = <b>1.0000011<sub>2</sub> &times; 2<sup>5</sup></b><br/>"
        "• Actual exponent <i>e</i> = 5.",
        "<b>Step 4: Calculate the biased exponent (E).</b><br/>"
        "For single-precision, bias is 127.<br/>"
        "Biased Exponent E = e + 127 = 5 + 127 = <b>132</b>.<br/>"
        "Converting 132 to 8-bit binary: <b>10000100<sub>2</sub></b>.",
        "<b>Step 5: Determine the mantissa (M).</b><br/>"
        "The fractional part is 0000011. Padded to 23 bits, it becomes: <b>0000 0110 0000 0000 0000 000</b>.",
    ]
)

section("Resulting 32-bit Single Precision Layout")
info_table(
    ["Sign (S)", "Biased Exponent (E)", "Fraction / Mantissa (M)"],
    [
        ["0", "10000100", "00000110000000000000000"],
    ],
)
body(
    "In hexadecimal representation, grouping the 32 bits `0100 0010 0000 0300 0000 0000 0000 0000` (binary `01000010000000110000000000000000`) "
    "gives: <b>42030000<sub>16</sub></b>."
)
sp(10)

# -- Q2 (e) / Q2 (b) [OVERLAPPED] --
chap_box(
    "Q2. e) [OR] What are the three ways to represent negative numbers? Elaborate them. Find range of numbers for n bit register in these three formats. [10 Marks] (June 2022)\n"
    "[AND]\n"
    "Q2. b) Explain signed magnitude, signed 1's complement and signed 2's complement representations of signed numbers. What is the range of these numbers for 8 bit register? [4 Marks] (June 2024)"
)
section("Negative Number Representations")
body(
    "There are three primary ways to represent negative integers in a digital computer. "
    "In all formats, the most significant bit (MSB) is the sign bit (0 = positive, 1 = negative)."
)

bullet(
    [
        "<b>1. Sign-Magnitude Representation:</b> The MSB represents the sign. The remaining (n - 1) bits "
        "represent the absolute magnitude of the number.<br/>"
        "• Example (+5, n=4): 0101<sub>2</sub> | Example (-5, n=4): 1101<sub>2</sub><br/>"
        "• <i>Range:</i> <b>[-(2<sup>n-1</sup> - 1), +(2<sup>n-1</sup> - 1)]</b>",
        "<b>2. 1's Complement Representation:</b> Positive values are identical to sign-magnitude. "
        "A negative value is represented by inverting (complementing) every single bit of its positive equivalent.<br/>"
        "• Example (+5, n=4): 0101<sub>2</sub> | Example (-5, n=4): 1010<sub>2</sub><br/>"
        "• <i>Range:</i> <b>[-(2<sup>n-1</sup> - 1), +(2<sup>n-1</sup> - 1)]</b>",
        "<b>3. 2's Complement Representation:</b> Positive values are identical. A negative value is "
        "represented by adding 1 to the least significant bit (LSB) of its 1's complement representation.<br/>"
        "• Example (+5, n=4): 0101<sub>2</sub> | Example (-5, n=4): 1010<sub>2</sub> + 1 = 1011<sub>2</sub><br/>"
        "• <i>Range:</i> <b>[-2<sup>n-1</sup>, +(2<sup>n-1</sup> - 1)]</b>",
    ]
)

section("Comparison Summary")
info_table(
    ["Format", "Number of Zeros", "Math Operations Complexity", "Range (for n=8)"],
    [
        [
            "Sign-Magnitude",
            "2 (+0 and -0)",
            "Complex: needs sign checks and shifts",
            "-127 to +127",
        ],
        [
            "1's Complement",
            "2 (+0 and -0)",
            "Moderate: needs end-around carry",
            "-127 to +127",
        ],
        [
            "2's Complement",
            "1 (Unique zero)",
            "Simple: subtraction is just addition",
            "-128 to +127",
        ],
    ],
)
br()

# -- Q2 (e) [OR] 2024 --
chap_box(
    "Q2. e) [OR] Perform the arithmetic operations below with binary numbers and with negative numbers in signed 2's complement representation. Use seven bit to accommodate each number together with its sign. In each case, determine if there is an overflow by checking the carries into and out of the sign bit position.\n i. (+35) + (+40)\n ii. (-35) + (-40)\n[10 Marks] (June 2024)\n"
    "[AND]\n"
    "Q2. c) Perform the arithmetic operations below with binary numbers and with negative numbers in signed 2's complement representation. Use seven bit to accommodate each number together with its sign. In each case, determine if there is an overflow by checking the carries into and out of the sign bit position.\n i) (+35)+(+40)\n ii) (-35)+(-40)\n[4 Marks] (May/June 2023)"
)
section("Signed 2's Complement Overflow Verification (7-bit Registers)")
body(
    "In a 7-bit signed register, the MSB (Bit 6) is the sign bit. The range of representable numbers is:<br/>"
    "Range = [-2<sup>6</sup>, 2<sup>6</sup> - 1] = <b>[-64, +63]</b>."
)

section("Part i: (+35) + (+40)")
bullet(
    [
        "<b>Convert operands to 7-bit signed binary:</b><br/>"
        "• +35 in binary is 0100011<sub>2</sub> (MSB = 0, positive)<br/>"
        "• +40 in binary is 0101000<sub>2</sub> (MSB = 0, positive)",
    ]
)
code_block("""
   Carries:     1 0 0 0 0 0 0
   Operand A:   0 1 0 0 0 1 1   (+35)
   Operand B: + 0 1 0 1 0 0 0   (+40)
   --------------------------
   Sum:         1 0 0 1 0 1 1   (which is -53 in 2's complement)
""")
bullet(
    [
        "<b>Overflow Analysis:</b><br/>"
        "• The carry into the sign bit (Bit 6) is <b>C<sub>in</sub> = 1</b> (from Bit 5).<br/>"
        "• The carry out of the sign bit is <b>C<sub>out</sub> = 0</b>.<br/>"
        "• Overflow flag: <b>V = C<sub>in</sub> XOR C<sub>out</sub> = 1 XOR 0 = 1</b>.<br/>"
        "• Since V = 1, <b>an overflow occurred</b>.<br/>"
        "• <i>Mathematical confirmation:</i> The mathematical sum is +75. However, the maximum limit for "
        "a 7-bit signed register is +63. Since +75 exceeds +63, overflow occurs and the sum spills into "
        "the sign bit, making it look negative.",
    ]
)

section("Part ii: (-35) + (-40)")
bullet(
    [
        "<b>Convert operands to 7-bit signed binary (2's complement):</b><br/>"
        "• +35 = 0100011<sub>2</sub> | 1's complement = 1011100<sub>2</sub> | 2's complement (-35) = <b>1011101<sub>2</sub></b><br/>"
        "• +40 = 0101000<sub>2</sub> | 1's complement = 1010111<sub>2</sub> | 2's complement (-40) = <b>1011000<sub>2</sub></b>",
    ]
)
code_block("""
   Carries:     1 1 1 1 0 0 0
   Operand A:   1 0 1 1 1 0 1   (-35)
   Operand B: + 1 0 1 1 0 0 0   (-40)
   --------------------------
   Sum:         0 1 1 0 1 0 1   (which is +53 in 2's complement)
   Carry-out:   1
""")
bullet(
    [
        "<b>Overflow Analysis:</b><br/>"
        "• The carry into the sign bit (Bit 6) is <b>C<sub>in</sub> = 0</b>.<br/>"
        "• The carry out of the sign bit is <b>C<sub>out</sub> = 1</b>.<br/>"
        "• Overflow flag: <b>V = C<sub>in</sub> XOR C<sub>out</sub> = 0 XOR 1 = 1</b>.<br/>"
        "• Since V = 1, <b>an overflow occurred</b>.<br/>"
        "• <i>Mathematical confirmation:</i> The mathematical sum is -75. However, the minimum limit for "
        "a 7-bit signed register is -64. Since -75 is less than -64, it exceeds the negative limit and spills over, "
        "making it look positive.",
    ]
)
sp(10)


# =============================================================================
#  QUESTION 3: CO3
# =============================================================================
part_box("QUESTION 3 -- CO3 INSTRUCTION FORMATS & I/O")

# -- Q3 (a) --
chap_box(
    "Q3. a) Identify the operation described by following statements:\n DR <- M[SP]\n SP <- SP + 1\n[3 Marks]"
)
section("Micro-operation Analysis")
body("The given statements describe a <b>POP operation from a memory stack</b>.")
bullet(
    [
        "<b>Step 1: DR <- M[SP]:</b> The CPU reads the data word from the memory address currently pointed to "
        "by the Stack Pointer (SP) and transfers it into the Data Register (DR). This retrieves the item from the stack top.",
        "<b>Step 2: SP <- SP + 1:</b> The Stack Pointer is incremented by 1. Since SP is incremented after the read, "
        "the stack grows toward lower memory addresses during pushes (decr SP) and shrinks toward higher memory addresses "
        "during pops (incr SP). This is a post-increment stack organization.",
    ]
)
sp(10)

# -- Q3 (b) / Q3 (a) [OVERLAPPED] --
chap_box(
    "Q3. b) What do you mean by implied addressing mode? Give examples. [4 Marks] (June 2022)\n"
    "[AND]\n"
    "Q3. a) What do you mean by implied and immediate mode of addressing? Give suitable examples. [3 Marks] (June 2024)\n"
    "[AND]\n"
    "Q3. b) With the help of examples discuss Implied and Immediate addressing mode of the instruction. [4 Marks] (May/June 2023)"
)
section("Implied and Immediate Addressing Modes")
definition(
    "<b>Addressing Mode:</b> The method by which the instruction address field specifies the "
    "location of the operand (in registers, memory, or the instruction itself)."
)
bullet(
    [
        "<b>1. Implied Addressing Mode:</b> An addressing mode where the operand is implicitly specified within the "
        "instruction opcode itself. No address field or register select bits are included in the instruction format.<br/>"
        "• <i>Example 1:</i> `CMA` - Complements the Accumulator. The operand (AC) is implied by the instruction.<br/>"
        "• <i>Example 2:</i> `HLT` - Halts the CPU execution. No explicit operand is needed.",
        "<b>2. Immediate Addressing Mode:</b> An addressing mode where the operand is specified directly in the instruction "
        "address field itself (rather than its memory address). It is used to load constants.<br/>"
        "• <i>Example 1:</i> `ADD #5` - Adds the constant value 5 directly to the Accumulator.<br/>"
        "• <i>Example 2:</i> `MVI A, 10` - Moves the constant 10 into Register A.",
    ]
)

section("Comparison Summary with Assembly Examples")
info_table(
    ["Addressing Mode", "Instruction Format", "Operand Location", "Typical Example"],
    [
        [
            "Implied",
            "Opcode Only (e.g. CMA, CLC)",
            "Implicitly defined by CPU design (e.g., Accumulator, Carry Flag)",
            "<b>CMA</b> (Complement Accumulator)",
        ],
        [
            "Immediate",
            "Opcode + Operand Value (e.g., ADD #5)",
            "Stored directly inside the instruction's address field",
            "<b>ADD #25</b> (Add 25 to Accumulator)",
        ],
    ],
)
sp(10)

# -- Q3 (b) 2024 --
chap_box(
    "Q3. b) What is difference between a direct and an indirect address instruction? How many references to the memory are needed for each type of instruction to bring an operand in to a processor register? [4 Marks] (June 2024)"
)
section("Direct vs. Indirect Address Instructions")
body(
    "Instructions specify the address of the operand in memory. The key differences lie in how "
    "the CPU determines the final <b>Effective Address (EA)</b> of the operand:"
)
bullet(
    [
        "<b>1. Direct Address Instruction:</b> The instruction's address field contains the actual effective address of "
        "the operand. The CPU directly accesses this address to fetch the data.<br/>"
        "• <i>Formula:</i> <b>EA = Address Field Value (ADR)</b><br/>"
        "• <i>Memory References:</i> **1 reference** (to read the operand from memory location EA). "
        "*(Note: 1 fetch cycle reference is also needed to retrieve the instruction itself, making it 2 references total).* ",
        "<b>2. Indirect Address Instruction:</b> The instruction's address field contains the address of a memory location "
        "where the actual effective address of the operand is stored. The CPU must first read the address from memory, "
        "and then access that address to fetch the operand.<br/>"
        "• <i>Formula:</i> <b>EA = M[ADR]</b><br/>"
        "• <i>Memory References:</i> **2 references** (first memory read to retrieve the effective address from memory location ADR, "
        "and a second memory read to fetch the operand from location EA). "
        "*(Note: Including the instruction fetch, this requires 3 memory references total).* ",
    ]
)

section("Addressing Mode Comparison Matrix")
info_table(
    ["Addressing Scheme", "Opcode Mode Bit (I)", "Formula", "Memory Read Cycles to fetch Operand", "Complexity"],
    [
        ["Direct Address", "I = 0", "EA = ADR", "1 Memory Reference", "Fast, simple, limited memory range"],
        ["Indirect Address", "I = 1", "EA = M[ADR]", "2 Memory References", "Slower, supports large address pointers"],
    ],
)
sp(10)

# -- Q3 (c) --
chap_box(
    "Q3. c) Write Algorithm for conversion of Infix to Postfix (RPN) Notation. [4 Marks] (June 2022)\n"
    "[AND]\n"
    "Q3. e) [OR] Write algorithm of conversion from infix to postfix (RPN). Convert the following expression in to RPN form:\n"
    " A*[B+C*(D+E)]/F*(G+H)\n"
    "[10 Marks] (May/June 2023)"
)
section("Shunting-Yard Algorithm for RPN")
body(
    "To convert an infix mathematical expression to postfix/Reverse Polish Notation (RPN), "
    "we use the stack-based Shunting-yard algorithm:"
)
bullet(
    [
        "<b>1.</b> Initialize an empty stack for operators and an empty list/string for the output.",
        "<b>2.</b> Read the infix expression tokens from left to right:",
        "   <b>a.</b> If the token is an <b>operand</b> (variable or number), append it to the output directly.",
        "   <b>b.</b> If the token is a <b>left parenthesis '('</b>, push it onto the operator stack.",
        "   <b>c.</b> If the token is a <b>right parenthesis ')'</b>, pop operators from the stack to the output "
        "until a '(' is encountered. Discard both parentheses.",
        "   <b>d.</b> If the token is an <b>operator</b> (+, -, *, /):",
        "      • Pop operators with <i>greater or equal precedence</i> from stack to the output.",
        "      • Push the new operator onto the stack.",
        "<b>3.</b> Once the expression is scanned, pop all remaining operators from the stack to the output.",
    ]
)
sp(10)

section("Step-by-Step Trace for A * [ B + C * ( D + E ) ] / F * ( G + H )")
body(
    "Let us trace the Shunting-yard algorithm for the infix expression: <b>A * [ B + C * ( D + E ) ] / F * ( G + H )</b>. "
    "Note that square brackets '[' and ']' behave exactly like parentheses '(' and ')'."
)

info_table(
    ["Token", "Type", "Action taken", "Operator Stack", "Postfix Output String"],
    [
        ["A", "Operand", "Append to Output", "[]", "A"],
        ["*", "Operator", "Push to Stack", "[*]", "A"],
        ["[", "Left Paren", "Push to Stack", "[*, (]", "A"],
        ["B", "Operand", "Append to Output", "[*, (]", "A B"],
        ["+", "Operator", "Push to Stack", "[*, (, +]", "A B"],
        ["C", "Operand", "Append to Output", "[*, (, +]", "A B C"],
        ["*", "Operator", "Push to Stack (higher precedence than +)", "[*, (, +, *]", "A B C"],
        ["(", "Left Paren", "Push to Stack", "[*, (, +, *, (]", "A B C"],
        ["D", "Operand", "Append to Output", "[*, (, +, *, (]", "A B C D"],
        ["+", "Operator", "Push to Stack", "[*, (, +, *, (, +]", "A B C D"],
        ["E", "Operand", "Append to Output", "[*, (, +, *, (, +]", "A B C D E"],
        [")", "Right Paren", "Pop stack until '('", "[*, (, +, *]", "A B C D E +"],
        ["]", "Right Paren", "Pop stack until '['", "[*]", "A B C D E + * +"],
        ["/", "Operator", "Pop '*' (same precedence), Push '/'", "[/]", "A B C D E + * + *"],
        ["F", "Operand", "Append to Output", "[/]", "A B C D E + * + * F"],
        ["*", "Operator", "Pop '/' (same precedence), Push '*'", "[*]", "A B C D E + * + * F /"],
        ["(", "Left Paren", "Push to Stack", "[*, (]", "A B C D E + * + * F /"],
        ["G", "Operand", "Append to Output", "[*, (]", "A B C D E + * + * F / G"],
        ["+", "Operator", "Push to Stack", "[*, (, +]", "A B C D E + * + * F / G"],
        ["H", "Operand", "Append to Output", "[*, (, +]", "A B C D E + * + * F / G H"],
        [")", "Right Paren", "Pop stack until '('", "[*]", "A B C D E + * + * F / G H +"],
        ["-", "End of Expr", "Pop remaining stack", "[]", "A B C D E + * + * F / G H + *"],
    ]
)
sp(10)

# -- Q3 (c) 2024 --
chap_box(
    "Q3. c) What do you mean by RISC and CISC computers? List out the main characteristic of RISC and CISC computers. [4 Marks] (June 2024)\n"
    "[AND]\n"
    "Q3. a) Differentiate RISC and CICS computers. [3 Marks] (May/June 2023)"
)
section("RISC vs. CISC Architectures")
definition(
    "<b>RISC (Reduced Instruction Set Computer):</b> A CPU design philosophy focused on simple, "
    "highly-optimized instructions that can execute in a single clock cycle, heavily utilizing registers and pipelining."
)
definition(
    "<b>CISC (Complex Instruction Set Computer):</b> A CPU design philosophy focused on rich, complex instruction sets "
    "that perform multiple operations or memory accesses within a single instruction, minimizing instructions per program."
)

section("Key Architectural Characteristics")
info_table(
    ["Architectural Aspect", "RISC Characteristics", "CISC Characteristics"],
    [
        [
            "Instruction Size &amp; Format",
            "Fixed length (e.g. 32 bits), simple decoding format.",
            "Variable length (e.g. 1 to 15 bytes), complex format.",
        ],
        [
            "Addressing Modes",
            "Very few (mostly Register Direct, Displacement).",
            "Many complex addressing modes.",
        ],
        [
            "Memory Access",
            "Load/Store architecture. Only Load and Store instructions access memory. Operations are register-to-register.",
            "Memory-to-memory and memory-to-register operations supported.",
        ],
        [
            "Execution Speed",
            "Single-cycle execution per instruction (CPI ~ 1) using deep pipelines.",
            "Multi-cycle execution per instruction (variable CPI).",
        ],
        [
            "Control Unit",
            "Hardwired control unit for high performance.",
            "Microprogrammed control unit using control ROM.",
        ],
        [
            "Registers Count",
            "Large number of general-purpose registers (typically 32 to 128+).",
            "Fewer general-purpose registers (typically 8 to 16).",
        ],
    ],
    col_widths=[140, 175, 178],
)
sp(10)

# -- Q3 (c) 2023 --
chap_box(
    "Q3. c) Draw and explain daisy chain priority interrupt. [4 Marks] (May/June 2023)"
)
section("Daisy Chain Priority Interrupt System")
body(
    "A <b>Daisy Chain Priority Interrupt</b> system is a hardware-based method for establishing "
    "interrupt priorities among multiple I/O devices by connecting them in a series (chain) configuration. "
    "The device closest to the CPU has the highest priority, and priority decreases down the chain."
)

section("Daisy Chain Priority Interrupt Schematic")
net_daisy = ed.NetworkDiagram(
    width=CW,
    height=130,
    theme=diag_theme,
    caption="Fig 3.1b: Daisy Chain Priority Interrupt configuration",
)
net_daisy.node("daisy_circ", "", x=CW/2, y=65, kind="custom", custom_draw=draw_daisy_chain)
story.extend(net_daisy.as_flowable())
sp(10)

section("Working Principle and Signals")
bullet(
    [
        "<b>1. Common Interrupt Request (INT):</b> All I/O devices share a single, open-collector Interrupt Request line (INT). "
        "When any device requires service, it pulls the INT line LOW (active-low wire-OR connection) to signal the CPU.",
        "<b>2. Serial Interrupt Acknowledge (INTA):</b> The CPU responds to INT by asserting the Interrupt Acknowledge (INTA) signal. "
        "This signal travels through a series line connecting the <b>Priority In (PI)</b> and <b>Priority Out (PO)</b> ports of the devices.",
        "<b>3. Priority Decision Logic:</b><br/>"
        "• If a device has requested an interrupt, its <b>PI = 1</b> but it sets <b>PO = 0</b>, blocking the INTA signal from propagating to lower-priority devices. "
        "It then places its <b>Interrupt Vector Address (VAD)</b> onto the Data Bus to identify itself to the CPU.<br/>"
        "• If a device has not requested an interrupt, it simply passes the INTA signal to the next device by setting <b>PO = PI</b> (typically PO = 1).",
        "<b>4. Vector Address Fetch:</b> The CPU reads the vector address from the Data Bus, uses it to index into the "
        "interrupt vector table, and branches to the corresponding Interrupt Service Routine (ISR).",
    ]
)
sp(10)

# -- Q3 (d) 2023 --
chap_box(
    "Q3. d) Evaluate the arithmetic statement X = (A + B) * (C + D) using zero, one, two, or three address instructions. "
    "Use the symbols ADD, SUB, MUL, and DIV for the four arithmetic operations; MOV for the transfer-type operation; "
    "and LOAD and STORE for transfers to and from memory and AC register. [10 Marks] (May/June 2023)"
)
section("Multi-Address Instruction Formats Evaluation")
body(
    "We write assembly-like programs to evaluate the expression <b>X = (A + B) &times; (C + D)</b> using "
    "different instruction formats. We assume memory locations A, B, C, D store the operands, "
    "X stores the result, and T1, T2 are temporary memory registers."
)

section("Three-Address Instructions")
body(
    "Three-address instructions specify two source operands and one destination operand. "
    "<b>Format:</b> Opcode Destination, Source1, Source2"
)
code_block(
    "ADD  T1, A, B      ; T1 <- A + B\n"
    "ADD  T2, C, D      ; T2 <- C + D\n"
    "MUL  X, T1, T2     ; X <- T1 * T2"
)

section("Two-Address Instructions")
body(
    "Two-address instructions specify one operand as both a source and the destination. "
    "<b>Format:</b> Opcode Destination/Source1, Source2"
)
code_block(
    "MOV  T1, A         ; T1 <- A\n"
    "ADD  T1, B         ; T1 <- T1 + B\n"
    "MOV  T2, C         ; T2 <- C\n"
    "ADD  T2, D         ; T2 <- T2 + D\n"
    "MUL  T1, T2        ; T1 <- T1 * T2\n"
    "MOV  X, T1         ; X <- T1"
)

section("One-Address Instructions")
body(
    "One-address instructions use an implicit accumulator (AC) register for all operations. "
    "<b>Format:</b> Opcode Source"
)
code_block(
    "LOAD  A            ; AC <- A\n"
    "ADD   B            ; AC <- AC + B\n"
    "STORE T1           ; T1 <- AC\n"
    "LOAD  C            ; AC <- C\n"
    "ADD   D            ; AC <- AC + D\n"
    "MUL   T1           ; AC <- AC * T1\n"
    "STORE X            ; X <- AC"
)

section("Zero-Address Instructions")
body(
    "Zero-address instructions use a Stack for all operations. Operands are pushed onto "
    "the stack, and ALU operations pop their inputs from the stack and push the result back. "
    "<b>Format:</b> Opcode"
)
code_block(
    "PUSH A             ; Stack <- A\n"
    "PUSH B             ; Stack <- B\n"
    "ADD                ; Stack <- (A + B)\n"
    "PUSH C             ; Stack <- C\n"
    "PUSH D             ; Stack <- D\n"
    "ADD                ; Stack <- (C + D)\n"
    "MUL                ; Stack <- (A + B) * (C + D)\n"
    "POP  X             ; X <- Stack"
)
sp(10)

# -- Q3 (d) --
chap_box("Q3. d) Convert infix expression A*(B + C*D)+E in to RPN form. [10 Marks]")
section("Step-by-Step Expression Conversion Trace")
body(
    "Let us trace the Shunting-yard algorithm for the infix expression: <b>A * ( B + C * D ) + E</b>."
)

info_table(
    ["Token", "Type", "Action taken", "Operator Stack", "Postfix Output String"],
    [
        ["A", "Operand", "Append to Output", "[]", "A"],
        ["*", "Operator", "Push to Stack", "[*]", "A"],
        ["(", "Left Paren", "Push to Stack", "[*, (]", "A"],
        ["B", "Operand", "Append to Output", "[*, (]", "A B"],
        ["+", "Operator", "Push to Stack", "[*, (, +]", "A B"],
        ["C", "Operand", "Append to Output", "[*, (, +]", "A B C"],
        [
            "*",
            "Operator",
            "Push to Stack (higher precedence than +)",
            "[*, (, +, *]",
            "A B C",
        ],
        ["D", "Operand", "Append to Output", "[*, (, +, *]", "A B C D"],
        [")", "Right Paren", "Pop stack until '('", "[*]", "A B C D * +"],
        [
            "+",
            "Operator",
            "Pop '*' (precedence >= +), then push '+'",
            "[+]",
            "A B C D * + *",
        ],
        ["E", "Operand", "Append to Output", "[+]", "A B C D * + * E"],
        ["End", "-", "Pop remaining stack operator", "[]", "<b>A B C D * + * E +</b>"],
    ],
)
sp(10)

# -- Q3 (d) 2024 --
chap_box(
    "Q3. d) What do you mean by reverse Polish notation? Convert the following arithmetic expressions from infix to Ren.\n A*B+C*D+E*F\n[10 Marks] (June 2024)"
)
section("Reverse Polish Notation (RPN)")
definition(
    "<b>Reverse Polish Notation (RPN):</b> Also known as postfix notation, it is a mathematical notation "
    "wherein operators follow their operands (e.g. `A B +` instead of `A + B`). This eliminates the need "
    "for parentheses and operator precedence rules, facilitating stack-based arithmetic evaluations in computer hardware."
)

section("Conversion Step-by-Step Table")
body(
    "We convert the infix expression <b>A * B + C * D + E * F</b> to RPN using Shunting-yard rules:"
)
info_table(
    ["Token", "Type", "Action taken", "Operator Stack", "Postfix Output String"],
    [
        ["A", "Operand", "Append to Output", "[]", "A"],
        ["*", "Operator", "Push to Stack", "[*]", "A"],
        ["B", "Operand", "Append to Output", "[*]", "A B"],
        ["+", "Operator", "Pop '*' (precedence >= +), then push '+'", "[+]", "A B *"],
        ["C", "Operand", "Append to Output", "[+]", "A B * C"],
        ["*", "Operator", "Push to Stack (precedence > +)", "[+, *]", "A B * C"],
        ["D", "Operand", "Append to Output", "[+, *]", "A B * C D"],
        ["+", "Operator", "Pop '*' (precedence >= +), pop '+' (precedence >= +), push '+'", "[+]", "A B * C D * +"],
        ["E", "Operand", "Append to Output", "[+]", "A B * C D * + E"],
        ["*", "Operator", "Push to Stack (precedence > +)", "[+, *]", "A B * C D * + E"],
        ["F", "Operand", "Append to Output", "[+, *]", "A B * C D * + E F"],
        ["End", "-", "Pop remaining stack operators", "[]", "<b>A B * C D * + E F * +</b>"],
    ],
)
sp(10)

# -- Q3 (e) --
chap_box(
    "Q3. e) [OR] Write different modes of data transfer. Elaborate any one of them. [10 Marks]"
)
section("Modes of Data Transfer")
body(
    "Data transfer between the CPU/Memory and I/O devices is classified into three main modes:"
)
bullet(
    [
        "<b>1. Programmed I/O:</b> The CPU is in complete control. It continually polls the status register "
        "of the I/O device. The CPU is fully occupied during transfer, leading to low efficiency.",
        "<b>2. Interrupt-Initiated I/O:</b> The CPU issues a command, then resumes normal execution. When the device "
        "is ready, it sends an interrupt signal. The CPU halts current work, runs the ISR, transfers data, and returns.",
        "<b>3. Direct Memory Access (DMA):</b> The CPU is bypassed. An external hardware DMA controller handles "
        "high-speed data block transfers directly between the memory and peripheral device.",
    ]
)

section("Elaboration of Direct Memory Access (DMA)")
body(
    "In DMA, high-speed peripherals transfer blocks of data without CPU intervention. "
    "The DMA Controller (DMAC) takes control of the system bus lines to perform read/write cycles directly."
)
bullet(
    [
        "<b>Bus Request (BR):</b> DMAC asserts this line to request bus control from the CPU.",
        "<b>Bus Grant (BG):</b> CPU releases the buses (high-impedance) and asserts BG to give control to DMAC.",
        "<b>Data Transfer:</b> DMAC generates memory addresses and I/O read/write control signals to move "
        "data bytes directly between memory and device, incrementing its internal address register and decrementing count.",
        "<b>Interrupt:</b> When the word count register reaches 0, DMAC releases the bus and asserts an interrupt to CPU.",
    ]
)

section("DMA System Architecture Block Diagram")
net_dma = ed.NetworkDiagram(
    width=CW,
    height=190,
    theme=diag_theme,
    caption="Fig 3.1: DMA controller system bus connections and interface",
)
net_dma.node("cpu", "CPU", x=90, y=130, kind="server")
net_dma.node("dma", "DMA Controller\n(DMAC)", x=250, y=130, kind="generic")
net_dma.node("mem", "Main Memory", x=410, y=130, kind="database")
net_dma.node("device", "I/O Device\n(Disk)", x=250, y=50, kind="storage")

net_dma.link("cpu", "dma", label="BR / BG")
net_dma.link("dma", "mem", label="Addr/Data")
net_dma.link("device", "dma", label="DREQ / DACK")
net_dma.link("device", "mem", label="Direct Data")
story.extend(net_dma.as_flowable())
br()

# -- Q3 (e) [OR] 2024 --
chap_box(
    "Q3. e) [OR] An instruction is stored at location 300 with its address field at location 301. The address field has the value 400. A processor register R1 contains the number 200. Evaluate the effective address if the addressing mode of the instruction is (a) direct; (b) immediate; (c) relative; (d) register indirect; (e) index with R1 as the index register. [10 Marks] (June 2024)"
)
section("Addressing Modes Parameter Values")
bullet(
    [
        "Instruction Address (Memory location): <b>300 &amp; 301</b> (address field is at 301)",
        "Address Field Value (ADR): <b>400</b>",
        "Index Register (R1): <b>200</b>",
        "Program Counter (PC): After fetching the instruction (which takes 2 words at 300 &amp; 301), "
        "the PC points to the next sequential instruction address: <b>PC = 302</b>.",
    ]
)

section("Effective Address (EA) Evaluation")
info_table(
    ["Addressing Mode", "Mathematical Equation / Derivation", "Effective Address (EA) Value", "Explanation"],
    [
        [
            "(a) Direct",
            "EA = ADR",
            "<b>400</b>",
            "The operand is stored in memory at location 400.",
        ],
        [
            "(b) Immediate",
            "EA = 301",
            "<b>301</b>",
            "The operand value is the constant 400 itself, which resides at location 301.",
        ],
        [
            "(c) Relative",
            "EA = PC + ADR = 302 + 400",
            "<b>702</b>",
            "The operand is located relative to the next instruction address (PC = 302).",
        ],
        [
            "(d) Register Indirect",
            "EA = R1",
            "<b>200</b>",
            "The operand is stored in memory at the address pointed to by R1 (address 200).",
        ],
        [
            "(e) Index with R1",
            "EA = ADR + R1 = 400 + 200",
            "<b>600</b>",
            "The address field 400 is offset by the index register value R1 (200) to yield address 600.",
        ],
    ],
    col_widths=[110, 160, 90, 123],
)
sp(10)


# =============================================================================
#  QUESTION 4: CO4
# =============================================================================
part_box("QUESTION 4 -- CO4 MEMORY ARCHITECTURE")

# -- Q4 (a) --
chap_box(
    "Q4. a) Estimate the number of address lines required to address a memory space of 2 Giga Bytes. [3 Marks]"
)
section("Address Line Calculation")
body(
    "To calculate the address bus lines, we must find the power of 2 that equals the memory capacity in bytes:"
)
bullet(
    [
        "1 Kilo Byte (KB) = 2<sup>10</sup> Bytes",
        "1 Mega Byte (MB) = 2<sup>20</sup> Bytes",
        "1 Giga Byte (GB) = 2<sup>30</sup> Bytes",
        "Memory Space = 2 Giga Bytes = 2 × 2<sup>30</sup> Bytes = <b>2<sup>31</sup> Bytes</b>",
    ]
)
body(
    "Number of address lines <i>N</i> = log<sub>2</sub>(Memory Capacity in Bytes) = log<sub>2</sub>(2<sup>31</sup>) = <b>31 lines</b>.<br/>"
    "Therefore, <b>31 address lines</b> (A<sub>0</sub> to A<sub>30</sub>) are required to address 2 GB of memory."
)
sp(10)

# -- Q4 (a) 2024 --
chap_box(
    "Q4. a) Define the need of cache memory in a computer system. What is 'Locality of references' concept? [3 Marks] (June 2024)\n"
    "[AND]\n"
    "Q4. b) Discuss \"locality of references\" Phenomenon of computer memory. Write expression for hit ratio. [4 Marks] (May/June 2023)"
)
section("Need for Cache Memory")
body(
    "<b>Cache Memory</b> is a small, ultra-fast semiconductor memory (SRAM) placed between the CPU and main memory (DRAM). "
    "It is needed to solve the **Processor-Memory speed gap**: while CPU speeds have grown exponentially, "
    "DRAM access times have improved very slowly. Without cache, the CPU would spend most of its time idle "
    "waiting for data from main memory (memory stalls)."
)

section("Principle of Locality of Reference")
definition(
    "<b>Locality of Reference:</b> The empirical observation that computer programs tend to access "
    "a relatively small portion of their address space at any given time. This makes caching highly effective."
)
bullet(
    [
        "<b>Temporal Locality:</b> If the CPU accesses a memory location once, it is highly likely to access the exact same location "
        "again in the near future. (Examples: loops, index variables, stack frames).",
        "<b>Spatial Locality:</b> If the CPU accesses a memory location, it is highly likely to access adjacent memory locations "
        "soon after. (Examples: sequential instruction execution, array traversals).",
    ]
)
section("Hit Ratio Expression")
definition(
    "<b>Hit Ratio (H):</b> The ratio of the number of successful data finds in the cache memory (hits) "
    "to the total number of memory access attempts (hits + misses). Expression:<br/>"
    "<b>Hit Ratio (H) = Hits &divide; (Hits + Misses)</b><br/>"
    "It represents the probability of a cache hit, where <b>0 &le; H &le; 1</b>. "
    "The closer H is to 1, the more effective the cache system is."
)
sp(10)

# -- Q4 (b) --
chap_box("Q4. b) Compare static and Dynamic RAM. Which one is used as cache? [4 Marks]")
section("SRAM vs DRAM Comparison")
info_table(
    ["Property", "Static RAM (SRAM)", "Dynamic RAM (DRAM)"],
    [
        [
            "Cell Structure",
            "Uses 6 transistors forming a latch (flip-flop). Stores bits as voltage states.",
            "Uses 1 transistor and 1 capacitor. Stores bits as charge levels.",
        ],
        [
            "Refresh Requirement",
            "Does not require refresh as long as power is continuously applied.",
            "Requires periodic refresh cycles (every few ms) due to charge leakage.",
        ],
        [
            "Operating Speed",
            "Very fast (access time 1 to 5 ns). Matches CPU bus speed.",
            "Slower (access time 10 to 50 ns) due to capacitor charging/discharging.",
        ],
        [
            "Density & Size",
            "Lower density. Takes more physical chip area per bit.",
            "Extremely high density. Denser layout, cheaper per bit.",
        ],
        [
            "Cost & Power",
            "High cost and higher active power consumption.",
            "Low cost and low power consumption.",
        ],
    ],
)
body(
    "<b>Usage:</b> <b>SRAM</b> is used for cache memory because of its high speed, while <b>DRAM</b> is used for main system memory."
)
sp(10)

# -- Q4 (b) 2024 --
chap_box(
    "Q4. b) What is hit ratio? How average access time can be reduced by cache? A computer has cache access time of 100ns, a main memory access time of 1000ns, and a hit ratio of 0.9, find average access time. [4 Marks] (June 2024)"
)
section("Cache Hit Ratio & Access Time Reduction")
definition(
    "<b>Hit Ratio (H):</b> The probability of finding the requested data in the cache memory. "
    "It is the ratio of the number of cache hits to the total number of memory access requests:<br/>"
    "<b>H = Hits / (Hits + Misses)</b>."
)
body(
    "Cache memory reduces the average access time by resolving the vast majority of memory requests "
    "at the high-speed cache level, bypassing the slow main memory. Since cache access time (T<sub>c</sub>) "
    "is much smaller than main memory access time (T<sub>m</sub>), and the hit ratio (H) is high (typically &gt; 0.90), "
    "the average access time (T<sub>avg</sub>) is pulled significantly closer to T<sub>c</sub>."
)

section("Numerical Calculation")
body(
    "Given parameters: Cache access time <b>T<sub>c</sub> = 100 ns</b>, Main memory access time <b>T<sub>m</sub> = 1000 ns</b>, "
    "Hit ratio <b>H = 0.9</b>, Miss ratio <b>(1 - H) = 0.1</b>."
)
bullet(
    [
        "<b>Case 1: Hierarchical Access (Serial check)</b><br/>"
        "On a cache miss, the cache is accessed first, and then main memory is accessed.<br/>"
        "T<sub>avg</sub> = T<sub>c</sub> + (1 - H) &times; T<sub>m</sub> = 100 + 0.1 &times; 1000 = 100 + 100 = <b>200 ns</b>.",
        "<b>Case 2: Simultaneous Access (Parallel check)</b><br/>"
        "Cache and main memory are accessed in parallel. If cache hits, main memory cycle is aborted.<br/>"
        "T<sub>avg</sub> = H &times; T<sub>c</sub> + (1 - H) &times; T<sub>m</sub> = 0.9 &times; 100 + 0.1 &times; 1000 = 90 + 100 = <b>190 ns</b>.",
    ]
)
sp(10)

# -- Q4 (c) --
chap_box(
    "Q4. c) Justify the use of hierarchical memory in a computer system. [4 Marks] (June 2022)\n"
    "[AND]\n"
    "Q4. a) Why we need memory hierarchy in a computer system? Draw and explain. [3 Marks] (May/June 2023)"
)
section("The Memory Hierarchy Justification")
body(
    "A computer system requires high memory capacity, high operating speed, and low cost. "
    "However, a single memory technology cannot meet all these requirements: fast memories (SRAM) are "
    "very expensive and have small capacity, while cheap memories (Hard disks, Flash) are extremely slow. "
    "A <b>hierarchical memory system</b> solves this conflict."
)

section("Principle of Locality of Reference")
body("The hierarchy is effective because of the <b>Locality of Reference</b>:")
bullet(
    [
        "<b>Temporal Locality:</b> If the CPU accesses a memory location once, it is highly likely to "
        "access the same location again in the near future (e.g., in loop counters).",
        "<b>Spatial Locality:</b> If the CPU accesses a location, it is highly likely to access adjacent locations "
        "soon after (e.g., sequential code execution, array elements).",
    ]
)

section("Memory Hierarchy Pyramid")
stack_mem = ed.LayeredStack(
    width=CW * 0.7,
    height=160,
    theme=diag_theme,
    caption="Fig 4.1: The memory hierarchy structure (speed vs capacity)",
)
stack_mem.layer("Registers", sublabel="1 cycle  |  <1 KB  |  CPU registers")
stack_mem.layer("Cache Memory", sublabel="2-10 cycles  |  L1/L2/L3 SRAM")
stack_mem.layer("Main Memory", sublabel="100-200 cycles  |  DRAM system memory")
stack_mem.layer("Secondary Storage", sublabel="Thousands of cycles  |  SSD/HDD")
story.extend(stack_mem.as_flowable())
sp(10)

# -- Q4 (c) 2024 --
chap_box(
    "Q4. c) Write and explain different page replacement algorithms. [4 Marks] (June 2024)"
)
section("Page Replacement Algorithms")
body(
    "When a page fault occurs and all physical memory frames are full, the operating system must "
    "select a page in memory to be replaced (a victim page) to make room for the incoming page. "
    "The primary algorithms used are:"
)
bullet(
    [
        "<b>1. First-In, First-Out (FIFO):</b> Replaces the oldest page in memory (the page that was loaded earliest). "
        "It is simple to implement using a queue. However, it can suffer from <b>Belady's Anomaly</b>, where "
        "increasing the number of physical frames results in an increase in the number of page faults.",
        "<b>2. Least Recently Used (LRU):</b> Replaces the page in memory that has not been accessed for the "
        "longest period of time. It is based on temporal locality. It is highly efficient and does not suffer from "
        "Belady's Anomaly, but requires hardware support (such as counters or a stack) to track access history, making it expensive.",
        "<b>3. Optimal (OPT / MIN):</b> Replaces the page that will not be used for the longest period of time in the "
        "future. This algorithm yields the lowest possible page fault rate for any frame allocation. However, "
        "it is impossible to implement in practice because it requires future knowledge of the program's execution path. "
        "It is used primarily as a benchmark for evaluating other algorithms.",
    ]
)
sp(10)

# -- Q4 (c) 2023 --
chap_box(
    "Q4. c) How many 128 x 8 RAM chips are needed to provide a memory capacity of 2048 bytes? "
    "How many lines of the address bus must be used to access 2048 bytes of memory? "
    "How many of these lines will be common to all chips? [4 Marks] (May/June 2023)"
)
section("RAM Chip Capacity and Addressing Analysis")
body(
    "We analyze the memory requirements and address line distribution for a memory system "
    "built using multiple individual RAM chips."
)

section("Part 1: RAM Chips Required")
body(
    "We calculate the total number of RAM chips needed to achieve the target memory capacity:<br/>"
    "• Target Memory Capacity = 2048 Bytes<br/>"
    "• Single RAM Chip Capacity = 128 &times; 8 bits = 128 Bytes<br/>"
    "• Number of RAM Chips = Target Capacity &divide; Single Chip Capacity = 2048 &divide; 128 = <b>16 chips</b>."
)

section("Part 2: Address Bus Lines")
body(
    "We determine the total number of address lines required to address the entire 2048-byte memory space:<br/>"
    "• Memory capacity = 2048 Bytes = 2<sup>11</sup> Bytes.<br/>"
    "• Since the memory is byte-addressable, we require <b>11 lines</b> on the address bus (A<sub>0</sub> to A<sub>10</sub>) "
    "to uniquely select any one of the 2048 memory locations."
)

section("Part 3: Common Address Lines")
body(
    "We determine how many of the 11 address lines are routed directly to all RAM chips in common:<br/>"
    "• A single 128-byte chip contains 128 addressable locations. "
    "Capacity = 128 Bytes = 2<sup>7</sup> Bytes. Thus, a single chip requires <b>7 address lines</b>.<br/>"
    "• These <b>7 address lines (A<sub>0</sub> to A<sub>6</sub>)</b> are connected directly and in common to the address pins of all 16 chips. "
    "They select a specific byte inside the active chip.<br/>"
    "• The remaining 4 address lines (A<sub>7</sub> to A<sub>10</sub>) are routed through a 4-to-16 line decoder. "
    "The decoder's 16 outputs are connected to the Chip Select (CS) inputs of the 16 individual RAM chips to select the active chip."
)
sp(10)

# -- Q4 (d) --
chap_box(
    "Q4. d) A computer employs RAM chips of 256 × 8 and ROM chips of 1024 × 8. The computer needs 2K bytes of RAM and 4K bytes of ROM. How many RAM, ROM chips are needed? [10 Marks]"
)
section("Chip Count Calculations")
body(
    "Let us compute the chip count requirement based on the capacities needed. "
    "Note: 258 × 8 in the question paper is a typo for the standard 256 × 8 chip size."
)
bullet(
    [
        "<b>1. Number of RAM chips needed:</b><br/>"
        "• Required RAM = 2 KB = 2 × 1024 Bytes = 2048 Bytes.<br/>"
        "• Size of one RAM chip = 256 Bytes (256 × 8 bits).<br/>"
        "• RAM Chips = Required RAM / Chip Size = 2048 / 256 = <b>8 chips</b>.",
        "<b>2. Number of ROM chips needed:</b><br/>"
        "• Required ROM = 4 KB = 4 × 1024 Bytes = 4096 Bytes.<br/>"
        "• Size of one ROM chip = 1 KB = 1024 Bytes (1024 × 8 bits).<br/>"
        "• ROM Chips = Required ROM / Chip Size = 4096 / 1024 = <b>4 chips</b>.",
    ]
)

section("Memory Address Map & Address Bus Lines")
body(
    "To address 2KB of RAM + 4KB of ROM, we need a total memory space of 6KB.<br/>"
    "Total Address lines required for 4KB ROM = log<sub>2</sub>(4096) = 12 lines (A<sub>0</sub> to A<sub>11</sub>).<br/>"
    "Total Address lines required for 2KB RAM = log<sub>2</sub>(2048) = 11 lines (A<sub>0</sub> to A<sub>10</sub>)."
)

info_table(
    ["Component", "Hex Address Range", "Address lines (A11 A10 A9 A8 ... A0)"],
    [
        [
            "RAM (8 chips)",
            "0x0000 - 0x07FF",
            "0 0 x x x x x x x x x (Select lines: A<sub>10</sub>, A<sub>9</sub>, A<sub>8</sub> select chip)",
        ],
        [
            "ROM (4 chips)",
            "0x0800 - 0x17FF",
            "1 x x x x x x x x x x x (Select lines: A<sub>11</sub> selects ROM block)",
        ],
    ],
)
sp(10)

# -- Q4 (e) / Q4 (d) [OVERLAPPED] --
chap_box(
    "Q4. e) [OR] A hierarchical cache memory sub system has following specifications:\n"
    " i) Cache access time of 100 ns\n"
    " ii) Main memory access time of 500 ns\n"
    " iii) 70% memory requests are read operations\n"
    " iv) Hit ratio is 0.8 for read access and write through scheme is used\n"
    "Calculate:\n"
    " A) Average access time of the system considering only memory read cycles.\n"
    " B) Average access time of the system for both read and write requests. [10 Marks] (June 2022)\n"
    "[AND]\n"
    "Q4. d) A hierarchical cache memory sub system has following specifications:\n"
    " i) Cache access time of 100 ns\n"
    " ii) Main memory access time of 500 ns\n"
    " iii) 70% memory requests are read operations\n"
    " iv) Hit ratio is 0.8 for read access and write through scheme is used\n"
    "Calculate:\n"
    " A) Average access time of the system, considering only memory read cycles.\n"
    " B) Average access time of the system for both read and write requests. [10 Marks] (June 2024)\n"
    "[AND]\n"
    "Q4. e) A hierarchical cache memory sub system has following specifications:\n"
    " i) Cache access time of 100 ns\n"
    " ii) Main memory access time of 500 ns\n"
    " iii) 70% memory requests are read operations\n"
    " iv) Hit ratio is 0.8 for read access and write through scheme is used\n"
    "Calculate:\n"
    " A) Average access time of the system, considering only memory read cycles.\n"
    " B) Average access time of the system for both read and write requests. [10 Marks] (May/June 2023)"
)
section("Parameter Definitions")
bullet(
    [
        "Cache access time (T<sub>c</sub>) = 100 ns",
        "Main memory access time (T<sub>m</sub>) = 500 ns",
        "Hit ratio for reads (H) = 0.8",
        "Miss ratio for reads (1 - H) = 0.2",
        "Read cycle frequency (P<sub>read</sub>) = 0.70",
        "Write cycle frequency (P<sub>write</sub>) = 0.30",
    ]
)

section("Part A: Average Access Time for Read Cycles (T<sub>read</sub>)")
body(
    "We calculate the average read access time using both hierarchical (serial) and simultaneous (parallel) assumptions."
)
bullet(
    [
        "<b>Assumption 1: Hierarchical Access (Serial check).</b><br/>"
        "On a miss, the cache is checked first (T<sub>c</sub>), and then main memory is accessed (T<sub>m</sub>).<br/>"
        "T<sub>read</sub> = T<sub>c</sub> + (1 - H) × T<sub>m</sub> = 100 + 0.2 × 500 = 100 + 100 = <b>200 ns</b>.",
        "<b>Assumption 2: Simultaneous Access (Parallel check).</b><br/>"
        "Cache and main memory are accessed in parallel. If cache hits, main memory cycle is aborted.<br/>"
        "T<sub>read</sub> = H × T<sub>c</sub> + (1 - H) × T<sub>m</sub> = 0.8 × 100 + 0.2 × 500 = 80 + 100 = <b>180 ns</b>.",
    ]
)

section("Part B: Average Access Time for both Read and Write (T<sub>avg</sub>)")
body(
    "For write operations, a <b>write-through</b> scheme is used. In write-through, every write "
    "must update main memory. Thus, the write access time is bounded by main memory: <b>T<sub>write</sub> = T<sub>m</sub> = 500 ns</b>."
)
bullet(
    [
        "<b>Under Assumption 1 (T<sub>read</sub> = 200 ns):</b><br/>"
        "T<sub>avg</sub> = P<sub>read</sub> × T<sub>read</sub> + P<sub>write</sub> × T<sub>write</sub><br/>"
        "T<sub>avg</sub> = 0.70 × 200 + 0.30 × 500 = 140 + 150 = <b>290 ns</b>.",
        "<b>Under Assumption 2 (T<sub>read</sub> = 180 ns):</b><br/>"
        "T<sub>avg</sub> = P<sub>read</sub> × T<sub>read</sub> + P<sub>write</sub> × T<sub>write</sub><br/>"
        "T<sub>avg</sub> = 0.70 × 180 + 0.30 × 500 = 126 + 150 = <b>276 ns</b>.",
    ]
)
br()

# -- Q4 (e) [OR] 2024 --
chap_box(
    "Q4. e) [OR] Name three cache mapping techniques. With the of suitable diagrams describe associative mapping in detail. [10 Marks] (June 2024)\n"
    "[AND]\n"
    "Q4. d) Name three cache mapping techniques. Explain Associative mapping method of cache memory organization. [4 Marks] (May/June 2023)"
)
section("Cache Mapping Techniques")
body(
    "Cache mapping is the method used to establish a correspondence between the large address space of "
    "main memory and the small address space of the cache. The three main techniques are:"
)
bullet(
    [
        "<b>1. Direct Mapping:</b> Each main memory block maps to exactly one specific line in the cache. "
        "It is simple and inexpensive but suffers from high conflict misses if multiple active blocks map to the same line.",
        "<b>2. Associative Mapping:</b> Any main memory block can be placed in any cache line. It offers maximum flexibility "
        "and zero conflict misses but requires expensive hardware (Content Addressable Memory - CAM) for parallel searches.",
        "<b>3. Set-Associative Mapping:</b> A compromise that divides cache lines into sets. A memory block maps to a specific set, "
        "but can be placed in any line within that set (e.g. 2-way or 4-way set associative).",
    ]
)

section("Associative Mapping in Detail")
body(
    "In <b>Associative Mapping</b>, the cache control logic has complete freedom to store any memory block in any cache line. "
    "To retrieve data, the CPU compares the Tag field of the memory address against the Tags of all cache lines "
    "**simultaneously in parallel** using associative (CAM) circuitry."
)
bullet(
    [
        "<b>Address Division:</b> The main memory address is divided into two fields:<br/>"
        "• <b>Tag Field:</b> Identifies the memory block uniquely.<br/>"
        "• <b>Word Field:</b> Identifies the specific word/byte within the block.<br/>"
        "*(Note: Since blocks can go anywhere, there is no Cache Index field in the address).* ",
        "<b>Read Access:</b> The CPU tag is broadcast to all cache line comparison units at once. "
        "If a match is found (<b>Cache Hit</b>), the corresponding block's data is enabled and the word offset selects the byte. "
        "If no match is found (<b>Cache Miss</b>), the CPU accesses main memory, fetches the block, and loads it into any free cache line.",
        "<b>Replacement Policy:</b> Since blocks can occupy any line, when the cache is full, a replacement policy "
        "(such as LRU or FIFO) is used to select and evict a victim block.",
    ]
)

section("Associative Cache Mapping Architecture Block Diagram")
net_assoc = ed.NetworkDiagram(
    width=CW,
    height=200,
    theme=diag_theme,
    caption="Fig 4.2: Hardware block diagram of Cache Associative Mapping architecture",
)
net_assoc.node("assoc_circ", "", x=CW/2, y=100, kind="custom", custom_draw=draw_associative_mapping)
story.extend(net_assoc.as_flowable())
sp(10)


# =============================================================================
#  QUESTION 5: CO5
# =============================================================================
part_box("QUESTION 5 -- CO5 PIPELINING & MULTIPROCESSORS")

# -- Q5 (a) --
chap_box(
    "Q5. a) Define the term Pipelining. How to get higher throughput through pipelining? [3 Marks]"
)
section("Pipelining Concept")
definition(
    "<b>Pipelining:</b> A technique of decomposing a sequential process into sub-operations, "
    "and executing each sub-operation in a dedicated segment (stage) that operates concurrently "
    "with all other stages. Instructions overlap in execution."
)

section("Throughput Enhancement Mechanism")
body(
    "Throughput is defined as the number of tasks completed per unit time. Pipelining increases "
    "throughput by overlapping instruction phases (Fetch, Decode, Execute):"
)
bullet(
    [
        "While instruction <i>i</i> is executing, instruction <i>i+1</i> is being decoded, and "
        "instruction <i>i+2</i> is being fetched from memory.",
        "Once the pipeline is fully loaded, a completed instruction is outputted on <b>every clock cycle</b>, "
        "regardless of the instruction latency. This speeds up the overall execution rate.",
    ]
)
sp(10)

# -- Q5 (b) / Q5 (a) [OVERLAPPED] --
chap_box(
    "Q5. b) Write equation of speedup factor of a k-stage pipeline over an equivalent non-pipelined processor. [4 Marks] (June 2022)\n"
    "[AND]\n"
    "Q5. a) Derive the expression for speed up ratio of a pipelined system. [3 Marks] (June 2024)\n"
    "[AND]\n"
    "Q5. b) Write and explain the expression for speed up ratio. [4 Marks] (June 2023)"
)
section("Mathematical Derivation of Pipeline Speedup")
body(
    "Let us derive the speedup ratio S of a k-stage pipeline executing n tasks compared to a non-pipelined system:"
)
bullet(
    [
        "Let <b>t<sub>n</sub></b> be the total execution time of a single task in the non-pipelined processor.",
        "Let <b>t<sub>p</sub></b> be the clock cycle time of the pipelined processor. In a balanced pipeline, "
        "t<sub>p</sub> is equal to the delay of the slowest stage plus latch overhead.",
        "<b>Time for non-pipelined processor (T<sub>np</sub>):</b> To process n independent tasks sequentially, the CPU requires:<br/>"
        "T<sub>np</sub> = n &times; t<sub>n</sub>",
        "If we assume a balanced pipeline where a task is divided into k equal segments, then <b>t<sub>n</sub> = k &times; t<sub>p</sub></b>. "
        "Thus: <b>T<sub>np</sub> = n &times; k &times; t<sub>p</sub></b>.",
        "<b>Time for pipelined processor (T<sub>p</sub>):</b> The first task requires k clock cycles to fill the pipeline. "
        "The remaining (n - 1) tasks complete at the rate of one task per clock cycle:<br/>"
        "T<sub>p</sub> = [k + (n - 1)] &times; t<sub>p</sub> = (k + n - 1) &times; t<sub>p</sub>",
        "<b>Speedup Factor (S):</b> The ratio of non-pipelined execution time to pipelined time:<br/>"
        "S = T<sub>np</sub> / T<sub>p</sub> = <b>(n &times; k &times; t<sub>p</sub>) / ((k + n - 1) &times; t<sub>p</sub>) = (n &times; k) / (k + n - 1)</b>",
    ]
)
body(
    "As the number of tasks becomes very large (n &rarr; &infin;):<br/>"
    "S<sub>max</sub> = lim<sub>n&rarr;&infin;</sub> (n &times; k) / (k + n - 1) = <b>k</b>.<br/>"
    "Thus, the maximum theoretical speedup of a k-stage pipeline is equal to the number of segments <b>k</b>."
)
sp(10)

# -- Q5 (b) 2024 --
chap_box(
    "Q5. b) A non pipeline system takes 50ns to process a task. The same task can be processed in a six segment pipeline with a clock cycle of 10ns. Determine the speedup ratio of the pipeline for 100 tasks. What is the maximum speed up that can be achieved? [4 Marks] (June 2024)\n"
    "[AND]\n"
    "Q5. e) A non-pipeline system takes 50ns to process a task. The same task can be processed in a six-segment pipeline with a clock cycle of 10ns. Determine the speedup ratio of the pipeline for 100 tasks. What is the maximum speed up that can be achieved? [10 Marks] (June 2023)"
)
section("Pipeline Speedup Numerical Calculation")
bullet(
    [
        "Non-pipelined task execution time (t<sub>n</sub>) = <b>50 ns</b>",
        "Pipeline clock cycle time (t<sub>p</sub>) = <b>10 ns</b>",
        "Number of stages (k) = <b>6</b>",
        "Number of tasks (n) = <b>100</b>",
    ]
)
bullet(
    [
        "<b>1. Non-pipelined execution time (T<sub>np</sub>):</b><br/>"
        "T<sub>np</sub> = n &times; t<sub>n</sub> = 100 &times; 50 ns = <b>5000 ns</b>.",
        "<b>2. Pipelined execution time (T<sub>p</sub>):</b><br/>"
        "T<sub>p</sub> = (k + n - 1) &times; t<sub>p</sub> = (6 + 100 - 1) &times; 10 ns = 105 &times; 10 ns = <b>1050 ns</b>.",
        "<b>3. Speedup Ratio for 100 tasks (S):</b><br/>"
        "S = T<sub>np</sub> / T<sub>p</sub> = 5000 ns / 1050 ns = <b>4.76</b>.<br/>"
        "Therefore, the pipeline achieves a speedup of <b>4.76</b> for 100 tasks.",
        "<b>4. Maximum Speedup (S<sub>max</sub>):</b><br/>"
        "• Based on cycle-time comparison: <b>S<sub>max</sub> = t<sub>n</sub> / t<sub>p</sub> = 50 ns / 10 ns = 5</b>.<br/>"
        "• Based on stage count (theoretical limit): <b>S<sub>limit</sub> = k = 6</b>.<br/>"
        "<i>Explanation of difference:</i> Since the non-pipelined execution time (50 ns) is less than k &times; t<sub>p</sub> (6 &times; 10 ns = 60 ns), "
        "the stages are slightly unbalanced or there is latch overhead in the pipeline. Thus, the practical maximum speedup is bounded by "
        "t<sub>n</sub> / t<sub>p</sub> = <b>5</b>, while the absolute theoretical limit if stages were perfectly balanced and overhead-free is <b>6</b>.",
    ]
)
sp(10)

# -- Q5 (c) / Q5 (e) / Q5 (c) [OVERLAPPED] --
chap_box(
    "Q5. c) Draw a space-time diagram for a six-segment pipeline showing the time it takes to process 8 tasks. [4 Marks] (June 2022)\n"
    "[AND]\n"
    "Q5. e) [OR] Define arithmetic and instruction pipeline. Draw a space time diagram for a six segment pipeline showing the time it takes to process eight tasks. [10 Marks] (June 2024)\n"
    "[AND]\n"
    "Q5. c) Explain Arithmetic pipeline in short. Differentiate it with instruction pipeline. [4 Marks] (June 2023)"
)
section("Arithmetic vs. Instruction Pipelines")
definition(
    "<b>Arithmetic Pipeline:</b> Decomposes a complex arithmetic operation into sequential sub-operations "
    "to execute them concurrently. It is combinational in nature and resides inside the ALU.<br/>"
    "• <i>Example:</i> Floating-point adder/subtractor pipeline (1. Exponent alignment, 2. Fraction add/sub, 3. Normalization)."
)
definition(
    "<b>Instruction Pipeline:</b> Overlaps the execution of consecutive instructions by decomposing the "
    "instruction execution cycle into sequential stages (e.g. Fetch, Decode, Execute, Write Back). It speeds up program execution."
)

section("Comparison of Arithmetic and Instruction Pipelines")
info_table(
    ["Comparison Feature", "Arithmetic Pipeline", "Instruction Pipeline"],
    [
        [
            "<b>Primary Purpose</b>",
            "To speed up execution of complex, repetitive arithmetic operations.",
            "To speed up execution of a stream of instructions in a program.",
        ],
        [
            "<b>Hardware Nature</b>",
            "Combinational logic segments inside the Arithmetic Logic Unit (ALU).",
            "Sequential stages involving control unit logic, register files, and buses.",
        ],
        [
            "<b>Inputs &amp; Outputs</b>",
            "Numeric operands (inputs) and computed results (outputs).",
            "Machine instructions (inputs) and CPU/memory state updates (outputs).",
        ],
        [
            "<b>Stage Examples</b>",
            "Exponent subtract, align mantissas, add/subtract mantissas, normalize result.",
            "Instruction Fetch (IF), Instruction Decode (ID), Operand Fetch (OF), Execute (EX), Write Back (WB).",
        ],
        [
            "<b>Dependencies &amp; Hazards</b>",
            "No dependencies between successive calculations in the pipeline.",
            "Hazards (Structural, Data, Control) can stall instruction flow.",
        ],
    ],
    col_widths=[110, 190, 193],
)
sp(10)

section("Space-Time Diagram Matrix for 6-segment, 8-task Pipeline")
body(
    "For a pipeline with <b>k = 6</b> stages and <b>n = 8</b> tasks, the total time required is "
    "k + n - 1 = 6 + 8 - 1 = <b>13 clock cycles</b>. Let us render the utilization matrix:"
)


# Custom dynamic ReportLab table generator for the space-time grid
def draw_spacetime_table():
    from reportlab.lib.enums import TA_CENTER
    from reportlab.lib.styles import ParagraphStyle

    t_theme = en.get_theme()

    th = ParagraphStyle(
        "ST_Header",
        fontSize=8,
        textColor=t_theme.rl("#ffffff"),
        fontName="Helvetica-Bold",
        alignment=TA_CENTER,
        leading=10,
    )
    td = ParagraphStyle(
        "ST_Data",
        fontSize=8,
        textColor=t_theme.rl(t_theme.text),
        fontName="Helvetica-Bold",
        alignment=TA_CENTER,
        leading=10,
    )

    headers = ["Segment"] + [f"C{i}" for i in range(1, 14)]
    data = [[Paragraph(h, th) for h in headers]]

    # 6 segments
    for s in range(1, 7):
        row = [Paragraph(f"<b>Seg {s}</b>", td)]
        for c in range(1, 14):
            t = c - s + 1
            if 1 <= t <= 8:
                cell_p = Paragraph(
                    f"<font color='{t_theme.accent}'><b>T{t}</b></font>", td
                )
            else:
                cell_p = Paragraph("", td)
            row.append(cell_p)
        data.append(row)

    widths = [55] + [33] * 13
    t = Table(data, colWidths=widths)

    style = [
        ("BACKGROUND", (0, 0), (-1, 0), t_theme.rl(t_theme.table_hdr)),
        ("GRID", (0, 0), (-1, -1), 0.5, t_theme.rl(t_theme.table_bdr)),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 2),
        ("RIGHTPADDING", (0, 0), (-1, -1), 2),
    ]

    for i in range(1, 7):
        row_bg = t_theme.surface if i % 2 == 1 else t_theme.surface_alt
        style.append(("BACKGROUND", (0, i), (-1, i), t_theme.rl(row_bg)))

    t.setStyle(TableStyle(style))
    add(t)
    sp(10)


draw_spacetime_table()
sp(10)

# -- Q5 (d) / Q5 (d) / Q5 (a) & (d) [OVERLAPPED] --
chap_box(
    "Q5. d) Give a survey of Hazards in pipeline. [10 Marks] (June 2022)\n"
    "[AND]\n"
    "Q5. d) Discuss different techniques of parallel processing. What are the advantages of pipelining? Discuss different pipeline hazards in detail. [10 Marks] (June 2024)\n"
    "[AND]\n"
    "Q5. a) What are the advantages of parallel processing? Write some techniques of parallel processing. [3 Marks] (June 2023)\n"
    "[AND]\n"
    "Q5. d) Give a survey of Hazards in pipeline. [10 Marks] (June 2023)"
)
section("Techniques of Parallel Processing")
body(
    "Parallel processing is the simultaneous execution of multiple instructions or tasks to increase "
    "computational throughput. Techniques include:"
)
bullet(
    [
        "<b>1. Pipelining:</b> Overlaps the execution of consecutive instructions in a segmented datapath.",
        "<b>2. Vector and Array Processing:</b> Performs the same operation on a vector of data in parallel (SIMD).",
        "<b>3. Superscalar Execution:</b> Multiple execution units in a single processor enable fetching and issuing "
        "multiple instructions in parallel per clock cycle.",
        "<b>4. Multiprocessing:</b> Uses two or more CPUs sharing memory/interconnections to execute multiple programs in parallel (MIMD).",
    ]
)

section("Advantages of Parallel Processing")
bullet(
    [
        "<b>Higher Throughput:</b> Increases instruction execution rate by processing multiple data items or instruction steps concurrently.",
        "<b>Time Reduction:</b> Drastically cuts computation time for complex scientific and engineering simulations.",
        "<b>Modular Scalability:</b> Provides a path to scale computational capacity by adding processors rather than increasing single-core clock frequencies (bounded by heat dissipation limits).",
        "<b>Fault Tolerance &amp; Reliability:</b> In multi-processor configurations, if one CPU fails, others can take over the workload, preventing complete system crashes.",
    ]
)

section("Advantages of Pipelining")
bullet(
    [
        "<b>Increased Throughput:</b> Enables the CPU to complete one instruction per clock cycle once the pipeline is full.",
        "<b>Efficient Resource Utilization:</b> Keeps different functional units (Fetch, Decode, ALU, Memory) active simultaneously.",
        "<b>Faster Execution:</b> Drastically reduces the execution time of instruction streams compared to non-pipelined execution.",
    ]
)

section("Pipeline Hazards Survey & Analysis")
body(
    "A pipeline hazard is any situation that prevents the next instruction in the instruction stream "
    "from executing in its designated clock cycle. Hazards reduce pipeline performance and are "
    "grouped into three main categories:"
)
bullet(
    [
        "<b>1. Structural Hazards (Resource Conflicts):</b> Occurs when two or more instructions in different stages "
        "attempt to access the same physical hardware resource simultaneously.<br/>"
        "• <i>Example:</i> A single-port memory is accessed for Instruction Fetch (IF) and Data memory Read/Write (MEM) at once.<br/>"
        "• <i>Solutions:</i> Introduce separate instruction and data caches (Harvard cache layout) or stall the pipeline.",
        "<b>2. Data Hazards (Data Dependency):</b> Occurs when an instruction depends on the result of a previous "
        "instruction that is still executing in the pipeline and has not yet written its result to the register file.<br/>"
        "• <i>RAW (Read-After-Write):</i> Operand is read before being written by predecessor (most common).<br/>"
        "• <i>WAR (Write-After-Read):</i> Destination is overwritten before being read.<br/>"
        "• <i>WAW (Write-After-Write):</i> Outputs written out of order.<br/>"
        "• <i>Solutions:</i> <b>Register Forwarding / Bypassing</b> (routing result directly from ALU output to input), "
        "compiler instruction scheduling, or stalling (inserting bubbles).",
        "<b>3. Control Hazards (Branch Conflicts):</b> Occurs when a conditional branch instruction is fetched, and the "
        "next instruction address cannot be determined because the branch decision and target address are still being computed.<br/>"
        "• <i>Solutions:</i> <b>Branch Prediction</b> (static or dynamic prediction using BTB), prefetching target, "
        "or **Delayed Branching** (executing instructions in branch delay slots).",
    ]
)

section("Example of RAW Data Hazard & Stall")
code_block("""
  Instruction Sequence:
    ADD R1, R2, R3    ; R1 <- R2 + R3 (Writes to R1 in WB stage)
    SUB R4, R1, R5    ; R4 <- R1 - R5 (Reads R1 in ID stage -- RAW Hazard!)

  Without Bypassing (Stall Inserted):
    Cycle:  1   2   3   4   5   6   7   8
    ADD:   IF  ID  EX  MEM WB
    SUB:       IF  ID  --  --  EX  MEM WB   (2-cycle stall inserted!)
""")
sp(10)

# -- Q5 (e) / Q5 (c) [OVERLAPPED] --
chap_box(
    "Q5. e) [OR] Define multiprocessors. Write its characteristics. [10 Marks] (June 2022)\n"
    "[AND]\n"
    "Q5. c) Write and explain the characteristics of Multiprocessors. [4 Marks] (June 2024)"
)
section("Definition of Multiprocessor Systems")
definition(
    "<b>Multiprocessor System:</b> A computer system containing two or more Central Processing Units (CPUs) "
    "that share common memory and I/O channels, operating under a single integrated operating system. It enables "
    "parallel processing by executing multiple threads or instructions simultaneously."
)

section("Key Characteristics of Multiprocessors")
bullet(
    [
        "<b>1. MIMD Classification:</b> Multiprocessors are classified as Multiple Instruction stream, Multiple Data "
        "stream (MIMD) systems under Flynn's Taxonomy.",
        "<b>2. Tightly Coupled vs Loosely Coupled:</b><br/>"
        "• <i>Shared Memory (Tightly Coupled):</i> All processors share a global physical memory space. Communication "
        "occurs through reading/writing shared variables.<br/>"
        "• <i>Distributed Memory (Loosely Coupled):</i> Each processor has its own local memory. Processors communicate "
        "by passing message packets over a high-speed network.",
        "<b>3. Interconnection Topologies:</b> Processors are connected to memory/IO using architectures such as "
        "Time-shared Common Bus, Multiport Memory, Crossbar Switch, or Multistage Switching Networks (e.g., Omega Network).",
        "<b>4. Cache Coherence Problem:</b> Because each processor has a private cache, copies of shared data can become "
        "inconsistent. Systems must use cache coherence protocols (Snooping/Directory-based, e.g., MESI) to maintain consistency.",
        "<b>5. Operating System (SMP vs Master-Slave):</b> Operating systems manage task scheduling. In Symmetric "
        "Multiprocessing (SMP), all CPUs are equal. In Master-Slave, one CPU directs other worker CPUs.",
        "<b>6. Synchronization primitives:</b> Requires hardware-supported atomic operations (e.g., Test-and-Set) to implement "
        "semaphores, mutexes, and prevent race conditions.",
    ]
)


# =============================================================================
#  BUILD DOCUMENT
# =============================================================================
sp(10)
rule(active_theme.rl(active_theme.accent), 1.0)
sp(6)
add(
    Paragraph(
        "Computer Architecture IT-404 PYQ 2022, 2023 &amp; 2024 Solutions  |  UIT-RGPV (Autonomous) Bhopal",
        en.COVER_SUB,
    )
)

build_doc(
    "CA_PYQ_Answers.pdf",
    title="Computer Architecture - 2022, 2023 &amp; 2024 Exam Solutions",
    author="Bharat Dangi",
)
print("Generated: CA_PYQ_Answers.pdf")
