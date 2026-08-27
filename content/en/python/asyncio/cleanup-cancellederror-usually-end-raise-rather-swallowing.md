---
id: py-async-0017
title: "Why should cleanup after a `CancelledError` usually end with a re-raise rather than swallowing the cancellation?"
description: "Why should cleanup after a `CancelledError` usually end with a re-raise rather than swallowing the cancellation?"
track: python
section: asyncio
level: senior
type: pitfall
tags: [cancellederror]
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

**If `CancelledError` is caught and not re-raised, the task looks like it completed normally –
outer code (`TaskGroup`, `gather`) never learns about the cancellation, which breaks structured
concurrency.**[^py314-library-asyncio-task] The correct pattern is `try/finally` for cleanup with
an implicit re-raise, or an explicit `raise` in `except CancelledError`. Swallowing it requires
`Task.uncancel()` and should only be used when the cancellation genuinely needs to be ignored.

## Detailed explanation

Before Python 3.8, `CancelledError` inherited from `Exception`, so an ordinary `except Exception:`
in code (for example, generic retry logic) would accidentally swallow cancellation along with real
errors. The change to `BaseException` was a deliberate decision so that a broad `except Exception`
no longer silently catches cancellation; now only an explicit `except CancelledError` or a bare
`except:` catches it.[^py314-library-asyncio-dev]

The consequence for `TaskGroup`: when one child Task fails with an exception, the group cancels the
remaining child Tasks and waits until each of them actually finishes – either with a
`CancelledError` or normally. If a child Task catches `CancelledError` and does not re-raise it, it
finishes as "successful", and `TaskGroup` considers the cancellation done and moves on, even though
the intent was to stop all the work; the outer code loses the signal that part of the work did not
actually complete correctly.[^py314-library-asyncio-task]

The `try/finally` pattern is the safest precisely because `finally` runs regardless of how `try`
finished and does not change the exception itself – it automatically propagates further after
`finally`, unless there is a separate `return` or `raise` inside it that replaces it. An explicit
`except CancelledError: ... raise` is equivalent, but it is easier to break with an accidental
`return` inside the `except` block that silently swallows the cancellation.

`gather(..., return_exceptions=True)` is a special case: it collects each task's `CancelledError`
as an ordinary result in the list instead of raising it, so the caller has to check every result
element for `isinstance(r, BaseException)` itself, otherwise a cancelled task gets silently
ignored.

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
