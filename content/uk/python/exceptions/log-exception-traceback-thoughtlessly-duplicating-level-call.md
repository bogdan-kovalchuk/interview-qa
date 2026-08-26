---
id: py-excpt-0016
title: "Як залогувати exception із traceback, не дублюючи його бездумно на кожному рівні call stack?"
description: "Логувати exception із traceback треба на одному рівні – зазвичай найнижчому, де exception вперше перехоплено, – використовуючи logger.exception() або logger.error(..., exc_info=True)."
track: python
section: exceptions
level: senior
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
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/exceptions.md#L488-L592
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Логувати exception із traceback треба на одному рівні – зазвичай найнижчому, де exception вперше перехоплено, – використовуючи `logger.exception()` або `logger.error(..., exc_info=True)`.**[^py314-tutorial-errors] На вищих рівнях або не логувати traceback, або додавати лише контекст без `exc_info`. `logger.exception()` автоматично бере traceback з `sys.exc_info()`, тому повторний виклик на кожному рівні створить дублікати в логах. Для передачі інформації між рівнями краще використовувати exception chaining (`raise ... from`).

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
