---
id: py-compfn-0010
title: "When is `singledispatch` better than an extensible `if/elif` chain, and on which argument does it choose the implementation?"
description: "When is `singledispatch` better than an extensible `if/elif` chain, and on which argument does it choose the implementation?"
track: python
section: comprehensions-and-functional
level: senior
type: comparison
tags: [singledispatch, if-elif]
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-howto-functional
    title: "Python 3.14: Howto/functional"
    url: https://docs.python.org/3.14/howto/functional.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-itertools
    title: "Python 3.14: Library/itertools"
    url: https://docs.python.org/3.14/library/itertools.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-functools
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-reference-expressions-displays-for-lists-sets-and-dict
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#displays-for-lists-sets-and-dictionaries
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/functional_programming.md#L49-L64
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**`singledispatch` chooses the implementation by the type of the first argument, using the MRO to
find the closest registered type.**[^py314-howto-functional] It is better than an `if/elif` chain
when extensibility is needed: new types are registered via `@fn.register(type)` without modifying
existing code (the open/closed principle). The base implementation (for `object`) serves as the
fallback. <span class="warn">Dispatch happens only on the first argument; the types of other
parameters do not affect the choice.</span>

## Detailed explanation

Type resolution does not work by simple equality comparison; it walks the `__mro__` of the
argument's concrete type: `singledispatch` looks for the closest registered ancestor in the class's
linearization order and calls that implementation, not necessarily the one registered for the
instance's exact class.[^py314-library-functools] So a subclass with no implementation of its own
automatically gets the implementation of its closest registered ancestor – that is the main
difference from an `if isinstance(...)` chain, where this behavior would have to be written out by
hand for every subclass.

The resolution result is cached: after the first call with a given concrete type, `singledispatch`
remembers the implementation it found for that type, so subsequent calls with the same type skip
walking `__mro__` again. The cache is cleared automatically whenever a new implementation is
registered via `register`, so types already called can re-evaluate their choice.

If, because of multiple inheritance, a type has two registered ancestors at the same distance in
`__mro__` and neither is an ancestor of the other, `singledispatch` does not pick one arbitrarily –
it raises a `RuntimeError` about the ambiguity, requiring an explicit implementation to be
registered for the problematic type itself.

An implementation can be registered two ways: explicitly, with `@fn.register(SomeType)`, or – since
Python 3.7 – via the type annotation on the function's first parameter, `@fn.register` with no
argument, when the function is declared as `def _(arg: SomeType): ...`. For methods on a class there
is a separate `functools.singledispatchmethod`, which ignores `self` and dispatches on the type of
the first argument after it.[^py314-library-functools]

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
