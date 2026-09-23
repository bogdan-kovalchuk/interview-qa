---
id: py-itergen-0002
title: "Чому `iter(container)` зазвичай повертає новий iterator, а `iter(iterator)` має повертати той самий object?"
description: "container.__iter__() створює новий iterator з власним станом, тоді як iterator.__iter__() повертає self."
track: python
section: iterators-and-generators
level: middle
type: mechanism
tags: [iter-container, iter-iterator]
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

**`container.__iter__()` створює новий iterator з власним станом, тоді як `iterator.__iter__()` повертає `self`.**[^py314-library-stdtypes-iterator-types] Це потрібно, щоб iterator можна було використовувати в `for` та інших конструкціях, які викликають `iter()`. Саме тому повторний `for` по контейнеру працює (щоразу новий iterator), а повторна ітерація по тому ж iterator – ні: він уже вичерпаний.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
