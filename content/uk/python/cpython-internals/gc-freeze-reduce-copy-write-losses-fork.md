---
id: py-cpyint-0016
title: "Коли `gc.freeze()` може зменшити copy-on-write втрати перед `fork()` і які умови потрібні для цього pattern?"
description: "gc.freeze() переносить усі поточні об'єкти під контролем GC у permanent generation, де вони ігноруються подальшими колекціями – це запобігає модифікації gc_refs довгоживучих об'єктів у child після fork(), зменшуючи..."
track: python
section: cpython-internals
level: senior
type: practical
tags: [gc-freeze, fork]
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
  - source_id: py314-library-dis
    title: "Python 3.14: Library/dis"
    url: https://docs.python.org/3.14/library/dis.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-gc
    title: "Python 3.14: Library/gc"
    url: https://docs.python.org/3.14/library/gc.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-c-api-memory
    title: "Python 3.14: C Api/memory"
    url: https://docs.python.org/3.14/c-api/memory.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-sys
    title: "Python 3.14: Library/sys"
    url: https://docs.python.org/3.14/library/sys.html
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
  - source_id: py314-howto-free-threading-python
    title: "Python 3.14: Howto/free Threading Python"
    url: https://docs.python.org/3.14/howto/free-threading-python.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-datamodel-traceback-objects
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#traceback-objects
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
---

## Short answer

**`gc.freeze()` переносить усі поточні об'єкти під контролем GC у permanent generation, де вони ігноруються подальшими колекціями – це запобігає модифікації `gc_refs` довгоживучих об'єктів у child після `fork()`, зменшуючи copy-on-write.**[^py314-library-dis] Рекомендований workflow: (1) `gc.disable()` на початку parent; (2) `gc.freeze()` безпосередньо перед `fork()`; (3) `gc.enable()` на початку child. Умови: заморожені об'єкти мають бути дійсно довгоживучими й незмінними; child не повинен модифікувати ці об'єкти інакше CoW все одно станеться. Pattern ефективний для pre-fork web workers (gunicorn, uwsgi).

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
