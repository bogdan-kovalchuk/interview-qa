---
id: py-itergen-0006
title: "Який state зберігає suspended generator між двома `yield` і що відбувається після його завершення?"
description: "Suspended generator зберігає локальні змінні, instruction pointer, evaluation stack та стан exception handling."
track: python
section: iterators-and-generators
level: middle
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

**Suspended generator зберігає локальні змінні, instruction pointer, evaluation stack та стан exception handling.**[^py314-library-stdtypes-iterator-types] Після завершення (return або вихід без yield) generator піднімає `StopIteration` і стає вичерпаним: усі наступні виклики `next()` знову підніматимуть `StopIteration`. Повторно запустити той самий generator неможливо.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
