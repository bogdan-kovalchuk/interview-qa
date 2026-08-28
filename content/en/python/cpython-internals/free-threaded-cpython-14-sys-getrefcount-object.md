---
id: py-cpyint-0015
title: "In free-threaded CPython 3.14, `sys.getrefcount()` for an object returns an unexpectedly large value: how does immortalization explain this, and why shouldn't that value be read as an exact reference count?"
description: "In free-threaded CPython 3.14, `sys.getrefcount()` for an object returns an unexpectedly large value: how does immortalization explain this, and why shouldn't that value be read as an exact reference count?"
track: python
section: cpython-internals
level: middle
type: practical
tags: [sys-getrefcount]
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  uk: 2
applies_to:
  - product: "CPython free-threaded build"
    version: "3.14"
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

**In a free-threaded build certain objects (code constants, interned strings) become immortal –
their refcount never changes and is set to a very large sentinel value, so `sys.getrefcount()`
returns exactly that, not a real count of references.**[^py314-library-dis] Immortalization removes
atomic refcount contention between threads: since the object will never be deallocated, there is no
need to update the counter. The documentation explicitly states that for immortal objects the
returned value does not reflect the actual number of references and should not be used for anything
except checking for 0 or 1.

## Detailed explanation

Immortalization is a CPython mechanism that marks specific objects as ones that will never be
deallocated: instead of ordinary reference counting, their `ob_refcnt` field is set to a fixed
sentinel value (a very large number, chosen so further inc/dec never overflow or zero it out), and
further incref/decref on such an object become a no-op.[^py314-howto-free-threading-python]

The idea appeared for the free-threaded build (PEP 703): without the GIL, every incref/decref would
have to be an atomic operation, and the hottest objects – `None`, `True`, `False`, small cached
ints, interned strings, code constants – are read and "held" from millions of places at once. By
making them immortal, the interpreter removes those atomic operations from the hot path instead of
trying to optimize them.[^py314-c-api-memory]

`sys.getrefcount(obj)` has no special case for immortal objects: it simply reads the same
`ob_refcnt` field and adds 1 for the temporary reference to `obj` during the call
itself.[^py314-library-sys] For an immortal object this field is not a counter but a sentinel
constant, so the returned number has nothing to do with the actual number of references and looks
unjustifiably large.

An example that shows the difference between a plain and an immortal object:

```python
import sys

class Plain:
    pass

obj = Plain()
print(sys.getrefcount(obj))     # small, real number of references

print(sys.getrefcount(None))    # huge sentinel value, not a real count
```

**Common mistakes:**
- reading the returned value as the exact number of `del`s needed to destroy the object;
- being surprised that the number does not decrease after removing local variables that referenced
  an immortal object;
- using `sys.getrefcount()` to diagnose memory leaks instead of `tracemalloc` or
  `gc.get_referrers()`;
- forgetting that since Python 3.12+ immortal objects include not just `None`/`True`/`False` but
  also small cached ints and some strings, so the behaviour differs from older versions.

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
