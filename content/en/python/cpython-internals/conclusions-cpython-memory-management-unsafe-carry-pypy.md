---
id: py-cpyint-0020
title: "What conclusions about CPython's memory management are unsafe to carry over to PyPy or another Python implementation?"
description: "What conclusions about CPython's memory management are unsafe to carry over to PyPy or another Python implementation?"
track: python
section: cpython-internals
level: senior
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/interpreter.md#L27-L46
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**Reference counting, immediate deallocation when refcount reaches 0, specific bytecode,
`sys.getrefcount()`, and `id()` as a memory address – all of these are CPython details that other
implementations do not guarantee.**[^py314-library-dis] PyPy uses a tracing GC instead of reference
counting: `__del__` may be called much later or in a different order; `sys.getrefcount()` returns a
meaningless value; `id()` does not correspond to a physical address; bytecode is absent (the JIT
compiles to machine code). Any code relying on finalization timing or a specific memory layout is
not portable.

## Detailed explanation

CPython is only one implementation of Python, and some of the observable behaviour that looks like
part of the language is actually a detail of CPython's specific allocator and reference
counting.[^py314-c-api-memory] Carrying such a conclusion over to PyPy, MicroPython, or Jython can
give a completely different result.

The most important example is when `__del__` gets called. In CPython an object is freed
synchronously the moment its refcount hits zero, so the finalizer fires deterministically at the
point of the last `del` or when the scope exits. PyPy instead uses a tracing (generational) GC
without reference counting: `__del__` is invoked during the next collection cycle, which can happen
much later or not happen at all before the process ends.[^py314-library-gc]

`sys.getrefcount()` and `id()` are two more tools whose semantics are tied to CPython.
`sys.getrefcount()` reads the `ob_refcnt` field, which does not exist in implementations without
reference counting, so the call is either absent or returns a meaningless value. `id()` in CPython
is the object's physical memory address, while in PyPy it is an arbitrary identifier unrelated to
where the object lives.[^py314-library-sys]

CPython bytecode (the `dis` output) is yet another detail that PyPy does not have at all: there,
methods are compiled by a JIT tracer into machine code, bypassing CPython's stable opcode set.

**What is unsafe to carry over from CPython to another implementation:**
- expecting a resource (a file, socket, or lock) to be released right after an object leaves scope,
  without an explicit `with` or `close()`;
- comparing performance or allocation counts via `sys.getrefcount()`;
- using `id()` as a stable, comparable address value;
- assumptions about the order or timing of `__del__` in cycles with references to each other.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
