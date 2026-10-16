---
id: py-oop-0004
title: "У якому порядку Python шукає атрибут instance за наявності data descriptor, instance dictionary, non-data descriptor і class attribute?"
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
  - source_id: py314-reference-datamodel-invoking-descriptors
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#invoking-descriptors
  - source_id: py314-reference-datamodel-object-getattr
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__getattr__
---

## Short answer

**Порядок: data descriptor -> instance `__dict__` -> non-data descriptor або class attribute -> `__getattr__`.**[^py314-reference-datamodel-invoking-descriptors] Data descriptor, який визначає `__get__` разом із `__set__` та/або `__delete__`, перемагає instance `__dict__`, а non-data descriptor (лише `__get__`) поступається запису в instance `__dict__`. Якщо за стандартного `object.__getattribute__` нічого не знайдено і визначено `__getattr__`, викликається він; інакше – `AttributeError`.[^py314-reference-datamodel-object-getattr]

## Detailed explanation

Для `a.x` Python спершу шукає `x` у класі (у `type(a)` і його базах за MRO) і перевіряє, чи це data descriptor (`__get__` разом із `__set__` та/або `__delete__`). Data descriptor, знайдений у класі, перемагає навіть запис із тим самим іменем в `a.__dict__`: його `__get__` викликається одразу.[^py314-reference-datamodel-invoking-descriptors] Саме так працює `property`, що є data descriptor, тому екземпляр не може перевизначити його поведінку.[^py314-reference-datamodel-invoking-descriptors] `property` без `setter` не дає записати атрибут навіть через `self.x = ...`.

Якщо data descriptor у класі немає, перевіряється `a.__dict__`. Запис в екземплярі перемагає non-data descriptor і звичайний атрибут класу. Саме тому методи, які є non-data descriptors, можна перевизначити для окремого екземпляра.[^py314-reference-datamodel-invoking-descriptors] Без запису в `__dict__` повертається non-data descriptor (через `__get__`) або атрибут класу.

Приклад охоплює всі ці випадки; кожен `print` показує, який спрацював:

```python
class DataDesc:
    def __get__(self, obj, objtype=None):
        return "data descriptor"

    def __set__(self, obj, value):
        pass

class NonDataDesc:
    def __get__(self, obj, objtype=None):
        return "non-data descriptor"

class C:
    d = DataDesc()
    n = NonDataDesc()
    k = "class attribute"

    def __getattr__(self, name):
        return f"__getattr__({name!r})"

c = C()
c.__dict__["d"] = "instance dict"
c.__dict__["n"] = "instance dict"
c.__dict__["k"] = "instance dict"
print(c.d)        # data descriptor: wins over the instance dict
print(c.n)        # instance dict: wins over a non-data descriptor
print(c.k)        # instance dict: wins over a plain class attribute
del c.__dict__["n"]
print(c.n)        # non-data descriptor, now that the dict entry is gone
print(c.missing)  # __getattr__('missing'): the normal lookup found nothing
```

`__getattr__` стоїть наприкінці ланцюжка і викликається лише тоді, коли звичайний пошук завершився `AttributeError`, тож існуючі атрибути він не перекриває.[^py314-reference-datamodel-object-getattr]

**Типові помилки:**
- вважати, що запис в `obj.__dict__` завжди перекриває атрибут класу: для `property` це не так, і `self.x = 5` у класі з `property` без setter дає `AttributeError: property 'x' of 'Q' object has no setter`;
- очікувати, що `__getattr__` викликається для кожного доступу; він спрацьовує лише тоді, коли звичайний пошук нічого не знайшов;
- забувати, що порядок описано для стандартного `object.__getattribute__`: перевизначений `__getattribute__` змінює цей шлях (див. qid:py-oop-0005).
