---
id: py-gil-0018
title: "When one thread has to hand a sequence of jobs and results to another, why does `queue.Queue` give a clearer hand-off contract than a shared list without a lock?"
description: "When one thread has to hand a sequence of jobs and results to another, why does `queue.Queue` give a clearer hand-off contract than a shared list without a lock?"
track: python
section: concurrency-and-gil
level: senior
type: comparison
tags: [queue-queue]
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-library-threading
    title: "Python 3.14: Library/threading"
    url: https://docs.python.org/3.14/library/threading.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-multiprocessing
    title: "Python 3.14: Library/multiprocessing"
    url: https://docs.python.org/3.14/library/multiprocessing.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-concurrent-futures
    title: "Python 3.14: Library/concurrent.futures"
    url: https://docs.python.org/3.14/library/concurrent.futures.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-howto-free-threading-python
    title: "Python 3.14: Howto/free Threading Python"
    url: https://docs.python.org/3.14/howto/free-threading-python.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-howto-free-threading-extensions
    title: "Python 3.14: Howto/free Threading Extensions"
    url: https://docs.python.org/3.14/howto/free-threading-extensions.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/gil_threads_processes.md#L126-L420
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**`queue.Queue` implements internal locking for all `put()`/`get()` operations, giving a thread-safe
hand-off without explicit locks.**[^py314-library-threading] A shared list without a lock leaves the
developer to synchronize access manually; even individual operations like `list.append()` do not
guarantee application-level atomicity for more complex protocols. `Queue` also supports `maxsize`
for backpressure, blocking the producer when the queue is full, and gives a clear contract: each
item goes to exactly one consumer.

## Detailed explanation

`queue.Queue` is a FIFO queue with a thread-safe interface: inside every call to `put()` and
`get()` it acquires and releases its own internal lock, so the calling code needs no extra
synchronization.[^py314-library-threading]

A shared list without a lock, in contrast, gives no contract at all. Individual calls like
`list.append()` or `list.pop(0)` are safe on their own, but a sequence of several such calls is not.
If one thread checks `if my_list:` before `pop(0)`, and another thread manages to take the last
element in between the check and the `pop`, a race condition and an `IndexError` follow.

An example of a hand-off without and with `Queue`:

```python
# fragile: check-then-act on a shared list
if job_list:
    job = job_list.pop(0)  # another thread may empty the list in between

# robust: Queue blocks and hands off exactly one item per get()
job = job_queue.get()
```

`Queue` also adds what a plain list does not have: `put()` can block once the queue reaches
`maxsize`, which gives simple backpressure – the producer slows down when the consumer cannot keep
up. There is also `task_done()` and `join()`, which let the producer wait until every submitted job
has been processed.[^py314-library-threading]

**What a shared list without an explicit protocol does not give you:**
- a guarantee that each job reaches exactly one consumer, not zero or two at once;
- a "queue is empty, wait" signal instead of a busy-wait loop checking the list's length;
- backpressure when the producer runs faster than the consumer;
- one place where the whole hand-off contract is visible, instead of checks and locks scattered
  around a list.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
