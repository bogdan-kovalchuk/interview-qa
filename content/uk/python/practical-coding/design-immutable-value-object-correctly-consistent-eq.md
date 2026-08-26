---
id: py-prac-0021
title: "Спроєктуйте immutable value object з коректно узгодженими `__eq__` та `__hash__`, придатний для `dict` key."
description: "__slots__ запобігає створенню __dict__, __setattr__ raise AttributeError для immutability, __eq__ порівнює поля, __hash__ повертає hash(tuple_of_fields) – гарантує a == b -> hash(a) == hash(b)."
track: python
section: practical-coding
level: senior
type: coding
tags: [eq, hash, dict]
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
  export: false
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/coding.md#L422-L452
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Task

TODO

## Constraints

TODO

## Short answer

**`__slots__` запобігає створенню `__dict__`, `__setattr__` raise `AttributeError` для immutability, `__eq__` порівнює поля, `__hash__` повертає `hash(tuple_of_fields)` – гарантує `a == b` -> `hash(a) == hash(b)`.** <span class="warn">Якщо `__eq__` перевизначено без `__hash__`, Python автоматично встановлює `__hash__ = None` – об'єкт стане unhashable.</span>

```python
class Point:
    __slots__ = ('_x', '_y')

    def __init__(self, x, y):
        object.__setattr__(self, '_x', x)
        object.__setattr__(self, '_y', y)

    @property
    def x(self):
        return self._x

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self._x == other._x and self._y == other._y

    def __hash__(self):
        return hash((self._x, self._y))

    def __setattr__(self, name, value):
        raise AttributeError("Point is immutable")

p1 = Point(1, 2)
p2 = Point(1, 2)
p1 == p2  # True
hash(p1) == hash(p2)  # True
d = {p1: "a"}
d[p2]  # "a"
```

## Detailed explanation

TODO

## Examples

TODO

## Solution

TODO

## Complexity

TODO

## Edge cases

TODO

## Tests

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
