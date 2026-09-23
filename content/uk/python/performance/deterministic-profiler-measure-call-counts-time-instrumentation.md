---
id: py-perf-0001
title: "Як deterministic profiler вимірює call counts та time і чому його instrumentation overhead треба враховувати під час інтерпретації?"
description: "Deterministic profiler (наприклад, cProfile) реєструє кожну подію виклику та повернення функції, фіксуючи ncalls, tottime (час у самому тілі) та cumtime (разом з підфункціями)."
track: python
section: performance
level: middle
type: mechanism
tags: []
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

**Deterministic profiler (наприклад, `cProfile`) реєструє кожну подію виклику та повернення функції, фіксуючи `ncalls`, `tottime` (час у самому тілі) та `cumtime` (разом з підфункціями).**[^py314-library-profile] Instrumentation overhead – затримка між подією та її записом; він накопичується на функціях з великою кількістю викликів і може суттєво спотворити абсолютні значення. `cProfile` (C-розширення) має помірний overhead, чистий Python-модуль `profile` – значно більший. Профілювальник призначений для пошуку гарячих точок, а не для точного бенчмаркінгу.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
