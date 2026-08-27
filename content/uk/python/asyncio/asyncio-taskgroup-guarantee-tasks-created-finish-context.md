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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/async.md#L746-L791
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`TaskGroup` – асинхронний context manager, який у `__aexit__` неявно очікує завершення всіх Tasks, створених через `tg.create_task()`, і не вийде з блоку, поки вони не завершаться.**[^py314-library-asyncio-task] Tasks створюються лише всередині `async with`-блоку. Після виходу з блоку (нормально чи через exception) `TaskGroup` чекає завершення всіх дочірніх Tasks, забезпечуючи structured concurrency.

## Detailed explanation

`TaskGroup.__aexit__` не просто виходить з блоку – він виконує внутрішню логіку, яка в циклі чекає,
поки set задач, зареєстрованих через `create_task()`, не стане порожнім.
[^py314-library-asyncio-task] Кожен виклик `tg.create_task(coro)` додає `Task` у внутрішній `set` і
навішує на неї `done_callback`, який видаляє Task із цього set та, якщо вона впала з exception,
ініціює скасування решти задач групи. Тому `__aexit__` не завершується, доки останній callback не
спрацює для всіх задач – незалежно від того, скільки їх було створено і в якому порядку вони
фінішували.

Якщо одна з Tasks кидає exception (окрім `CancelledError`), `TaskGroup` скасовує всі інші ще активні
Tasks у групі та чекає, поки вони теж завершаться (включно з обробкою `CancelledError` всередині
них), і лише потім піднімає `ExceptionGroup`, що об'єднує всі зібрані помилки, навіть якщо впала
лише одна Task. Це і є structured concurrency: неможливо вийти з блоку, залишивши осиротілі задачі,
що виконуються у фоні без нагляду, – на відміну від "голого" `asyncio.create_task()` без TaskGroup,
де забута Task може продовжувати жити і після того, як функція, що її створила, повернула
керування.

`create_task()` можна викликати лише всередині самого блоку `async with`; спроба додати нову Task
після початку `__aexit__` (наприклад, з callback-а іншої задачі) підніме `RuntimeError`, бо група
вже перейшла у стан завершення і більше не приймає нових членів.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
