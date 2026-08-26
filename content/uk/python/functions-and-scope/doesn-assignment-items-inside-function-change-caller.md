---
id: py-funcs-0009
title: "Чому присвоєння `items = []` усередині функції не змінює список викликача, а `items.append(value)` може його змінити?"
description: "items = [] створює нове локальне зв'язування імені, тоді як items.append(value) змінює той самий об'єкт, на який посилаються і локальний параметр, і змінна викликача."
track: python
section: functions-and-scope
level: middle
type: comparison
tags: [items, items-append-value]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: py314-faq-programming-how-do-i-write-a-function-with-output
    title: "Python 3.14: Faq/programming"
    url: https://docs.python.org/3.14/faq/programming.html#how-do-i-write-a-function-with-output-parameters-call-by-reference
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/functions.md#L373-L421
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`items = []` створює нове локальне зв'язування імені, тоді як `items.append(value)` змінює той самий об'єкт, на який посилаються і локальний параметр, і змінна викликача.**[^py314-faq-programming-how-do-i-write-a-function-with-output] Присвоєння переприв'язує локальне ім'я `items` до нового об'єкта, не впливаючи на оригінал. Метод `.append()` модифікує об'єкт за посиланням – оскільки викликач і функція мають посилання на один список, зміна видима обом.

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
