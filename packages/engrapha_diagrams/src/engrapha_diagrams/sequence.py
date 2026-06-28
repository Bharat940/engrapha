"""
sequence.py -- Sequence diagram builder.

Actors (participants) are placed evenly across the top.
Each actor has a vertical dashed lifeline extending downward.
Messages are horizontal arrows at auto-computed y positions.
Activation bars (narrow rectangles) can be placed on lifelines.
Notes, dividers, and self-messages are supported.
"""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel

from . import shapes as S
from .base import DiagramBase
from .layout import sequence_x_positions
from .theme import DiagramTheme

MessageArrow = Literal["solid", "dashed", "solid_open", "dashed_open"]

_ACTOR_W = 70.0
_ACTOR_H = 24.0
_ACTOR_MARGIN_TOP = 20.0
_ROW_HEIGHT = 32.0
_ACTIVATION_W = 10.0
_NOTE_W = 70.0
_NOTE_H = 22.0
_BOTTOM_PAD = 12.0
_LABEL_FONT_SIZE = 7.5
_LABEL_LINE_H = 9.5
_LABEL_PAD_X = 8.0  # padding inside each side of the arrow span


class _SeqActor(BaseModel):
    id: str
    label: str


class _SeqMessage(BaseModel):
    from_id: str
    to_id: str
    label: str
    arrow: MessageArrow = "solid"
    row: int = 0  # populated by builder
    extra_rows: int = 0  # extra row-slots consumed by a wrapped label


class _SeqActivation(BaseModel):
    actor_id: str
    start_row: int
    end_row: int


class _SeqNote(BaseModel):
    actor_id: str
    text: str
    side: Literal["left", "right"]
    row: int


class _SeqDivider(BaseModel):
    text: str
    row: int


class SequenceDiagram(DiagramBase):
    """
    Sequence diagram builder.

    Usage::

        seq = SequenceDiagram(width=400, height=200, caption="TCP 3-Way Handshake")
        seq.actor("client", "Client")
        seq.actor("server", "Server")
        seq.message("client", "server", "SYN", arrow="solid")
        seq.message("server", "client", "SYN-ACK", arrow="solid")
        seq.message("client", "server", "ACK", arrow="solid")
        story.extend(seq.as_flowable())
    """

    def __init__(
        self,
        width: float,
        height: float,
        theme: DiagramTheme | None = None,
        caption: str | None = None,
        row_height: float = _ROW_HEIGHT,
        actor_margin_top: float = _ACTOR_MARGIN_TOP,
        margin: float = 120.0,
    ) -> None:
        super().__init__(width, height, theme, caption)
        self.row_height = row_height
        self.actor_margin_top = actor_margin_top
        self.margin = margin
        self.actor_h = _ACTOR_H
        self._actors: list[_SeqActor] = []
        self._actor_index: dict[str, _SeqActor] = {}
        self._events: list[_SeqMessage | _SeqDivider] = []
        self._activations: list[_SeqActivation] = []
        self._current_row = 1
        self._open_activations: dict[str, int] = {}
        self._row_extra: dict[int, int] = {}  # row -> extra row-slots

    def actor(self, id: str, label: str) -> "SequenceDiagram":
        """Add a participant (actor / lifeline)."""
        if id in self._actor_index:
            raise ValueError(f"Duplicate actor id: '{id}'")
        a = _SeqActor(id=id, label=label)
        self._actors.append(a)
        self._actor_index[id] = a
        return self

    def _actor_span_width(self, from_id: str, to_id: str) -> float:
        """Return the horizontal span (pixels) between two actors."""
        if from_id == to_id or len(self._actors) < 2:
            return 150.0
        xs = sequence_x_positions(len(self._actors), self.width, margin=self.margin)
        fix = next(i for i, a in enumerate(self._actors) if a.id == from_id)
        tix = next(i for i, a in enumerate(self._actors) if a.id == to_id)
        return abs(xs[fix] - xs[tix])

    def _label_extra_rows(self, label: str, span_w: float) -> int:
        """Return extra row-slots consumed by a wrapped label (0 for single-line)."""
        max_w = max(span_w - _LABEL_PAD_X * 2, 20.0)
        lines = S.wrap_text(label, max_w, font="Helvetica", size=_LABEL_FONT_SIZE)
        return max(0, len(lines) - 1)

    def message(
        self,
        from_id: str,
        to_id: str,
        label: str,
        arrow: MessageArrow = "solid",
    ) -> "SequenceDiagram":
        """
        Add a message arrow between two actors.
        Use from_id == to_id for a self-message (drawn as a small loop).
        """
        for aid in (from_id, to_id):
            if aid not in self._actor_index:
                raise ValueError(
                    f"Actor id '{aid}' not found. Add actor before messaging."
                )
        # Estimate label wrap before we know exact xs; use width as upper bound
        span_w = self._actor_span_width(from_id, to_id)
        extra = self._label_extra_rows(label, span_w)
        row = self._current_row
        msg = _SeqMessage(
            from_id=from_id,
            to_id=to_id,
            label=label,
            arrow=arrow,
            row=row,
            extra_rows=extra,
        )
        self._events.append(msg)
        self._current_row += 1 + extra
        return self

    def activate(self, actor_id: str) -> "SequenceDiagram":
        """Begin an activation bar on the actor's lifeline."""
        if actor_id not in self._actor_index:
            raise ValueError(f"Actor id '{actor_id}' not found.")
        self._open_activations[actor_id] = self._current_row
        return self

    def deactivate(self, actor_id: str) -> "SequenceDiagram":
        """End the most recent activation bar on the actor's lifeline."""
        if actor_id not in self._open_activations:
            raise ValueError(f"No open activation for actor '{actor_id}'.")
        start = self._open_activations.pop(actor_id)
        self._activations.append(
            _SeqActivation(
                actor_id=actor_id, start_row=start, end_row=self._current_row
            )
        )
        return self

    def divider(self, text: str = "") -> "SequenceDiagram":
        """Add a horizontal divider line with optional label."""
        self._events.append(_SeqDivider(text=text, row=self._current_row))
        self._current_row += 1
        return self

    # -- Internal geometry --

    def _actor_x(self, actor_id: str) -> float:
        idx = next(i for i, a in enumerate(self._actors) if a.id == actor_id)
        xs = sequence_x_positions(len(self._actors), self.width, margin=self.margin)
        return xs[idx]

    def _row_y(self, row: int) -> float:
        """Y coordinate for a given row (counting from top, row 1 = first message)."""
        top = self.height - self.actor_margin_top - self.actor_h
        return top - row * self.row_height

    def _msg_label_y(self, msg: _SeqMessage) -> float:
        """Y centre of the label block for a message (may span multiple row-heights)."""
        top_y = self._row_y(msg.row)
        if msg.extra_rows == 0:
            return top_y
        # Centre of the wrapped label block
        bot_y = self._row_y(msg.row + msg.extra_rows)
        return (top_y + bot_y) / 2

    def _lifeline_top(self) -> float:
        return self.height - self.actor_margin_top - self.actor_h

    def _lifeline_bottom(self) -> float:
        return self._row_y(self._current_row + 1)

    def _ensure_event_height(self) -> None:
        """Grow the canvas so every event row remains within the reserved flowable area."""
        required_height = (
            self.actor_margin_top
            + self.actor_h
            + (self._current_row + 1) * self.row_height
            + _BOTTOM_PAD
        )
        if required_height > self.height:
            self.height = required_height
            self.drawing.height = required_height

    def _is_active(self, actor_id: str, row: int) -> bool:
        for act in self._activations:
            if act.actor_id == actor_id and act.start_row <= row <= act.end_row:
                return True
        if actor_id in self._open_activations:
            start = self._open_activations[actor_id]
            if start <= row:
                return True
        return False

    def build(self) -> None:
        t = self.theme
        # Calculate dynamic actor box height based on maximum lines of wrapped labels
        font_size = 8.5
        line_height = 10.5
        max_lines = 1
        for actor in self._actors:
            w_lines = S.wrap_text(
                actor.label, _ACTOR_W - 8.0, font=t.font_name_bold, size=font_size
            )
            max_lines = max(max_lines, len(w_lines))
        self.actor_h = max_lines * line_height + 8.0

        # Dynamically shrink margin or expand width to prevent actor boxes (70px wide) from overlapping
        min_spacing = _ACTOR_W + 15.0  # 85.0 points minimum center-to-center
        if len(self._actors) > 1:
            default_usable = self.width - 2 * self.margin
            if default_usable / (len(self._actors) - 1) < min_spacing:
                # Shrink margins to make more space
                self.margin = max(
                    40.0, (self.width - (len(self._actors) - 1) * min_spacing) / 2
                )

            # If even with 40.0 margins it doesn't fit, expand self.width
            needed_width = len(self._actors) * min_spacing + 2.0 * self.margin
            if needed_width > self.width:
                self.width = needed_width
                if hasattr(self, "drawing") and self.drawing:
                    self.drawing.width = needed_width

        self._ensure_event_height()
        xs = sequence_x_positions(len(self._actors), self.width, margin=self.margin)
        ll_top = self._lifeline_top()
        ll_bottom = max(self._lifeline_bottom(), 10.0)

        # 1. Lifelines (dashed vertical)
        for ax in xs:
            self._add(
                S.dashed_line(
                    ax, ll_bottom, ax, ll_top, color=t.lifeline_color, width=1.1
                )
            )

        # 2. Activation bars
        for act in self._activations:
            idx = next(i for i, a in enumerate(self._actors) if a.id == act.actor_id)
            ax = xs[idx]
            y_top = self._row_y(act.start_row)
            y_bot = self._row_y(act.end_row)
            aw = _ACTIVATION_W
            self._add(
                S.plain_rect(
                    ax - aw / 2,
                    y_bot,
                    aw,
                    y_top - y_bot,
                    fill=t.activation_fill,
                    stroke=t.activation_stroke,
                    stroke_width=0.9,
                )
            )

        # 3. Messages
        for event in self._events:
            if isinstance(event, _SeqDivider):
                ry = self._row_y(event.row)
                self._add(
                    S.dashed_line(
                        10, ry, self.width - 10, ry, color=t.lifeline_color, width=1.0
                    )
                )
                if event.text:
                    max_div_w = self.width - 24.0
                    self._add(
                        S.centered_wrapped_label(
                            self.width / 2,
                            ry + 5,
                            event.text,
                            max_width=max_div_w,
                            font=t.font_name_italic,
                            size=8.0,
                            color=t.actor_text,
                            anchor="middle",
                        )
                    )
                continue

            msg = event
            fix = next(i for i, a in enumerate(self._actors) if a.id == msg.from_id)
            tix = next(i for i, a in enumerate(self._actors) if a.id == msg.to_id)
            fx = xs[fix]
            tx = xs[tix]
            ry = self._row_y(msg.row)

            dashed = msg.arrow in ("dashed", "dashed_open")
            filled = msg.arrow in ("solid", "dashed")

            if msg.from_id == msg.to_id:
                # Self-message: small right-angled loop
                is_act = self._is_active(msg.from_id, msg.row)
                offset_x = _ACTIVATION_W / 2 if is_act else 0.0
                start_x = fx + offset_x
                loop_w = 24.0
                loop_h = 14.0
                self._add(
                    S.solid_line(
                        start_x, ry, start_x + loop_w, ry, color=t.message_color
                    )
                )
                self._add(
                    S.solid_line(
                        start_x + loop_w,
                        ry,
                        start_x + loop_w,
                        ry - loop_h,
                        color=t.message_color,
                    )
                )
                self._add(
                    S.arrow_line(
                        start_x + loop_w,
                        ry - loop_h,
                        start_x,
                        ry - loop_h,
                        color=t.message_color,
                        arrow_size=6.0,
                        filled_head=filled,
                    )
                )
                # Self-message label: wrap to remaining width
                avail_w = self.width - (start_x + loop_w + 6.0) - 4.0
                avail_w = max(avail_w, 30.0)
                self._add(
                    S.centered_wrapped_label(
                        start_x + loop_w + 6,
                        ry - loop_h / 2,
                        msg.label,
                        max_width=avail_w,
                        font=t.font_name,
                        size=_LABEL_FONT_SIZE,
                        color=t.message_text,
                        anchor="start",
                    )
                )
            else:
                fx_shift = (
                    _ACTIVATION_W / 2 if self._is_active(msg.from_id, msg.row) else 0.0
                )
                tx_shift = (
                    _ACTIVATION_W / 2 if self._is_active(msg.to_id, msg.row) else 0.0
                )

                if fx < tx:
                    x1 = fx + fx_shift
                    x2 = tx - tx_shift
                else:
                    x1 = fx - fx_shift
                    x2 = tx + tx_shift

                self._add(
                    S.arrow_line(
                        x1,
                        ry,
                        x2,
                        ry,
                        color=t.message_color,
                        width=1.2,
                        arrow_end=True,
                        dashed=dashed,
                        filled_head=filled,
                        arrow_size=7.0,
                    )
                )
                mx = (x1 + x2) / 2
                span_w = abs(x2 - x1)
                max_label_w = max(span_w - _LABEL_PAD_X * 2, 20.0)
                label_y = self._msg_label_y(msg)
                # Position label slightly above the arrow line
                label_cy = label_y + _LABEL_FONT_SIZE * 0.6
                self._add(
                    S.centered_wrapped_label(
                        mx,
                        label_cy,
                        msg.label,
                        max_width=max_label_w,
                        font=t.font_name,
                        size=_LABEL_FONT_SIZE,
                        color=t.message_text,
                        anchor="middle",
                    )
                )

        # 4. Actor boxes (drawn last, on top of lifelines)
        for i, actor in enumerate(self._actors):
            ax = xs[i]
            ex = ax - _ACTOR_W / 2
            ey = self.height - self.actor_margin_top - self.actor_h
            self._add(
                S.rounded_rect(
                    ex,
                    ey,
                    _ACTOR_W,
                    self.actor_h,
                    rx=4,
                    fill=t.actor_fill,
                    stroke=t.actor_stroke,
                )
            )
            self._add(
                S.centered_wrapped_label(
                    ax,
                    ey + self.actor_h / 2,
                    actor.label,
                    max_width=_ACTOR_W - 8.0,
                    font=t.font_name_bold,
                    size=8.5,
                    color=t.actor_text,
                    anchor="middle",
                )
            )
