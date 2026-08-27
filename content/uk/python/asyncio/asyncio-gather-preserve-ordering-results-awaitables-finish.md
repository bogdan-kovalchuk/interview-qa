---
id: py-async-0012
title: "Як `asyncio.gather()` зберігає ordering results, якщо awaitables завершуються в іншому порядку?"
description: "gather() повертає список результатів у тому ж порядку, що й вхідні awaitables, незалежно від реального порядку їх завершення."
track: python
section: asyncio
level: middle
type: mechanism
tags: [asyncio-gather]
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

**`gather()` повертає список результатів у тому ж порядку, що й вхідні awaitables, незалежно від реального порядку їх завершення.**[^py314-library-asyncio-task] Кожному awaitable відповідає позиція у result list за індексом входу. Наприклад, якщо `gather(slow(), fast())` і `fast()` завершиться першою, результат все одно буде `[result_slow, result_fast]`.

## Detailed explanation

`gather()` не чекає awaitables послідовно і не сортує результати за часом завершення – він від
самого початку створює для кожного вхідного awaitable окрему `Task` (або обгортку `Future`, якщо
це вже Future) і зберігає впорядкований список цих об'єктів за позицією аргументу.
[^py314-library-asyncio-task] Коли конкретна Task завершується, її callback записує результат у
result list за тим самим індексом, яким ця Task була додана, а не за моментом виконання. Сам event
loop планує coroutines кооперативно: кожен `await` всередині них – точка, де контроль повертається
до loop, і саме loop вирішує, яка з задач отримає час на CPU далі; порядок виконання кроків може
бути яким завгодно, але масив індексів фіксований одразу при виклику `gather()`.

Це принципово відрізняє `gather()` від `asyncio.as_completed()`, який навпаки повертає awaitables
у порядку фактичного завершення, а не у вхідному порядку – вибір між ними залежить від того, чи
потрібен caller-у порядок результатів, чи швидкість реакції на перший готовий результат.

За замовчуванням `return_exceptions=False`: якщо одна з awaitables кидає exception, `gather()`
одразу піднімає його caller-у, але решта Tasks не скасовуються автоматично і продовжують
виконуватися у фоні – це джерело поширеної помилки, коли забуті Tasks логують exceptions пізніше в
повідомленні `Task exception was never retrieved`. З `return_exceptions=True` exception сам стає
значенням у result list на своїй позиції, і caller отримує повний список без обриву на першій
помилці.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
