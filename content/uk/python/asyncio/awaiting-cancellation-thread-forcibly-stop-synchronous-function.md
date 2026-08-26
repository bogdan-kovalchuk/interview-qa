---
id: py-async-0020
title: "Чому cancellation await на `to_thread()` не може примусово зупинити вже запущену synchronous function у worker thread?"
description: "Python не має механізму примусового зупинення thread; cancellation скасовує лише awaitable на стороні event loop, а worker thread продовжує виконання до завершення функції."
track: python
section: asyncio
level: senior
type: pitfall
tags: [to-thread]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/async.md#L938-L1042
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Python не має механізму примусового зупинення thread; cancellation скасовує лише awaitable на стороні event loop, а worker thread продовжує виконання до завершення функції.**[^py314-library-asyncio-task] <span class="warn">Це означає, що ресурси (сокети, файлові дескриптори) можуть залишатися зайнятими після скасування.</span> Для контролю потрібно, щоб сама функція періодично перевіряла cancellation flag або використовувала cooperative signaling.

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
