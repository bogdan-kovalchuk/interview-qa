---
id: py-async-0011
title: "Коли structured concurrency через `TaskGroup` дає надійнішу lifetime та failure semantics, ніж вільний набір `create_task()`?"
description: "TaskGroup гарантує, що при падінні будь-якого завдання всі sibling-завдання скасовуються, а exception збираються в ExceptionGroup – тоді як набір create_task() потребує ручного відстеження й може залишити завдання без..."
track: python
section: asyncio
level: senior
type: comparison
tags: [taskgroup, create-task]
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

**`TaskGroup` гарантує, що при падінні будь-якого завдання всі sibling-завдання скасовуються, а exception збираються в `ExceptionGroup` – тоді як набір `create_task()` потребує ручного відстеження й може залишити завдання без нагляду.**[^py314-library-asyncio-task] При виході з `async with TaskGroup()` context manager неявно awaiting всі завдання; якщо одне з них впало з exception (не `CancelledError`), решта скасовуються, нові завдання не приймаються, і після завершення всіх – raises `ExceptionGroup`. Це усуває класичну помилку «забутого» task, який тихо fail-ить.

## Detailed explanation

Ключова ідея structured concurrency – жодна асинхронна операція не повинна пережити той scope, у
якому її запустили. `TaskGroup` реалізує це буквально: вихід з `async with TaskGroup()` неможливий,
доки всі Tasks, створені всередині нього через `tg.create_task()`, не завершаться, тому функція, що
містить цей блок, фізично не може повернутися, лишивши після себе роботу, яка виконується
далі.[^py314-library-asyncio-task] Lifetime кожної Task жорстко прив'язаний до lifetime блоку, у
якому вона народилась.

Голий набір `create_task()` цієї гарантії не дає взагалі. Функція може створити кілька Tasks і
повернутися одразу, не чекаючи на жодну з них – вони продовжать виконуватися, прив'язані лише до
loop, а не до жодного видимого scope в коді. Якщо викликач такої функції не зберіг посилання на
ці Tasks, він навіть не знає про їхнє існування, і подальша доля цих Tasks – окрема історія: якщо
одна впаде з exception, ніхто про це не дізнається, поки хтось явно не прочитає результат.

Друга відмінність – напрям поширення cancellation. Якщо cancel зовнішню coroutine, що містить
`async with TaskGroup()`, group перехоплює цей `CancelledError` і каскадно скасовує всі свої
children, перш ніж дозволити cancellation піднятися далі. Голі Tasks, створені через
`create_task()` без group, такої прив'язки не мають: скасування coroutine, яка їх запустила, ніяк
автоматично не скасовує сирітські Tasks – вони просто лишаються працювати самі по собі, відірвані
від логіки, що їх породила.

Тому "надійність" тут – не про продуктивність чи API, а про те, чи можна дивлячись на межі одного
блоку коду точно сказати, яка конкурентна робота ще триває. З `TaskGroup` відповідь завжди
однозначна: усе, що всередині блоку, або вже завершилось, або точно завершиться (успішно чи через
cancellation) до виходу з нього.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
