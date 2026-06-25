"""
paperforge_notes.packet -- Frame/packet format diagram helpers.

Provides two complementary frame display functions:

  frame_format(caption, fields) -- Horizontal field-name / field-size row table.
  packet_format(caption, fields, bit_ruler) -- 32-bit RFC-style bit-grid.

Both write to the paperforge_notes.helpers.story list by default.
"""

from __future__ import annotations

from typing import Any

from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle

from .theme import get_theme
from .styles import S

# Counters ensure unique ReportLab style names within a document session.
_ff_counter = 0
_pf_counter = 0


def frame_format(caption: str, fields: list[tuple[str, str]]) -> None:
    """
    Render a horizontal frame diagram.

    Row 1: field names (themed accent, bold).
    Row 2: field sizes (muted text_dim italic).
    Column widths are proportional to the longest text in each field.
    """
    from .helpers import add, sp

    global _ff_counter
    _ff_counter += 1
    uid = f"FF{_ff_counter}"

    t_theme = get_theme()

    th = S(
        f"PN_FF_H_{uid}",
        fontSize=8.5,
        textColor=t_theme.rl(t_theme.accent),
        fontName="Helvetica-Bold",
        alignment=TA_CENTER,
        leading=11,
    )
    td = S(
        f"PN_FF_D_{uid}",
        fontSize=7.5,
        textColor=t_theme.rl(t_theme.text_dim),
        fontName="Helvetica-Oblique",
        alignment=TA_CENTER,
        leading=10,
    )

    headers = [Paragraph(f"<b>{name}</b>", th) for name, _ in fields]
    sizes = [Paragraph(size, td) for _, size in fields]
    data = [headers, sizes]

    total_chars = sum(max(len(name), len(size)) for name, size in fields)
    col_widths = [
        max(28.0, 493.0 * max(len(name), len(size)) / total_chars)
        for name, size in fields
    ]
    scale = 493.0 / sum(col_widths)
    col_widths = [w * scale for w in col_widths]

    t = Table(data, colWidths=col_widths)
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), t_theme.rl(t_theme.surface)),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("GRID", (0, 0), (-1, -1), 0.75, t_theme.rl(t_theme.table_bdr)),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                ("LEFTPADDING", (0, 0), (-1, -1), 2),
                ("RIGHTPADDING", (0, 0), (-1, -1), 2),
            ]
        )
    )
    setattr(t, "_is_frame_format", True)
    add(t)
    if caption:
        add(Spacer(1, 4))
        add(
            Paragraph(
                f"<i>{caption}</i>",
                S(
                    f"PN_FF_CAP_{uid}",
                    fontSize=8.5,
                    textColor=t_theme.rl(t_theme.text_dim),
                    fontName="Helvetica-Oblique",
                    alignment=TA_CENTER,
                    leading=12,
                ),
            )
        )
    sp(6)


def packet_format(
    caption: str,
    fields: list[tuple[str, int]],
    bit_ruler: bool = True,
) -> None:
    """
    Render an RFC/Tanenbaum-style 32-bit-aligned packet header grid.

    fields: list of (name, bit_width) tuples. Fields wider than 32 bits
            span multiple rows (e.g. IP source address = 32 bits fills one row;
            IPv6 source address = 128 bits fills four rows).
    """
    from .helpers import add, sp

    global _pf_counter
    _pf_counter += 1
    uid = f"PF{_pf_counter}"

    t_theme = get_theme()

    ruler_style = S(
        f"PN_PF_RULER_{uid}",
        fontSize=6.5,
        textColor=t_theme.rl(t_theme.text_dim),
        fontName="Helvetica-Bold",
        alignment=TA_CENTER,
        leading=8,
    )

    # -- Split fields into 32-bit grid rows -----------------------------------
    grid_rows: list[list[tuple[str, int]]] = []
    current_row: list[tuple[str, int]] = []
    current_width = 0

    for name, width in fields:
        if width >= 32 and current_width > 0:
            current_row.append(("", 32 - current_width))
            grid_rows.append(current_row)
            current_row = []
            current_width = 0
        if width >= 32:
            grid_rows.append([(name, width)])
        else:
            if current_width + width > 32:
                current_row.append(("", 32 - current_width))
                grid_rows.append(current_row)
                current_row = []
                current_width = 0
            current_row.append((name, width))
            current_width += width
            if current_width == 32:
                grid_rows.append(current_row)
                current_row = []
                current_width = 0

    if current_row:
        current_row.append(("", 32 - current_width))
        grid_rows.append(current_row)

    # -- Build cell matrix -----------------------------------------------------
    matrix: list[list[Any]] = []
    spans: list[tuple[Any, ...]] = []

    if bit_ruler:
        ruler_cells: list[Any] = [""] * 32
        for col_idx in [0, 4, 8, 16, 24, 31]:
            ruler_cells[col_idx] = Paragraph(str(col_idx), ruler_style)
        matrix.append(ruler_cells)
        ruler_offset = 1
    else:
        ruler_offset = 0

    current_rl_row = ruler_offset
    for r_idx, r_fields in enumerate(grid_rows):
        max_height = 1
        for name, width in r_fields:
            if width > 32:
                max_height = max(max_height, width // 32)
        for _ in range(max_height):
            matrix.append([""] * 32)

        col_cursor = 0
        for name, width in r_fields:
            if not name and width == 0:
                continue
            if width == 0:
                continue

            if width > 32:
                f_sz = 7.5
                l_ing = 11.0
            elif width >= 16:
                f_sz = 8.0
                l_ing = 12.0
            elif width >= 8:
                f_sz = 7.5
                l_ing = 11.0
            else:
                f_sz = 6.0
                l_ing = 9.0

            if name:
                cell_th = S(
                    f"PN_PF_H_{uid}_{r_idx}_{col_cursor}",
                    fontSize=f_sz,
                    textColor=t_theme.rl(t_theme.accent),
                    fontName="Helvetica-Bold",
                    alignment=TA_CENTER,
                    leading=l_ing,
                )
                dim_color = t_theme.text_dim
                if width >= 8:
                    text = f"<b>{name}</b><br/><font size=5.5 color='{dim_color}'>{width} bits</font>"
                else:
                    text = f"<b>{name}</b><br/><font size=5.0 color='{dim_color}'>{width}</font>"
                text_p = Paragraph(text, cell_th)
            else:
                text_p = ""

            matrix[current_rl_row][col_cursor] = text_p
            start_col = col_cursor
            end_col = col_cursor + min(width, 32) - 1
            start_row = current_rl_row
            end_row = current_rl_row + max_height - 1
            if start_col != end_col or start_row != end_row:
                spans.append(("SPAN", (start_col, start_row), (end_col, end_row)))
            col_cursor += min(width, 32)

        current_rl_row += max_height

    # -- Render ---------------------------------------------------------------
    CW_PTS = 493.0  # standard content width in points
    col_widths_cells = [CW_PTS / 32.0] * 32
    row_heights: list[float] = []
    if bit_ruler:
        row_heights.append(10)
    for _ in range(len(matrix) - (1 if bit_ruler else 0)):
        row_heights.append(20)

    t = Table(matrix, colWidths=col_widths_cells, rowHeights=row_heights)
    style_cmds: list[Any] = [
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
        ("LEFTPADDING", (0, 0), (-1, -1), 1),
        ("RIGHTPADDING", (0, 0), (-1, -1), 1),
    ]
    start_grid_row = 1 if bit_ruler else 0
    style_cmds += [
        ("GRID", (0, start_grid_row), (-1, -1), 0.75, t_theme.rl(t_theme.table_bdr)),
        ("BACKGROUND", (0, start_grid_row), (-1, -1), t_theme.rl(t_theme.surface)),
    ]
    style_cmds.extend(spans)
    t.setStyle(TableStyle(style_cmds))
    setattr(t, "_is_packet_format", True)
    add(t)
    if caption:
        add(Spacer(1, 4))
        add(
            Paragraph(
                f"<i>{caption}</i>",
                S(
                    f"PN_PF_CAP_{uid}",
                    fontSize=8.5,
                    textColor=t_theme.rl(t_theme.text_dim),
                    fontName="Helvetica-Oblique",
                    alignment=TA_CENTER,
                    leading=12,
                ),
            )
        )
    sp(6)


__all__ = ["frame_format", "packet_format"]
