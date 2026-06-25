# Diagram: Schema

Schema diagrams display database table structures: columns, data types, primary key and foreign key markers, plus labelled relationship arcs.

## Minimal example

```python
import paperforge_notes as pn
import paperforge_diagrams as pd

schema = pd.SchemaDiagram(
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

pn.add(schema.as_flowable())
```

## Column flags

```python
schema.table("orders", [
    ("id",        "INTEGER", {"pk": True}),    # Primary Key
    ("user_id",   "INTEGER", {"fk": True}),     # Foreign Key
    ("total",     "DECIMAL", {}),
])
```

- `pk=True`: **PK** appended, bold accent-colored text
- `fk=True`: **(FK)** appended, relation-colored text

## Auto layout

If every table is at `(0, 0)` (the default), SchemaDiagram distributes them on a grid automatically:

```python
schema.table("users", [...])
schema.table("orders", [...])
schema.table("products", [...])
# → auto-positioned in a grid
```

## Choosing between ER and Schema

Use `ERDiagram` when you care about:

- Chen notation (entity rectangles, diamonds)
- Weak vs strong entities
- Cardinalities (1, N, M)
- Identifying relationships

Use `SchemaDiagram` when you care about:

- Table-like view with column types
- Primary / Foreign key markers
- Quick SQL-style wireframes

## Next

- [ER Diagram](er.md)
- [Architecture](architecture.md)
