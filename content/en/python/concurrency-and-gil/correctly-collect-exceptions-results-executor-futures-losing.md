---
id: py-gil-0020
title: "How do you correctly collect exceptions and results from executor futures without losing a worker failure?"
description: "How do you correctly collect exceptions and results from executor futures without losing a worker failure?"
track: python
section: concurrency-and-gil
level: senior
type: practical
tags: []
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-library-threading
    title: "Python 3.14: Library/threading"
    url: https://docs.python.org/3.14/library/threading.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-multiprocessing
    title: "Python 3.14: Library/multiprocessing"
    url: https://docs.python.org/3.14/library/multiprocessing.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-concurrent-futures
    title: "Python 3.14: Library/concurrent.futures"
    url: https://docs.python.org/3.14/library/concurrent.futures.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-howto-free-threading-python
    title: "Python 3.14: Howto/free Threading Python"
    url: https://docs.python.org/3.14/howto/free-threading-python.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-howto-free-threading-extensions
    title: "Python 3.14: Howto/free Threading Extensions"
    url: https://docs.python.org/3.14/howto/free-threading-extensions.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/gil_threads_processes.md#L940-L986
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**`Future.result()` returns the value or re-raises the worker's exception; `Future.exception()`
returns the exception object or `None`.**[^py314-library-threading] To collect results from
several futures, use `concurrent.futures.as_completed(fs)`, which yields futures in the order they
finish – letting you handle each failure individually. `Executor.map()` returns results in call
order, but the exception is only raised when that result is accessed. <span
class="warn">If `result()` is never called and a future is never handled through `as_completed`,
the worker's exception is silently lost.</span>

## Detailed explanation

A `Future` is a promise-like object for the result of an asynchronous task submitted to an
executor. It always ends up in one of three states: completed successfully with a result,
completed with an exception, or cancelled. The problem in practice is not that the result is
technically lost – the `Future` keeps the exception inside it – but that code can simply never
check that state.[^py314-library-concurrent-futures]

`future.result()` returns the value if the task finished successfully, and re-raises the same
exception if the worker failed. `future.exception()` gives access to the exception object without
re-raising it, returning `None` on success. Both methods block the caller until the task finishes
(with an optional `timeout`).

Example of correctly collecting results and errors from several futures:

```python
from concurrent.futures import as_completed

futures = [executor.submit(worker, item) for item in items]
for future in as_completed(futures):
    try:
        result = future.result()
    except Exception as exc:
        log_failure(future, exc)
    else:
        process(result)
```

`as_completed()` yields futures in the order they finish, not the order they were submitted, so
each result or error is handled as soon as it is ready, without waiting for the slowest one.
`Executor.map()`, by contrast, preserves call order and only raises an exception at the moment the
corresponding element is iterated – if iteration stops early, errors from the remaining tasks are
never seen.

**Common ways to silently lose a worker failure:**
- submit tasks via `submit()` and never call `result()` or `exception()` on the returned futures –
  execution finishes and the exception simply disappears;
- iterate over a list of futures in submission order instead of using `as_completed()`, or apply
  `map()` without handling the exception at each step of iteration;
- use `executor.map()` and keep only the generator itself without fully iterating over it – an
  exception on a later element never gets raised.

Explicitly checking every `Future` – via `result()`, `exception()`, or `add_done_callback()` – is
the only way to reliably see a worker's failure.[^py314-library-concurrent-futures]

## Environment

TODO

## Deliverable

TODO

## Acceptance criteria

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
