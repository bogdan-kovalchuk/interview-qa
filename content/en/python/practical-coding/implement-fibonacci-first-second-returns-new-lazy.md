---
id: py-prac-0016
title: "Implement `fibonacci(n, first=0, second=1)` that returns a new lazy iterator on every call and yields exactly n values with a constant number of state variables."
description: "Return a new inner generator that retains the current and next terms."
track: python
section: practical-coding
level: middle
type: coding
tags: [fibonacci-n-first-0-second-1]
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
- source_id: py313-yield
  title: 'Python 3.13: Yield expressions'
  url: https://docs.python.org/3.13/reference/expressions.html#yield-expressions
  accessed: '2026-10-04'
  kind: official
  version: '3.13'
  applicability: API semantics and language guarantees used by this solution.
- source_id: py313-types
  title: 'Python 3.13: Built-in types'
  url: https://docs.python.org/3.13/library/stdtypes.html
  accessed: '2026-10-04'
  kind: official
  version: '3.13'
  applicability: API semantics and language guarantees used by this solution.
- source_id: py313-long-add
  title: 'Python 3.13: CPython 3.13.15 integer addition implementation'
  url: https://github.com/python/cpython/blob/v3.13.15/Objects/longobject.c
  accessed: '2026-10-04'
  kind: official
  version: '3.13'
  applicability: Pinned implementation supporting the integer-addition bit-cost analysis.
---

## Task

Implement `fibonacci(n, first=0, second=1)` returning a fresh lazy iterator of exactly n terms. Retain only a constant number of sequence values.

## Constraints

- n is a non-negative int excluding bool; first and second are integers excluding bool.
- Validate at function call time.
- Terms use Python arbitrary-precision integers, so constant state variables do not imply constant bytes.

## Short answer

**Return a new inner generator that retains the current and next terms.** Yield the current term and advance the pair by addition. Validate before returning the iterator so invalid arguments fail immediately.

## Detailed explanation

Each iterator owns its local pair and advances independently. The outer function performs validation immediately, while generator iteration performs the additions. Integer values grow, so the state has constant cardinality but increasing byte size. [^py313-yield] [^py313-types] [^py313-long-add]

## Examples

```python
assert list(fibonacci(5)) == [0, 1, 1, 2, 3]
```

## Solution

```python
def fibonacci(n, first=0, second=1):
    if any(type(value) is not int for value in (n, first, second)):
        raise TypeError("arguments must be integers")
    if n < 0:
        raise ValueError("n must be non-negative")
    def generate():
        a, b = first, second
        for _ in range(n):
            yield a
            a, b = b, a + b
    return generate()
```

## Complexity

There are O(n) iterations and O(1) stored integer objects. With default seeds, term bit lengths grow linearly with the index; retained integer storage is O(n) bits and summing the addition costs gives O(n^2) bit work for CPython-style linear-time addition. [^py313-yield] [^py313-types] [^py313-long-add]

## Edge cases

Test n=0 and n=1, custom seeds, independent iterators, exhaustion and immediate rejection of negative n.

## Tests

Run after the Solution block with pytest installed.

```python
import pytest

assert list(fibonacci(8)) == [0, 1, 1, 2, 3, 5, 8, 13]
assert list(fibonacci(0)) == []
assert list(fibonacci(1, 4, 7)) == [4]
assert list(fibonacci(4, 2, 3)) == [2, 3, 5, 8]
a, b = fibonacci(3), fibonacci(3)
assert a is not b and iter(a) is a
assert next(a) == 0 and next(a) == 1 and next(b) == 0
assert list(a) == [1] and list(a) == []
with pytest.raises(ValueError):
    fibonacci(-1)
with pytest.raises(TypeError):
    fibonacci(True)
```

## Evaluation guide

### Expected signals

Explain laziness and independence. Do not claim constant byte memory for unbounded Python integers.

### Red flags

The implementation misses a stated boundary case or its complexity claim omits allocated data.

### Level-up follow-up

How would you compute a single distant term without yielding every prefix term?

## Sources

<!-- generated from frontmatter -->
