---
id: py-decor-0011
title: "Як decorator для `async def` має зберегти awaitability та коректне поширення exceptions?"
track: python
section: decorators
sources:
  - source_id: py314-glossary-term-decorator
    title: "Python 3.14: Glossary"
    url: https://docs.python.org/3.14/glossary.html#term-decorator
  - source_id: py314-library-functools-functools-wraps
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html#functools.wraps
  - source_id: py314-reference-compound-stmts-function-definitions
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#function-definitions
  - source_id: py314-reference-datamodel-coroutine-objects
    title: "Python 3.14: Reference/datamodel, Coroutine Objects"
    url: https://docs.python.org/3.14/reference/datamodel.html#coroutine-objects
  - source_id: py314-library-inspect-iscoroutinefunction
    title: "Python 3.14: Library/inspect, iscoroutinefunction"
    url: https://docs.python.org/3.14/library/inspect.html#inspect.iscoroutinefunction
---

## Short answer

**Wrapper для `async def` має сам бути `async def` і викликати оригінал через `await`.** Тоді код навколо виклику, як-от `try/except`, виконується під час `await`. Виняток оригінальної корутини доходить до wrapper.[^py314-reference-datamodel-coroutine-objects] Звичайний `def` wrapper лише повертає coroutine object, який ще можна чекати (`await`), тож `try/except` його не бачить, а `inspect.iscoroutinefunction(wrapper)` дає `False`.[^py314-reference-datamodel-coroutine-objects][^py314-library-inspect-iscoroutinefunction]

## Detailed explanation

Декоратор замінює ім’я функції результатом свого виклику один раз, під час `def`.[^py314-reference-compound-stmts-function-definitions] Якщо декорована функція є `async def`, її виклик не виконує тіло одразу: створюється coroutine object, який є awaitable. Його виконання керується через `__await__()`, а виняток з корутини передається далі ітератором.[^py314-reference-datamodel-coroutine-objects] Тому wrapper має бути корутинною функцією. Інакше його код навколо виклику виконається в момент виклику, а не тоді, коли результат справді чекають.

Правильний варіант – `async def wrapper` з `return await func(...)`. Тіло оригінальної корутини виконується всередині `await`, тож `ValueError` з нього ловиться в `try`, і caller отримує fallback:

```python
import asyncio
import functools
import inspect

def with_fallback(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)   # the coroutine body runs here
        except ValueError:
            return "fallback"
    return wrapper

@with_fallback
async def fetch():
    raise ValueError("boom")

print(asyncio.run(fetch()))                  # fallback
print(inspect.iscoroutinefunction(fetch))    # True
```

Звичайний `def` wrapper, який повертає `func(*args, **kwargs)`, працює синхронно: виклик одразу повертає coroutine object, тож `try` навколо виклику нічого не ловить. Виняток вилітає вже на `await` поза wrapper, а сам `await` працює, бо coroutine object є awaitable. Ще одна помилка – `async def` wrapper без `await` (`return func(...)`): він повертає coroutine object як результат, і caller отримує не значення, а не-awaited корутину з попередженням `never awaited`.

`inspect.iscoroutinefunction()` повертає `True` для функцій, визначених через `async def`, і `False` для звичайного `def` wrapper.[^py314-library-inspect-iscoroutinefunction] Код, що перевіряє цей прапорець, може тому вважати декоровану асинхронну функцію синхронною. Тому вибір між `async def` і `def` wrapper робиться під час декорування: якщо оригінал є корутинною функцією, wrapper теж має бути `async def`. `@functools.wraps(func)` зберігає `__name__`, `__doc__` і додає `__wrapped__`, що вказує на оригінал.[^py314-library-functools-functools-wraps]

**Типові помилки:**
- написати wrapper як `def` і вважати, що `try/except` навколо `return func(...)` ловитиме помилки корутини;
- написати `async def` wrapper і повернути `func(...)` без `await`: caller отримає coroutine object замість результату;
- пропустити `@functools.wraps(func)`: тоді `__name__` і `__doc__` вказують на wrapper.
