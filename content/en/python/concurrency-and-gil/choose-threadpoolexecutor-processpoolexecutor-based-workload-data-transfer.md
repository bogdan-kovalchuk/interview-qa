---
id: py-gil-0019
title: "How do you choose between `ThreadPoolExecutor` and `ProcessPoolExecutor` based on workload, data-transfer cost, and failure model?"
description: "How do you choose between `ThreadPoolExecutor` and `ProcessPoolExecutor` based on workload, data-transfer cost, and failure model?"
track: python
section: concurrency-and-gil
level: middle
type: comparison
tags: [threadpoolexecutor, processpoolexecutor]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/gil_threads_processes.md#L1344-L1416
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**`ThreadPoolExecutor` is for I/O-bound tasks with minimal overhead (shared memory, no
serialization); `ProcessPoolExecutor` is for CPU-bound pure-Python tasks that need to get around
the GIL.**[^py314-library-threading] Data-transfer cost: threads share memory, processes require
pickling arguments and results across pipes. Failure model: `BrokenProcessPool` occurs when a
worker process crashes and makes the executor unusable; with threads the failure of one worker is
less destructive. For CPU-bound work on free-threaded CPython (3.13+), threads can also give
parallelism without process overhead.

## Detailed explanation

`ThreadPoolExecutor` and `ProcessPoolExecutor` share the same interface (`submit`, `map`,
`Future`), so choosing between them is not a question of API convenience but of what actually
bounds the workload and how much it costs to hand data to a
worker.[^py314-library-concurrent-futures]

For I/O-bound tasks (network requests, file reads, database calls) threads are the better fit: all
workers are in the same process and share memory, so passing arguments and results needs no
serialization. The GIL is released for the duration of blocking I/O, so threads genuinely overlap
while waiting.

For CPU-bound pure-Python code (parsing, computation in loops) threads give no speedup, because
the GIL serializes bytecode execution. `ProcessPoolExecutor` creates separate processes, each with
its own GIL, so computation actually runs in parallel across multiple
cores.[^py314-library-multiprocessing]

Example where the choice of executor depends on the nature of the task:

```python
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

with ThreadPoolExecutor() as pool:
    pool.map(fetch_url, urls)          # I/O-bound: threads are enough

with ProcessPoolExecutor() as pool:
    pool.map(cpu_heavy_parse, chunks)  # CPU-bound: needs separate interpreters
```

The data-transfer cost for `ProcessPoolExecutor` is real: arguments and results get pickled and
sent through pipes, so passing large objects (a DataFrame, arrays) can wipe out the gain from
parallelism. Threads have no such cost – only a reference to the object is passed.

The failure model also differs. If a worker process crashes (say, a segfault in a C extension),
`ProcessPoolExecutor` raises `BrokenProcessPool` for all futures, and the executor itself becomes
unusable for further work.[^py314-library-concurrent-futures] In `ThreadPoolExecutor`, one
worker's failure is less destructive: it lands on the specific `Future` as an exception, and the
pool keeps accepting new tasks.

**When to reconsider the default choice:**
- on free-threaded CPython (3.13+, no GIL) threads can give real parallelism even for CPU-bound
  code, without the cost of separate processes;[^py314-howto-free-threading-python]
- if the CPU-bound computation is done by a C extension that releases the GIL (numpy, for
  example), threads can be effective even on a GIL-enabled build.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
