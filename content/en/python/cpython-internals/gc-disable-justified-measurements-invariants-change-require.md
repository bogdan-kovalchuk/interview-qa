---
id: py-cpyint-0011
title: "When can `gc.disable()` be justified, and what measurements and invariants does that change require beforehand?"
description: "When can `gc.disable()` be justified, and what measurements and invariants does that change require beforehand?"
track: python
section: cpython-internals
level: senior
type: practical
tags: [gc-disable]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/interpreter.md#L102-L197
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**`gc.disable()` is justified in latency-sensitive code where cyclic GC pauses are unacceptable,
provided that reference cycles are either absent or collected manually with `gc.collect()` at
predictable points.**[^py314-library-dis] After `gc.disable()`, reference counting keeps working:
objects without cycles are freed immediately. Before disabling it you need to measure a baseline:
the frequency and duration of automatic collections (`gc.get_threshold()`, `gc.get_count()`), the
list of cycle sources, and confirm the invariant – memory does not grow unbounded with manual
`gc.collect()` at fixed intervals.

## Detailed explanation

`gc.disable()` turns off only the cyclic collector – the three generations that periodically look
for reference cycles – not reference counting: objects without cycles are still freed immediately,
as soon as their refcount drops to zero.[^py314-library-gc]

The reason this can help: a cyclic GC pass stops the current thread for a pause whose length depends
on the number of tracked objects in the generation being checked. For latency-sensitive code (say, a
request handler where p99 matters), even a rare pause of a few milliseconds is noticeable in the
tail percentiles, while ordinary reference counting introduces no such delay.

The risk mirrors the benefit: if the code still creates reference cycles (parent<->child, closures
that capture `self`, retained tracebacks), they never free themselves, and memory grows unbounded
until someone calls `gc.collect()` manually.

Before disabling it, you should measure a baseline: `gc.get_stats()` and `gc.get_count()` show the
frequency and number of objects collected per generation, while an allocation profiler or
`objgraph` shows the actual sources of cycles in the code and its libraries. After disabling it you
need to keep an invariant: either cycles are guaranteed not to be created, or `gc.collect()` is
called manually at predictable, safe points (end of a request, worker idle time), and memory is then
watched in production, not only at code-review time.

A typical pattern:

```python
import gc

gc.disable()  # keep refcounting; stop only cyclic collection

def handle_request(request_count):
    ...
    if request_count % 1000 == 0:
        gc.collect()  # release accumulated cycles at a safe point
```

**Common mistakes:**
- disabling the GC without measuring a baseline, simply hoping things will improve;
- forgetting about cycles inside third-party libraries (an ORM, event-loop callbacks) that were
  previously cleaned up automatically;
- never calling `gc.collect()` manually, turning `disable()` into a slow memory leak;
- confusing `gc.disable()` with disabling reference counting – the latter cannot be disabled at all.

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
