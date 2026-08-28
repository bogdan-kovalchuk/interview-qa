---
id: py-gil-0012
title: "When is `ThreadPoolExecutor` an appropriate choice for an I/O-bound workload?"
description: "When is `ThreadPoolExecutor` an appropriate choice for an I/O-bound workload?"
track: python
section: concurrency-and-gil
level: middle
type: practical
tags: [threadpoolexecutor]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/gil_threads_processes.md#L940-L986
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**`ThreadPoolExecutor` is a good fit when a task spends most of its time waiting for external
responses (network, disk, a database) rather than computing.**[^py314-library-threading] In
GIL-enabled CPython, threads can wait on I/O in parallel because the GIL is released during system
calls. The default number of workers is `min(32, os.process_cpu_count() + 4)`, sized specifically
for I/O-bound workloads. For CPU-bound tasks, threads do not give real parallelism because of the
GIL.

## Detailed explanation

`ThreadPoolExecutor` is a pool of worker threads from `concurrent.futures` that runs callables from
a task queue and returns a `Future` for each call.[^py314-library-concurrent-futures]

It fits I/O-bound workloads specifically because the GIL is released during system calls: while one
thread waits for a response from the network, disk, or a database, the GIL can move to another
thread, and several I/O operations effectively proceed at the same time even in a regular
GIL-enabled CPython.[^py314-howto-free-threading-python]

An example of typical use – parallel network requests:

```python
from concurrent.futures import ThreadPoolExecutor

def fetch(url):
    ...  # a blocking network call; the GIL is released while waiting

with ThreadPoolExecutor(max_workers=8) as pool:
    results = list(pool.map(fetch, urls))
```

The default number of workers, when `max_workers` is not given, is `min(32,
os.process_cpu_count() + 4)`. This number is explicitly sized for I/O-bound tasks: it is
significantly larger than the core count, because the threads spend most of their time waiting, not
computing.[^py314-library-concurrent-futures]

For CPU-bound work, the same pool gives no speed-up: the GIL is not released during computation in
pure Python code, so the threads execute bytecode in turn, and the overhead of context switching
only adds up. `ProcessPoolExecutor` fits that kind of work instead, bypassing the GIL at the cost of
a separate process and data serialization for each call.

**Signs that `ThreadPoolExecutor` is the right choice:**
- the task spends most of its time waiting (network, disk, a database, an external process) rather
  than computing;
- shared access to process memory is needed, without IPC or serialization;
- the number of concurrent tasks is moderate, and thread overhead is not critical.

**Signs that something else is a better fit:**
- the computation is CPU-bound – then `ProcessPoolExecutor` or a free-threaded build is needed;
- there are very many tasks and they mostly wait on the network – then `asyncio` scales better than
  threads with their fixed number of workers.

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
