---
id: py-oop-0017
title: "Чому zero-argument `super()` означає «наступний у MRO», а не просто «безпосередній parent class»?"
description: "super() без аргументів еквівалентний super(__class__, <перший аргумент методу>) і шукає наступний клас у MRO фактичного типу об'єкта, а не класу, де super() написаний."
track: python
section: oop-and-data-model
level: middle
type: mechanism
tags: [super]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: py314-reference-datamodel
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-howto-descriptor
    title: "Python 3.14: Howto/descriptor"
    url: https://docs.python.org/3.14/howto/descriptor.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-howto-mro
    title: "Python 3.14: Howto/mro"
    url: https://docs.python.org/3.14/howto/mro.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-dataclasses
    title: "Python 3.14: Library/dataclasses"
    url: https://docs.python.org/3.14/library/dataclasses.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
---

## Short answer

**`super()` без аргументів еквівалентний `super(__class__, <перший аргумент методу>)` і шукає наступний клас у MRO фактичного типу об'єкта, а не класу, де `super()` написаний.**[^py314-reference-datamodel] Це ключово для cooperative multiple inheritance: у diamond `D -> B, C -> A` виклик `super()` у `B` може передати керування `C` (а не `A`), якщо MRO фактичного типу такий. Текстове написання `super()` не фіксує parent – порядок визначається динамічно через `__mro__` runtime-типу.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
