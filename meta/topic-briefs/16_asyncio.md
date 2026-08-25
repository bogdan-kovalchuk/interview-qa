# Topic brief: 16_asyncio

## Goal and scope

Test coroutine/task semantics, event-loop cooperation, structured concurrency, cancellation,
timeouts, blocking bridges, synchronization, and overload behavior. Exclude web frameworks and
specific HTTP clients.

## Sources

- Official: https://docs.python.org/3.14/library/asyncio-task.html
- Official: https://docs.python.org/3.14/library/asyncio-eventloop.html
- Official: https://docs.python.org/3.14/library/asyncio-dev.html
- Candidate Q&A: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/async.md

## Coverage plan

| Cluster | Retrieval operation | Middle | Senior | Total |
|---|---|---:|---:|---:|
| Coroutines awaitables and tasks | distinguish and trace | 3 | 1 | 4 |
| Event loop readiness and cooperation | explain and diagnose | 2 | 2 | 4 |
| `TaskGroup` structured concurrency | apply and compare | 2 | 1 | 3 |
| `gather` `wait` and `as_completed` | choose and predict | 2 | 1 | 3 |
| Cancellation timeouts and shielding | design and diagnose | 2 | 2 | 4 |
| Blocking work `to_thread` and executors | choose and constrain | 1 | 1 | 2 |
| Async synchronization and races | diagnose and protect | 1 | 1 | 2 |
| `ContextVar` debugging and backpressure | design and observe | 1 | 1 | 2 |

Planned total: 24 fronts, all Middle+.

## Sensitive boundaries

- Creating coroutine objects is not the same as scheduling concurrent tasks.
- Cancellation is cooperative and cleanup code must preserve cancellation semantics.
