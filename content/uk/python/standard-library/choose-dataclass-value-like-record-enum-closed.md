---
id: py-stdlib-0016
title: "Коли обрати `dataclass` для value-like record, а коли `Enum` для закритого набору symbolic values?"
description: "dataclass автоматично генерує __init__, __repr__, __eq__ для класів із даними; Enum зв’язує скінченну кількість символічних імен з унікальними константами."
track: python
section: standard-library
level: middle
type: comparison
tags: [dataclass, enum]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-library-dataclasses
    title: "Python 3.14: Library/dataclasses"
    url: https://docs.python.org/3.14/library/dataclasses.html
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: @dataclass генерує __init__, __repr__ і __eq__; згенерований __eq__ порівнює поля по черзі для об’єктів одного типу; з 3.13 поля порівнюються окремо."
  - source_id: py314-library-dataclasses-dataclass
    title: "Python 3.14: Library/dataclasses, dataclass"
    url: https://docs.python.org/3.14/library/dataclasses.html#dataclasses.dataclass
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: правила створення __hash__ для dataclass залежно від параметрів eq і frozen."
  - source_id: py314-library-enum
    title: "Python 3.14: Library/enum"
    url: https://docs.python.org/3.14/library/enum.html#module-enum
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: enum – набір символічних імен, зв’язаних з унікальними значеннями; члени з однаковим значенням стають aliases; @unique забороняє aliases; ітерація дає канонічні члени в порядку оголошення."
---

## Short answer

**`dataclass` автоматично генерує `__init__`, `__repr__` і `__eq__` для класу з полями.**[^py314-library-dataclasses] `Enum` зв’язує символічні імена з константами: члени з однаковим значенням стають aliases, а `@unique` цього не дозволяє.[^py314-library-enum] `dataclass` підходить, коли потрібно згрупувати кілька полів у запис, наприклад `Point(x, y)`; з `frozen=True` (за типового `eq=True` і без власного `__hash__`) такий запис ще й хешується.[^py314-library-dataclasses-dataclass] `Enum` – коли набір значень відомий наперед і вичерпний, наприклад стани чи статуси; його члени ітерабельні в порядку оголошення.[^py314-library-enum]

## Detailed explanation

`@dataclass` читає анотації класу і генерує `__init__`, `__repr__` і `__eq__`. Згенерований `__eq__` порівнює поля по черзі й вимагає, щоб обидва об’єкти були одного типу. З Python 3.13 поля порівнюються окремо, а не через кортежі.[^py314-library-dataclasses] Саме так запис стає value-like: два окремі `Point(1, 2)` рівні між собою, бо рівні їхні поля.

Хешовність залежить від параметрів. За замовчуванням `eq=True` і `frozen=False`, тож `__hash__` дорівнює `None`, і такий запис не можна використати як ключ словника чи елемент множини. З `frozen=True` `__hash__` генерується, якщо `eq=True` (типово) і клас сам його не визначає; явний `__hash__` dataclass не змінює, а з `eq=False` лишається `__hash__` суперкласу.[^py314-library-dataclasses-dataclass]

Приклад (виконано на CPython 3.13 і 3.14):

```python
from dataclasses import dataclass
from enum import Enum, unique

@dataclass(frozen=True)
class Point:
    x: int
    y: int

@unique
class Status(Enum):
    OPEN = "open"
    CLOSED = "closed"

p = Point(1, 2)
print(p)                                  # Point(x=1, y=2)
print(p == Point(1, 2))                   # True
print({p: "ok"})                          # {Point(x=1, y=2): 'ok'}  frozen=True makes it hashable
print(list(Status))                       # [<Status.OPEN: 'open'>, <Status.CLOSED: 'closed'>]
print(Status("open") is Status.OPEN)      # True
print(Status.OPEN == "open")              # False: a plain Enum member is not equal to its value

@dataclass
class MutablePoint:
    x: int
    y: int

try:
    {MutablePoint(1, 2): "ok"}
except TypeError as error:
    print(type(error).__name__)           # TypeError (the message text differs between 3.13 and 3.14)
```

У прикладі `Point` з `frozen=True` працює як ключ словника, а `MutablePoint` без `frozen` дає `TypeError`. `Status("open")` повертає `Status.OPEN`, але `Status.OPEN == "open"` дає `False` (спостережено в CPython 3.13 і 3.14). `@unique` не дає двом іменам мати одне значення.[^py314-library-enum]

**Типові помилки:**
- використати `@dataclass` без `frozen=True` як ключ словника або елемент множини: `__hash__` дорівнює `None`, і це дає `TypeError`.[^py314-library-dataclasses-dataclass]
- написати `Enum` з двома іменами на одне значення без `@unique`: другий член стає aliasом і не з’являється в ітерації.[^py314-library-enum]
- порівнювати член `Enum` зі значенням (`Status.OPEN == "open"`) і очікувати `True`.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
