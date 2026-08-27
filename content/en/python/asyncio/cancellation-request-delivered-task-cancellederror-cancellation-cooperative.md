---
id: py-async-0015
title: "How is a cancellation request delivered to a Task as a `CancelledError`, and why is cancellation cooperative?"
description: "How is a cancellation request delivered to a Task as a `CancelledError`, and why is cancellation cooperative?"
track: python
section: asyncio
level: middle
type: mechanism
tags: [cancellederror]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/async.md#L1248-L1289
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**`Task.cancel()` schedules a throw of `CancelledError` into the coroutine at the next `await`, but
the coroutine can catch that exception – which is why cancellation is cooperative.**[^py314-library-asyncio-task]
`CancelledError` is a subclass of `BaseException`. If the coroutine catches it and does not
re-raise, the task is considered to have completed normally rather than cancelled. Proper
cancellation requires either a re-raise or calling `Task.uncancel()` to clear the cancellation
state.

## Detailed explanation

`Task.cancel()` does not raise an exception immediately – it only marks the Task as pending
cancellation and, if the Task is currently awaiting some `Future`, cancels that `Future`. The
`CancelledError` itself only appears in the coroutine at the point of the nearest `await` – until
then the code keeps running as usual, even if cancellation has already been requested.[^py314-library-asyncio-eventloop]
If a suspension point is far away (for example, a long CPU-bound loop with no `await`), delivery is
postponed until the first `await`, or until the coroutine finishes naturally, and `cancel()`
effectively has no effect.

Since 3.11, every call to `cancel()` increments an internal counter that `Task.cancelling()`
returns. This lets you distinguish the case where cancellation was requested multiple times
independently of each other – for instance, both an outer caller and `asyncio.timeout()` at the
same time. `Task.uncancel()` decrements the counter by one; only once it reaches zero does the
task fully leave the cancellation state. Code that deliberately catches `CancelledError` for its
own purposes (`asyncio.timeout()` itself does this when it was its own timeout that fired) must
call `uncancel()` rather than just swallowing the exception – otherwise the outer caller will see
the task as having completed successfully even though it asked for cancellation.

A specific `await` can be shielded from cancellation with `asyncio.shield()`: it wraps the
awaitable in a separate Task, and cancelling the outer coroutine cancels only the shield, not the
inner Task, so the protected operation keeps running in the background to completion even after
whoever was awaiting it has already received a `CancelledError`.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
