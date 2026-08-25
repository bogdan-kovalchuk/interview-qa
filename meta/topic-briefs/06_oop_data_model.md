# Topic brief: 06_oop_data_model

## Goal and scope

Test Python's object model through construction, attribute access, descriptors, method binding,
inheritance, protocols, and class creation. Avoid language-agnostic OOP trivia unless it changes a
Python design decision.

## Sources

- Official: https://docs.python.org/3.14/reference/datamodel.html
- Official: https://docs.python.org/3.14/howto/descriptor.html
- Official: https://docs.python.org/3.14/howto/mro.html
- Official: https://docs.python.org/3.14/library/dataclasses.html
- Candidate Q&A: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/class_and_object.md
- Candidate Q&A: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/metaclass.md
- Candidate Q&A: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/computer_science/oop.md

## Coverage plan

| Cluster | Retrieval operation | Middle | Senior | Total |
|---|---|---:|---:|---:|
| Object construction and initialization | predict and design | 2 | 1 | 3 |
| Attribute lookup and interception | trace and diagnose | 3 | 2 | 5 |
| Descriptors and properties | explain and implement | 2 | 2 | 4 |
| Method binding and method kinds | contrast and choose | 2 | 1 | 3 |
| Inheritance MRO and `super()` | trace and design | 3 | 2 | 5 |
| Data-model protocols and dunder methods | apply and constrain | 3 | 1 | 4 |
| ABCs and duck typing | contrast and choose | 1 | 1 | 2 |
| Dataclasses and `__slots__` | choose and assess | 2 | 1 | 3 |
| Metaclasses and class creation | explain and justify | 1 | 1 | 2 |

Planned total: 31 fronts, all Middle+.

## Sensitive boundaries

- `__del__`, layout, and memory savings are implementation- and lifecycle-sensitive.
- Descriptor precedence and MRO questions must use documented Python behavior.
