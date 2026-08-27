---
id: py-async-0014
title: "What failure and cancellation semantics of `gather()` must be taken into account so sibling work isn't left unsupervised?"
description: "What failure and cancellation semantics of `gather()` must be taken into account so sibling work isn't left unsupervised?"
track: python
section: asyncio
level: senior
type: pitfall
tags: [gather]
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

**With `return_exceptions=False` (the default) the first exception is immediately propagated to the
caller, but the other awaitables keep running – they are not cancelled
automatically.**[^py314-library-asyncio-task] If cancelling sibling tasks on failure is needed, use
`TaskGroup` or cancel the tasks manually. With `return_exceptions=True`, exceptions are treated as
results and aggregated into a list – but the caller must check each element for an exception itself.

## Detailed explanation

Mechanically, `gather()` wraps each coroutine passed to it in its own Task (Futures and already
existing Tasks are used as-is) and waits for all of them to finish. Each of these internal Tasks is
scheduled on the loop independently and starts running right after `gather()` is called, well before
the first exception happens.[^py314-library-asyncio-task] When one of them fails, `gather()` simply
sets an exception on its own Future and returns control to the caller – but it does not touch the
other Tasks itself, because they already live independently on the loop rather than inside `gather()`.

This must be kept separate from cancelling `gather()` itself. If the awaitable that `gather()`
returns is cancelled (for example, by cancelling the Task that is awaiting it), `gather()` does
propagate cancellation to all of its internal Tasks – the opposite behavior from the exception case.
In other words: cancelling the outer call cascades to the siblings, but a failure inside one of the
awaitables does not.

The practical consequence is that unsupervised siblings can finish later with their own result or
their own exception that nobody reads; for an exception this produces the same
`Task exception was never retrieved` warning as for ordinary orphaned Tasks. So the pattern "fire off
a bunch of requests through `gather()` and catch the first exception" is unsafe in production code
without explicitly cancelling the rest.

`TaskGroup` solves this systematically: on an exception in any child, it cancels all siblings itself,
with no manual code needed. The manual alternative without `TaskGroup` is to keep a list of Tasks,
wrap `gather()` in `try/except`, and in the `except` clause explicitly call `.cancel()` on every Task
that has not finished yet.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
