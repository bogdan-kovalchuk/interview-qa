---
id: py-gil-0005
title: "What exactly does the GIL serialize in an ordinary GIL-enabled build of CPython?"
description: "What exactly does the GIL serialize in an ordinary GIL-enabled build of CPython?"
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
  - product: "CPython with GIL"
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/gil_threads_processes.md#L689-L849
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**The GIL serializes the execution of Python bytecode – only one thread at a time executes the
interpreter's bytecode.**[^py314-library-threading] This protects CPython's internal structures
(reference counts, object state) from concurrent access by multiple threads. <span
class="warn">The GIL does not serialize application logic:</span> between any two bytecode
instructions, the GIL can be handed to another thread, so compound operations are not atomic at
the level of Python code.

## Detailed explanation

The GIL (global interpreter lock) is a single mutex for the whole CPython process that must be
held to execute Python bytecode. At any given moment only the thread holding the GIL can execute
interpreter instructions – every other thread that is ready to run waits its
turn.[^py314-library-threading]

The reason the GIL exists is not the multithreading model as such, but CPython's internal
implementation. Reference counting, which CPython uses to manage object memory, is not a
thread-safe operation by itself: incrementing and decrementing a reference count is a
read-modify-write, and without a global lock two threads could simultaneously corrupt the count
for the same object, causing premature deallocation or a leak.[^py314-howto-free-threading-python]

The GIL protects exactly these internal structures – reference counts, the state of lists,
dictionaries, the interpreter itself – not the logic written by the application developer. This is
the key distinction: the GIL makes individual bytecode operations safe at the CPython level, but
guarantees nothing about sequences of operations written by application code.

```python
import sys

x = []
sys.getrefcount(x)  # internal refcount, protected by the GIL from concurrent corruption
```

The CPython scheduler periodically forces the thread holding the GIL to release it – by default
roughly every 5 milliseconds (`sys.setswitchinterval()`) – or immediately when a thread releases
the GIL itself on a blocking call. This gives the illusion of OS-level parallelism, even though
bytecode is still executed by only one thread at a time.

**What exactly is serialized, and what is not:**
- it serializes the execution of the interpreter's bytecode instructions – only one thread
  executes at a time;
- it serializes access to CPython's internal state (reference counts, internal object
  structures) – this is exactly why the GIL exists;
- it does not serialize all Python code as one atomic block – compound expressions made of
  several bytecode instructions can be interrupted between them;
- it does not stop C extensions from explicitly releasing the GIL for the duration of their own
  computation – this is exactly how numpy or a free-threaded build (3.13+) achieve real
  parallelism.[^py314-howto-free-threading-extensions]

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
