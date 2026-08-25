# Topic brief: 07_decorators

## Goal and scope

Test when decoration happens, wrapper correctness, factories, composition, state, and callable
variants. Avoid asking only for the textbook definition of a decorator.

## Sources

- Official: https://docs.python.org/3.14/glossary.html#term-decorator
- Official: https://docs.python.org/3.14/library/functools.html#functools.wraps
- Official: https://docs.python.org/3.14/reference/compound_stmts.html#function-definitions
- Candidate Q&A: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/decorators.md

## Coverage plan

| Cluster | Retrieval operation | Middle | Senior | Total |
|---|---|---:|---:|---:|
| Evaluation and application timing | predict and explain | 2 | 0 | 2 |
| Wrapper metadata and signatures | diagnose and preserve | 1 | 1 | 2 |
| Decorator factories and parameters | implement and explain | 1 | 1 | 2 |
| Callable objects and class decorators | contrast and choose | 1 | 1 | 2 |
| Stacking order and composition | predict and design | 1 | 1 | 2 |
| Stateful async and error-handling pitfalls | diagnose and repair | 1 | 1 | 2 |

Planned total: 12 fronts, all Middle+.

## Sensitive boundaries

- Do not conflate decoration-time calls with wrapper invocation-time calls.
- Async wrappers must preserve coroutine behavior and exception propagation.
