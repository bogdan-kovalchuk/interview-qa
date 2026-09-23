---
id: py-perf-0019
title: "Чому один positive `tracemalloc` snapshot diff після workload ще не доводить leak і як repeated steady-state measurements відрізняють cache growth від unbounded retention?"
description: "tracemalloc показує лише Python-аллокації між двома snapshots; single diff може відображати legitimate cache growth, lazy initialization або peak usage, а не leak."
track: python
section: performance
level: middle
type: pitfall
tags: [tracemalloc]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
applies_to:
  - product: "CPython"
    version: null
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

**`tracemalloc` показує лише Python-аллокації між двома snapshots; single diff може відображати legitimate cache growth, lazy initialization або peak usage, а не leak.**[^py314-library-profile] Щоб відрізнити bounded cache від unbounded retention, потрібно: (1) запустити workload до steady state, (2) зробити кілька snapshot-ів з інтервалами, (3) перевірити, що `size_diff` між пізніми snapshots стабілізується (≈ 0). Якщо ріст продовжується лінійно після багатьох ітерацій – це leak; якщо вийшов на плато – це bounded cache. <span class="warn">`tracemalloc` не бачить аллокації напряму через C `malloc`, тому «чистий» snapshot diff не гарантує відсутність leak на рівні C extension.</span>

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
