# Example: Engineering Notes

A complete engineering-notes session using Engrapha.

```python title="engineering_notes.py"
import engrapha_notes as en
import engrapha_diagrams as ed

# Theme and global footer
en.set_theme(en.OCEAN_DARK)
en.set_global_header(
    left="Advanced Algorithms",
    center="Unit IV",
    right="Session 2026",
)
en.set_global_footer(
    left="Bharat Dangi",
    right="0171IT241013",
    show_page_num=True,
)

# Cover
en.bookmark("Cover Page")
en.suppress_header(page_only=True)
en.suppress_footer(page_only=True)
en.sp(40)
en.cover_card(
    "Advanced Algorithms",
    "Unit IV: Graph Algorithms",
)
en.br()

# TOC with fancy style
en.suppress_footer(page_only=True)
en.toc(style="index")
en.footer(left="Advanced Algorithms", right="Unit IV", show_page_num=True)

# Part
en.part_box("Unit IV: Graph Algorithms")
en.chap_box("4.1 Shortest Path")

en.section("Dijkstra's Algorithm")
en.body(
    "Dijkstra's algorithm finds shortest paths from a single source to "
    "all other vertices. It only works on non-negative weight graphs."
)
en.tip("It is the backbone of GPS navigation systems.")

# Code block
en.code_block("""
 def dijkstra(graph, source):
     dist = {v: float('inf') for v in graph}
     dist[source] = 0
     pq = [(0, source)]
     while pq:
         d, u = heapq.heappop(pq)
         if d > dist[u]:
             continue
         for v, w in graph[u].items():
             nd = d + w
             if nd < dist[v]:
                 dist[v] = nd
                 heapq.heappush(pq, (nd, v))
     return dist
""", lang="python")

# Embed flowchart
fc = ed.Flowchart(
    width=en.CW, height=140, caption="Fig 4.1: Dijkstra main loop"
)
fc.terminal("s", "START")
fc.process("init",  "Initialize distances")
fc.process("pq",    "Priority Queue")
fc.decision("d",    "Queue empty?")
fc.process("pop",   "Pop min-dist node")
fc.process("relax", "Relax neighbors")
fc.terminal("e",    "END")
fc.edge("s", "init").edge("init", "pq").edge("pq", "d")
fc.edge("d", "e", branch="yes")
fc.edge("d", "pop", branch="no")
fc.edge("pop", "relax").edge("relax", "pq")
en.add(fc.as_flowable())

# Flashcards
en.flashcard(
    "Time complexity of Dijkstra (heap)",
    "O((V + E) log V) using a binary heap"
)
en.flashcard(
    "What prevents negative-weight cycles?",
    "Dijkstra assumes all weights ≥ 0"
)

# Build
en.build_doc("engineering_notes.pdf")
```

## Result

- Cover card + TOC (auto-generated)
- Themed sections, body, tip callout
- Syntax-highlighted Python code block
- Vector flowchart aligned to document width
- Two flashcards auto-exported to CSV / JSON / APKG

![Screenshot placeholder](../assets/screenshots/notes_engineering.png)

