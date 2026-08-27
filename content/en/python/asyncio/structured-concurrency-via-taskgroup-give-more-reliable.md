---
id: py-async-0011
title: "When does structured concurrency via `TaskGroup` give more reliable lifetime and failure semantics than a loose set of `create_task()` calls?"
description: "When does structured concurrency via `TaskGroup` give more reliable lifetime and failure semantics than a loose set of `create_task()` calls?"
track: python
section: asyncio
level: senior
type: comparison
tags: [taskgroup, create-task]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/async.md#L746-L791
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**`TaskGroup` guarantees that when any task fails, all sibling tasks are cancelled and exceptions
are collected into an `ExceptionGroup` – whereas a loose set of `create_task()` calls requires
manual tracking and can leave a task unsupervised.**[^py314-library-asyncio-task] Exiting
`async with TaskGroup()` implicitly awaits every task; if one of them failed with an exception
(other than `CancelledError`), the rest are cancelled, no new tasks are accepted, and once all of
them finish it raises an `ExceptionGroup`. This eliminates the classic mistake of a "forgotten" task
that fails silently.

## Detailed explanation

The core idea of structured concurrency is that no asynchronous operation should outlive the scope
it was started in. `TaskGroup` implements this literally: exiting `async with TaskGroup()` is
impossible until every Task created inside it via `tg.create_task()` has finished, so the function
containing that block physically cannot return while leaving behind work that is still
running.[^py314-library-asyncio-task] Each Task's lifetime is tightly bound to the lifetime of the
block it was born in.

A bare set of `create_task()` calls gives no such guarantee at all. A function can create several
Tasks and return right away without waiting on any of them – they keep running, tied only to the
loop, not to any visible scope in the code. If the caller of that function did not keep a reference
to those Tasks, it does not even know they exist, and the further fate of those Tasks is a separate
story: if one fails with an exception, nobody finds out until someone explicitly reads its result.

The second difference is the direction cancellation propagates. If the outer coroutine containing
`async with TaskGroup()` is cancelled, the group intercepts that `CancelledError` and cascades
cancellation to all of its children before letting the cancellation continue propagating further.
Bare Tasks created via `create_task()` with no group have no such binding: cancelling the coroutine
that spawned them does not automatically cancel the orphaned Tasks in any way – they simply keep
running on their own, detached from the logic that created them.

So "reliability" here is not about performance or API surface, but about whether, looking at the
boundaries of one block of code, you can say for certain what concurrent work is still in flight.
With `TaskGroup` the answer is always unambiguous: everything inside the block has either already
finished, or is guaranteed to finish (successfully or via cancellation) before the block exits.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
