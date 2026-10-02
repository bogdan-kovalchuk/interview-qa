---
id: py-prac-0014
title: "Реалізуйте streaming RLE encoder, який з iterable characters ліниво видає tuples `(character, positive_count)` з a constant number of auxiliary objects; empty input не видає нічого."
description: "Зберігайте поточний символ та count його run, видаючи результат при зміні символу."
track: python
section: practical-coding
level: middle
type: coding
tags: [character-positive-count]
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
- source_id: py313-itertools
  title: 'Python 3.13: Adjacent groups'
  url: https://docs.python.org/3.13/library/itertools.html#itertools.groupby
  accessed: '2026-10-04'
  kind: official
  version: '3.13'
  applicability: API semantics and language guarantees used by this solution.
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
---

## Task

Реалізуйте `rle_encode(iterable)`, що ліниво видає `(character, positive_count)` для consecutive однакових символів. Порожній input нічого не видає.

## Constraints

- Input – iterable односимвольних strings.
- Не сортуйте й не матеріалізуйте його.
- Зберігайте сталу кількість state variables; потрібен lookahead не більш ніж на один символ.
- Нескінченний однаковий run не може видати завершений count.

## Short answer

**Зберігайте поточний символ та count його run, видаючи результат при зміні символу.** Видайте останній run після exhaustion і обробіть empty input до ініціалізації run. Sorting змінює структуру runs і не має використовуватися.

## Detailed explanation

Run завершується лише при читанні наступного іншого символу або exhaustion джерела. Generator зупиняється після yield, зберігаючи boundary character як lookahead. groupby також групує adjacent runs; sorting для RLE не потрібний. [^py313-itertools] [^py313-yield] [^py313-types]

## Examples

```python
assert list(rle_encode("aab")) == [("a", 2), ("b", 1)]
```

## Solution

```python
def rle_encode(iterable):
    iterator = iter(iterable)
    try:
        current = next(iterator)
    except StopIteration:
        return
    count = 1
    for character in iterator:
        if character == current:
            count += 1
        else:
            yield current, count
            current, count = character, 1
    yield current, count
```

## Complexity

O(n) input steps і стала кількість допоміжних objects для n символів. Count є arbitrary-precision integer та потребує O(log r) bits для run довжини r; стала кількість objects не означає сталу кількість байтів. [^py313-itertools] [^py313-yield] [^py313-types]

## Edge cases

Перевірте empty input, singleton, alternating characters, one-shot input, non-adjacent повтори та bounded lookahead.

## Tests

Виконайте після блока Solution із встановленим pytest.

```python
import pytest

assert list(rle_encode("")) == []
assert list(rle_encode("x")) == [("x", 1)]
assert list(rle_encode("aaabbc")) == [("a", 3), ("b", 2), ("c", 1)]
assert list(rle_encode(iter("aba"))) == [("a", 1), ("b", 1), ("a", 1)]
seen = []
def source():
    for ch in "aabc":
        seen.append(ch)
        yield ch
encoded = rle_encode(source())
assert seen == []
assert next(encoded) == ("a", 2)
assert seen == ["a", "a", "b"]
assert list(encoded) == [("b", 1), ("c", 1)]
```

## Evaluation guide

### Expected signals

Покажіть, що generator нічого не читає під час створення й не зчитує все джерело до першого результату.

### Red flags

Implementation пропускає зазначений boundary case або complexity claim не враховує allocated data.

### Level-up follow-up

Чому нескінченний однаковий run ніколи не видасть final count?

## Sources

<!-- generated from frontmatter -->
