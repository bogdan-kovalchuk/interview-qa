---
id: py-async-0001
title: "How do a coroutine function, a coroutine object, and the result of `await` differ from each other?"
description: "How do a coroutine function, a coroutine object, and the result of `await` differ from each other?"
track: python
section: asyncio
level: middle
type: comparison
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/async.md#L17-L43
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**A coroutine function is an `async def` function; a coroutine object is the object that calling
such a function returns; the result of `await` is the value the coroutine returns once it
finishes.**[^py314-library-asyncio-task] Calling an `async def` function does not run its body, it
only creates a coroutine object. For the code to actually run, that object has to be passed to
`await`, `asyncio.create_task()`, or another launch mechanism. The result of `await coro()` is
whatever the coroutine returns via `return`.

## Detailed explanation

If a coroutine object that nobody awaits gets garbage collected while still unstarted, Python
issues a `RuntimeWarning: coroutine '...' was never awaited`, because this is a common mistake: a
developer called an `async def` function, forgot the `await`, and the code silently did
nothing.[^py314-library-asyncio-task] This is what sets a coroutine object apart from an ordinary
function call: an ordinary function runs immediately when called, while a coroutine object only
reserves state (an execution frame) and waits for something to start "advancing" it via `await` or
an equivalent.

Every call to an `async def` function creates a new, independent coroutine object with its own
frame – two calls to the same function with the same arguments do not share state. At the same
time, the same coroutine object cannot be awaited twice: once it has finished, awaiting it again
raises a `RuntimeError` ("cannot reuse already awaited coroutine"), because its internal frame has
already been released.

Awaiting a coroutine object runs it synchronously within the current Task – it does not create a
new unit of scheduling, it just "inlines" the coroutine's logic into whatever is awaiting it. By
contrast, `asyncio.create_task(coro())` registers the coroutine with the event loop as a separate
Task that runs concurrently with the rest of the code, and the result of `await`-ing that Task is
the same `return` value, but obtained after the Task got to run alongside other code, rather than
immediately in the same call frame.[^py314-library-asyncio-eventloop]

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
