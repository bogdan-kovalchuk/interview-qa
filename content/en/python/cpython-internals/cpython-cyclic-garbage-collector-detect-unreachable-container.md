---
id: py-cpyint-0010
title: "How does CPython's cyclic garbage collector detect unreachable container cycles on top of reference counting?"
description: "How does CPython's cyclic garbage collector detect unreachable container cycles on top of reference counting?"
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/interpreter.md#L102-L197
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**The GC tracks container objects (list, dict, user-defined instances), traverses the graph of
their references, and frees groups of objects that have no external (non-GC) references.**[^py314-library-dis]
Objects are split across three generations (0, 1, 2); new containers land in generation 0. When the
number of allocations minus deallocations exceeds a threshold, a collection runs. The GC checks
whether objects are reachable from the roots; if not, they are collectable. Older generations are
collected less often, which reduces overhead.

## Detailed explanation

CPython's cyclic garbage collector is an additional mechanism that complements reference counting
and can find and free groups of container objects (list, dict, set, class instances) that reference
each other in a cycle, even when the external refcount of each of them never drops to
zero.[^py314-library-gc]

Only container objects are registered with the GC, because only they can take part in a cycle:
numbers, strings, or tuples without references to containers do not need checking. New container
objects land in generation 0; every object that survives a collection moves to the next generation
(0 -> 1 -> 2). A collection of generation 0 runs when the difference between the number of
allocations and deallocations exceeds the `gc.get_threshold()` threshold; older generations are
collected less often, because long-lived objects less often turn into garbage.

The algorithm itself is not a search for `refcount == 0`, but "trial deletion": the GC temporarily
subtracts from each container object's refcount the number of references coming from other objects
in the same generation. What remains after that subtraction is the refcount coming from "outside"
the generation. Objects with a positive external refcount are considered reachable roots, and the
GC traverses the graph from them; everything unreachable from those roots is collectable, even if
the objects hold each other in a cycle.

```python
import gc

gc.collect()  # force a full collection across all generations
print(gc.get_threshold())  # (700, 10, 10) by default
```

**Common mistakes with the cyclic GC:**
- assuming a cycle without `__del__` is a problem – since Python 3.4 the GC frees such cycles
  without restriction;
- disabling `gc.disable()` for speed without accounting for the fact that this leaves all cycles
  uncollected;
- forgetting that objects with `__del__` participating in a cycle used to be (before 3.4)
  uncollectable at all.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
