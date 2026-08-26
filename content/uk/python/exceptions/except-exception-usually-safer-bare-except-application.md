---
id: py-excpt-0001
title: "Чому `except Exception` зазвичай безпечніший за bare `except` для application-level обробки?"
description: "Bare except перехоплює всі BaseException, включно з SystemExit і KeyboardInterrupt, тоді як except Exception пропускає ці signal-винятки."
track: python
section: exceptions
level: middle
type: comparison
tags: [except-exception]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/exceptions.md#L3-L28
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Bare `except` перехоплює всі `BaseException`, включно з `SystemExit` і `KeyboardInterrupt`, тоді як `except Exception` пропускає ці signal-винятки.**[^py314-tutorial-errors] Класи `SystemExit`, `KeyboardInterrupt` і `GeneratorExit` успадковуються безпосередньо від `BaseException`, а не від `Exception`. Тому `except Exception` дозволяє процесу завершитися через `sys.exit()` або реакцією на Ctrl-C, що критично для graceful shutdown.

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
