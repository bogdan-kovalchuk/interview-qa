---
id: py-async-0019
title: "When is `asyncio.to_thread()` appropriate for a blocking function inside an asynchronous application?"
description: "When is `asyncio.to_thread()` appropriate for a blocking function inside an asynchronous application?"
track: python
section: asyncio
level: middle
type: practical
tags: [asyncio-to-thread]
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

**`to_thread()` is appropriate for I/O-bound blocking functions (file operations, blocking
third-party libraries) so they do not block the event loop; for CPU-bound work,
`ProcessPoolExecutor` is better.**[^py314-library-asyncio-task] The function runs in a worker thread
of the default executor (or a custom one). The event loop stays free for other tasks. Keyword
arguments are passed directly, unlike `run_in_executor`, which needs `functools.partial`.

## Detailed explanation

`asyncio.to_thread(func, *args, **kwargs)` is a thin wrapper over `loop.run_in_executor()` using the
loop's default `ThreadPoolExecutor`, which additionally copies the current `contextvars.Context`
into the worker thread, so context variables (for example, ones set via `ContextVar.set()`) remain
visible inside the blocking function.[^py314-library-asyncio-eventloop] Unlike calling
`run_in_executor(None, func, arg1, arg2)` directly, where keyword arguments would have to be passed
through `functools.partial(func, kw=value)`, `to_thread()` accepts `**kwargs` directly – this is a
purely ergonomic difference, the execution mechanics are the same.

Why a thread at all, rather than a plain call inside a coroutine: an I/O-bound blocking call
(reading a file, DNS resolution, a blocking HTTP client) holds the GIL only in short bursts, and
spends most of its time inside a system call with the GIL released while waiting on the OS; while
that thread waits on I/O, the event loop on the main thread can keep running other coroutines. The
default executor is a `ThreadPoolExecutor` with a bounded number of workers
(`min(32, os.cpu_count() + 4)`), so there cannot be an unlimited number of concurrent blocking calls
without explicitly configuring `loop.set_default_executor()`.

For CPU-bound work (heavy computation with no I/O), `to_thread()` does not help: the GIL is not
released between bytecode instructions enough to give real parallelism, so such a thread just
competes with the main thread for the GIL and even adds context-switch overhead. In that case a
separate process is needed, via `ProcessPoolExecutor`, where each worker has its own interpreter and
its own GIL.

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
