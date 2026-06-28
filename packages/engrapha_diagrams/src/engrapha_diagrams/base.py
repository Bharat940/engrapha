from __future__ import annotations

import os
import math
from reportlab.graphics import renderPDF
from reportlab.graphics.shapes import Drawing
from reportlab.platypus import Paragraph, Flowable
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER


def point_to_segment_distance(
    px: float, py: float, ax: float, ay: float, bx: float, by: float
) -> float:
    dx = bx - ax
    dy = by - ay
    if dx == 0 and dy == 0:
        return math.hypot(px - ax, py - ay)
    t = ((px - ax) * dx + (py - ay) * dy) / (dx * dx + dy * dy)
    t = max(0.0, min(1.0, t))
    cx = ax + t * dx
    cy = ay + t * dy
    return math.hypot(px - cx, py - cy)


class DiagramBase:
    def __init__(
        self, width: float, height: float, theme=None, caption: str | None = None
    ) -> None:
        if width <= 0:
            raise ValueError("width must be greater than 0")
        if height < 0:
            raise ValueError("height cannot be negative")
        self.width = width
        self.height = height
        self.theme = (
            theme
            if theme is not None
            else __import__("engrapha_diagrams.theme", fromlist=["DARK"]).DARK
        )
        self.caption = caption
        self.drawing = Drawing(self.width, self.height)
        setattr(self.drawing, "_diagram_theme", self.theme)
        self._label_rects: list[tuple[float, float, float, float]] = []
        self._built = False

    def _add(self, shape) -> None:
        if shape is not None:
            self.drawing.add(shape)

    def _ensure_built(self) -> None:
        if not self._built:
            self.build()
            self._built = True

    def as_flowable(self) -> list:
        self._ensure_built()

        flowables: list[Flowable] = [
            ResponsiveDrawingFlowable(self.drawing, caption=self.caption)
        ]
        if self.caption:
            style = ParagraphStyle(
                name="DiagramCaption",
                fontName=self.theme.font_name_italic,
                fontSize=9,
                textColor=self.theme.text,
                alignment=TA_CENTER,
                spaceBefore=6,
                spaceAfter=12,
            )
            flowables.append(Paragraph(self.caption, style))
        return flowables

    def save(self, filename: str) -> None:
        self._ensure_built()
        from reportlab.graphics import renderPDF, renderPM, renderSVG

        ext = os.path.splitext(filename)[1].lower()
        if ext == ".pdf":
            renderPDF.drawToFile(self.drawing, filename)
        elif ext == ".svg":
            renderSVG.drawToFile(self.drawing, filename)
        elif ext in {".png", ".jpg", ".jpeg"}:
            fmt = "PNG" if ext == ".png" else "JPG"
            try:
                renderPM.drawToFile(self.drawing, filename, fmt=fmt)
            except Exception as exc:
                raise RuntimeError(f"rlpycairo backend unavailable: {exc}") from exc
        else:
            raise RuntimeError(f"Unsupported export file format: {ext}")

    def build(self) -> None:
        pass

    def get_non_overlapping_position(
        self, lx: float, ly: float, w: float, h: float
    ) -> tuple[float, float]:
        directions = [
            (0, 0),
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0),
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1),
        ]
        step_x = 5.0
        step_y = 5.0
        for ring in range(25):
            for dx, dy in directions:
                cx = lx + dx * step_x * ring
                cy = ly + dy * step_y * ring
                overlap = False
                for rx, ry, rw, rh in self._label_rects:
                    if abs(cx - rx) < (w + rw) / 2.0 and abs(cy - ry) < (h + rh) / 2.0:
                        overlap = True
                        break
                if not overlap:
                    self._label_rects.append((cx, cy, w, h))
                    return cx, cy
        self._label_rects.append((lx, ly, w, h))
        return lx, ly


    def get_segment_label_position(
        self,
        x1: float,
        y1: float,
        x2: float,
        y2: float,
        w: float,
        h: float,
        segment_type: str,
        label_pos: str = "middle",
        other_segments: list[tuple[float, float, float, float]] | None = None,
    ) -> tuple[float, float]:
        if label_pos == "start":
            pref_frac = 0.25
        elif label_pos == "end":
            pref_frac = 0.75
        else:
            pref_frac = 0.5

        # Try fractions from 0.15 to 0.85 with a step of 0.1
        fractions = [0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75, 0.85]
        
        candidates = []
        if segment_type == "horizontal":
            offsets_y = [10.0, -10.0]
            for frac in fractions:
                cx = x1 + (x2 - x1) * frac
                for oy in offsets_y:
                    cy = y1 + oy
                    candidates.append((cx, cy, frac))
        else:
            offsets_x = [15.0, -15.0]
            for frac in fractions:
                cy = y1 + (y2 - y1) * frac
                for ox in offsets_x:
                    cx = x1 + ox
                    candidates.append((cx, cy, frac))

        best_pos = None
        best_score = float("-inf")

        for cx, cy, frac in candidates:
            # Check hard constraints: overlap with nodes or placed labels
            overlap = False
            for rx, ry, rw, rh in self._label_rects:
                if abs(cx - rx) < (w + rw) / 2.0 and abs(cy - ry) < (h + rh) / 2.0:
                    overlap = True
                    break
            if overlap:
                continue

            # Compute distance to other connection lines
            min_line_dist = float("inf")
            if other_segments:
                for sx1, sy1, sx2, sy2 in other_segments:
                    d = point_to_segment_distance(cx, cy, sx1, sy1, sx2, sy2)
                    if d < min_line_dist:
                        min_line_dist = d

            # Penalize deviation from preferred fraction
            penalty = abs(frac - pref_frac) * 40.0
            
            # Penalize getting too close to other lines
            collision_penalty = 0.0
            if min_line_dist < 12.0:
                collision_penalty = (12.0 - min_line_dist) * 100.0

            score = min_line_dist - penalty - collision_penalty
            if score > best_score:
                best_score = score
                best_pos = (cx, cy)

        if best_pos is not None:
            self._label_rects.append((best_pos[0], best_pos[1], w, h))
            return best_pos

        # Fallback
        if segment_type == "horizontal":
            return self.get_non_overlapping_position((x1 + x2) / 2.0, y1 + 10.0, w, h)
        else:
            return self.get_non_overlapping_position(x1 + 15.0, (y1 + y2) / 2.0, w, h)


class ResponsiveDrawingFlowable(Flowable):
    def __init__(self, drawing: Drawing, caption: str | None = None) -> None:
        super().__init__()
        self.drawing = drawing
        self.caption = caption
        self._scale = 1.0
        self.scale_factor = 1.0
        self.hAlign = "CENTER"

    def wrap(self, aW: float, aH: float) -> tuple[float, float]:
        self._scale = 1.0
        if self.drawing.width > aW and aW > 0:
            self._scale = aW / self.drawing.width

        h = self.drawing.height * self._scale
        # If the scaled height is still too tall AND we are on a relatively fresh page
        # (e.g. > 500 points available), scale it down further to fit the page.
        # If aH is small, we return the large height so ReportLab triggers a page break.
        if h > aH and aH > 500:
            scale_y = aH / self.drawing.height
            if scale_y < self._scale:
                self._scale = scale_y

        self.scale_factor = self._scale
        self.width = max(1.0, self.drawing.width * self._scale)
        self.height = max(1.0, self.drawing.height * self._scale)

        return self.width, self.height

    def draw(self) -> None:
        self.canv.saveState()
        self.canv.scale(self._scale, self._scale)
        renderPDF.draw(self.drawing, self.canv, 0, 0)
        self.canv.restoreState()
