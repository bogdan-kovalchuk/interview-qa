---
id: py-gil-0009
title: "What does the free-threaded build of CPython 3.14 mean, and how does it coexist with the GIL-enabled build?"
description: "What does the free-threaded build of CPython 3.14 mean, and how does it coexist with the GIL-enabled build?"
track: python
section: concurrency-and-gil
level: middle
type: comparison
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

**A free-threaded build is a separate CPython configuration (since Python 3.13) with the GIL
disabled, letting threads run with true parallelism across multiple CPU cores.**[^py314-library-threading]
It is not a runtime switch but a separate build (`configure --disable-gil`). Detected through
`sys._is_gil_enabled()` (returns `False`) or the string "free-threading build" in `sys.version`.
Uses mimalloc instead of pymalloc, and biased reference counting; single-threaded overhead is about
1-8%.

## Detailed explanation

A free-threaded build is a separate CPython configuration, built with the `--disable-gil` flag, in
which the global interpreter lock is disabled at the interpreter level itself, not merely unused by
a particular piece of code.[^py314-howto-free-threading-python]

This configuration does not replace the GIL-enabled build; it exists alongside it. Both are built
from the same CPython source tree but are distributed as separate binary packages with a different
ABI tag (for example `cp314` for the regular build and `cp314t` for the free-threaded one, where `t`
stands for threading). The package installer picks the wheel matching the interpreter's tag; a C
extension built against the regular ABI is not compatible with the free-threaded build and needs a
separate build.[^py314-howto-free-threading-extensions]

You can tell which build you are running on in two ways:

```python
import sys

print(sys.version)            # contains "free-threading build" on that build
print(sys._is_gil_enabled())  # False on free-threaded build, unless re-enabled
```

`sys._is_gil_enabled()` can still return `True` on a free-threaded build if the GIL was explicitly
re-enabled (`PYTHON_GIL=1`) or automatically turned back on because of an incompatible C extension.

The free-threaded build also changes the internal memory model: it uses the mimalloc allocator
instead of pymalloc, and reference counting becomes biased - each object keeps separate fields for
its owning thread's counter and for a shared counter, which avoids atomic operations on the fast
path when only one thread touches the object. The cost is a single-threaded overhead of roughly
1-8% compared to the regular build.

**What to weigh when choosing it:**
- the library ecosystem, especially C extensions, is not yet fully compatible with the free-threaded
  ABI;
- it needs a separate deployment - the matching wheel tag, not just a runtime flag;
- the payoff only shows up for CPU-bound code running on multiple threads; for I/O-bound workloads
  the difference is minimal.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
