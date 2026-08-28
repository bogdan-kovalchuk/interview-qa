---
id: py-gil-0017
title: "What conditions create a deadlock, and how does lock ordering reduce the risk?"
description: "What conditions create a deadlock, and how does lock ordering reduce the risk?"
track: python
section: concurrency-and-gil
level: senior
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/gil_threads_processes.md#L421-L483
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**A deadlock occurs when two or more threads block forever, each waiting for a resource held by
another; the classic condition is a circular wait on locks acquired in different
order.**[^py314-library-threading] If thread A holds Lock1 and waits for Lock2, while thread B
holds Lock2 and waits for Lock1, neither can proceed. Lock ordering reduces the risk: if all
threads acquire locks in a single global order (for example, always Lock1 before Lock2), a cycle
becomes impossible. Additionally, use `with` to guarantee release and a timeout on `acquire()`.

## Detailed explanation

A deadlock is a state where several threads wait on each other forever and none can proceed.
Classically this requires four conditions at once: mutual exclusion (a resource belongs to only
one owner at a time), hold-and-wait (a thread holds one lock while waiting for another), no
preemption (a lock cannot be taken away from outside), and a circular wait. Removing any one of
these conditions is enough to make a deadlock impossible.[^py314-library-threading]

In practice, the circular wait is the easiest one to remove, which is why it names the typical
scenario: two threads acquire two locks in opposite order.

```python
import threading

lock_a = threading.Lock()
lock_b = threading.Lock()

def thread_1():
    with lock_a:
        with lock_b:  # waits for lock_b, held by thread_2
            ...

def thread_2():
    with lock_b:
        with lock_a:  # waits for lock_a, held by thread_1
            ...
```

If `thread_1` manages to acquire `lock_a` and `thread_2` acquires `lock_b`, each is waiting for a
resource the other holds, and neither will release its own. Neither a default timeout nor the GIL
prevents this – the GIL only governs bytecode execution, not the order in which locks are
acquired.

Lock ordering removes the possibility of a cycle: if every thread in the program acquires several
locks always in the same global order (for example, by object id, or by a predefined list), a
wait cycle cannot form, because a thread will never wait on a lock that comes "earlier" than one
it already holds.

**Other ways to lower deadlock risk:**
- use `with lock:` instead of manual `acquire()`/`release()`, so the lock is always released even
  on an exception;
- pass a `timeout` to `acquire()` and handle the failure instead of waiting forever;
- minimize the number of locks that must be held at once by narrowing the critical section;
- where possible, replace several small locks with one lock that covers the whole related state.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
