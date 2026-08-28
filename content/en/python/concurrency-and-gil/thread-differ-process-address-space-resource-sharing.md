---
id: py-gil-0002
title: "How does a thread differ from a process in address space, resource sharing, and failure isolation?"
description: "How does a thread differ from a process in address space, resource sharing, and failure isolation?"
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/gil_threads_processes.md#L29-L64
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**A thread runs inside its parent process and shares the same address space; a process has its own,
isolated address space.**[^py314-library-threading] Threads share the heap, loaded modules, and open
file descriptors, while each process gets its own copy of memory and needs IPC (pickling through
`Queue`/`Pipe`, shared memory through `Value`/`Array`). A crash in one thread (an unhandled
exception) terminates the whole process; a crash in a separate process is isolated – the parent
process keeps running.

## Detailed explanation

A thread is a unit of execution inside one process; several threads of the same process share one
and the same address space, while each process gets its own, isolated address space – a separate
memory mapping managed by the operating system.[^py314-library-threading]

Because of the shared address space, threads see the same objects in memory: a variable, a list, or
a dict created in one thread is accessible from another without any copying or serialization. This
is cheap and fast, but it is exactly why it requires explicit synchronization for shared mutable
state.

A process, by contrast, is isolated at the memory level by the operating system: two processes
cannot simply read each other's variables. Data exchange between them goes through IPC –
`multiprocessing.Queue`, `Pipe`, or shared memory (`Value`, `Array`) – and in most cases the data is
serialized (`pickle`) before it is sent.[^py314-library-multiprocessing]

Example: creating a worker as a thread and as a process looks almost identical in code, but the
memory behaviour differs:

```python
import threading
import multiprocessing

def worker(shared_list):
    shared_list.append(1)  # visible to the parent immediately for a thread,
                            # needs a Manager/shared memory for a process

t = threading.Thread(target=worker, args=([],))
p = multiprocessing.Process(target=worker, args=([],))
```

The difference also shows up on failure. An unhandled exception in a non-main thread terminates only
that thread; the rest of the process keeps running, though the shared memory state may end up
inconsistent. A process that crashes or is killed (for example, by the OOM killer) does not touch
the memory of its parent or of other processes – the OS simply frees its address space.

**The main consequences of this difference:**
- threads are cheaper to create and switch between, but need locks or queues for safe access to
  shared data;
- processes are more expensive and need serialization to exchange data, but give real failure
  isolation and bypass the GIL for CPU-bound work;[^py314-library-multiprocessing]
- the choice between them is a trade-off between cheap shared state and safe isolation.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
