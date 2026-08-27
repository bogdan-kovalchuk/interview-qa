---
id: py-async-0003
title: "Чому просте створення кількох coroutine objects ще не запускає їх concurrently?"
description: "Виклик async def-функції лише створює coroutine object, але не планує його виконання – код не запуститься, поки об'єкт не буде await-нуто або передано в asyncio.create_task()."
track: python
section: asyncio
level: middle
type: pitfall
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

**Виклик `async def`-функції лише створює coroutine object, але не планує його виконання – код не запуститься, поки об'єкт не буде `await`-нуто або передано в `asyncio.create_task()`.**[^py314-library-asyncio-task] Послідовний `await` кількох coroutine виконує їх по черзі, а не паралельно. Для справжньої конкурентності потрібно створити Task для кожного coroutine, щоб event loop міг перемикатися між ними на suspension points.

## Detailed explanation

Виклик `async def`-функції не запускає жодного рядка її тіла. Технічно він створює coroutine
object – state machine, схожу на generator, з власним frame, який ще жодного разу не виконувався.
Тіло почне виконуватися лише тоді, коли щось викличе на цьому об'єкті `send(None)` (саме це робить
`await` або крок event loop), і зупиниться на першій точці, де тіло саме зробить `await` чогось
іншого.[^py314-library-asyncio-task] Якщо coroutine object створено і жодного разу не
задрайвлено – ні напряму, ні через Task, – інтерпретатор під час garbage collection видає
`RuntimeWarning: coroutine '...' was never awaited`, бо це майже завжди помилка логіки, а не
навмисна поведінка.

`await coro` і `create_task(coro)` запускають виконання по-різному. `await` драйвить coroutine у
контексті поточної Task: код одразу починає виконувати тіло coroutine синхронно, аж до першої
внутрішньої точки призупинення, і рядок після `await` не виконається, поки цей coroutine повністю
не завершиться. `create_task()`, навпаки, лише реєструє нову Task у loop і негайно повертає
керування викликачу – саме тіло coroutine почне виконуватися пізніше, коли loop дійде до цієї Task
у своїй черзі, можливо навіть після того, як викликач продовжить виконувати наступні рядки.

Звідси й різниця в поведінці для кількох coroutine поспіль: `await a(); await b()` виконує `a`
повністю, потім `b` повністю – це послідовне виконання в одній логічній лінії, навіть якщо обидва
async. А `t1 = create_task(a()); t2 = create_task(b()); await t1; await t2` дозволяє loop
перемикатися між `a` і `b` на кожній їхній внутрішній точці призупинення, тому робота, що чекає на
I/O в одній, не блокує прогрес іншої.

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
