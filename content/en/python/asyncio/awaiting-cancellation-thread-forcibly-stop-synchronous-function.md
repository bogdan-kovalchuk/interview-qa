---
id: py-async-0020
title: "Why can't awaiting cancellation on `to_thread()` forcibly stop a synchronous function already running in the worker thread?"
description: "Why can't awaiting cancellation on `to_thread()` forcibly stop a synchronous function already running in the worker thread?"
track: python
section: asyncio
level: senior
type: pitfall
tags: [to-thread]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/async.md#L938-L1042
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**Python has no mechanism for forcibly stopping a thread; cancellation only cancels the awaitable
on the event loop side, while the worker thread keeps running until the function finishes.**
[^py314-library-asyncio-task] <span class="warn">This means resources (sockets, file descriptors)
can stay held after the cancellation.</span> To get control you need the function itself to
periodically check a cancellation flag or use cooperative signaling.

## Detailed explanation

Cancellation in asyncio works by delivering a `CancelledError` into the coroutine that is waiting
for the result – this is only possible because the coroutine cooperatively hands control back at
every `await`. The worker thread running the function passed to `to_thread()` is not a coroutine: it
executes plain Python bytecode with no points where the event loop could "step in" and substitute
an exception for its execution.[^py314-library-asyncio-task] When the caller cancels the awaiting
Task, the `CancelledError` is raised at the point where the coroutine was waiting on the `Future`
from the thread pool executor – that is, on the main thread, not inside the worker.

The `concurrent.futures.Future` that `to_thread()` wraps only supports `cancel()` while the work has
not yet started running in the worker thread; once `func` has actually started, `cancel()` returns
`False` and has no effect on it – CPython has no safe public API to forcibly interrupt an arbitrary
thread from the outside (an equivalent of a forced kill for arbitrary bytecode is unsafe, because it
could interrupt execution in the middle of holding an internal lock or mutating a data structure).
So the cancellation only "releases" the waiting coroutine with an exception, while the worker thread
itself keeps running until its natural `return` or `raise`, and its result is simply discarded
whenever it eventually arrives.

The practical consequence is that resources opened inside the function (file descriptors, sockets,
locks) stay held for as long as the function itself has not finished, even if the caller received
the `CancelledError` long ago and has moved on; if the function holds, say, a `threading.Lock`, and
execution gets stuck, this can lead to a resource leak that outlives the cancellation itself.

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
