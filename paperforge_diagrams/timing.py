"""
timing.py -- Timing diagram builder.

Renders digital-style waveforms for signal timing and clock diagrams.
Each signal is a horizontal waveform. Signals are stacked top-to-bottom.
A time axis runs along the bottom.

Supports:
  - Arbitrary signal transitions as (time, level) pairs (level: 0 or 1)
  - clock() convenience method for regular clock signals
  - Auto-scaled time axis with tick marks and labels
"""

from __future__ import annotations

from pydantic import BaseModel, model_validator

from . import shapes as S
from .base import DiagramBase
from .theme import DiagramTheme

_LABEL_W = 120.0  # left margin for signal names
_SIGNAL_H = 28.0  # height of each signal track
_SIGNAL_VGAP = 8.0  # vertical gap between signal tracks
_AXIS_H = 22.0  # height of the time axis area
_TOP_PAD = 10.0
_WAVEFORM_PAD = 4.0  # vertical padding inside signal track


class _Signal(BaseModel):
    name: str
    transitions: list[tuple[float, int]]

    @model_validator(mode="after")
    def validate_transitions(self) -> "_Signal":
        if not self.transitions:
            raise ValueError(
                f"Signal '{self.name}' must have at least one transition point"
            )
        for t, level in self.transitions:
            if level not in (0, 1):
                raise ValueError(
                    f"Signal '{self.name}': level must be 0 or 1, got {level} at time {t}"
                )
        return self


class TimingDiagram(DiagramBase):
    """
    Timing (waveform) diagram builder.

    Usage::

        td = TimingDiagram(width=400, height=150, caption="Clock and Data Signals")
        td.clock("CLK", period=20.0, cycles=8)
        td.signal("DATA", transitions=[
            (0, 0), (20, 1), (60, 0), (100, 1), (140, 0), (160, 0)
        ])
        story.extend(td.as_flowable())
    """

    def __init__(
        self,
        width: float,
        height: float,
        theme: DiagramTheme | None = None,
        caption: str | None = None,
        grid: bool = True,
    ) -> None:
        super().__init__(width, height, theme, caption)
        self.grid = grid
        self._signals: list[_Signal] = []

    def signal(
        self,
        name: str,
        transitions: list[tuple[float, int]],
    ) -> "TimingDiagram":
        """
        Add a signal with explicit (time, level) transitions.
        Time values should be non-decreasing. Level is 0 (low) or 1 (high).
        """
        self._signals.append(_Signal(name=name, transitions=transitions))
        return self

    def clock(
        self,
        name: str,
        period: float,
        duty: float = 0.5,
        cycles: int = 8,
    ) -> "TimingDiagram":
        """
        Add a clock signal with regular transitions.
        duty: fraction of period in the high state (default 0.5 = 50%).
        """
        if not (0.0 < duty < 1.0):
            raise ValueError(f"duty must be between 0 and 1, got {duty}")
        if cycles < 1:
            raise ValueError(f"cycles must be >= 1, got {cycles}")
        high_t = period * duty
        transitions: list[tuple[float, int]] = [(0.0, 0)]
        t = 0.0
        for _ in range(cycles):
            transitions.append((t, 0))
            transitions.append((t, 1))
            t += high_t
            transitions.append((t, 1))
            transitions.append((t, 0))
            t += period - high_t
        transitions.append((t, 0))
        self._signals.append(_Signal(name=name, transitions=transitions))
        return self

    # -- Build --

    def build(self) -> None:
        if not self._signals:
            return

        t = self.theme
        draw_w = self.width - _LABEL_W - 10  # usable waveform area width

        # Find time range across all signals
        all_times = [pt for sig in self._signals for pt, _ in sig.transitions]
        t_min = min(all_times)
        t_max = max(all_times)
        t_range = max(t_max - t_min, 1.0)

        def time_to_x(tm: float) -> float:
            return _LABEL_W + (tm - t_min) / t_range * draw_w

        # Stack signals top-to-bottom
        y_start: float = self.height - _TOP_PAD - _SIGNAL_H

        for sig_idx, sig in enumerate(self._signals):
            base_y = y_start - sig_idx * (_SIGNAL_H + _SIGNAL_VGAP)
            high_y = base_y + _SIGNAL_H - _WAVEFORM_PAD
            low_y = base_y + _WAVEFORM_PAD

            # Signal name label
            self._add(
                S.label(
                    _LABEL_W - 6,
                    base_y + _SIGNAL_H / 2 - 4,
                    sig.name,
                    font=t.font_name_bold,
                    size=8.0,
                    color=t.signal_label_color,
                    anchor="end",
                )
            )

            # Draw waveform
            pts = sig.transitions
            for i in range(len(pts)):
                cur_t, cur_level = pts[i]
                cur_x = time_to_x(cur_t)
                cur_y = high_y if cur_level == 1 else low_y

                if i == 0:
                    prev_x, prev_y = cur_x, cur_y
                    continue

                prev_t, prev_level = pts[i - 1]
                prev_x = time_to_x(prev_t)
                prev_y = high_y if prev_level == 1 else low_y

                # Horizontal segment at previous level
                seg_color = (
                    t.signal_high_color if prev_level == 1 else t.signal_low_color
                )
                self._add(
                    S.solid_line(
                        prev_x, prev_y, cur_x, prev_y, color=seg_color, width=1.5
                    )
                )

                # Vertical transition
                if prev_level != cur_level:
                    self._add(
                        S.solid_line(
                            cur_x, prev_y, cur_x, cur_y, color=seg_color, width=1.5
                        )
                    )

            # Final segment to end of drawing
            if pts:
                last_t, last_level = pts[-1]
                last_x = time_to_x(last_t)
                last_y = high_y if last_level == 1 else low_y
                end_x = time_to_x(t_max)
                seg_color = (
                    t.signal_high_color if last_level == 1 else t.signal_low_color
                )
                self._add(
                    S.solid_line(
                        last_x, last_y, end_x, last_y, color=seg_color, width=1.5
                    )
                )

            # Track background separator
            self._add(
                S.dashed_line(
                    _LABEL_W,
                    base_y - _SIGNAL_VGAP / 2,
                    self.width - 5,
                    base_y - _SIGNAL_VGAP / 2,
                    color=t.time_tick_color,
                    width=0.5,
                )
            )

        # Time axis
        axis_y = y_start - len(self._signals) * (_SIGNAL_H + _SIGNAL_VGAP)
        self._add(
            S.solid_line(
                _LABEL_W,
                axis_y,
                self.width - 5,
                axis_y,
                color=t.time_axis_color,
                width=1.0,
            )
        )

        # Tick marks -- aim for ~6 ticks
        tick_count = min(6, int(t_range) + 1)
        tick_step = t_range / max(tick_count - 1, 1)

        # Draw vertical grid lines if enabled
        if self.grid:
            for i in range(tick_count):
                tick_t = t_min + i * tick_step
                tx = time_to_x(tick_t)
                self._add(
                    S.dashed_line(
                        tx,
                        axis_y,
                        tx,
                        y_start + _SIGNAL_H - _WAVEFORM_PAD,
                        color=t.time_tick_color,
                        width=0.5,
                    )
                )

        for i in range(tick_count):
            tick_t = t_min + i * tick_step
            tx = time_to_x(tick_t)
            self._add(
                S.solid_line(
                    tx, axis_y - 3, tx, axis_y + 3, color=t.time_axis_color, width=0.8
                )
            )
            label_val = f"{int(tick_t)}" if tick_t == int(tick_t) else f"{tick_t:.1f}"
            self._add(
                S.label(
                    tx,
                    axis_y - 10,
                    label_val,
                    font=t.font_name,
                    size=7.0,
                    color=t.time_tick_color,
                    anchor="middle",
                )
            )

        # Time axis label
        self._add(
            S.label(
                self.width / 2,
                axis_y - 18,
                "Time",
                font=t.font_name_italic,
                size=7.5,
                color=t.signal_label_color,
                anchor="middle",
            )
        )
