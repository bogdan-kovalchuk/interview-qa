---
id: py-ctxmgr-0002
title: "What does a truthy return value from `__exit__` mean, and why is an accidental `return True` dangerous?"
description: "What does a truthy return value from `__exit__` mean, and why is an accidental `return True` dangerous?"
track: python
section: context-managers
level: middle
type: pitfall
tags: [exit, return-true]
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

**A truthy return value from `__exit__` suppresses the exception – it will not propagate beyond the `with` block.**[^py314-reference-datamodel-with-statement-context-managers] <span class="warn">An accidental `return True` swallows any exception, including `TypeError`, `KeyboardInterrupt`, and errors within the cleanup code itself.</span> This severely complicates diagnostics: bugs inside the `with` body become completely invisible. It is generally safer to return `False` or `None` and suppress only expected types through explicit checks.

## Detailed explanation

The `__exit__(exc_type, exc_val, exc_tb)` method of a context manager is invoked by the interpreter when leaving a `with` block, and its boolean return value dictates the fate of any active exception: any truthy value signals Python that the exception was handled and its propagation must be suppressed.[^py314-reference-datamodel-with-statement-context-managers]

If no error occurred within the `with` block, all three arguments `exc_type`, `exc_val`, and `exc_tb` are `None`. When an exception is raised, the interpreter passes its type, instance, and traceback to `__exit__`. By default, if the method terminates without an explicit `return` (returning `None`) or explicitly returns `False`, Python resumes re-raising the exception up the call stack.

The danger arises when developers write `return True` out of habit, mistaking it for a status code indicating that cleanup succeeded. Consequently, the context manager silently swallows critical programming bugs (`NameError`, `TypeError`, `AttributeError`), unexpected runtime exceptions, and even `KeyboardInterrupt` or `asyncio.CancelledError`.[^py314-library-asyncio-task-task-cancellation] Subsequent code then proceeds with corrupted or invalid state, leaving developers with no traceback or logs to diagnose why the failure occurred.

Demonstration of dangerous versus safe return values from `__exit__`:

```python
class SwallowingManager:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # DANGEROUS: unconditional truthy return swallows all exceptions!
        return True


class SafeManager:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Safe: inspect exc_type and only suppress specific, expected errors
        if exc_type is not None and issubclass(exc_type, KeyError):
            return True  # Suppress only KeyError
        return False  # Propagate TypeError, NameError, KeyboardInterrupt, etc.


# 1. Dangerous pattern hides critical bugs
with SwallowingManager():
    typo_name_error  # NameError is silently swallowed; bug goes unnoticed

# 2. Safe pattern suppresses only intended exceptions
with SafeManager():
    data = {}
    _ = data["missing"]  # KeyError is cleanly handled and suppressed

print("Execution continued safely")
```

To eliminate such subtle bugs, the standard library provides specialized utilities such as `contextlib.suppress`, where the exception types eligible for suppression are declared explicitly.[^py314-library-contextlib]

**Common mistakes and recommendations:**
- returning `True` as a status indicator that cleanup completed without error, resulting in the accidental loss of the real exception;
- omitting type inspection before suppressing – always verify `exc_type` via `issubclass(exc_type, ExpectedException)` or `isinstance(exc_val, ExpectedException)`;
- accidentally swallowing control-flow and system exceptions (`KeyboardInterrupt`, `SystemExit`, `CancelledError`), which should never be suppressed by general-purpose context managers;
- explicitly returning `False` or omitting `return` entirely (defaulting to `None`) when the context manager's sole responsibility is resource cleanup rather than error handling.

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
