---
id: py-coll-0020
title: "Що означає stability сортування Python і як використати її для multi-key sorting без custom comparator?"
description: "Stability означає, що елементи з однаковим key зберігають початковий відносний порядок; це дозволяє сортувати за кількома keys послідовно, від менш значущого до більш значущого."
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/sequences.md#L292-L321
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Stability означає, що елементи з однаковим key зберігають початковий відносний порядок; це дозволяє сортувати за кількома keys послідовно, від менш значущого до більш значущого.**[^py314-library-stdtypes] Наприклад, щоб сортувати за спаданням `grade` і зростанням `age`: спочатку `sorted(data, key=age)`, потім `sorted(result, key=grade, reverse=True)`. Stability гарантує, що порядок за `age` збережеться для однакових `grade`. Альтернатива для одного напрямку – tuple key: `key=itemgetter(grade, age)`.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
