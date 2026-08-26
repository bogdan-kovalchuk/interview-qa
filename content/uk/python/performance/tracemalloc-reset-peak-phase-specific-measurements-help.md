---
id: py-perf-0010
title: "Як `tracemalloc.reset_peak()` та phase-specific measurements допомагають відрізнити temporary allocation spike від retained memory growth?"
description: "tracemalloc.reset_peak() встановлює поточний розмір як новий маркер peak, не очищаючи trace-и, що дозволяє виміряти peak окремо для кожної фази виконання."
track: python
section: performance
level: senior
type: practical
tags: [tracemalloc-reset-peak]
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

**`tracemalloc.reset_peak()` встановлює поточний розмір як новий маркер peak, не очищаючи trace-и, що дозволяє виміряти peak окремо для кожної фази виконання.**[^py314-library-profile] Викликаємо `reset_peak()` між фазами; потім `get_traced_memory()` повертає `(current, peak)`. Якщо `peak` значно більший за `current` – був temporary spike (пам'ять виділена й звільнена). Якщо `current` стабільно зростає – це retained growth, тобто об'єкти залишаються живими. Snapshot comparison (`Snapshot.compare_to`) додатково показує, де саме з'явилися нові allocation.

## Detailed explanation

TODO

## Environment

TODO

## Deliverable

TODO

## Acceptance criteria

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
