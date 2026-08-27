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

**`deque` гарантує O(1) append і pop з обох кінців, тоді як `list` вимагає O(n) для `insert(0, v)` та `pop(0)` через зсув елементів у масиві.**[^py314-library-stdtypes] Тому `deque` кращий для черг, ковзних вікон та алгоритмів, де потрібна ефективна робота з обома кінцями. <span class="warn">Водночас `deque` має O(n) доступ до середини за індексом, тому для random access list залишається кращим.</span>

## Detailed explanation

Внутрішньо `deque` – це двозв'язний список блоків фіксованого розміру (кожен блок містить кілька
десятків елементів), а не список окремих вузлів на кожен елемент і не суцільний
масив.[^py314-library-collections] Такий блоковий дизайн дає amortized O(1) для `append`,
`appendleft`, `pop` і `popleft`, бо додавання чи вилучення зазвичай зачіпає лише один блок на краю
структури, без переміщення інших елементів.

`list.append()` теж amortized O(1) завдяки надлишковому виділенню пам'яті в кінці масиву, але
операції з лівого краю – `insert(0, v)` і `pop(0)` – завжди O(n), бо `list` фізично зсуває всі
елементи, щоб зберегти суцільність масиву в пам'яті; блокова структура `deque` цього зсуву не
потребує.

Плата за це – довільний доступ за індексом: `d[i]` у `deque` вимагає проходу від найближчого краю
(лівого чи правого) через блоки, тобто O(n) у гіршому випадку, тоді як `list[i]` – завжди O(1),
бо масив дає прямий offset у пам'яті.

Параметр `maxlen` робить `deque` зручним ring buffer для sliding window: коли довжина досягає
`maxlen`, кожен новий `append` автоматично виштовхує елемент з протилежного краю без явного
виклику `popleft`.

Ще одна практична деталь – `append`/`pop` з протилежних кінців `deque` в CPython атомарні на
рівні GIL, тому для найпростіших producer-consumer сценаріїв між двома потоками `deque` не
потребує додаткового блокування; для `list` така гарантія на операціях з обох кінців не
документована так само явно.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
