# Diagram: Class (UML)

UML class diagrams express OOP structure: classes with stereotypes, attributes, methods, and six relationship types.

## Relationship kinds

| Kind | Line style | Arrowhead |
| ---- | ---------- | --------- |
| `inheritance` | solid | open triangle up |
| `realization` | dashed | open triangle up |
| `composition` | solid | filled diamond |
| `aggregation` | solid | open diamond |
| `association` | solid | open triangle |
| `dependency` | dashed | open triangle |

## Minimal example

```python
import paperforge_notes as pn
import paperforge_diagrams as pd

cd = pd.ClassDiagram(width=420, height=200, caption="Fig 5: Shape Inheritance")

cd.uml_class(
    "Animal", "Animal",
    stereotype="abstract",
    methods=["+speak(): void"],
)
cd.uml_class("Dog", "Dog",
    attributes=["-name: String", "-age: int"],
    methods=["+speak(): void", "+fetch(): void"],
)
cd.relate("Dog", "Animal", kind="inheritance")
cd.relate("Dog", "Animal", kind="realization", label="implements")

pn.add(cd.as_flowable())
```

## Multiplicity labels

```python
cd.relate(
    "Department", "Employee",
    kind="association",
    from_mult="1", to_mult="0..*",
    label="employs"
)
```

## Layout

Only specify x, y when you need manual positioning. Otherwise let `auto_layout()` decide:

```python
cd.uml_class("A", "A")
cd.uml_class("B", "B")
cd.relate("A", "B", kind="dependency")
```


