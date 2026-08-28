---
id: py-ctxmgr-0009
title: "How should `__aexit__` finish cleanup after a `CancelledError` without swallowing the task's cancellation?"
description: "How should `__aexit__` finish cleanup after a `CancelledError` without swallowing the task's cancellation?"
track: python
section: context-managers
level: senior
type: practical
tags: [aexit, cancellederror]
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-reference-datamodel-with-statement-context-managers
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#with-statement-context-managers
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-contextlib
    title: "Python 3.14: Library/contextlib"
    url: https://docs.python.org/3.14/library/contextlib.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-asyncio-task-task-cancellation
    title: "Python 3.14: Library/asyncio Task"
    url: https://docs.python.org/3.14/library/asyncio-task.html#task-cancellation
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
---

## Short answer

**`__aexit__` should finish cleanup and then either not catch `CancelledError` or re-raise it, so
the cancellation still reaches the task.**[^py314-reference-datamodel-with-statement-context-managers]
`CancelledError` inherits from `BaseException`, so a plain `except Exception` will not catch it.
<span class="warn">If code deliberately suppresses `CancelledError`, it must call `Task.uncancel()`,
or structured concurrency (TaskGroup, timeout) will behave incorrectly.</span> General rule: cleanup
-> re-raise.

## Detailed explanation

`CancelledError` is the exception asyncio uses to signal a coroutine that it must stop; it reaches
`__aexit__` the same way any other error does, through the `exc_type`, `exc_val`, and `exc_tb`
parameters.[^py314-reference-datamodel-with-statement-context-managers]

The main trap is that `CancelledError` inherits from `BaseException`, not
`Exception`.[^py314-library-asyncio-task-task-cancellation] So a plain `except Exception` never
catches it, and cleanup code written "as usual" correctly lets the cancellation propagate further.
The problem appears when `__aexit__` explicitly catches something broader (`except BaseException` or
a bare `except:`) for the sake of cleanup – in that case it must finish the needed work and
immediately re-raise, otherwise the task's cancellation gets swallowed and the task keeps running as
if nothing happened.

A safe pattern is to run cleanup inside a `try` and either not catch `CancelledError` at all or
re-raise it:

```python
async def __aexit__(self, exc_type, exc_val, exc_tb):
    try:
        await self.conn.close()
    except asyncio.CancelledError:
        # cleanup already ran above; re-raise so cancellation reaches the task
        raise
```

If the cleanup code itself makes await calls, those can receive `CancelledError` too – wrapping them
in `try/finally` guarantees the resource still closes even when the cancellation arrives exactly
while it is closing.

If code deliberately decides to suppress the cancellation (for example, `__aexit__` returns a truthy
value), it must call `task.uncancel()`, because `asyncio.TaskGroup` and `asyncio.timeout()` count
active cancellation requests and, without that call, will still consider the task
cancelled.[^py314-library-asyncio-task-task-cancellation]

**Common mistakes with `__aexit__` and cancellation:**
- catching `CancelledError` with `except Exception`, assuming it behaves like an ordinary exception;
- catching `CancelledError` for cleanup and forgetting to `raise`, which loses the cancellation;
- suppressing `CancelledError` (`return True`) without calling `task.uncancel()`, which breaks
  `TaskGroup` accounting.

## Environment

TODO

## Deliverable

TODO

## Acceptance criteria

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
