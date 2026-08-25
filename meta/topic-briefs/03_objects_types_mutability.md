# Topic brief: 03_objects_types_mutability

## Goal and scope

Test the object/reference model, equality contracts, mutability, copying, hashability, binary/text
boundaries, and the role of static type hints. Collection-specific APIs belong to topic 04.

## Sources

- Official: https://docs.python.org/3.14/reference/datamodel.html
- Official: https://docs.python.org/3.14/library/stdtypes.html
- Official: https://docs.python.org/3.14/library/copy.html
- Official: https://docs.python.org/3.14/library/typing.html
- Candidate Q&A: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/data_types.md

## Coverage plan

| Cluster | Retrieval operation | Middle | Senior | Total |
|---|---|---:|---:|---:|
| Identity equality and `is` | contrast and diagnose | 3 | 1 | 4 |
| Mutability aliasing and rebinding | predict and explain | 3 | 1 | 4 |
| Shallow and deep copying | choose and diagnose | 2 | 1 | 3 |
| Hashability and equality contract | explain and design | 2 | 1 | 3 |
| Numeric and floating-point behavior | predict and mitigate | 2 | 1 | 3 |
| Text bytes and buffer types | convert and choose | 2 | 1 | 3 |
| Runtime types vs static typing | contrast and qualify | 1 | 1 | 2 |

Planned total: 22 fronts, all Middle+.

## Sensitive boundaries

- Never infer identity guarantees from CPython caching or interning observations.
- Type hints normally do not enforce values at runtime.
