---
id: py-gil-0014
title: "Why can parallelizing small CPU tasks across processes be slower than sequential execution?"
description: "Why can parallelizing small CPU tasks across processes be slower than sequential execution?"
track: python
section: concurrency-and-gil
level: senior
type: practical
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/gil_threads_processes.md#L1082-L1090
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**The overhead of creating processes, pickling arguments and results, and IPC communication over
pipes exceeds the computation time itself for small tasks.**[^py314-library-threading] Every
`submit()` call on a `ProcessPoolExecutor` requires pickling the callable and its arguments and
sending them through a pipe. If a task runs in microseconds while serialization and communication
take milliseconds, the combined overhead dominates. The fix is to group tasks into larger batches.

## Detailed explanation

Parallelizing across processes has a fixed per-task cost that has nothing to do with the work
itself; when a task is small, that cost dominates the total time, and the parallel version ends up
slower than a plain sequential loop.[^py314-library-concurrent-futures]

The cost is made up of several steps, and each `submit()` (or element in `map()`) pays for them
separately: pickling the callable and its arguments in the parent process, writing the bytes to a
pipe, unpickling them in the worker process, running the task, pickling the result back, and
unpickling it in the parent process. Starting the worker processes themselves is amortized over the
lifetime of the pool, but this serialize/IPC cycle is not - it repeats for every task.

Order of magnitude, pickling and an IPC round trip take tens to hundreds of microseconds even for
simple objects, while a computation like multiplying two numbers takes nanoseconds. So the overhead
can outweigh the useful work by thousands of times.

```python
from concurrent.futures import ProcessPoolExecutor

def square(x):
    return x * x

# naive: one task per element - overhead dominates for cheap work
with ProcessPoolExecutor() as pool:
    results = list(pool.map(square, range(1_000_000)))

# batched: fewer, larger tasks amortize the per-submit overhead
def square_batch(chunk):
    return [x * x for x in chunk]
```

The simplest way to cut this overhead is to group work into larger batches: instead of a million
separate tasks, hand each worker a list of elements and get back a list of results in one pickle
cycle. `ProcessPoolExecutor.map()` does some of this for you through the `chunksize` parameter,
which bundles several elements of the iterable into a single task.[^py314-library-multiprocessing]

**When this is worth worrying about:**
- a task runs in microseconds rather than milliseconds or longer;
- the arguments or the result are large or complex objects that are expensive to serialize;
- the number of `submit()` calls or elements in `map()` is much larger than the number of worker
  processes.

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
