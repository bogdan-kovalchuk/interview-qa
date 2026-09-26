---
id: py-cpyint-0014
title: "Why shouldn't `__del__` be used as the primary mechanism for the timely release of external resources?"
description: "Why shouldn't `__del__` be used as the primary mechanism for the timely release of external resources?"
track: python
section: cpython-internals
level: senior
type: pitfall
tags: [del]
status: published
updated: 2026-09-27
content_revision: 2
reconciled_with:
  uk: 2
applies_to:
  - product: "CPython"
    version: null
anki:
  export: true
sources:
  - source_id: py314-library-dis
    title: "Python 3.14: Library/dis"
    url: https://docs.python.org/3.14/library/dis.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-gc
    title: "Python 3.14: Library/gc"
    url: https://docs.python.org/3.14/library/gc.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-c-api-memory
    title: "Python 3.14: C Api/memory"
    url: https://docs.python.org/3.14/c-api/memory.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-sys
    title: "Python 3.14: Library/sys"
    url: https://docs.python.org/3.14/library/sys.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-tracemalloc
    title: "Python 3.14: Library/tracemalloc"
    url: https://docs.python.org/3.14/library/tracemalloc.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-howto-free-threading-python
    title: "Python 3.14: Howto/free Threading Python"
    url: https://docs.python.org/3.14/howto/free-threading-python.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-reference-datamodel-traceback-objects
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#traceback-objects
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
---

## Short answer

**`__del__` guarantees neither prompt execution nor that it will run at all: it can be delayed by cyclic GC, skipped during interpreter shutdown, and exceptions within it are ignored.**[^py314-library-dis] Key risks: (1) in reference cycles, `__del__` is deferred until cyclic GC collection; (2) during interpreter shutdown, global variables may already be `None`; (3) invocation from an arbitrary thread risks deadlocks when acquiring locks. For timely release, use a context manager (`with`) or `weakref.finalize`.

## Detailed explanation

The `__del__` method in Python acts as an asynchronous finalizer rather than a deterministic destructor (unlike C++ RAII), offering no guarantee of timely release for scarce system resources such as file descriptors, sockets, or database connections.[^py314-library-gc] CPython primarily relies on reference counting: `__del__` runs immediately only when an object's reference counter drops to zero. However, when an object becomes involved in a reference cycle – easily introduced via callbacks, closures, or back-references – its reference count never reaches zero upon exiting local scope. Reclaiming cyclic garbage is deferred until the cyclic garbage collector (`gc.collect()`) runs, which risks exhausting operating system quotas long before memory reclamation triggers.

Finalizers face severe operational hazards during interpreter shutdown (`sys.exit()`, process termination, or unhandled errors). As the runtime tears down module namespaces, global variables and module attributes are progressively set to `None`, causing cleanup logic inside `__del__` that references external modules or helpers to fail unpredictably with `AttributeError` or `TypeError`.[^py314-library-sys] Furthermore, exceptions raised inside `__del__` are uncatchable by user `try...except` blocks; CPython merely outputs a warning to `sys.stderr` and continues execution, silently swallowing cleanup errors.

In professional architecture, deterministic resource management must always rely on context managers (`with` or `async with`) and explicit `.close()` protocols. When an automatic safety net is required for forgotten cleanup, modern Python relies on `weakref.finalize`, which binds cleanup callbacks via weak references without preventing cyclic garbage collection and executes reliably during process shutdown.

Demonstration of how a reference cycle delays `__del__` execution beyond scope exit:

```python
import gc

class BadResource:
    def __init__(self, name: str):
        self.name = name
        self.other = None

    def __del__(self):
        print(f"__del__ executed for {self.name}")

def create_cycle():
    a = BadResource("A")
    b = BadResource("B")
    a.other = b
    b.other = a
    # a and b go out of scope here, but refcounts remain 1 due to the cycle
    print("Scope exited, but finalizers have not run yet.")

create_cycle()
# Both resources are leaked until explicit or threshold cyclic GC runs
print("Triggering manual GC collection:")
gc.collect()

# Output:
# Scope exited, but finalizers have not run yet.
# Triggering manual GC collection:
# __del__ executed for A
# __del__ executed for B
```

**Architectural risks and common mistakes with `__del__`:**
- relying on `__del__` instead of context managers: scarce external handles (file descriptors, sockets) exhaust operating system quotas before garbage collection triggers;
- deadlocks in multi-threaded programs: `__del__` can run on an arbitrary thread during memory allocations, creating lock inversion risks;
- object resurrection: inadvertently binding `self` to an external reference inside `__del__` revives the dead object in an inconsistent state.

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
