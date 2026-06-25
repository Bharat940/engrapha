"""
cli.py -- Command Line Interface for compiling markdown notes to themed PDFs.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from typing import List, Dict, Optional

import paperforge_notes as pn
import paperforge_diagrams as pd
from reportlab.platypus import Paragraph, Spacer, Table, PageBreak, Flowable


class PDFCompilerError(Exception):
    """Base exception for PDF compiler errors."""

    pass


def parse_metadata(lines: List[str]) -> tuple[Dict[str, str], List[str]]:
    """
    Parse optional front-matter metadata from the top of the file.
    Example:
    ---
    title: Java Programming
    author: Bharat Dangi
    ---
    """
    metadata: Dict[str, str] = {}
    content_lines = lines

    if len(lines) > 0 and lines[0].strip() == "---":
        metadata_lines = []
        idx = 1
        while idx < len(lines) and lines[idx].strip() != "---":
            metadata_lines.append(lines[idx])
            idx += 1

        if idx < len(lines):
            content_lines = lines[idx + 1 :]
            for line in metadata_lines:
                if ":" in line:
                    k, v = line.split(":", 1)
                    metadata[k.strip().lower()] = v.strip()

    return metadata, content_lines


def format_inline_markdown(text: str) -> str:
    """
    Convert markdown inline elements (**bold**, *italic*, `code`)
    to ReportLab paragraph XML tags.
    """
    import xml.sax.saxutils as saxutils

    escaped = saxutils.escape(text)

    escaped = escaped.replace("&lt;b&gt;", "<b>").replace("&lt;/b&gt;", "</b>")
    escaped = escaped.replace("&lt;i&gt;", "<i>").replace("&lt;/i&gt;", "</i>")
    escaped = escaped.replace("&lt;u&gt;", "<u>").replace("&lt;/u&gt;", "</u>")

    escaped = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", escaped)
    escaped = re.sub(r"__(.*?)__", r"<b>\1</b>", escaped)

    escaped = re.sub(r"\*(.*?)\*", r"<i>\1</i>", escaped)
    escaped = re.sub(r"_(.*?)_", r"<i>\1</i>", escaped)

    escaped = re.sub(r"`(.*?)`", r'<font face="Courier" size="8.5">\1</font>', escaped)

    return escaped


def parse_diagram_dsl(block_type: str, content: List[str]) -> Optional[List[Flowable]]:
    """
    Parse a simple textual DSL inside diagram code blocks and return flowables.
    """

    def parse_kwargs(line: str) -> Dict[str, str]:
        pattern = r'(\w+)\s*=\s*(?:"([^"]*)"|\'([^\']*)\'|([^\s]+))'
        matches = re.findall(pattern, line)
        return {m[0].lower(): (m[1] or m[2] or m[3]) for m in matches}

    width = 450.0
    height = 240.0
    caption: Optional[str] = None
    direction = "TB"
    scale_factor: Optional[float] = None
    label: Optional[str] = None

    dsl_lines = []
    for line in content:
        line_strip = line.strip()
        if not line_strip or line_strip.startswith("#"):
            continue
        is_config = False
        if "=" in line_strip:
            parts_eq = line_strip.split("=", 1)
            if parts_eq[0].strip().lower() in (
                "width",
                "height",
                "caption",
                "direction",
                "scale_factor",
            ):
                is_config = True
        if is_config:
            k, v = line_strip.split("=", 1)
            k = k.strip().lower()
            v = v.strip().strip('"').strip("'")
            if k == "width":
                width = float(v)
            elif k == "height":
                height = float(v)
            elif k == "caption":
                caption = v
            elif k == "direction":
                direction = v
            elif k == "scale_factor":
                scale_factor = float(v)
        else:
            dsl_lines.append(line_strip)

    theme = pd.DiagramTheme.from_notes_theme(pn.get_theme())

    norm_block_type = block_type.lower()
    if norm_block_type == "er":
        norm_block_type = "schema"
    elif norm_block_type == "arch":
        norm_block_type = "architecture"
    elif norm_block_type == "c4container":
        norm_block_type = "c4"
    elif norm_block_type == "cloud":
        norm_block_type = "aws"

    try:
        if norm_block_type == "flowchart":
            fc = pd.Flowchart(
                width=width,
                height=height,
                theme=theme,
                caption=caption,
                direction=direction,
                scale_factor=scale_factor,
            )
            for line in dsl_lines:
                parts = line.split(maxsplit=2)
                if not parts:
                    continue
                cmd = parts[0].lower()

                if cmd in (
                    "terminal",
                    "process",
                    "decision",
                    "io",
                    "connector",
                    "predefined",
                ):
                    if len(parts) < 2:
                        continue
                    node_id = parts[1]
                    node_label: str = (
                        parts[2].strip('"').strip("'")
                        if len(parts) > 2
                        else node_id.upper()
                    )

                    if cmd == "terminal":
                        fc.terminal(node_id, node_label)
                    elif cmd == "process":
                        fc.process(node_id, node_label)
                    elif cmd == "decision":
                        fc.decision(node_id, node_label)
                    elif cmd == "io":
                        fc.io_box(node_id, node_label)
                    elif cmd == "connector":
                        fc.connector(node_id, node_label)
                    elif cmd == "predefined":
                        fc.predefined(node_id, node_label)

                elif cmd == "edge":
                    subparts = re.findall(r'(?:[^\s"\']|"[^"]*"|\'[^\']*\')+', line)
                    if len(subparts) < 3:
                        continue
                    src = subparts[1]
                    dst = subparts[2]

                    label_val = None
                    orthogonal_val = False

                    for param in subparts[3:]:
                        if "=" in param:
                            pk, pv = param.split("=", 1)
                            pk = pk.strip().lower()
                            pv = pv.strip().strip('"').strip("'")
                            if pk == "orthogonal":
                                orthogonal_val = pv.lower() == "true"
                            elif pk == "label":
                                label_val = pv
                        else:
                            label_val = param.strip('"').strip("'")

                    fc.edge(src, dst, label=label_val or "", orthogonal=orthogonal_val)

            return fc.as_flowable()

        elif norm_block_type == "sequence":
            seq = pd.SequenceDiagram(
                width=width, height=height, theme=theme, caption=caption
            )
            for line in dsl_lines:
                subparts = re.findall(r'(?:[^\s"\']|"[^"]*"|\'[^\']*\')+', line)
                if not subparts:
                    continue
                cmd = subparts[0].lower()

                if cmd in ("actor", "participant"):
                    if len(subparts) < 2:
                        continue
                    actor_id = subparts[1]
                    actor_label = (
                        subparts[2].strip('"').strip("'")
                        if len(subparts) > 2
                        else actor_id.upper()
                    )

                    # Both commands map to seq.actor()
                    seq.actor(actor_id, actor_label)

                elif cmd == "message":
                    if len(subparts) < 4:
                        continue
                    src = subparts[1]
                    dst = subparts[2]
                    msg_text = subparts[3].strip('"').strip("'")

                    seq.message(src, dst, msg_text)

                elif cmd == "divider":
                    text_val = (
                        subparts[1].strip('"').strip("'") if len(subparts) > 1 else ""
                    )
                    seq.divider(text=text_val)

            return seq.as_flowable()

        elif norm_block_type == "layeredstack":
            stack = pd.LayeredStack(
                width=width, height=height, theme=theme, caption=caption
            )
            for line in dsl_lines:
                subparts = re.findall(r'(?:[^\s"\']|"[^"]*"|\'[^\']*\')+', line)
                if not subparts:
                    continue
                cmd = subparts[0].lower()

                if cmd == "layer":
                    if len(subparts) < 2:
                        continue
                    layer_label = subparts[1].strip('"').strip("'")
                    sublabel = (
                        subparts[2].strip('"').strip("'") if len(subparts) > 2 else None
                    )

                    stack.layer(layer_label, sublabel=sublabel or "")

            return stack.as_flowable()

        elif norm_block_type == "schema":
            schema = pd.SchemaDiagram(
                width=width, height=height, theme=theme, caption=caption
            )
            current_table = None
            for line in dsl_lines:
                table_match = re.match(
                    r"^table\s+(\w+)(?:\s+x\s*=\s*([0-9\.]+))?(?:\s+y\s*=\s*([0-9\.]+))?:?",
                    line,
                    re.IGNORECASE,
                )
                if table_match:
                    current_table = table_match.group(1)
                    tx = float(table_match.group(2)) if table_match.group(2) else 0.0
                    ty = float(table_match.group(3)) if table_match.group(3) else 0.0
                    schema.table(current_table, [], x=tx, y=ty)
                    continue

                if line.lower().startswith("relation") or line.lower().startswith(
                    "relate"
                ):
                    rel_line = re.sub(
                        r"^(?:relation|relate)\s+", "", line, flags=re.IGNORECASE
                    )
                    subparts = re.split(r"\s*(?:->|to|\s)\s*", rel_line)
                    subparts = [p for p in subparts if p]
                    if len(subparts) >= 2:
                        p1 = subparts[0]
                        p2 = subparts[1]
                        if "." in p1 and "." in p2:
                            ft, fc = p1.split(".", 1)
                            tt, tc = p2.split(".", 1)
                            schema.relation(
                                ft.strip(), fc.strip(), tt.strip(), tc.strip()
                            )
                        elif len(subparts) >= 4:
                            schema.relation(
                                subparts[0], subparts[1], subparts[2], subparts[3]
                            )
                    continue

                if current_table and ":" in line:
                    parts_col = line.split(":", 1)
                    col_name = parts_col[0].strip()
                    rest = parts_col[1].strip()

                    relation_target = None
                    if "->" in rest:
                        rest, target = rest.split("->", 1)
                        relation_target = target.strip()

                    is_pk = "(pk)" in rest.lower()
                    is_fk = "(fk)" in rest.lower() or relation_target is not None

                    col_type = (
                        rest.replace("(pk)", "")
                        .replace("(PK)", "")
                        .replace("(fk)", "")
                        .replace("(FK)", "")
                        .strip()
                    )
                    if not col_type:
                        col_type = "VARCHAR"

                    schema._tables[current_table]["columns"].append(
                        (col_name, col_type, {"pk": is_pk, "fk": is_fk})
                    )

                    if relation_target:
                        if "." in relation_target:
                            target_table, target_col = relation_target.split(".", 1)
                            schema.relation(
                                current_table,
                                col_name,
                                target_table.strip(),
                                target_col.strip(),
                            )
                        else:
                            schema.relation(
                                current_table, col_name, relation_target, "id"
                            )

            return schema.as_flowable()

        elif norm_block_type == "git":
            git = pd.GitDiagram(
                width=width, height=height, theme=theme, caption=caption
            )
            known_branches = {"main"}
            for line in dsl_lines:
                kwargs = parse_kwargs(line)
                parts = re.findall(r'(?:[^\s"\']|"[^"]*"|\'[^\']*\')+', line)
                if not parts:
                    continue
                cmd = parts[0].lower()

                if cmd == "commit":
                    branch = kwargs.get("branch") or kwargs.get("branch_name")
                    label = (
                        kwargs.get("label")
                        or kwargs.get("msg")
                        or kwargs.get("message")
                    )
                    if not branch and not label:
                        if len(parts) > 1:
                            val = parts[1].strip("\"'")
                            if val in known_branches:
                                branch = val
                                if len(parts) > 2:
                                    label = parts[2].strip("\"'")
                            else:
                                branch = "main"
                                label = val
                    if not branch:
                        branch = "main"
                    git.commit(branch, label or "")

                elif cmd == "branch":
                    parent = kwargs.get("parent") or kwargs.get("from")
                    child = kwargs.get("child") or kwargs.get("to")
                    if not parent and not child:
                        if len(parts) > 2:
                            parent = parts[1].strip("\"'")
                            child = parts[2].strip("\"'")
                    if parent and child:
                        known_branches.add(child)
                        git.branch(parent, child)

                elif cmd == "merge":
                    from_b = kwargs.get("from") or kwargs.get("from_branch")
                    to_b = kwargs.get("to") or kwargs.get("to_branch")
                    label = kwargs.get("label") or kwargs.get("msg")
                    if not from_b and not to_b:
                        if len(parts) > 2:
                            from_b = parts[1].strip("\"'")
                            to_b = parts[2].strip("\"'")
                            if len(parts) > 3:
                                label = parts[3].strip("\"'")
                    if from_b and to_b:
                        git.merge(from_b, to_b, label or "")

            return git.as_flowable()

        elif norm_block_type == "architecture":
            arch = pd.ArchitectureDiagram(
                width=width, height=height, theme=theme, caption=caption
            )
            for line in dsl_lines:
                kwargs = parse_kwargs(line)
                parts = re.findall(r'(?:[^\s"\']|"[^"]*"|\'[^\']*\')+', line)
                if not parts:
                    continue
                cmd = parts[0].lower()

                if cmd in ("client", "service", "database", "queue"):
                    name = kwargs.get("name")
                    label = kwargs.get("label")
                    if not name and len(parts) > 1:
                        name = parts[1].strip("\"'")
                        if len(parts) > 2:
                            label = parts[2].strip("\"'")
                    if name:
                        if cmd == "client":
                            arch.client(name, label or "")
                        elif cmd == "service":
                            arch.service(name, label or "")
                        elif cmd == "database":
                            arch.database(name, label or "")
                        elif cmd == "queue":
                            arch.queue(name, label or "")
                elif cmd in ("connect", "link", "edge"):
                    from_node = kwargs.get("from") or kwargs.get("src")
                    to_node = kwargs.get("to") or kwargs.get("dst")
                    label = kwargs.get("label")
                    if not from_node and not to_node and len(parts) > 2:
                        from_node = parts[1].strip("\"'")
                        to_node = parts[2].strip("\"'")
                        if len(parts) > 3:
                            label = parts[3].strip("\"'")
                    if from_node and to_node:
                        arch.connect(from_node, to_node, label or "")

            return arch.as_flowable()

        elif norm_block_type == "c4":
            c4 = pd.C4ContainerDiagram(
                width=width, height=height, theme=theme, caption=caption
            )
            for line in dsl_lines:
                kwargs = parse_kwargs(line)
                parts = re.findall(r'(?:[^\s"\']|"[^"]*"|\'[^\']*\')+', line)
                if not parts:
                    continue
                cmd = parts[0].lower()

                if cmd == "system":
                    name = kwargs.get("name")
                    desc = kwargs.get("desc") or kwargs.get("description")
                    if not name and len(parts) > 1:
                        name = parts[1].strip("\"'")
                        if len(parts) > 2:
                            desc = parts[2].strip("\"'")
                    if name:
                        c4.system(name, desc or "")
                elif cmd == "container":
                    name = kwargs.get("name")
                    tech = kwargs.get("tech") or kwargs.get("technology")
                    desc = kwargs.get("desc") or kwargs.get("description")
                    if not name and len(parts) > 1:
                        name = parts[1].strip("\"'")
                        if len(parts) > 2:
                            tech = parts[2].strip("\"'")
                        if len(parts) > 3:
                            desc = parts[3].strip("\"'")
                    if name:
                        c4.container(name, tech or "", desc or "")
                elif cmd in ("relate", "connect", "link", "edge"):
                    from_item = kwargs.get("from") or kwargs.get("src")
                    to_item = kwargs.get("to") or kwargs.get("dst")
                    label = kwargs.get("label")
                    if not from_item and not to_item and len(parts) > 2:
                        from_item = parts[1].strip("\"'")
                        to_item = parts[2].strip("\"'")
                        if len(parts) > 3:
                            label = parts[3].strip("\"'")
                    if from_item and to_item:
                        c4.relate(from_item, to_item, label or "")

            return c4.as_flowable()

        elif norm_block_type == "aws":
            aws = pd.AWSDiagram(
                width=width, height=height, theme=theme, caption=caption
            )
            for line in dsl_lines:
                kwargs = parse_kwargs(line)
                parts = re.findall(r'(?:[^\s"\']|"[^"]*"|\'[^\']*\')+', line)
                if not parts:
                    continue
                cmd = parts[0].lower()

                if cmd in ("ec2", "rds", "s3", "lambda", "lambda_fn", "sqs"):
                    name = kwargs.get("name")
                    label = kwargs.get("label")
                    if not name and len(parts) > 1:
                        name = parts[1].strip("\"'")
                        if len(parts) > 2:
                            label = parts[2].strip("\"'")
                    if name:
                        if cmd == "ec2":
                            aws.ec2(name, label or "")
                        elif cmd == "rds":
                            aws.rds(name, label or "")
                        elif cmd == "s3":
                            aws.s3(name, label or "")
                        elif cmd in ("lambda", "lambda_fn"):
                            aws.lambda_fn(name, label or "")
                        elif cmd == "sqs":
                            aws.sqs(name, label or "")
                elif cmd in ("connect", "link", "edge"):
                    from_node = kwargs.get("from") or kwargs.get("src")
                    to_node = kwargs.get("to") or kwargs.get("dst")
                    label = kwargs.get("label")
                    if not from_node and not to_node and len(parts) > 2:
                        from_node = parts[1].strip("\"'")
                        to_node = parts[2].strip("\"'")
                        if len(parts) > 3:
                            label = parts[3].strip("\"'")
                    if from_node and to_node:
                        aws.connect(from_node, to_node, label or "")

            return aws.as_flowable()

    except Exception as exc:
        sys.stderr.write(f"Warning: Failed to compile diagram DSL: {exc}\n")
        return None

    return None


def compile_markdown_to_pdf(
    input_file: str,
    output_file: Optional[str] = None,
    theme_name: str = "dark",
    title: Optional[str] = None,
    author: Optional[str] = None,
) -> None:
    """
    Parse a markdown file and compile it into a themed PDF notes document.
    """
    if not os.path.exists(input_file):
        raise PDFCompilerError(f"Input file not found: {input_file}")

    try:
        with open(input_file, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except Exception as exc:
        raise PDFCompilerError(f"Failed to read input file {input_file}: {exc}")

    metadata, content_lines = parse_metadata(lines)

    doc_title = metadata.get("title", title)
    doc_author = metadata.get("author", author)
    doc_theme = metadata.get("theme", theme_name).lower()

    pn.set_story([])

    all_themes = {
        "dark": pn.DARK,
        "light": pn.LIGHT,
        "ocean-dark": pn.OCEAN_DARK,
        "forest-dark": pn.FOREST_DARK,
        "sunset-dark": pn.SUNSET_DARK,
        "midnight-dark": pn.MIDNIGHT_DARK,
        "ocean-light": pn.OCEAN_LIGHT,
        "sepia": pn.SEPIA,
        "catppuccin-latte": pn.CATPPUCCIN_LATTE,
        "catppuccin-mocha": pn.CATPPUCCIN_MOCHA,
    }

    theme_obj = all_themes.get(doc_theme, pn.DARK)
    pn.set_theme(theme_obj)

    if doc_title:
        pn.bookmark("Cover Page")
        pn.suppress_footer(page_only=True)
        pn.add(Spacer(1, 40))
        pn.add(Table([[Paragraph(doc_title, pn.COVER_H1)]], colWidths=[pn.CW]))
        pn.add(Spacer(1, 10))
        if doc_author:
            pn.add(Paragraph(f"Author: {doc_author}", pn.COVER_SUB))
        pn.add(PageBreak())
        pn.toc()

    pn.footer(
        left=doc_title if doc_title else "Study Notes",
        right=doc_author if doc_author else "",
        show_page_num=True,
    )

    parse_markdown_lines(content_lines)

    if not output_file:
        base, _ = os.path.splitext(input_file)
        output_file = f"{base}.pdf"

    try:
        pn.build_doc(output_file, title=doc_title, author=doc_author)
    except Exception as exc:
        raise PDFCompilerError(f"Failed to build PDF output {output_file}: {exc}")


def parse_markdown_lines(content_lines: List[str]) -> None:
    """Parse markdown lines and append content flowables to the active story."""
    in_code_block = False
    code_block_lang = ""
    code_block_lines: List[str] = []

    in_alert = False
    alert_type = ""
    alert_lines: List[str] = []

    bullet_items: List[str] = []

    in_table = False
    table_rows: List[List[str]] = []
    table_header: List[str] = []

    def flush_table() -> None:
        nonlocal in_table, table_rows, table_header
        if in_table and table_header:
            formatted_header = [format_inline_markdown(h) for h in table_header]
            formatted_rows = [
                [format_inline_markdown(cell) for cell in row]
                for row in table_rows
            ]
            pn.info_table(formatted_header, formatted_rows)
            table_rows.clear()
            table_header.clear()
        in_table = False

    def flush_bullets() -> None:
        if bullet_items:
            pn.bullet(bullet_items)
            bullet_items.clear()

    def flush_alert() -> None:
        nonlocal in_alert, alert_type, alert_lines
        if in_alert and alert_lines:
            text = " ".join(alert_lines)
            if alert_type == "note":
                pn.note(text)
            elif alert_type == "tip":
                pn.tip(text)
            elif alert_type in ("warning", "caution"):
                pn.highlight(text)
            alert_lines.clear()
            in_alert = False

    idx = 0
    while idx < len(content_lines):
        line = content_lines[idx]
        line_strip = line.strip()

        if line_strip.startswith("```"):
            if in_code_block:
                if code_block_lang in (
                    "flowchart",
                    "sequence",
                    "layeredstack",
                    "schema",
                    "er",
                    "git",
                    "architecture",
                    "arch",
                    "c4",
                    "c4container",
                    "aws",
                    "cloud",
                ):
                    diagram_flowables = parse_diagram_dsl(
                        code_block_lang, code_block_lines
                    )
                    if diagram_flowables:
                        for f in diagram_flowables:
                            pn.add(f)
                else:
                    code_text = "\n".join(code_block_lines)
                    pn.code_block(code_text, lang=code_block_lang)

                in_code_block = False
                code_block_lines.clear()
            else:
                flush_bullets()
                flush_alert()
                in_code_block = True
                code_block_lang = line_strip[3:].strip().lower()
                code_block_lines = []

            idx += 1
            continue

        if in_code_block:
            code_block_lines.append(line.rstrip("\n"))
            idx += 1
            continue

        # Table detection (GitHub-flavored markdown)
        is_table_line = False
        if (
            not in_code_block
            and not in_alert
            and "|" in line_strip
            and not line_strip.startswith(">")
        ):
            parts = [c.strip() for c in line_strip.split("|")]
            if parts and parts[0] == "":
                parts = parts[1:]
            if parts and parts[-1] == "":
                parts = parts[:-1]
            if len(parts) >= 2:
                is_separator = all(
                    re.match(r"^:?-+:?$", p) for p in parts
                )
                if is_separator:
                    in_table = True
                    idx += 1
                    is_table_line = True
                elif not in_table:
                    table_header = parts
                    in_table = True
                    idx += 1
                    is_table_line = True
                else:
                    table_rows.append(parts)
                    idx += 1
                    is_table_line = True

        if in_table and not is_table_line:
            flush_table()

        if is_table_line:
            continue

        alert_match = re.match(
            r"^>\s*\[!(NOTE|TIP|WARNING|CAUTION)\](.*)", line_strip, re.IGNORECASE
        )
        if alert_match:
            flush_bullets()
            flush_alert()
            in_alert = True
            alert_type = alert_match.group(1).lower()
            initial_text = alert_match.group(2).strip()
            if initial_text:
                alert_lines.append(format_inline_markdown(initial_text))
            idx += 1
            continue

        if in_alert:
            if line_strip.startswith(">"):
                content = line_strip[1:].strip()
                if content:
                    alert_lines.append(format_inline_markdown(content))
                idx += 1
                continue
            else:
                flush_alert()

        bullet_match = re.match(r"^^[\-\*\+]\s+(.*)", line_strip)
        if bullet_match:
            flush_alert()
            bullet_items.append(format_inline_markdown(bullet_match.group(1)))
            idx += 1
            continue
        elif line_strip:
            if not in_alert:
                flush_bullets()

        if line_strip.startswith("#"):
            flush_bullets()
            flush_alert()
            flush_table()

            level = 0
            while level < len(line_strip) and line_strip[level] == "#":
                level += 1

            title_text = line_strip[level:].strip()
            title_formatted = format_inline_markdown(title_text)

            if level == 1:
                pn.part_box(title_formatted)
            elif level == 2:
                pn.chap_box(title_formatted)
            elif level == 3:
                pn.section(title_formatted)
            else:
                pn.subsection(title_formatted)

            idx += 1
            continue

        if not line_strip:
            flush_bullets()
            flush_alert()
            flush_table()
            idx += 1
            continue

        pn.body(format_inline_markdown(line_strip))
        idx += 1

    flush_bullets()
    flush_alert()
    flush_table()


def main() -> None:
    """CLI entrypoint."""
    parser = argparse.ArgumentParser(
        description="Compile Markdown documents to themed ReportLab PDFs with native diagrams."
    )
    parser.add_argument("input", help="Path to the input markdown file.")
    parser.add_argument(
        "-o",
        "--output",
        help="Path to the output PDF file (defaults to same name with .pdf extension).",
    )
    parser.add_argument(
        "-t",
        "--theme",
        default="dark",
        help="Theme name (options: dark, light, ocean-dark, forest-dark, catppuccin-mocha, etc. Default: dark).",
    )
    parser.add_argument("--title", help="Document title metadata.")
    parser.add_argument("--author", help="Document author metadata.")

    args = parser.parse_args()

    try:
        compile_markdown_to_pdf(
            input_file=args.input,
            output_file=args.output,
            theme_name=args.theme,
            title=args.title,
            author=args.author,
        )
        print(
            f"Successfully compiled PDF document: {args.output if args.output else args.input.replace('.md', '.pdf')}"
        )
    except PDFCompilerError as err:
        sys.stderr.write(f"Error: {err}\n")
        sys.exit(1)
    except Exception as exc:
        sys.stderr.write(f"Unhandled error: {exc}\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
