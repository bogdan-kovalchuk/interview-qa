---
id: py-coll-0011
title: "Як dict union operators `|` і `|=` вирішують конфлікти однакових keys та чим відрізняються за mutation?"
description: "Обидва оператори при дублікаті keys залишають значення з правого операнда; | повертає новий dict, а |= оновлює лівий in-place."
track: python
section: collections
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/set_and_dict.md#L118-L138
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Обидва оператори при дублікаті keys залишають значення з правого операнда; `|` повертає новий dict, а `|=` оновлює лівий in-place.**[^py314-library-stdtypes] `d1 | d2` створює новий словник, `d1` не змінюється. `d1 |= d2` еквівалентний `d1.update(d2)` – модифікує `d1` на місці. Порядок keys у результаті: спочатку keys з лівого операнда в їхньому порядку, потім нові keys з правого.

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
