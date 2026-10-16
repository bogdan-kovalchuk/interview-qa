---
id: py-oop-0022
title: "Як `__len__` може впливати на truthiness об’єкта за відсутності `__bool__`?"
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
  - source_id: py314-reference-datamodel-object-bool
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__bool__
  - source_id: py314-reference-datamodel-object-len
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__len__
  - source_id: py314-reference-datamodel-special-method-lookup
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#special-method-lookup
---

## Short answer

**Якщо `__bool__` не визначено, Python викликає `__len__`: нульовий результат робить об’єкт false, а ненульовий – true.**[^py314-reference-datamodel-object-bool] Якщо не визначені ні `__bool__`, ні `__len__`, усі екземпляри такого класу вважаються true.[^py314-reference-datamodel-object-bool] Наприклад, `bool(obj)` для об’єкта з `__len__`, що повертає 0, дає `False`.[^py314-reference-datamodel-object-len]

## Detailed explanation

Перевірка істинності (truth value testing) відбувається в булевому контексті: `if obj:`, `while obj:`, `not obj` і `bool(obj)`. Python спочатку шукає метод `__bool__`, який має повернути `True` або `False`.[^py314-reference-datamodel-object-bool] Якщо його немає, але визначено `__len__`, інтерпретатор використовує результат `__len__`: об’єкт вважається false, коли `__len__` повертає 0, і true для будь-якого ненульового значення.[^py314-reference-datamodel-object-len]

Приклад показує ці правила і те, що `__bool__` має пріоритет над `__len__`.

```python
class Basket:
    def __init__(self, items):
        self.items = list(items)

    def __len__(self):
        return len(self.items)

class Flag(Basket):
    def __bool__(self):
        return True

class Ticket:
    pass

print(bool(Basket([])))          # False: __len__() returns 0
print(bool(Basket(["apple"])))   # True: __len__() returns 1
print(bool(Flag([])))            # True: __bool__() takes precedence over __len__()
print(bool(Ticket()))            # True: neither __bool__ nor __len__ is defined

ticket = Ticket()
ticket.__bool__ = lambda: False  # instance attribute, not on the type
print(bool(ticket))              # True: special methods are looked up on the type
```

Неявні виклики спеціальних методів гарантовано працюють лише тоді, коли метод визначено в типі, а не в словнику екземпляра. Тому присвоєння `ticket.__bool__` не змінює `bool(ticket)`. Документація показує той самий ефект для `len()`: після `c.__len__ = lambda: 5` виклик `len(c)` дає `TypeError`.[^py314-reference-datamodel-special-method-lookup]

Документація вимагає, щоб `__len__` повертав ціле число не менше за 0.[^py314-reference-datamodel-object-len] У CPython від’ємне значення дає `ValueError` уже під час перевірки істинності.

**Типові помилки:**
- думати, що `__len__` впливає лише на `len()`, а не на `if obj:` і `bool()`;
- повертати 0 з `__len__` для «порожнього» стану, не врахувавши, що тоді об’єкт стає false в усіх булевих контекстах;
- визначати `__bool__` і `__len__` з несумісною логікою, через що `bool()` і `len()` дають суперечливі відповіді.
