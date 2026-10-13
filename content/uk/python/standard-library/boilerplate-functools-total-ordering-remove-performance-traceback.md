---
id: py-stdlib-0008
title: "Який boilerplate усуває `functools.total_ordering` і які performance та traceback trade-offs варто врахувати?"
description: "@total_ordering доповнює відсутні методи порівняння (__lt__, __le__, __gt__, __ge__) з одного визначеного методу порядку; бажано також визначити __eq__."
track: python
section: standard-library
level: senior
type: practical
tags: [functools-total-ordering]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-library-functools-total-ordering
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html#functools.total_ordering
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14, розділ total_ordering: які методи клас має визначити, рекомендація __eq__, повільніше виконання і складніші stack traces, порада реалізувати всі методи явно, неперевизначення успадкованих методів."
---

## Short answer

**`@total_ordering` доповнює відсутні методи порівняння (`__lt__`, `__le__`, `__gt__`, `__ge__`) з одного визначеного методу порядку; клас має визначити хоча б один з них і бажано `__eq__`.**[^py314-library-functools-total-ordering] Trade-off: похідні методи повільніші й дають складніші traceback. Якщо benchmark показує, що порівняння є вузьким місцем, краще реалізувати всі методи явно.[^py314-library-functools-total-ordering]

## Detailed explanation

`@total_ordering` – це class decorator, який доповнює решту методів порівняння з одного визначеного методу порядку. Документація вимагає, щоб клас визначав хоча б один з `__lt__`, `__le__`, `__gt__`, `__ge__`, і радить мати `__eq__`.[^py314-library-functools-total-ordering] Декоратор не перевизначає методи, які вже є в класі або його суперкласах, навіть абстрактні.[^py314-library-functools-total-ordering] У CPython клас без жодного методу порядку призводить до `ValueError`.

Клас нижче визначає лише `__eq__` і `__lt__`; решту операторів додає декоратор:

```python
import functools

@functools.total_ordering
class Version:
    def __init__(self, major, minor):
        self.major = major
        self.minor = minor

    def __eq__(self, other):
        return (self.major, self.minor) == (other.major, other.minor)

    def __lt__(self, other):
        return (self.major, self.minor) < (other.major, other.minor)

print(Version(1, 2) <= Version(1, 3))  # True, __le__ is derived from __lt__ and __eq__
print(Version(2, 0) > Version(1, 9))   # True, __gt__ is derived too
```

Похідні методи – це звичайні функції з `functools.py`. У CPython тіло похідного `__gt__`, яке генерує `total_ordering` (функція `_gt_from_lt`), обчислює `not (a < b) and a != b`: спочатку викликається `__lt__`, а `__eq__` (через `!=`) викликається, лише якщо `__lt__` повернув `False`. Тож `Version(2, 0) > Version(1, 9)` викликає `__lt__` і `__eq__`, тоді як явний `__gt__` був би одним викликом.

Ціна така: кожне похідне порівняння – це додатковий Python-рівневий виклик. Якщо `__lt__` кидає виключення під час `>`, у traceback між оператором і вашим кодом з’являється кадр `_gt_from_lt` з `functools.py`. Документація називає це повільнішим виконанням і складнішими stack traces для похідних методів, а при вузькому місці радить реалізувати всі шість методів явно.[^py314-library-functools-total-ordering] Назва кадру однакова на CPython 3.13 і 3.14.

**Типові помилки:**
- вважати декоратор безкоштовним: похідні методи повільніші й ускладнюють налагодження;
- не визначити `__eq__`: тоді `==` порівнює ідентичність, і для класу лише з `__lt__` вираз `NoEq(2) <= NoEq(2)` дає `False`;
- очікувати, що декоратор замінить оператор, який уже є в базовому класі: він його не чіпає.

## Environment

TODO

## Deliverable

TODO

## Acceptance criteria

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
