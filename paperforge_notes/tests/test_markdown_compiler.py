from __future__ import annotations

from paperforge_notes.cli import compile_markdown_to_pdf, parse_diagram_dsl

def test_parse_new_diagram_dsls() -> None:
    # 1. Test Schema Diagram DSL
    schema_dsl = [
        "width = 400",
        "height = 200",
        "table users:",
        "  id: INT (pk)",
        "  name: VARCHAR",
        "table orders:",
        "  id: INT (pk)",
        "  user_id: INT (fk) -> users.id",
    ]
    flowables = parse_diagram_dsl("schema", schema_dsl)
    assert flowables is not None
    assert len(flowables) == 1
    assert flowables[0].__class__.__name__ == "ResponsiveDrawingFlowable"

    # 2. Test Git Diagram DSL
    git_dsl = [
        "commit branch=main label='Init'",
        "branch parent=main child=dev",
        "commit branch=dev label='Feature'",
        "merge from=dev to=main label='Merge'",
    ]
    flowables = parse_diagram_dsl("git", git_dsl)
    assert flowables is not None
    assert len(flowables) == 1

    # 3. Test Architecture Diagram DSL
    arch_dsl = [
        "client web 'Web App'",
        "service api 'Auth API'",
        "database db 'Postgres'",
        "connect web api",
        "connect api db",
    ]
    flowables = parse_diagram_dsl("architecture", arch_dsl)
    assert flowables is not None
    assert len(flowables) == 1

    # 4. Test C4 Diagram DSL
    c4_dsl = [
        "system sys 'My Software'",
        "container db 'Database' 'MySQL' 'Stores data'",
        "relate sys db 'Reads/Writes'",
    ]
    flowables = parse_diagram_dsl("c4", c4_dsl)
    assert flowables is not None
    assert len(flowables) == 1

    # 5. Test AWS Diagram DSL
    aws_dsl = [
        "ec2 instance 'Web'",
        "rds database 'DB'",
        "s3 bucket 'Assets'",
        "connect instance database",
        "connect instance bucket",
    ]
    flowables = parse_diagram_dsl("aws", aws_dsl)
    assert flowables is not None
    assert len(flowables) == 1

def test_compile_markdown_with_diagram_fences(tmp_path) -> None:
    md_content = """---
title: System Design Notes
author: test-author
---

# Section Title

Here is a system architecture overview:

```architecture
width = 400
height = 180
client user "Web Browser"
service server "API Gateway"
database rds "RDS Postgres"
connect user server "HTTPS"
connect server rds "SQL"
```

## Database Schema

```schema
width = 300
height = 150
table users:
  id: INT (pk)
  email: VARCHAR
```
"""
    md_file = tmp_path / "notes.md"
    md_file.write_text(md_content, encoding="utf-8")
    
    pdf_file = tmp_path / "notes.pdf"
    
    # Run compiler
    compile_markdown_to_pdf(str(md_file), str(pdf_file))
    
    assert pdf_file.exists()
    assert pdf_file.stat().st_size > 1000
