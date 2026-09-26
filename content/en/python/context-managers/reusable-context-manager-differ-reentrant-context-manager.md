---
id: py-ctxmgr-0010
title: "How does a reusable context manager differ from a reentrant context manager?"
description: "How does a reusable context manager differ from a reentrant context manager?"
track: python
section: context-managers
level: middle
type: comparison
tags: []
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

**A reusable context manager can be used across multiple sequential `with` blocks but cannot be nested inside itself; a reentrant context manager can be both reused sequentially and nested recursively.**[^py314-reference-datamodel-with-statement-context-managers] Example of reusable: `contextlib.ExitStack` or `threading.Lock` – a new `with` block works after exit, but nesting on the same instance corrupts internal state or deadlocks. Example of reentrant: `threading.RLock` or `contextlib.redirect_stdout` – they correctly support nesting by tracking recursion depth or managing an internal stack of previous states.

## Detailed explanation

The distinction between reusable and reentrant context managers lies in their ability to correctly support simultaneous activation across nested `with` blocks within the same thread.[^py314-library-contextlib] A reusable context manager permits repeated invocations of `__enter__` and `__exit__` strictly sequentially: upon exiting a block, its internal state resets so the instance can be used in a subsequent `with` statement. However, attempting to enter an already active instance before the previous exit completes causes state corruption, an exception, or a deadlock.

A reentrant context manager is not only reusable sequentially, but also safely tolerates arbitrary levels of recursive or nested entries.[^py314-reference-datamodel-with-statement-context-managers] Instead of maintaining a single binary activity flag, it maintains a nesting depth counter (as seen in `threading.RLock`) or an internal stack of previous environments (as in `contextlib.redirect_stdout`). Each `__enter__` call increments the depth or pushes the active environment, while the matching `__exit__` decrements the counter or pops the stack, only releasing the underlying resource once the outermost context exits.

Most standard context managers, such as file descriptors from `open()` or generators decorated with `@contextlib.contextmanager`, are single-use: attempting to reuse the same instance in another `with` block raises a `ValueError` or `RuntimeError`. Designing a truly reentrant context manager requires choosing state representations that isolate or stack each nesting layer rather than overwriting shared instance attributes.

Demonstration of the difference between a sequential activity flag and a nesting depth counter:

```python
class ReusableContext:
    def __init__(self):
        self._active = False

    def __enter__(self):
        if self._active:
            raise RuntimeError("Cannot re-enter an already active context")
        self._active = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._active = False

class ReentrantContext:
    def __init__(self):
        self._depth = 0

    def __enter__(self):
        self._depth += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._depth -= 1

# Sequential reuse: both work
reusable = ReusableContext()
with reusable:
    pass
with reusable:
    pass  # Succeeds sequentially

# Nested entry: Reusable fails, Reentrant succeeds
reentrant = ReentrantContext()
with reentrant:
    with reentrant:
        print(f"Reentrant depth: {reentrant._depth}")

try:
    with reusable:
        with reusable:
            pass
except RuntimeError as err:
    print(f"Reusable error: {err}")

# Output:
# Reentrant depth: 2
# Reusable error: Cannot re-enter an already active context
```

**Common mistakes and practical limitations:**
- treating `@contextlib.contextmanager` instances as reusable: generators cannot be restarted after finishing, requiring a fresh call for each `with` block;
- assuming `threading.Lock` is reentrant: attempting to acquire a standard lock a second time in the same thread causes a deadlock, whereas `threading.RLock` tracks the owning thread and recursion count;
- confusing single-thread reentrancy with thread-safety: reentrancy applies to nested calls on the same execution thread, rather than concurrent access from distinct threads.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
