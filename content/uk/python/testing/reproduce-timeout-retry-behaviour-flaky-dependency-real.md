---
id: py-testing-0006
title: "Як відтворити timeout та retry behavior без flaky dependence від реального external service?"
description: "Mock HTTP-клієнта з side_effect імітує послідовність помилок і успіх, а тест перевіряє кількість викликів і backoff-логіку без реальної мережі."
track: python
section: testing
level: senior
type: practical
tags: []
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: py314-library-unittest
    title: "Python 3.14: Library/unittest"
    url: https://docs.python.org/3.14/library/unittest.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-unittest-mock
    title: "Python 3.14: Library/unittest.mock"
    url: https://docs.python.org/3.14/library/unittest.mock.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: pytest-docs
    title: "pytest documentation"
    url: https://docs.pytest.org/en/stable/
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Офіційна документація pytest."
  - source_id: hypothesis-docs
    title: "Hypothesis documentation"
    url: https://hypothesis.readthedocs.io/en/latest/
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Офіційна документація Hypothesis (property-based testing)."
  - source_id: mutmut-docs
    title: "mutmut documentation"
    url: https://mutmut.readthedocs.io/en/latest/
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Офіційна документація mutmut (mutation testing)."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/computer_science/testing.md#L397-L406
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Mock HTTP-клієнта з `side_effect` імітує послідовність помилок і успіх, а тест перевіряє кількість викликів і backoff-логіку без реальної мережі.**[^py314-library-unittest] 

```text
client_mock = Mock(side_effect=[TimeoutError, TimeoutError, ok_response])
result = fetch_with_retry(client_mock, retries=3)
assert client_mock.call_count == 3
```

DI підставляє mock замість реального клієнта; `side_effect` як iterable відтворює сценарій "два таймаути -> успіх" детерміновано. <span class="warn">Реальні sleep у retry-логіці варто підмінювати на injectable delay-функцію, інакше тест стане повільним.</span>

## Detailed explanation

TODO

## Environment

TODO

## Deliverable

TODO

## Acceptance criteria

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
