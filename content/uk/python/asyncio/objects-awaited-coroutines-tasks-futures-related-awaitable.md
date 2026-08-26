---
id: py-async-0002
title: "Які objects можна `await` і як coroutine, Task та Future пов’язані через awaitable protocol?"
description: "await приймає будь-який awaitable-об'єкт – coroutine, Task або Future, – тобто об'єкт з методом __await__."
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/async.md#L135-L203
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`await` приймає будь-який awaitable-об'єкт – coroutine, Task або Future, – тобто об'єкт з методом `__await__`.**[^py314-library-asyncio-task] Coroutine – це «сирий» об'єкт з `async def`. Task – обгортка над coroutine, яку event loop виконує concurrently. Future – low-level примітив, що представляє майбутній результат; Task є підкласом Future. Усі троє реалізують awaitable protocol, тому взаємозамінні в `await`.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
