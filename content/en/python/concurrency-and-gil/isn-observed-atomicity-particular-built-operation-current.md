---
id: py-gil-0008
title: "Why isn't the observed atomicity of a particular built-in operation in the current CPython a stable synchronization contract?"
description: "Why isn't the observed atomicity of a particular built-in operation in the current CPython a stable synchronization contract?"
track: python
section: concurrency-and-gil
level: senior
type: pitfall
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

**The atomicity of individual built-in operations (for example, `list.append()`) is a CPython
implementation detail, not a language guarantee.**[^py314-library-threading] This behavior can
change between CPython versions, differ in other implementations (PyPy, GraalPy), or be absent on
the free-threaded build. <span class="warn">Application code must never rely on observed
atomicity</span> - always use explicit synchronization primitives (`Lock`, `RLock`) to protect
shared mutable state.

## Detailed explanation

The atomicity of a particular built-in operation means the operation runs as a single C-level call
with no intermediate point where the GIL could hand control to another thread, so from the outside
it looks indivisible. But that is a consequence of CPython's specific bytecode-loop implementation,
not a guarantee made by the Python language or by any documented API.[^py314-library-threading]

The GIL switches threads between individual bytecode instructions (or after a certain number of
"ticks"/amount of time), not in the middle of a C function that implements one built-in operation.
So if the entire effect of an operation is a single C-level call (for example, in CPython
`list.append(x)` is one call to `list_append`), another thread physically cannot interrupt it
partway through.

The problem is that outwardly simple expressions often compile to several bytecode instructions,
and the GIL can switch threads between any of them:

```python
counter = 0

def increment():
    global counter
    counter += 1  # LOAD_GLOBAL, BINARY_ADD, STORE_GLOBAL - not one atomic step
```

`counter += 1` looks just as simple as `list.append(x)`, but it is actually a read, an addition, and
a write - three separate steps, and a thread switch between any of them can lose an increment.

On the free-threaded build the situation becomes even less predictable: without the GIL there is no
bytecode serialization either, so operations that used to look atomic only thanks to the GIL stop
being atomic unless CPython synchronizes them explicitly internally. The same applies to alternative
implementations (PyPy, GraalPy) - they are not obligated to reproduce the same incidental atomicity,
because the Python language never documents it as a guarantee anywhere.[^py314-howto-free-threading-python]

**Why you cannot rely on it:**
- the atomicity of a particular operation is an artifact of the current bytecode implementation, not
  part of the language specification;
- it can disappear after a CPython optimization, a bytecode change between versions, or a move to
  the free-threaded build;
- code that relies on it works "by accident" and breaks unpredictably when the interpreter's version
  or implementation changes.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
