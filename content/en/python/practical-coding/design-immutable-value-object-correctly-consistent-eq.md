---
id: py-prac-0021
title: "Design an immutable value object with correctly consistent `__eq__` and `__hash__`, suitable as a `dict` key."
description: "Use a frozen dataclass with slots and validated integer fields."
track: python
section: practical-coding
level: senior
type: coding
tags: [eq, hash, dict]
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
- source_id: py313-dataclasses
  title: 'Python 3.13: Frozen dataclasses and hash generation'
  url: https://docs.python.org/3.13/library/dataclasses.html
  accessed: '2026-10-04'
  kind: official
  version: '3.13'
  applicability: API semantics and language guarantees used by this solution.
- source_id: py313-model
  title: 'Python 3.13: Data model: hashing and context managers'
  url: https://docs.python.org/3.13/reference/datamodel.html
  accessed: '2026-10-04'
  kind: official
  version: '3.13'
  applicability: API semantics and language guarantees used by this solution.
---

## Task

Implement an immutable-by-public-API Point value object with integer x and y fields, consistent equality and hashing, and use as a dict key.

## Constraints

- Fields are built-in ints excluding bool.
- Ordinary assignment and deletion must fail; equality compares the same class and both fields.
- Deliberate object.__setattr__ bypasses are outside the public API contract; frozen does not provide a security boundary.

## Short answer

**Use a frozen dataclass with slots and validated integer fields.** It generates equality and hashing from the same fields. Frozen blocks ordinary assignment and deletion, but does not prevent deliberate low-level mutation.

## Detailed explanation

With eq and frozen enabled, dataclass generates a hash consistent with field equality. Integer fields avoid nested mutable state; type annotations alone do not validate constructor arguments, so __post_init__ does. slots removes the usual instance dictionary but is not itself immutability. [^py313-dataclasses] [^py313-model]

## Examples

```python
assert {Point(1, 2): "value"}[Point(1, 2)] == "value"
```

## Solution

```python
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class Point:
    x: int
    y: int

    def __post_init__(self):
        if type(self.x) is not int or type(self.y) is not int:
            raise TypeError("coordinates must be integers")
```

## Complexity

There are two stored field references. Equality and hashing costs depend on the bit lengths of the integer fields; only a fixed-width integer model makes them O(1). Dict operations are expected constant-time in the number of entries, plus key hashing and equality costs. [^py313-dataclasses] [^py313-model]

## Edge cases

Test equal keys, unequal coordinates, unrelated types, invalid coordinates, assignment, deletion and absence of __dict__.

## Tests

Run after the Solution block with pytest installed.

```python
import pytest

from dataclasses import FrozenInstanceError
a, b = Point(1, 2), Point(1, 2)
assert a == b and hash(a) == hash(b)
assert {a: "found"}[b] == "found"
assert a != Point(2, 1) and a != (1, 2)
assert a.__eq__((1, 2)) is NotImplemented
assert not hasattr(a, "__dict__")
with pytest.raises(FrozenInstanceError):
    a.x = 3
with pytest.raises(FrozenInstanceError):
    del a.y
assert a == b
for invalid in (True, [], 1.0):
    with pytest.raises(TypeError):
        Point(invalid, 2)
```

## Evaluation guide

### Expected signals

Explain the equality/hash invariant without claiming collision freedom or absolute immutability.

### Red flags

The implementation misses a stated boundary case or its complexity claim omits allocated data.

### Level-up follow-up

What changes when a field is mutable or a subclass adds equality state?

## Sources

<!-- generated from frontmatter -->
