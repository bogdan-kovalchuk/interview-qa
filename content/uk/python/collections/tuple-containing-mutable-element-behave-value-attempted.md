---
id: py-coll-0005
title: "Як tuple, що містить mutable element, поводиться під час спроби `t[0] += value`, і чому mutation може статися до `TypeError`?"
description: "+= для mutable елемента всередині tuple спочатку виконує in-place mutation, а потім намагається присвоїти результат назад у tuple – присвоєння викликає TypeError, але мутація вже відбулася."
track: python
section: collections
level: senior
type: pitfall
tags: [t-0-value, typeerror]
status: published
updated: 2026-09-27
content_revision: 2
reconciled_with:
  en: 2
execution:
  language: python
  standard: null
  toolchain:
    name: cpython
    version: "3.14.7"
  flags: []
anki:
  export: true
sources:
  - source_id: py314-library-stdtypes
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-collections
    title: "Python 3.14: Library/collections"
    url: https://docs.python.org/3.14/library/collections.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-howto-sorting
    title: "Python 3.14: Howto/sorting"
    url: https://docs.python.org/3.14/howto/sorting.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
---

## Short answer

**`+=` для mutable елемента всередині tuple спочатку виконує in-place mutation, а потім намагається присвоїти результат назад у tuple – присвоєння викликає `TypeError`, але мутація вже відбулася.**[^py314-library-stdtypes]

```text
t = ([1, 2], [3])
t[0] += [3]    # TypeError, but t[0] is already [1, 2, 3]
```

Вираз `t[0] += [3]` фактично виконує `t[0] = t[0].__iadd__([3])`: `__iadd__` модифікує список, а потім `tuple.__setitem__` відхиляє присвоєння.

## Detailed explanation

Парадокс виразу `t[0] += [3]` над кортежем виникає через те, що оператор доповненого присвоєння (augmented assignment) поєднує дві окремі операції: in-place мутацію самого об'єкта та наступне присвоєння результату назад у контейнер.[^py314-library-stdtypes]

На рівні байт-коду CPython конструкція `target[index] += value` транслюється в послідовність інструкцій, яка спочатку завантажує об'єкт зі слота контейнера, виконує над ним операцію `INPLACE_ADD` (викликаючи метод `__iadd__`), а потім намагається зберегти повернене значення назад через `STORE_SUBSCR`.[^py314-library-stdtypes] Для об'єктів типу `list` метод `__iadd__` змінює список на місці (еквівалентно `extend()`) і повертає посилання на той самий список `self`. Мутація успішно завершується, однак наступний крок виконання інструкції `STORE_SUBSCR` викликає `tuple.__setitem__`, який завжди генерує виняток `TypeError: 'tuple' object does not support item assignment`, оскільки кортежі є незмінними.

Така поведінка порушує транзакційність та гарантію atomic execution: операція зазнає аварійної невдачі з винятком, але залишає після себе частково змінений стан системи. Це є прямим архітектурним компромісом у дизайні Python: мова не застосовує механізмів відкату (rollback) при виникненні винятків у складних інструкціях. Якщо структура вимагає мутацій, слід використовувати `list` або спеціалізовані контейнери замість кортежів зі змінюваними елементами, або викликати явний метод `t[0].extend(...)`, який не намагається виконувати присвоєння у слот кортежу.

Невдале доповнене присвоєння та неатомарна мутація:

```python
# 1. Setup a tuple holding a mutable list:
t = ([1, 2], [3])

# 2. Augmented assignment causes an in-place mutation followed by TypeError:
try:
    t[0] += [3]
except TypeError as exc:
    print(exc)  # 'tuple' object does not support item assignment

# The list inside the tuple was mutated before the exception was raised:
print(t[0])  # [1, 2, 3]

# 3. Explicit method call mutates without attempting tuple item assignment:
t[1].extend([4])
print(t[1])  # [3, 4]
```

**Архітектурні наслідки та типові помилки:**
- припущення, що падіння операції з винятком гарантує збереження попереднього стану даних (відсутність rollback у Python);
- збереження змінюваних структур (`list`, `dict`) всередині `tuple`, що порушує гарантію незмінності кортежу та робить його негешованим;
- плутанина між методом мутації `lst.extend(...)`, який не чіпає слот кортежу, та оператором `+=`, який обов'язково намагається записати результат назад;
- перехоплення `TypeError` навколо `+=` як способу «безпечної» мутації, що є грубим антипатерном і заплутує контроль потоку виконання.

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
