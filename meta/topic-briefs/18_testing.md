# Topic brief: 18_testing

## Goal and scope

Test test-boundary design, determinism, fixtures, doubles, mocking, asynchronous dependencies,
coverage interpretation, and flaky-test diagnosis. Avoid framework syntax trivia.

## Sources

- Official: https://docs.python.org/3.14/library/unittest.html
- Official: https://docs.python.org/3.14/library/unittest.mock.html
- Official project docs: https://docs.pytest.org/en/stable/
- Official project docs: https://hypothesis.readthedocs.io/en/latest/
- Official project docs: https://mutmut.readthedocs.io/en/latest/
- Candidate Q&A: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/computer_science/testing.md

## Coverage plan

| Cluster | Retrieval operation | Middle | Senior | Total |
|---|---|---:|---:|---:|
| Unit integration and end-to-end boundaries | classify and choose | 2 | 1 | 3 |
| Determinism seams and external dependencies | design and diagnose | 2 | 1 | 3 |
| Fixtures parametrization and isolation | apply and assess | 2 | 1 | 3 |
| Test doubles and where to patch | choose and debug | 3 | 1 | 4 |
| Async time and randomness control | design and diagnose | 1 | 1 | 2 |
| Property-based testing | recognize and choose | 1 | 0 | 1 |
| Coverage and mutation-test strength | interpret and improve | 2 | 0 | 2 |
| Flaky-test diagnosis | diagnose and preserve evidence | 0 | 1 | 1 |

Planned total: 19 fronts, all Middle+.

## Sensitive boundaries

- Mock behavior must not become a test of the mock implementation.
- Coverage percentage is not proof of behavioral coverage.
