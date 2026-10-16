---
id: py-async-0014
title: "Які failure та cancellation semantics `gather()` потрібно врахувати, щоб не залишити sibling work без нагляду?"
track: python
section: asyncio
sources:
  - source_id: py314-library-asyncio-task
    title: "Python 3.14: Library/asyncio Task"
    url: https://docs.python.org/3.14/library/asyncio-task.html
  - source_id: py314-library-asyncio-eventloop
    title: "Python 3.14: Library/asyncio Eventloop"
    url: https://docs.python.org/3.14/library/asyncio-eventloop.html
  - source_id: py314-library-asyncio-dev
    title: "Python 3.14: Library/asyncio Dev"
    url: https://docs.python.org/3.14/library/asyncio-dev.html
---

## Short answer

**З `return_exceptions=False` (default) перший exception негайно propagated до caller, але інші awaitables продовжують виконуватися – вони не скасовуються автоматично.**[^py314-library-asyncio-task] Якщо потрібне скасування sibling-завдань при помилці, слід використовувати `TaskGroup` або вручну скасовувати tasks. З `return_exceptions=True` exception трактуються як результати й агрегуються у список – але caller повинен сам перевірити кожен елемент на exception.

## Detailed explanation

Механічно `gather()` обгортає кожен переданий coroutine у власну Task (Futures та вже готові Tasks
лишаються як є) і чекає, поки всі вони завершаться. Кожна з цих внутрішніх Tasks запланована в loop
незалежно й почала виконуватись одразу після виклику `gather()`, ще до того, як стався перший
exception.[^py314-library-asyncio-task] Коли одна з них падає, `gather()` лише встановлює exception
на своєму власному Future і повертає керування caller-у – але сама не чіпає інші Tasks, тому що вони
вже живуть окремо в loop, а не всередині `gather()`.

Це важливо відрізняти від cancellation самого `gather()`. Якщо скасувати саме awaitable, що
повертає `gather()` (наприклад, скасувавши Task, яка на нього чекає), `gather()` дійсно поширює
cancellation на всі свої внутрішні Tasks – це протилежна поведінка до випадку з exception. Тобто:
скасування зовнішнього виклику каскадно скасовує siblings, а помилка всередині одного з awaitables –
ні.

Практичний наслідок – siblings, що лишились без нагляду, можуть завершитися пізніше з власним
результатом або власним exception, який ніхто не прочитає; для exception це призводить до того ж
попередження `Task exception was never retrieved`, що й для звичайних orphaned Tasks. Тому
паттерн "запустити купу запитів через `gather()` і одразу зловити перший exception" небезпечний
у продакшн-коді без явного скасування решти.

`TaskGroup` вирішує це системно: при exception у будь-якому child він скасовує всіх siblings сам,
без ручного коду. Ручна альтернатива без `TaskGroup` – зберегти список Tasks, обгорнути `gather()`
у `try/except`, і в `except` явно викликати `.cancel()` на кожній ще не завершеній Task.
