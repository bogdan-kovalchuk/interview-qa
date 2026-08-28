---
id: py-cpyint-0019
title: "How does comparing `tracemalloc` snapshots help find the source locations of growing allocations?"
description: "How does comparing `tracemalloc` snapshots help find the source locations of growing allocations?"
track: python
section: cpython-internals
level: middle
type: practical
tags: [tracemalloc]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/interpreter.md#L334-L381
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**`Snapshot.compare_to(old_snapshot, key_type)` computes the difference (`size_diff`, `count_diff`)
between two snapshots, grouped by filename, lineno, or traceback, and sorts by absolute
`size_diff`.**[^py314-library-dis] Typical workflow: `tracemalloc.start()` -> take a first snapshot
at a checkpoint -> run the suspect code -> take a second snapshot -> `current.compare_to(prev,
'lineno')` returns a `StatisticDiff` list where the top rows are the source locations with the
biggest growth. `key_type='traceback'` gives full call stacks for more precise diagnosis, but
requires `nframe > 1` in `tracemalloc.start()`.

## Detailed explanation

`tracemalloc` is a built-in module that records where (the source location) each memory allocation
for Python objects was made, and lets you compare those records between two points in time.[^py314-library-tracemalloc]

The `Snapshot.compare_to(old_snapshot, key_type)` method compares the current snapshot with a
previous one and returns a list of `StatisticDiff` entries, where each entry has `size`,
`size_diff`, `count`, and `count_diff` fields – the absolute value and the change relative to the
old snapshot. The `key_type` parameter sets the grouping level: `'filename'` groups by file,
`'lineno'` by a specific line, and `'traceback'` by the full allocation call stack. The list is
always sorted by descending absolute `size_diff`, so the top entries are the locations with the
biggest growth.

The typical workflow is to take a snapshot before the suspect code, run that code, take a second
snapshot, and compare them; that way you see only the change, not the whole baseline of process
allocations.

An example of comparing two snapshots by source line:

```python
tracemalloc.start()
snapshot1 = tracemalloc.take_snapshot()
run_suspect_code()
snapshot2 = tracemalloc.take_snapshot()

diff = snapshot2.compare_to(snapshot1, 'lineno')
for stat in diff[:3]:
    print(stat)  # top growth: <file>:<line>: size=..., count=...
```

To get `key_type='traceback'` with the full call stack rather than just the last line, you must
call `tracemalloc.start(nframe)` with `nframe > 1` before the first snapshot – the number of stored
frames is fixed at start time and cannot be changed retroactively.

**Common mistakes when working with tracemalloc:**
- comparing snapshots from different processes or interpreter restarts – addresses and line
  numbers may not correspond to each other;
- forgetting to call `tracemalloc.start(nframe)` with the needed `nframe` before the first
  snapshot, when `key_type='traceback'` is required;
- interpreting `count_diff` without `size_diff` – many small allocations can weigh less than a few
  large ones.

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
