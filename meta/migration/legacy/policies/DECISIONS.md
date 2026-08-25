# Project decisions

## Scope

- Primary: Python Core, CPython where relevant, standard library, testing, performance and coding.
- Brief overview only: algorithms/data structures, databases/SQL, Git/CI/CD/SDLC.
- Excluded: Web/API, Django, DRF, FastAPI, SQLAlchemy, frontend and area-specific infrastructure.

## Language and terminology

- Explanations and questions: Ukrainian.
- Code, identifiers, API names and established Python terms: English.
- Use `картка` for card, `нотатка` for Anki note and `колода` for deck.
- Keep `trade-off`, `runtime`, `bytecode`, `event loop`, `free-threaded` and `GIL-enabled`
  in English where a Ukrainian substitute would make the interview terminology less recognizable.

## Storage

- One production package: `Python Interview Questions.apkg`, with one root deck and 23 topic subdecks.
- One note type: `Python Interview Basic` with `Front` and `Back`.
- One reviewed TSV source deck per topic directly in `cards/`; topics are tags, not subdecks.
- Tags are hierarchical and space-separated.
- All files use UTF-8; TSV rows use real TAB separators.

## Versioning

- Baseline as of 2026-09-02: stable Python 3.14.
- Python 3.15 content is preview until its final release.
- Language rules, CPython details and version-dependent behavior are never presented as interchangeable.

## AI

- AI is a drafting and review tool, not the factual authority.
- Generation and final review are separate passes.
- Generation is grounded in topic-specific supplied sources.
- Code and version-sensitive claims receive executable or authoritative verification.

## Quality gates

- Overview topics are capped at 7 accepted cards each. The cap is a ceiling, not a quota.
- Package-source TSV files require metadata, HTML, provenance, coverage, Code-card evidence, and
  Anki smoke validation. Front-only work is not stored in this repository.
