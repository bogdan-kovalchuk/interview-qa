---
id: py-excpt-0006
title: "How can an exception in `finally` mask the original exception, and how do you preserve the diagnostic context?"
description: "How can an exception in `finally` mask the original exception, and how do you preserve the diagnostic context?"
track: python
section: exceptions
level: senior
type: pitfall
tags: []
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-tutorial-errors
    title: "Python 3.14: Tutorial/errors"
    url: https://docs.python.org/3.14/tutorial/errors.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-exceptions
    title: "Python 3.14: Library/exceptions"
    url: https://docs.python.org/3.14/library/exceptions.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-reference-compound-stmts-the-try-statement
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#the-try-statement
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
---

## Short answer

**If `finally` raises a new exception, it replaces the original one in propagation, and the original survives only as `__context__`.**[^py314-reference-compound-stmts-the-try-statement] <span class="warn">If you log only the new exception, the original cause disappears from the log.</span> To keep the context, wrap the cleanup in an inner `try/except` inside `finally` and log the cleanup error; the saved original exception is then re-raised at the end of `finally`.[^py314-reference-compound-stmts-the-try-statement]

## Detailed explanation

If `finally` raises a new exception while another is still propagating, the original exception is not lost: it becomes the `__context__` of the new one. The documentation describes this: when an exception is raised while another is being handled, its `__context__` is set automatically, and handling can also happen in a `finally` clause.[^py314-library-exceptions] The new exception replaces the old one in propagation, so an `except` further up the stack sees only the new one.[^py314-reference-compound-stmts-the-try-statement]

```python
def work():
    try:
        raise ValueError("original failure")
    finally:
        raise RuntimeError("cleanup failed")  # replaces the original in flight

try:
    work()
except RuntimeError as e:
    print(e)                          # cleanup failed
    print(repr(e.__context__))        # ValueError('original failure')
```

In CPython the standard traceback prints both exceptions, separated by the line "During handling of the above exception, another exception occurred". The problem is code that sees only the new exception: it logs only its text, or catches the type of the original exception, which no longer reaches it.

The safer option is to handle the cleanup error inside `finally`. The inner `except` absorbs it, so no new exception arises, and the saved original exception is re-raised at the end of the `finally` clause.[^py314-reference-compound-stmts-the-try-statement]

```python
def work():
    try:
        raise ValueError("original failure")
    finally:
        try:
            raise RuntimeError("cleanup failed")  # stands in for a failing close()
        except RuntimeError as cleanup_error:
            print("cleanup error logged:", cleanup_error)

try:
    work()
except ValueError as e:
    print("original propagated:", e)  # original propagated: original failure
```

In real code, use `logging` instead of `print`. An explicit chain via `raise ... from` (`__cause__`) is appropriate when the new exception is really a consequence of the old one, not an unrelated cleanup failure.[^py314-library-exceptions]

**Common mistakes:**
- logging only `str(e)` of the new exception and losing the root cause;
- catching the original exception's type from outside without noticing that a different type was raised;
- assuming `__context__` is always visible: code that prints only an exception's message will not show it.

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
