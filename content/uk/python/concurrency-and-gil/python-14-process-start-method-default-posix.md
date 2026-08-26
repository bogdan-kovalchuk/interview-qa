---
id: py-gil-0021
title: "У Python 3.14 який process start method є default на POSIX і Windows, та коли потрібно явно обрати `spawn`, `fork` чи `forkserver`?"
description: "У Python 3.14 default на POSIX – forkserver, на Windows – spawn."
track: python
section: concurrency-and-gil
level: senior
type: comparison
tags: [spawn, fork, forkserver]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
applies_to:
  - product: "CPython"
    version: "3.14"
anki:
  export: true
sources:
  - source_id: py314-library-threading
    title: "Python 3.14: Library/threading"
    url: https://docs.python.org/3.14/library/threading.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-multiprocessing
    title: "Python 3.14: Library/multiprocessing"
    url: https://docs.python.org/3.14/library/multiprocessing.html
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
  - source_id: py314-howto-free-threading-python
    title: "Python 3.14: Howto/free Threading Python"
    url: https://docs.python.org/3.14/howto/free-threading-python.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-howto-free-threading-extensions
    title: "Python 3.14: Howto/free Threading Extensions"
    url: https://docs.python.org/3.14/howto/free-threading-extensions.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/gil_threads_processes.md#L1274-L1328
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**У Python 3.14 default на POSIX – `forkserver`, на Windows – `spawn`.**[^py314-library-threading] <span class="warn">Зміна POSIX-default з `fork` на `forkserver` сталася саме в 3.14 для уникнення проблем багатопотокового `fork()`.</span> `spawn` – найбезпечніший (новий інтерпретатор), але повільніший; `fork` – швидкий, але небезпечний якщо батьківський процес має threads (може призвести до crash/deadlock); `forkserver` – баланс: один server-процес стартує через `spawn`, подальші fork-и від нього. `fork` слід обирати лише для legacy-коду без threads; `spawn` – коли потрібна максимальна ізоляція.

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
