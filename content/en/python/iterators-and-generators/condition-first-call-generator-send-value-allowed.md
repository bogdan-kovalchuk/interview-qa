---
id: py-itergen-0011
title: "Under what condition is the first call to `generator.send(value)` allowed, and why is `None` usually sent first?"
description: "Under what condition is the first call to `generator.send(value)` allowed, and why is `None` usually sent first?"
track: python
section: iterators-and-generators
level: middle
type: pitfall
tags: [generator-send-value]
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
---

## Short answer

**For a just-created generator, the first `send()` accepts only `None`, because there is no `yield` before the first one that could receive a value.**[^py314-reference-expressions-generator-iterator-methods] In CPython, any other value raises `TypeError`. That is why a generator is usually started with `next(gen)`, which passes `None` and stops the generator at the first `yield`.[^py314-reference-expressions-generator-iterator-methods]

## Detailed explanation

The expression `send(value)` makes `value` the result of the current `yield` expression and returns the next value that the generator yields. So `send()` can deliver a value only when the generator is already suspended at a `yield`. A just-created generator has no such place yet, because its body has not run. The documentation requires that the call starting the generator pass `None`, because there is no `yield` expression that could receive the value.[^py314-reference-expressions-generator-iterator-methods]

The example shows both situations: a failed first `send()` and a start with `None`. The comments show the output, checked on CPython 3.13 and 3.14:

```python
def echo():
    received = yield 'ready'        # the value sent later arrives here
    print('got', received)
    yield 'next'

g = echo()
try:
    g.send('hello')                 # first call with a non-None value
except TypeError as error:
    print('TypeError:', error)      # can't send non-None value to a just-started generator
print(g.send(None))                 # ready: runs the body up to the first yield
print(g.send('hello'))              # got hello, then next
```

In CPython, the failed first `send('hello')` does not start the generator, so the next `send(None)` begins it from the top and stops at the first `yield`. The value `'hello'` reaches `received` only once the generator is suspended at a `yield`. A second point: `send()` returns the next value that the generator yields, not the value that was sent in. When the generator is resumed with `__next__()`, the current `yield` expression always evaluates to `None`.[^py314-reference-expressions-generator-iterator-methods]

So the condition is this: for a just-created generator, the first value passed through `send()` must be `None`. After the generator has stopped at a `yield`, `send(value)` works with any value. In practice, a generator is therefore usually primed with one `next(gen)`, which stops it at the first `yield`, and values are then passed with `send()`.[^py314-reference-expressions-generator-iterator-methods]

**Common mistakes:**
- starting a generator with `send(value)` and a value other than `None`; in CPython this raises `TypeError`;
- assuming that `send(value)` returns the value that was sent; it returns the next value that the generator yielded;
- confusing `next(gen)` with `send(value)`: both resume the generator, but only `send()` passes a value into the current `yield`.

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
