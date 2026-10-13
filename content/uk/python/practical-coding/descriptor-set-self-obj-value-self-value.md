---
id: py-prac-0011
title: "У descriptor з `__set__(self, obj, value): self._value = value` два instances бачать останнє записане value: чому так сталося і де зберігати per-instance state?"
description: "self у __set__ – це descriptor-об’єкт, що лежить у класі-власнику як один атрибут класу, тож self._value спільний для всіх instances."
track: python
section: practical-coding
level: middle
type: pitfall
tags: [set-self-obj-value-self-value-value]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  en: 2
applies_to:
  - product: "CPython"
    version: null
anki:
  export: true
sources:
  - source_id: py314-reference-datamodel-implementing-descriptors
    title: "Python 3.14: Reference/datamodel, Implementing Descriptors"
    url: https://docs.python.org/3.14/reference/datamodel.html#implementing-descriptors
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: descriptor має бути в class dictionary класу-власника або його батька; __set__ викликається для instance класу-власника. Не описує descriptor, збережений як атрибут instance."
  - source_id: py314-reference-datamodel-invoking-descriptors
    title: "Python 3.14: Reference/datamodel, Invoking Descriptors"
    url: https://docs.python.org/3.14/reference/datamodel.html#invoking-descriptors
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: data descriptor з __get__ разом з __set__ і/або __delete__ перекриває запис в instance dictionary; descriptor без __get__ повертає сам себе, якщо в instance dictionary немає значення. Не описує приклади користувацьких descriptor-ів."
  - source_id: py314-reference-datamodel-object-set-name
    title: "Python 3.14: Reference/datamodel, object.__set_name__"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__set_name__
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: __set_name__ викликається при створенні класу для descriptor-а, призначеного атрибуту класу, і отримує ім’я атрибута. Не описує валідацію."
  - source_id: py314-reference-datamodel-slots
    title: "Python 3.14: Reference/datamodel, __slots__"
    url: https://docs.python.org/3.14/reference/datamodel.html#slots
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: __slots__ забороняє створення __dict__ і __weakref__, якщо їх не оголошено в __slots__. Не описує інші механізми зберігання стану."
  - source_id: py314-library-weakref-weakkeydictionary
    title: "Python 3.14: Library/weakref, WeakKeyDictionary"
    url: https://docs.python.org/3.14/library/weakref.html#weakref.WeakKeyDictionary
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: WeakKeyDictionary тримає ключі слабко, записи зникають, коли на ключ немає сильних посилань; не всі об’єкти підтримують weakref. Не описує hashable-вимоги до ключів."
---

## Short answer

**`self` у `__set__` – це descriptor-об’єкт, а не instance: він лежить у класі-власнику один раз, тож `self._value` спільний для всіх instances.**[^py314-reference-datamodel-implementing-descriptors] <span class="warn">Per-instance state треба зберігати на `obj`:</span> `obj.__dict__[self.name] = value` разом з `__get__`, який читає той самий ключ.[^py314-reference-datamodel-invoking-descriptors] Альтернатива – `WeakKeyDictionary`, ключований за `obj`, якщо `obj` hashable і підтримує weakref.[^py314-library-weakref-weakkeydictionary]

## Detailed explanation

Descriptor – це об’єкт, що лежить у class dictionary класу-власника, і протокол викликає його методи з instance як аргументом `obj`.[^py314-reference-datamodel-implementing-descriptors] Тому `A.__dict__['x']` містить один об’єкт `Shared`, а не по одному на кожен `A()`. Коли `__set__` виконує `self._value = value`, значення записується в цей єдиний об’єкт. `a.x = 1` і `b.x = 2` перезаписують одне місце, тож обидва instances читають останнє значення:

```python
class Shared:
    def __get__(self, obj, objtype=None):
        return self._value

    def __set__(self, obj, value):
        self._value = value  # stored on the descriptor, not on obj


class A:
    x = Shared()


a, b = A(), A()
a.x = 1
b.x = 2
print(a.x, b.x)  # 2 2
```

Правильне місце для стану – сам `obj`. Descriptor перехоплює читання тоді, коли він data descriptor з `__get__` разом з `__set__` і/або `__delete__`: такий descriptor завжди перекриває запис в instance dictionary.[^py314-reference-datamodel-invoking-descriptors] Descriptor лише з `__set__` (або `__delete__`) без `__get__` читання не перехоплює. Ім’я для ключа дає `__set_name__`, який Python викликає при створенні класу з descriptor-ом у класовому атрибуті.[^py314-reference-datamodel-object-set-name] Читання без запису в `obj.__dict__` піднімає `KeyError` у цьому прикладі; у реальному коді його варто обробити.

```python
class Field:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__[self.name]

    def __set__(self, obj, value):
        obj.__dict__[self.name] = value


class C:
    x = Field()


c1, c2 = C(), C()
c1.x = 1
c2.x = 2
print(c1.x, c2.x)  # 1 2
```

Без `__get__` поведінка інша. Descriptor, що має лише `__set__`, при читанні повертає значення з `obj.__dict__`, якщо воно є, а інакше повертає сам descriptor-об’єкт, без помилки.[^py314-reference-datamodel-invoking-descriptors] Тому клас з одним `__set__`, який пише в `obj.__dict__`, при читанні до першого запису дає не значення, а descriptor.

`WeakKeyDictionary`, ключований за `obj`, не змінює сам `obj`: його записи зникають, коли на ключ більше немає сильних посилань.[^py314-library-weakref-weakkeydictionary] Умови такі: `obj` має бути hashable, бо це ключ словника, і має підтримувати weakref. Клас з `__slots__` без `__dict__` не має `obj.__dict__`, а `__weakref__` там теж не створюється, якщо його не оголошено в `__slots__`.[^py314-reference-datamodel-slots]

**Типові помилки:**
- зберігати per-instance стан у `self._value` descriptor-а: всі instances ділять одне значення;
- написати лише `__set__` і очікувати, що читання без попереднього запису поверне значення: воно поверне сам descriptor-об’єкт;
- використовувати `obj.__dict__` для класу з `__slots__` без `__dict__`: отримаєте `AttributeError`.

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
