---
id: py-gil-0019
title: "Як вибрати між `ThreadPoolExecutor` та `ProcessPoolExecutor` за workload, data-transfer cost і failure model?"
description: "ThreadPoolExecutor – для I/O-bound задач з мінімальним overhead (спільна пам'ять, без серіалізації); ProcessPoolExecutor – для CPU-bound pure-Python задач, де потрібен обхід GIL."
track: python
section: concurrency-and-gil
level: middle
type: comparison
tags: [threadpoolexecutor, processpoolexecutor]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/gil_threads_processes.md#L1344-L1416
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`ThreadPoolExecutor` – для I/O-bound задач з мінімальним overhead (спільна пам'ять, без серіалізації); `ProcessPoolExecutor` – для CPU-bound pure-Python задач, де потрібен обхід GIL.**[^py314-library-threading] Data-transfer cost: threads ділять пам'ять, processes вимагають pickle-серіалізації аргументів і результатів через pipes. Failure model: `BrokenProcessPool` виникає при crash worker-процесу й робить executor непридатним; у threads failure одного worker менш руйнівний. Для CPU-bound у free-threaded CPython (3.13+) threads також можуть дати паралелізм без process overhead.

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
