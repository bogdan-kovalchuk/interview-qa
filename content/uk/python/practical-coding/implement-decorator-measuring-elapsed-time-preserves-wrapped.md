---
id: py-prac-0017
title: "Реалізуйте decorator для вимірювання elapsed time, який зберігає metadata, return value та exception behavior wrapped callable."
description: "functools.wraps копіює metadata (__name__, __doc__, __wrapped__), time.perf_counter() для high-resolution elapsed time, return value передається через return result, exception propagation гарантується відсутністю..."
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/coding.md#L198-L221
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

**`functools.wraps` копіює metadata (`__name__`, `__doc__`, `__wrapped__`), `time.perf_counter()` для high-resolution elapsed time, return value передається через `return result`, exception propagation гарантується відсутністю `try/except` що ловить помилки.** Тут <span class="warn">`time.time()` має нижчу точність та чутливий до system clock changes; `time.perf_counter()` є monotonic та має найвищу доступну точність.</span>

```python
import time
import functools

def timed(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        try:
            result = func(*args, **kwargs)
            return result
        finally:
            elapsed = time.perf_counter() - start
            wrapper.last_elapsed = elapsed
    wrapper.last_elapsed = None
    return wrapper

@timed
def slow_add(a, b):
    time.sleep(0.01)
    return a + b

slow_add(1, 2)  # 3
slow_add.__name__  # 'slow_add'
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
