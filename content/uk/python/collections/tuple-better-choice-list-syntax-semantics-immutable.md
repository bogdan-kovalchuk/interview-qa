---
id: py-coll-0001
title: "Коли tuple є кращим вибором за list не через syntax, а через семантику незмінної структури даних?"
description: "Tuple варто обирати, коли дані логічно є незмінним записом (record) – його immutability сигналізує про намір і дозволяє використовувати tuple як dict key або елемент set."
track: python
section: collections
level: middle
type: comparison
tags: []
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

**Tuple варто обирати, коли дані логічно є незмінним записом (record) – його immutability сигналізує про намір і дозволяє використовувати tuple як dict key або елемент set.**[^py314-library-stdtypes] Наприклад, координати `(x, y)`, row tuple з БД, або складений ключ словника. <span class="warn">Якщо всередині tuple є mutable об'єкт (наприклад `list`), його вміст можна змінити – сам tuple залишається тим самим об'єктом з тим самим `id`.</span>

## Detailed explanation

TODO

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
