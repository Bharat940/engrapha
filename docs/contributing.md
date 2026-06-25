# Contributing

Thank you for considering contributing to PaperForge! This page explains how to set up a development environment, run tests, and submit changes.

## Development Setup

```bash
git clone https://github.com/bharatdangi/paperforge
cd paperforge

pip install -e ./paperforge -e ./paperforge_diagrams -e ./paperforge_notes[dev]
```

## Documentation Build

To preview the docs site locally:

```bash
pip install "mkdocs-material[full]"
mkdocs serve
```

## Running Tests

Both packages use **pytest**:

```bash
# Diagrams package
pytest paperforge_diagrams/tests/

# Notes package
pytest paperforge_notes/tests/

# Combined
pytest
```

## Linting & Type-checking

```bash
ruff check .
ruff format .
mypy paperforge_diagrams paperforge_notes
```

## Adding a New Diagram

1. Create `/paperforge_diagrams/<diagram_name>.py`
2. Define a `DiagramBase` subclass with:
   - `_add_node(...)` / similar methods
   - `build()` to render shapes via `self.theme`
   - `as_flowable()` to return the platform Flowable list
3. Register the public class in `paperforge_diagrams/__init__.py`
4. Add usage docs to `docs/diagrams/<diagram_name>.md`
5. Reference the diagram in the gallery's `docs/diagrams/overview.md`
6. Add a screenshot placeholder under `docs/assets/screenshots/<diagram>.png`
7. Add a smoke test under `tests/`

## Adding a New Theme

1. Add the `NotesTheme` instance to `paperforge_notes/theme.py` (mention it in `ALL_THEMES`)
2. Add the matching `DiagramTheme` mapping in `paperforge_diagrams/theme.py`'s `from_notes_theme()` if accent colors diverge
3. Document the theme in `themes.md`

## Submitting a PR

1. Fork the repo
2. Create a feature branch: `git checkout -b feat/my-change`
3. Make your changes with appropriate tests
4. Run `pytest`, `ruff`, `mypy` locally and ensure all green
5. Open a PR with a clear description and screenshots if visual

## Documentation fixes / additions

Pull requests to fix typos or improve examples are welcome! Author the change under `docs/` directly.

For new concepts or significant changes, please open an issue first.

## Release process

PaperForge follows semantic versioning. Maintainers will handle release tagging.

For announcements, follow the [GitHub releases page](https://github.com/bharatdangi/paperforge/releases).

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
