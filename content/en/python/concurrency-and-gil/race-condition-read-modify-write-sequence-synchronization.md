---
id: py-gil-0015
title: "What is a race condition on a read-modify-write sequence, and why is a synchronization primitive needed?"
description: "What is a race condition on a read-modify-write sequence, and why is a synchronization primitive needed?"
track: python
section: concurrency-and-gil
level: middle
type: mechanism
tags: []
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  uk: 2
applies_to:
  - product: "CPython"
    version: null
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/gil_threads_processes.md#L559-L688
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**A race condition occurs when several threads perform a read-modify-write on a shared resource
without synchronization, and the outcome depends on the interleaving order of the
operations.**[^py314-library-threading] For example, `counter += 1` is three operations: read,
increment, write. If two threads read the same value at the same time, one increment is lost. Even
in CPython with the GIL, bytecode instructions can be interrupted between operations, so a `Lock` or
another synchronization primitive is needed for atomicity at the application level.

## Detailed explanation

A race condition is a situation where the outcome of execution depends on the exact order in which
operations from several threads (or processes) interleave over one shared resource, and at least
one of them modifies that resource.[^py314-library-threading]

It shows up most often on a read-modify-write sequence: read a value, compute a new one, write it
back. These are three separate steps even when the code looks like a single expression, and the
scheduler can switch threads between any two of them.

An example of a race condition on a simple counter without synchronization:

```python
counter = 0

def increment():
    global counter
    for _ in range(100_000):
        counter += 1  # read, add 1, write - not atomic
```

If two threads call `increment()` at the same time, the final value of `counter` will almost
certainly be less than 200000: both threads manage to read the old value before either writes the
new one, and one increment is lost.

CPython has the GIL, which guarantees that a single bytecode instruction executes atomically, but
the expression `counter += 1` compiles to several bytecode instructions (load, add, store), and the
GIL can switch threads between them.[^py314-howto-free-threading-python] So the GIL protects against
corrupting an object's internal structure, but it does not protect against logical race conditions
at the application level.

**How to fix a race condition on a read-modify-write sequence:**
- wrap the whole read-modify-write sequence in a `threading.Lock` (or `RLock`) to make it atomic at
  the application level;
- replace the shared mutable state with a structure that already guarantees atomicity for the
  operation you need, such as `queue.Queue`, or move the state into a separate process;
- keep in mind that on a free-threaded build (without the GIL) this problem gets more relevant, not
  less: even the accidental protection from being interrupted between bytecode instructions is
  gone.[^py314-howto-free-threading-python]

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
