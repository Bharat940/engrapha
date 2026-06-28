# Changelog

All notable changes to Engrapha are documented here. Engrapha follows [Semantic Versioning](https://semver.org/).

## [Unreleased]

### In progress

- Documentation website (mkdocs + Material)

## [0.1.0] - 2026

Initial public release of Engrapha. Both packages contain feature-complete implementations:

### Engrapha Diagrams — `engrapha_diagrams`
- **Flowchart**: ANSI/ISO shapes with orthogonal routing
- **SequenceDiagram**: UML sequence with activation bars
- **ClassDiagram**: UML class with inheritance, composition, etc.
- **ERDiagram**: Chen notation with primary keys, multi-valued attributes
- **StateMachine**: DFA/NFA with initial/accepting state markers
- **NetworkDiagram**: hosts, servers, switches, clouds, topologies
- **ArchitectureDiagram**: clients, services, databases, queues
- **C4ContainerDiagram**: System / Container / relations
- **AWSDiagram**: vector-native EC2, RDS, S3, Lambda, SQS icons
- **GitDiagram**: branches, commits, merges
- **SchemaDiagram**: tables with foreign keys
- **TimingDiagram**: digital waveforms
- **LayeredStack**: OSI / TCP-IP / memory hierarchy
- 10 preset themes + custom theme support
- `DiagramTheme.from_notes_theme()` for theme matching
- Vector-native PDF/SVG/PNG export

### Engrapha Notes — `engrapha_notes`
  - 15 preset themes + ThemeBuilder + print-light theme
  - Cover cards, part / chap / section / subsection blocks
  - Callouts: tip, note, warning, important, exam, theorem, proof
  - Question blocks, qbox, answer, mcq, revision_card
  - Flashcards with Anki APKG / CSV / JSON export
  - Tables, code blocks with Pygments syntax highlighting
  - Formula / formula_block (LaTeX math via matplotlib mathtext)
  - Image with remote caching & fallbacks
  - Frame and packet format helpers (Ethernet, IPv4 header)
  - Multiple page numbering styles
  - Running headers and footers
  - TOC, bookmarks, footnotes, indices
  - Markdown CLI compiler
  - 4 export formats: PDF, HTML, PPTX, multiple-from-one document

### Security

  - No external network or binaries required
  - No raster fallbacks
  - Standard fonts only by default

