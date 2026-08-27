---
id: py-async-0005
title: "What makes an asyncio Task or callback ready after I/O, a timer, or a suspension point, and which fairness and exact-ordering guarantees can application code not assume?"
description: "What makes an asyncio Task or callback ready after I/O, a timer, or a suspension point, and which fairness and exact-ordering guarantees can application code not assume?"
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/async.md#L204-L259
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**The event loop runs ready callbacks in FIFO order for `call_soon`, but the order of timer
callbacks with the same deadline is unspecified, and there is no strict fairness guarantee between
Tasks.**[^py314-library-asyncio-task] When I/O finishes or a timer fires, the loop adds the
corresponding callback to the ready queue. Callbacks registered via `call_soon` are invoked in
registration order. But for `call_later` / `call_at` with the same timestamp, the order is not
guaranteed. A Task that never yields control via `await` can delay other Tasks indefinitely.

## Detailed explanation

Internally, on every iteration the loop does two things: it polls the selector
(`epoll`/`kqueue`/`select`, depending on the OS) with a timeout up to the nearest scheduled timer,
and moves into the ready queue both the callbacks for file descriptors that became ready and any
timers from its internal heap whose time has already arrived.[^py314-library-asyncio-eventloop]
Only after that does the loop run, in sequence, everything that has piled up in the ready queue at
that point.

A Task resuming after `await` goes through this exact same mechanism, not some separate "task
scheduler". When a Task suspends on a Future, it registers a callback on that Future via
`add_done_callback`. When the Future gets a result (for example, I/O finished), that callback runs
and simply puts the Task's continuation onto the ready queue via `call_soon()`. In other words, a
"waiting" Task is just a callback hanging off an event, not a separate entity with its own priority.

That is the source of the fairness limits. The ready queue does not know how long a Task has been
waiting or how "urgent" it is – the only ordering criterion is FIFO position in the queue of
callbacks for that iteration. Two Tasks woken up in the same iteration run in the order their
`call_soon()` calls happened, not in the order they were created or how important they are. And for
timers with the same `deadline`, the order depends on the internal heap implementation
(insertion-order tie-breaking is not guaranteed by the
specification).[^py314-library-asyncio-eventloop] That means code has no right to assume either
"round-robin across Tasks" or "the timer scheduled first runs first when deadlines tie" – the only
hard guarantee is that callbacks queued via `call_soon` run in the order `call_soon` was called.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
