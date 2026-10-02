---
id: py-prac-0008
title: "Реалізуйте суму integers у довільно вкладених lists: `bool` відхиляти, інші types мають викликати `TypeError`, а cycle у lists – `ValueError`."
description: "Використовуйте явний stack ітераторів lists та відстежуйте identities активних lists."
track: python
section: practical-coding
level: middle
type: coding
tags: [bool, typeerror, valueerror]
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

Реалізуйте `nested_sum(data)` для довільно глибоких acyclic вкладених lists із integers. Відхиляйте bool та інші типи через TypeError, а цикли lists – через ValueError.

## Constraints

- Корінь має бути list.
- Shared sublist враховується для кожного входження й не є циклом.
- Використовуйте iterative traversal без обмежень Python recursion; int subclasses, крім bool, дозволені.

## Short answer

**Використовуйте явний stack ітераторів lists та відстежуйте identities активних lists.** Відхиляйте bool до прийняття int. Видаляйте identity після виходу зі списку, щоб shared sublists залишалися дозволеними.

## Detailed explanation

Цикл замикають лише ancestors поточного шляху. Глобальна visited set помилково відхиляла б повторні references; active set відповідає входу й виходу. Ітератори обмежують пам’ять глибиною вкладення, а не шириною lists. [^py313-types] [^py313-builtins]

## Examples

```python
assert nested_sum([1, [2, 3]]) == 6
```

## Solution

```python
def nested_sum(data):
    if not isinstance(data, list):
        raise TypeError("root must be list")
    active = {id(data)}
    stack = [(id(data), iter(data))]
    total = 0
    while stack:
        identity, iterator = stack[-1]
        try:
            item = next(iterator)
        except StopIteration:
            active.remove(identity)
            stack.pop()
            continue
        if isinstance(item, bool):
            raise TypeError("bool is not allowed")
        if isinstance(item, int):
            total += item
        elif isinstance(item, list):
            identity = id(item)
            if identity in active:
                raise ValueError("cycle detected")
            active.add(identity)
            stack.append((identity, iter(item)))
        else:
            raise TypeError("unsupported leaf")
    return total
```

## Complexity

O(v) операцій обходу й O(d) допоміжних references для v відвіданих входжень та максимальної глибини d за expected constant-time set operations. Вартість big-integer addition і байти accumulator додаються; shared subtrees обходяться повторно. [^py313-types] [^py313-builtins]

## Edge cases

Перевірте self-cycles, indirect cycles, повторні shared lists, хибні leaves та глибину понад recursion limit.

## Tests

Виконайте після блока Solution із встановленим pytest.

```python
import pytest

assert nested_sum([]) == 0
assert nested_sum([1, [2, [-3]], []]) == 0
shared = [2, 3]
assert nested_sum([shared, shared]) == 10
cycle = []
cycle.append(cycle)
with pytest.raises(ValueError):
    nested_sum(cycle)
a, b = [], []
a.append(b)
b.append(a)
with pytest.raises(ValueError):
    nested_sum(a)
for invalid in (True, 1.0, "1", (1,), None):
    with pytest.raises(TypeError):
        nested_sum([invalid])
with pytest.raises(TypeError):
    nested_sum(1)
deep = [7]
for _ in range(2000):
    deep = [deep]
assert nested_sum(deep) == 7
```

## Evaluation guide

### Expected signals

Відрізняйте active ancestor від раніше відвіданого list. Не реалізуйте довільну глибину recursive calls.

### Red flags

Implementation пропускає зазначений boundary case або complexity claim не враховує allocated data.

### Level-up follow-up

Як обмежити роботу для input graphs із великою кількістю shared references?

## Sources

<!-- generated from frontmatter -->
