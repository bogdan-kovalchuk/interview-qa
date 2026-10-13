---
id: py-itergen-0004
title: "Як реалізувати re-iterable collection так, щоб дві вкладені ітерації не ділили один cursor?"
description: "Розділити iterable та iterator: __iter__() колекції має щоразу повертати новий iterator."
track: python
section: iterators-and-generators
level: senior
type: practical
tags: []
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-library-stdtypes-iterator-types
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html#iterator-types
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-expressions-yield-expressions
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#yield-expressions
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-datamodel-object-iter
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__iter__
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
---

## Short answer

**Розділити iterable та iterator: `__iter__()` колекції має щоразу повертати новий iterator.**[^py314-reference-datamodel-object-iter] Типовий підхід – зберігати дані в колекції, а `__iter__()` реалізовувати як generator function або повертати окремий клас-iterator. Тоді кожна вкладена ітерація отримає власний незалежний cursor і не конфліктуватиме з іншими.

```python
class MyCollection:
    def __init__(self, data):
        self._data = data
    def __iter__(self):
        for item in self._data:
            yield item
```

## Detailed explanation

Вкладені ітерації ділять один cursor, якщо колекція сама є iterator: її `__iter__()` повертає `self`, а позиція зберігається в атрибуті колекції. Тоді обидва цикли читають один лічильник:

```python
class Shared:
    def __init__(self, data):
        self._data = list(data)
        self._pos = 0

    def __iter__(self):
        return self                  # the cursor lives on the collection itself

    def __next__(self):
        if self._pos >= len(self._data):
            raise StopIteration
        item = self._data[self._pos]
        self._pos += 1
        return item

pairs = Shared([1, 2, 3])
for a in pairs:
    for b in pairs:
        print(a, b)                  # only 1 2 and 1 3: the inner loop used up the shared cursor
```

Внутрішній цикл вичерпує спільну позицію, тож зовнішній цикл більше не отримує елементів. Замість дев’яти пар (3 × 3) виходять лише дві.

Виправлення – створювати новий iterator на кожен виклик `__iter__()`. У CPython `iter(list)` саме так і робить: кожен виклик дає новий `list_iterator` із власною позицією. Колекція може просто делегувати цю роботу:

```python
class Collection:
    def __init__(self, data):
        self._data = list(data)

    def __iter__(self):
        return iter(self._data)      # a new list_iterator with its own position

c = Collection([1, 2, 3])
print(len([(a, b) for a in c for b in c]))  # 9: every outer item pairs with every inner item
```

Той самий результат дає generator function, як у Short answer. Кожен її виклик повертає новий generator, тобто новий iterator зі своїм станом.[^py314-reference-expressions-yield-expressions] Цей варіант коротший. Окремий клас з `__next__()` потрібен тоді, коли iterator має мати додаткові методи або явно керований стан.

Дані варто копіювати в `__init__()`. Якщо передати генератор або інший одноразовий iterator і не зберегти його елементи, колекція вичерпається після першого проходу. Виклик `list(data)` зберігає елементи один раз, тому кожен цикл бачить повний набір.

**Типові помилки:**
- зберігати позицію в `self` і повертати `self` з `__iter__()`: вкладені та послідовні цикли ділять її;
- створити iterator один раз у `__init__()` і повертати його з кожного `__iter__()`: після першого проходу кожен наступний отримує вичерпаний iterator, тобто порожній результат;
- зберігати переданий генератор замість його елементів і вважати, що колекцію можна ітерувати багато разів.

## Environment

TODO

## Deliverable

TODO

## Acceptance criteria

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
