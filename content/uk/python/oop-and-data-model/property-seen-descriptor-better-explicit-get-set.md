---
id: py-oop-0011
title: "Чому `property` можна розглядати як descriptor і коли він кращий за явні `get_*`/`set_*` methods?"
description: "property – це вбудований data descriptor, який реалізує __get__, __set__ і __delete__, тому повністю підпорядковується descriptor protocol."
track: python
section: oop-and-data-model
level: middle
type: comparison
tags: [property, get, set]
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
  - source_id: py314-reference-datamodel-invoking-descriptors
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#invoking-descriptors
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: розділ Invoking Descriptors моделі даних; data descriptor і його пріоритет над instance dictionary."
  - source_id: py314-howto-descriptor-properties
    title: "Python 3.14: Howto/descriptor"
    url: https://docs.python.org/3.14/howto/descriptor.html#properties
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: розділ Properties; property як data descriptor, що викликає функцію при доступі до атрибута."
  - source_id: py314-howto-descriptor-invocation-summary
    title: "Python 3.14: Howto/descriptor"
    url: https://docs.python.org/3.14/howto/descriptor.html#summary-of-invocation-logic
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: розділ Summary of invocation logic; descriptor-и викликаються через __getattribute__, тому його перевизначення вимикає автоматичні виклики."
---

## Short answer

**`property` – це вбудований data descriptor, який реалізує `__get__`, `__set__` і `__delete__`.**[^py314-reference-datamodel-invoking-descriptors] Він кращий за явні `get_*`/`set_*` методи, коли треба додати валідацію чи обчислення до вже існуючого attribute access, не змінюючи публічний API: клієнти далі пишуть `obj.attr`, а не `obj.get_attr()`. Як data descriptor, `property` має пріоритет над `instance.__dict__`: читання йде через getter, доки реалізація `__getattribute__` класу не обходить механізм `object`.[^py314-reference-datamodel-invoking-descriptors][^py314-howto-descriptor-invocation-summary] Присвоєння йде через setter за стандартного `__setattr__`; власний `__setattr__` може поводитися інакше.

## Detailed explanation

Коли над методом стоїть `@property`, Python кладе в namespace класу об’єкт типу `property` замість функції. Цей об’єкт є descriptor-ом: він визначає `__get__`, `__set__` і `__delete__`, тому належить до data descriptors.[^py314-reference-datamodel-invoking-descriptors] Перевірити це можна напряму: `hasattr(property, "__set__")` дорівнює `True`.

Механізм простий. Для `t.celsius` Python знаходить `property` у класі, бачить data descriptor і викликає його `__get__`, а той виконує функцію-getter. Присвоєння `t.celsius = v` викликає setter, а `del t.celsius` викликає deleter, якщо він заданий.[^py314-howto-descriptor-properties] Data descriptor має пріоритет над instance dictionary, тож запис `t.__dict__["celsius"] = 999` нічого не змінює: `t.celsius` усе одно повертає результат getter-а.[^py314-reference-datamodel-invoking-descriptors]

Приклад показує getter, setter і спробу обійти descriptor через `__dict__`. Коментарі містять результат запуску (CPython 3.14):

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("below absolute zero")
        self._celsius = value

t = Temperature(20)
print(t.celsius)                                                       # 20: the getter runs
print(hasattr(property, "__set__"), hasattr(property, "__delete__"))   # True True
t.__dict__["celsius"] = 999                                            # a plain entry in the instance dict
print(t.celsius)                                                       # 20: the data descriptor wins
try:
    t.celsius = -300                                                   # the setter runs and rejects the value
except ValueError as error:
    print("ValueError:", error)                                        # ValueError: below absolute zero
```

Коли `property` кращий за явні методи. Методи `get_*`/`set_*` змінюють контракт: щойно з’являється валідація, доводиться переписувати всіх викликачів. З `property` код викликача лишається `t.celsius`, а логіка переїжджає всередину класу. Це доречно, коли атрибут справді є станом об’єкта, а перевірка чи обчислення дешеві. Межі: кожне звернення до атрибута виконує функцію, тому дорогий getter або getter, що кидає виняток, несподівано поводиться як поле. Крім того, `property` описує один атрибут в одному класі; щоб повторно використати ту саму перевірку для багатьох атрибутів, пишуть окремий descriptor class (див. qid:py-oop-0012).

**Типові помилки:**
- вважати `property` звичайним методом і писати `t.celsius()`: значення не викликається, буде `TypeError`;
- очікувати, що property без setter дозволяє присвоєння: буде `AttributeError`;
- ховати в getter важкі обчислення чи побічні ефекти, хоча викликач очікує просте читання поля.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
