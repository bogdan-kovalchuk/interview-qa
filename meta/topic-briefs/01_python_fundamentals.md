# Topic brief: 01_python_fundamentals

## Goal and scope

Test whether a Middle+ candidate can explain Python's execution and type model, separate the
language from CPython, and use introspection without relying on slogans. Exclude beginner syntax,
installation trivia, and detailed memory management owned by topic 14.

## Sources

- Official: https://docs.python.org/3.14/reference/executionmodel.html
- Official: https://docs.python.org/3.14/reference/datamodel.html
- Official: https://docs.python.org/3.14/faq/general.html
- Candidate Q&A: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/general.md

The candidate source has no detected license. Use only its concept map and create exact line
permalinks later in `tracking/front_sources.csv`.

## Coverage plan

| Cluster | Retrieval operation | Middle | Senior | Total |
|---|---|---:|---:|---:|
| Source to execution pipeline | explain and contrast | 2 | 1 | 3 |
| Dynamic typing and name binding | explain and diagnose | 2 | 1 | 3 |
| Python language vs implementation | qualify guarantees | 1 | 1 | 2 |
| Introspection and monkey patching | choose and assess risk | 2 | 0 | 2 |
| Reflection and runtime structure | apply and bound | 2 | 0 | 2 |

Planned total: 12 fronts, all Middle+.

## Sensitive boundaries

- Bytecode format, reference counting, interning, and object layout are CPython details.
- `compiled` and `interpreted` are pipeline properties, not mutually exclusive language labels.
