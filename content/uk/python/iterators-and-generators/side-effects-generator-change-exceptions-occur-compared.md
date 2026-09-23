---
id: py-itergen-0008
title: "Як side effects у generator змінюють момент виникнення exceptions порівняно з eager list construction?"
description: "Side effects у generator відкладені до моменту споживання, тому exception виникає лише при next(), а не при створенні."
track: python
section: iterators-and-generators
level: senior
type: mechanism
tags: []
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: py314-library-stdtypes-iterator-types
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html#iterator-types
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-expressions-yield-expressions
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#yield-expressions
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-datamodel-object-iter
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__iter__
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
---

## Short answer

**Side effects у generator відкладені до моменту споживання, тому exception виникає лише при `next()`, а не при створенні.**[^py314-library-stdtypes-iterator-types] На відміну від list comprehension, де всі side effects виконуються одразу під час побудови списку, generator виконує код ліниво. Якщо generator не спожито повністю, частину side effects може бути взагалі не виконано, а `GeneratorExit` або GC можуть запустити cleanup.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
