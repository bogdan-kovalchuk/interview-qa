---
id: py-itergen-0013
title: "Чому повторна ітерація вже exhausted generator не починає обчислення спочатку?"
description: "Після першого StopIteration generator остаточно завершений: протокол вимагає, що всі наступні __next__() також піднімають StopIteration."
track: python
section: iterators-and-generators
level: middle
type: pitfall
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
  - source_id: py314-reference-expressions-generator-iterator-methods
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#generator-iterator-methods
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: методи generator-iterator (__next__, send, throw, close) і їхня поведінка у призупиненому стані."
  - source_id: py314-glossary-term-iterator
    title: "Python 3.14: Glossary"
    url: https://docs.python.org/3.14/glossary.html#term-iterator
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: визначення iterator і exhausted."
---

## Short answer

**Після першого `StopIteration` generator остаточно завершений: протокол вимагає, що всі наступні `__next__()` також піднімають `StopIteration`.**[^py314-library-stdtypes-iterator-types] Тіло функції виконується лише до `return`, кінця або непійманого винятку, і після цього немає призупиненого стану, який можна відновити.[^py314-reference-expressions-generator-iterator-methods] Контейнер має повертати новий iterator при кожному `iter()`.[^py314-reference-datamodel-object-iter] Generator сам є своїм iterator, тож почати спочатку можна лише новим generator, тобто повторним викликом generator function.[^py314-library-stdtypes-iterator-types]

## Detailed explanation

`Exhausted` означає, що iterator уже видав усі свої значення, і кожен наступний виклик `next()` піднімає `StopIteration`.[^py314-glossary-term-iterator] Протокол iterator вимагає того самого від будь-якої реалізації: після першого `StopIteration` наступні `__next__()` мають знову піднімати його, інакше реалізацію вважають зламаною.[^py314-library-stdtypes-iterator-types] Тому другий `list(gen)` мовчки повертає порожній список, другий `for` не виконує жодного кроку, а `next(gen)` піднімає `StopIteration`.

Приклад: `countdown` вичерпується після одного проходу. Коментарі показують вивід на CPython 3.13 і 3.14:

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

gen = countdown(3)
print(list(gen))                    # [3, 2, 1]
print(list(gen))                    # []: already exhausted
print(next(gen, 'empty'))           # empty: the default is returned instead of StopIteration
print(iter(gen) is gen)             # True: a generator is its own iterator
print(list(countdown(3)))           # [3, 2, 1]: a new call creates a new generator
```

Виклик generator function повертає новий generator, і тіло починає виконуватися лише тоді, коли викликають один із його методів.[^py314-reference-expressions-yield-expressions] Коли тіло доходить до кінця, нового `yield` уже немає, і generator піднімає `StopIteration`.[^py314-reference-expressions-generator-iterator-methods] Призупиненого стану, який можна було б відновити, більше немає. У CPython після цього `gi_frame` дорівнює `None`, але це деталь реалізації, а не правило мови.

Правило стосується одного generator object. Контейнер має повертати новий iterator при кожному `iter()`, тому по `list` можна проходити багато разів.[^py314-reference-datamodel-object-iter] Generator сам є своїм iterator: `iter(gen) is gen`, як показано в прикладі.[^py314-library-stdtypes-iterator-types] Тому для повторного проходу треба зберегти дані в `list` або викликати generator function заново. Той самий висновок стосується generator, який завершився винятком: наступний `next()` піднімає `StopIteration`, а не повторює виняток (спостереження у CPython).

**Типові помилки:**
- очікувати, що другий `for` по тому самому generator знову пройде всі елементи;
- зберігати generator в змінній, передавати його в кілька місць і дивуватися порожньому результату після першого споживання;
- плутати iterable (`list`, `range`), по якому можна проходити багато разів, з iterator (generator), який можна пройти один раз.

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
