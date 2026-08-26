---
id: py-excpt-0002
title: "Як порядок кількох `except` clauses впливає на досяжність handlers для subclass exceptions?"
description: "Python перевіряє except clauses зверху вниз і спрацьовує перший збіг; якщо parent class стоїть перед child, handler для child стає недосяжним."
track: python
section: exceptions
level: middle
type: mechanism
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/exceptions.md#L29-L64
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Python перевіряє `except` clauses зверху вниз і спрацьовує перший збіг; якщо parent class стоїть перед child, handler для child стає недосяжним.**[^py314-tutorial-errors] Наприклад, `except Exception` перед `except ValueError` перехопить `ValueError` першим, і другий clause ніколи не виконається – interpreter видасть `SyntaxWarning` або `SyntaxError` для таких dead-code handlers. Правильний порядок: від найвужчих (subclass) до найширших (parent).

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
