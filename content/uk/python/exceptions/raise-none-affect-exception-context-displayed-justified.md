---
id: py-excpt-0009
title: "Як `raise ... from None` впливає на відображення exception context і коли це виправдано?"
description: "raise NewError(...) from None встановлює __cause__ = None і __suppress_context__ = True, тому traceback приховує implicit __context__."
track: python
section: exceptions
level: senior
type: practical
tags: [raise-from-none]
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

**`raise NewError(...) from None` встановлює `__cause__ = None` і `__suppress_context__ = True`, тому traceback приховує implicit `__context__`.**[^py314-tutorial-errors] Оригінальний exception залишається доступним через атрибут `__context__`, але не відображається. Виправдано, коли внутрішній exception є деталлю реалізації і не несе корисної інформації для користувача бібліотеки – наприклад, при трансформації низькорівневого exception у зрозумілий API-level exception.

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
