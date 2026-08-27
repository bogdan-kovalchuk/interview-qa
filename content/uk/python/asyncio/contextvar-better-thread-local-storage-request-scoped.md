---
id: py-async-0023
title: "Чому `ContextVar` краще за thread-local storage для request-scoped state між asyncio Tasks?"
description: "ContextVar ізолює значення за логічним контекстом (Task), а не за фізичним thread, тому кілька Task в одному thread не «затікають» одна в одну."
track: python
section: asyncio
level: middle
type: comparison
tags: [contextvar]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/async.md#L1443-L1542
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`ContextVar` ізолює значення за логічним контекстом (Task), а не за фізичним thread, тому кілька Task в одному thread не «затікають» одна в одну.**[^py314-library-asyncio-task] `threading.local()` прив'язує стан до OS thread; в asyncio багато Task виконуються в одному thread і бачили б однакове thread-local значення. `asyncio.create_task()` автоматично копіює поточний `Context` у нову Task, тому кожна Task має власні значення `ContextVar` (наприклад, request_id, tenant). Зміна `ContextVar` в одній Task не впливає на інші Task, навіть якщо вони виконуються в тому ж thread.

## Detailed explanation

Технічно `Context` – незмінна (immutable) мапа: `ContextVar.set()` не мутує наявний контекст, а
створює нове значення у поточному контексті виконання, повертаючи `Token`, який можна передати в
`reset()`, щоб повернути попереднє значення. Coroutine, Task і callback завжди виконуються всередині
якогось `Context`; коли `asyncio.create_task()` створює нову Task, вона отримує **копію** поточного
`Context` на момент створення – це знімок, а не спільне посилання.[^py314-library-asyncio-task]

Звідси важливий нюанс, якого немає в короткій відповіді: успадкування односпрямоване. Дочірня Task
бачить значення `ContextVar`, встановлені батьківською Task **до** моменту `create_task()`, але
зміна `ContextVar` усередині дочірньої Task ніяк не повертається назад у батьківську – кожна Task
працює зі своєю копією, а не зі спільним мутабельним сховищем. Це відрізняється від `threading.local()`
лише термінологічно, у нюансі copy-on-fork, а не поведінково: `threading.local()` теж не ділиться
між потоками, але прив'язка йде до OS thread, а не до логічної одиниці виконання, тож усередині
одного thread з кількома Task усі вони бачили б те саме значення `threading.local()`, тоді як
`ContextVar` розрізняє їх.

Є одна пастка: якщо код виконує callback через `loop.call_soon()` або відправляє роботу в
`run_in_executor()`, `Context` копіюється автоматично лише для `call_soon`/`call_later`/Task, а
явний виклик у `ThreadPoolExecutor` виконується в чужому потоці без автоматичного перенесення
`Context` – щоб отримати ті самі значення там, потрібно обгорнути виклик у
`contextvars.copy_context().run(...)`.[^py314-library-asyncio-eventloop]

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
