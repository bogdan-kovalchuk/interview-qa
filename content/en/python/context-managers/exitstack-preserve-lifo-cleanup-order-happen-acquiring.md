---
id: py-ctxmgr-0007
title: "How does `ExitStack` preserve LIFO cleanup order, and what should happen if acquiring one of the resources fails?"
description: "How does `ExitStack` preserve LIFO cleanup order, and what should happen if acquiring one of the resources fails?"
track: python
section: context-managers
level: senior
type: mechanism
tags: [exitstack]
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

**`ExitStack` maintains a list of exit callbacks in registration order and invokes them in reverse order (LIFO), exactly like nested `with` statements.**[^py314-reference-datamodel-with-statement-context-managers] If `enter_context()` raises an exception for a subsequent resource, `ExitStack` still invokes `__exit__` for all previously registered managers – the already-acquired resources. This guarantees proper cleanup even during a partial acquisition failure.

## Detailed explanation

`contextlib.ExitStack` implements a dynamic LIFO (Last-In, First-Out) stack of context managers and arbitrary callbacks by storing them in an internal `_exit_callbacks` list.[^py314-library-contextlib] When `stack.enter_context(cm)` is called, `ExitStack` first extracts the unbound `__exit__` method from the manager's type, executes `__enter__()`, and appends `__exit__` to the internal stack only after a successful return.[^py314-reference-datamodel-with-statement-context-managers] If acquiring a subsequent resource raises an exception, that failed manager is never registered, but the exception immediately propagates into the enclosing `with ExitStack()`, initiating an unwinding sequence for all previously registered resources.

Unwinding precisely reproduces the semantics of nested `with` statements: callbacks are popped one by one and called with arguments representing the current active exception.[^py314-library-contextlib] If any callback returns a truthy value, the exception is considered suppressed, and preceding (outer) callbacks receive `None, None, None`, exactly as if an inner `try...except` block had handled it. If a callback itself raises a new exception during unwinding, Python links it to the pending exception via exception chaining (`__context__`), preventing the original failure cause from being silently lost.

In senior architecture, `ExitStack` is the standard building block for transactional multi-resource acquisition (the all-or-nothing pattern). This is accomplished using `stack.pop_all()`, which migrates all registered callbacks into a new `ExitStack` and clears the current one.[^py314-library-contextlib] When all resources are successfully acquired, a factory function calls `return stack.pop_all()`, disarming the local stack upon function exit and transferring cleanup responsibility to the caller.

Demonstration of LIFO cleanup of already-acquired resources when a subsequent acquisition fails:

```python
from contextlib import ExitStack

class Resource:
    def __init__(self, name: str, fail_on_enter: bool = False):
        self.name = name
        self.fail_on_enter = fail_on_enter

    def __enter__(self):
        if self.fail_on_enter:
            raise RuntimeError(f"Failed to acquire {self.name}")
        print(f"Acquired: {self.name}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Cleaned up: {self.name} (exc: {exc_type.__name__ if exc_type else None})")
        return False  # Do not suppress exceptions

# When acquiring resource 'res3' fails, res2 and res1 are cleaned up in LIFO order
try:
    with ExitStack() as stack:
        r1 = stack.enter_context(Resource("res1"))
        r2 = stack.enter_context(Resource("res2"))
        r3 = stack.enter_context(Resource("res3", fail_on_enter=True))
except RuntimeError as err:
    print(f"Caught: {err}")

# Output:
# Acquired: res1
# Acquired: res2
# Cleaned up: res2 (exc: RuntimeError)
# Cleaned up: res1 (exc: RuntimeError)
# Caught: Failed to acquire res3
```

**Practical consequences and architectural nuances:**
- partial initialization does not leak resources: every previously opened file descriptor, socket, or lock is guaranteed to be closed;
- cleanup order is strictly the inverse of acquisition order: dependent resources are torn down before the resources they depend on;
- to safely transfer ownership of resources outside the local scope, use `stack.pop_all()` rather than attempting to manually mutate the internal callback list.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
