---
id: py-funcs-0023
title: "Чи змінюють type annotations runtime-семантику виклику звичайної Python-функції та чи перевіряє інтерпретатор типи аргументів автоматично?"
description: "Ні: type annotations не змінюють runtime-семантику виклику, і інтерпретатор НЕ перевіряє типи аргументів автоматично."
track: python
section: functions-and-scope
level: middle
type: pitfall
tags: []
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: py314-reference-compound-stmts-annotations
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#annotations
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-typing
    title: "Python 3.14: Library/typing"
    url: https://docs.python.org/3.14/library/typing.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/data_types.md#L610-L648
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Ні: type annotations не змінюють runtime-семантику виклику, і інтерпретатор НЕ перевіряє типи аргументів автоматично.**[^py314-reference-compound-stmts-annotations] Анотації – це метадані, які зберігаються у функції (через `__annotate__`/`__annotations__` у Python 3.14) і доступні для інспекції, але не впливають на binding аргументів чи перевірку під час виклику. Статичну перевірку виконують зовнішні інструменти (mypy, pyright), а runtime-валідація потребує бібліотек на кшталт pydantic або beartype.<br><span class="warn">Поширена помилка:</span> розробники зі статично типованих мов можуть очікувати автоматичну перевірку типів – у Python її немає.

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
