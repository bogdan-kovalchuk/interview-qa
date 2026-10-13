---
id: py-excpt-0004
title: "When does the `else` clause of a `try/except/else/finally` construct run, and why put success-path code there?"
description: "When does the `else` clause of a `try/except/else/finally` construct run, and why put success-path code there?"
track: python
section: exceptions
level: middle
type: mechanism
tags: [try-except-else-finally]
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

**`else` runs only when `try` finishes without an exception and without a `return`, `break` or `continue`.**[^py314-reference-compound-stmts-the-try-statement] Code that must run only when the `try` clause raises no exception is useful in `else`.[^py314-tutorial-errors] An exception raised in `else` is not handled by the preceding `except` clauses, but `finally` still runs for cleanup.[^py314-reference-compound-stmts-the-try-statement]

## Detailed explanation

A `try` block should guard only the operation that may raise the expected exception, while success-path code runs after it. `else` runs when control leaves `try` without an exception and without a `return`, `break` or `continue`.[^py314-reference-compound-stmts-the-try-statement] So a `return` in `try` skips `else`, but `finally` always runs.

```python
def to_int(text):
    try:
        number = int(text)            # the only call here that may raise ValueError
    except ValueError:
        return None
    else:
        return number * 2             # runs only when int() succeeded
    finally:
        print("checked", repr(text))

print(to_int("21"))  # checked '21', then 42
print(to_int("x"))   # checked 'x', then None
```

If the success-path steps stay inside `try`, `except ValueError` also catches their exceptions, even though it exists only for parsing errors. For example, a `ValueError` raised by a number-processing function would look like an input error. Handlers apply to exceptions raised in the `try` block, including inside functions called from it (even indirectly).[^py314-reference-compound-stmts-the-try-statement][^py314-tutorial-errors] So the less code there, the more precisely it is defined what gets caught.

An exception raised in `else` is not handled by the preceding `except` clauses, but `finally` still runs, and the temporarily saved exception is re-raised afterwards.[^py314-reference-compound-stmts-the-try-statement] So `else` is for success-path code, `try` for calls that can be expected to fail, and `finally` for cleanup.

**Common mistakes:**
- putting a risky call in `else` and expecting `except` to catch it;
- assuming `else` runs after a `return` in `try`;
- confusing `else` with `finally`: `else` is skipped on `return`, `break` or `continue`, while `finally` is not.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
