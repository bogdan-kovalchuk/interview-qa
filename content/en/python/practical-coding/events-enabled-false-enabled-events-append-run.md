---
id: py-prac-0002
title: "What does `events = []; enabled = False; enabled and events.append(\"run\"); print(events)` print, and why didn't the side effect happen?"
description: "It prints []: `and` short-circuits because enabled is False, so append is never called."
track: python
section: practical-coding
level: middle
type: mechanism
tags: [events-enabled-false-enabled-and-events-append-run-print-events]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-tutorial
    title: "Python 3.14: Tutorial"
    url: https://docs.python.org/3.14/tutorial/
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-reference
    title: "Python 3.14: Reference"
    url: https://docs.python.org/3.14/reference/
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-reference-expressions
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#boolean-operations
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation, Boolean operations section: `and` evaluates its left operand first and evaluates the right one only when the left one does not decide the result; the operand's value is returned, not converted to bool."
---

## Short answer

**It prints `[]`: the `append` method is never called.** The `and` operator evaluates its left operand first; if that operand is false, it becomes the value of the expression and the right operand is not evaluated.[^py314-reference-expressions] Because `enabled` is `False`, `events.append("run")` never runs, and the list stays empty.

## Detailed explanation

`and` is not a function that receives two values that are already computed; it is an expression with a defined evaluation order. Python first evaluates the left operand, `enabled`. If its value is false, the expression returns it without evaluating the right operand.[^py314-reference-expressions] So `events.append("run")` is never called, and `print(events)` sees an empty list.

To see this without a list, replace the right operand with a function call that has a visible side effect:

```python
def log(message):
    print("called:", message)
    return True


enabled = False
enabled and log("run")  # no output: the right operand is never evaluated
enabled = True
enabled and log("run")  # called: run
```

The value of `and` is not reduced to `bool`: the last evaluated operand is returned. So `0 and "x"` gives `0`, and `"a" and "b"` gives `"b"`.[^py314-reference-expressions] The expression `enabled and events.append("run")` gives `False`, but nothing uses that value. For a side effect, `if enabled:` with a separate block is clearer: the condition then reads as a command, not as a value being computed.

**Common mistakes:**
- assuming that the right operand of `and` is always evaluated, so `append` is at least called;
- treating `and` as a function that always returns `True` or `False`;
- putting side effects into `and` or `or` instead of using `if`.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
