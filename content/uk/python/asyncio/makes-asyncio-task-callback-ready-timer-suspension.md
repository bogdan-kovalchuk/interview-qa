---
id: py-async-0005
title: "Що робить asyncio Task або callback ready після I/O, timer чи suspension point і яких fairness та exact-order guarantees application code не має припускати?"
description: "Event loop виконує готові callback у порядку FIFO для call_soon, але порядок timer-callbackів з однаковим часом є невизначеним, а строгих fairness-гарантій між Tasks немає."
track: python
section: asyncio
level: middle
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
  - source_id: py314-library-asyncio-task
    title: "Python 3.14: Library/asyncio Task"
    url: https://docs.python.org/3.14/library/asyncio-task.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-asyncio-eventloop
    title: "Python 3.14: Library/asyncio Eventloop"
    url: https://docs.python.org/3.14/library/asyncio-eventloop.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-asyncio-dev
    title: "Python 3.14: Library/asyncio Dev"
    url: https://docs.python.org/3.14/library/asyncio-dev.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/async.md#L204-L259
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Event loop виконує готові callback у порядку FIFO для `call_soon`, але порядок timer-callbackів з однаковим часом є невизначеним, а строгих fairness-гарантій між Tasks немає.**[^py314-library-asyncio-task] Коли I/O завершується або спливає timer, loop додає відповідний callback у ready-чергу. Callbacks, зареєстровані через `call_soon`, викликаються в порядку реєстрації. Проте для `call_later` / `call_at` з однаковим timestamp порядок не гарантовано. Task, яка не поступається керуванням через `await`, може відкладати інші Tasks на невизначений час.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
