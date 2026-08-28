---
id: py-gil-0010
title: "Which thread-safety assumptions about shared mutable objects need to be revisited when moving to free-threaded CPython?"
description: "Which thread-safety assumptions about shared mutable objects need to be revisited when moving to free-threaded CPython?"
track: python
section: concurrency-and-gil
level: senior
type: practical
tags: []
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
  - source_id: py314-library-threading
    title: "Python 3.14: Library/threading"
    url: https://docs.python.org/3.14/library/threading.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-multiprocessing
    title: "Python 3.14: Library/multiprocessing"
    url: https://docs.python.org/3.14/library/multiprocessing.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-concurrent-futures
    title: "Python 3.14: Library/concurrent.futures"
    url: https://docs.python.org/3.14/library/concurrent.futures.html
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
  - source_id: py314-howto-free-threading-extensions
    title: "Python 3.14: Howto/free Threading Extensions"
    url: https://docs.python.org/3.14/howto/free-threading-extensions.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/gil_threads_processes.md#L689-L849
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**In a free-threaded build, several threads execute bytecode at the same time, so every access to
shared mutable state needs explicit synchronization – internal locking of built-in types is an
implementation detail, not an API contract.**[^py314-library-threading] Iterators over shared
collections are not thread-safe (elements can be skipped or duplicated). Accessing `frame.f_locals`
from another thread can crash the interpreter. In C extensions, borrowed references (for example,
`PyList_GET_ITEM`) are unsafe – migration to the strong-reference API (`PyList_GetItemRef`,
`PyDict_GetItemRef`) is needed.

## Detailed explanation

Free-threaded CPython (a build without the GIL) is a mode where several threads of one process can
execute Python bytecode literally at the same time on different cores, instead of taking turns as in
a GIL-enabled build.[^py314-howto-free-threading-python]

In regular CPython, the GIL incidentally, but usually reliably, protected individual operations on
built-in types from being interrupted mid-way: for example, `list.append()` looked atomic not
because that is an API guarantee, but because the GIL did not let another thread interfere. On a
free-threaded build that assumption no longer holds – the internal locks of built-in types exist to
avoid corrupting the object's own structure, not to make a sequence of operations atomic at the
application level.[^py314-howto-free-threading-python]

This means any access to shared mutable state – a dict, a list, a set, an object's attributes –
without an explicit `Lock` is now genuinely dangerous, not just theoretically so. Iterating over a
shared collection that another thread mutates in parallel can skip elements, repeat them, or raise
an exception.

An example of code that used to "accidentally work" under the GIL but does not on a free-threaded
build:

```python
shared = {}

def writer():
    for i in range(1000):
        shared[i] = i  # mutating a dict from multiple threads without a lock

def reader():
    for key in shared:  # iterating while another thread mutates - unsafe here
        ...
```

A separate danger is C extensions written under GIL assumptions. Patterns like borrowed references
(`PyList_GET_ITEM`) are no longer safe, because the owner of the object may release it from another
thread; migration to the strong-reference API such as `PyList_GetItemRef` and `PyDict_GetItemRef` is
needed.[^py314-howto-free-threading-extensions]

**What to revisit when moving to a free-threaded build:**
- any shared mutable state without an explicit `Lock` or another synchronization primitive;
- iterating over shared collections in one thread while another mutates them;
- accessing `frame.f_locals` from a foreign thread – it can crash the interpreter;
- C extensions that rely on borrowed references to built-in types.

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
