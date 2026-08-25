# Topic brief: 13_comprehensions_functional

## Goal and scope

Test comprehension scope and evaluation, lazy pipelines, higher-order utilities, and functional
trade-offs in idiomatic Python. Exclude abstract functional-programming history.

## Sources

- Official: https://docs.python.org/3.14/howto/functional.html
- Official: https://docs.python.org/3.14/library/itertools.html
- Official: https://docs.python.org/3.14/library/functools.html
- Official: https://docs.python.org/3.14/reference/expressions.html#displays-for-lists-sets-and-dictionaries
- Candidate Q&A: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/functional_programming.md

## Coverage plan

| Cluster | Retrieval operation | Middle | Senior | Total |
|---|---|---:|---:|---:|
| Comprehension scope and evaluation order | predict and explain | 2 | 1 | 3 |
| Generator expression vs materialization | choose and assess | 2 | 0 | 2 |
| Functional transforms and iterator consumption | predict and compose | 2 | 0 | 2 |
| Higher-order functions partial and dispatch | apply and design | 2 | 1 | 3 |
| `map` `filter` `reduce` and readability | compare and choose | 1 | 1 | 2 |

Planned total: 12 fronts, all Middle+.

## Sensitive boundaries

- Comprehension scope differs from ordinary loop-variable leakage.
- Laziness claims must distinguish iterator creation from element evaluation.
