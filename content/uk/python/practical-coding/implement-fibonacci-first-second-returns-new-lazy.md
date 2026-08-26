---
id: py-prac-0016
title: "Реалізуйте `fibonacci(n, first=0, second=1)`, що повертає новий lazy iterator для кожного виклику і видає рівно n values з O(1) state."
description: "Внутрішній generator зберігає a, b як O(1) state та range(n) для лічильника; кожен виклик fibonacci() створює новий generator object."
track: python
section: practical-coding
level: middle
type: coding
tags: [fibonacci-n-first-0-second-1]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/coding.md#L115-L131
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

**Внутрішній generator зберігає `a, b` як O(1) state та `range(n)` для лічильника; кожен виклик `fibonacci()` створює новий generator object.** Generator є lazy – значення обчислюються лише при ітерації. <span class="warn">Не використовуйте рекурсію без memoization – O(2^n) time complexity.</span>

```python
def fibonacci(n, first=0, second=1):
    def gen():
        a, b = first, second
        for _ in range(n):
            yield a
            a, b = b, a + b
    return gen()

list(fibonacci(8))  # [0, 1, 1, 2, 3, 5, 8, 13]
list(fibonacci(0))  # []
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
