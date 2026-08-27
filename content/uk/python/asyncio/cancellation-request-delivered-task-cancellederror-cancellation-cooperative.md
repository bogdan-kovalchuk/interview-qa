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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/async.md#L1248-L1289
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`Task.cancel()` планує throw `CancelledError` у coroutine на наступному `await`, але coroutine може перехопити цей exception – тому cancellation є cooperative.**[^py314-library-asyncio-task] `CancelledError` – підклас `BaseException`. Якщо coroutine перехоплює його й не re-raise, task вважається завершеною нормально, а не скасованою. Для коректного скасування потрібно або re-raise, або викликати `Task.uncancel()` для зняття cancellation state.

## Detailed explanation

`Task.cancel()` не піднімає виняток одразу – він лише позначає Task як таку, що очікує скасування,
і якщо Task наразі очікує на якийсь `Future`, скасовує цей `Future`. Сам `CancelledError`
з'являється в coroutine лише в точці найближчого `await` – доти код виконується як звичайно, навіть
якщо скасування вже запитане.[^py314-library-asyncio-eventloop] Якщо suspension point ще довго не
настане (наприклад, довгий CPU-bound цикл без `await`), доставка відкладається до першого `await`
або взагалі до природного завершення coroutine, і `cancel()` фактично не матиме ефекту.

Починаючи з 3.11, кожен виклик `cancel()` збільшує внутрішній лічильник, який повертає
`Task.cancelling()`. Це дає змогу відрізнити ситуацію, коли скасування запитали кілька разів
незалежно одне від одного – наприклад, і зовнішній caller, і `asyncio.timeout()` одночасно.
`Task.uncancel()` зменшує лічильник на одиницю; лише коли він досягає нуля, task повністю виходить
зі стану скасування. Код, який навмисно ловить `CancelledError` для власних потреб (сам
`asyncio.timeout()` робить так, коли спрацював саме його таймаут), зобов'язаний викликати
`uncancel()`, а не просто поглинути виняток – інакше зовнішній caller побачить task як успішно
завершений, навіть коли сам просив скасування.

Скасувати конкретний `await` можна ізольовано через `asyncio.shield()`: він огортає awaitable в
окремий Task, і скасування зовнішнього coroutine скасовує лише shield, а не внутрішній Task, тож
захищена операція продовжує виконуватися у фоні до завершення, навіть якщо той, хто на неї чекав,
уже отримав `CancelledError`.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
