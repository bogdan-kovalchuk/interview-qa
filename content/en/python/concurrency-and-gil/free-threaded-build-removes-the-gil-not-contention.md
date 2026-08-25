---
id: py-gil-0001
title: "Why does the free-threaded build not make every Python program faster?"
description: "Removing the GIL removes one global lock, not the coordination that shared mutable state still needs."
track: python
section: concurrency-and-gil
level: middle
type: mechanism
tags: [gil, free-threading, threads, scaling]
status: published
updated: 2026-09-03
content_revision: 2
reconciled_with:
  uk: 3
see_also: [cs-cmplx-0001]
applies_to:
  - product: CPython free-threaded build
    version: "3.14"
  - product: CPython with GIL
    version: "3.14"
anki:
  export: true
sources:
  - source_id: py314-free-threading-howto
    title: "Python support for free threading"
    url: https://docs.python.org/3.14/howto/free-threading-python.html
    accessed: 2026-09-03
    kind: official
    version: "3.14"
    applicability: "The free-threaded CPython build; does not describe other implementations."
  - source_id: py314-free-threading-extensions
    title: "C API extension support for free threading"
    url: https://docs.python.org/3.14/howto/free-threading-extensions.html
    accessed: 2026-09-03
    kind: official
    version: "3.14"
    applicability: "Opt-in requirements for C extension modules under the free-threaded build."
  - source_id: pep-779
    title: "PEP 779: Criteria for supported status for free-threaded Python"
    url: https://peps.python.org/pep-0779/
    accessed: 2026-09-03
    kind: spec
    version: null
    applicability: "The support status of the free-threaded build from CPython 3.14 onwards."
  - source_id: pep-703
    title: "PEP 703: Making the Global Interpreter Lock Optional in CPython"
    url: https://peps.python.org/pep-0703/
    accessed: 2026-09-03
    kind: spec
    version: null
    applicability: "Design rationale and the runtime mechanisms that replace the GIL."
---

## Short answer

**The GIL was one bottleneck, not the only one.** Removing it lets CPython bytecode run on several
cores at once, but the runtime replaces it with per-object locking and a more elaborate reference
counting scheme, and that machinery is not free.[^pep-703] Code that was already I/O bound gained
nothing, code that shares mutable state now pays for finer-grained synchronisation, and every C
extension has to opt in before it may run without the GIL.[^py314-free-threading-extensions] The
speed-up is real for CPU-bound work over mostly independent data, and close to zero elsewhere.

## Detailed explanation

The free-threaded build ships as a separate interpreter configuration. It was experimental in 3.13 and
is officially supported from 3.14 on, but it is still not the default build, so a program only runs
without the GIL if it was deliberately started on that interpreter.[^pep-779]

What the GIL actually provided was a single, extremely cheap mutual exclusion over the whole
interpreter. Reference count updates, dictionary mutation and list resizing were safe because only one
thread ever executed bytecode. Removing the lock means each of those has to be made safe on its own:
CPython uses biased and deferred reference counting so that the common case of an object touched by
one thread stays cheap, and per-object locks for containers.[^pep-703] Uncontended, that is a modest
constant overhead on every operation; contended, it is a real lock, with the cache line ping-pong that
any shared counter causes.

This is why the shape of the workload decides the outcome:

- CPU-bound work over data that threads do not share scales close to linearly, and this is the case
  the build was designed for.
- I/O-bound work already released the GIL around blocking calls, so it was never limited by it and
  gains nothing measurable.
- Work that hammers a shared dictionary, counter or queue moves the contention from the GIL to that
  object, and can end up slower than the GIL build, because a single global lock is cheaper than many
  contended small ones.
- Work bound by memory bandwidth or by the allocator does not scale with cores regardless of locking.

Single-threaded programs pay a residual cost as well: the supported 3.14 build is measurably slower on
single-threaded benchmarks than the default build, which is one of the reasons free threading is not
the default.[^pep-779]

The last constraint is ecosystem-wide rather than technical. An extension module must declare that it
supports running without the GIL; when a module that has not declared it is imported, the interpreter
re-enables the GIL for the whole process unless the operator has forced it off.[^py314-free-threading-extensions]
A single unmarked dependency therefore silently returns the program to the old execution model, and
measuring is the only way to notice.

## Evaluation guide

### Expected signals

- Names what replaced the GIL rather than saying the lock was simply deleted: per-object locks plus
  biased or deferred reference counting.
- Distinguishes CPU-bound-and-independent work from I/O-bound and from shared-state work, and predicts
  a different result for each.
- Knows the free-threaded interpreter is a separate build that has to be chosen.
- Mentions that C extensions must opt in, and that an unmarked one can re-enable the GIL at runtime.

### Red flags

- "The GIL is gone, so threads are now as fast as processes" with no mention of contention.
- Believes 3.14 removed the GIL from the default interpreter.
- Proposes threads for a workload that is bound by disk or network and expects a speed-up.

### Level-up follow-up

Ask how they would decide between the free-threaded build, `multiprocessing` and `asyncio` for a
specific service, and what they would measure before committing. A senior answer starts from the
profile, not from the feature.

Then ask what happens to a program that relies on a dictionary update being atomic because of the
GIL, once it runs on the free-threaded build.

## Sources

<!-- generated from frontmatter -->
