---
id: py-async-0017
title: "Чому cleanup після `CancelledError` має зазвичай завершуватися re-raise, а не поглинанням cancellation?"
description: "Якщо CancelledError перехопити й не re-raise, task здається завершеною нормально – outer code (TaskGroup, gather) не дізнається про скасування, що порушує structured concurrency."
track: python
section: asyncio
level: senior
type: pitfall
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

**Якщо `CancelledError` перехопити й не re-raise, task здається завершеною нормально – outer code (`TaskGroup`, `gather`) не дізнається про скасування, що порушує structured concurrency.**[^py314-library-asyncio-task] Правильний патерн: `try/finally` для cleanup із неявним re-raise, або явний `raise` у `except CancelledError`. Поглинання вимагає `Task.uncancel()` і має використовуватися лише коли скасування дійсно потрібно ігнорувати.

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
