---
id: py-async-0004
title: "Why does a fire-and-forget Task need a strong reference kept and its outcome explicitly handled?"
description: "Why does a fire-and-forget Task need a strong reference kept and its outcome explicitly handled?"
track: python
section: asyncio
level: senior
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/async.md#L665-L745
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**The event loop only keeps weak references to Tasks, so a Task with no external reference can be
destroyed by the GC before it finishes.**[^py314-library-asyncio-task] If a Task finishes with an
exception and nobody reads the result, Python emits
<span class="warn">"Task exception was never retrieved"</span>. The standard pattern is to keep
Tasks in a `set` and remove the reference via `add_done_callback`, or to use `TaskGroup`, which
automatically holds strong references.

## Detailed explanation

This is a deliberate design choice, not an oversight: if the loop itself kept a strong reference to
every Task it creates, a long-running process that keeps calling `create_task()` for fire-and-forget
work would never free the memory of those Tasks, even after they finish.[^py314-library-asyncio-eventloop]
So responsibility for a Task's lifetime is deliberately placed on the code that created it.

The moment the GC destroys the Task matters for which warning the developer actually sees. If a
Task is destroyed while still pending (no strong reference exists, and it has not finished yet),
Python emits a different warning – "Task was destroyed but it is pending!" – and the work it was
supposed to do simply breaks off midway. If instead the Task managed to finish with an exception
before being destroyed, the Task's own `__del__` runs, checks whether the exception was read via
`.result()` or `.exception()`, and if not, prints "Task exception was never retrieved" to the
loop's exception handler.[^py314-library-asyncio-task]

The idiomatic pattern recommended by the documentation is to keep all fire-and-forget Tasks in a
module-level `set` and drop the reference only after they finish:

```python
background_tasks: set[asyncio.Task] = set()
task = asyncio.create_task(worker())
background_tasks.add(task)
task.add_done_callback(background_tasks.discard)
```

`add_done_callback` here is not for handling the result, only for cleaning up the set – the callback
itself is invoked by the loop after the Task has already finished, once holding the reference is no
longer necessary.

`TaskGroup` solves this same problem structurally: it holds strong references to all of its children
itself for as long as the `async with` block runs, which is exactly why it is impossible to
accidentally "lose" a Task there – a Task's lifetime is tightly bound to the block's lifetime.

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
