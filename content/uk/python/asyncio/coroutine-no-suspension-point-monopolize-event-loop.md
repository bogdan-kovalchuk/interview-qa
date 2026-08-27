---
id: py-async-0006
title: "Чому coroutine без suspension point може монополізувати event-loop thread?"
description: "Coroutine, яка не містить жодного await, виконується синхронно від початку до кінця, не передаючи керування event loop, і тим самим блокує виконання всіх інших Tasks та I/O."
track: python
section: asyncio
level: middle
type: mechanism
tags: []
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  en: 2
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/async.md#L590-L652
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Coroutine, яка не містить жодного `await`, виконується синхронно від початку до кінця, не передаючи керування event loop, і тим самим блокує виконання всіх інших Tasks та I/O.**[^py314-library-asyncio-task] Cooperative multitasking працює лише тоді, коли кожна coroutine періодично поступається через suspension point. Без цього event loop не може обробляти інші ready callbacks, навіть якщо вони давно чекають.

## Detailed explanation

Найпоширеніша причина цієї проблеми на практиці – не CPU-важкий код сам собою, а синхронний
блокуючий виклик усередині `async def`, який виглядає нешкідливо: `time.sleep(1)` або
синхронний HTTP-запит бібліотекою на кшталт `requests`. Жоден з них не є suspension point для
event loop – вони просто утримують control flow, поки не завершаться, і loop фізично не може
обробити нічого іншого в цей час, навіть таймери `asyncio.sleep()` інших Task, які вже мали
спрацювати.[^py314-library-asyncio-eventloop]

Це відрізняється від deadlock: рано чи пізно синхронний виклик завершиться сам, і event loop
відновить нормальну роботу – просто ввесь цей час усі інші Task і I/O-callback чекають у черзі
ready, навіть якщо вони готові вже давно. У debug-режимі asyncio можна побачити симптом напряму:
якщо виконання одного callback перевищує поріг `loop.slow_callback_duration` (типово 0.1 секунди),
loop логує попередження "Executing ... took X seconds", що й вказує на відсутність suspension
point.[^py314-library-asyncio-dev]

Явний спосіб примусово віддати керування навіть без реального очікування – `await asyncio.sleep(0)`:
він не затримує виконання щонайменше на нуль секунд, а просто ставить coroutine в кінець черги
ready callbacks на один оберт event loop, даючи іншим Task шанс попрацювати. Для CPU-bound
обчислень це лише полегшує симптом, а не лікує причину – справжнє рішення тут: винести важку
роботу в `run_in_executor()` або окремий процес, щоб вона взагалі не займала event-loop thread.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
