---
id: py-itergen-0016
title: "Коли generator expression кращий за list comprehension, а коли повторне використання або indexing робить list доречнішим?"
description: "Generator expression кращий для одноразового споживання великих або нескінченних послідовностей, бо не матеріалізує всі елементи в пам'яті."
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/iterator_and_generator.md#L430-L435
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Generator expression кращий для одноразового споживання великих або нескінченних послідовностей, бо не матеріалізує всі елементи в пам'яті.**[^py314-library-stdtypes-iterator-types] List comprehension доречніший, коли потрібні багаторазова ітерація, indexing (`lst[i]`), `len()`, slicing або збереження проміжного результату. Trade-off: generator економить пам'ять (`O(1)` замість `O(n)`), але програє у швидкості доступу та не підтримує повторне читання.

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
