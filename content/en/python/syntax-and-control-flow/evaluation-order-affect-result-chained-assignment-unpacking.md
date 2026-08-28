---
id: py-syntax-0006
title: "How does evaluation order affect the result of a chained assignment or unpacking when the right-hand expression has side effects?"
description: "How does evaluation order affect the result of a chained assignment or unpacking when the right-hand expression has side effects?"
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

**The right-hand side is evaluated first, then the targets on the left are assigned left to right; side effects in the right-hand expression therefore affect all targets.**[^py314-reference-expressions] With `i, x[i] = 1, 2` (where `i=0, x=[0,1]`), for example, the tuple `(1, 2)` is evaluated first, then `i` becomes `1`, and after that `x[1]` (with the new `i` already in effect) becomes `2` - giving `x == [0, 2]`.

## Detailed explanation

Assignment in Python has two steps in a strictly defined order: the right-hand side is evaluated in
full first, then the result is distributed over the targets on the left **left to
right**.[^py314-reference-simple-stmts]

While the targets are independent, that order is invisible. It becomes visible when one target
affects where another one is written - when a name on the left is also part of the index of another
target, for instance.

```python
i = 0
x = [0, 1]

i, x[i] = 1, 2
# step 1: the right side becomes the tuple (1, 2)
# step 2: i = 1        <- the name is rebound first
# step 3: x[i] = 2     <- and `i` is already 1 here, so x[1] is written

x    # [0, 2]  - not [2, 1]
```

Swapping the targets changes the result, because the write into the list happens with the old `i`.

```python
x[i], i = 2, 1
# step 2: x[0] = 2     <- `i` is still 0 here
# step 3: i = 1
```

Chained assignment obeys the same rule: `a = b = expr` evaluates `expr` once and assigns it to the
targets left to right, so `a` first and then `b`. It is not `a = (b = expr)` - no such expression
exists in Python.

```python
a = b = []
a.append(1)
b            # [1] - both names refer to the SAME object, evaluated once
```

**What follows in practice:**
- `a, b = b, a` works precisely because the right-hand side is evaluated before the first
  assignment: the tuple already holds the old values;
- `a = b = []` creates **one** list for two names, not two empty ones - the classic reason for "why
  did my second list change too";
- when unpacking with side effects on the right, all the calls happen before any target receives a
  value;
- augmented assignment (`x[i] += 1`) is a separate case: it reads, modifies and writes the same
  target, and the index is evaluated once.[^py314-reference-expressions]

The rule reduces to one sentence: the right is evaluated fully and once; the left is assigned in
turn and already sees the earlier assignments.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
