---
id: py-itergen-0010
title: "Як значення `return` у subgenerator передається delegating generator через `yield from`?"
description: "return value у subgenerator встановлює StopIteration.value, а yield from витягує це значення як результат виразу."
track: python
section: iterators-and-generators
level: senior
type: mechanism
tags: [yield-from]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/iterator_and_generator.md#L270-L337
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`return value` у subgenerator встановлює `StopIteration.value`, а `yield from` витягує це значення як результат виразу.**[^py314-library-stdtypes-iterator-types] Коли subgenerator виконує `return value`, він піднімає `StopIteration` з атрибутом `value`, встановленим у `value`. Вираз `yield from` перехоплює цей виняток і повертає `value` як власний результат, який можна присвоїти змінній у delegating generator.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
