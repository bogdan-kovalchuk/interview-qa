---
id: py-prac-0006
title: "Реалізуйте FizzBuzz для integers 1..N з ordered rules `[(3, \"Fizz\"), (5, \"Buzz\")]`, щоб нове правило не вимагало нової branch."
description: "Data-driven підхід: для кожного числа конкатенувати label усіх правил, де i % divisor == 0, і fallback на str(i), якщо рядок порожній."
track: python
section: practical-coding
level: middle
type: coding
tags: [3-fizz-5-buzz]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
execution:
  language: python
  standard: null
  toolchain:
    name: cpython
    version: "3.14.7"
  flags: []
anki:
  export: false
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/coding.md#L21-L44
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Task

TODO

## Constraints

TODO

## Short answer

**Data-driven підхід: для кожного числа конкатенувати label усіх правил, де `i % divisor == 0`, і fallback на `str(i)`, якщо рядок порожній.**

```python
def fizzbuzz(n, rules=None):
    if rules is None:
        rules = [(3, "Fizz"), (5, "Buzz")]
    result = []
    for i in range(1, n + 1):
        out = "".join(label for d, label in rules if i % d == 0)
        result.append(out or str(i))
    return result
```

Додавання нового правила – просто елемент у списку; жодної `if/elif` гілки змінювати не треба.

## Detailed explanation

TODO

## Examples

TODO

## Solution

TODO

## Complexity

TODO

## Edge cases

TODO

## Tests

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
