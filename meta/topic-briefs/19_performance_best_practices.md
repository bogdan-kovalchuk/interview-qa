# Topic brief: 19_performance_best_practices

## Goal and scope

Test measurement-first optimization, complexity, allocation, caching, concurrency choice, memory
diagnostics, and maintainability trade-offs. Exclude benchmark folklore and unexplained micro-tips.

## Sources

- Official: https://docs.python.org/3.14/library/profile.html
- Official: https://docs.python.org/3.14/library/timeit.html
- Official: https://docs.python.org/3.14/library/tracemalloc.html
- Official: https://docs.python.org/3.14/library/concurrent.futures.html
- Official: https://docs.python.org/3.14/faq/programming.html#performance
- Official: https://docs.python.org/3.14/library/functools.html#functools.lru_cache
- Official: https://docs.python.org/3.14/library/stdtypes.html#common-sequence-operations
- Candidate Q&A: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/python_packages.md

## Coverage plan

| Cluster | Retrieval operation | Middle | Senior | Total |
|---|---|---:|---:|---:|
| Profiling benchmarking and measurement bias | choose and interpret | 2 | 2 | 4 |
| Algorithmic and data-structure cost | diagnose and improve | 2 | 1 | 3 |
| Allocation copying and lazy processing | assess and optimize | 2 | 1 | 3 |
| Cache key and semantic constraints | diagnose misuse | 2 | 0 | 2 |
| Cache invalidation and eviction | design and bound | 0 | 1 | 1 |
| Concurrency choice for performance | choose and justify | 1 | 1 | 2 |
| I/O batching vectorization and native code | choose and constrain | 1 | 1 | 2 |
| Readability and Pythonic trade-offs | review and justify | 2 | 0 | 2 |
| Memory growth and `tracemalloc` | diagnose | 1 | 1 | 2 |

Planned total: 21 fronts, all Middle+.

## Sensitive boundaries

- Performance statements need workload and implementation context.
- A single timing run is evidence about that run, not a language guarantee.
