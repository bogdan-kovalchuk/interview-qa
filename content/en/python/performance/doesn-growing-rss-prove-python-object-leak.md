---
id: py-perf-0020
title: "Why doesn't growing RSS prove a Python object leak, and what additional measurements are needed?"
description: "Growing RSS alone does not prove a leak: RSS also counts pymalloc arenas, fragmentation and C-extension memory."
track: python
section: performance
level: senior
type: pitfall
tags: []
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  uk: 2
applies_to:
  - product: "CPython"
    version: null
anki:
  export: true
sources:
  - source_id: py314-library-tracemalloc
    title: "Python 3.14: Library/tracemalloc"
    url: https://docs.python.org/3.14/library/tracemalloc.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation, tracemalloc module: traces most memory blocks allocated by Python (not all of the process memory); comparing two snapshots to detect leaks."
  - source_id: py314-c-api-memory
    title: "Python 3.14: C Api/memory"
    url: https://docs.python.org/3.14/c-api/memory.html#the-pymalloc-allocator
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation, pymalloc section: small objects up to 512 bytes, arenas of a fixed size (1 MiB on 64-bit); larger allocations go to PyMem_RawMalloc. It does not describe when arenas are returned to the OS."
  - source_id: cpython-obmalloc-arena-release
    title: "CPython Objects/obmalloc.c: arena release"
    url: https://github.com/python/cpython/blob/v3.14.6/Objects/obmalloc.c#L2431
    accessed: 2026-10-13
    kind: official
    version: "3.14.6"
    applicability: "CPython 3.14.6 source, Objects/obmalloc.c, line 2431 (if (nf == ao->ntotalpools && ao->nextarena != NULL)): an arena is freed to the system when all its pools are free and it is not the last one in the list. An implementation detail of CPython, not a language guarantee."
  - source_id: py314-library-gc
    title: "Python 3.14: Library/gc"
    url: https://docs.python.org/3.14/library/gc.html#gc.is_tracked
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation, gc.get_objects and gc.is_tracked: returns only objects tracked by the collector; atomic types as a rule are not tracked. It does not describe process memory."
  - source_id: py314-library-sys
    title: "Python 3.14: Library/sys"
    url: https://docs.python.org/3.14/library/sys.html#sys.getallocatedblocks
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation, sys.getallocatedblocks: number of memory blocks allocated by the interpreter; the value can vary between calls because of internal caches, so gc.collect() and _clear_internal_caches() may be needed. It is not a measure of RSS."
---

## Short answer

**Growing RSS alone does not prove a Python object leak: RSS shows all physical memory the process holds, not only live Python objects.** Small objects of up to 512 bytes live in pymalloc arenas,[^py314-c-api-memory] and in CPython an arena is returned to the OS only when all of its pools are free,[^cpython-obmalloc-arena-release] so RSS can stay high after objects are freed. To tell a leak apart, compare `tracemalloc` snapshots, count `gc.get_objects()`, and read `sys.getallocatedblocks()` after `gc.collect()` (and, if needed, `sys._clear_internal_caches()`) under a repeated workload.[^py314-library-sys]

## Detailed explanation

RSS (Resident Set Size) is the part of the process's memory that is currently held in physical RAM. It does not show what occupies that memory: live Python objects, blocks that Python has freed but not yet returned to the OS, fragmentation, memory used by C extensions, or files mapped into memory. Growing RSS is therefore a symptom to explain, not proof of a leak.

CPython allocates small objects with pymalloc. Objects up to 512 bytes come from arenas of a fixed size, and larger allocations go to `PyMem_RawMalloc()`.[^py314-c-api-memory] Freeing a small object only frees its block inside a pool. An arena goes back to the OS only when all of its pools are free,[^cpython-obmalloc-arena-release] so one live block in an arena keeps the whole arena in RSS. That is why RSS can stay high after `del`, even when no references to the objects remain.

A Python-level leak means the number of objects keeps growing under a steady workload, usually because something still references them: a global list, an unbounded cache, a closure, or a callback registry. A bounded cache grows only up to its limit and then levels off, so the signal is a trend from one iteration to the next under the same load, not a single reading. RSS growth without such a trend is only a suspicion.

Measurements that show Python-level growth:

- **tracemalloc.** The module traces most memory blocks allocated by Python and stores the traceback of each allocation. Its documentation names comparing two snapshots as a way to detect memory leaks.[^py314-library-tracemalloc]
- **gc.get_objects().** Returns the objects tracked by the garbage collector. As a general rule, atomic types are not tracked: in CPython `gc.is_tracked("abc")` returns `False`, so strings do not appear in this list.[^py314-library-gc]
- **sys.getallocatedblocks().** Returns the number of memory blocks the interpreter currently holds. The value can differ between calls because of internal caches, so `gc.collect()` (and, if needed, `sys._clear_internal_caches()`) may be needed before comparing trends.[^py314-library-sys]

The example shows how a snapshot diff points at the line that keeps objects alive. The loop stores 10 000 `bytes` objects of 1000 bytes each in a dictionary, and the largest difference is attributed to line 8.

```python
import tracemalloc

tracemalloc.start()
cache = {}
before = tracemalloc.take_snapshot()

for i in range(10_000):
    cache[i] = bytes(1000)

after = tracemalloc.take_snapshot()
top = after.compare_to(before, "lineno")[0]
print(top.traceback[0].lineno)  # 8: the cache[i] = ... line keeps the blocks alive
```

tracemalloc does not see everything. In CPython, memory that a C extension requests directly with `malloc()` does not appear in tracemalloc snapshots, so no growth in tracemalloc does not prove that the C code is leak-free.

**Common mistakes:**
- treating RSS growth as proof of a leak without snapshots or a repeated workload;
- reading one `sys.getallocatedblocks()` value without `gc.collect()` and without comparing trends;
- looking for leaked strings or bytes with `gc.get_objects()`, where as a rule they do not appear.

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
