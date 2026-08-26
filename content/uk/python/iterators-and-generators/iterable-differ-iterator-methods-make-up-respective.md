---
id: py-itergen-0001
title: "Чим iterable відрізняється від iterator і які methods утворюють їхні основні protocols?"
description: "Iterable реалізує __iter__(), який повертає iterator; iterator реалізує __iter__() (повертає сам об’єкт) та __next__()."
track: python
section: iterators-and-generators
level: middle
type: comparison
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
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/iterator_and_generator.md#L19-L104
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Iterable реалізує `__iter__()`, який повертає iterator; iterator реалізує `__iter__()` (повертає сам об’єкт) та `__next__()`.**[^py314-library-stdtypes-iterator-types] Iterable – це колекція, з якої можна отримати iterator (наприклад, `list`, `tuple`, `str`). Iterator зберігає стан ітерації та повертає елементи по одному через `__next__()`, а коли елементи вичерпано – піднімає `StopIteration`. Кожен iterator є iterable (бо має `__iter__`), але не навпаки.

## Detailed explanation

TODO

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
