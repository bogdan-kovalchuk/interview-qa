---
id: py-async-0014
title: "Які failure та cancellation semantics `gather()` потрібно врахувати, щоб не залишити sibling work без нагляду?"
description: "З return_exceptions=False (default) перший exception негайно propagated до caller, але інші awaitables продовжують виконуватися – вони не скасовуються автоматично"
track: python
section: asyncio
level: senior
type: pitfall
tags: [gather]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/async.md#L792-L832
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
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
