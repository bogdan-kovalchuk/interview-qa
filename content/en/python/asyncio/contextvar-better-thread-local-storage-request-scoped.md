---
id: py-async-0023
title: "Why is `ContextVar` better than thread-local storage for request-scoped state across asyncio Tasks?"
description: "Why is `ContextVar` better than thread-local storage for request-scoped state across asyncio Tasks?"
track: python
section: asyncio
level: middle
type: comparison
tags: [contextvar]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/async.md#L1443-L1542
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**`ContextVar` isolates a value by logical context (Task), not by physical thread, so several
Tasks in the same thread do not "leak" into each other.**[^py314-library-asyncio-task]
`threading.local()` ties state to an OS thread; in asyncio, many Tasks run on a single thread and
would see the same thread-local value. `asyncio.create_task()` automatically copies the current
`Context` into the new Task, so each Task has its own `ContextVar` values (for example, request_id,
tenant). Changing a `ContextVar` in one Task does not affect other Tasks, even if they run on the
same thread.

## Detailed explanation

Technically, `Context` is an immutable map: `ContextVar.set()` does not mutate the existing
context, it creates a new value in the current execution context and returns a `Token` that can be
passed to `reset()` to restore the previous value. A coroutine, Task, or callback always runs
inside some `Context`; when `asyncio.create_task()` creates a new Task, it gets a **copy** of the
current `Context` at creation time – a snapshot, not a shared reference.[^py314-library-asyncio-task]

There is an important nuance here that the short answer does not cover: inheritance is one-way. A
child Task sees the `ContextVar` values the parent Task set **before** `create_task()` was called,
but changing a `ContextVar` inside the child Task never propagates back to the parent – each Task
works with its own copy, not a shared mutable store. This differs from `threading.local()` only
terminologically, in the copy-on-fork detail, not in behaviour: `threading.local()` is also not
shared between threads, but it is tied to the OS thread rather than to the logical unit of
execution, so inside one thread running several Tasks, all of them would see the same
`threading.local()` value, whereas `ContextVar` tells them apart.

There is one trap: if code runs a callback via `loop.call_soon()` or dispatches work to
`run_in_executor()`, `Context` is copied automatically only for `call_soon`/`call_later`/Task, and
an explicit call into a `ThreadPoolExecutor` runs on a foreign thread with no automatic `Context`
transfer – to get the same values there, the call has to be wrapped in
`contextvars.copy_context().run(...)`.[^py314-library-asyncio-eventloop]

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
