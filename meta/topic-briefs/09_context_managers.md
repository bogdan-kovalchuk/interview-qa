# Topic brief: 09_context_managers

## Goal and scope

Test deterministic setup/cleanup, suppression semantics, generator-based managers, dynamic
resource stacks, and async context management. General exception design belongs to topic 10.

## Sources

- Official: https://docs.python.org/3.14/reference/datamodel.html#with-statement-context-managers
- Official: https://docs.python.org/3.14/library/contextlib.html
- Official: https://docs.python.org/3.14/library/asyncio-task.html#task-cancellation
- Candidate Q&A: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/namespace_and_context_manager.md

## Coverage plan

| Cluster | Retrieval operation | Middle | Senior | Total |
|---|---|---:|---:|---:|
| `__enter__` `__exit__` and suppression | trace and implement | 2 | 1 | 3 |
| Class vs generator-based manager | contrast and choose | 2 | 0 | 2 |
| `ExitStack` and dynamic resources | apply and design | 1 | 1 | 2 |
| Async context managers | implement and qualify | 1 | 1 | 2 |
| Reentrancy and reuse | diagnose | 1 | 0 | 1 |

Planned total: 10 fronts, all Middle+.

## Sensitive boundaries

- Returning a truthy value from `__exit__` suppresses the exception.
- Context managers guarantee protocol execution, not successful cleanup under process failure.
