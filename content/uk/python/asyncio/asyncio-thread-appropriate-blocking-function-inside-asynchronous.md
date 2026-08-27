---
id: py-async-0019
title: "Коли `asyncio.to_thread()` доречний для blocking function у асинхронній application?"
description: "to_thread() доречний для I/O-bound blocking функцій (файлові операції, blocking сторонні бібліотеки), щоб не блокувати event loop; для CPU-bound краще ProcessPoolExecutor."
track: python
section: asyncio
level: middle
type: practical
tags: [asyncio-to-thread]
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

**`to_thread()` доречний для I/O-bound blocking функцій (файлові операції, blocking сторонні бібліотеки), щоб не блокувати event loop; для CPU-bound краще `ProcessPoolExecutor`.**[^py314-library-asyncio-task] Функція виконується у worker thread default executor-а (або кастомного). Event loop залишається вільним для інших tasks. Keyword arguments передаються напряму, на відміну від `run_in_executor`, де потрібен `functools.partial`.

## Detailed explanation

`asyncio.to_thread(func, *args, **kwargs)` – це тонка обгортка над `loop.run_in_executor()` з
дефолтним `ThreadPoolExecutor` циклу, яка додатково копіює поточний `contextvars.Context` у worker
thread, тому змінні контексту (наприклад, ті, що встановлені через `ContextVar.set()`) залишаються
видимими всередині blocking функції.[^py314-library-asyncio-eventloop] На відміну від прямого
виклику `run_in_executor(None, func, arg1, arg2)`, де keyword arguments довелося б передавати через
`functools.partial(func, kw=value)`, `to_thread()` приймає `**kwargs` напряму – це суто ергономічна
відмінність, механіка виконання та сама.

Чому саме thread, а не звичайний виклик у корутині: I/O-bound blocking виклик (читання файлу,
DNS-резолюшн, blocking HTTP-клієнт) утримує GIL лише короткими сплесками, а більшість часу
проводить у системному виклику з GIL, звільненим на час очікування ОС; поки цей thread чекає на
I/O, event loop у головному thread може продовжувати виконувати інші coroutines. Дефолтний
executor – `ThreadPoolExecutor` з обмеженою кількістю worker-ів (`min(32, os.cpu_count() + 4)`),
тож паралельних blocking викликів не може бути безмежно багато без явного налаштування
`loop.set_default_executor()`.

Для CPU-bound роботи (важкі обчислення без I/O) `to_thread()` не рятує: GIL не звільняється між
bytecode-інструкціями достатньо, щоб дати реальний паралелізм, тому такий thread просто конкурує з
головним thread-ом за GIL і навіть додає overhead на перемикання контексту. У цьому випадку
потрібен окремий процес через `ProcessPoolExecutor`, де кожен worker має власний інтерпретатор і
власний GIL.

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
