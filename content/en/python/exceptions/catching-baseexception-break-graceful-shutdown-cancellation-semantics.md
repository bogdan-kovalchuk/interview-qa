---
id: py-excpt-0003
title: "When can catching `BaseException` break graceful shutdown or cancellation semantics?"
description: "When can catching `BaseException` break graceful shutdown or cancellation semantics?"
track: python
section: exceptions
level: senior
type: pitfall
tags: [baseexception]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-tutorial-errors
    title: "Python 3.14: Tutorial/errors"
    url: https://docs.python.org/3.14/tutorial/errors.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-exceptions
    title: "Python 3.14: Library/exceptions"
    url: https://docs.python.org/3.14/library/exceptions.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-reference-compound-stmts-the-try-statement
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#the-try-statement
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-asyncio-task-task-cancellation
    title: "Python 3.14: Library/asyncio Task"
    url: https://docs.python.org/3.14/library/asyncio-task.html#task-cancellation
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: CancelledError directly subclasses BaseException; TaskGroup and asyncio.timeout() may misbehave if a coroutine swallows CancelledError; CancelledError should generally be propagated again after cleanup."
  - source_id: py314-library-asyncio-task-cancel-method
    title: "Python 3.14: Library/asyncio Task"
    url: https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task.cancel
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: Task.cancel() does not guarantee cancellation if the coroutine suppresses the exception; suppressing cancellation is actively discouraged and requires calling Task.uncancel()."
  - source_id: py314-reference-expressions-generator-iterator-methods
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#generator-iterator-methods
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: generator.close() raises GeneratorExit at the paused yield; if the generator does not catch it, close() returns without error; if the generator yields a value, close() raises RuntimeError."
  - source_id: py314-reference-expressions-yield-expressions
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#yield-expressions
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: if a generator is finalized without being resumed, close() is called, allowing pending finally blocks to run."
---

## Short answer

**`except BaseException` catches `SystemExit`, `KeyboardInterrupt` and `GeneratorExit`; if the handler does not re-raise, the process does not exit on `sys.exit()` or Ctrl-C.**[^py314-library-exceptions] `asyncio.CancelledError` also inherits from `BaseException`, so a handler without `raise` silently swallows task cancellation.[^py314-library-asyncio-task-task-cancellation] <span class="warn">If a caught `GeneratorExit` is followed by a `yield`, `.close()` on the generator raises `RuntimeError`.</span>[^py314-reference-expressions-generator-iterator-methods] Such a handler is appropriate when the exception is re-raised after cleanup, for example at the top level of a program.

## Detailed explanation

`Exception` is a subclass of `BaseException`, but `SystemExit` and `KeyboardInterrupt` inherit from `BaseException` directly so that code catching `Exception` does not intercept a request to exit; `GeneratorExit` does so because it is technically not an error. So `sys.exit()` and Ctrl-C propagate up to the interpreter, which then ends the process.[^py314-library-exceptions]

If `except BaseException` does not re-raise, `sys.exit()` stops ending the program and Ctrl-C seems to do nothing. `GeneratorExit` has its own trap. `generator.close()` raises it at the paused `yield`. If the generator does not catch it, `close()` returns quietly and any `finally` blocks run.[^py314-reference-expressions-yield-expressions][^py314-reference-expressions-generator-iterator-methods] If the handler yields a value instead, `close()` raises `RuntimeError`:

```python
def reader():
    try:
        yield "line 1"
    except BaseException:       # catches the GeneratorExit raised by close()
        yield "cleanup"         # yielding here makes close() fail

gen = reader()
next(gen)
try:
    gen.close()
except RuntimeError as error:
    print(error)                # generator ignored GeneratorExit
```

`asyncio.CancelledError` also inherits from `BaseException` directly, so `except BaseException` without `raise` silently swallows a task's cancellation.[^py314-library-asyncio-task-task-cancellation] The `Task.cancel()` documentation warns that cancellation is not guaranteed if the coroutine suppresses the exception.[^py314-library-asyncio-task-cancel-method] `TaskGroup` and `asyncio.timeout()` depend on cancellation and may misbehave if a coroutine swallows it.[^py314-library-asyncio-task-task-cancellation] Example:

```python
import asyncio

async def worker():
    try:
        await asyncio.sleep(10)
    except BaseException:       # swallows CancelledError
        return "finished"

async def main():
    task = asyncio.create_task(worker())
    await asyncio.sleep(0)      # let the task reach sleep()
    task.cancel()
    print(await task)           # finished
    print(task.cancelled())     # False: the cancellation was swallowed

asyncio.run(main())
```

If cancellation is suppressed deliberately, `Task.uncancel()` must also be called; suppressing it is actively discouraged.[^py314-library-asyncio-task-cancel-method] The correct pattern is cleanup followed by `raise`.[^py314-library-asyncio-task-task-cancellation]

**Common mistakes:**
- writing `except BaseException` instead of `except Exception` when only `Exception` is needed;
- catching `BaseException` without `raise` in a coroutine that `TaskGroup` or `asyncio.timeout()` must cancel;
- yielding a value from a `GeneratorExit` handler and expecting `close()` to finish without an error.

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
