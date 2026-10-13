---
id: py-oop-0002
title: "Чому для налаштування immutable subclass на кшталт custom `tuple` потрібний `__new__`, а зміни лише в `__init__` запізнюються?"
description: "Immutable типи (tuple, str, int) задають своє значення під час створення в __new__; до моменту виклику __init__ об’єкт уже створений, і його вміст не змінити."
track: python
section: oop-and-data-model
level: middle
type: mechanism
tags: [tuple, new, init]
status: published
updated: 2026-10-13
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
  - source_id: py314-howto-descriptor
    title: "Python 3.14: Howto/descriptor"
    url: https://docs.python.org/3.14/howto/descriptor.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-howto-mro
    title: "Python 3.14: Howto/mro"
    url: https://docs.python.org/3.14/howto/mro.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-dataclasses
    title: "Python 3.14: Library/dataclasses"
    url: https://docs.python.org/3.14/library/dataclasses.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-datamodel-object-new
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__new__
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: розділ object.__new__ моделі даних."
  - source_id: py314-reference-datamodel-object-init
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__init__
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: розділ object.__init__ моделі даних."
  - source_id: py314-library-stdtypes-tuple
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html#tuple
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: розділ про tuple у стандартних типах."
---

## Short answer

**Immutable типи (`tuple`, `str`, `int`) задають своє значення під час створення в `__new__`, а `__init__` викликається вже після цього.**[^py314-reference-datamodel-object-new] Тож кастомізація вмісту immutable підкласу має відбуватися в `__new__`: `__init__` отримує вже створений об’єкт, а `tuple` не дозволяє змінювати свої елементи.[^py314-library-stdtypes-tuple]

```python
class Doubled(tuple):
    def __new__(cls, *args):
        return super().__new__(cls, (x * 2 for x in args))
```

## Detailed explanation

Щоб зрозуміти, чому `__init__` тут не допомагає, треба розділити два етапи. Спочатку викликається `__new__`, і саме він створює об’єкт із його вмістом. Лише після цього викликається `__init__` для вже готового об’єкта.[^py314-reference-datamodel-object-init] Для звичайного класу це майже не має значення, бо атрибути можна додати пізніше. Для `tuple` вміст є частиною самого значення, і після створення його змінити не можна.[^py314-library-stdtypes-tuple]

Документація називає призначення `__new__` прямо: він потрібен, щоб підкласи immutable типів (`int`, `str`, `tuple`) могли налаштовувати створення instance.[^py314-reference-datamodel-object-new] Ось підклас `tuple`, у якому `__new__` формує вміст, а `__init__` лише його бачить:

```python
class Doubled(tuple):
    def __new__(cls, *args):
        return super().__new__(cls, (x * 2 for x in args))

    def __init__(self, *args):
        # args are the original values; self already holds the doubled ones
        print("in __init__:", tuple(self), args)

d = Doubled(1, 2, 3)  # in __init__: (2, 4, 6) (1, 2, 3)
print(d)              # (2, 4, 6)
# d[0] = 10           # TypeError: 'Doubled' object does not support item assignment
```

Отже, `__init__` бачить обидва набори даних: вхідні аргументи і вже сформований `self`. Він може прочитати вміст, але не може його замінити. Присвоєння елемента в `tuple` не підтримується[^py314-library-stdtypes-tuple], і спроба дає `TypeError`. Тому якщо вміст має відрізнятися від аргументів, його треба сформувати в `__new__`. `__init__` підходить для того, що не змінює вміст, наприклад для додаткових атрибутів підкласу.

**Типові помилки:**
- перенести формування вмісту в `__init__`: код там виконається, але вміст уже зафіксований;
- написати `super().__new__(cls, *args)`: `tuple.__new__` приймає один ітерабельний аргумент, тож для трьох значень з’являється `TypeError: tuple expected at most 1 argument, got 3`;
- вважати, що `str` або `int` можна налаштувати через `__init__` так само, як звичайний клас.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
