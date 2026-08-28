---
id: py-syntax-0012
title: "In what order does Python evaluate the function expression, positional arguments, and keyword arguments in a call, when they have side effects?"
description: "In what order does Python evaluate the function expression, positional arguments, and keyword arguments in a call, when they have side effects?"
track: python
section: syntax-and-control-flow
level: senior
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
  - source_id: py314-reference-expressions
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-reference-simple-stmts
    title: "Python 3.14: Reference/simple Stmts"
    url: https://docs.python.org/3.14/reference/simple_stmts.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-reference-compound-stmts
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
---

## Short answer

**Python evaluates the callable expression first, then all the argument expressions before the call begins, with `*expr` evaluated before the keyword arguments even when it is written after them.**[^py314-reference-expressions] The overall order is: primary expression -> positional arguments (left to right) -> `*unpack` -> keyword arguments -> `**unpack`. This is a language guarantee (left-to-right evaluation), not an implementation detail.

## Detailed explanation

A call in Python is an ordinary expression, and its parts are evaluated in a fixed order defined by
the language rather than left to the implementation. The callable itself is evaluated first, then
the arguments, and only after that does the call happen.[^py314-reference-expressions]

That the callable is evaluated **first** becomes visible when it is itself an expression with a side
effect: `get_handler()(compute())` calls `get_handler` before `compute`, even though they sit next
to each other in the text.

The arguments are evaluated left to right, and that applies to all the forms together - positional,
`*` unpacking, keyword and `**` unpacking.

```python
def trace(name):
    print(name)
    return name

f(trace('a'), trace('b'), key=trace('c'))
# prints a, b, c - strictly left to right
```

A subtlety that is easy to miss: `*expr` is evaluated together with the positional arguments, that
is **before** the keyword ones - even when it is written after them.

```python
f(key=trace('kw'), *trace_iterable('star'))
# prints star, then kw - the *unpacking goes first despite the written order
```

That is precisely why such a spelling is confusing and considered poor style: the visual order does
not match the evaluation order. Writing `*args` before the keyword arguments is a simple way to
avoid it.

**The overall order worth remembering:**
- the expression producing the callable;
- positional arguments, left to right;
- `*expr` unpacking;
- keyword arguments, left to right;
- `**expr` unpacking;
- and only then the call itself, with parameter binding.

This is a language guarantee rather than a CPython detail, so it can be relied on in portable code.
But it is worth relying on rarely: code whose correctness depends on argument evaluation order is
hard to read - better to compute the values on separate lines and pass them ready-made.[^py314-reference-simple-stmts]

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
