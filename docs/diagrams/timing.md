# Diagram: Timing

Timing diagrams render digital waveforms side-by-side, perfect for busses, SPI, I2C, and memory timing.

## Minimal example

```python
import paperforge_notes as pn
import paperforge_diagrams as pd

td = pd.TimingDiagram(
    width=400, height=150, caption="Fig 13: SPI Timing"
)

# 50% duty-cycle clock
td.clock("CLK", period=20.0, cycles=6)

# Custom signal: (time, level)
td.signal(
    "MISO",
    transitions=[(0, 0), (10, 1), (30, 0), (50, 1), (70, 0)]
)

pn.add(td.as_flowable())
```

## Clock parameters

```python
td.clock(
    name="SCLK",
    period=20.0,   # nanoseconds
    duty=0.5,      # high-fraction of period
    cycles=8,
)
```

## Signal transitions

```python
td.signal(
    "CS",
    transitions=[
        (0, 1),   # start high
        (5, 0),   # pull low (select)
        (85, 1),  # return high (deselect)
    ],
)
```

Transition time values should be non-decreasing. Levels must be `0` or `1`.

## Grid

Grid is enabled by default. Disable it:

```python
td = pd.TimingDiagram(width=400, height=150, grid=False)
```

## Height

The canvas grows automatically as signals are stacked. Each signal occupies ~36 points with an 8-point gap.

## Colors

The active theme maps:

- `signal_high_color` — high waveform color
- `signal_low_color` — low waveform color
- `time_tick_color` — grid/tick colour
- `time_axis_color` — axis and ruler colour
- `signal_label_color` — label text

## Next

- [Git](git.md)
- [Gallery](../gallery/index.md)
