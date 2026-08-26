---
id: py-prac-0015
title: "Перемістіть numeric zeros в кінець list in place, зберігши order інших elements та O(1) extra space; `False` не вважайте нулем."
description: "Двох-показчиковий алгоритм: pos вказує на наступну позицію для non-zero, i сканує список; isinstance(item, bool) перевіряється перед item != 0, бо False == 0 в Python."
track: python
section: practical-coding
level: middle
type: coding
tags: []
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
execution:
  language: python
  standard: null
  toolchain:
    name: cpython
    version: "3.14.7"
  flags: []
anki:
  export: false
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/coding.md#L726-L760
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Task

TODO

## Constraints

TODO

## Short answer

**Двох-показчиковий алгоритм: `pos` вказує на наступну позицію для non-zero, `i` сканує список; `isinstance(item, bool)` перевіряється перед `item != 0`, бо `False == 0` в Python.** <span class="warn">Уникайте `lst.sort(key=lambda x: x == 0)` – це не stable для bool та не зберігає порядок non-zero елементів.</span>

```python
def move_zeros(lst):
    pos = 0
    for i in range(len(lst)):
        item = lst[i]
        if isinstance(item, bool) or item != 0:
            lst[pos], lst[i] = lst[i], lst[pos]
            pos += 1

a = [1, 0, 2, 0, 3, False, 0, 4]
move_zeros(a)  # [1, 2, 3, False, 4, 0, 0, 0]
```

## Detailed explanation

TODO

## Examples

TODO

## Solution

TODO

## Complexity

TODO

## Edge cases

TODO

## Tests

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
