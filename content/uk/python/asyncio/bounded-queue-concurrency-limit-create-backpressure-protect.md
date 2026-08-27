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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/async.md#L1305-L1325
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Bounded `asyncio.Queue(maxsize=N)` зупиняє producer через `await put()`, коли черга заповнена, а `Semaphore(limit)` обмежує кількість одночасних операцій – разом вони не дають service накопичувати нескінченну кількість pending завдань.**[^py314-library-asyncio-task] Producer, що викликає `await queue.put(item)`, призупиняється доки consumer не звільнить слот через `get()` – це природний backpressure. `Semaphore` доповнює це, обмежуючи одночасні зовнішні виклики (наприклад, HTTP-запити до БД): після вичерпання лічильника нові Task чекають `acquire()`. Без цих механізмів швидкий producer або burst вхідних запитів може вичерпати пам'ять або перевантажити downstream.

## Detailed explanation

`asyncio.Queue` реалізує backpressure не через якийсь спеціальний механізм, а через звичайне
`await`: коли `put()` викликають на заповненій черзі (`maxsize` вже досягнуто), coroutine
producer-а підвішується на внутрішньому `Future`, доданому в чергу очікувачів, і жодного bytecode
producer-а більше не виконується, доки consumer не викличе `get()` і не звільнить слот.
[^py314-library-asyncio-task] Це і є суть backpressure: швидкість, з якою producer може породжувати
нову роботу, механічно прив'язана до швидкості, з якою consumer її забирає, а не працює незалежно.

`Semaphore(limit)` діє на іншому рівні: він не буферизує вхідні елементи, а обмежує, скільки coroutine
можуть одночасно перебувати між `acquire()` і `release()`. Внутрішній лічильник зменшується на кожен
`acquire()`; коли він доходить до нуля, наступні виклики `acquire()` підвішуються у FIFO-черзі
очікування, і кожен `release()` будить рівно одного наступного очікувача. Це обмежує не кількість
накопичених завдань, а кількість завдань, що реально виконуються паралельно (наприклад, одночасних
HTTP-запитів до одного backend-у).

Разом ці два механізми закривають дві різні діри: без bounded queue producer, швидший за
consumer-а, необмежено накопичує pending items у пам'яті (наприклад, звичайний unbounded `Queue`
росте, доки процес не впаде через нестачу пам'яті); без semaphore навіть bounded queue не заважає
consumer-у запустити необмежену кількість одночасних downstream-викликів одразу, як тільки елементи
з'являться в черзі, перевантаживши БД чи зовнішній сервіс сплеском запитів. Bounded queue обмежує
*накопичену* роботу, semaphore обмежує *одночасно виконувану* роботу – потрібні обидва рівні
захисту, бо вони діють на різних ділянках pipeline.

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
