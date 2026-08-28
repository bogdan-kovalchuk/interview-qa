---
id: py-gil-0009
title: "Що означає free-threaded build CPython 3.14 і як він співіснує з GIL-enabled build?"
description: "Free-threaded build – це окрема конфігурація CPython (з Python 3.13) з вимкненим GIL, що дозволяє threads виконуватися справжньою паралельністю на кількох CPU cores."
track: python
section: concurrency-and-gil
level: middle
type: comparison
tags: []
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  en: 2
applies_to:
  - product: "CPython free-threaded build"
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/gil_threads_processes.md#L689-L849
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Free-threaded build – це окрема конфігурація CPython (з Python 3.13) з вимкненим GIL, що дозволяє threads виконуватися справжньою паралельністю на кількох CPU cores.**[^py314-library-threading] Це не runtime-перемикач, а окремий білд (configure `--disable-gil`). Визначається через `sys._is_gil_enabled()` (повертає `False`) або рядок "free-threading build" у `sys.version`. Використовує mimalloc замість pymalloc, biased reference counting; single-threaded overhead ~1–8%.

## Detailed explanation

Free-threaded build - окрема конфігурація CPython, яка збирається з прапорцем `--disable-gil` і в
якій глобальний interpreter lock вимкнений на рівні самого interpreter, а не просто не
використовується в конкретному коді.[^py314-howto-free-threading-python]

Ця конфігурація не замінює GIL-enabled build, а існує паралельно з ним: обидві збираються з одного
вихідного дерева CPython, але розповсюджуються як окремі бінарні пакети з різним тегом ABI
(наприклад, `cp314` для звичайного build і `cp314t` для free-threaded, де `t` означає threading).
Інструмент встановлення пакетів обирає wheel за тегом інтерпретатора; C extension, зібраний під
звичайний ABI, несумісний із free-threaded build і потребує окремої збірки.[^py314-howto-free-threading-extensions]

Визначити, на якому build виконується код, можна двома способами:

```python
import sys

print(sys.version)            # contains "free-threading build" on that build
print(sys._is_gil_enabled())  # False on free-threaded build, unless re-enabled
```

`sys._is_gil_enabled()` може повернути `True` навіть на free-threaded build, якщо GIL був вимкнений
явно (`PYTHON_GIL=1`) або автоматично увімкнений через несумісний C extension.

Free-threaded build змінює й внутрішню memory-модель: замість pymalloc використовується allocator
mimalloc, а reference counting стає biased - кожен об'єкт має окремі поля для лічильника власного
(owning) потоку і для спільного (shared) лічильника, що дозволяє уникнути atomic-операцій на
швидкому шляху, коли об'єктом користується лише один потік. Ціна цього - single-threaded overhead
приблизно 1-8% порівняно зі звичайним build.

**На що зважати при виборі:**
- екосистема бібліотек (особливо C extensions) ще не повністю сумісна з free-threaded ABI;
- потрібен окремий деплой - відповідний wheel tag, а не просто прапорець запуску;
- виграш з'являється лише для CPU-bound коду на кількох threads; для I/O-bound навантаження різниця
  мінімальна.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
