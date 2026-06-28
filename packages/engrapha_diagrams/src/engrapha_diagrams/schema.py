from __future__ import annotations

from typing import Any
from .base import DiagramBase
from .theme import DiagramTheme
from . import shapes as S


class SchemaDiagram(DiagramBase):
    """
    Database Schema Diagram builder.
    Draws detailed table structures with fields, data types, primary/foreign key markers,
    and orthogonal relation lines.
    """

    def __init__(
        self,
        width: float,
        height: float,
        theme: DiagramTheme | None = None,
        caption: str | None = None,
    ) -> None:
        super().__init__(width, height, theme, caption)
        self._tables: dict[str, dict[str, Any]] = {}
        self._relations: list[tuple[str, str, str, str]] = []
        self._table_w = 140.0
        self._header_h = 24.0
        self._row_h = 16.0

    def table(
        self,
        name: str,
        columns: list[tuple[str, str, dict[str, bool]]],
        x: float = 0.0,
        y: float = 0.0,
    ) -> "SchemaDiagram":
        """
        Add a table structure to the diagram.

        Columns format:
            [("id", "INTEGER", {"pk": True}), ("user_id", "INTEGER", {"fk": True})]
        """
        self._tables[name] = {
            "columns": columns,
            "x": x,
            "y": y,
        }
        return self

    def relation(
        self,
        from_table: str,
        from_col: str,
        to_table: str,
        to_col: str,
    ) -> "SchemaDiagram":
        """Add a foreign key relation link between two columns."""
        self._relations.append((from_table, from_col, to_table, to_col))
        return self

    def _normalize_bounds(self) -> None:
        if not self._tables:
            return

        min_x, max_x = float("inf"), float("-inf")
        min_y, max_y = float("inf"), float("-inf")
        for name, tb in self._tables.items():
            tx, ty = tb["x"], tb["y"]
            cols = tb["columns"]
            tb_h = self._header_h + self._row_h * len(cols)

            min_x = min(min_x, tx)
            max_x = max(max_x, tx + self._table_w)
            min_y = min(min_y, ty)
            max_y = max(max_y, ty + tb_h)

        margin = 35.0
        calculated_width = max_x - min_x + margin * 2
        calculated_height = max_y - min_y + margin * 2

        shift_x = margin - min_x
        shift_y = margin - min_y

        for name in self._tables:
            self._tables[name]["x"] += shift_x
            self._tables[name]["y"] += shift_y

        self.width = calculated_width
        self.height = calculated_height
        if hasattr(self, "drawing") and self.drawing:
            self.drawing.width = self.width
            self.drawing.height = self.height

    def build(self) -> None:
        t = self.theme

        # Auto-layout tables if they are all at (0, 0)
        all_zeros = all(
            tb["x"] == 0.0 and tb["y"] == 0.0 for tb in self._tables.values()
        )
        if all_zeros and self._tables:
            from .layout import auto_layout_graph

            edges = [(r[0], r[2]) for r in self._relations]
            node_ids = list(self._tables.keys())

            # Use spacious layouts to keep schema tables apart
            coords = auto_layout_graph(
                node_ids=node_ids,
                edges=edges,
                width=self.width,
                height=self.height,
                margin_x=70.0,
                margin_y=60.0,
                direction="TB",
                node_spacing=180.0,
                layer_spacing=150.0,
            )

            for name, (cx, cy) in coords.items():
                cols = self._tables[name]["columns"]
                tb_h = self._header_h + self._row_h * len(cols)
                self._tables[name]["x"] = cx - self._table_w / 2.0
                self._tables[name]["y"] = cy - tb_h / 2.0

            self._normalize_bounds()
        else:
            self._normalize_bounds()

        # Draw tables
        for name, tb in self._tables.items():
            tx, ty = tb["x"], tb["y"]
            cols = tb["columns"]
            tb_h = self._header_h + self._row_h * len(cols)

            # Draw table body rect
            self._add(
                S.plain_rect(
                    tx,
                    ty,
                    self._table_w,
                    tb_h,
                    fill=t.class_body_fill,
                    stroke=t.class_stroke,
                    stroke_width=1.2,
                )
            )

            # Draw table header rect
            self._add(
                S.plain_rect(
                    tx,
                    ty + tb_h - self._header_h,
                    self._table_w,
                    self._header_h,
                    fill=t.class_header_fill,
                    stroke=t.class_stroke,
                    stroke_width=1.2,
                )
            )

            # Draw table name (Header Text)
            self._add(
                S.label(
                    tx + self._table_w / 2.0,
                    ty + tb_h - self._header_h + 7.0,
                    name,
                    font=t.font_name_bold,
                    size=10.0,
                    color=t.class_header_text,
                    anchor="middle",
                )
            )

            # Draw column entries
            for idx, col in enumerate(cols):
                col_name, col_type, col_attrs = col
                row_y = (
                    ty + tb_h - self._header_h - self._row_h * idx - self._row_h + 4.0
                )

                # Determine styling colors
                text_color = t.class_body_text
                font_name = t.font_name

                name_str = col_name
                if col_attrs.get("pk"):
                    name_str += " (PK)"
                    text_color = t.pk_text
                    font_name = t.font_name_bold
                elif col_attrs.get("fk"):
                    name_str += " (FK)"
                    text_color = t.relation_text

                # Draw column name
                self._add(
                    S.label(
                        tx + 8.0,
                        row_y,
                        name_str,
                        font=font_name,
                        size=8.5,
                        color=text_color,
                        anchor="start",
                    )
                )

                # Draw column type
                self._add(
                    S.label(
                        tx + self._table_w - 8.0,
                        row_y,
                        col_type,
                        font=t.font_name_mono,
                        size=7.5,
                        color=t.class_method_text,
                        anchor="end",
                    )
                )

        # Determine theme darkness for edge color palette
        is_dark = (
            t.surface.startswith("#1")
            or t.surface.startswith("#0")
            or t.surface.startswith("#2")
        )
        if is_dark:
            edge_colors = [
                "#38bdf8",
                "#34d399",
                "#f472b6",
                "#fb923c",
                "#a78bfa",
                "#facc15",
            ]
        else:
            edge_colors = [
                "#0284c7",
                "#059669",
                "#db2777",
                "#ea580c",
                "#7c3aed",
                "#ca8a04",
            ]

        # Draw relationships (orthogonal routing with offset to prevent overlap)
        for rel_idx, (from_table, from_col, to_table, to_col) in enumerate(
            self._relations
        ):
            if from_table not in self._tables or to_table not in self._tables:
                continue

            tb1 = self._tables[from_table]
            tb2 = self._tables[to_table]

            # Find column index
            idx1 = next(
                (i for i, c in enumerate(tb1["columns"]) if c[0] == from_col), 0
            )
            idx2 = next((i for i, c in enumerate(tb2["columns"]) if c[0] == to_col), 0)

            tb1_h = self._header_h + self._row_h * len(tb1["columns"])
            tb2_h = self._header_h + self._row_h * len(tb2["columns"])

            y1 = (
                tb1["y"]
                + tb1_h
                - self._header_h
                - self._row_h * idx1
                - self._row_h / 2.0
            )
            y2 = (
                tb2["y"]
                + tb2_h
                - self._header_h
                - self._row_h * idx2
                - self._row_h / 2.0
            )

            line_color = edge_colors[rel_idx % len(edge_colors)]

            # If tables overlap horizontally (even if not perfectly vertically aligned), route to the side
            if abs(tb1["x"] - tb2["x"]) < self._table_w:
                # 1. Left-side candidate
                x1_l = tb1["x"]
                x2_l = tb2["x"]
                offset_l = -8.0 - (rel_idx % 4) * 8.0
                mid_x_l = min(tb1["x"], tb2["x"]) + offset_l

                left_collisions = 0
                for name, tb in self._tables.items():
                    if name in (from_table, to_table):
                        continue
                    tx = tb["x"]
                    ty = tb["y"]
                    tb_h = self._header_h + self._row_h * len(tb["columns"])
                    if tx <= mid_x_l <= tx + self._table_w:
                        if not (max(y1, y2) < ty or min(y1, y2) > ty + tb_h):
                            left_collisions += 1

                # 2. Right-side candidate
                x1_r = tb1["x"] + self._table_w
                x2_r = tb2["x"] + self._table_w
                offset_r = 8.0 + (rel_idx % 4) * 8.0
                mid_x_r = (
                    max(tb1["x"] + self._table_w, tb2["x"] + self._table_w) + offset_r
                )

                right_collisions = 0
                for name, tb in self._tables.items():
                    if name in (from_table, to_table):
                        continue
                    tx = tb["x"]
                    ty = tb["y"]
                    tb_h = self._header_h + self._row_h * len(tb["columns"])
                    if tx <= mid_x_r <= tx + self._table_w:
                        if not (max(y1, y2) < ty or min(y1, y2) > ty + tb_h):
                            right_collisions += 1

                # Choose best side
                if left_collisions < right_collisions:
                    use_left = True
                elif right_collisions < left_collisions:
                    use_left = False
                else:
                    # Tie-break based on average position
                    avg_x = (tb1["x"] + tb2["x"]) / 2.0
                    use_left = avg_x >= self.width / 2.0

                if use_left:
                    x1, x2, mid_x = x1_l, x2_l, mid_x_l
                else:
                    x1, x2, mid_x = x1_r, x2_r, mid_x_r

                self._add(S.solid_line(x1, y1, mid_x, y1, color=line_color, width=1.2))
                self._add(
                    S.solid_line(mid_x, y1, mid_x, y2, color=line_color, width=1.2)
                )
                self._add(
                    S.arrow_line(
                        mid_x,
                        y2,
                        x2,
                        y2,
                        color=line_color,
                        width=1.2,
                        arrow_end=True,
                        arrow_size=6.0,
                    )
                )
            # Determine whether source is left or right of target
            elif tb1["x"] + self._table_w / 2.0 < tb2["x"] + self._table_w / 2.0:
                # Source on left table, target on right table
                x1 = tb1["x"] + self._table_w
                x2 = tb2["x"]

                # Try different offsets to find one with minimum table collisions
                offsets = [-20.0, -10.0, 0.0, 10.0, 20.0]
                best_mid_x = (x1 + x2) / 2.0
                min_collisions = 999

                for off in offsets:
                    cand_mid_x = (x1 + x2) / 2.0 + off
                    min_x = min(x1, x2) + 25.0
                    max_x = max(x1, x2) - 25.0
                    if max_x > min_x:
                        cand_mid_x = max(min_x, min(max_x, cand_mid_x))
                    else:
                        cand_mid_x = (x1 + x2) / 2.0

                    # Count collisions
                    collisions = 0
                    for name, tb in self._tables.items():
                        if name in (from_table, to_table):
                            continue
                        tx = tb["x"]
                        ty = tb["y"]
                        tb_h = self._header_h + self._row_h * len(tb["columns"])
                        if tx <= cand_mid_x <= tx + self._table_w:
                            if not (max(y1, y2) < ty or min(y1, y2) > ty + tb_h):
                                collisions += 1

                    if collisions < min_collisions:
                        min_collisions = collisions
                        best_mid_x = cand_mid_x

                mid_x = best_mid_x

                # Draw orthogonal segments
                self._add(S.solid_line(x1, y1, mid_x, y1, color=line_color, width=1.2))
                self._add(
                    S.solid_line(mid_x, y1, mid_x, y2, color=line_color, width=1.2)
                )
                # Add segment with arrow pointing at target
                self._add(
                    S.arrow_line(
                        mid_x,
                        y2,
                        x2,
                        y2,
                        color=line_color,
                        width=1.2,
                        arrow_end=True,
                        arrow_size=6.0,
                    )
                )
            else:
                # Source on right table, target on left table
                x1 = tb1["x"]
                x2 = tb2["x"] + self._table_w

                # Try different offsets to find one with minimum table collisions
                offsets = [-20.0, -10.0, 0.0, 10.0, 20.0]
                best_mid_x = (x1 + x2) / 2.0
                min_collisions = 999

                for off in offsets:
                    cand_mid_x = (x1 + x2) / 2.0 + off
                    min_x = min(x1, x2) + 25.0
                    max_x = max(x1, x2) - 25.0
                    if max_x > min_x:
                        cand_mid_x = max(min_x, min(max_x, cand_mid_x))
                    else:
                        cand_mid_x = (x1 + x2) / 2.0

                    # Count collisions
                    collisions = 0
                    for name, tb in self._tables.items():
                        if name in (from_table, to_table):
                            continue
                        tx = tb["x"]
                        ty = tb["y"]
                        tb_h = self._header_h + self._row_h * len(tb["columns"])
                        if tx <= cand_mid_x <= tx + self._table_w:
                            if not (max(y1, y2) < ty or min(y1, y2) > ty + tb_h):
                                collisions += 1

                    if collisions < min_collisions:
                        min_collisions = collisions
                        best_mid_x = cand_mid_x

                mid_x = best_mid_x

                self._add(S.solid_line(x1, y1, mid_x, y1, color=line_color, width=1.2))
                self._add(
                    S.solid_line(mid_x, y1, mid_x, y2, color=line_color, width=1.2)
                )
                self._add(
                    S.arrow_line(
                        mid_x,
                        y2,
                        x2,
                        y2,
                        color=line_color,
                        width=1.2,
                        arrow_end=True,
                        arrow_size=6.0,
                    )
                )
