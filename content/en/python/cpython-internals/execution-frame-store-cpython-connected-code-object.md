---
id: py-cpyint-0002
title: "What does an execution frame store in CPython, and how is it connected to the code object and the call stack?"
description: "What does an execution frame store in CPython, and how is it connected to the code object and the call stack?"
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
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/interpreter.md#L242-L269
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**A frame object stores a reference to the code object (`f_code`), the globals (`f_globals`) and
locals (`f_locals`) dictionaries, and a pointer to the previous frame (`f_back`), forming a linked
list – the call stack.**[^py314-library-dis] Each function or method call creates a new frame.
Through `f_lasti`, the frame records the current execution position within the bytecode. The frame
is also accessible via traceback objects and trace functions.

## Detailed explanation

An execution frame (`frame object`) is a data structure that CPython creates for every function or
method call, to hold the entire execution state of that specific call separately from the code
being executed.[^py314-reference-datamodel-traceback-objects]

A frame holds a reference to the `code object` it is executing (`f_code`) – this is what ties the
frame to the specific bytecode, `co_consts`, and `co_varnames`. Separately, the frame stores two
dictionaries: `f_globals` – the namespace of the module the function is defined in, and `f_locals` –
the local variables of this call. The `f_lasti` field records the offset of the last executed
bytecode instruction – this is exactly how a traceback knows which line an exception happened on.

Every function call creates a new frame, and the `f_back` field points to the frame the call was
made from. This `f_back` chain is the call stack: to walk it from the current call to `__main__`,
it's enough to iterate over `f_back` until it becomes `None`. Traceback objects and functions such
as `sys._getframe()` or `traceback.extract_stack()` do exactly that.[^py314-library-sys]

```python
import sys

def inner():
    frame = sys._getframe()
    print(frame.f_code.co_name)  # inner
    print(frame.f_back.f_code.co_name)  # outer

def outer():
    inner()

outer()
```

**Common mistakes when working with frame objects:**
- holding a reference to a frame longer than the call lasts – this prevents freeing all of that
  call's local variables for as long as the frame stays alive;
- storing an exception's traceback (and with it the chain of frames) in a variable outside the
  `except` block without an explicit `del`, creating a reference cycle;
- confusing `f_locals` with an ordinary, always-synchronized dictionary – for functions (unlike
  module/class scope) it is a snapshot that does not always reflect live variable changes.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
