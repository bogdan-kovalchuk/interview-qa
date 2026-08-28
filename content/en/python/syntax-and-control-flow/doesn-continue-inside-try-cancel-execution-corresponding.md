---
id: py-syntax-0008
title: "Why doesn't `continue` inside a `try` cancel the execution of the corresponding `finally` before the next iteration?"
description: "Why doesn't `continue` inside a `try` cancel the execution of the corresponding `finally` before the next iteration?"
track: python
section: syntax-and-control-flow
level: middle
type: pitfall
tags: [continue]
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

**`finally` always runs "on the way out" of a `try`, no matter whether the exit happens through `return`, `break` or `continue`.**[^py314-reference-expressions] When a `continue` executes inside a `try` block, Python runs the `finally` clause first and only then moves to the next iteration of the loop. <span class="warn">If the `finally` itself executes a `return`, `break` or `continue`, that overwrites the pending instruction from the `try`.</span>

## Detailed explanation

`finally` is not "the block that runs after `try`" but the block that runs on **any exit** from the
`try`. The language lists those exits explicitly: normal completion, an exception, `return`, `break`
and `continue`.[^py314-reference-compound-stmts]

A `continue` therefore does not cancel `finally`; it defers itself. The interpreter remembers the
intent to move to the next iteration, runs `finally`, and only then carries that intent out. The
same goes for `return`: the value is already computed, but the return happens after `finally`.

```python
for i in range(3):
    try:
        if i == 1:
            continue
        print('body', i)
    finally:
        print('finally', i)

# body 0 / finally 0 / finally 1 / body 2 / finally 2
```

For `i == 1` the body did not continue, yet the `finally` did run. This is what the reliability of
resource release rests on: no way of leaving the block lets you skip it.

The dangerous part begins when the `finally` itself executes a `return`, `break` or `continue`. The
intent saved from the `try` is then simply lost - including an exception that was supposed to
propagate.[^py314-reference-simple-stmts]

```python
def f():
    try:
        raise ValueError('lost')
    finally:
        return 'swallowed'    # the exception disappears silently

f()   # 'swallowed' - no traceback, no error
```

**What to take away from this:**
- `finally` runs before a `continue`, `break` or `return` actually happens;
- an exception flying through the `try` also waits for `finally` and only then propagates;
- a `return` in `finally` suppresses both the exception and any earlier `return` - almost always a
  bug, and linters complain about it;
- a `break` or `continue` in `finally` does the same to control flow: it overwrites the saved
  intent.

The practical rule: put only cleanup in a `finally`. Any statement that changes control flow turns
the "guaranteed block" into the place where the guarantees are lost.

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
