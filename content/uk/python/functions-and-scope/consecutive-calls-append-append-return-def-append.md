---
id: py-funcs-0006
title: "Що повернуть два послідовні виклики `append(1)` і `append(2)` для `def append(x, items=[]): items.append(x); return items`, і чому?"
description: "append(1) повертає [1], append(2) повертає [1, 2] – обидва виклики працюють з одним і тим самим списком."
track: python
section: functions-and-scope
level: middle
type: pitfall
tags: [append-1, append-2, def-append-x-items-items-append-x-return-items]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: py314-reference-compound-stmts-function-definitions
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#function-definitions
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-faq-programming-why-are-default-values-shared-between
    title: "Python 3.14: Faq/programming"
    url: https://docs.python.org/3.14/faq/programming.html#why-are-default-values-shared-between-objects
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/functions.md#L94-L138
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`append(1)` повертає `[1]`, `append(2)` повертає `[1, 2]` – обидва виклики працюють з одним і тим самим списком.**[^py314-reference-compound-stmts-function-definitions] Default-об'єкт `[]` створюється один раз під час виконання `def`, а не при кожному виклику. Параметр `items` вказує на цей єдиний об'єкт, тому `.append()` накопичує елементи між викликами. <span class="warn">Це класична пастка mutable default.</span> Правильний патерн – використовувати `items=None` і створювати новий список усередині функції.

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
