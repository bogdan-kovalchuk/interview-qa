---
id: py-async-0009
title: "Як `asyncio.TaskGroup` гарантує, що створені в ньому Tasks завершаться до виходу з context manager?"
description: "TaskGroup – асинхронний context manager, який у __aexit__ неявно очікує завершення всіх Tasks, створених через tg.create_task(), і не вийде з блоку, поки вони не завершаться."
track: python
section: asyncio
level: middle
type: mechanism
tags: [asyncio-taskgroup]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/async.md#L746-L791
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`TaskGroup` – асинхронний context manager, який у `__aexit__` неявно очікує завершення всіх Tasks, створених через `tg.create_task()`, і не вийде з блоку, поки вони не завершаться.**[^py314-library-asyncio-task] Tasks створюються лише всередині `async with`-блоку. Після виходу з блоку (нормально чи через exception) `TaskGroup` чекає завершення всіх дочірніх Tasks, забезпечуючи structured concurrency.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
