from __future__ import annotations

from .architecture import ArchitectureDiagram
from .theme import DiagramTheme
from . import shapes as S


class AWSDiagram(ArchitectureDiagram):
    """
    AWS Infrastructure Diagram builder.
    Inherits from ArchitectureDiagram and draws custom vector-native AWS resource icons.

    Defaults to ``orientation="vertical"`` (top-to-bottom flow) which matches the
    conventional AWS architecture style: compute on top, data stores below.
    Pass ``orientation="horizontal"`` to flip to a left-to-right layout instead.
    """

    def __init__(
        self,
        width: float,
        height: float,
        theme: DiagramTheme | None = None,
        caption: str | None = None,
        orientation: str = "vertical",
    ) -> None:
        super().__init__(width, height, theme, caption, orientation)

    def ec2(
        self,
        name: str,
        label: str = "",
        x: float | None = None,
        y: float | None = None,
    ) -> "AWSDiagram":
        """Add an EC2 Virtual Server node."""
        self._add_node(name, "ec2", label, x, y)
        return self

    def rds(
        self,
        name: str,
        label: str = "",
        x: float | None = None,
        y: float | None = None,
    ) -> "AWSDiagram":
        """Add an RDS Database node."""
        self._add_node(name, "rds", label, x, y)
        return self

    def s3(
        self,
        name: str,
        label: str = "",
        x: float | None = None,
        y: float | None = None,
    ) -> "AWSDiagram":
        """Add an S3 Simple Storage bucket node."""
        self._add_node(name, "s3", label, x, y)
        return self

    def lambda_fn(
        self,
        name: str,
        label: str = "",
        x: float | None = None,
        y: float | None = None,
    ) -> "AWSDiagram":
        """Add a Lambda Serverless function node."""
        self._add_node(name, "lambda_fn", label, x, y)
        return self

    def sqs(
        self,
        name: str,
        label: str = "",
        x: float | None = None,
        y: float | None = None,
    ) -> "AWSDiagram":
        """Add an SQS Queue node."""
        self._add_node(name, "sqs", label, x, y)
        return self

    def build(self) -> None:
        # Pre-assign standard kinds so parent layout knows what to do
        for nd in self._nodes.values():
            kind = nd["kind"]
            if kind in ("ec2", "lambda_fn"):
                nd["kind_orig"] = kind
                nd["kind"] = "service"
            elif kind in ("rds", "s3"):
                nd["kind_orig"] = kind
                nd["kind"] = "database"
            elif kind == "sqs":
                nd["kind_orig"] = kind
                nd["kind"] = "queue"
            else:
                nd["kind_orig"] = kind

        # Let parent compute coordinates
        super().build()

        # Draw AWS-specific icons over the generic architecture nodes. Older
        # versions buffered shapes internally, but current diagrams draw
        # directly into the ReportLab drawing.
        t = self.theme
        from reportlab.graphics.shapes import Group

        # Draw custom AWS nodes
        for name, nd in self._nodes.items():
            nx, ny = nd["x"], nd["y"]
            kind = nd.get("kind_orig", nd["kind"])
            label_text = nd["label"]

            x_left = nx - self._node_w / 2.0
            y_bottom = ny - self._node_h / 2.0

            node_grp = Group()
            setattr(node_grp, "_is_node", True)

            # Node card fill and stroke
            fill_color = (
                t.surface_alt if kind in ("ec2", "lambda_fn", "sqs") else t.surface
            )
            stroke_color = t.decision_stroke if kind in ("rds", "s3") else t.node_stroke

            node_grp.add(
                S.rounded_rect(
                    x_left,
                    y_bottom,
                    self._node_w,
                    self._node_h,
                    rx=3.0,
                    fill=fill_color,
                    stroke=stroke_color,
                    stroke_width=1.3,
                )
            )

            # Draw vector icons inside node (positioned on the left side)
            icon_x = x_left + 14.0
            icon_y = ny
            icon_color = stroke_color

            if kind == "ec2":
                # Upgraded Server Blade Chassis
                node_grp.add(
                    S.plain_rect(
                        icon_x - 8.0,
                        icon_y - 8.0,
                        16.0,
                        16.0,
                        fill=fill_color,
                        stroke=icon_color,
                        stroke_width=1.0,
                    )
                )
                node_grp.add(
                    S.solid_line(
                        icon_x - 6.0,
                        icon_y + 4.0,
                        icon_x + 2.0,
                        icon_y + 4.0,
                        color=icon_color,
                        width=0.8,
                    )
                )
                node_grp.add(
                    S.solid_line(
                        icon_x - 6.0,
                        icon_y,
                        icon_x + 2.0,
                        icon_y,
                        color=icon_color,
                        width=0.8,
                    )
                )
                node_grp.add(
                    S.solid_line(
                        icon_x - 6.0,
                        icon_y - 4.0,
                        icon_x + 2.0,
                        icon_y - 4.0,
                        color=icon_color,
                        width=0.8,
                    )
                )
                node_grp.add(
                    S.circle(
                        icon_x + 4.5,
                        icon_y + 4.0,
                        1.0,
                        fill=t.terminal_stroke,
                        stroke="none",
                    )
                )
                node_grp.add(
                    S.circle(
                        icon_x + 4.5, icon_y, 1.0, fill=t.terminal_stroke, stroke="none"
                    )
                )
                node_grp.add(
                    S.circle(
                        icon_x + 4.5,
                        icon_y - 4.0,
                        1.0,
                        fill=t.terminal_stroke,
                        stroke="none",
                    )
                )
            elif kind == "rds":
                # Multi-disc Database Cylinder with Rings
                node_grp.add(
                    S.cylinder(
                        icon_x - 7.0,
                        icon_y - 9.0,
                        14.0,
                        18.0,
                        fill=fill_color,
                        stroke=icon_color,
                        stroke_width=1.0,
                    )
                )
                node_grp.add(
                    S.solid_line(
                        icon_x - 7.0,
                        icon_y + 2.0,
                        icon_x + 7.0,
                        icon_y + 2.0,
                        color=icon_color,
                        width=0.8,
                    )
                )
                node_grp.add(
                    S.solid_line(
                        icon_x - 7.0,
                        icon_y - 3.0,
                        icon_x + 7.0,
                        icon_y - 3.0,
                        color=icon_color,
                        width=0.8,
                    )
                )
            elif kind == "s3":
                # Trapezoidal Bucket with Curved Handle
                points = [
                    icon_x - 6.0,
                    icon_y - 8.0,
                    icon_x + 6.0,
                    icon_y - 8.0,
                    icon_x + 8.0,
                    icon_y + 5.0,
                    icon_x - 8.0,
                    icon_y + 5.0,
                ]
                node_grp.add(
                    S.polygon(
                        points, fill=fill_color, stroke=icon_color, stroke_width=1.0
                    )
                )
                node_grp.add(
                    S.oval(
                        icon_x,
                        icon_y + 5.0,
                        8.0,
                        2.5,
                        fill=fill_color,
                        stroke=icon_color,
                        stroke_width=1.0,
                    )
                )
                from reportlab.graphics.shapes import Path

                handle = Path()
                handle.moveTo(icon_x - 8.0, icon_y + 5.0)
                handle.curveTo(
                    icon_x - 8.0,
                    icon_y + 11.0,
                    icon_x + 8.0,
                    icon_y + 11.0,
                    icon_x + 8.0,
                    icon_y + 5.0,
                )
                handle.fillColor = None
                handle.strokeColor = S._hex(icon_color)
                handle.strokeWidth = 1.0
                node_grp.add(handle)
            elif kind == "lambda_fn":
                # Actual vector Lambda (λ) logo symbol with rounded line caps
                l_leg1 = S.solid_line(
                    icon_x + 3.5,
                    icon_y + 7.0,
                    icon_x - 3.5,
                    icon_y - 7.0,
                    color=t.note_stroke or icon_color,
                    width=2.2,
                )
                l_leg1.strokeLineCap = 1
                node_grp.add(l_leg1)

                l_leg2 = S.solid_line(
                    icon_x - 0.5,
                    icon_y - 1.0,
                    icon_x + 3.5,
                    icon_y - 7.0,
                    color=t.note_stroke or icon_color,
                    width=2.2,
                )
                l_leg2.strokeLineCap = 1
                node_grp.add(l_leg2)
            elif kind == "sqs":
                # Message Queue Stadium with message slots
                node_grp.add(
                    S.stadium(
                        icon_x - 11.0,
                        icon_y - 6.0,
                        22.0,
                        12.0,
                        fill=fill_color,
                        stroke=icon_color,
                        stroke_width=1.0,
                    )
                )
                node_grp.add(
                    S.plain_rect(
                        icon_x - 8.0,
                        icon_y - 3.0,
                        4.0,
                        6.0,
                        fill=icon_color,
                        stroke="none",
                    )
                )
                node_grp.add(
                    S.plain_rect(
                        icon_x - 2.0,
                        icon_y - 3.0,
                        4.0,
                        6.0,
                        fill=icon_color,
                        stroke="none",
                    )
                )
                node_grp.add(
                    S.plain_rect(
                        icon_x + 4.0,
                        icon_y - 3.0,
                        4.0,
                        6.0,
                        fill=icon_color,
                        stroke="none",
                    )
                )
            else:
                node_grp.add(
                    S.circle(
                        icon_x,
                        icon_y,
                        6.0,
                        fill=fill_color,
                        stroke=icon_color,
                        stroke_width=1.0,
                    )
                )

            # Resource name label
            node_grp.add(
                S.centered_wrapped_label(
                    x_left + 54.0,
                    ny,
                    label_text,
                    self._node_w - 36.0,
                    font=t.font_name_bold,
                    size=7.5,
                    color=t.text,
                )
            )

            self._add(node_grp)
