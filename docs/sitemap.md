# Sitemap

A semantic map of all documentation pages for Engrapha, helping both users and AI agents navigate the codebase tools.


## Home
- [Home](index.md) - Generate beautiful PDFs, notes, diagrams, slides, and flashcards from Python or Markdown.

## Getting Started
- [Getting Started](getting-started.md) - Engrapha lets you produce themed academic PDFs, vector diagrams, and flashcards with just a few lines of Python.
- [Why Engrapha?](why-engrapha.md) - Several tools can help you produce diagrams or notes. Engrapha's value is combining all of them into one Python toolkit with vector-native graphics,...

## Notes
- [Notes: Basics](notes/basics.md) - This page covers the core API of `engrapha_notes`: themes, headings, body, and footers. By the end of this page you'll be able to construct a struct...
- [Notes: Callouts and Highlights](notes/callouts.md) - Engrapha ships with semantic callout blocks for all the most common exam-note situations.
- [Notes: Study and Revision Helpers](notes/study.md) - Engrapha ships several blocks specifically for preparation: question, qbox, mcq, revision card, and flashcard.
- [Notes: Advanced](notes/advanced.md) - Advanced ingredients you will need for full-length textbooks, lab reports, and research notes.
- [Notes: Templates](notes/templates.md) - Engrapha ships built-in helpers for common document types. Each returns a ready-to-use `NotesTheme`, so you do not have to configure fonts, colors, ...
- [Notes: Export Formats](notes/export.md) - Once your story is assembled, Engrapha can emit PDF, HTML, PPTX, and Anki packages.

## Diagrams
- [Diagrams: Overview](diagrams/overview.md) - Engrapha ships with 13 vector-native diagram types. This page helps you pick the right one.
- [Diagram: Flowchart](diagrams/flowchart.md) - Draw ANSI/ISO flowchart symbols: terminals (pills), rectangles, decisions (diamonds), I/O (parallelograms), connectors (circles), and predefined-proce...
- [Diagram: Sequence](diagrams/sequence.md) - A UML sequence diagram maps ordered message arrows over lifelines. Each actor is placed left-to-right at the top. A dashed lifeline drops down. Activa...
- [Diagrams: ER and Schema](diagrams/er.md) - This page covers `ERDiagram` (Chen notation -professional- style) and `SchemaDiagram` (plain database table with FK lines).
- [Diagram: Schema](diagrams/schema.md) - Schema diagrams display database table structures: columns, data types, primary key and foreign key markers, plus labelled relationship arcs.
- [Diagram: Class (UML)](diagrams/class.md) - UML class diagrams express OOP structure: classes with stereotypes, attributes, methods, and six relationship types.
- [Diagram: State Machine](diagrams/state-machine.md) - State machines are suitable for DFAs, process states, and life-cycle flows. States are circles (double-circles for accepting states). Transitions are ...
- [Diagram: Network](diagrams/network.md) - Network topology diagrams render hosts, switches, routers, clouds, firewalls, databases, wireless points, and more. Presets for `bus`, `star`, `ring`,...
- [Diagrams: Architecture, C4, and AWS](diagrams/architecture.md) - Three closely related diagram types: `ArchitectureDiagram`, `C4ContainerDiagram`, and `AWSDiagram`. All share the same auto-layout engine and orthogon...
- [Diagram: C4 Container](diagrams/c4.md) - C4 Container diagrams document software systems and their containers (web apps, databases, APIs) with descriptive relationships.
- [Diagram: AWS Cloud](diagrams/cloud.md) - AWS diagrams render vector-native AWS resource icons on top of the standard ArchitectureDiagram layout. All auto-layout and orthogonal routing from `A...
- [Diagram: Layered Stack](diagrams/stack.md) - LayeredStack draws horizontal layers and dividers. Ideal for OSI/TCP-IP stacks, memory hierarchies, and any stacked software structure.
- [Diagram: Timing](diagrams/timing.md) - Timing diagrams render digital waveforms side-by-side, perfect for busses, SPI, I2C, and memory timing.
- [Diagram: Git](diagrams/git.md) - Git diagrams visualize branches, commits, and merge commits on horizontal or vertical timelines.

## Gallery
- [Gallery](gallery/index.md) - Screenshots and examples for each diagram type and theme combination. Screenshots will be added later; placeholder markers are in place.
- [Gallery: Flowcharts](gallery/flowcharts.md) - Flowcharts are the most frequently used diagram type in Engrapha. This page shows standard variations.
- [Gallery: ER Diagrams](gallery/er-diagrams.md) - ER and Schema diagrams built with the Chen and SQL table notations.
- [Gallery: Sequence Diagrams](gallery/sequence-diagrams.md) - Sequence diagrams express API calls, handshake protocols, and event ordering.
- [Gallery: Network Diagrams](gallery/network-diagrams.md) - Network topology examples: simple LAN, bus topology, star, mesh, and tree.
- [Gallery: Architecture Diagrams](gallery/architectures.md) - System architecture and cloud topology examples.
- [Gallery: Themes](gallery/themes.md) - The same diagram rendered in every preset Engrapha theme. This page shows the power and clean auto-matching of the theme system.
- [Gallery: Notes Pages](gallery/notes-pages.md) - Full page screenshots of notes documents generated by Engrapha. Each entry shows a representative document-type alongside the Python that generates ...

## Examples
- [Example: Engineering Notes](examples/engineering-notes.md) - A complete engineering-notes session using Engrapha.
- [Example: Resume](examples/resume.md) - A single-page resume using Engrapha's section blocks, bullet lists, and timeline blocks.
- [Example: Assignment](examples/assignment.md) - Assignment sheet with question numbers, code blocks, marking rubrics, and MCQs.
- [Example: Thesis Chapter](examples/thesis.md) - Academic chapter with sections, citations, formulas, index entries, and an embedded diagram.
- [Example: Networking Notes](examples/networking-notes.md) - Networking notes using OSI-layer stacks, packet header diagrams, and sequence diagrams to show the stack holistically.

## API Reference
- [API Reference: engrapha_notes](api/notes.md) - Quick reference grouped by purpose. Full docstrings are in the source.
- [API Reference: engrapha_diagrams](api/diagrams.md) - All public classes and their constructors. Every diagram inherits from `DiagramBase` which exposes `save(filename)`, `as_flowable()`, and `theme`.

## Themes
- [Themes](themes.md) - Engrapha comes with **10 preset themes** for `engrapha_diagrams` and **15 preset themes** for `engrapha_notes`.

## Markdown
- [Markdown Compiler](markdown.md) - Engrapha ships with a CLI tool that compiles standard Markdown files into themed PDFs. Two commands, `engrapha` and `pdfnotes`, are installed by t...

## Changelog
- [Changelog](changelog.md) - All notable changes to Engrapha are documented here. Engrapha follows [Semantic Versioning](https://semver.org/).

## Contributing
- [Contributing](contributing.md) - Thank you for considering contributing to Engrapha! This page explains how to set up a development environment, run tests, and submit changes.

## Sitemap
- [Sitemap](sitemap.md) - A semantic map of all documentation pages for Engrapha, helping both users and AI agents navigate the codebase tools.

---

For a structured index optimized for LLMs, see [llms.txt](llms.txt).

