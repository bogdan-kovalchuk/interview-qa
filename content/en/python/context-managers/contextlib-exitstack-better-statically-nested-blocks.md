---
id: py-ctxmgr-0006
title: "When is `contextlib.ExitStack` better than statically nested `with` blocks?"
description: "When is `contextlib.ExitStack` better than statically nested `with` blocks?"
track: python
section: context-managers
level: middle
type: comparison
tags: [contextlib-exitstack]
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

**`ExitStack` is needed when the number of resources or cleanup operations is determined dynamically at runtime.**[^py314-reference-datamodel-with-statement-context-managers] Static nested `with` statements only work when the set of resources is fixed and known in advance. `ExitStack` allows registering context managers and arbitrary callbacks conditionally or inside loops, guaranteeing LIFO cleanup order. It is also invaluable for "all-or-nothing" acquisition: if opening one resource fails, all previously acquired resources are reliably closed.

## Detailed explanation

The `contextlib.ExitStack` class provides a programmatic interface for managing dynamic collections of context managers and cleanup callbacks whose quantity and structure are only known at runtime.[^py314-library-contextlib]

A static `with` statement (whether nested across multiple indentation levels or combined via commas like `with A() as a, B() as b:`) requires hardcoding the exact set of resources at authoring time. Moreover, compound comma-separated `with` expressions harbor an acquisition hazard: if initializing resource `B()` raises an exception, resource `A()` may be leaked without being entered into an active context. Static syntax cannot handle a variable-length list of resources or conditional resource acquisition inside loops.

`ExitStack` resolves this limitation by maintaining an internal LIFO (Last-In, First-Out) stack of cleanup callbacks. The `stack.enter_context(cm)` method first calls `__enter__`, and only upon successful entry registers the manager's `__exit__` method onto the stack. If an exception occurs while acquiring the N-th resource, `ExitStack` immediately unwinds the stack in reverse order, ensuring that all previously acquired resources are deterministically closed.[^py314-reference-datamodel-with-statement-context-managers] Furthermore, `stack.callback()` accepts arbitrary cleanup functions directly, and `stack.pop_all()` enables transactional "all-or-nothing" resource handoff patterns.

Dynamic resource management and guaranteed teardown using `ExitStack`:

```python
from contextlib import ExitStack
from tempfile import NamedTemporaryFile


def process_dynamic_files(file_paths):
    # Static 'with' cannot handle a variable-length list of paths.
    # ExitStack guarantees LIFO cleanup even if an error occurs mid-loop.
    with ExitStack() as stack:
        handles = [stack.enter_context(open(path, "r")) for path in file_paths]
        # Register an arbitrary cleanup callback without a full context manager
        stack.callback(print, "All files processed, closing resources")
        return [h.read() for h in handles]


# Demonstration with temporary files
with NamedTemporaryFile("w+", delete=False) as f1, NamedTemporaryFile(
    "w+", delete=False
) as f2:
    f1.write("file1")
    f2.write("file2")
    f1.flush()
    f2.flush()

    contents = process_dynamic_files([f1.name, f2.name])
    print(f"Read {len(contents)} files successfully")
```

**Key advantages of `ExitStack` over static blocks:**
- dynamic resource pools: effortlessly manages variable-length collections of resources in a loop without increasing indentation depth;
- atomic acquisition: if an error occurs mid-loop, all previously acquired descriptors are guaranteed to be cleaned up;
- arbitrary callbacks: the `callback()` method eliminates the need to create custom context manager classes for simple teardown functions (`close`, `release`, `disconnect`);
- ownership transfer: `pop_all()` transfers the cleanup responsibilities to a newly created stack or long-lived object once all resources have successfully initialized.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
