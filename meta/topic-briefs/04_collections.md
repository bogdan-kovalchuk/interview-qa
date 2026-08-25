# Topic brief: 04_collections

## Goal and scope

Test collection selection, protocols, ordering, lookup behavior, and complexity trade-offs. Avoid
memorizing complete method inventories and avoid general algorithm coursework.

## Sources

- Official: https://docs.python.org/3.14/library/stdtypes.html
- Official: https://docs.python.org/3.14/library/collections.html
- Official: https://docs.python.org/3.14/howto/sorting.html
- Candidate Q&A: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/sequences.md
- Candidate Q&A: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/set_and_dict.md

## Coverage plan

| Cluster | Retrieval operation | Middle | Senior | Total |
|---|---|---:|---:|---:|
| List tuple and range trade-offs | choose and explain | 4 | 1 | 5 |
| Dictionary contracts and views | predict and design | 4 | 2 | 6 |
| Set and frozenset behavior | choose and diagnose | 3 | 1 | 4 |
| Collection protocols and live views | explain and apply | 2 | 1 | 3 |
| Ordering sorting and stability | predict and choose | 2 | 1 | 3 |
| Lookup and iteration complexity | compare and justify | 2 | 1 | 3 |

Planned total: 24 fronts, all Middle+.

## Sensitive boundaries

- Separate language guarantees such as dict insertion order from CPython table layout.
- Complexity claims need documented assumptions and must not be presented as strict worst-case
  guarantees when they are average-case implementation behavior.
