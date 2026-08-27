---
id: py-async-0016
title: "How does the `asyncio.timeout()` context manager bound an operation's duration, and what exception does the caller see from outside?"
description: "How does the `asyncio.timeout()` context manager bound an operation's duration, and what exception does the caller see from outside?"
track: python
section: asyncio
level: middle
type: mechanism
tags: [asyncio-timeout]
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-library-asyncio-task
    title: "Python 3.14: Library/asyncio Task"
    url: https://docs.python.org/3.14/library/asyncio-task.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-asyncio-eventloop
    title: "Python 3.14: Library/asyncio Eventloop"
    url: https://docs.python.org/3.14/library/asyncio-eventloop.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-asyncio-dev
    title: "Python 3.14: Library/asyncio Dev"
    url: https://docs.python.org/3.14/library/asyncio-dev.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/async.md#L833-L937
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**`asyncio.timeout(delay)` cancels the current task once the deadline is exceeded, and the inner
`CancelledError` is turned into a `TimeoutError`, which the caller sees from outside the context
manager.**[^py314-library-asyncio-task] Inside the block the task sees a plain `CancelledError` – so
it should not be caught inside `async with`. The deadline can be changed via
`cm.reschedule(new_deadline)`.

## Detailed explanation

On entering `async with`, `asyncio.timeout(delay)` schedules a `loop.call_later(delay, callback)`
which, once the deadline arrives, calls `task.cancel()` on the Task running the block's body –
exactly as if an outside `task.cancel()` had been called by someone else.
[^py314-library-asyncio-task] So there is no special exception inside the block – it is a plain
`CancelledError`, which is exactly why catching it inside `async with` is dangerous: code that
catches `CancelledError` for itself hides the fact of cancellation from the event loop, and the
Task might never stop correctly.

The trick happens in `__aexit__`: when a `CancelledError` reaches the edge of the block, the context
manager checks whether this is the exact cancel it itself triggered (via an internal counter,
compared against the Task's state after `task.uncancel()`). If so, it swallows that specific
`CancelledError` and raises a `TimeoutError` in its place, which is what the caller sees outside
`async with`. If the cancellation came from a different source instead (for example, an outside
`task.cancel()` during that same timeout's lifetime, or a nested `asyncio.timeout()` that fired
earlier), `__aexit__` does not substitute the exception – the `CancelledError` propagates onward as
is, because a timeout is only responsible for its own deadline, not for every possible cancellation
of the Task.

The deadline is not fixed forever: `cm.reschedule(new_deadline)` lets you push back the moment it
fires, without leaving the block or creating a new context manager – useful when the time limit
depends on an intermediate result (for example, extending the wait after receiving the first bytes
of a response). The `cm.expired()` method lets you check after the fact whether it was this specific
timeout that caused the block to exit.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
