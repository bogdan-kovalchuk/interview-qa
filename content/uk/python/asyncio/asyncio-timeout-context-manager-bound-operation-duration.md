---
id: py-async-0016
title: "Як context manager `asyncio.timeout()` обмежує час операції та який exception бачить caller зовні?"
description: "asyncio.timeout(delay) скасовує поточну task при перевищенні deadline, а внутрішній CancelledError перетворюється на TimeoutError, який caller бачить за межами context manager."
track: python
section: asyncio
level: middle
type: mechanism
tags: [asyncio-timeout]
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

**`asyncio.timeout(delay)` скасовує поточну task при перевищенні deadline, а внутрішній `CancelledError` перетворюється на `TimeoutError`, який caller бачить за межами context manager.**[^py314-library-asyncio-task] Всередині блоку task бачить звичайний `CancelledError` – тому перехоплювати його всередині `async with` не слід. Deadline можна змінити через `cm.reschedule(new_deadline)`.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
