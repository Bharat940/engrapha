# Example: Thesis Chapter

Academic chapter with sections, citations, formulas, index entries, and an embedded diagram.

```python title="thesis_chapter.py"
import paperforge_notes as pn
import paperforge_diagrams as pd

pn.set_theme(pn.DARK)
pn.set_global_header(left="Thesis", center="Chapter 3", right="Draft 0.1")

pn.chap_box("3. Distributed Consensus via Raft")

pn.body(
    "Raft achieves consensus by electing a single leader that manages "
    "replicated log entries. Safety is guaranteed by the restriction that "
    "only the current leader can commit entries."
)

pn.index_entry("Raft")
pn.index_entry("Consensus")

pn.section("Leader Election")

pn.body(
    "Quotes from Ongaro and Ousterhout [1] describe randomised election "
    "timeouts as the mechanism for split-vote resolution."
)

# Inline formula + advanced paragraph
pn.body(
    "The election timeout range is typically chosen from \\\\(T \\in [150, 300] ms\\\\) "
    "to reduce collision probability."
)

pn.section("Log Replication")

# Diagram
seq = pd.SequenceDiagram(
    width=340, height=200,
    caption="Fig 3.1: Client request → majority commit",
)
seq.actor("client", "Client")
seq.actor("ldr",    "Leader")
seq.actor("f1",     "Follower 1")
seq.actor("f2",     "Follower 2")

seq.message("client", "ldr", "PUT x=1")
seq.activate("ldr")
seq.message("ldr", "f1", "Append RPC")
seq.message("ldr", "f2", "Append RPC")
seq.message("f2", "ldr", "ACK", arrow="dashed")
seq.message("f1", "ldr", "ACK", arrow="dashed")
seq.message("ldr", "client", "COMMIT", arrow="dashed")
seq.deactivate("ldr")

pn.add(seq.as_flowable())

# References section
pn.section("References")
pn.body("[1] Diego Ongaro and John Ousterhout. *In Search of an Understandable Consensus Algorithm.* USENIX ATC 2014.")

pn.build_doc("thesis_chapter.pdf")
```

![Screenshot placeholder](../assets/screenshots/notes_thesis.png)
