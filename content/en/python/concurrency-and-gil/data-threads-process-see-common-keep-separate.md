---
id: py-gil-0003
title: "Which data do threads within one process see in common, and which must they keep separate?"
description: "Which data do threads within one process see in common, and which must they keep separate?"
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/gil_threads_processes.md#L3-L28
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**Threads see all heap objects in common (global variables, module state, mutable containers) and
open file descriptors, but each thread has its own call stack, local variables, and
registers.**[^py314-library-threading] `threading.local()` is used for isolated state – its values
are bound to a specific thread and are not visible to others. The absence of explicit state
separation is the main source of race conditions.

## Detailed explanation

Threads within one process run inside a single address space, so most of a program's state is
available to them in common by default. This is the key difference from processes, where each has
its own copy of the address space and sees nothing automatically.[^py314-library-threading]

Shared in common: all objects on the heap – module-level global variables, class and instance
attributes, elements of lists and dictionaries, as well as open file descriptors and sockets. If
one thread mutates a list or dictionary, every other thread holding a reference to that same
object sees the change immediately.

Separate per thread: its own call stack, the local variables of the functions that particular
thread is executing, and the CPU registers at the point of execution. This is what makes each
thread an independent flow of control, even though memory is shared.

```python
import threading

counter = 0  # shared across all threads

def worker():
    local_value = 0  # private stack-local variable
    global counter
    for _ in range(1000):
        local_value += 1
        counter += 1  # visible to every thread, not synchronized

threads = [threading.Thread(target=worker) for _ in range(4)]
```

In the example, `local_value` exists separately in each call to `worker()`, while `counter` is a
single object accessed by all four threads at once, with no guarantee of atomicity.

When state needs to be private to a thread without manually passing it through arguments,
`threading.local()` is used – each attribute of such an object is bound to a specific thread and
not visible to others, even though the object itself is formally a single one for the whole
program.[^py314-library-threading]

**Common sources of errors caused by shared state:**
- assuming a function's local variable is isolated, when in fact a shared mutable object passed
  into the function by reference is what actually gets mutated;
- forgetting that module-level global variables and class attributes are shared across all
  threads without explicit synchronization;
- confusing process isolation (`multiprocessing`) with thread isolation – processes see no shared
  state at all, while threads see almost everything except the stack and local variables.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
