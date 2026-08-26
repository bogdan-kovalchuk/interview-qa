---
id: py-prac-0024
title: "Складіть tests для maximum-overlapping-intervals function: інтервали closed `[start, end]`, тому start і end в одну мить вважаються overlapping."
description: "Ключовий boundary – closed intervals: дотичні [1,5] і [5,10] дають overlap == 2 у точці 5."
track: python
section: practical-coding
level: middle
type: practical
tags: [start-end]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: py314-tutorial
    title: "Python 3.14: Tutorial"
    url: https://docs.python.org/3.14/tutorial/
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference
    title: "Python 3.14: Reference"
    url: https://docs.python.org/3.14/reference/
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-threading
    title: "Python 3.14: Library/threading"
    url: https://docs.python.org/3.14/library/threading.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-time-time-monotonic
    title: "Python 3.14: Library/time"
    url: https://docs.python.org/3.14/library/time.html#time.monotonic
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/coding.md#L585-L632
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Ключовий boundary – closed intervals: дотичні `[1,5]` і `[5,10]` дають overlap == 2 у точці 5.**[^py314-tutorial] Тести: дотик `[(1,5),(5,10)] -> 2`; повна вкладеність `[(1,10),(2,9),(3,8)] -> 3`; без перетину `[(1,3),(5,7)] -> 1`; порожній список -> 0; один інтервал -> 1; усі однакові `[(1,5)]*4 -> 4`; вироджений `[(3,3),(3,3)] -> 2`.

## Detailed explanation

TODO

## Environment

TODO

## Deliverable

TODO

## Acceptance criteria

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
