---
id: py-perf-0007
title: "Чому Big O недостатньо для прогнозу latency без розміру input, constants та memory-access behavior?"
description: "Big O описує лише асимптотичне зростання, відкидаючи constants, які на практичних розмірах можуть переважити різницю класів, і не враховує cache-friendly доступ до пам'яті."
track: python
section: performance
level: senior
type: pitfall
tags: []
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

**Big O описує лише асимптотичне зростання, відкидаючи constants, які на практичних розмірах можуть переважити різницю класів, і не враховує cache-friendly доступ до пам'яті.**[^py314-library-profile] По-перше, на конкретному розмірі `n` алгоритм `O(n log n)` з великим coefficient може бути повільнішим за `O(n²)` з малим. По-друге, contiguous memory layout (наприклад, `list` чи `array`) використовує CPU cache ефективно, тоді як pointer-chasing у `linked list` чи розріджений hash-table дають cache misses, що уповільнює виконання в рази. Тому прогноз latency потребує знати `n`, constants і патерн доступу до пам'яті.

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
