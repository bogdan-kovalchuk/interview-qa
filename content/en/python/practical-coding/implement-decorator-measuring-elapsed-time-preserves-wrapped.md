---
id: py-prac-0017
title: "Implement a decorator for measuring elapsed time that preserves the wrapped callable's metadata, return value, and exception behaviour."
description: "Use wraps, read perf_counter before the call and record the difference in finally."
track: python
section: practical-coding
level: middle
type: coding
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  uk: 3
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

Implement `timed(func, *, clock=perf_counter)` for synchronous calls, preserving metadata, return values and exceptions. Store the most recent elapsed duration on the wrapper.

## Constraints

- The injected clock returns monotonic numeric readings and must not raise.
- Measure successful and failing calls. last_elapsed is None before a call and is shared diagnostic state, not a thread-local metric; async functions are out of scope.

## Short answer

**Use `wraps`, read `perf_counter` before the call and record the difference in finally.** Return the wrapped result directly. The finally block also records failed calls while allowing their exceptions to propagate.

## Detailed explanation

Only differences between clock readings represent durations. finally runs on both return and exception paths; it must not return or raise and mask the original outcome. An injected non-failing clock makes the tests deterministic. [^py313-functools] [^py313-time] [^py313-compound]

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

O(1) wrapper work and storage per call, excluding the wrapped function and clock costs. Overlapping calls share last_elapsed, so this attribute is not an attribution-safe concurrent recorder. [^py313-functools] [^py313-time] [^py313-compound]

## Edge cases

Test metadata, keyword arguments, result identity, exact fake-clock durations and exception identity.

## Tests

Run after the Solution block with pytest installed.

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

Use an injected clock instead of sleep-based timing assertions. Explain the synchronous and concurrency limits.

### Red flags

The implementation misses a stated boundary case or its complexity claim omits allocated data.

### Level-up follow-up

How would you record durations for concurrent calls independently?

## Sources

<!-- generated from frontmatter -->
