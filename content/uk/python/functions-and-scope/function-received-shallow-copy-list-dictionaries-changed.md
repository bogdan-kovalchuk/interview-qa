---
id: py-funcs-0011
title: "Функція отримала shallow copy списку словників і змінила значення у вкладеному словнику. Чому зміна може бути видима викликачу, хоча зовнішній список скопійовано?"
description: "copy.copy (shallow copy) створює новий зовнішній список, але вставляє в нього посилання на ті самі вкладені об'єкти, що й в оригіналі."
track: python
section: functions-and-scope
level: senior
type: practical
tags: []
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: py314-library-copy
    title: "Python 3.14: Library/copy"
    url: https://docs.python.org/3.14/library/copy.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-faq-programming-why-did-changing-list-y-also-change-li
    title: "Python 3.14: Faq/programming"
    url: https://docs.python.org/3.14/faq/programming.html#why-did-changing-list-y-also-change-list-x
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

**`copy.copy` (shallow copy) створює новий зовнішній список, але вставляє в нього посилання на ті самі вкладені об'єкти, що й в оригіналі.**[^py314-library-copy] Тому мутація вкладеного словника через скопійований список змінює той самий об'єкт, на який посилається і оригінал. Щоб повністю ізолювати вкладені структури, потрібен `copy.deepcopy`.

## Detailed explanation

TODO

## Environment

TODO

## Deliverable

TODO

## Acceptance criteria

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
