---
id: py-prac-0016
title: "Реалізуйте `fibonacci(n, first=0, second=1)`, що повертає новий lazy iterator для кожного виклику і видає рівно n values з сталою кількістю state variables."
description: "Повертайте новий inner generator, що зберігає поточний та наступний terms."
track: python
section: practical-coding
level: middle
type: coding
tags: [fibonacci-n-first-0-second-1]
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

Реалізуйте `fibonacci(n, first=0, second=1)`, що повертає новий lazy iterator рівно n terms. Зберігайте лише сталу кількість sequence values.

## Constraints

- n – невід’ємний int, крім bool; first та second – integers, крім bool.
- Перевіряйте під час function call.
- Terms використовують Python arbitrary-precision integers, тому сталі state variables не означають сталі байти.

## Short answer

**Повертайте новий inner generator, що зберігає поточний та наступний terms.** Видавайте поточний term і оновлюйте pair через addition. Перевіряйте перед поверненням iterator, щоб хибні arguments відхилялися негайно.

## Detailed explanation

Кожен iterator має власну local pair та просувається незалежно. Outer function перевіряє arguments негайно, а additions виконує generator iteration. Integer values зростають, тому state має сталу кількість елементів, але більший byte size. [^py313-yield] [^py313-types] [^py313-long-add]

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

Виконується O(n) iterations і зберігається O(1) integer objects. За default seeds bit lengths terms зростають лінійно з index; пам’ять integers – O(n) bits, а сума addition costs дає O(n^2) bit work для CPython-style linear-time addition. [^py313-yield] [^py313-types] [^py313-long-add]

## Edge cases

Перевірте n=0 та n=1, custom seeds, незалежні iterators, exhaustion та негайне відхилення negative n.

## Tests

Виконайте після блока Solution із встановленим pytest.

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

Поясніть laziness та незалежність. Не стверджуйте constant byte memory для unbounded Python integers.

### Red flags

Implementation пропускає зазначений boundary case або complexity claim не враховує allocated data.

### Level-up follow-up

Як обчислити один віддалений term без видавання всіх prefix terms?

## Sources

<!-- generated from frontmatter -->
