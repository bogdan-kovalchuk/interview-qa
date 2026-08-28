---
id: py-cpyint-0016
title: "When can `gc.freeze()` reduce copy-on-write losses before `fork()`, and what conditions does this pattern need?"
description: "When can `gc.freeze()` reduce copy-on-write losses before `fork()`, and what conditions does this pattern need?"
track: python
section: cpython-internals
level: senior
type: practical
tags: [gc-freeze, fork]
status: published
updated: 2026-09-05
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

**`gc.freeze()` moves all objects currently tracked by the GC into the permanent generation, where
later collections ignore them – this prevents modifying the `gc_refs` field of long-lived objects in
the child after `fork()`, reducing copy-on-write.**[^py314-library-dis] Recommended workflow: (1)
`gc.disable()` at the start of the parent; (2) `gc.freeze()` right before `fork()`; (3)
`gc.enable()` at the start of the child. Conditions: the frozen objects must be genuinely long-lived
and immutable; the child must not modify these objects, or CoW happens anyway. The pattern is
effective for pre-fork web workers (gunicorn, uwsgi).

## Detailed explanation

`gc.freeze()` takes every object the cyclic collector currently tracks and moves it into the
permanent generation – a group that later `gc.collect()` calls no longer check or touch.[^py314-library-gc]

Without freeze, every cyclic GC pass physically writes a bookkeeping field (an internal counter for
the trial-deletion algorithm) into each tracked object to compute reachability. Even if the object
did not change from the Python code's point of view, that bookkeeping write at the C level "dirties"
the memory page. After `fork()`, such a page stops being shared between parent and child and gets
copied – a copy-on-write happens even though the data itself never actually changed.[^py314-c-api-memory]

A typical workflow: the parent process (say, gunicorn's or uwsgi's pre-fork model) loads long-lived
data – configs, ORM models, caches – calls `gc.freeze()` right before `fork()`, and each child can
call `gc.enable()` right after starting, if the GC was disabled in the parent for stability before
the freeze. No cyclic collector visits the frozen objects afterward, so their pages stay shared with
the parent.

Conditions under which the pattern actually pays off: the frozen objects must be genuinely long-lived
and essentially immutable; if the child modifies them at the Python level (not just through a GC
pass), CoW happens anyway – freeze only protects against writes caused by the collector itself, not
against mutations from code. Objects created after `fork()` in each child are not part of the
permanent generation and are tracked separately.

```python
import gc
import os

load_shared_data()   # populate long-lived objects
gc.freeze()           # move them out of future collections
pid = os.fork()
if pid == 0:
    serve_requests()   # child; frozen objects' pages stay shared
```

**Common mistakes:**
- calling `gc.freeze()` before all long-lived data has been loaded – new objects stay tracked and
  writable;
- expecting freeze to protect against Python-level mutations too – it only removes GC-caused writes;
- forgetting about `gc.unfreeze()` or monitoring `gc.get_freeze_count()` once the pattern is no
  longer needed, accumulating a permanent generation nobody ever collects.

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
