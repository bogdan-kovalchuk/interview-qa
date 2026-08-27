---
id: py-async-0018
title: "When does `asyncio.shield()` protect an inner Task but not cancel the caller's own cancellation?"
description: "When does `asyncio.shield()` protect an inner Task but not cancel the caller's own cancellation?"
track: python
section: asyncio
level: senior
type: comparison
tags: [asyncio-shield]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/async.md#L1248-L1289
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**`shield()` protects the inner awaitable from cancellation of the outer caller: the caller gets a
`CancelledError`, but the inner task keeps running.**[^py314-library-asyncio-task]
<span class="warn">If the inner task is cancelled some other way (for example, self-cancellation),
`shield()` propagates that cancellation too.</span> To fully ignore cancellation you could wrap
`shield()` in `try/except CancelledError`, but that is usually not recommended.

## Detailed explanation

`asyncio.shield(aw)` does not block cancellation as such – it breaks the link between the
`CancelledError` that reaches the caller and the inner Task itself.[^py314-library-asyncio-task]
Inside `shield()`, the awaitable is wrapped in its own `Task` (via `ensure_future`), and the caller
actually awaits not the inner Task itself but a `Future` proxy. When the caller is cancelled, the
`CancelledError` is delivered exactly at the point of `await shield(...)`, not into the inner Task:
shield catches that exception, detaches the proxy from the inner Task (removing the callback that
would have cancelled it) and immediately re-raises the `CancelledError` to the caller. The inner
Task itself does not receive a cancellation request and keeps running on the event loop regardless
of what the caller does next.

The key consequence is that the caller loses direct control over the result: if it did not keep a
separate reference to the inner Task, it can neither await its completion later nor learn about an
exception it raised – `Task exception was never retrieved` is the typical symptom here. That is why
`shield()` is usually used together with a separately stored variable holding the Task itself,
rather than only as `await asyncio.shield(coro())`.

`shield()` only protects against cancellation initiated from the outside, through the caller. If
the inner Task is cancelled directly (`task.cancel()`) or performs self-cancellation, shield does
nothing – the `CancelledError` originates inside the Task itself and propagates the normal way,
because shield only breaks one specific cancellation-delivery chain, not makes the Task
indestructible altogether.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
