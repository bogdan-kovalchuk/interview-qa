---
id: py-perf-0017
title: "Новий variant обробки даних лише на 2% швидший у representative benchmark, але суттєво складніший: як обґрунтувати вибір за latency budget і maintenance cost?"
description: "Якщо 2% покращення не наближає систему до latency budget і не змінює масштабної здатності, складніший variant не вартий adoption – maintenance cost перевищує benefit."
track: python
section: performance
level: middle
type: practical
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

**Якщо 2% покращення не наближає систему до latency budget і не змінює масштабної здатності, складніший variant не вартий adoption – maintenance cost перевищує benefit.**[^py314-library-profile] Критерії прийняття: (1) чи наближає optimization до SLO/latency target, (2) чи змінюється max throughput на рівні, що відкладає необхідність масштабування, (3) чи зростає складність читання/тестування/налагодження. <span class="warn">Без чіткого latency budget «2% швидше» – це optimization без business justification, яка додає defect risk без вимірного виграшу.</span> Профілювання через `timeit` та `profile` має показувати, де саме досягнуто покращення, щоб оцінити його стійкість на різних даних.

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
