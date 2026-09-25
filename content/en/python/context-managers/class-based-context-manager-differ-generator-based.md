---
id: py-ctxmgr-0004
title: "How does a class-based context manager differ from a generator-based manager built with `@contextmanager`?"
description: "How does a class-based context manager differ from a generator-based manager built with `@contextmanager`?"
track: python
section: context-managers
level: middle
type: comparison
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

**A class-based context manager defines `__enter__` and `__exit__` as separate methods and easily maintains state in `self`; a generator-based manager uses a single generator function with `yield`, where code before `yield` is enter and code after is exit.**[^py314-reference-datamodel-with-statement-context-managers] The `@contextmanager` decorator eliminates boilerplate for simple use cases, but yields a "one-shot" object – reusing the same instance in another `with` statement raises a `RuntimeError`. A class-based approach is superior when reusability, reentrancy, or complex object lifecycle state is required.

## Detailed explanation

A class-based context manager directly implements the language protocol via `__enter__` and `__exit__` magic methods, whereas a generator-based manager uses the `@contextmanager` decorator from `contextlib` to adapt a generator function containing a single `yield` into a context manager object.[^py314-reference-datamodel-with-statement-context-managers][^py314-library-contextlib]

Under the hood, `@contextmanager` wraps the generator in a helper class called `_GeneratorContextManager`. Upon entering a `with` block, Python triggers `__enter__`, which calls `next(gen)` to execute statements up to the `yield` expression; whatever value is yielded becomes the target of the `as` clause. When exiting the block, `__exit__` invokes `next(gen)` to execute cleanup code following `yield` if no errors occurred, or invokes `gen.throw()` if an exception was raised, enabling developers to structure cleanup using standard `try...finally` syntax.

A major operational difference lies in lifecycle and reusability: generator-based managers are inherently "one-shot" objects. Because a generator cannot be rewound once exhausted, assigning the manager instance to a variable and passing it into a second `with` statement raises a `RuntimeError`. In contrast, a class-based manager maintains total control over instance state in `self` and can be engineered to be reusable or even reentrant by initializing or incrementing tracking state inside `__enter__`.

Comparison of class-based and generator-based context manager implementations:

```python
from contextlib import contextmanager


# 1. Generator-based manager: concise, one-shot
@contextmanager
def managed_resource_gen(name):
    print(f"Acquiring {name}")
    try:
        yield name
    finally:
        print(f"Releasing {name}")


# 2. Class-based manager: explicit protocol, reusable instance
class ManagedResourceClass:
    def __init__(self, name):
        self.name = name
        self.active = False

    def __enter__(self):
        print(f"Acquiring {self.name}")
        self.active = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.active = False
        print(f"Releasing {self.name}")
        return False  # Propagate any exception


with managed_resource_gen("connection-A") as conn:
    print(f"Using {conn}")

res = ManagedResourceClass("connection-B")
with res:
    print(f"Using {res.name}, active: {res.active}")
# Class-based instances can be reused if written to support it:
with res:
    print(f"Reused {res.name}, active: {res.active}")
```

**Decision criteria between the approaches:**
- generator-based is ideal for concise, linear workflows (temporary configuration toggles, lock acquisition, execution timing);
- class-based is essential when the manager must expose helper methods, attributes, or complex lifecycle state to the caller via the `as` target;
- exception suppression mechanics: in `@contextmanager`, catching an error around `yield` via `except` automatically suppresses it, whereas class-based managers require returning `True` from `__exit__`;
- performance characteristics: generator-based managers introduce minor overhead due to generator frame creation and suspension, whereas class methods have slightly lower latency in hot paths.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
