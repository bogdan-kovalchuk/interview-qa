---
id: py-coll-0002
title: "Чому `range` може представляти дуже великий діапазон без зберігання всіх integers у пам’яті?"
description: "range зберігає лише три значення – start, stop, step – і обчислює елементи на вимогу, тому споживає O(1) пам'яті незалежно від діапазону."
track: python
section: collections
level: middle
type: mechanism
tags: [range]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/sequences.md#L406-L428
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`range` зберігає лише три значення – `start`, `stop`, `step` – і обчислює елементи на вимогу, тому споживає O(1) пам'яті незалежно від діапазону.**[^py314-library-stdtypes] `range(10**15)` і `range(10)` займають однаковий обсяг пам'яті. Операції `in` (арифметична перевірка) та індексація виконуються за O(1).

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
