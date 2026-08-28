---
id: py-ctxmgr-0008
title: "Чим `async with` і methods `__aenter__`/`__aexit__` відрізняються від синхронного context-manager protocol?"
description: "__aenter__ і __aexit__ – це coroutine-методи: вони повертають awaitable, який event loop має await, тоді як синхронні __enter__/__exit__ викликаються як звичайні функції."
track: python
section: context-managers
level: middle
type: comparison
tags: [async-with, aenter, aexit]
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-reference-datamodel-with-statement-context-managers
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#with-statement-context-managers
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-contextlib
    title: "Python 3.14: Library/contextlib"
    url: https://docs.python.org/3.14/library/contextlib.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-asyncio-task-task-cancellation
    title: "Python 3.14: Library/asyncio Task"
    url: https://docs.python.org/3.14/library/asyncio-task.html#task-cancellation
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/namespace_and_context_manager.md#L3-L98
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`__aenter__` і `__aexit__` – це coroutine-методи: вони повертають awaitable, який event loop має await, тоді як синхронні `__enter__`/`__exit__` викликаються як звичайні функції.**[^py314-reference-datamodel-with-statement-context-managers] `async with` можна використовувати лише всередині `async def`. Семантика suppression та сама: truthy return з `__aexit__` пригнічує exception. Async-варіант потрібен, коли enter/exit виконують I/O (мережеві з'єднання, пули БД, async-locks).

## Detailed explanation

`__aenter__` і `__aexit__` – асинхронні аналоги `__enter__` і `__exit__`: вони оголошені як
`async def`, тому виклик повертає coroutine, яку `async with` awaits, замість того щоб отримати
значення напряму.[^py314-reference-datamodel-with-statement-context-managers]

Через це `async with` можна писати лише всередині `async def` – синтаксично поза coroutine-функцією
його немає. Сам вираз працює так само, як `with`: `async with expr as x:` викликає `__aenter__()`,
await-ить результат і присвоює його `x`, а по виходу await-ить `__aexit__(exc_type, exc_val,
exc_tb)`.

Семантика suppression exception та сама, що й у синхронного protocol: truthy return з `__aexit__`
пригнічує exception, а falsy (у тому числі `None`) дозволяє йому поширитися
далі.[^py314-reference-datamodel-with-statement-context-managers] Різниця лише в тому, що і сам
виклик `__aexit__`, і будь-який await всередині нього можуть призупинити coroutine, поки event loop
обробляє інші задачі.

Приклад асинхронного context manager, який відкриває з'єднання в `__aenter__` і закриває в
`__aexit__`:

```python
class AsyncConn:
    async def __aenter__(self):
        self.conn = await connect()
        return self.conn

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.conn.close()
        return False

async def main():
    async with AsyncConn() as conn:
        ...
```

Клас, що має лише `__aenter__`/`__aexit__`, не працює зі звичайним `with` – Python шукає саме
`__enter__`/`__exit__` і не підмінює їх асинхронними варіантами. Для generator-based варіанту
синхронного `@contextmanager` асинхронний аналог – `contextlib.asynccontextmanager`, який так само
перетворює `async def` generator з одним `yield` на async context manager.[^py314-library-contextlib]

**Коли потрібен саме async варіант:**
- enter/exit виконують мережеві I/O-операції (HTTP, черги, бази даних) і не повинні блокувати event
  loop;
- потрібна async-безпечна synchronization (наприклад, `asyncio.Lock` як context manager);
- ресурс сам надає лише async API для встановлення й закриття з'єднання.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
