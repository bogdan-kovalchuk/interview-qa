---
id: py-funcs-0016
title: "Чому всі функції, створені як `[lambda: i for i in range(3)]`, після завершення comprehension повертають те саме значення?"
description: "Усі lambda захоплюють одну й ту саму змінну i за посиланням, а не її значення на момент створення; після циклу i == 2, і кожен виклик повертає 2."
track: python
section: functions-and-scope
level: middle
type: pitfall
tags: [lambda-i-for-i-in-range-3]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
execution:
  language: python
  standard: null
  toolchain:
    name: cpython
    version: "3.14"
  flags: []
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
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/functions.md#L422-L516
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Усі lambda захоплюють одну й ту саму змінну `i` за посиланням, а не її значення на момент створення; після циклу `i == 2`, і кожен виклик повертає `2`.**[^py314-faq-programming-why-do-lambdas-defined-in-a-loop-with] 

```python
funcs = [lambda: i for i in range(3)]
print([f() for f in funcs])  # [2, 2, 2]
```

 Щоб зафіксувати поточне значення, використовують default argument: `lambda i=i: i`.

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
