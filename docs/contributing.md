# Contributing

Thank you for considering contributing to Engrapha! This page explains how to set up a development environment, run tests, and submit changes.

## Development Setup

```bash
git clone https://github.com/Bharat940/engrapha
cd engrapha

pip install -e ./packages/engrapha -e ./packages/engrapha_diagrams -e ./packages/engrapha_notes[dev]
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
pytest packages/engrapha_diagrams/tests/

# Notes package
pytest packages/engrapha_notes/tests/

# Combined
pytest
```

## Linting & Type-checking

```bash
ruff check .
ruff format .
mypy packages/engrapha_diagrams packages/engrapha_notes
```

## Adding a New Diagram

1. Create `/packages/engrapha_diagrams/src/engrapha_diagrams/<diagram_name>.py`
2. Define a `DiagramBase` subclass with:
   - `_add_node(...)` / similar methods
   - `build()` to render shapes via `self.theme`
   - `as_flowable()` to return the platform Flowable list
3. Register the public class in `packages/engrapha_diagrams/src/engrapha_diagrams/__init__.py`
4. Add usage docs to `docs/diagrams/<diagram_name>.md`
5. Reference the diagram in the gallery's `docs/diagrams/overview.md`
6. Add a screenshot placeholder under `docs/assets/screenshots/<diagram>.png`
7. Add a smoke test under `tests/`

## Adding a New Theme

1. Add the `NotesTheme` instance to `packages/engrapha_notes/src/engrapha_notes/theme.py` (mention it in `ALL_THEMES`)
2. Add the matching `DiagramTheme` mapping in `packages/engrapha_diagrams/src/engrapha_diagrams/theme.py`'s `from_notes_theme()` if accent colors diverge
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

Engrapha follows semantic versioning. Maintainers will handle release tagging.

For announcements, follow the [GitHub releases page](https://github.com/Bharat940/Engrapha/releases).

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

