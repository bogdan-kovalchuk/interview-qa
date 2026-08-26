---
id: py-funcs-0015
title: "Чому ім’я, визначене в тілі класу, не стає звичайним enclosing lexical scope для коду методу цього класу?"
description: "Scope імен, визначених у class block, обмежений самим class block і не поширюється на методи класу."
track: python
section: functions-and-scope
level: senior
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
  - source_id: py314-reference-executionmodel-resolution-of-names
    title: "Python 3.14: Reference/executionmodel"
    url: https://docs.python.org/3.14/reference/executionmodel.html#resolution-of-names
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/namespace_and_context_manager.md#L99-L132
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Scope імен, визначених у class block, обмежений самим class block і не поширюється на методи класу.**[^py314-reference-executionmodel-resolution-of-names] Методи не можуть звертатися до атрибутів класу через звичайний lexical lookup – потрібний явний доступ через `self.attr` або `ClassName.attr`. Виняток: annotation scopes (type parameters, annotations) мають доступ до namespace класу.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
