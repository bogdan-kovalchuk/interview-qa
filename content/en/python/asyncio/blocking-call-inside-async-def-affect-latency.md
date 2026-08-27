---
id: py-async-0007
title: "How does one blocking call inside `async def` affect the latency of every other Task on the same loop?"
description: "How does one blocking call inside `async def` affect the latency of every other Task on the same loop?"
track: python
section: asyncio
level: senior
type: practical
tags: [async-def]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/async.md#L1222-L1247
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**Any synchronous blocking call (for example, `time.sleep()`, file I/O, or CPU-bound computation)
stops the event loop for the whole duration it runs, delaying every other Task and I/O event.**
[^py314-library-asyncio-task] The fix is to move the blocking operation into a separate thread or
process via `asyncio.to_thread()` or `loop.run_in_executor()`. Debug mode logs callbacks that run
longer than `slow_callback_duration` (100 ms by default).

## Detailed explanation

The asyncio event loop is single-threaded and cooperative: at any given moment at most one piece of
Python bytecode is executing, and switching between Tasks happens only at `await` points, where a
coroutine explicitly hands control back to the loop.[^py314-library-asyncio-eventloop] A blocking
call – `time.sleep()`, synchronous file I/O, a synchronous DB driver, heavy CPU computation –
contains no such point: it is an ordinary function call that runs to completion before returning
control. For as long as that call runs, the loop physically cannot do anything else: no other `Task`
gets CPU time, no selector callback for a ready socket fires, and even an `asyncio.sleep()` whose
timer has already expired does not return control to its Task, because the loop never gets to
process that callback.

The consequence is that the latency of **every** pending operation on that same loop grows by at
least the duration of the blocking call, no matter how many Tasks were waiting: five Tasks that were
each due to wake up in 10 ms are all delayed equally if a 500 ms blocking call runs somewhere at
that same moment. This differs from blocking in a multithreaded model, where the OS can preempt a
long-running thread; asyncio has no such forced preemption at all.

The fix is to move the blocking call somewhere that does not occupy the loop's thread:
`asyncio.to_thread()` or `loop.run_in_executor()` for I/O-bound work, `ProcessPoolExecutor` for
CPU-bound work. For diagnosis, the event loop's debug mode helps: if enabled
(`asyncio.run(main(), debug=True)` or `PYTHONASYNCIODEBUG=1`), the loop logs a warning for any
callback that ran longer than `slow_callback_duration` (100 ms by default) – a direct way to find
the blocking call that is quietly wrecking the rest of the system's latency.
[^py314-library-asyncio-dev]

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
