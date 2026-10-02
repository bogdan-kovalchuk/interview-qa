---
id: py-prac-0017
title: "Реалізуйте decorator для вимірювання elapsed time, який зберігає metadata, return value та exception behavior wrapped callable."
description: "Використовуйте wraps, читайте perf_counter перед викликом і записуйте різницю у finally."
track: python
section: practical-coding
level: middle
type: coding
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  en: 3
execution:
  language: python
  standard: null
  toolchain:
    name: cpython
    version: "3.13.15"
  flags: []
anki:
  export: true
sources:
- source_id: py313-functools
  title: 'Python 3.13: Wrapper metadata'
  url: https://docs.python.org/3.13/library/functools.html#functools.wraps
  accessed: '2026-10-04'
  kind: official
  version: '3.13'
  applicability: API semantics and language guarantees used by this solution.
- source_id: py313-time
  title: 'Python 3.13: Performance counter'
  url: https://docs.python.org/3.13/library/time.html#time.perf_counter
  accessed: '2026-10-04'
  kind: official
  version: '3.13'
  applicability: API semantics and language guarantees used by this solution.
- source_id: py313-compound
  title: 'Python 3.13: Compound statements: with and finally'
  url: https://docs.python.org/3.13/reference/compound_stmts.html
  accessed: '2026-10-04'
  kind: official
  version: '3.13'
  applicability: API semantics and language guarantees used by this solution.
---

## Task

Реалізуйте `timed(func, *, clock=perf_counter)` для synchronous calls, зберігши metadata, return values та exceptions. Зберігайте останню elapsed duration на wrapper.

## Constraints

- Injected clock повертає monotonic numeric readings і не має піднімати exceptions.
- Вимірюйте successful та failing calls. last_elapsed – None до виклику і є shared diagnostic state, а не thread-local metric; async functions поза scope.

## Short answer

**Використовуйте `wraps`, читайте `perf_counter` перед викликом і записуйте різницю у finally.** Повертайте wrapped result безпосередньо. Finally також записує failed calls, дозволяючи їхнім exceptions поширюватися.

## Detailed explanation

Лише різниці clock readings представляють durations. Finally виконується і для return, і для exception paths; він не має return або raise, що приховають початковий результат. Injected non-failing clock робить tests deterministic. [^py313-functools] [^py313-time] [^py313-compound]

## Examples

```python
assert timed(lambda x: x + 1)(2) == 3
```

## Solution

```python
from functools import wraps
from time import perf_counter

def timed(func, *, clock=perf_counter):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = clock()
        try:
            return func(*args, **kwargs)
        finally:
            wrapper.last_elapsed = clock() - start
    wrapper.last_elapsed = None
    return wrapper
```

## Complexity

O(1) роботи й пам’яті wrapper на виклик, без вартості wrapped function та clock. Overlapping calls поділяють last_elapsed, тому цей attribute не є recorder з коректною attribution для concurrency. [^py313-functools] [^py313-time] [^py313-compound]

## Edge cases

Перевірте metadata, keyword arguments, result identity, точні fake-clock durations та exception identity.

## Tests

Виконайте після блока Solution із встановленим pytest.

```python
import pytest

ticks = iter([10.0, 10.25, 20.0, 20.75])
result = object()
def operation(*, fail=False):
    """A timed operation."""
    if fail:
        raise failure
    return result
failure = ValueError("failed")
wrapped = timed(operation, clock=lambda: next(ticks))
assert wrapped.last_elapsed is None
assert wrapped() is result and wrapped.last_elapsed == 0.25
assert wrapped.__name__ == operation.__name__
assert wrapped.__doc__ == operation.__doc__ and wrapped.__wrapped__ is operation
with pytest.raises(ValueError) as caught:
    wrapped(fail=True)
assert caught.value is failure and wrapped.last_elapsed == 0.75
```

## Evaluation guide

### Expected signals

Використовуйте injected clock замість sleep-based timing assertions. Поясніть synchronous та concurrency limits.

### Red flags

Implementation пропускає зазначений boundary case або complexity claim не враховує allocated data.

### Level-up follow-up

Як записувати durations concurrent calls незалежно?

## Sources

<!-- generated from frontmatter -->
