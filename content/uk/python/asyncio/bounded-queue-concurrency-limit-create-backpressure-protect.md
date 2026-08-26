---
id: py-async-0024
title: "Як bounded queue та concurrency limit створюють backpressure і захищають async service від необмеженого fan-out?"
description: "Bounded asyncio.Queue(maxsize=N) зупиняє producer через await put(), коли черга заповнена, а Semaphore(limit) обмежує кількість одночасних операцій – разом вони не дають service накопичувати нескінченну кількість..."
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

**Bounded `asyncio.Queue(maxsize=N)` зупиняє producer через `await put()`, коли черга заповнена, а `Semaphore(limit)` обмежує кількість одночасних операцій – разом вони не дають service накопичувати нескінченну кількість pending завдань.**[^py314-library-asyncio-task] Producer, що викликає `await queue.put(item)`, призупиняється доки consumer не звільнить слот через `get()` – це природний backpressure. `Semaphore` доповнює це, обмежуючи одночасні зовнішні виклики (наприклад, HTTP-запити до БД): після вичерпання лічильника нові Task чекають `acquire()`. Без цих механізмів швидкий producer або burst вхідних запитів може вичерпати пам'ять або перевантажити downstream.

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
