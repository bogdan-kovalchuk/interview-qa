---
id: py-objtypes-0003
title: "Why can't the result of an identity comparison between two identical literals be used as proof of interning or as a portable Python guarantee?"
description: "Why can't the result of an identity comparison between two identical literals be used as proof of interning or as a portable Python guarantee?"
track: python
section: objects-and-types
level: senior
type: pitfall
tags: []
status: published
updated: 2026-09-27
content_revision: 2
reconciled_with:
  uk: 2
applies_to:
  - product: "CPython"
    version: null
anki:
  export: true
sources:
  - source_id: py314-reference-datamodel
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-stdtypes
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-copy
    title: "Python 3.14: Library/copy"
    url: https://docs.python.org/3.14/library/copy.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-typing
    title: "Python 3.14: Library/typing"
    url: https://docs.python.org/3.14/library/typing.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
---

## Short answer

**Interning of small integers and certain strings is an implementation detail of CPython rather than a language guarantee.**[^py314-reference-datamodel] CPython caches objects within a specific range (such as integers from -5 to 256), but this range and interning mechanisms can change across versions. Two literals with identical values may or may not share the same `id()` depending on how they were constructed and on compiler optimizations.

## Detailed explanation

The Python language specification guarantees value equivalence for identical literals, but fundamentally treats object reuse and memory caching as implementation-dependent optimizations.[^py314-reference-datamodel]

In CPython, developers often confuse two distinct mechanisms: runtime interning (pre-allocating objects for small integers from -5 to 256 and interning identifier strings) and compiler constant folding during bytecode compilation.[^py314-library-stdtypes] When the compiler parses a single code block (such as an individual module or function), it deduplicates identical immutable literals and stores them in a unified constant tuple `co_consts`.

Consequently, executing `a = 1000; b = 1000` within a single file yields `a is b == True` because both variables point to the same entry in `co_consts`. However, evaluating the exact same lines sequentially in an interactive REPL or computing the value dynamically via `int("1000")` compiles each statement in an isolated context and creates distinct heap objects. Using literal identity comparisons to prove global interning mistakes an optimization pass of the compiler for an architectural memory guarantee.

Relying on identity instead of equality produces brittle code that breaks when switching between CPython and alternative implementations (such as PyPy or GraalPy), adjusting optimization flags, or crossing cache boundaries.

An example demonstrating the difference between compiler constant folding and runtime caching:

```python
# In a single function, the compiler merges duplicate constants via co_consts:
def demonstrate_constant_folding():
    x = 1000
    y = 1000
    print(x is y)  # True: both reference the identical object in co_consts

demonstrate_constant_folding()

# Dynamically evaluated numbers bypass constant folding:
a = 1000
b = int("1000")
print(a == b)  # True: values are equal
print(a is b)  # False: distinct heap objects with separate memory addresses

# Pre-allocated small integer cache (-5 to 256) in CPython:
small_a = 256
small_b = int("256")
print(small_a is small_b)  # True: both resolve to the global singleton in CPython
```

**Architectural trade-offs and common pitfalls:**
- conflating constant folding with interning: literal deduplication within a single compilation unit creates a false sense of singleton uniqueness that collapses under dynamic evaluation;
- tight coupling to CPython internals: alternative runtimes (such as PyPy or GraalPy) and newer CPython releases employ different constant optimization strategies;
- latent defects across boundary values: code using `x is 100` passes unit tests with small inputs, but silently fails in production when data exceeds `256`;
- compiler diagnostics: starting in Python 3.8, the compiler raises a `SyntaxWarning: "is" with a literal. Did you mean "=="?` whenever `is` is used with a literal.

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
