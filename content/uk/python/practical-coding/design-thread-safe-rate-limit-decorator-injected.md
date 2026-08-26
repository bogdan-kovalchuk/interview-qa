---
id: py-prac-0018
title: "Спроєктуйте thread-safe rate-limit decorator з injected monotonic clock: до X викликів за rolling T seconds, перевищення викликає явний exception."
description: "threading.Lock захищає timestamps list, injected clock (default time.monotonic) дозволяє тестування, rolling window реалізується видаленням expired timestamps з початку list."
track: python
section: practical-coding
level: senior
type: practical
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/coding.md#L761-L799
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`threading.Lock` захищає `timestamps` list, injected `clock` (default `time.monotonic`) дозволяє тестування, rolling window реалізується видаленням expired timestamps з початку list.**[^py314-tutorial] <span class="warn">`time.time()` не підходить – не monotonic; `time.monotonic()` гарантує відсутність backward jumps. Race condition між `len(timestamps)` check та `timestamps.append()` вимагає lock.</span>

```python
import threading
import time
import functools

class RateLimitExceeded(Exception):
    pass

def rate_limit(max_calls, period, clock=None):
    if clock is None:
        clock = time.monotonic
    def decorator(func):
        lock = threading.Lock()
        timestamps = []
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            now = clock()
            with lock:
                cutoff = now - period
                while timestamps and timestamps[0] <= cutoff:
                    timestamps.pop(0)
                if len(timestamps) >= max_calls:
                    raise RateLimitExceeded(
                        f"Rate limit: {max_calls} calls per {period}s"
                    )
                timestamps.append(now)
            return func(*args, **kwargs)
        return wrapper
    return decorator
```

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
