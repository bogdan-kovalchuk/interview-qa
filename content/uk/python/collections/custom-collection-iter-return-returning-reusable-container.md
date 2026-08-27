---
id: py-coll-0018
title: "Що повинен повертати `__iter__` custom collection і чому повернення самого reusable container зазвичай некоректне?"
description: "__iter__ має повертати новий iterator (об'єкт з __next__) при кожному виклику, щоб незалежні ітерації не конфліктували."
track: python
section: collections
level: senior
type: mechanism
tags: [iter]
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  en: 2
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

**`__iter__` має повертати новий iterator (об'єкт з `__next__`) при кожному виклику, щоб незалежні ітерації не конфліктували.**[^py314-library-stdtypes] Якщо container повертає `self`, він стає iterator із одним спільним станом: після першого `list(obj)` iterator вичерпується, і друга ітерація дасть порожній результат. Правильна реалізація: `def __iter__(self): return iter(self._data)` – створює окремий iterator для кожного виклику.

## Detailed explanation

Протокол ітерації розрізняє дві різні ролі: iterable (об'єкт із `__iter__`) і iterator (об'єкт із
`__iter__` та `__next__`, де стан обходу – позиція, стек, індекс – зберігається саме в ньому).
Iterator за конвенцією повертає `self` зі свого власного `__iter__` – це нормально, бо iterator
одноразовий за визначенням. Проблема виникає, коли контейнер, що призначений для повторного
використання, сам відіграє роль iterator: тоді весь стан обходу – наприклад, поточний індекс –
живе в самому об'єкті контейнера, а не в окремій сутності.[^py314-library-stdtypes]

Найпомітніший симптом – вкладені цикли по одному й тому самому об'єкту: `for x in obj: for y in
obj: ...` зіпсує зовнішній цикл, бо внутрішній цикл посуне той самий спільний вказівник позиції, і
після виходу з внутрішнього циклу `obj` вже вичерпаний для зовнішнього.

Найпростіший спосіб гарантувати новий iterator при кожному виклику – написати `__iter__` як
генераторну функцію: `def __iter__(self): yield from self._data`. Виклик генераторної функції
завжди створює новий обʼєкт-генератор із власним фреймом виконання, навіть якщо викликати цю саму
функцію багато разів підряд на одному й тому самому `self`, тому конфлікту стану не виникає.

Делегування через `iter(self._data)` працює аналогічно – воно щоразу створює новий iterator над
внутрішньою структурою даних, а не повторно використовує один і той самий обʼєкт. Це критично для
структур, що підтримують паралельні незалежні обходи, наприклад дерево з кількома одночасними
DFS-проходами.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
