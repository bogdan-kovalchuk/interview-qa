---
id: py-gil-0023
title: "When is `threading.local()` better than a shared dictionary keyed by thread ID, and when does it hide unwanted implicit state?"
description: "When is `threading.local()` better than a shared dictionary keyed by thread ID, and when does it hide unwanted implicit state?"
track: python
section: concurrency-and-gil
level: middle
type: comparison
tags: [threading-local]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/gil_threads_processes.md#L987-L1043
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**`threading.local()` is better when you need automatic isolation of data between threads and
automatic cleanup when a thread finishes; a shared dictionary keyed by `threading.get_ident()` is
better when you need explicitness and full control over the structure.**[^py314-library-threading]
Advantages of `threading.local()`: no lock is needed for the storage itself, data is removed
automatically when the thread finishes, and attribute access is more convenient.
<span class="warn">Danger of implicit state:</span> values look like ordinary attributes but are
invisible across threads – this makes debugging harder and can cause bugs if a value from `local` is
passed to another thread. A shared dict needs a lock for updates and manual removal of dead threads'
entries, otherwise it leaks memory.

## Detailed explanation

`threading.local()` is a class that gives each thread its own, isolated copy of its attributes:
setting `local.value = 1` in one thread has no effect on what `local.value` looks like in
another.[^py314-library-threading]

Functionally this resembles a shared dictionary keyed by `threading.get_ident()`, with values holding
each thread's data. The difference is in who is responsible for isolation and cleanup. In
`threading.local()`, isolation is built in: no lock is needed to read or write "your own" value, and
the entry is removed automatically when the thread finishes. With a shared dict, all of that has to
be done by hand: a lock around every access by key, and explicit removal of a dead thread's entry,
or the dictionary grows forever.

An example of two implementations that serve the same purpose but differ in cost:

```python
# threading.local: isolation and cleanup are automatic
local_data = threading.local()
local_data.connection = get_connection()

# shared dict keyed by thread id: isolation and cleanup are manual
connections = {}
connections[threading.get_ident()] = get_connection()
```

**When `threading.local()` wins:**
- the data is genuinely only needed within one thread (for example, a per-thread DB connection or
  request context) and should not "leak" between threads;
- automatic cleanup on thread completion matters, without manually removing entries.

**When a shared dict with an explicit key is better:**
- you need to inspect or tear down the state of all threads at once from another thread (for
  example, for monitoring or graceful shutdown) – `threading.local()` simply does not give you that,
  because each thread only sees its own;
- explicitness matters: code that reads `connections[tid]` immediately shows that this is a
  per-thread structure guarded by a lock, while `local_data`'s attributes look like ordinary
  attributes, and that is exactly the risk.

The danger here is implicit state: `threading.local()` values look like plain object attributes, so
it is easy to forget that they are invisible across threads, and accidentally pass a reference to
`local_data` into another thread, expecting to see the same data there.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
