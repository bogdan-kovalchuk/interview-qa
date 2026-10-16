---
id: py-excpt-0012
title: "What problem do `ExceptionGroup` and `except*` solve in concurrent code?"
track: python
section: exceptions
sources:
  - source_id: py314-tutorial-errors
    title: "Python 3.14: Tutorial/errors"
    url: https://docs.python.org/3.14/tutorial/errors.html
  - source_id: py314-library-exceptions
    title: "Python 3.14: Library/exceptions"
    url: https://docs.python.org/3.14/library/exceptions.html
  - source_id: py314-reference-compound-stmts-the-try-statement
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#the-try-statement
  - source_id: py314-library-asyncio-task-taskgroup
    title: "Python 3.14: Library/asyncio Task"
    url: https://docs.python.org/3.14/library/asyncio-task.html#asyncio.TaskGroup
  - source_id: py314-library-asyncio-task-gather
    title: "Python 3.14: Library/asyncio Task"
    url: https://docs.python.org/3.14/library/asyncio-task.html#asyncio.gather
  - source_id: py314-reference-compound-stmts-except-star
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#except-star
  - source_id: pep-0654-exception-groups
    title: "PEP 654: Exception Groups and except*"
    url: https://peps.python.org/pep-0654/
---

## Short answer

**`ExceptionGroup` lets you raise several unrelated exceptions at once, and `except*` lets you handle selected types without losing the rest.**[^py314-tutorial-errors] In concurrent code, such as `asyncio.TaskGroup`, several tasks can fail with different exceptions. A single `raise` carries only one exception, so the group collects them into one object, and `except*` splits it by type, handling each subgroup separately.[^py314-library-asyncio-task-taskgroup]

## Detailed explanation

A plain `raise` hands one exception to the handler. When several parallel tasks fail at the same time, that is the usual situation in concurrency frameworks, and the Python tutorial says that in such a case you should collect all the errors instead of raising only the first one.[^py314-tutorial-errors] For example, `asyncio.gather()` without `return_exceptions=True` propagates only the first exception to the awaiting caller; the others do not reach it.[^py314-library-asyncio-task-gather]

`ExceptionGroup(msg, excs)` (since Python 3.11) solves this as one ordinary exception that holds a list of other exceptions.[^pep-0654-exception-groups] The nested exceptions are available read-only through the `exceptions` attribute.[^py314-library-exceptions] `ExceptionGroup` is a subclass of `Exception`, so `except Exception` catches it, but `except ValueError` does not, because the group itself is not a `ValueError`.[^py314-library-exceptions] `asyncio.TaskGroup` uses the same shape: once all tasks have finished and some have failed with an exception other than `CancelledError`, it raises an `ExceptionGroup` with those errors. It re-raises `KeyboardInterrupt` and `SystemExit` as they are, without a group.[^py314-library-asyncio-task-taskgroup]

The example below starts three tasks: two fail with `ValueError`, one with `KeyError`. Each `except*` clause receives its own subgroup:

```python
import asyncio

async def fail(n):
    await asyncio.sleep(0)
    raise ValueError(f"task {n} failed")

async def bad_key():
    await asyncio.sleep(0)
    raise KeyError("missing")

async def main():
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(fail(1))
            tg.create_task(fail(2))
            tg.create_task(bad_key())
    except* ValueError as eg:
        print("ValueError group:", eg.exceptions)
    except* KeyError as eg:
        print("KeyError group:", eg.exceptions)

asyncio.run(main())

# ValueError group: (ValueError('task 1 failed'), ValueError('task 2 failed'))
# KeyError group: (KeyError('missing'),)
```

Use a group when several failures are real, independent results that each need handling. If there is only one failure, a plain exception is simpler.

**Common mistakes:**
- expecting `except ValueError` to catch an error inside a group: handle the group with `except*` or with `except ExceptionGroup`;
- mixing `except` and `except*` in one `try`, which is a syntax error;[^py314-reference-compound-stmts-except-star]
- logging the group with `str(eg)`, which shows the group message and the number of nested exceptions (for example `there were problems (2 sub-exceptions)`), but not their types or messages.[^py314-tutorial-errors]
