---
id: py-cpyint-0005
title: "Why can a retained traceback in CPython keep frames and their local objects alive after the function has finished?"
description: "Why can a retained traceback in CPython keep frames and their local objects alive after the function has finished?"
track: python
section: cpython-internals
level: middle
type: mechanism
tags: []
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

**A traceback object holds `tb_frame`, which points to a frame object, and `frame.f_locals` may
hold the exception object – forming a cycle: frame -> locals -> exception -> __traceback__ ->
traceback -> frame.**[^py314-library-dis] This cycle prevents reference counting from freeing the
objects, so the frames and their local variables stay in memory even after the function has
returned. The cyclic GC will eventually clear the cycle, or it can be broken explicitly with
`frame.clear()`.

## Detailed explanation

A traceback object holds `tb_frame` – a reference to the frame in which the exception occurred –
and that frame, through `f_locals`, holds references to every local variable of that call, possibly
including the exception object itself.

If the exception object is saved somewhere – say, in a list of logs, in a variable outside the
`except` block, or simply via `sys.exc_info()` – and it in turn has a `__traceback__` attribute
pointing back at the traceback, a cycle forms: `frame -> f_locals -> exception -> __traceback__ ->
traceback -> tb_frame -> frame`.[^py314-reference-datamodel-traceback-objects]

Until the cyclic garbage collector clears this cycle, every frame in the chain – not just the one
where the except happened, but every "parent" frame up the call stack – and all their local
variables stay alive, even though the corresponding functions returned long ago. In practice this
can keep large objects alive (a connection handle, a large buffer) simply because they happened to
be a local variable somewhere on the stack at the moment of the exception.

This is exactly why, since Python 3.0, CPython automatically deletes the variable bound by
`except ... as e:` at the end of the except block – it breaks one of the most common sources of this
cycle, where the handler itself holds `e` longer than necessary.

```python
try:
    raise ValueError("boom")
except ValueError as exc:
    saved = exc  # keeps exc.__traceback__ -> frame -> f_locals -> exc alive

# saved now holds a reference cycle through its own __traceback__
```

**Common mistakes:**
- saving an exception (`sys.exc_info()`, `logging.exception`, a custom error list) without realizing
  this extends the lifetime of the whole frame stack;
- assuming `except Exception as e: ...` is always safe, ignoring the case where `e` is explicitly
  copied into an outer variable;
- being surprised that memory is not freed right after a handled exception, instead of checking for
  reference cycles with `gc`.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
