---
id: py-cpyint-0009
title: "Why can't reference counting by itself free an unreachable reference cycle?"
description: "Why can't reference counting by itself free an unreachable reference cycle?"
track: python
section: cpython-internals
level: middle
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/interpreter.md#L102-L197
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**Because every object in the cycle has a reference count of at least 1 from another object in the
same cycle, and no refcount ever reaches zero – even though the whole cycle is no longer reachable
from outside.**[^py314-library-dis] For example, if `a` refers to `b` and `b` refers to `a`, and
there are no external references, both refcounts equal 1. Reference counting cannot tell such a
"dead" cycle apart from live references. That requires a cyclic garbage collector.

## Detailed explanation

Reference counting frees an object only once its refcount drops exactly to zero. In a cycle every
element holds a reference to another one, so even if nothing outside the cycle refers to it anymore,
each individual refcount stays at least 1 and, naturally, never reaches zero.[^py314-library-gc]

For example: `a = []`, `b = []`, `a.append(b)`, `b.append(a)`, then `del a` and `del b`. After that,
both refcounts equal 1 (each element holds the other), even though no variable names either `a` or
`b` anymore.

Reference counting is a purely local mechanism: it only knows "how many times am I referenced from",
not "is there a path to me from the roots" (the call stack, global variables, modules). For a cycle
these two things diverge, and without a global analysis of the object graph that divergence cannot
be fixed.

The cyclic GC (the `gc` module) solves this with a trial-deletion algorithm: for every container
object in a generation it counts how many references to it come from other container objects in the
same generation, and subtracts that number from the real refcount. If the result is zero, the object
(and the rest of the cycle) is unreachable from outside the generation and counts as
garbage.[^py314-library-gc]

```python
import gc

class Node:
    def __init__(self):
        self.other = None

a, b = Node(), Node()
a.other, b.other = b, a  # reference cycle
del a, b                  # refcount of each node is still 1
gc.collect()               # only the cyclic collector can free them
```

**Common mistakes:**
- treating `del` as equivalent to a guaranteed release of memory;
- forgetting that the cyclic collector only tracks container types (list, dict, objects with
  `__dict__`, and so on) – plain non-container objects cannot be part of a cycle;
- disabling `gc` while still creating cycles, without manual `gc.collect()`, resulting in a memory
  leak.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
