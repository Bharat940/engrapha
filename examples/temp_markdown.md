---
title: Included Markdown Chapter
author: Modular Demo
theme: ocean-dark
style: index
---

## Markdown Section

### Included Markdown Content
This chapter was compiled from `temp_markdown.md` using `en.include_markdown()`.

> [!NOTE]
> Markdown files support alert boxes, code blocks, and diagram blocks.

> [!TIP]
> Keep theme and theme overrides consistent across chapters for best results.

### Code Sample
```python
from engrapha_notes import build_doc
build_doc("output.pdf")
```

### Key Points
- Uses OCEAN_DARK preset.
- Supports standard markdown syntax and alerts.
- Merge multiple `.md` files into one document.
