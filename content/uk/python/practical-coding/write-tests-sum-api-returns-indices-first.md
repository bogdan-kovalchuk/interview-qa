---
id: py-prac-0023
title: "Складіть tests для Two Sum API, який повертає indices першої пари в lexicographic order, не використовує element двічі і повертає `None` без solution."
description: "Tests перевіряють чотири властивості: сума пари дорівнює target, пара лексикографічно найменша, жоден індекс не використано двічі, None коли розв'язку немає."
track: python
section: practical-coding
level: middle
type: practical
tags: []
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/coding.md#L850-L880
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Tests перевіряють чотири властивості: сума пари дорівнює target, пара лексикографічно найменша, жоден індекс не використано двічі, `None` коли розв'язку немає.**[^py314-tutorial] Кейси: базовий `[2,7,11,15], target=9 -> (0,1)`; заборона повтору – `[3,2,4], target=6 -> (1,2)`, а не `(0,0)`; лексикографічна першість – за наявності кількох пар повертається найменша за `(i,j)`; `[1,2,3], target=100 -> None`; edge cases: порожній список, від'ємні числа, дублікати значень.

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
