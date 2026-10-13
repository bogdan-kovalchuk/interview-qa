---
id: py-oop-0009
title: "Чим data descriptor відрізняється від non-data descriptor і як ця різниця змінює precedence під час attribute lookup?"
description: "Data descriptor визначає __set__ або __delete__ і перемагає instance __dict__; non-data descriptor визначає лише __get__ і поступається instance __dict__."
track: python
section: oop-and-data-model
level: senior
type: comparison
tags: []
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
    title: "Python 3.14: Reference/datamodel, Invoking Descriptors"
    url: https://docs.python.org/3.14/reference/datamodel.html#invoking-descriptors
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: data descriptor визначає __set__ або __delete__ і має пріоритет над словником екземпляра; non-data descriptor визначає лише __get__ і словник екземпляра може його перекрити; @property є data descriptor. Не описує власні приклади descriptor."
  - source_id: py314-reference-datamodel-implementing-descriptors
    title: "Python 3.14: Reference/datamodel, Implementing Descriptors"
    url: https://docs.python.org/3.14/reference/datamodel.html#implementing-descriptors
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: descriptor має бути в словнику класу власника або його батьків; додавання __set__ або __delete__ змінює вид descriptor на data descriptor. Не описує поведінку descriptor, записаного в словник екземпляра."
---

## Short answer

**Data descriptor визначає `__set__` та/або `__delete__` (разом із `__get__` він перекриває instance `__dict__` при читанні); non-data descriptor визначає лише `__get__` і поступається instance `__dict__`.**[^py314-reference-datamodel-invoking-descriptors] Descriptor лише з `__set__` без `__get__` при читанні словник не перекриває. Приклад data descriptor – `property`; приклад non-data descriptor – звичайний метод. Тому `obj.method = 42` перезаписує метод для конкретного instance, а `obj.prop = 42` викликає setter property (без setter – `AttributeError`).

## Detailed explanation

Descriptor – це об’єкт, який визначає хоча б один із методів `__get__`, `__set__`, `__delete__`. Він стає data descriptor, якщо визначає `__set__` або `__delete__`; якщо визначено лише `__get__`, це non-data descriptor.[^py314-reference-datamodel-invoking-descriptors] Назва «data» стосується наявності цих методів, а не того, чи зберігає об’єкт дані. Descriptor працює лише тоді, коли знаходиться в словнику класу або його базового класу, тому descriptor, записаний у `__dict__` екземпляра, не викликається.[^py314-reference-datamodel-implementing-descriptors]

Під час `obj.x` Python знаходить `x` у класі. Якщо знайдений об’єкт визначає `__get__` і `__set__` або `__delete__` (data descriptor), викликається його `__get__`, і словник екземпляра не читається. Інакше перевіряється словник екземпляра: якщо там є `x`, його значення повертається. Лише якщо в словнику немає `x`, викликається `__get__` non-data descriptor.[^py314-reference-datamodel-invoking-descriptors] Отже, словник екземпляра перекриває non-data descriptor, але не data descriptor.

Приклад із двома descriptor і однаковим значенням у словнику екземпляра:

```python
class DataDesc:
    def __get__(self, obj, objtype=None):
        return 'data __get__'
    def __set__(self, obj, value):
        print('data __set__ called')

class NonDataDesc:
    def __get__(self, obj, objtype=None):
        return 'non-data __get__'

class C:
    d = DataDesc()
    n = NonDataDesc()

c = C()
vars(c)['d'] = 'in dict'
vars(c)['n'] = 'in dict'
print(c.d)      # data __get__: the data descriptor wins over the instance dict
print(c.n)      # in dict: the instance dict wins over the non-data descriptor
c.d = 1         # data __set__ called: assignment goes to __set__, not to the dict
print(vars(c))  # {'d': 'in dict', 'n': 'in dict'}
```

Звичайний метод – non-data descriptor, тому його можна перекрити для одного екземпляра:

```python
class Greeter:
    def hello(self):
        return 'method'

g = Greeter()
g.hello = lambda: 'instance'     # a function is a non-data descriptor, so the dict entry wins
print(g.hello())                 # instance
print(Greeter().hello())         # method
```

**Типові помилки:**
- думати, що «data» означає «зберігає дані»: назва визначається наявністю `__set__` або `__delete__`;
- очікувати, що `obj.prop = 42` завжди спрацює: для property без setter присвоєння піднімає `AttributeError`;
- записати descriptor як атрибут екземпляра (`obj.d = Desc()`), а не в клас: Python його не викликатиме.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
