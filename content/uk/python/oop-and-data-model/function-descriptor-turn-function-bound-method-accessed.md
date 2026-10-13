---
id: py-oop-0015
title: "Як function descriptor перетворює function у bound method при доступі через instance, але не при доступі через class?"
description: "function.__get__(obj, objtype) перевіряє obj: якщо obj is None (доступ через клас), повертає саму функцію; інакше повертає MethodType(func, obj)."
track: python
section: oop-and-data-model
level: senior
type: mechanism
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
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#invoking-descriptors
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: розділ Invoking Descriptors моделі даних; аргументи __get__ при доступі через instance і через клас."
  - source_id: py314-howto-descriptor-functions-and-methods
    title: "Python 3.14: Howto/descriptor"
    url: https://docs.python.org/3.14/howto/descriptor.html#functions-and-methods
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: розділ Functions and Methods; функція як non-data descriptor, що повертає себе при obj None і MethodType інакше."
  - source_id: py314-howto-descriptor-class-methods
    title: "Python 3.14: Howto/descriptor"
    url: https://docs.python.org/3.14/howto/descriptor.html#class-methods
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: розділ Class methods; classmethod отримує клас і при доступі через клас, і через instance."
  - source_id: py314-howto-descriptor-static-methods
    title: "Python 3.14: Howto/descriptor"
    url: https://docs.python.org/3.14/howto/descriptor.html#static-methods
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: розділ Static methods; staticmethod повертає базову функцію без змін."
  - source_id: cpython-funcobject-func-descr-get
    title: "CPython Objects/funcobject.c: func_descr_get"
    url: https://github.com/python/cpython/blob/v3.14.7/Objects/funcobject.c
    accessed: 2026-10-13
    kind: official
    version: "3.14.7"
    applicability: "Вихідний код CPython 3.14.7: функція func_descr_get; деталь реалізації CPython, а не гарантія мови."
---

## Short answer

**`function.__get__(obj, objtype)` перевіряє `obj`: якщо `obj is None` (доступ через клас), повертає саму функцію; інакше повертає `MethodType(func, obj)`.**[^py314-howto-descriptor-functions-and-methods] Тому `MyClass.method` дає звичайну функцію без прив’язки до instance, а `instance.method` – bound method із уже зафіксованим `__self__`. Ця логіка є в `func_descr_get()` у CPython і діє для всіх user-defined functions.[^cpython-funcobject-func-descr-get]

## Detailed explanation

Коли Python знаходить descriptor у класі (або в його базах) і ім’я не перекрите значенням в instance dictionary, він викликає `__get__(obj, objtype)`. При доступі через instance `obj` – це сам instance. При доступі через клас `obj` дорівнює `None`, а `objtype` – клас.[^py314-reference-datamodel-invoking-descriptors] Функція реалізує це так: при `None` повертає себе, інакше створює bound method.[^py314-howto-descriptor-functions-and-methods][^cpython-funcobject-func-descr-get]

Наслідок видно з коду. `Calc.add` – звичайна функція, тому `self` треба передавати явно. Через клас функція повертається без змін, тож перший аргумент ніде не перевіряється: `Calc.add(42, 1)` працює і дає `2`. `c.add` – bound method, який сам передає `c`.

Приклад показує, що доступ через клас не прив’язує функцію, а classmethod прив’язується навіть через клас. Коментарі показують результат запуску (CPython 3.14):

```python
class Calc:
    def add(self, x):
        return x + 1

    @classmethod
    def make(cls):
        return cls

c = Calc()
print(type(Calc.add).__name__)       # function: no binding on class access
print(Calc.add(c, 1))                # 2: self must be passed explicitly
print(Calc.add(42, 1))               # 2: no type check on the first argument
print(type(c.add).__name__)          # method: bound on instance access
print(c.add.__self__ is c)           # True
print(Calc.make)                     # <bound method Calc.make of <class '__main__.Calc'>>
```

Прив’язка при доступі через клас залежить від типу descriptor-а. `classmethod` прив’язує клас і при доступі через клас, і через instance. `staticmethod` повертає функцію без змін в обох випадках.[^py314-howto-descriptor-class-methods][^py314-howto-descriptor-static-methods] Тому правило «доступ через клас не прив’язує» стосується звичайних функцій, а не всіх методів.

**Типові помилки:**
- вважати `Calc.add` bound method і викликати `Calc.add(1)`: буде `TypeError`, бо `1` стане `self`, а аргумент `x` не буде передано;
- вважати, що `classmethod` при доступі через клас поводиться як звичайна функція: він прив’язується до класу;
- плутати `c.add` без дужок із викликом: повертається bound method, а не результат.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
