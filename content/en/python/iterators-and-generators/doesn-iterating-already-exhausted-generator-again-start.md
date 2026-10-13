---
id: py-itergen-0013
title: "Why doesn't iterating an already exhausted generator again start the computation over?"
description: "Why doesn't iterating an already exhausted generator again start the computation over?"
track: python
section: iterators-and-generators
level: middle
type: pitfall
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
    applicability: "Official Python 3.14 documentation: generator-iterator methods (__next__, send, throw, close) and their behaviour in a suspended state."
  - source_id: py314-glossary-term-iterator
    title: "Python 3.14: Glossary"
    url: https://docs.python.org/3.14/glossary.html#term-iterator
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: definition of iterator and exhausted."
---

## Short answer

**After the first `StopIteration`, a generator is permanently finished: the protocol requires every later `__next__()` to raise `StopIteration` as well.**[^py314-library-stdtypes-iterator-types] The function body runs only until a `return`, the end of the body, or an unhandled exception; after that there is no suspended state to resume.[^py314-reference-expressions-generator-iterator-methods] A container should return a new iterator on each `iter()` call.[^py314-reference-datamodel-object-iter] A generator is its own iterator, so starting over is possible only with a new generator, that is, by calling the generator function again.[^py314-library-stdtypes-iterator-types]

## Detailed explanation

`Exhausted` means that an iterator has already produced all of its values, and every later call to `next()` raises `StopIteration`.[^py314-glossary-term-iterator] The iterator protocol requires the same of any implementation: after the first `StopIteration`, later `__next__()` calls must raise it again, otherwise the implementation is considered broken.[^py314-library-stdtypes-iterator-types] So a second `list(gen)` silently returns an empty list, a second `for` loop performs no iterations, and `next(gen)` raises `StopIteration`.

The example: `countdown` is exhausted after one pass. The comments show the output on CPython 3.13 and 3.14:

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

gen = countdown(3)
print(list(gen))                    # [3, 2, 1]
print(list(gen))                    # []: already exhausted
print(next(gen, 'empty'))           # empty: the default is returned instead of StopIteration
print(iter(gen) is gen)             # True: a generator is its own iterator
print(list(countdown(3)))           # [3, 2, 1]: a new call creates a new generator
```

Calling a generator function returns a new generator; the body starts running only when one of the generator's methods is called.[^py314-reference-expressions-yield-expressions] When the body reaches its end, there is no `yield` left, and the generator raises `StopIteration`.[^py314-reference-expressions-generator-iterator-methods] No suspended state remains that could be resumed. In CPython, `gi_frame` is `None` after that, but this is an implementation detail, not a language rule.

The rule concerns one generator object. A container should return a new iterator on each `iter()` call, so a `list` can be traversed many times.[^py314-reference-datamodel-object-iter] A generator is its own iterator: `iter(gen) is gen`, as the example shows.[^py314-library-stdtypes-iterator-types] So a repeated pass requires storing the data in a `list` or calling the generator function again. The same conclusion applies to a generator that ended with an exception: the next `next()` raises `StopIteration` and does not repeat the exception (observed in CPython).

**Common mistakes:**
- expecting a second `for` loop over the same generator to traverse all the items again;
- storing a generator in a variable, passing it to several places, and being surprised by an empty result after the first consumer;
- confusing an iterable (`list`, `range`), which can be traversed many times, with an iterator (a generator), which can be traversed once.

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
