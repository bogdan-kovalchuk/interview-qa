---
id: py-async-0006
title: "Why can a coroutine with no suspension point monopolize the event-loop thread?"
description: "Why can a coroutine with no suspension point monopolize the event-loop thread?"
track: python
section: asyncio
level: middle
type: mechanism
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/async.md#L590-L652
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**A coroutine that contains no `await` at all runs synchronously from start to finish without
handing control back to the event loop, and so it blocks every other Task and I/O from
running.**[^py314-library-asyncio-task] Cooperative multitasking only works when each coroutine
periodically yields via a suspension point. Without that, the event loop cannot process other ready
callbacks, even if they have been waiting for a long time.

## Detailed explanation

The most common cause of this in practice is not CPU-heavy code by itself, but a synchronous
blocking call inside an `async def` that looks harmless: `time.sleep(1)`, or a synchronous HTTP
request through a library like `requests`. Neither of these is a suspension point for the event
loop – they simply hold onto the control flow until they finish, and the loop physically cannot
process anything else during that time, not even the `asyncio.sleep()` timers of other Tasks that
were already due to fire.[^py314-library-asyncio-eventloop]

This differs from a deadlock: sooner or later the synchronous call finishes on its own, and the
event loop resumes normal operation – it is just that during that whole time every other Task and
I/O callback sits waiting in the ready queue, even if it has been ready for a while. In debug mode,
asyncio makes the symptom directly visible: if executing one callback exceeds the
`loop.slow_callback_duration` threshold (0.1 seconds by default), the loop logs a warning
"Executing ... took X seconds", which points straight at a missing suspension point.[^py314-library-asyncio-dev]

The explicit way to force control to be handed over even without a real wait is `await
asyncio.sleep(0)`: it does not delay execution by zero seconds so much as put the coroutine at the
back of the ready-callback queue for one turn of the event loop, giving other Tasks a chance to
run. For CPU-bound computation this only eases the symptom, not the cause – the real fix there is
to move the heavy work into `run_in_executor()` or a separate process, so it never occupies the
event-loop thread at all.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
