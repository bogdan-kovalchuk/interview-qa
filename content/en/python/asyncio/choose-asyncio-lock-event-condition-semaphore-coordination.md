---
id: py-async-0022
title: "How do you choose between `asyncio.Lock`, `Event`, `Condition`, and `Semaphore` for a coordination protocol?"
description: "How do you choose between `asyncio.Lock`, `Event`, `Condition`, and `Semaphore` for a coordination protocol?"
track: python
section: asyncio
level: senior
type: comparison
tags: [asyncio-lock, event, condition, semaphore]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/async.md#L1141-L1186
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**`Lock` is mutual exclusion; `Event` is a "something happened" signal to many Tasks; `Condition`
waits for a state change while holding a lock; `Semaphore` limits how many callers can access a
resource concurrently.**[^py314-library-asyncio-task] `Lock` fits when one Task is modifying a
shared resource. `Event` fits when one Task must tell others it is ready, and `set()` stays in
effect until `clear()`. `Condition` fits when a Task waits for a condition and needs exclusive
access right after waking – the classic producer/consumer case. `Semaphore(N)` caps N concurrent
users of a resource, such as a connection pool or an API throttle.

## Detailed explanation

All four primitives are built on `Future` and are not thread-safe – they are meant for
coordinating Tasks within a single event loop, not threads or processes; sharing one `Lock` object
across two event loops gives unpredictable results.[^py314-library-asyncio-task]

`Condition` effectively wraps a `Lock` (its own or a passed-in one) and adds `wait()`/`notify()`:
`wait()` can only be called while holding the lock, after which the lock is released temporarily
and the Task blocks until someone calls `notify()` or `notify_all()` – and the lock is
automatically reacquired before `wait()` returns. This is what distinguishes `Condition` from a
plain `Event`: `Event` is not tied to any resource and does not guarantee exclusive access after
waking up, whereas `Condition` does guarantee it, because the lock is reacquired before returning
from `wait()`.

`asyncio.Lock` is not reentrant: calling `acquire()` again from the same Task that already holds
the lock leads to a deadlock, unlike `threading.RLock`. Waiters on `Lock` and `Semaphore` are
served in FIFO order, so starvation of an individual Task is not possible in theory, as long as
other Tasks release the resource correctly.

`BoundedSemaphore` is a variant of `Semaphore` that raises `ValueError` if `release()` is called
more times than `acquire()` was; this is useful for catching an "extra release" bug while
developing a connection pool or rate limiter, a case where a plain `Semaphore` would just silently
let its counter grow past the initial value.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
