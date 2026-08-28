---
id: py-syntax-0002
title: "What value does the expression `[] or \"fallback\"` produce, and why is the result not `True` or `False`?"
description: "What value does the expression `[] or \"fallback\"` produce, and why is the result not `True` or `False`?"
track: python
section: syntax-and-control-flow
level: middle
type: mechanism
tags: [or-fallback]
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  uk: 2
execution:
  language: python
  standard: null
  toolchain:
    name: cpython
    version: "3.14.7"
  flags: []
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
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/coding.md#L3-L20
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**The result is `'fallback'`, because `[]` is falsy and `or` returns its second operand.**[^py314-reference-expressions] The `or` operator does not reduce its result to a `bool`; it returns the very object that settled the result. An empty list has `__bool__` -> `False`, so `or` evaluates and returns `"fallback"` as it is.

```text
>>> [] or "fallback"
'fallback'
```

## Detailed explanation

`or` is not a converter to `bool`. It evaluates the left operand, asks it for truthiness, and
returns an **object**: the left one if it is truthy, otherwise the right one - as
is.[^py314-reference-expressions]

Here the left operand is an empty list. A list defines `__len__`, and a zero length makes it falsy,
so `or` moves on to the right operand and returns the string `'fallback'` rather than `True`.

```python
[] or 'fallback'      # 'fallback' - the str object itself
[1] or 'fallback'     # [1]        - the list, because it is truthy
[] or []              # []         - the second empty list; still falsy
bool([] or 'fallback')  # True     - only bool() actually converts
```

The truthiness rule is simple: an object is falsy if its `__bool__` returned `False`, or, in the
absence of `__bool__`, if `__len__` returned zero. Everything else is truthy, including non-empty
containers, non-zero numbers and any object defining neither
method.[^py314-reference-simple-stmts]

**What follows from this:**
- the result type of `or` is the union of the operand types, not `bool`; an annotation `-> bool`
  would be wrong;
- the chain `a or b or c` returns the first truthy operand, and if all are falsy the last one, `c`;
- `x or default` cannot tell "no value given" from "a falsy value given": `0` and `''` get replaced
  too;
- if a boolean result is what is needed, say so explicitly: `bool(x or y)`;
- inside an `if` the difference is invisible, because `if` reduces the result to truthiness itself -
  which is why the mistake is only noticed once the value is stored or returned.

The same applies to `and`, only mirrored: `[] and 'x'` gives `[]`, because the first operand is
falsy and settles the result immediately.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
