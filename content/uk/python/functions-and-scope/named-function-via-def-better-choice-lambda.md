---
id: py-funcs-0021
title: "Коли іменована функція через `def` є кращим вибором за `lambda`, навіть якщо обидві можуть реалізувати той самий короткий вираз?"
description: "def кращий, коли потрібне зрозуміле ім'я для traceback, docstring, type annotations або кілька інструкцій у тілі."
track: python
section: functions-and-scope
level: middle
type: comparison
tags: []
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: py314-reference-expressions-lambdas
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#lambdas
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-compound-stmts-function-definitions
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#function-definitions
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/functions.md#L315-L372
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`def` кращий, коли потрібне зрозуміле ім'я для traceback, docstring, type annotations або кілька інструкцій у тілі.**[^py314-reference-expressions-lambdas] Lambda обмежена одним виразом і не підтримує statements чи анотації, а її `__name__` завжди `"<lambda>"`, що ускладнює діагностику. `def` створює function object із повноцінним `__qualname__`, який з'являється в traceback і логах.

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
