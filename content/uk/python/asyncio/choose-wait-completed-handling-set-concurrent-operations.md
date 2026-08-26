---
id: py-async-0013
title: "Коли обрати `wait()`, а коли `as_completed()` для обробки набору concurrent operations?"
description: "wait() повертає два множества (done, pending) і підходить для контролю через return_when; as_completed() повертає ітератор результатів у порядку завершення – зручний для потокової обробки."
track: python
section: asyncio
level: middle
type: comparison
tags: [wait, as-completed]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/async.md#L833-L937
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`wait()` повертає два множества `(done, pending)` і підходить для контролю через `return_when`; `as_completed()` повертає ітератор результатів у порядку завершення – зручний для потокової обробки.**[^py314-library-asyncio-task] При цьому `wait()` не скасовує pending tasks при timeout і приймає лише Task/Future (не coroutine). А `as_completed()` теж не скасовує tasks при зупинці ітерації, але дає результати одразу в порядку готовності, що краще для прогрес-барів або early-exit сценаріїв.

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
