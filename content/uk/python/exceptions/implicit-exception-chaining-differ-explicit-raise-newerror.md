---
id: py-excpt-0007
title: "Чим implicit exception chaining відрізняється від явного `raise NewError(...) from original`?"
description: "Implicit chaining автоматично встановлює __context__, коли exception виникає всередині except-блоку; явний from встановлює __cause__ і демонструє прямий причинний зв'язок."
track: python
section: exceptions
level: middle
type: comparison
tags: [raise-newerror-from-original]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/exceptions.md#L200-L221
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Implicit chaining автоматично встановлює `__context__`, коли exception виникає всередині `except`-блоку; явний `from` встановлює `__cause__` і демонструє прямий причинний зв'язок.**[^py314-tutorial-errors] Implicit показується як «During handling of the above exception, another exception occurred», а явний – як «The above exception was the direct cause of the following exception». Встановлення `__cause__` автоматично ставить `__suppress_context__ = True`, тому traceback показує `__cause__`, а не `__context__`.

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
