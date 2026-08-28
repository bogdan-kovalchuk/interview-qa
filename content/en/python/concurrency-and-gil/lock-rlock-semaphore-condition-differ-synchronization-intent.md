---
id: py-gil-0016
title: "How do `Lock`, `RLock`, `Semaphore`, and `Condition` differ in synchronization intent?"
description: "How do `Lock`, `RLock`, `Semaphore`, and `Condition` differ in synchronization intent?"
track: python
section: concurrency-and-gil
level: middle
type: comparison
tags: [lock, rlock, semaphore, condition]
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

**`Lock` provides mutual exclusion (one thread in the critical section); `RLock` is a reentrant lock
that the same thread can reacquire; `Semaphore` is a counter limiting the number of concurrent
entries; `Condition` waits for a state change via notify/notify_all.**[^py314-library-threading] Any
thread can release a `Lock`; an `RLock` can only be released by its owning thread, with a matching
number of `release()` calls. `Semaphore` suits resource pools (a connection pool, for example).
`Condition` is for producer-consumer patterns, where one thread waits for a signal from another.

## Detailed explanation

In the `threading` module, each synchronization primitive expresses a different intent, not just a
different API: they differ in which property of a shared resource they protect, not only in call
details.[^py314-library-threading]

`Lock` and `RLock` both implement mutual exclusion, but for different scenarios. `Lock` can only be
acquired once; acquiring it again from the same thread deadlocks. `RLock` keeps an internal count of
acquisitions and an owning thread: the same thread can reacquire it without blocking, but must call
`release()` the same number of times. `RLock` exists specifically for recursive functions or methods
that call one another while holding the same lock.

`Semaphore` expresses a different intent - not "one thread at a time" but "no more than N threads at
a time". That is the natural choice for limiting access to a fixed-size resource pool (for example, a
connection pool). `BoundedSemaphore` adds a check: if `release()` is called more often than
`acquire()`, it raises an exception, whereas a plain `Semaphore` silently lets the counter grow past
its initial value, hiding a bug.

`Condition` solves a different problem - waiting for a state change, not just acquiring a resource.
It is built on top of `Lock` (or `RLock`) and adds `wait()`/`notify()`/`notify_all()`: a waiting
thread atomically releases the underlying lock while it waits and reacquires it on waking. This is
the basis of the producer-consumer pattern:

```python
condition = threading.Condition()
queue = []

def consumer():
    with condition:
        while not queue:
            condition.wait()
        item = queue.pop(0)
```

**Common mistakes:**
- using `Lock` where a recursive call from the same thread needs `RLock`, causing a self-deadlock;
- using a plain `Semaphore` for a resource pool where a `BoundedSemaphore` is needed to catch extra
  `release()` calls as an error instead of silently hiding them;
- calling `notify()` or `wait()` outside a `with condition` block, which raises `RuntimeError`;
- checking the condition with `if` instead of `while` around `condition.wait()`, ignoring spurious
  wakeups.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
