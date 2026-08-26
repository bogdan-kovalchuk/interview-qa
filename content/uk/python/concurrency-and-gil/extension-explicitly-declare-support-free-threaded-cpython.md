---
id: py-gil-0011
title: "Як C extension явно позначає підтримку free-threaded CPython 3.14 і що може статися під час import несумісного extension?"
description: "C extension позначає підтримку free-threaded build через слот Py_mod_gil зі значенням Py_MOD_GIL_NOT_USED (multi-phase init) або виклик PyUnstable_Module_SetGIL(module, Py_MOD_GIL_NOT_USED) (single-phase init)."
track: python
section: concurrency-and-gil
level: senior
type: mechanism
tags: []
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
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
---

## Short answer

**C extension позначає підтримку free-threaded build через слот `Py_mod_gil` зі значенням `Py_MOD_GIL_NOT_USED` (multi-phase init) або виклик `PyUnstable_Module_SetGIL(module, Py_MOD_GIL_NOT_USED)` (single-phase init).**[^py314-library-threading] <span class="warn">Якщо extension не декларує підтримку:</span> при import видається warning і GIL автоматично вмикається назад, зводячи нанівець переваги free-threaded build. Для умовної компіляції використовується макрос `Py_GIL_DISABLED`.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
