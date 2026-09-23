---
id: py-itergen-0005
title: "Коли виконується тіло generator function: під час виклику функції чи першого `next()`?"
description: "Тіло generator function не виконується під час виклику – воно запускається лише при першому next()."
track: python
section: iterators-and-generators
level: middle
type: mechanism
tags: [next]
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

**Тіло generator function не виконується під час виклику – воно запускається лише при першому `next()`.**[^py314-library-stdtypes-iterator-types] Виклик generator function миттєво повертає generator object без виконання жодного рядка тіла. Перший `next()` (або `for`) запускає виконання з початку до першого `yield`. Тому помилки в тілі виникають лише під час ітерації, а не при створенні generator.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
