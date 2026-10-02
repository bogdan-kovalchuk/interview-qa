---
id: py-prac-0021
title: "Спроєктуйте immutable value object з коректно узгодженими `__eq__` та `__hash__`, придатний для `dict` key."
description: "Використовуйте frozen dataclass зі slots та перевіреними integer fields."
track: python
section: practical-coding
level: senior
type: coding
tags: [eq, hash, dict]
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

Реалізуйте immutable через public API value object Point з integer fields x та y, узгодженими equality і hashing та використанням як dict key.

## Constraints

- Fields – built-in ints, крім bool.
- Звичайні assignment та deletion мають відхилятися; equality порівнює той самий class і обидва fields.
- Навмисний обхід через object.__setattr__ поза public API contract; frozen не є security boundary.

## Short answer

**Використовуйте frozen dataclass зі slots та перевіреними integer fields.** Він генерує equality та hashing із тих самих fields. Frozen блокує звичайні assignment і deletion, але не запобігає навмисній low-level mutation.

## Detailed explanation

За eq та frozen dataclass генерує hash, узгоджений із field equality. Integer fields уникають nested mutable state; type annotations не перевіряють constructor arguments, тому це робить __post_init__. Slots прибирає звичайний instance dictionary, але саме собою не забезпечує immutability. [^py313-dataclasses] [^py313-model]

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

Зберігаються два field references. Equality та hashing залежать від bit lengths integer fields; лише fixed-width integer model робить їх O(1). Dict operations мають expected constant time за числом entries, плюс key hashing та equality costs. [^py313-dataclasses] [^py313-model]

## Edge cases

Перевірте equal keys, нерівні coordinates, unrelated types, invalid coordinates, assignment, deletion та відсутність __dict__.

## Tests

Виконайте після блока Solution із встановленим pytest.

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

Поясніть equality/hash invariant без обіцянки collision freedom або absolute immutability.

### Red flags

Implementation пропускає зазначений boundary case або complexity claim не враховує allocated data.

### Level-up follow-up

Що зміниться, коли field mutable або subclass додає equality state?

## Sources

<!-- generated from frontmatter -->
