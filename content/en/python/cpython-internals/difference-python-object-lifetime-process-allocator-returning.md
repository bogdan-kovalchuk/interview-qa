---
id: py-cpyint-0012
title: "What is the difference between a Python object's lifetime and the process allocator returning memory to the operating system?"
description: "What is the difference between a Python object's lifetime and the process allocator returning memory to the operating system?"
track: python
section: cpython-internals
level: middle
type: comparison
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
  - source_id: py314-library-dis
    title: "Python 3.14: Library/dis"
    url: https://docs.python.org/3.14/library/dis.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-gc
    title: "Python 3.14: Library/gc"
    url: https://docs.python.org/3.14/library/gc.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-c-api-memory
    title: "Python 3.14: C Api/memory"
    url: https://docs.python.org/3.14/c-api/memory.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-sys
    title: "Python 3.14: Library/sys"
    url: https://docs.python.org/3.14/library/sys.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-tracemalloc
    title: "Python 3.14: Library/tracemalloc"
    url: https://docs.python.org/3.14/library/tracemalloc.html
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
  - source_id: py314-reference-datamodel-traceback-objects
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#traceback-objects
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/interpreter.md#L270-L333
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**Object lifetime is the moment a Python object becomes unreachable and its memory is freed at the
Python level; returning memory to the OS is a separate stage, where the process allocator (a
pymalloc arena or mimalloc) decides to give a page back.**[^py314-library-dis] An object is freed
once its refcount reaches zero, but its block returns to the allocator's pool, not straight to the
OS. An arena returns to the OS only once fully empty, so a "dead" object's memory can still sit in
the process's RSS.

## Detailed explanation

A Python object's lifetime and the process allocator returning memory to the operating system are
two different stages of one process, separated by the allocator layer, and confusing them means
misreading why a process's RSS does not drop right after objects become "dead".[^py314-c-api-memory]

An object's lifetime ends at the Python level: when `refcount` reaches zero (or when the cyclic GC
collects a cycle), CPython calls the destructor and frees the object's memory block. This is visible
from Python's perspective – the next call to `id()` for the same address will give a different
object, and `sys.getrefcount()` for the deleted name no longer makes sense.

The freed block, however, is not returned to the OS right away. For small objects (up to 512 bytes)
CPython uses `pymalloc`: the block goes back into a pool of a given size inside an arena (typically
1 MiB), so the next allocation of the same size does not have to go to the OS. An arena is returned
to the operating system only once every pool in it becomes completely empty – if even one block in
the arena is still alive, the whole arena stays reserved for the process.

```python
big = [object() for _ in range(1_000_000)]
del big  # objects are freed at the Python level immediately
# process RSS typically does not shrink here: arenas stay reserved
```

So a long-running process that once allocated and freed a large structure can hold significant RSS
without any memory leak at the Python level: arena fragmentation, not a leak, explains the memory
graph.[^py314-c-api-memory]

**Practical consequences of this difference:**
- RSS dropping after `del` or `gc.collect()` is not guaranteed and is not a sign of a leak if there
  isn't one;
- to actually check for a leak, track the number of live objects (`tracemalloc`,
  `gc.get_objects()`) rather than RSS;
- periodically restarting worker processes is a typical workaround for arena fragmentation, not a
  bug in the code.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
