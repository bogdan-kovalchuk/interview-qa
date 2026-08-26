---
id: py-funcs-0004
title: "Як Python зв’яже аргументи у виклику `f(1, 2, 3, b=4, x=5)` із параметрами `def f(a, *args, b=0, **kwargs): ...`?"
description: "a = 1, args = (2, 3), b = 4, kwargs = {'x': 5}."
track: python
section: functions-and-scope
level: middle
type: mechanism
tags: [f-1-2-3-b-4-x-5, def-f-a-args-b-0-kwargs]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: py314-reference-expressions-calls
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#calls
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/functions.md#L35-L93
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`a = 1`, `args = (2, 3)`, `b = 4`, `kwargs = {'x': 5}`.**[^py314-reference-expressions-calls] Перший позиційний аргумент заповнює параметр `a`. Наступні позиційні `2, 3` не мають відповідних параметрів до `*`, тому збираються в `*args`. Keyword `b=4` збігається з keyword-only параметром `b`. Keyword `x=5` не збігається з жодним іменованим параметром і потрапляє до `**kwargs`.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
