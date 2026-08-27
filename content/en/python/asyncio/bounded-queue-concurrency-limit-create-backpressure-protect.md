---
id: py-async-0024
title: "How do a bounded queue and a concurrency limit create backpressure and protect an async service from unbounded fan-out?"
description: "How do a bounded queue and a concurrency limit create backpressure and protect an async service from unbounded fan-out?"
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

**A bounded `asyncio.Queue(maxsize=N)` suspends the producer on `await put()` when the queue is
full, and `Semaphore(limit)` caps concurrent operations – together they stop a service from piling
up unbounded pending work.**[^py314-library-asyncio-task] A producer calling `await
queue.put(item)` waits until a consumer frees a slot via `get()` – natural backpressure.
`Semaphore` adds to this by limiting concurrent outbound calls, e.g. HTTP requests to a database:
once its counter is exhausted, new Tasks wait on `acquire()`. Without these, a fast producer or a
burst of requests can exhaust memory or overload downstream.

## Detailed explanation

`asyncio.Queue` implements backpressure not through some special mechanism but through a plain
`await`: when `put()` is called on a full queue (`maxsize` already reached), the producer's
coroutine suspends on an internal `Future` added to a queue of waiters, and no more of the
producer's bytecode runs until a consumer calls `get()` and frees a slot.
[^py314-library-asyncio-task] That is the essence of backpressure: the rate at which the producer
can generate new work is mechanically tied to the rate at which the consumer takes it, rather than
running independently.

`Semaphore(limit)` operates at a different level: it does not buffer incoming items, it limits how
many coroutines can be simultaneously between `acquire()` and `release()`. An internal counter is
decremented on every `acquire()`; once it reaches zero, further `acquire()` calls suspend on a FIFO
queue of waiters, and every `release()` wakes exactly one next waiter. This limits not the amount of
accumulated work but the amount of work actually running in parallel (for example, concurrent HTTP
requests to one backend).

Together these two mechanisms close two different gaps: without a bounded queue, a producer faster
than the consumer accumulates pending items in memory without limit (for example, a plain unbounded
`Queue` keeps growing until the process crashes from running out of memory); without a semaphore,
even a bounded queue does not stop a consumer from launching an unbounded number of concurrent
downstream calls as soon as items show up in the queue, overloading a database or an external
service with a burst of requests. A bounded queue limits *accumulated* work, a semaphore limits
*concurrently running* work – both layers of protection are needed, because they act on different
parts of the pipeline.

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
