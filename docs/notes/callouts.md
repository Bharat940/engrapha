# Notes: Callouts and Highlights

PaperForge ships with semantic callout blocks for all the most common exam-note situations.

## Available callouts

| Helper | Color | Will render |
| ------ | ----- | ----------- |
| `tip(text)` | green border + bg | EXAM TIP box |
| `note(text)` | yellow border + bg | NOTE box |
| `warning(text)` | red border + bg | WARNING box |
| `important(text)` | purple/indigo border + bg | IMPORTANT box |
| `highlight(text)` | yellow border | exam/highlight box |
| `exam(text)` | yellow border | EXAM box |
| `definition(text)` | light surface + accent border | definition box |
| `theorem(text)` | purple border + bg | THEOREM box |
| `proof(text)` | indented italic text | Proof ending in `[Q.E.D.]` |

## Quick usage

```python
pn.tip("Average case is O(N log N). Use Random Pivots.")
pn.note("Pivot selection is the only difference vs Quick Sort.")
pn.warning("Do not apply on reverse-sorted arrays.")
pn.important("Master the recurrence relation.")
pn.exam("A frequent exam question.")
pn.theorem("If p is prime and a | b, then p^(a-1) divides b^(p-1) - 1 modulo p.")
pn.proof(
    "By Fermat's Little Theorem and induction on prime factors."
)
pn.highlight("Time complexity O(N log N) is best-case and average-case.")
pn.definition("A sorting algorithm is 'in-place' if O(1) extra memory.")
```

## Visual contract

Each callout has:

- A 1.2pt accent-colored border
- A muted version of the accent as background fill
- 8-12 point internal padding
- No text antialiasing violations: text remains black-on-color

## Integration with the Plain-Questions theme

In `plain_questions=True` themes (such as the Print Light preset), the callouts are rendered as plain body text with a prefix:

```python
pn.tip("Pivot selection matters")  # → "Exam Tip: Pivot selection matters"
pn.note("Use random pivots")       # → "Note: Use random pivots"
```

This avoids boxed layouts for exam/print output.

## Layout rules

- **Callouts** always include the bold prefix (e.g., `EXAM TIP:`).
- **theorem** boxes cannot contain callouts but can contain `formula_block()`.
- **proof** blocks always end in `[Q.E.D.]`.
- **definition** callouts are surface-only (no colour shift), suitable for dense text.

## Next

- [Study helpers](study.md)
- [Advanced topics](advanced.md)
