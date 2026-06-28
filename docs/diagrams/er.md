# Diagrams: ER and Schema

This page covers `ERDiagram` (Chen notation -professional- style) and `SchemaDiagram` (plain database table with FK lines).

## ERDiagram

Entity-Relationship diagrams use Chen notation: rectangles for entities, diamonds for relationships, rounded rectangles or ovals for attributes.

### Quick example

```python
import engrapha_notes as en
import engrapha_diagrams as ed

er = ed.ERDiagram(width=450, height=220, caption="Fig 3: University ER Model")

er.entity("STUDENT")
er.entity("COURSE")
er.relationship("ENROLLS")

er.entity_attributes(
    "STUDENT",
    [("Student_ID", {"pk": True}), "Name", ("Email", {"derived": True})],
)
er.entity_attributes(
    "COURSE",
    [("Course_ID", {"pk": True}), "Title"],
)

er.connect("STUDENT", "ENROLLS", card_from="1", card_to="N")
er.connect("COURSE", "ENROLLS", card_from="1", card_to="N")

en.add(er.as_flowable())
en.build_doc("er.pdf")
```

### Entities

```python
er.entity("STUDENT", weak=False)   # Strong (default)
er.entity("COURSE", weak=True)     # Weak
```

### Relationships

```python
er.relationship("ENROLLS", identifying=True)
```

### Attributes

```python
er.attribute("Grade", parent="ENROLLS", x=225, y=55)
```

Or use `entity_attributes(...)` for concentric-circle layout:

```python
er.entity_attributes(
    "STUDENT",
    [
        ("ID",          {"pk": True}),
        "Name",
        ("Email",       {"derived": True}),
        ("Phone",       {"multivalued": True}),
    ],
    distance=70.0,
    start_angle=90.0,
)
```

### Connections

```python
er.connect("STUDENT", "ENROLLS",
           card_from="1", card_to="N",
           total_from=True, total_to=False)
```

Boundary conditions:

- `total_from` / `total_to` uses a double-line symbol (total participation).
- Several cardinality label strings supported: `"1"`, `"N"`, `"M"`, `"0..1"`.

## SchemaDiagram

Schema diagrams display table structures: columns, types, primary and foreign key markers, plus labelled relationship arcs.

### Quick example

```python
import engrapha_notes as en
import engrapha_diagrams as ed

schema = ed.SchemaDiagram(
    width=450, height=200, caption="Fig 4: Blog Schema"
)

schema.table("users", [
    ("id",         "INTEGER", {"pk": True}),
    ("email",      "VARCHAR", {}),
    ("created_at", "TIMESTAMP", {}),
])

schema.table("posts", [
    ("id",          "INTEGER",  {"pk": True}),
    ("user_id",     "INTEGER",  {"fk": True}),
    ("title",       "VARCHAR",  {}),
    ("published_at", "TIMESTAMP", {}),
])

schema.relation("posts", "user_id", "users", "id")

en.add(schema.as_flowable())
en.build_doc("schema.pdf")
```

### Column flags

```python
schema.table("orders", [
    ("id",        "INTEGER", {"pk": True}),    # Primary Key
    ("user_id",   "INTEGER", {"fk": True}),     # Foreign Key
    ("total",     "DECIMAL", {}),
])
```

- `pk=True`: **PK** appended, bold king-colored text
- `fk=True`: **(FK)** appended, relation-colored text

### Auto layout

If every table is at `(0, 0)` (the default), SchemaDiagram distributes them on a grid automatically:

```python
schema.table("users", [...])
schema.table("orders", [...])
schema.table("products", [...])
# → auto-positioned in a 2×2 grid
```

## Choosing between ER and Schema

Use `ERDiagram` when you care about:

- Chen notation (entity rectangles or rounded, double diamonds)
- Weak vs strong entities
- Cardinalities (1, N, M)
- Identifying relationships

Use `SchemaDiagram` when you care about:

- Table-like view with column types
- Primary / Foreign key markers
- Quick SQL-style wireframes

## Next

- [Schema](schema.md)
- [Class](class.md)

