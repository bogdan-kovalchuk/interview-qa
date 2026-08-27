---
id: py-async-0008
title: "How can a CPU-heavy coroutine or an unbounded ready queue cause starvation even in a cooperative scheduler?"
description: "How can a CPU-heavy coroutine or an unbounded ready queue cause starvation even in a cooperative scheduler?"
track: python
section: asyncio
level: senior
type: practical
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/async.md#L1305-L1325
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**Even in a cooperative model, a coroutine with a long computation between `await` points holds the
event-loop thread and prevents other Tasks from running, causing starvation.**[^py314-library-asyncio-task]
The fix: break long computations into chunks with `await asyncio.sleep(0)` between them, or offload
CPU-heavy work to a `ProcessPoolExecutor` via `run_in_executor()`. `asyncio.sleep(0)` explicitly
yields control, letting the loop process other ready callbacks.

## Detailed explanation

The event loop is single-threaded and runs exactly one callback at a time: until the current
callback returns control, no other one – not a finished-I/O handler, not a fired timer, not another
Task's continuation – can start running.[^py314-library-asyncio-eventloop] `await` inside a coroutine
is the only point where a Task hands control back to the loop; ordinary computational code with no
`await` never creates that point, so such a fragment runs atomically from the loop's point of view,
no matter how long it takes.

The `ready queue` is the list of callbacks that are already runnable: the results of finished I/O,
fired timers, and anything scheduled directly via `call_soon()` or `create_task()`. The queue has no
priorities – only FIFO order – and the loop drains it in full on every iteration before it polls I/O
again. So an unbounded queue hurts the same way as one CPU-heavy chunk does: if code in a loop
schedules thousands of small callbacks in a row (for example, `create_task()` with no `await` between
calls), an important callback can end up at the back of the queue behind thousands of others, and its
total delay is no different from one long blocking stretch – it is just spread across many small
pieces instead of one big one.

In practice, starvation is spotted in two ways: turning on the loop's debug mode, which logs
callbacks that ran longer than `loop.slow_callback_duration`, or profiling by
hand.[^py314-library-asyncio-dev] The fix is the same regardless of which shape the problem takes –
break the work into chunks with suspension points (`await asyncio.sleep(0)` between loop iterations)
or move the computation somewhere the loop cannot see it: a `ThreadPoolExecutor` for I/O-like waiting,
or a `ProcessPoolExecutor` for genuinely CPU-bound work.

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
