---
id: py-async-0002
title: "Які objects можна `await` і як coroutine, Task та Future пов’язані через awaitable protocol?"
description: "await приймає будь-який awaitable-об'єкт – coroutine, Task або Future, – тобто об'єкт з методом __await__."
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/async.md#L135-L203
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`await` приймає будь-який awaitable-об'єкт – coroutine, Task або Future, – тобто об'єкт з методом `__await__`.**[^py314-library-asyncio-task] Coroutine – це «сирий» об'єкт з `async def`. Task – обгортка над coroutine, яку event loop виконує concurrently. Future – low-level примітив, що представляє майбутній результат; Task є підкласом Future. Усі троє реалізують awaitable protocol, тому взаємозамінні в `await`.

## Detailed explanation

Bytecode-рівень `await` фактично каже: викликати `__await__()` на об'єкті, отримати iterator і
резюмувати його доти, доки він не підніме `StopIteration` (значення якого й стає результатом
`await`) або якийсь інший exception.[^py314-library-asyncio-task] Різні типи реалізують цей
iterator по-різному, і саме ця різниця пояснює, чим вони відрізняються один від одного.

`Future.__await__` – найпростіший випадок: якщо результат ще не встановлено, метод один раз
`yield self`, тобто повертає сам Future об'єкт назовні як "проміжне значення" iterator-а. Саме цей
yield розпізнає machinery Task, що керує coroutine: коли всередині coroutine yield'иться Future
(а не звичайне значення), Task реєструє на ньому `add_done_callback` і призупиняє себе, а не
трактує це як помилку. Коли Future отримує результат чи exception, callback резюмує `__await__`
через `send`/`throw`, і `StopIteration` завершує очікування.

Coroutine object не yield'ить Future напряму сама – вона делегує це вглиб, до того місця, де її
власний код зробив `await` на чомусь іншому. Тобто `await` на coroutine просто драйвить її як
iterator, і врешті-решт цей ланцюг `await` усередині `await` доходить до якогось Future
(найчастіше – Future, що представляє I/O-подію в selector-і), саме він і є єдиним місцем, звідки
насправді береться "проміжна зупинка".

Task – підклас Future, і тому успадковує його `__await__`: `await task` веде себе так само, як
`await` будь-якого Future – призупиняє викликача, поки `task` не встановить свій результат. Але
всередині сама Task – окремий driver: вона резюмує обгорнуту coroutine через власний internal
`__step()`, ловить кожен Future, який ця coroutine yield'ить, підписується на нього і повторює
цикл, аж доки coroutine не завершиться – і саме тоді Task як Future встановлює власний результат,
розбуджуючи все, що на неї чекало.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
