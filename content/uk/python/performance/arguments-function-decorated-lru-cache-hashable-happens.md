---
id: py-perf-0011
title: "Чому arguments для function з `lru_cache` мають бути hashable і що станеться, якщо передати `list` чи `dict`?"
description: "lru_cache зберігає результати у внутрішньому dict, де ключем є кортеж аргументів виклику, тому всі positional і keyword arguments мають бути hashable."
track: python
section: performance
level: middle
type: pitfall
tags: [lru-cache, list, dict]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: py314-library-profile
    title: "Python 3.14: Library/profile"
    url: https://docs.python.org/3.14/library/profile.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-timeit
    title: "Python 3.14: Library/timeit"
    url: https://docs.python.org/3.14/library/timeit.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-tracemalloc
    title: "Python 3.14: Library/tracemalloc"
    url: https://docs.python.org/3.14/library/tracemalloc.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-concurrent-futures
    title: "Python 3.14: Library/concurrent.futures"
    url: https://docs.python.org/3.14/library/concurrent.futures.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-faq-programming-performance
    title: "Python 3.14: Faq/programming"
    url: https://docs.python.org/3.14/faq/programming.html#performance
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-functools-functools-lru-cache
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html#functools.lru_cache
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-stdtypes-common-sequence-operations
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html#common-sequence-operations
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
---

## Short answer

**`lru_cache` зберігає результати у внутрішньому dict, де ключем є кортеж аргументів виклику, тому всі positional і keyword arguments мають бути hashable.**[^py314-library-profile] Якщо передати `list` або `dict`, Python підніме `TypeError: unhashable type`, бо ці типи не реалізують `__hash__`. Обхідний шлях – перетворити аргумент на `tuple(...)` або `frozenset(...)` перед викликом, або використати `functools.cache` лише коли аргументи гарантовано immutable.

## Detailed explanation

TODO

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
