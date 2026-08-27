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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/async.md#L833-L937
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`asyncio.timeout(delay)` скасовує поточну task при перевищенні deadline, а внутрішній `CancelledError` перетворюється на `TimeoutError`, який caller бачить за межами context manager.**[^py314-library-asyncio-task] Всередині блоку task бачить звичайний `CancelledError` – тому перехоплювати його всередині `async with` не слід. Deadline можна змінити через `cm.reschedule(new_deadline)`.

## Detailed explanation

`asyncio.timeout(delay)` на вході в `async with` планує `loop.call_later(delay, callback)`, який за
настання deadline викликає `task.cancel()` для тієї Task, що виконує тіло блоку – точнісінько так
само, як зовнішній `task.cancel()`, викликаний кимось іншим.[^py314-library-asyncio-task] Тому
всередині блоку немає жодної спеціальної exception – це звичайний `CancelledError`, і саме тому
перехоплювати його всередині `async with` небезпечно: код, що ловить `CancelledError` у себе,
приховує факт скасування від event loop, і Task може ніколи коректно не зупинитися.

Магія відбувається в `__aexit__`: коли `CancelledError` доходить до межі блоку, context manager
перевіряє, чи це саме той cancel, який він сам ініціював (через внутрішній лічильник, порівняний зі
станом Task після `task.uncancel()`). Якщо так – він гасить цей конкретний `CancelledError` і
замість нього піднімає `TimeoutError`, який і бачить caller зовні `async with`. Якщо ж скасування
прийшло з іншого джерела (наприклад, зовнішній `task.cancel()` під час дії того самого timeout, або
вкладений `asyncio.timeout()`, що спрацював раніше), `__aexit__` не підміняє exception –
`CancelledError` пробрасується далі як є, бо timeout відповідає лише за власний deadline, а не за
всі можливі скасування Task.

Deadline не фіксований назавжди: `cm.reschedule(new_deadline)` дозволяє зсунути момент спрацювання,
не виходячи з блоку і не створюючи новий context manager – зручно, коли ліміт часу залежить від
проміжного результату (наприклад, продовжити очікування після отримання перших байтів відповіді).
Метод `cm.expired()` дає змогу перевірити постфактум, чи саме цей timeout спричинив вихід із блоку.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
