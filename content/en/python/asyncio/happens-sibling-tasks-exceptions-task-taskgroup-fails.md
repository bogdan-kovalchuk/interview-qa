---
id: py-async-0010
title: "What happens to sibling Tasks and their exceptions when one Task in a `TaskGroup` fails?"
description: "What happens to sibling Tasks and their exceptions when one Task in a `TaskGroup` fails?"
track: python
section: asyncio
level: middle
type: mechanism
tags: [taskgroup]
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

**If any Task in a `TaskGroup` finishes with an exception (other than `CancelledError`), all
sibling Tasks are cancelled, and all exceptions are aggregated into an `ExceptionGroup`, which is
raised when the context manager exits.**[^py314-library-asyncio-task] New Tasks cannot be added
after the first failure. `KeyboardInterrupt` and `SystemExit` are raised immediately without
aggregation. If the body of the `async with` block itself raises an exception, it is also included
in the final `ExceptionGroup`.

## Detailed explanation

The sequence of events inside a `TaskGroup` is fixed. As soon as the first child Task fails with a
"real" exception (not `CancelledError`), the group moves into an "aborting" state and immediately
calls `.cancel()` on every sibling Task that has not finished yet.[^py314-library-asyncio-task]
After that, `__aexit__` waits for absolutely all children to actually finish – both the cancelled
ones and the one that failed first – before deciding what to raise next.

Importantly, cancelling the siblings does not guarantee a "quiet" finish: a Task that was cancelled
can catch `CancelledError` in a `try/except` and, instead of re-raising it, raise something else
during cleanup. That "second" exception is also included in the final `ExceptionGroup`, so the set
of collected exceptions can end up larger than one. The `CancelledError` that arises in a sibling
purely as a result of the group's own cancellation, on the other hand, is not added to the
`ExceptionGroup` – that is an expected outcome, not a failure.

`TaskGroup` deliberately raises an `ExceptionGroup` (PEP 654) instead of just the first exception,
which is what `gather()` does by default: if several Tasks fail at the same time (for example, two
of them were talking to the same unreachable service), the developer sees all the causes at once,
not just whichever one happened to arrive first. Handling that result requires `except*` rather than
a plain `except`, because an `ExceptionGroup` is not itself a direct instance of any single exception
type inside it.

The "aborting" state also blocks further `create_task()` calls on that same group – attempting to
add a new Task after cancellation has started raises a `RuntimeError`, because the group can no
longer guarantee it will manage to wait for and cancel something added after teardown began.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
