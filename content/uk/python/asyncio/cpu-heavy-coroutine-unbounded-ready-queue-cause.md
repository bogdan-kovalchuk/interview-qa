---
id: py-async-0008
title: "Як CPU-heavy coroutine або необмежена ready queue може створити starvation навіть у cooperative scheduler?"
description: "Навіть у cooperative моделі coroutine з довгим обчисленням між await-точками утримує event-loop thread і не дає виконуватися іншим Tasks, створюючи starvation."
track: python
section: asyncio
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/async.md#L1305-L1325
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Навіть у cooperative моделі coroutine з довгим обчисленням між `await`-точками утримує event-loop thread і не дає виконуватися іншим Tasks, створюючи starvation.**[^py314-library-asyncio-task] Рішення: розбивати довгі обчислення на фрагменти з `await asyncio.sleep(0)` між ними, або виносити CPU-heavy роботу в `ProcessPoolExecutor` через `run_in_executor()`. `asyncio.sleep(0)` явно поступається керуванням, дозволяючи loop обробити інші ready callbacks.

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
