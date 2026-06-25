# Example: Resume

A single-page resume using PaperForge's section blocks, bullet lists, and timeline blocks.

```python title="resume.py"
import paperforge_notes as pn
import paperforge_diagrams as pd

pn.set_theme(pn.LIGHT)
pn.set_global_footer(left="Bharat Dangi", show_page_num=True)

pn.cover_card("Software Engineer", "Bharat Dangi  ·  bharat@example.com")

pn.chap_box("Summary")
pn.body(
    "Senior backend engineer specialising in distributed systems, "
    "Python microservices, and observability. 6+ years building production "
    "systems at scale."
)

pn.chap_box("Skills")
skills = ["Python", "Go", "Kubernetes", "gRPC", "PostgreSQL", "Terraform"]
pn.bullet([f"<b>{s}</b>" for s in skills])

pn.chap_box("Experience")

pn.subsection("TechCorp — Senior Engineer (2021 → Present)")
pn.bullet([
    "Led migration of 12 services to gRPC",
    "Reduced p99 latency from 800 ms to 220 ms",
    "Owner of observability stack: Prometheus, OTel, Grafana",
])

pn.subsection("StartupXYZ — Engineer (2019 → 2021)")
pn.bullet([
    "Built first production ML pipeline (Python, scikit-learn)",
    "Wired monorepo migration from Jinja + Make to Poe",
])

pn.build_doc("resume.pdf")
```

![Screenshot placeholder](../assets/screenshots/notes_resume.png)
