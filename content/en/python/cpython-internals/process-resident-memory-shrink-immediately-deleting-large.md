---
id: py-cpyint-0013
title: "Why might a process's resident memory not shrink immediately after deleting a large number of Python objects?"
description: "Why might a process's resident memory not shrink immediately after deleting a large number of Python objects?"
track: python
section: cpython-internals
level: senior
type: mechanism
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

**Pymalloc returns an arena to the OS only once it becomes fully empty, and fragmentation of
surviving objects across arenas usually prevents that.**[^py314-library-dis] Even if thousands of
objects are freed via refcounting or `gc.collect()`, their blocks remain in pools inside arenas. As
long as at least one live object remains in an arena, it will not be unmapped. In addition, the
system allocator (malloc/free), used for large objects (>512 bytes), may also not return memory to
the OS right away. So RSS shrinks only once entire arenas become empty.

## Detailed explanation

Pymalloc – CPython's allocator for small objects (up to 512 bytes) – requests memory from the OS in
large 1 MiB blocks called arenas, and splits each arena into 4 KiB pools for blocks of the same
size. An arena is returned to the OS only once every pool in it becomes completely
empty.[^py314-c-api-memory]

Even if an application has deleted millions of small objects, as long as an arena still holds even
one live object – say, one small dict or string – the whole 1 MiB arena is not freed. A typical heap
with an arbitrary order of allocations and deallocations gets fragmented: live long-lived objects
end up scattered across many arenas instead of clustering into a few, so none of them ever becomes
fully empty.

For objects larger than 512 bytes, CPython delegates allocation to the system allocator
(`malloc`/`free`). Malloc implementations (glibc, for instance) also keep freed chunks in their own
free lists and do not always return pages to the OS via `brk`/`munmap` right away – that usually
happens only for very large, mmap'd allocations, not for typical medium-sized objects.

That is why the RSS reported by `top`/`ps` reflects how many memory pages are pinned to the process,
not how much "live" Python data it actually holds: it can stay high long after millions of objects
have already been freed.

```python
import gc

big_objects = [dict(value=i) for i in range(1_000_000)]
del big_objects
gc.collect()  # frees Python objects, but arenas may stay mapped
```

**Common mistakes:**
- treating a drop in `sys.getsizeof`/`tracemalloc` figures as equivalent to a drop in RSS shown by
  `top`;
- expecting `gc.collect()` to release OS memory – it only clears reference cycles, and the
  arena/OS level operates separately;
- ignoring fragmentation: one long-lived object can keep an entire 1 MiB arena alive;
- trying to "fix" this by forcing `gc.collect()` instead of reviewing allocation patterns or
  periodically restarting workers.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
