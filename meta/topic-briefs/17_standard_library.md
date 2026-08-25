# Topic brief: 17_standard_library

## Goal and scope

Test whether a candidate selects high-value standard-library tools instead of reimplementing them.
Avoid method inventories and obscure modules that are normal documentation lookups.

## Sources

- Official: https://docs.python.org/3.14/library/collections.html
- Official: https://docs.python.org/3.14/library/itertools.html
- Official: https://docs.python.org/3.14/library/functools.html
- Official: https://docs.python.org/3.14/library/pathlib.html
- Official: https://docs.python.org/3.14/library/datetime.html
- Official: https://docs.python.org/3.14/library/re.html
- Official: https://owasp.org/www-community/attacks/Regular_expression_Denial_of_Service_-_ReDoS
- Candidate Q&A: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/standard_library.md

## Coverage plan

| Cluster | Retrieval operation | Middle | Senior | Total |
|---|---|---:|---:|---:|
| `collections` specialized containers | choose and justify | 2 | 1 | 3 |
| `itertools` lazy composition | select and predict | 2 | 1 | 3 |
| `functools` properties and ordering | apply and assess | 1 | 1 | 2 |
| `pathlib` and `os` boundary | choose | 2 | 0 | 2 |
| `datetime` and `zoneinfo` correctness | diagnose and choose | 2 | 0 | 2 |
| `heapq` and `bisect` use cases | select and assess | 2 | 0 | 2 |
| `logging` library design | configure conceptually | 1 | 0 | 1 |
| `dataclasses` and `enum` | choose | 1 | 0 | 1 |
| `inspect` runtime introspection | assess coupling | 0 | 1 | 1 |
| `re` denial-of-service boundary | diagnose risk | 0 | 1 | 1 |

Planned total: 18 fronts, all Middle+.

## Sensitive boundaries

- Questions test tool selection and trade-offs, not memorized signatures.
- Datetime fronts must distinguish naive and aware objects.
