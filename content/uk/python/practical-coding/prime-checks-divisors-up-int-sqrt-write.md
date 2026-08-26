---
id: py-prac-0022
title: "Для `is_prime(n)`, яка перевіряє divisors до `int(sqrt(n))`, складіть tests, що вбивають mutants `<` vs `<=` на square boundary і помилку для `n < 2`."
description: "Три групи тестів: base case n < 2, perfect square (вбиває мутацію < vs <=) і звичайні prime/composite."
track: python
section: practical-coding
level: middle
type: practical
tags: [is-prime-n, int-sqrt-n, lt, n-lt-2]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: py314-tutorial
    title: "Python 3.14: Tutorial"
    url: https://docs.python.org/3.14/tutorial/
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference
    title: "Python 3.14: Reference"
    url: https://docs.python.org/3.14/reference/
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-threading
    title: "Python 3.14: Library/threading"
    url: https://docs.python.org/3.14/library/threading.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-time-time-monotonic
    title: "Python 3.14: Library/time"
    url: https://docs.python.org/3.14/library/time.html#time.monotonic
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/coding.md#L83-L104
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Три групи тестів: base case `n < 2`, perfect square (вбиває мутацію `<` vs `<=`) і звичайні prime/composite.**[^py314-tutorial] Для мутації: `is_prime(4)` – `int(sqrt(4)) == 2`; з правильним `<=` divisor 2 знаходить `4 % 2 == 0` -> `False`, а з `<` діапазон порожній і повертає хибний `True`. Аналогічно `is_prime(9)` (sqrt=3). Для `n < 2`: `is_prime(0)`, `is_prime(1)`, `is_prime(-7)` -> `False`. Додатково: `is_prime(2)` -> `True`, `is_prime(25)` -> `False`.

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
