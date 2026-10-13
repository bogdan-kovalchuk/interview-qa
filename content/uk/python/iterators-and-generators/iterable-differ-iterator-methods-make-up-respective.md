---
id: py-itergen-0001
title: "Чим iterable відрізняється від iterator і які methods утворюють їхні основні protocols?"
description: "Iterable дає iterator, зазвичай через __iter__(); iterator зберігає стан, повертає елементи через __next__() і сам є iterable."
track: python
section: iterators-and-generators
level: middle
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
  - source_id: py314-reference-datamodel-object-getitem
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__getitem__
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: sequence iteration protocol очікує IndexError для неприпустимого індексу як ознаку кінця послідовності."
  - source_id: py314-glossary-term-iterable
    title: "Python 3.14: Glossary"
    url: https://docs.python.org/3.14/glossary.html#term-iterable
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: визначення iterable, включно з об’єктами з __getitem__() за семантикою послідовності."
  - source_id: py314-glossary-term-iterator
    title: "Python 3.14: Glossary"
    url: https://docs.python.org/3.14/glossary.html#term-iterator
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: визначення iterator; кожен iterator є iterable, бо має __iter__(), що повертає його самого."
  - source_id: py314-library-functions-iter
    title: "Python 3.14: Library/functions"
    url: https://docs.python.org/3.14/library/functions.html#iter
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: вимоги до аргументу iter(), протокол ітерації (__iter__()) або протокол послідовності (__getitem__() з цілими індексами від 0)."
---

## Short answer

**Iterable – це об’єкт, з якого можна отримати iterator, зазвичай через `__iter__()`.**[^py314-glossary-term-iterable] Iterator зберігає стан і повертає елементи по одному через `__next__()`, а коли елементи вичерпано, піднімає `StopIteration`.[^py314-glossary-term-iterator] Кожен iterator є iterable, бо має `__iter__()`, який повертає його самого.[^py314-glossary-term-iterator] Не кожен iterable є iterator: `list`, `tuple` і `str` мають `__iter__()`, але не мають `__next__()`.

## Detailed explanation

Iterable і iterator – два різні поняття, які легко сплутати, бо кожен iterator також є iterable. Iterable – це об’єкт, здатний по одному віддати свої елементи. До нього належать усі послідовності (наприклад, `list`, `str`, `tuple`) і будь-який клас із `__iter__()` або з `__getitem__()`, що поводиться як послідовність.[^py314-glossary-term-iterable] Для iterable головне – уміння створити iterator. Вбудована функція `iter()` приймає об’єкт, який підтримує протокол ітерації (`__iter__()`) або протокол послідовності (`__getitem__()` з цілими індексами від 0).[^py314-library-functions-iter]

Iterator – це об’єкт зі станом: він пам’ятає, на якому елементі зупинився. Його протокол складається з двох методів. `__iter__()` повертає сам iterator, що дає змогу використати його в `for` і `in` так само, як контейнер. `__next__()` повертає наступний елемент, а коли елементів більше немає, піднімає `StopIteration`.[^py314-library-stdtypes-iterator-types] Наступний приклад показує обидві ролі на `list`:

```python
nums = [1, 2, 3]
print(hasattr(nums, '__next__'))     # False: a list is iterable, not an iterator
it = iter(nums)                      # calls nums.__iter__() and returns a new iterator
print(type(it).__name__)             # list_iterator
print(hasattr(it, '__next__'))       # True
print(iter(it) is it)                # True: an iterator's __iter__() returns itself
print(next(it), next(it), next(it))  # 1 2 3
try:
    next(it)
except StopIteration:
    print('StopIteration')           # the iterator is exhausted
```

Після того як `__next__()` підніме `StopIteration`, кожен наступний його виклик має знову піднімати цей виняток.[^py314-library-stdtypes-iterator-types] Iterator не перезапускається. Щоб пройти ті самі дані ще раз, потрібен новий iterator, який створює `iter()` від iterable.

Не кожен iterable має `__iter__()`. Клас, у якого є лише `__getitem__()`, теж працює з `iter()` через протокол послідовності. Для такого класу iterator викликає `__getitem__(0)`, `__getitem__(1)` і так далі.[^py314-library-functions-iter] У CPython він зупиняється, коли `__getitem__()` піднімає `IndexError`.[^py314-reference-datamodel-object-getitem] Лише `__iter__()` не робить об’єкт iterator: iterator потрібен ще `__next__()`, а його `__iter__()` має повертати сам об’єкт.

**Типові помилки:**
- вважати iterable і iterator синонімами та викликати `next()` на списку: `next([1, 2])` підніме `TypeError: 'list' object is not an iterator`;
- шукати `__next__()` у `list`, `tuple` чи `str`: це iterable, але не iterator;
- вважати, що iterator можна обійти двічі: після вичерпання він не починає спочатку.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
