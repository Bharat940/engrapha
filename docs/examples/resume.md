# Example: Resume

A single-page resume using Engrapha's section blocks, bullet lists, and timeline blocks.

```python title="resume.py"
import engrapha_notes as en
import engrapha_diagrams as ed

en.set_theme(en.LIGHT)
en.set_global_footer(left="Bharat Dangi", show_page_num=True)

en.cover_card("Software Engineer", "Bharat Dangi  ·  bharat@example.com")

en.chap_box("Summary")
en.body(
    "Senior backend engineer specialising in distributed systems, "
    "Python microservices, and observability. 6+ years building production "
    "systems at scale."
)

en.chap_box("Skills")
skills = ["Python", "Go", "Kubernetes", "gRPC", "PostgreSQL", "Terraform"]
en.bullet([f"<b>{s}</b>" for s in skills])

en.chap_box("Experience")

en.subsection("TechCorp — Senior Engineer (2021 → Present)")
en.bullet([
    "Led migration of 12 services to gRPC",
    "Reduced p99 latency from 800 ms to 220 ms",
    "Owner of observability stack: Prometheus, OTel, Grafana",
])

en.subsection("StartupXYZ — Engineer (2019 → 2021)")
en.bullet([
    "Built first production ML pipeline (Python, scikit-learn)",
    "Wired monorepo migration from Jinja + Make to Poe",
])

en.build_doc("resume.pdf")
```

![Screenshot placeholder](../assets/screenshots/notes_resume.png)

