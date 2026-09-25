---
id: py-ctxmgr-0005
title: "Why must a generator used with `@contextmanager` execute exactly one `yield`?"
description: "Why must a generator used with `@contextmanager` execute exactly one `yield`?"
track: python
section: context-managers
level: middle
type: pitfall
tags: [contextmanager]
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

**The `@contextmanager` protocol maps exactly one `yield` to a single enter/exit pairing; zero or multiple yields violate this contract.**[^py314-reference-datamodel-with-statement-context-managers] If the generator fails to execute `yield` (for instance, via an early `return`), `@contextmanager` raises `RuntimeError: generator didn't yield`. If it yields an additional value after the first one, it raises `RuntimeError: generator didn't stop`. This invariant guarantees that context entry and exit logic are executed exactly once.

## Detailed explanation

The `@contextmanager` decorator relies on a strict two-phase execution lifecycle where a single `yield` statement serves as the unambiguous dividing line between setup and teardown.[^py314-library-contextlib]

Upon entering a `with` block, the wrapper's `__enter__` method calls `next(gen)`. The generator is expected to execute initial configuration and suspend at `yield`, providing the target value for the `as` clause. If an early `return` or unhandled guard clause causes the generator to terminate before reaching `yield`, the iterator protocol raises `StopIteration` prematurely, which `@contextmanager` catches and converts into a fatal `RuntimeError("generator didn't yield")`.[^py314-reference-datamodel-with-statement-context-managers]

Upon exiting the `with` block, the wrapper's `__exit__` method resumes the generator using `next(gen)` (or `gen.throw()` if an exception occurred in the body). The contract dictates that the generator must finish executing and raise `StopIteration`. If the generator encounters a second `yield` (for example, inside a loop), the wrapper receives an unexpected value instead of termination and raises `RuntimeError("generator didn't stop")`. Both assertions enforce symmetry, ensuring that resource acquisition and cleanup run exactly once.

Lifecycle violations in `@contextmanager` generators and their resolution:

```python
from contextlib import contextmanager


# 1. Pitfall: early return causes "generator didn't yield"
@contextmanager
def faulty_guard_manager(enabled=False):
    if not enabled:
        return  # BUG: returns before yield -> RuntimeError: generator didn't yield
    yield "ready"


# 2. Pitfall: multiple yields cause "generator didn't stop"
@contextmanager
def faulty_loop_manager():
    for item in ["first", "second"]:
        yield item  # BUG: second iteration -> RuntimeError: generator didn't stop


# 3. Correct pattern: exactly one yield wrapped in try/finally
@contextmanager
def correct_manager(enabled=True):
    resource = None
    try:
        resource = "connected" if enabled else "disabled"
        yield resource
    finally:
        # Cleanup executes deterministically on normal exit or exception
        resource = None


with correct_manager() as status:
    print(f"Status: {status}")  # Status: connected
```

**Common causes of contract violations:**
- early return guard clauses: if a resource cannot be initialized, raise an explicit exception rather than executing an early `return` before `yield`;
- placing `yield` inside `for` or `while` loops: a context manager generator must yield exactly one value during its entire lifetime;
- omitting `try...finally`: if an exception occurs within the `with` block and the post-yield code is not wrapped in `finally`, cleanup is bypassed entirely;
- accidental `yield from`: delegating to an iterable that produces multiple elements inevitably triggers the "generator didn't stop" failure.

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
