---
id: py-excpt-0005
title: "In Python 3.14, what happens to a pending `return` from a `try` if `finally` also executes a `return`, and why does the compiler now emit a `SyntaxWarning` for that control flow?"
track: python
section: exceptions
sources:
  - source_id: py314-tutorial-errors
    title: "Python 3.14: Tutorial/errors"
    url: https://docs.python.org/3.14/tutorial/errors.html
  - source_id: py314-library-exceptions
    title: "Python 3.14: Library/exceptions"
    url: https://docs.python.org/3.14/library/exceptions.html
  - source_id: py314-reference-compound-stmts-the-try-statement
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#the-try-statement
  - source_id: pep-0765-finally-control-flow
    title: "PEP 765: Disallow return/break/continue that exit a finally block"
    url: https://peps.python.org/pep-0765/
---

## Short answer

**A `return` in `finally` always wins: the function returns the value from `finally`, and the pending `return` from `try` is discarded.**[^py314-tutorial-errors] It is the last `return` executed, so the interpreter uses its value. CPython 3.14 emits a `SyntaxWarning` for `return` in `finally`, because such a pattern hides exceptions and makes control flow confusing.[^py314-tutorial-errors]

```python
def foo():
    try:
        return 'try'
    finally:
        return 'finally'

foo()  # returns 'finally'; CPython 3.14 warns at compile time
```

## Detailed explanation

When `try` reaches a `return`, the value is already computed, but the function has not returned yet: `finally` runs first, and the last `return` executed determines the result. If `finally` contains a `return`, its value becomes the function's result, and the value from `try` is discarded. Likewise, a `return`, `break` or `continue` in `finally` discards an exception that was propagating from `try`: it is not re-raised.[^py314-reference-compound-stmts-the-try-statement]

```python
def bar():
    try:
        1 / 0                     # raises ZeroDivisionError
    finally:
        return 42                 # the exception is discarded, not re-raised

print(bar())                      # 42
```

CPython 3.14 emits a `SyntaxWarning` for `return`, `break` or `continue` that exit a `finally` block. Before that, including in CPython 3.13, there is no such warning.[^py314-reference-compound-stmts-the-try-statement][^py314-tutorial-errors] The motivation is that a swallowed exception is more dangerous than a wrong return value, because it is more likely to slip through testing.[^pep-0765-finally-control-flow]

The language specification permits a `SyntaxWarning` or a `SyntaxError`, and PEP 765 expects the warning to appear at compilation, not when already compiled code runs.[^pep-0765-finally-control-flow] On CPython 3.14 it appears with `compile()`, when a module is imported without an up-to-date `.pyc`, and under `py_compile`, but not with `ast.parse()` and not when a module is imported from an existing `.pyc`. So a tool that only parses code with `ast.parse()` will not see it. In CPython 3.14, a `return` inside a nested function defined in `finally` does not trigger the warning, because it exits that other function, not the `finally` block.

**Common mistakes:**
- assuming that a `return` in `try` takes effect when `finally` also contains a `return`;
- expecting an exception from `try` to be re-raised after a `finally` with `return`, `break` or `continue`;
- ignoring the `SyntaxWarning` because the code already works: the warning is shown at compile time, not while compiled code runs.
