---
id: py-itergen-0006
title: "What state does a suspended generator keep between two `yield`s, and what happens after it finishes?"
description: "What state does a suspended generator keep between two `yield`s, and what happens after it finishes?"
track: python
section: iterators-and-generators
level: middle
type: mechanism
tags: []
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  uk: 2
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
    applicability: "Official Python 3.14 documentation: generator-iterator methods (__next__, send, throw, close) and their behaviour after the generator finishes."
---

## Short answer

**A suspended generator keeps its local variables, instruction pointer, evaluation stack and exception-handling state.**[^py314-reference-expressions-yield-expressions] When the body finishes through `return` or by running off the end without a `yield`, `next()` raises `StopIteration`.[^py314-reference-expressions-generator-iterator-methods] After that, every further `next()` raises `StopIteration` again.[^py314-library-stdtypes-iterator-types] To iterate again, you must call the generator function again, which creates a new generator.[^py314-reference-expressions-yield-expressions]

## Detailed explanation

A suspended generator is more than a function waiting to continue. When execution reaches a `yield`, the whole execution state is kept: the bindings of local variables, the instruction pointer, the internal evaluation stack and the state of exception handling. When the consumer calls a generator method again, the body continues as if the `yield` were an ordinary call.[^py314-reference-expressions-yield-expressions]

In this example, the local variable `x` lives across calls, and the generator finishes after the last `yield`:

```python
def gen():
    x = 10                          # local variable kept while suspended
    yield x                         # suspended here
    yield x + 1                     # resumed here by the next call

g = gen()
print(next(g))                      # 10
print(next(g))                      # 11
try:
    next(g)                         # the body ends: StopIteration
except StopIteration:
    print("finished")
try:
    next(g)                         # a finished generator keeps raising StopIteration
except StopIteration:
    print("still finished")
```

The output is `10`, `11`, then `finished` and `still finished`. When the body reaches its end or executes `return`, the generator exits without another `yield`, and `next()` raises `StopIteration`.[^py314-reference-expressions-generator-iterator-methods] If an exception is not caught inside the body, it propagates to the caller of `next()`.[^py314-reference-expressions-generator-iterator-methods] After that the generator has finished, and in CPython the next `next()` raises `StopIteration`; this is an observation from runs on CPython 3.12 to 3.14, not a separate rule in the documentation.

Iterating the same sequence again through the same generator object is impossible: after `StopIteration` it produces nothing more, and each following `next()` raises `StopIteration` again. An implementation of the iterator protocol that did not behave this way would be considered broken.[^py314-library-stdtypes-iterator-types] To get a new sequence, you must call the generator function again, which creates a new generator with its own state.[^py314-reference-expressions-yield-expressions]

**Common mistakes:**
- assuming a generator "restarts" when `next()` is called again after `StopIteration`;
- expecting local variables to reset between calls: a suspended generator keeps them;
- after an exception has escaped the body, expecting to continue from the same point.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
