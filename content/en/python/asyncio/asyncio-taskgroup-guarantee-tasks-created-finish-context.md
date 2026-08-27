---
id: py-async-0009
title: "How does `asyncio.TaskGroup` guarantee that the Tasks created in it finish before the context manager exits?"
description: "How does `asyncio.TaskGroup` guarantee that the Tasks created in it finish before the context manager exits?"
track: python
section: asyncio
level: middle
type: mechanism
tags: [asyncio-taskgroup]
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

**`TaskGroup` is an asynchronous context manager whose `__aexit__` implicitly waits for all Tasks
created through `tg.create_task()` to finish, and does not exit the block until they do.**
[^py314-library-asyncio-task] Tasks can only be created inside the `async with` block. After the
block exits (normally or via an exception), `TaskGroup` waits for all its child Tasks to finish,
providing structured concurrency.

## Detailed explanation

`TaskGroup.__aexit__` does not simply exit the block – it runs internal logic that loops, waiting
until the set of tasks registered through `create_task()` becomes empty.
[^py314-library-asyncio-task] Every call to `tg.create_task(coro)` adds a `Task` to an internal
`set` and attaches a `done_callback` to it, which removes the Task from that set and, if it failed
with an exception, triggers cancellation of the rest of the group's tasks. So `__aexit__` does not
complete until the last callback has fired for every task – regardless of how many were created or
in what order they finished.

If one of the Tasks raises an exception (other than `CancelledError`), `TaskGroup` cancels all
other still-active Tasks in the group and waits for them to finish too (including handling the
`CancelledError` inside them), and only then raises an `ExceptionGroup` that bundles all collected
errors, even if only one Task failed. This is structured concurrency in practice: it is impossible
to exit the block while leaving orphaned tasks running unsupervised in the background – unlike a
"bare" `asyncio.create_task()` without a TaskGroup, where a forgotten Task can keep living even
after the function that created it has already returned.

`create_task()` can only be called inside the `async with` block itself; trying to add a new Task
after `__aexit__` has started (for example, from another task's callback) raises a `RuntimeError`,
because the group has already moved into its finishing state and no longer accepts new members.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
