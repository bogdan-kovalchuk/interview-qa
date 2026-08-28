---
id: py-decor-0010
title: "Why can state in a closure-based decorator create a race condition under concurrent calls to the wrapped function?"
description: "Why can state in a closure-based decorator create a race condition under concurrent calls to the wrapped function?"
track: python
section: decorators
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
  - source_id: py314-glossary-term-decorator
    title: "Python 3.14: Glossary"
    url: https://docs.python.org/3.14/glossary.html#term-decorator
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-functools-functools-wraps
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html#functools.wraps
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-reference-compound-stmts-function-definitions
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#function-definitions
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/decorators.md#L80-L111
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**A closure holds shared mutable state in the enclosing scope, and every thread that calls the
decorated function reaches the same variable with no synchronization.**[^py314-glossary-term-decorator]
In CPython with the GIL, simple operations like `x += 1` on an integer are atomic at the bytecode
level, but more complex patterns (check-then-act, conditional updates to a dict or list) are not
atomic even with the GIL. In free-threaded CPython (3.13+) even simple operations are not protected
by the GIL, so closure state needs an explicit lock (`threading.Lock`) or immutable state.

## Detailed explanation

A closure-based decorator creates one wrapper function and one closure scope exactly once, when the
decorator is applied to the function, not on every call. Any variable the wrapper reads or mutates
through `nonlocal` lives in that single closure scope and is shared by every call to the decorated
function, from any thread.[^py314-glossary-term-decorator]

The race condition does not come from sharing state as such, but from non-atomic operations on it.
The GIL guarantees that a single bytecode instruction runs without interruption, but even an
operation that looks simple, like `count = count + 1`, compiles into several separate instructions:
read `count`, compute the new value, write it back. The interpreter can switch threads between any
two of these steps, so two threads that read the same old value of `count` at the same time can lose
one increment.

A check-then-act pattern suffers even more: checking a condition (`if key not in cache`) and the
following action (`cache[key] = value`) are two separate operations, and the GIL is entirely free
to hand control to another thread in between. In free-threaded CPython (3.13+, no GIL by default),
even a single `x += 1` on a plain `int` is no longer automatically protected, so any shared closure
state needs explicit synchronization no matter how simple the operation looks.

An example of a decorator with a shared counter that demonstrates lost increments:

```python
def call_counter(func):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        current = count
        count = current + 1  # two threads can read the same `current`
        return func(*args, **kwargs)
    return wrapper

@call_counter
def handler():
    ...
```

If 1000 threads call `handler()` concurrently, the final value of `count` will almost certainly end
up below 1000 – some increments are lost because one thread reads `current` before another thread
manages to write its own update back.

**Ways to avoid a race condition in closure state:**
- wrap the read-and-write in a `threading.Lock` obtained once when the decorator is applied;
- replace a manual counter with `itertools.count()` or `collections.Counter` where the operation
  truly reduces to one atomic call;
- do not keep mutable state in the closure at all – move it into thread-local storage
  (`threading.local`) or pass it explicitly as an argument when every call needs its own
  independent state;
- check this especially carefully on a free-threaded build: code that "happened to work" under the
  GIL can start losing updates in places that used to look safe.

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
