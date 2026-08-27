---
id: py-compfn-0001
title: "What scope does the iteration variable of a list comprehension have in Python 3, and does it replace a same-named outer variable?"
description: "What scope does the iteration variable of a list comprehension have in Python 3, and does it replace a same-named outer variable?"
track: python
section: comprehensions-and-functional
level: middle
type: mechanism
tags: []
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
---

## Short answer

**The iteration variable of a list comprehension runs in its own implicit nested scope and does not
leak into the enclosing scope.**[^py314-howto-functional] So a same-named outer variable keeps its
own value: after `x = 99; result = [x for x in range(3)]`, `x` is still `99`, not `2`. This
distinguishes a comprehension from a regular `for` loop, where the iteration variable remains in the
current scope.

## Detailed explanation

The scope isolation is implemented mechanically: since Python 3, a comprehension compiles into its
own implicit code object (a small nested function), which is called immediately with the first
(outermost) iterable passed to it as an argument.[^py314-howto-functional] That is why the variable
`x` lives only inside that hidden call and never reaches the enclosing scope – this is not a special
case carved out for comprehensions, it is ordinary function-local isolation.

This differs from Python 2, where a list comprehension (unlike a generator expression or a set/dict
comprehension, which always had their own scope) ran in the current scope and left the iteration
variable accessible afterward; Python 3 unified all four comprehension kinds so that every one of
them gets its own implicit scope.

The consequence for closures: functions (a `lambda`, for example) created inside a comprehension's
body capture the iteration variable from the comprehension's own implicit scope, not from the
enclosing scope. That means `[lambda: i for i in range(3)]` creates lambdas that, once the
comprehension has finished running, all return `2` – the classic late-binding problem, except it now
happens inside the comprehension's own isolated scope rather than the enclosing one.

When a comprehension has several `for` clauses, the whole comprehension gets one implicit scope, not
one per `for`: the iteration variables of every nesting level live in the same hidden function and
are equally inaccessible from outside. The one exception is the iterable expression of the very
first `for` – it is evaluated in the enclosing scope before entering the implicit function, which is
why it alone can safely refer to names that would otherwise clash with names used inside the
comprehension.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
