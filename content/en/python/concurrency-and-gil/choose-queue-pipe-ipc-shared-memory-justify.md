---
id: py-gil-0022
title: "When should you choose a queue or a pipe for IPC, and when does shared memory justify the extra synchronization complexity?"
description: "When should you choose a queue or a pipe for IPC, and when does shared memory justify the extra synchronization complexity?"
track: python
section: concurrency-and-gil
level: middle
type: comparison
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/gil_threads_processes.md#L126-L420
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**`Queue` and `Pipe` are message passing with built-in synchronization; shared memory is justified
only when the serialization overhead for large data is a real bottleneck.**[^py314-library-threading]
`multiprocessing.Queue` supports many producers/consumers and serializes objects via `pickle`.
`Pipe` is more efficient for two processes but does not guarantee integrity when reading and
writing the same end concurrently. `SharedMemory`, `Array`, and `Value` give zero-copy access
without serialization, but any shared mutation requires explicit locks (even `counter.value += 1`
is not atomic). Documentation favors message passing over shared state where possible.

## Detailed explanation

IPC (inter-process communication) in `multiprocessing` is a way to pass data between processes
that do not share memory by default. Message passing (`Queue`, `Pipe`) and shared memory are two
fundamentally different approaches to this problem, with different costs and different
guarantees.

`multiprocessing.Queue` is implemented on top of a `Pipe` and a background feeder thread: every
item put on the queue is serialized via `pickle`, sent through an OS channel, and deserialized on
the other end.[^py314-library-multiprocessing] This makes `Queue` convenient for an arbitrary
number of producers and consumers, and safe for concurrent use from multiple processes without
extra locks on the caller's side.

`Pipe` is a lower-level primitive: it gives a pair of connected ends for exchange between exactly
two processes. It is faster than `Queue`, since it has no feeder thread and no extra in-memory
queue, but it does not guarantee data integrity if several processes concurrently write to or read
from the same end – the documentation warns about this directly.

Example of passing a large array through shared memory instead of serialization:

```python
from multiprocessing import shared_memory

shm = shared_memory.SharedMemory(create=True, size=array.nbytes)
buf = np.ndarray(array.shape, dtype=array.dtype, buffer=shm.buf)
buf[:] = array[:]  # zero-copy: no pickle round-trip
```

`SharedMemory`, `Array`, and `Value` give zero-copy access to a single block of memory from all
processes, avoiding the cost of serializing large objects. The price is losing built-in
synchronization: any shared mutation (even incrementing a counter) requires an explicit `Lock`,
because an operation on shared memory is not atomic by itself.

**When shared memory is justified:**
- the data is large (arrays, buffers), and the serialization overhead measurably dominates
  computation time;
- access is mostly read-only, or updates are rare and easy to protect with a single lock;
- what is actually needed is zero-copy access, not just "a faster channel".

In other cases `Queue` or `Pipe` are simpler, safer by default, and that is exactly why the
documentation recommends them as the primary way to exchange data between
processes.[^py314-library-multiprocessing]

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
