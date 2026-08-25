# Topic brief: 10_exceptions

## Goal and scope

Test exception selection, control flow, chaining, re-raising, groups, warnings, and observability.
Exclude rote enumeration of the full exception hierarchy.

## Sources

- Official: https://docs.python.org/3.14/tutorial/errors.html
- Official: https://docs.python.org/3.14/library/exceptions.html
- Official: https://docs.python.org/3.14/reference/compound_stmts.html#the-try-statement
- Candidate Q&A: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/exceptions.md

## Coverage plan

| Cluster | Retrieval operation | Middle | Senior | Total |
|---|---|---:|---:|---:|
| Hierarchy and catching boundaries | choose and diagnose | 2 | 1 | 3 |
| `else` `finally` return and cleanup | predict and explain | 2 | 1 | 3 |
| Chaining traceback and re-raise | preserve and diagnose | 2 | 1 | 3 |
| Custom exception design | design and justify | 2 | 0 | 2 |
| `ExceptionGroup` and `except*` | apply and qualify | 1 | 1 | 2 |
| EAFP vs LBYL | choose | 1 | 0 | 1 |
| Warnings and exception logging | select and diagnose | 1 | 1 | 2 |

Planned total: 16 fronts, all Middle+.

## Sensitive boundaries

- Bare `except` and catching `BaseException` require explicit justification.
- `ExceptionGroup` behavior is version-sensitive and must state Python 3.14.
