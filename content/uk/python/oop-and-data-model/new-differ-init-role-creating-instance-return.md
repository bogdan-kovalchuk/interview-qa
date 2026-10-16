---
id: py-oop-0001
title: "Чим `__new__` відрізняється від `__init__` за роллю у створенні instance та за return value?"
track: python
section: oop-and-data-model
sources:
  - source_id: py314-reference-datamodel
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html
  - source_id: py314-howto-descriptor
    title: "Python 3.14: Howto/descriptor"
    url: https://docs.python.org/3.14/howto/descriptor.html
  - source_id: py314-howto-mro
    title: "Python 3.14: Howto/mro"
    url: https://docs.python.org/3.14/howto/mro.html
  - source_id: py314-library-dataclasses
    title: "Python 3.14: Library/dataclasses"
    url: https://docs.python.org/3.14/library/dataclasses.html
  - source_id: py314-reference-datamodel-object-new
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__new__
  - source_id: py314-reference-datamodel-object-init
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__init__
---

## Short answer

**`__new__` створює та повертає новий instance, тоді як `__init__` лише ініціалізує вже створений instance.**[^py314-reference-datamodel-object-new] `__new__` – неявний staticmethod, який отримує `cls` і повертає об’єкт, зазвичай instance `cls`. `__init__` отримує готовий `self`, налаштовує його атрибути і не повертає нічого, крім `None`.[^py314-reference-datamodel-object-init]

## Detailed explanation

`__new__` і `__init__` відповідають за різні етапи створення об’єкта. `__new__` – це статичний метод (декоратор `@staticmethod` для нього не потрібен), який першим аргументом отримує клас і повертає новий об’єкт, зазвичай instance цього класу.[^py314-reference-datamodel-object-new] `__init__` не створює об’єкт: Python викликає його вже після `__new__`, для готового instance, щоб заповнити його атрибути.[^py314-reference-datamodel-object-init]

Коли ви пишете `Cls(...)`, Python спочатку викликає `__new__(cls, ...)` з тими самими аргументами. Далі `__init__` викликається лише тоді, коли `__new__` повернув instance `cls`. Якщо результат іншого типу, `__init__` не виконується, а значенням виразу `Cls(...)` стає саме те, що повернув `__new__`.[^py314-reference-datamodel-object-new] Так це виглядає на практиці:

```python
class Redirect:
    def __new__(cls, x):
        return x                  # an int, not an instance of Redirect

    def __init__(self, x):
        print("never printed")    # skipped: __new__ did not return a Redirect

r = Redirect(5)
print(r, type(r))                 # 5 <class 'int'>
```

Вимога до `__init__` інша: він не повинен повертати нічого, крім `None`. Це окреме правило, яке розглянуто в qid:py-oop-0003. Тож `__init__` використовують, щоб налаштувати об’єкт, а `__new__` – щоб визначити, який об’єкт узагалі створюється.

**Коли потрібен `__new__`.** Для звичайних класів достатньо `__init__`. Перевизначати `__new__` варто, коли треба вплинути на сам створюваний об’єкт. Документація прямо називає його призначення: дозволити підкласам immutable типів (`int`, `str`, `tuple`) налаштовувати створення instance.[^py314-reference-datamodel-object-new]

**Типові помилки:**
- вважати, що `__init__` створює об’єкт, і тому `return self` наприкінці `__init__` здається способом повернути результат;
- забути `return` у `__new__`: вираз `super().__new__(cls)` без повернення дає `None`, і `__init__` не викликається;
- очікувати, що `__init__` виконається завжди, хоча `__new__` повернув об’єкт іншого типу.
