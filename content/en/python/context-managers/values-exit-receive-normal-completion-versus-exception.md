---
id: py-ctxmgr-0001
title: "What values does `__exit__` receive on normal completion versus on an exception inside the `with` block?"
description: "What values does `__exit__` receive on normal completion versus on an exception inside the `with` block?"
track: python
section: context-managers
level: middle
type: mechanism
tags: [exit]
status: published
updated: 2026-09-27
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-reference-datamodel-with-statement-context-managers
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#with-statement-context-managers
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-contextlib
    title: "Python 3.14: Library/contextlib"
    url: https://docs.python.org/3.14/library/contextlib.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-asyncio-task-task-cancellation
    title: "Python 3.14: Library/asyncio Task"
    url: https://docs.python.org/3.14/library/asyncio-task.html#task-cancellation
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
---

## Short answer

**On normal completion, `__exit__` receives `(None, None, None)`, whereas on an exception inside the `with` block it receives `(exc_type, exc_val, exc_tb)`: the exception class, instance, and traceback.**[^py314-reference-datamodel-with-statement-context-managers] If no exception occurred, all three arguments are `None`; if an exception was raised, they correspond to the values returned by `sys.exc_info()`. The return value of `__exit__` determines whether the exception is suppressed or propagated.

## Detailed explanation

The context manager protocol in Python is governed by two complementary methods: `__enter__()` and `__exit__(self, exc_type, exc_val, exc_tb)`.[^py314-reference-datamodel-with-statement-context-managers] The `__enter__` method executes immediately before entering the body of the `with` statement, while `__exit__` is guaranteed to be invoked upon leaving the block under all conditions – whether completing normally, raising an unhandled exception, or exiting early via `return`, `break`, or `continue`.

The three arguments passed into `__exit__` explicitly differentiate execution outcomes:
- normal completion: if the body of the `with` block executes without error or exits through control-flow statements (`return`, `break`), `__exit__` is called with `(None, None, None)`;
- exception raised: if an unhandled exception occurs inside the block, the arguments receive a triad matching `sys.exc_info()`: `exc_type` receives the exception class, `exc_val` holds the specific exception instance, and `exc_tb` receives the call-stack `traceback` object.

The runtime behaviour following `__exit__` depends entirely on its return value. If `__exit__` returns a truthy value (such as `True`), Python suppresses the exception, and execution resumes normally with the statement immediately following the `with` block. If it returns `False`, `None` (the default when no explicit `return` statement is written), or any other falsy value, Python automatically re-raises the original exception, preserving its initial traceback intact.[^py314-reference-datamodel-with-statement-context-managers] For generator-based context managers decorated with `@contextlib.contextmanager`, this mechanism is mediated by calling `generator.throw()` at the `yield` statement.[^py314-library-contextlib]

Demonstration of received arguments and exception suppression semantics in `__exit__`:

```python
class TrackerContext:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print("Normal exit:", (exc_type, exc_val, exc_tb))
            return None  # return value is ignored on normal completion
        print(f"Exception caught: {exc_type.__name__}: {exc_val}")
        # Suppress ValueError, propagate any other exception
        return issubclass(exc_type, ValueError)

# Case 1: Normal completion
with TrackerContext():
    print("Executing body normally")
# Output:
# Executing body normally
# Normal exit: (None, None, None)

# Case 2: Exception raised and suppressed
with TrackerContext():
    raise ValueError("demonstration failure")
print("Continued execution after suppressed ValueError")
# Output:
# Exception caught: ValueError: demonstration failure
# Continued execution after suppressed ValueError
```

**Common mistakes and practical rules:**
- explicitly re-raising `raise exc_val` inside `__exit__` is an anti-pattern: it attaches redundant traceback frames; to propagate an exception, simply return `False` or `None`;
- inadvertently returning a truthy value (such as the result of a logging call or `return 1`) silently swallows all exceptions in the block, masking critical bugs;
- upon normal completion, the return value of `__exit__` is completely ignored; it only affects execution flow when `exc_type is not None`;
- if `__exit__` itself raises a new exception during cleanup, that new exception supersedes the original one, chaining it through the `__context__` attribute.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
