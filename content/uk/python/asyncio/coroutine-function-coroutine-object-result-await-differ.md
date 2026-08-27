---
id: py-async-0001
title: "Чим coroutine function, coroutine object та результат `await` відрізняються між собою?"
description: "Coroutine function – це async def-функція; coroutine object – об'єкт, який повертає виклик такої функції; результат await – значення, яке coroutine повертає після виконання."
track: python
section: asyncio
level: middle
type: comparison
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/async.md#L17-L43
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Coroutine function – це `async def`-функція; coroutine object – об'єкт, який повертає виклик такої функції; результат `await` – значення, яке coroutine повертає після виконання.**[^py314-library-asyncio-task] Виклик `async def`-функції не виконує її тіло, а лише створює coroutine object. Щоб код справді виконався, цей об'єкт потрібно передати в `await`, `asyncio.create_task()` або інший механізм запуску. Результат `await coro()` – це те, що coroutine повертає через `return`.

## Detailed explanation

Незапущений coroutine object, який ніхто не await, і збирач сміття його знищує – Python видає
`RuntimeWarning: coroutine '...' was never awaited`, бо є типова помилка: розробник викликав
`async def`-функцію, забув `await`, і код мовчки нічого не зробив.[^py314-library-asyncio-task] Це
відрізняє coroutine object від звичайного виклику функції: звичайна функція виконується одразу
під час виклику, а coroutine object лише резервує стан (кадр виконання) і чекає, доки хтось
почне його «просувати» через `await` чи еквівалент.

Кожен виклик `async def`-функції створює новий, незалежний coroutine object зі своїм власним
кадром – два виклики тієї самої функції з тими самими аргументами не поділяють стан. Водночас
один і той самий coroutine object не можна await двічі: після завершення повторний `await`
піднімає `RuntimeError` ("cannot reuse already awaited coroutine"), бо його внутрішній кадр уже
звільнений.

`await` на coroutine object виконує її синхронно в межах поточної Task – це не створює нову
одиницю планування, а просто «вбудовує» логіку coroutine у виконання того, хто на неї await.
На відміну від цього, `asyncio.create_task(coro())` реєструє coroutine у event loop як окрему
Task, яка виконується конкурентно з рештою коду, а результат `await` на такому Task – це те саме
значення `return`, але отримане після того, як Task встигла виконатися паралельно з іншими,
а не негайно в тому самому кадрі виклику.[^py314-library-asyncio-eventloop]

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
