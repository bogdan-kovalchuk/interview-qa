---
id: py-gil-0007
title: "Why doesn't the GIL eliminate race conditions in Python application code?"
description: "Why doesn't the GIL eliminate race conditions in Python application code?"
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/gil_threads_processes.md#L559-L688
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**The GIL guarantees atomicity for a single bytecode instruction, but compound operations
(read-modify-write) consist of several bytecode instructions and can be interrupted between
them.**[^py314-library-threading] For example, `x += 1` compiles to three bytecode instructions:
`LOAD x`, `ADD 1`, `STORE x` – the GIL can be handed to another thread between any of them. So
even in a GIL-enabled build, explicit synchronization primitives are still required
(`threading.Lock`, `queue.Queue`).

## Detailed explanation

The GIL is often taken as a guarantee that "threads in Python are safe by default", but that is an
inaccurate simplification. The GIL only guarantees that two bytecode instructions never execute
literally at the same time – it says nothing about what happens *between* the instructions of one
logical expression.[^py314-library-threading]

Every piece of Python code that looks like a single operation is compiled by the interpreter into
a sequence of separate bytecode instructions. The GIL can be handed to another thread after *any*
of them, not only between statements. So "atomicity at the bytecode level" does not mean
"atomicity at the level of a line of code".

```python
counter = 0

def increment():
    global counter
    counter += 1  # LOAD_FAST/GLOBAL, BINARY_ADD, STORE -- not one instruction
```

The classic example is read-modify-write: `counter += 1` looks like one action, but compiles to
several bytecode instructions – load the value, add one, store the result. If two threads execute
this line at the same time, the following can happen: both read the old value before either has
written the new one, and one increment is lost.

This problem is not limited to simple operators. `list.append()` is protected by its internal
implementation and cannot be interrupted mid-operation, but a sequence like
`if key not in dict: dict[key] = ...` is already two separate operations, and the GIL can switch
threads between them, so the check becomes stale by the time the write happens
(check-then-act race).

**Why this is application code, not the GIL itself:**
- the GIL protects CPython's internal state (reference counts, interpreter data structures) – this
  is implementation safety, not program-logic safety;
- compound operations at the Python-code level (read-modify-write, check-then-act) consist of
  several independent steps, and the GIL freely switches threads between them;
- single-bytecode library operations really are atomic (for example, `list.append(x)`), which
  makes it easy to mistakenly extend that property to all code.

The defense against this kind of race condition is explicit synchronization: a `threading.Lock`
around the critical section, or a data structure with atomic operations (`queue.Queue`), no matter
how simple the code looks.[^py314-library-threading]

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
