---
id: py-excpt-0008
title: "Коли використовують bare `raise` усередині handler і чому `raise exc` може змінити traceback presentation?"
description: "Bare raise всередині except повторно кидає той самий exception object без зміни traceback; raise exc додає поточний frame до traceback."
track: python
section: exceptions
level: middle
type: mechanism
tags: [raise-exc]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: py314-tutorial-errors
    title: "Python 3.14: Tutorial/errors"
    url: https://docs.python.org/3.14/tutorial/errors.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-exceptions
    title: "Python 3.14: Library/exceptions"
    url: https://docs.python.org/3.14/library/exceptions.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-compound-stmts-the-try-statement
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#the-try-statement
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
---

## Short answer

**Bare `raise` всередині `except` повторно кидає той самий exception object без зміни traceback; `raise exc` додає поточний frame до traceback.**[^py314-tutorial-errors] Bare `raise` зберігає оригінальний traceback, що важливо для діагностики. `raise exc` (навіть того самого об'єкта) інтерпретується як новий raise і додає frame поточної позиції, що може заплутати при аналізі стеку викликів.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
