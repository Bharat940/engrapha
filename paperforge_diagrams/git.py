from __future__ import annotations

from typing import Any
from .base import DiagramBase
from .theme import DiagramTheme
from . import shapes as S


class GitDiagram(DiagramBase):
    """
    Git Branch Diagram builder.
    Visualizes horizontal branch lines, commits, parent-child branch points, and merges.
    """

    def __init__(
        self,
        width: float,
        height: float,
        theme: DiagramTheme | None = None,
        caption: str | None = None,
        commit_spacing: float = 65.0,
    ) -> None:
        super().__init__(width, height, theme, caption)
        self._commits: list[dict[str, Any]] = []
        self._branches: dict[str, dict[str, Any]] = {
            "main": {"y": self.height / 2.0, "last_x": 30.0, "color_idx": 0}
        }
        self._branch_y_offset = 40.0
        self._commit_spacing = commit_spacing
        self._current_x = 30.0
        self._operations: list[dict[str, Any]] = []
        self._branch_colors = [
            "#38bdf8",  # cyan
            "#a855f7",  # purple
            "#34d399",  # green
            "#fb923c",  # orange
            "#f87171",  # red
        ]

    def commit(self, branch: str = "main", label: str = "") -> "GitDiagram":
        """Record a commit on a branch."""
        self._operations.append({"type": "commit", "branch": branch, "label": label})
        return self

    def branch(self, parent_branch: str, child_branch: str) -> "GitDiagram":
        """Create a new branch branching from the parent branch."""
        self._operations.append(
            {"type": "branch", "parent": parent_branch, "child": child_branch}
        )
        return self

    def merge(self, from_branch: str, to_branch: str, label: str = "") -> "GitDiagram":
        """Merge from_branch into to_branch."""
        self._operations.append(
            {
                "type": "merge",
                "from": from_branch,
                "to": to_branch,
                "label": label or f"Merge {from_branch}",
            }
        )
        return self

    def build(self) -> None:
        t = self.theme

        # Determine y levels for all branches first
        max_level = 0
        min_level = 0

        # Execute a pre-pass to register all branches and allocate y offsets
        for op in self._operations:
            if op["type"] == "branch":
                child = op["child"]
                parent = op["parent"]
                if child not in self._branches:
                    # Alternating directions: up, down, up, down
                    if max_level <= -min_level:
                        max_level += 1
                        level = max_level
                    else:
                        min_level -= 1
                        level = min_level

                    self._branches[child] = {
                        "y": self.height / 2.0 + level * self._branch_y_offset,
                        "last_x": 30.0,
                        "color_idx": len(self._branches) % len(self._branch_colors),
                    }

        # Initialize last commits map to track connections
        last_commit_pos: dict[str, tuple[float, float]] = {}

        # Draw start of main timeline
        main_y = self._branches["main"]["y"]
        self._add(
            S.solid_line(15.0, main_y, 30.0, main_y, color=t.line_color, width=1.5)
        )
        last_commit_pos["main"] = (30.0, main_y)

        # Draw the operations in order
        for op in self._operations:
            self._current_x += self._commit_spacing

            if op["type"] == "commit":
                branch = op["branch"]
                b_cfg = self._branches[branch]
                bx, by = self._current_x, b_cfg["y"]
                color = self._branch_colors[b_cfg["color_idx"]]

                # Draw connection line from last commit on this branch
                if branch in last_commit_pos:
                    lx, ly = last_commit_pos[branch]
                    self._add(S.solid_line(lx, ly, bx, by, color=color, width=2.0))

                # Draw commit node
                self._add(
                    S.circle(bx, by, 5.0, fill=color, stroke=t.bg, stroke_width=1.0)
                )

                # Label commit message above/below the node to prevent overlap
                if op["label"]:
                    count = b_cfg.setdefault("commit_count", 0)
                    y_off = 9.0 if count % 2 == 0 else -15.0
                    self._add(
                        S.label(
                            bx,
                            by + y_off,
                            op["label"],
                            font=t.font_name,
                            size=7.5,
                            color=t.node_text,
                            anchor="middle",
                        )
                    )
                    b_cfg["commit_count"] = count + 1

                last_commit_pos[branch] = (bx, by)
                b_cfg["last_x"] = bx

            elif op["type"] == "branch":
                parent = op["parent"]
                child = op["child"]

                p_cfg = self._branches[parent]
                c_cfg = self._branches[child]
                color = self._branch_colors[c_cfg["color_idx"]]

                px, py = last_commit_pos.get(parent, (30.0, p_cfg["y"]))
                cx, cy = self._current_x, c_cfg["y"]

                # Draw a curved connection from parent to child
                # For simplicity, a diagonal segment or bezier curved line works beautifully
                from reportlab.graphics.shapes import Path

                path = Path()
                path.moveTo(px, py)
                # Bezier curves to branch smoothly
                path.curveTo(px + 15.0, py, cx - 15.0, cy, cx, cy)
                path.fillColor = None
                path.strokeColor = S._hex(color)
                path.strokeWidth = 2.0
                self._add(path)

                # Create initial commit on the child branch immediately
                self._add(
                    S.circle(cx, cy, 5.0, fill=color, stroke=t.bg, stroke_width=1.0)
                )
                last_commit_pos[child] = (cx, cy)
                c_cfg["last_x"] = cx

            elif op["type"] == "merge":
                from_b = op["from"]
                to_b = op["to"]

                f_cfg = self._branches[from_b]
                t_cfg = self._branches[to_b]
                color_to = self._branch_colors[t_cfg["color_idx"]]
                color_from = self._branch_colors[f_cfg["color_idx"]]

                fx, fy = last_commit_pos[from_b]
                tx, ty = self._current_x, t_cfg["y"]

                # 1. Draw connection line from last commit of target branch
                if to_b in last_commit_pos:
                    lx, ly = last_commit_pos[to_b]
                    self._add(S.solid_line(lx, ly, tx, ty, color=color_to, width=2.0))

                # 2. Draw curved connection from from_branch to merge commit
                from reportlab.graphics.shapes import Path

                path = Path()
                path.moveTo(fx, fy)
                path.curveTo(fx + 15.0, fy, tx - 15.0, ty, tx, ty)
                path.fillColor = None
                path.strokeColor = S._hex(color_from)
                path.strokeWidth = 2.0
                self._add(path)

                # Draw merge commit node
                self._add(
                    S.circle(tx, ty, 5.0, fill=color_to, stroke=t.bg, stroke_width=1.0)
                )

                # Label merge message above/below the node to prevent overlap
                if op["label"]:
                    count = t_cfg.setdefault("commit_count", 0)
                    y_off = 9.0 if count % 2 == 0 else -15.0
                    self._add(
                        S.label(
                            tx,
                            ty + y_off,
                            op["label"],
                            font=t.font_name,
                            size=7.5,
                            color=t.node_text,
                            anchor="middle",
                        )
                    )
                    t_cfg["commit_count"] = count + 1

                last_commit_pos[to_b] = (tx, ty)
                t_cfg["last_x"] = tx

        # Draw termination lines for each branch to the edge of diagram
        # We need at least 40px after the last commit to draw the timeline tail,
        # and we expand self.width dynamically to fit the branch name label.
        end_x = max(self.width - 20.0, self._current_x + 40.0)
        self.width = max(self.width, end_x + 35.0)
        if hasattr(self, "drawing") and self.drawing:
            self.drawing.width = self.width

        for b_name, b_cfg in self._branches.items():
            if b_name in last_commit_pos:
                lx, ly = last_commit_pos[b_name]
                color = self._branch_colors[b_cfg["color_idx"]]
                # Draw main timeline indicator line
                self._add(S.solid_line(lx, ly, end_x, ly, color=color, width=2.0))
                # Add label of branch name at the end
                self._add(
                    S.label(
                        end_x + 5.0,
                        ly - 2.5,
                        b_name,
                        font=t.font_name_bold,
                        size=8.0,
                        color=color,
                        anchor="start",
                    )
                )
