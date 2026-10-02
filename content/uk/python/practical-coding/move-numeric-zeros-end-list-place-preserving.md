---
id: py-prac-0015
title: "Перемістіть numeric zeros в кінець list in place, зберігши order інших elements та O(1) extra space; `False` не вважайте нулем."
description: "Підтримуйте наступну non-zero position та міняйте з нею кожен збережений element."
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
- source_id: py313-types
  title: 'Python 3.13: Built-in types'
  url: https://docs.python.org/3.13/library/stdtypes.html
  accessed: '2026-10-04'
  kind: official
  version: '3.13'
  applicability: API semantics and language guarantees used by this solution.
- source_id: py313-builtins
  title: 'Python 3.13: Built-in functions'
  url: https://docs.python.org/3.13/library/functions.html
  accessed: '2026-10-04'
  kind: official
  version: '3.13'
  applicability: API semantics and language guarantees used by this solution.
---

## Task

Реалізуйте `move_zeros(values)` in place: перемістіть numeric zeros у кінець, зберігши relative order решти elements, включно з False.

## Constraints

- Input – list built-in int, float, complex та bool.
- Нуль – non-bool value, рівний 0.
- Використовуйте O(1) допоміжних references, повертайте None та зберігайте також zero objects.

## Short answer

**Підтримуйте наступну non-zero position та міняйте з нею кожен збережений element.** Обробляйте bool окремо, бо False порівнюється рівним нулю. Це зберігає non-zero order та використовує сталу кількість references.

## Detailed explanation

Перед кожним кроком prefix містить усі вже знайдені збережені elements у вихідному порядку. Між prefix та scan position залишаються лише zeros, тому swap не порушує попередні retained elements. Python sorting є stable, проте sorting зайвий і не відповідає вимозі constant auxiliary space. [^py313-types] [^py313-builtins]

## Examples

```python
values = [0, 1, False, 0, 2]
move_zeros(values)
assert values[:3] == [1, False, 2]
assert values[1] is False
```

## Solution

```python
def move_zeros(values):
    position = 0
    for index, item in enumerate(values):
        if isinstance(item, bool) or item != 0:
            values[position], values[index] = values[index], values[position]
            position += 1
```

## Complexity

O(n) comparisons та swaps для n elements, з O(1) допоміжних references. Input list і його objects використовуються повторно; гарантується лише relative order non-zero elements. [^py313-types] [^py313-builtins]

## Edge cases

Перевірте False, True, 0.0, complex zero, empty input, лише zeros та вже впорядкований list.

## Tests

Виконайте після блока Solution із встановленим pytest.

```python
import pytest

values = [0, False, 2, 0.0, True, 3, 0j]
identity = id(values)
assert move_zeros(values) is None and id(values) == identity
assert values[:4] == [False, 2, True, 3]
assert values[0] is False and values[2] is True
assert all(not isinstance(x, bool) and x == 0 for x in values[4:])
for data in ([], [0, 0], [1, 2], [1, 0]):
    before = sorted(map(id, data))
    move_zeros(data)
    assert sorted(map(id, data)) == before
```

## Evaluation guide

### Expected signals

У тестах використовуйте identity checks для bool, бо list equality не відрізняє False від 0.

### Red flags

Implementation пропускає зазначений boundary case або complexity claim не враховує allocated data.

### Level-up follow-up

Як вимога stable zero order змінить algorithm?

## Sources

<!-- generated from frontmatter -->
