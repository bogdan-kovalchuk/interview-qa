---
id: py-cpyint-0008
title: "Why can't relying on immediate deallocation in CPython be treated as a portable Python language guarantee?"
description: "Why can't relying on immediate deallocation in CPython be treated as a portable Python language guarantee?"
track: python
section: cpython-internals
level: senior
type: pitfall
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

**Immediate deallocation at refcount=0 is a CPython implementation detail, not a guarantee of the
Python language; other implementations and the free-threaded build may defer freeing
objects.**[^py314-library-dis] The Python Language Reference describes object lifecycle in general
terms and does not mandate immediate finalization. PyPy uses a tracing GC, and free-threaded
CPython uses deferred refcounting. So resources (files, sockets, locks) should be managed through
`with` / context managers, not by relying on the moment of destruction.

## Detailed explanation

Immediate deallocation – an object being freed exactly at the point where its last reference
disappears – is a consequence of CPython's specific reference-counting implementation, not a
guarantee made by the Python language specification.

The Python Language Reference describes the object lifecycle in general terms: an object will
eventually be "reclaimed", `__del__` may be called, but the specification does not fix exactly when
that happens, and does not even guarantee `__del__` is called in every case – for instance, with
reference cycles or at interpreter shutdown.[^py314-reference-datamodel-traceback-objects]

Other implementations honor that specification but not the CPython mechanism: PyPy uses a
generational tracing GC, where objects are freed in batches during a collection pass rather than at
the moment of the last decref. The same is true within CPython itself in the free-threaded build
(3.13+), where deferred and biased reference counting postpone the actual release until the nearest
safe point instead of doing it synchronously.[^py314-howto-free-threading-python]

The practical consequence: code that relies on a destructor's side effect – closing a file,
releasing a lock, committing a transaction – right after a variable goes out of scope or is
reassigned will work on "ordinary" CPython, but can accumulate unclosed resources (a file-descriptor
leak, tasks holding a lock longer than needed) on PyPy or in future CPython variants.

**Common mistakes:**
- writing `f = open(path); ...; f = None`, expecting the file to close immediately, instead of
  `with open(path) as f: ...`;
- relying on the order in which `__del__` is called to release interdependent resources;
- testing only on CPython and treating destructor behaviour as part of the language rather than an
  implementation detail.

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
