---
id: py-async-0012
title: "How does `asyncio.gather()` preserve the ordering of results when the awaitables finish in a different order?"
description: "How does `asyncio.gather()` preserve the ordering of results when the awaitables finish in a different order?"
track: python
section: asyncio
level: middle
type: mechanism
tags: [asyncio-gather]
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-library-asyncio-task
    title: "Python 3.14: Library/asyncio Task"
    url: https://docs.python.org/3.14/library/asyncio-task.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-asyncio-eventloop
    title: "Python 3.14: Library/asyncio Eventloop"
    url: https://docs.python.org/3.14/library/asyncio-eventloop.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-asyncio-dev
    title: "Python 3.14: Library/asyncio Dev"
    url: https://docs.python.org/3.14/library/asyncio-dev.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/async.md#L792-L832
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**`gather()` returns the list of results in the same order as the input awaitables, regardless of
the order in which they actually finish.**[^py314-library-asyncio-task] Each awaitable corresponds
to a position in the result list by its input index. For example, if `gather(slow(), fast())` is
called and `fast()` finishes first, the result is still `[result_slow, result_fast]`.

## Detailed explanation

`gather()` does not await the awaitables sequentially and does not sort the results by completion
time – it immediately wraps each input awaitable in its own `Task` (or a `Future` wrapper, if it is
already a Future) and keeps an ordered list of these objects by argument position.
[^py314-library-asyncio-task] When a particular Task finishes, its callback writes the result into
the result list at the same index the Task was added at, not at the moment it finished. The event
loop itself schedules coroutines cooperatively: every `await` inside them is a point where control
returns to the loop, and it is the loop that decides which task gets CPU time next; the order in
which steps run can be arbitrary, but the array of indices is fixed the moment `gather()` is
called.

This is what fundamentally separates `gather()` from `asyncio.as_completed()`, which instead yields
awaitables in the order they actually finish rather than the input order – the choice between them
depends on whether the caller needs the results in order or needs to react to the first ready
result as fast as possible.

By default `return_exceptions=False`: if one of the awaitables raises an exception, `gather()`
immediately raises it to the caller, but the remaining Tasks are not cancelled automatically and
keep running in the background – this is a common source of bugs where forgotten Tasks later log
exceptions as `Task exception was never retrieved`. With `return_exceptions=True` the exception
itself becomes the value in the result list at its position, and the caller gets the full list
without an early break on the first failure.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
