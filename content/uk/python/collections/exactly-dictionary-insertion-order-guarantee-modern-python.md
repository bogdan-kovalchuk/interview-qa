---
id: py-coll-0006
title: "Що саме гарантує insertion order словника в сучасному Python і чого ця гарантія не говорить про внутрішню hash table?"
description: "Починаючи з Python 3.7, dict зберігає елементи в порядку вставки – це гарантія мови, а не деталь реалізації."
track: python
section: collections
level: middle
type: mechanism
tags: []
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
applies_to:
  - product: "CPython"
    version: "3.14"
anki:
  export: true
sources:
  - source_id: py314-library-stdtypes
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-collections
    title: "Python 3.14: Library/collections"
    url: https://docs.python.org/3.14/library/collections.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-howto-sorting
    title: "Python 3.14: Howto/sorting"
    url: https://docs.python.org/3.14/howto/sorting.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/set_and_dict.md#L293-L387
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Починаючи з Python 3.7, `dict` зберігає елементи в порядку вставки – це гарантія мови, а не деталь реалізації.**[^py314-library-stdtypes] Гарантія стосується порядку ітерації (`keys()`, `values()`, `items()`), але не розкриває структуру hash table. У CPython це реалізовано через компактну таблицю з масивом індексів і масивом записів; інші реалізації Python можуть досягти того ж порядку іншим шляхом.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
