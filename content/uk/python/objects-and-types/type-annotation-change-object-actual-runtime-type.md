---
id: py-objtypes-0020
title: "Чи змінює type annotation фактичний runtime type об’єкта або автоматично забороняє присвоєння значення іншого типу?"
description: "Ні, type annotation не змінює runtime type об'єкта і не забороняє присвоєння значення іншого типу – Python runtime ігнорує анотації при виконанні."
track: python
section: objects-and-types
level: middle
type: pitfall
tags: []
status: published
updated: 2026-09-27
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-reference-datamodel
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-stdtypes
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-copy
    title: "Python 3.14: Library/copy"
    url: https://docs.python.org/3.14/library/copy.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-typing
    title: "Python 3.14: Library/typing"
    url: https://docs.python.org/3.14/library/typing.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
---

## Short answer

**Ні, type annotation не змінює runtime type об'єкта і не забороняє присвоєння значення іншого типу – Python runtime ігнорує анотації при виконанні.**[^py314-reference-datamodel] Анотації зберігаються в `__annotations__` і доступні через `typing.get_type_hints()`, але інтерпретатор не перевіряє їх. Перевірку виконують зовнішні інструменти: статичні type checkers (mypy, pyright), IDE та linters. <span class="warn">Написати `x: int = 'hello'` – цілком валідний Python-код без помилок runtime.</span>

## Detailed explanation

Type annotations у Python є виключно синтаксичними метаданими, які жодним чином не впливають на виконання коду, прив'язування імен чи реальні типи об'єктів у рантаймі.[^py314-reference-datamodel]

Python за своєю архітектурою залишається динамічно типізованою мовою. Під час компіляції вихідного коду у байткод CPython не генерує жодних інструкцій для перевірки відповідності типів чи їх примусового приведення. Анотації локальних змінних усередині функцій взагалі відкидаються після генерації байткоду, а анотації модулів, класів та сигнатур функцій лише зберігаються як словники метаданих `__annotations__` (або обчислюються ліниво в Python 3.14 відповідно до PEP 649 / PEP 749). Отже, вказівка типу не конвертує значення і не генерує винятків при присвоєнні несумісних даних.[^py314-library-typing]

Перевірка коректності типів повністю винесена на окремий етап статичного аналізу, який виконується зовнішніми інструментами на кшталт `mypy` або `pyright` до запуску програми. Під час же виконання діє динамічна типізація та качина типізація (duck typing): об'єкт сам визначає свій тип (`type(obj)`), а виклики методів успішні доти, доки об'єкт підтримує відповідний інтерфейс. Будь-яка валідація типів у рантаймі можлива лише за наявності явного коду перевірки (наприклад, через `isinstance()`) або сторонніх бібліотек, які інспектують анотації під час виконання (таких як Pydantic чи Typeguard).

Приклад нехтування анотаціями інтерпретатором під час виконання:

```python
import typing

# Runtime ignores mismatched annotations completely
number: int = "not an integer"
print(type(number))  # <class 'str'>
print(number.upper())  # NOT AN INTEGER

def add_numbers(a: int, b: int) -> int:
    return a + b

# Dynamic dispatch works according to actual argument types at runtime
result = add_numbers("hello ", "world")
print(result)  # hello world
print(type(result))  # <class 'str'>

# Annotations are stored purely as metadata on functions
hints = typing.get_type_hints(add_numbers)
print(hints)  # {'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}
```

**Типові помилки та хибні очікування щодо анотацій:**
- очікування автоприведення типів: припущення, що `age: int = "25"` автоматично перетворить рядок на число `25`, тоді як змінна збереже тип `str`;
- відчуття захищеності без CI: написання type hints без обов'язкового запуску статичного аналізатора (`mypy`, `pyright`) у CI/CD не захищає код у продакшні від помилок типів;
- валідація зовнішніх даних: використання стандартних анотацій для автоматичної перевірки вхідних JSON або HTTP-запитів без валідаційних бібліотек (Pydantic, attrs) залишає систему вразливою;
- відсутність локальних анотацій: анотації локальних змінних усередині тіла функції не зберігаються в `__annotations__` після компіляції.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
