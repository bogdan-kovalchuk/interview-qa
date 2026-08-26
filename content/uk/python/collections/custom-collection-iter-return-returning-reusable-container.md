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
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
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

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
