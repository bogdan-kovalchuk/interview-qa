---
id: py-testing-0009
title: "Як broad-scoped mutable fixture може створити order-dependent tests і state leakage?"
description: "Fixture з scope=\"module\" або scope=\"session\", що повертає mutable об'єкт (dict, list, DB connection), створює один спільний екземпляр для всіх тестів у scope – і якщо один тест модифікує цей об'єкт, наступні тести..."
track: python
section: testing
level: senior
type: pitfall
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/python_packages.md#L122-L168
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Fixture з `scope="module"` або `scope="session"`, що повертає mutable об'єкт (dict, list, DB connection), створює один спільний екземпляр для всіх тестів у scope – і якщо один тест модифікує цей об'єкт, наступні тести отримують забруднений state.**[^py314-library-unittest] 

```python
@pytest.fixture(scope="module")
def shared_cache():
    return {}  # один dict на весь module

def test_a(shared_cache):
    shared_cache["key"] = "value"

def test_b(shared_cache):
    assert "key" not in shared_cache  # FAIL: state leakage
```

Це створює order-dependent tests: результат залежить від порядку виконання. Рішення: `function` scope для mutable fixtures, immutable factory-функція, або явний reset у teardown.

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
