---
id: py-async-0003
title: "Why doesn't simply creating several coroutine objects already run them concurrently?"
description: "Why doesn't simply creating several coroutine objects already run them concurrently?"
track: python
section: asyncio
level: middle
type: pitfall
tags: []
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/async.md#L590-L652
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**Calling an `async def` function only creates a coroutine object, but does not schedule it to run –
the code will not run until the object is `await`-ed or passed to
`asyncio.create_task()`.**[^py314-library-asyncio-task] Sequentially `await`-ing several coroutines
runs them one after another, not in parallel. True concurrency requires creating a Task for each
coroutine so the event loop can switch between them at suspension points.

## Detailed explanation

Calling an `async def` function does not run a single line of its body. Technically it creates a
coroutine object – a state machine similar to a generator, with its own frame that has never been
executed. The body only starts running once something calls `send(None)` on that object (which is
exactly what `await` or an event-loop step does), and it stops at the first point where the body
itself `await`s something else.[^py314-library-asyncio-task] If a coroutine object is created and
never driven – neither directly nor through a Task – the interpreter emits a
`RuntimeWarning: coroutine '...' was never awaited` during garbage collection, because that is
almost always a logic error rather than intended behavior.

`await coro` and `create_task(coro)` start execution differently. `await` drives the coroutine in
the current Task's context: the code immediately starts running the coroutine's body synchronously,
up to its first internal suspension point, and the line after `await` does not run until that
coroutine finishes completely. `create_task()`, by contrast, only registers a new Task with the loop
and returns control to the caller right away – the coroutine's body itself only starts running later,
when the loop reaches that Task in its queue, possibly even after the caller has already moved on to
the next lines.

That difference explains the behavior for several coroutines in a row: `await a(); await b()` runs
`a` to completion, then `b` to completion – sequential execution on one logical line, even though
both are async. But `t1 = create_task(a()); t2 = create_task(b()); await t1; await t2` lets the loop
switch between `a` and `b` at each of their internal suspension points, so work waiting on I/O in one
does not block progress in the other.

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
