---
id: py-coll-0023
title: "Коли `collections.deque` кращий за list для роботи з обома кінцями послідовності?"
description: "deque гарантує O(1) append і pop з обох кінців, тоді як list вимагає O(n) для insert(0, v) та pop(0) через зсув елементів у масиві."
track: python
section: collections
level: middle
type: comparison
tags: [collections-deque]
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

**`deque` гарантує O(1) append і pop з обох кінців, тоді як `list` вимагає O(n) для `insert(0, v)` та `pop(0)` через зсув елементів у масиві.**[^py314-library-stdtypes] Тому `deque` кращий для черг, ковзних вікон та алгоритмів, де потрібна ефективна робота з обома кінцями. <span class="warn">Водночас `deque` має O(n) доступ до середини за індексом, тому для random access list залишається кращим.</span>

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
