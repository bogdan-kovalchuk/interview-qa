---
id: py-async-0013
title: "When should you choose `wait()`, and when `as_completed()`, for handling a set of concurrent operations?"
description: "When should you choose `wait()`, and when `as_completed()`, for handling a set of concurrent operations?"
track: python
section: asyncio
level: middle
type: comparison
tags: [wait, as-completed]
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

**`wait()` returns two sets `(done, pending)` and fits controlling completion via `return_when`;
`as_completed()` returns an iterator of results in the order they finish – convenient for streaming
processing.**[^py314-library-asyncio-task] That said, `wait()` does not cancel pending tasks on
timeout and only accepts Task/Future (not a coroutine). And `as_completed()` likewise does not
cancel tasks when iteration stops, but it gives results as soon as they are ready, which is better
for progress bars or early-exit scenarios.

## Detailed explanation

`wait()` accepts a `return_when` parameter with three modes: `ALL_COMPLETED` (the default) waits
for everything, `FIRST_COMPLETED` returns as soon as the first task finishes, and
`FIRST_EXCEPTION` returns as soon as some task finishes with an exception (or once everything
finishes without one). In all three cases `wait()` itself does not cancel anything and does not
raise – each task's exception has to be retrieved manually via `task.exception()` or
`task.result()`, otherwise it just sits silently in the `done` set.[^py314-library-asyncio-task]

Historically `wait()` accepted both coroutines and Task/Future objects, but passing bare coroutines
directly was deprecated and removed: arguments now have to already be wrapped in a Task (for
example via `asyncio.create_task()`), otherwise `wait()` raises `TypeError`.[^py314-library-asyncio-dev]
This is an important difference from `as_completed()`, which still accepts an awaitable of any
kind and wraps it in a Task itself when needed.

`as_completed()` does not return the results themselves, but awaitable wrappers in completion
order; getting the result or exception of a specific operation requires `await`-ing each element of
the iterator, and that is where (not when the element is pulled from the iterator) an exception
surfaces if the task failed. If the code exits the `for` loop early (for example via `break` after
finding the first result it needed), the remaining tasks keep running in the background –
`as_completed()` has no way to cancel them automatically; that is the caller's responsibility.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
