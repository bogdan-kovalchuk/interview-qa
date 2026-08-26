---
id: py-async-0015
title: "Як cancellation request до Task доставляється як `CancelledError` і чому cancellation є cooperative?"
description: "Task.cancel() планує throw CancelledError у coroutine на наступному await, але coroutine може перехопити цей exception – тому cancellation є cooperative."
track: python
section: asyncio
level: middle
type: mechanism
tags: [cancellederror]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/async.md#L1248-L1289
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`Task.cancel()` планує throw `CancelledError` у coroutine на наступному `await`, але coroutine може перехопити цей exception – тому cancellation є cooperative.**[^py314-library-asyncio-task] `CancelledError` – підклас `BaseException`. Якщо coroutine перехоплює його й не re-raise, task вважається завершеною нормально, а не скасованою. Для коректного скасування потрібно або re-raise, або викликати `Task.uncancel()` для зняття cancellation state.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
