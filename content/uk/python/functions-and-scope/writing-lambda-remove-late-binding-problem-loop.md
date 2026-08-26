---
id: py-funcs-0017
title: "Чому запис `lambda i=i: i` усуває late-binding проблему в циклі, хоча default arguments самі можуть бути джерелом помилок?"
description: "Default arguments обчислюються один раз – у момент виконання def/lambda, тому i=i зберігає поточне значення i як локальний параметр кожної lambda."
track: python
section: functions-and-scope
level: middle
type: mechanism
tags: [lambda-i-i-i]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: py314-faq-programming-why-do-lambdas-defined-in-a-loop-with
    title: "Python 3.14: Faq/programming"
    url: https://docs.python.org/3.14/faq/programming.html#why-do-lambdas-defined-in-a-loop-with-different-values-all-return-the-same-result
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/functions.md#L422-L516
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Default arguments обчислюються один раз – у момент виконання `def`/`lambda`, тому `i=i` зберігає поточне значення `i` як локальний параметр кожної lambda.**[^py314-faq-programming-why-do-lambdas-defined-in-a-loop-with] Кожна lambda отримує власний параметр `i` з фіксованим значенням, і виклик `f()` повертає саме його. Ризик: якщо default – мутабельний об'єкт (наприклад, `[]`), його зміна в одному виклику вплине на всі наступні.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
