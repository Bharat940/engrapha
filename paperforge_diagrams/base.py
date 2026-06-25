from __future__ import annotations

import os

from reportlab.graphics import renderPDF
from reportlab.graphics.shapes import Drawing
from reportlab.platypus import Paragraph, Flowable
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER


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
            else __import__("paperforge_diagrams.theme", fromlist=["DARK"]).DARK
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
