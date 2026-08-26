---
id: py-funcs-0012
title: "Чому функція може отримати `UnboundLocalError` під час читання глобального `x`, якщо нижче в її тілі є присвоєння `x = ...`?"
description: "Компілятор CPython визначає, що ім'я є локальним, якщо будь-де в тілі функції є операція зв'язування (присвоєння, for, import тощо), і тому всі звертання до цього імені в функції трактуються як до локального."
track: python
section: functions-and-scope
level: middle
type: pitfall
tags: [unboundlocalerror]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
applies_to:
  - product: "CPython"
    version: null
anki:
  export: true
sources:
  - source_id: py314-reference-executionmodel-resolution-of-names
    title: "Python 3.14: Reference/executionmodel"
    url: https://docs.python.org/3.14/reference/executionmodel.html#resolution-of-names
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-faq-programming-why-am-i-getting-an-unboundlocalerror
    title: "Python 3.14: Faq/programming"
    url: https://docs.python.org/3.14/faq/programming.html#why-am-i-getting-an-unboundlocalerror-when-the-variable-has-a-value
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/namespace_and_context_manager.md#L133-L189
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Компілятор CPython визначає, що ім'я є локальним, якщо будь-де в тілі функції є операція зв'язування (присвоєння, `for`, `import` тощо), і тому всі звертання до цього імені в функції трактуються як до локального.**[^py314-reference-executionmodel-resolution-of-names] Якщо читання `x` відбувається до першого присвоєння, змінна ще не має значення – виникає `UnboundLocalError`. Щоб звернутися до глобального `x`, потрібна декларація `global x`.

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
