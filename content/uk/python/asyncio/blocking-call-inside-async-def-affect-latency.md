---
id: py-async-0007
title: "Як один blocking call в `async def` впливає на latency всіх інших Tasks у тому самому loop?"
description: "Будь-який синхронний blocking call (наприклад, time.sleep(), I/O файлів, CPU-обчислення) зупиняє event loop на весь час виконання, затримуючи всі інші Tasks і I/O-події."
track: python
section: asyncio
level: senior
type: practical
tags: [async-def]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/async.md#L1222-L1247
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Будь-який синхронний blocking call (наприклад, `time.sleep()`, I/O файлів, CPU-обчислення) зупиняє event loop на весь час виконання, затримуючи всі інші Tasks і I/O-події.**[^py314-library-asyncio-task] Рішення – винести blocking операцію в окремий thread або process через `asyncio.to_thread()` або `loop.run_in_executor()`. Debug mode логує callback-и, що виконуються довше `slow_callback_duration` (за замовчуванням 100 мс).

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
