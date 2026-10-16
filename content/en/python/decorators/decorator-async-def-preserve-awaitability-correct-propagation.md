---
id: py-decor-0011
title: "How should a decorator for `async def` preserve awaitability and the correct propagation of exceptions?"
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

**A wrapper for `async def` should itself be an `async def` that calls the original function through `await`.** Then the code around the call, such as `try/except`, runs during `await`. An exception raised by the original coroutine reaches the wrapper.[^py314-reference-datamodel-coroutine-objects] A plain `def` wrapper only returns a coroutine object, which can still be awaited, so `try/except` cannot see the exception, and `inspect.iscoroutinefunction(wrapper)` returns `False`.[^py314-reference-datamodel-coroutine-objects][^py314-library-inspect-iscoroutinefunction]

## Detailed explanation

A decorator replaces the function's name with the result of calling it once, at `def` time.[^py314-reference-compound-stmts-function-definitions] If the decorated function is an `async def`, calling it does not run the body immediately: it creates a coroutine object, which is awaitable. Its execution is controlled through `__await__()`, and an exception raised in the coroutine is propagated by the iterator.[^py314-reference-datamodel-coroutine-objects] So the wrapper must be a coroutine function. Otherwise the code around the call runs at call time, not when the result is actually awaited.

The correct version is an `async def wrapper` with `return await func(...)`. The body of the original coroutine runs inside `await`, so a `ValueError` raised from it is caught by the `try`, and the caller receives the fallback. The example below shows this:

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

A plain `def` wrapper that returns `func(*args, **kwargs)` works synchronously: the call immediately returns a coroutine object, so a `try` around the call catches nothing. The exception escapes only at the `await` outside the wrapper, while the `await` itself still works, because a coroutine object is awaitable. Another mistake is an `async def` wrapper without `await` (`return func(...)`): it returns the coroutine object as its result, so the caller gets a never-awaited coroutine (with a `never awaited` warning) instead of a value.

`inspect.iscoroutinefunction()` returns `True` for functions defined with `async def` and `False` for an ordinary `def` wrapper.[^py314-library-inspect-iscoroutinefunction] Code that checks this flag may therefore treat a decorated async function as synchronous. This is why the choice between an `async def` and a `def` wrapper is made at decoration time: if the original is a coroutine function, the wrapper must also be `async def`. `@functools.wraps(func)` preserves `__name__` and `__doc__` and adds `__wrapped__`, which points to the original.[^py314-library-functools-functools-wraps]

**Common mistakes:**
- writing the wrapper as a `def` and assuming that a `try/except` around `return func(...)` will catch errors from the coroutine;
- writing an `async def` wrapper that returns `func(...)` without `await`: the caller gets a coroutine object instead of the result;
- omitting `@functools.wraps(func)`: then `__name__` and `__doc__` describe the wrapper.
