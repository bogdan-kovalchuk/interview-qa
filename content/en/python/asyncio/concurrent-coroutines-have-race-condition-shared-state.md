---
id: py-async-0021
title: "Why can concurrent coroutines have a race condition on shared state even within a single OS thread?"
description: "Why can concurrent coroutines have a race condition on shared state even within a single OS thread?"
track: python
section: asyncio
level: middle
type: pitfall
tags: []
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/async.md#L1141-L1186
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**Because `await` is a voluntary yield point: the event loop can switch execution to another Task,
and that Task will see an intermediate state of the shared resource.**[^py314-library-asyncio-task]
In CPython the event loop cooperatively schedules tasks: until a Task executes an `await`, no other
Task in that same thread runs. But as soon as a coroutine does an `await` (for example, on I/O or
`asyncio.sleep`), the loop hands control to another Task, which can change a shared dict, counter,
or list before the first Task resumes. The fix is to use `asyncio.Lock` around critical sections, or
design the code so that state stays consistent between `await` points.

## Detailed explanation

The key difference from a race condition between OS threads: here a switch can only happen at an
`await` point, not at an arbitrary spot, so a straight-line stretch of code with no `await` in it
always runs atomically with respect to other Tasks. That narrows the surface of the problem but
does not remove it: a classic example is "check, then act" over a shared resource, where the check
and the action are separated by an `await`:

```python
if balance >= amount:
    await ledger.write(amount)   # інша Task встигає списати тут
    balance -= amount
```

If there is an `await ledger.write(...)` between checking `balance >= amount` and actually
deducting it, another Task can run the same block in between and also pass the check against the
old value of `balance`, after which both deduct funds even though there was not enough for both
combined.[^py314-library-asyncio-dev]

Unlike a race condition between threads, the order of switches here is not arbitrary in the sense
of a hardware race – it is deterministic relative to which callbacks became ready and in what
order. But to the caller it looks just as nondeterministic, because the order of readiness depends
on external factors (for example, exactly when a network response arrives), not on the order of
lines in the code.

The most reliable way to avoid the problem is to keep the critical section that contains both the
check and the state change free of any `await` inside it; if an `await` is unavoidable (for
example, I/O is needed to write), the section has to be wrapped in an `asyncio.Lock`, so other
Tasks wait for it to be released instead of running through the same block in parallel.

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
