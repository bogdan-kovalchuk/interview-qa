# Topic brief: 08_iterators_generators

## Goal and scope

Test iterable/iterator contracts, generator state, delegation, bidirectional generator methods,
exhaustion, and lazy composition. Async iteration belongs to topic 16.

## Sources

- Official: https://docs.python.org/3.14/library/stdtypes.html#iterator-types
- Official: https://docs.python.org/3.14/reference/expressions.html#yield-expressions
- Official: https://docs.python.org/3.14/reference/datamodel.html#object.__iter__
- Candidate Q&A: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/iterator_and_generator.md

## Coverage plan

| Cluster | Retrieval operation | Middle | Senior | Total |
|---|---|---:|---:|---:|
| Iterable and iterator protocols | implement and trace | 3 | 1 | 4 |
| Generator creation state and laziness | predict and explain | 3 | 1 | 4 |
| `yield from` `send` `throw` and `close` | trace and apply | 2 | 2 | 4 |
| Exhaustion cleanup and one-shot behavior | diagnose and design | 2 | 1 | 3 |
| Generator expressions and pipeline composition | choose and assess | 2 | 1 | 3 |

Planned total: 18 fronts, all Middle+.

## Sensitive boundaries

- A generator object is an iterator; an iterable need not be an iterator.
- Generator cleanup and finalization must not be presented as deterministic resource management.
