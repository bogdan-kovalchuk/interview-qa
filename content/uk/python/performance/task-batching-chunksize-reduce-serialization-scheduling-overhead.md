---
id: py-perf-0013
title: "Як task batching та `chunksize` можуть зменшити serialization і scheduling overhead у process pool, але погіршити load balancing?"
description: "chunksize у ProcessPoolExecutor.map() об'єднує елементи iterable у більші task-и, що зменшує кількість pickle-серіалізацій і IPC-викликів."
track: python
section: performance
level: middle
type: comparison
tags: [chunksize]
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

**`chunksize` у `ProcessPoolExecutor.map()` об'єднує елементи iterable у більші task-и, що зменшує кількість pickle-серіалізацій і IPC-викликів.**[^py314-library-profile] За `chunksize=1` кожен елемент окремо серіалізується та планується – це забезпечує рівномірне завантаження workers, але має високий per-task overhead. Збільшення `chunksize` різко знижує overhead для довгих iterable, проте якщо час виконання елементів відрізняється, деякі workers завершують свої chunk-и швидко й простоюють, поки інші ще обробляють великий chunk. <span class="warn">`chunksize` не впливає на `ThreadPoolExecutor.map()` – там він ігнорується.</span>

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
