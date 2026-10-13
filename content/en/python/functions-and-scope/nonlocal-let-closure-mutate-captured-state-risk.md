---
id: py-funcs-0018
title: "How does `nonlocal` let a closure mutate captured state, and what risk does that create under concurrent calls?"
description: "How does `nonlocal` let a closure mutate captured state, and what risk does that create under concurrent calls?"
track: python
section: functions-and-scope
level: senior
type: practical
tags: [nonlocal]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  uk: 2
applies_to:
  - product: "CPython with GIL"
    version: null
anki:
  export: true
sources:
  - source_id: py314-reference-simple-stmts-the-nonlocal-statement
    title: "Python 3.14: Reference/simple Stmts"
    url: https://docs.python.org/3.14/reference/simple_stmts.html#the-nonlocal-statement
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation, section The nonlocal statement: nonlocal binds the name to the nearest enclosing scope where it is already bound."
  - source_id: py314-reference-executionmodel-resolution-of-names
    title: "Python 3.14: Reference/executionmodel"
    url: https://docs.python.org/3.14/reference/executionmodel.html#resolution-of-names
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation, section Resolution of names: a name used in a block but not defined there is a free variable."
  - source_id: py314-faq-library-what-kinds-of-global-value-mutation-are-thread-safe
    title: "Python 3.14: Faq/library"
    url: https://docs.python.org/3.14/faq/library.html#what-kinds-of-global-value-mutation-are-thread-safe
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation, FAQ: Python switches threads only between bytecode instructions, and i = i + 1 is not an atomic operation."
  - source_id: py314-library-threading-lock-objects
    title: "Python 3.14: Library/threading"
    url: https://docs.python.org/3.14/library/threading.html#lock-objects
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation, section Lock objects: acquire() blocks until another thread calls release(); a lock supports the context management protocol."
---

## Short answer

**`nonlocal` lets a closure rebind a variable in the enclosing function scope, which turns it into shared mutable state across all calls of the closure.**[^py314-reference-simple-stmts-the-nonlocal-statement] In single-threaded code this is the standard stateful-closure pattern (a counter, a cache). <span class="warn">In multithreaded code on CPython with the GIL, updating shared state with a read-modify-write (for example `count += 1`) is not atomic: a thread can be interrupted between the read and the write, which causes a race condition.</span>[^py314-faq-library-what-kinds-of-global-value-mutation-are-thread-safe] Synchronization is needed, for example a `threading.Lock`.[^py314-library-threading-lock-objects]

## Detailed explanation

`nonlocal` binds the name to the nearest enclosing scope where it is already bound, so an assignment changes that variable instead of creating a local one.[^py314-reference-simple-stmts-the-nonlocal-statement] A name that is used in a block but not defined there is a free variable.[^py314-reference-executionmodel-resolution-of-names] Closures from one factory call see the same cell, so the state accumulates.

The danger is that `count += 1` is a read, an add and a write. Python switches threads only between bytecode instructions, so a switch can happen between the read and the write. The FAQ explicitly lists `i = i + 1` as not atomic.[^py314-faq-library-what-kinds-of-global-value-mutation-are-thread-safe]

In a test on CPython 3.14, `count += 1` with no call inside did not lose updates, but a Python function call on the right-hand side did. This does not make the bare form safe: the lack of lost updates is an implementation detail of the current interpreter, not a guarantee; the FAQ lists `i = i + 1` as not atomic.[^py314-faq-library-what-kinds-of-global-value-mutation-are-thread-safe] Example:

```python
def price(item):
    return item                       # illustrative: any Python-level call

def make_total():
    total = 0

    def add(item):
        nonlocal total
        total = total + price(item)   # read total, call price(), then store total
        return total

    return add
```

Four threads making 50 000 calls each to `add(1)` (with `sys.setswitchinterval(1e-6)`) gave 151 605 and 140 043 instead of 200 000. One correct run proves nothing.

The fix is a `threading.Lock`. A thread calling `acquire()` on a locked lock blocks until another thread calls `release()`; `with lock:` does both steps.[^py314-library-threading-lock-objects] The call to `price(item)` is moved out of the lock:

```python
import threading

# price() is defined in the previous example
def make_safe_total():
    total = 0
    lock = threading.Lock()

    def add(item):
        nonlocal total
        value = price(item)           # outside the critical section
        with lock:
            total = total + value     # read and store inside one critical section
        return total

    return add
```

**Common mistakes:**
- assuming that a single-threaded test proves a `nonlocal` closure is safe;
- reading `total` outside the lock and writing it inside: an update can still be lost;
- assuming that the GIL makes `count += 1` atomic.

## Environment

TODO

## Deliverable

TODO

## Acceptance criteria

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
