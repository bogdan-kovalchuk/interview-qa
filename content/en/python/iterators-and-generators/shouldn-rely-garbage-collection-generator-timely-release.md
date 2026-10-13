---
id: py-itergen-0015
title: "Why shouldn't you rely on garbage collection of a generator for the timely release of an external resource?"
description: "Why shouldn't you rely on garbage collection of a generator for the timely release of an external resource?"
track: python
section: iterators-and-generators
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
  - source_id: py314-library-stdtypes-iterator-types
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html#iterator-types
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-reference-expressions-yield-expressions
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#yield-expressions
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-reference-datamodel-object-iter
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__iter__
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-reference-expressions-generator-iterator-methods
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#generator-iterator-methods
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation, section generator-iterator methods: close() raises GeneratorExit at the point where the generator is suspended."
  - source_id: py314-reference-datamodel-object-del
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__del__
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation, section object.__del__: a reference cycle keeps the reference count from reaching zero; the cyclic GC removes such a cycle."
  - source_id: py314-reference-datamodel-objects-values-and-types
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#objects-values-and-types
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation, section Objects, values and types: an implementation may postpone garbage collection or omit it altogether."
  - source_id: py314-library-gc-set-threshold
    title: "Python 3.14: Library/gc"
    url: https://docs.python.org/3.14/library/gc.html#gc.set_threshold
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation, gc.set_threshold: automatic collection starts when allocations minus deallocations exceed threshold0."
---

## Short answer

**When `close()` runs for a generator that was not run to completion is not guaranteed: finalization calls it, and finalization depends on the reference count and on the implementation.**[^py314-reference-expressions-yield-expressions] In CPython, a reference cycle keeps a generator alive after its outside references are gone; the cyclic GC frees it later, and when that GC runs is unpredictable.[^py314-reference-datamodel-object-del][^py314-library-gc-set-threshold] Other implementations may postpone garbage collection or skip it altogether.[^py314-reference-datamodel-objects-values-and-types] For deterministic release of a resource, call `close()` explicitly in `try/finally`, or use a context manager.

## Detailed explanation

A generator can hold a resource in `try/finally`, but that `finally` runs only when the generator finishes or someone calls its `close()`. If a generator is suspended at a `yield` and nothing refers to it any more, Python calls `close()` itself during finalization.[^py314-reference-expressions-yield-expressions] `close()` raises `GeneratorExit` at the suspended `yield`, and the `finally` clause runs when that exception passes through it.[^py314-reference-expressions-generator-iterator-methods] But the moment of finalization is decided by the lifetime of references, not by the generator's code.

In CPython an object is freed as soon as its reference count drops to zero, so in simple cases the resource is released on time, and that is easy to mistake for a guarantee. The trouble is reference cycles: objects that refer to each other never reach zero, and only the cyclic GC can remove them.[^py314-reference-datamodel-object-del] In the code below, `Stream` holds the generator, and the generator's frame holds `Stream` as its argument:

```python
import gc

def read_lines(stream):
    print('acquire')
    try:
        yield 'line 1'
    finally:
        print('release')        # runs only when the generator is closed

class Stream:
    def __init__(self):
        self.lines = read_lines(self)   # the generator's frame refers back to self

gc.disable()                    # keep automatic cyclic GC out of this demo
s = Stream()
print(next(s.lines))            # prints 'acquire', then 'line 1'
del s                           # the reference cycle keeps Stream and the generator alive
print('after del')              # 'release' is not printed yet
gc.collect()                    # the cyclic GC closes the generator here
print('after gc.collect()')
```

After `del s` the `release` line is not printed, because the cycle is still alive; it appears only after `gc.collect()`. Without `gc.disable()`, the moment is set by the automatic GC, which starts when allocations minus deallocations exceed `threshold0`.[^py314-library-gc-set-threshold] The delay depends on the memory state of the whole program, not on the logic that owns the resource.

The reliable option is not to depend on finalization: call `close()` explicitly in a `finally` block, or wrap the resource in a context manager that releases it in `__exit__`. Other Python implementations may postpone garbage collection or skip it altogether, so the resource may be released much later there.[^py314-reference-datamodel-objects-values-and-types]

**Common mistakes:**
- assuming that a generator's `finally` runs right away as soon as the loop is broken;
- carrying CPython's release timing over to other Python implementations without testing;
- using finalization as a timer for closing files, sockets or connections.

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
