---
id: py-async-0002
title: "What objects can be awaited, and how are coroutines, Tasks, and Futures related through the awaitable protocol?"
description: "What objects can be awaited, and how are coroutines, Tasks, and Futures related through the awaitable protocol?"
track: python
section: asyncio
level: middle
type: mechanism
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/async.md#L135-L203
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**`await` accepts any awaitable object – a coroutine, a Task, or a Future – that is, an object with
an `__await__` method.**[^py314-library-asyncio-task] A coroutine is the "raw" object produced by
`async def`. A Task is a wrapper around a coroutine that the event loop runs concurrently. A Future
is a low-level primitive representing a future result; Task is a subclass of Future. All three
implement the awaitable protocol, so they are interchangeable inside `await`.

## Detailed explanation

At the bytecode level, `await` effectively means: call `__await__()` on the object, get an
iterator, and resume it until it raises `StopIteration` (whose value becomes the result of `await`)
or some other exception.[^py314-library-asyncio-task] Different types implement that iterator
differently, and that difference is exactly what distinguishes them from one another.

`Future.__await__` is the simplest case: if the result has not been set yet, the method does a
single `yield self`, meaning it returns the Future object itself out to the caller as the
iterator's "intermediate value". This exact yield is what the Task machinery driving a coroutine
recognizes: when a Future (rather than an ordinary value) is yielded from inside a coroutine, the
Task registers an `add_done_callback` on it and suspends itself, rather than treating it as an
error. When the Future gets a result or an exception, the callback resumes `__await__` via
`send`/`throw`, and `StopIteration` ends the wait.

A coroutine object does not yield a Future directly itself – it delegates that down, to the point
where its own code did `await` on something else. So `await` on a coroutine simply drives it as an
iterator, and eventually that chain of `await` inside `await` reaches some Future (most often a
Future representing an I/O event in the selector), which is the only place the "intermediate
suspension" actually comes from.

Task is a subclass of Future, and so it inherits its `__await__`: `await task` behaves the same way
as `await`-ing any Future – it suspends the caller until `task` sets its own result. But internally
a Task is itself a separate driver: it resumes the wrapped coroutine through its own internal
`__step()`, catches every Future that coroutine yields, subscribes to it, and repeats the cycle
until the coroutine finishes – and only then does the Task, as a Future, set its own result, waking
up everything that was waiting on it.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
