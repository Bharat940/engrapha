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

    def build(self) -> None:
        t = self.theme

        # Auto-layout tables if they are all at (0, 0)
        all_zeros = all(
            tb["x"] == 0.0 and tb["y"] == 0.0 for tb in self._tables.values()
        )
        if all_zeros and self._tables:
            num_tables = len(self._tables)
            import math

            cols = math.ceil(math.sqrt(num_tables))
            rows = math.ceil(num_tables / cols)

            # Grid spacing
            cell_w = self.width / cols
            cell_h = self.height / rows

            for idx, name in enumerate(sorted(self._tables.keys())):
                r = idx // cols
                c = idx % cols
                # Center table in grid cell
                table_h = self._header_h + self._row_h * len(
                    self._tables[name]["columns"]
                )
                self._tables[name]["x"] = c * cell_w + (cell_w - self._table_w) / 2.0
                self._tables[name]["y"] = self.height - (
                    r * cell_h + (cell_h + table_h) / 2.0
                )

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

        # Draw relationships (orthogonal routing)
        for from_table, from_col, to_table, to_col in self._relations:
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

            # Determine whether source is left or right of target
            if tb1["x"] + self._table_w / 2.0 < tb2["x"] + self._table_w / 2.0:
                # Source on right, target on left
                x1 = tb1["x"] + self._table_w
                x2 = tb2["x"]
                # Direction of routing
                mid_x = (x1 + x2) / 2.0

                # Draw orthogonal segments
                self._add(
                    S.solid_line(x1, y1, mid_x, y1, color=t.line_color, width=1.2)
                )
                self._add(
                    S.solid_line(mid_x, y1, mid_x, y2, color=t.line_color, width=1.2)
                )
                # Add segment with arrow pointing at target
                self._add(
                    S.arrow_line(
                        mid_x,
                        y2,
                        x2,
                        y2,
                        color=t.line_color,
                        width=1.2,
                        arrow_end=True,
                        arrow_size=6.0,
                    )
                )
            else:
                # Source on left, target on right
                x1 = tb1["x"]
                x2 = tb2["x"] + self._table_w
                mid_x = (x1 + x2) / 2.0

                self._add(
                    S.solid_line(x1, y1, mid_x, y1, color=t.line_color, width=1.2)
                )
                self._add(
                    S.solid_line(mid_x, y1, mid_x, y2, color=t.line_color, width=1.2)
                )
                self._add(
                    S.arrow_line(
                        mid_x,
                        y2,
                        x2,
                        y2,
                        color=t.line_color,
                        width=1.2,
                        arrow_end=True,
                        arrow_size=6.0,
                    )
                )
