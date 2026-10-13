---
id: py-itergen-0002
title: "Чому `iter(container)` зазвичай повертає новий iterator, а `iter(iterator)` має повертати той самий object?"
description: "container.__iter__() створює новий iterator з власним станом, тоді як iterator.__iter__() повертає self."
track: python
section: iterators-and-generators
level: middle
type: mechanism
tags: [iter-container, iter-iterator]
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
  - source_id: py314-glossary-term-iterator
    title: "Python 3.14: Glossary"
    url: https://docs.python.org/3.14/glossary.html#term-iterator
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: визначення iterator; контейнер дає новий iterator на кожен iter() або for, а повторний прохід по iterator дає той самий вичерпаний об’єкт."
---

## Short answer

**`container.__iter__()` зазвичай створює новий iterator з власним станом, тоді як `iterator.__iter__()` повертає сам iterator.**[^py314-glossary-term-iterator] Це потрібно, щоб і контейнери, і iterator можна було використовувати в `for` та `in`.[^py314-library-stdtypes-iterator-types] Тому повторний `for` по контейнеру починає спочатку, а повторний `for` по тому самому iterator продовжує з місця зупинки і не дає елементів, якщо той уже вичерпаний.[^py314-glossary-term-iterator]

## Detailed explanation

Коли `for` або `iter()` бере контейнер, позиція ітерації не зберігається в самому контейнері. Її тримає iterator, який повертає `__iter__()` контейнера. Документація радить, щоб `container.__iter__()` повертав новий iterator, який проходить усі елементи контейнера.[^py314-reference-datamodel-object-iter] Тому два незалежні цикли по одному `list` не заважають одне одному:

```python
nums = [1, 2, 3]
a = iter(nums)                # a new iterator, position 0
b = iter(nums)                # another iterator, its own position 0
print(next(a))                # 1
print(next(b))                # 1: b does not share a's position
print(list(a))                # [2, 3]: a continues from where it stopped
print(iter(a) is a)           # True: iter() on an iterator returns the same object
```

Інший випадок – коли `iter()` повертає той самий об’єкт, бо він уже є iterator. Генераторний вираз створює iterator, тож повторний перегляд дає порожній результат:

```python
gen = (x * x for x in range(3))  # a generator expression creates an iterator
print(iter(gen) is gen)          # True
print(list(gen))                 # [0, 1, 4]
print(list(gen))                 # []: the same iterator is already exhausted
```

Звідси практичне правило: функція, яка має пройти дані двічі, повинна отримувати контейнер (наприклад, `list`), а не iterator. Інакше перший прохід спожив елементи, і другий бачить порожній результат:

```python
def count_and_list(items):
    n = sum(1 for _ in items)   # the first pass consumes a generator
    return n, list(items)       # the second pass sees nothing

print(count_and_list([1, 2, 3]))             # (3, [1, 2, 3])
print(count_and_list(x for x in [1, 2, 3]))  # (3, [])
```

Правило «контейнер дає новий iterator» – це рекомендація документації, а не перевірка інтерпретатора. Клас може повернути з `__iter__()` уже існуючий iterator, і тоді всі цикли по ньому ділитимуть одну позицію. Тому в класі-контейнері `__iter__()` має створювати новий iterator на кожен виклик.

**Типові помилки:**
- очікувати, що повторний `for` по iterator почне спочатку: він продовжує з місця зупинки або нічого не дає;
- сплутати `iterator.__iter__()` (повертає self) з `container.__iter__()` (створює новий iterator) і повертати self з класу-контейнера;
- викликати `next()` на `list`: `next([1, 2])` підніме `TypeError`, бо список – iterable, а не iterator.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
