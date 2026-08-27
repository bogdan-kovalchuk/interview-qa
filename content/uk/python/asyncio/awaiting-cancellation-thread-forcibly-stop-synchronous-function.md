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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/async.md#L938-L1042
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Python не має механізму примусового зупинення thread; cancellation скасовує лише awaitable на стороні event loop, а worker thread продовжує виконання до завершення функції.**[^py314-library-asyncio-task] <span class="warn">Це означає, що ресурси (сокети, файлові дескриптори) можуть залишатися зайнятими після скасування.</span> Для контролю потрібно, щоб сама функція періодично перевіряла cancellation flag або використовувала cooperative signaling.

## Detailed explanation

Скасування в asyncio працює через доставку `CancelledError` у coroutine, яка чекає на результат –
це можливо лише тому, що coroutine кооперативно повертає керування на кожному `await`. Worker
thread, у якому виконується функція, передана в `to_thread()`, – не coroutine: він виконує звичайний
Python bytecode без жодних точок, де event loop міг би "втрутитися" і підмінити виконання винятком.
[^py314-library-asyncio-task] Коли caller скасовує awaiting Task, `CancelledError` піднімається у
тій точці, де coroutine чекала на `Future` від thread pool executor-а, – тобто в головному thread-і,
а не всередині worker-а.

`concurrent.futures.Future`, яку обгортає `to_thread()`, підтримує `cancel()` лише доки завдання ще
не почало виконуватися в worker thread; щойно `func` реально запустилася, `cancel()` повертає
`False` і ніяк на неї не впливає – у CPython немає безпечного публічного API для примусового
переривання довільного thread ззовні (аналог примусового `kill` для довільного bytecode небезпечний,
бо може перервати виконання посеред утримання internal lock-а чи мутації структури даних). Тому
await, що скасовується, лише "відпускає" очікуючу coroutine із exception, а сам worker thread
продовжує виконуватися до природного `return` або `raise`, і його результат просто ігнорується,
коли він зрештою прийде.

Практичний наслідок – ресурси, відкриті всередині функції (файлові дескриптори, сокети, locks),
залишаються зайнятими на весь час, доки функція сама не завершиться, навіть якщо caller давно
отримав `CancelledError` і рухається далі; якщо функція тримає, наприклад, `threading.Lock`, і
виконання застрягло, це може призвести до resource leak, що переживає саму cancellation.

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
