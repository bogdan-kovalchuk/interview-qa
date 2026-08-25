# Topic brief: 05_functions_scope_closures

## Goal and scope

Test argument binding, defaults, Python's pass-by-assignment model, scopes, closures, and callable
design. Decorator mechanics belong to topic 07.

## Sources

- Official: https://docs.python.org/3.14/reference/compound_stmts.html#function-definitions
- Official: https://docs.python.org/3.14/reference/expressions.html#calls
- Official: https://docs.python.org/3.14/reference/executionmodel.html
- Official: https://docs.python.org/3.14/faq/programming.html
- Candidate Q&A: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/functions.md
- Candidate Q&A: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/namespace_and_context_manager.md

## Coverage plan

| Cluster | Retrieval operation | Middle | Senior | Total |
|---|---|---:|---:|---:|
| Signature and argument binding | predict and design | 4 | 1 | 5 |
| Defaults and sentinel objects | diagnose and choose | 2 | 1 | 3 |
| Pass-by-assignment and mutation | explain and predict | 2 | 1 | 3 |
| LEGB `global` and `nonlocal` | resolve and debug | 3 | 1 | 4 |
| Closures and late binding | predict and repair | 2 | 2 | 4 |
| First-class callables and lambda | apply and constrain | 2 | 1 | 3 |
| Annotations and callable contracts | interpret and design | 1 | 1 | 2 |

Planned total: 24 fronts, all Middle+.

## Sensitive boundaries

- Defaults are evaluated when the function definition executes, not necessarily once per process.
- Closure behavior is not specific to lambdas.
