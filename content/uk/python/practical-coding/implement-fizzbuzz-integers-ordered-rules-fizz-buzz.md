---
id: py-prac-0006
title: "Реалізуйте FizzBuzz для integers 1..N з ordered rules `[(3, \"Fizz\"), (5, \"Buzz\")]`, щоб нове правило не вимагало нової branch."
description: "Зберігайте правила як дані й об’єднуйте labels, чиї divisors ділять поточне число."
track: python
section: practical-coding
level: middle
type: coding
tags: [3-fizz-5-buzz]
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  en: 3
execution:
  language: python
  standard: null
  toolchain:
    name: cpython
    version: "3.13.15"
  flags: []
anki:
  export: true
sources:
- source_id: py313-types
  title: 'Python 3.13: Built-in types'
  url: https://docs.python.org/3.13/library/stdtypes.html
  accessed: '2026-10-04'
  kind: official
  version: '3.13'
  applicability: API semantics and language guarantees used by this solution.
- source_id: py313-expressions
  title: 'Python 3.13: Expressions: arithmetic operations'
  url: https://docs.python.org/3.13/reference/expressions.html#binary-arithmetic-operations
  accessed: '2026-10-04'
  kind: official
  version: '3.13'
  applicability: API semantics and language guarantees used by this solution.
---

## Task

Реалізуйте `fizzbuzz(n, rules=None)`, що повертає рядки для чисел від 1 до n. Об’єднуйте всі відповідні labels у порядку правил; без збігів використовуйте саме число.

## Constraints

- n – невід’ємний int, крім bool.
- Правила – скінченний iterable пар із додатним integer divisor та непорожнім string label.
- Хибні типи викликають TypeError, хибні значення – ValueError.
- Порожній набір правил дозволений.

## Short answer

**Зберігайте правила як дані й об’єднуйте labels, чиї divisors ділять поточне число.** Зберігайте порядок правил і використовуйте `str(i)`, коли збігів немає. Перевіряйте конфігурацію до формування результату.

## Detailed explanation

Modulo визначає відповідні правила; об’єднання labels обробляє одночасні збіги без додаткової гілки. Одноразова матеріалізація правил підтримує також one-shot iterables. Перевірка непорожніх labels робить fallback однозначним. [^py313-types] [^py313-expressions]

## Examples

```python
assert fizzbuzz(3) == ["1", "2", "Fizz"]
```

## Solution

```python
def fizzbuzz(n, rules=None):
    if type(n) is not int:
        raise TypeError("n must be int")
    if n < 0:
        raise ValueError("n must be non-negative")
    rules = tuple([(3, "Fizz"), (5, "Buzz")] if rules is None else rules)
    for divisor, label in rules:
        if type(divisor) is not int or not isinstance(label, str):
            raise TypeError("invalid rule type")
        if divisor <= 0 or not label:
            raise ValueError("invalid rule value")
    return ["".join(label for d, label in rules if i % d == 0) or str(i)
            for i in range(1, n + 1)]
```

## Complexity

Для n чисел і r правил виконується O(n*r) перевірок divisibility. Час також включає запис символів результату; пам’ять – O(r) плюс повернуті рядки. Це оцінка за unit-cost integer arithmetic. [^py313-types] [^py313-expressions]

## Edge cases

Перевірте n=0, відсутність правил, одночасні збіги, порядок правил, one-shot правила та хибні divisors.

## Tests

Виконайте після блока Solution із встановленим pytest.

```python
import pytest

assert fizzbuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]
assert fizzbuzz(15)[-1] == "FizzBuzz"
assert fizzbuzz(0) == []
assert fizzbuzz(3, []) == ["1", "2", "3"]
assert fizzbuzz(6, iter([(3, "A"), (2, "B")]))[-1] == "AB"
for rules in ([(0, "A")], [(-1, "A")], [(2, "")]):
    with pytest.raises(ValueError):
        fizzbuzz(1, rules)
with pytest.raises(TypeError):
    fizzbuzz(True)
with pytest.raises(ValueError):
    fizzbuzz(-1)
```

## Evaluation guide

### Expected signals

Додавання правила має вимагати лише нового елемента даних. Нульові divisors потрібно відхилити до modulo.

### Red flags

Implementation пропускає зазначений boundary case або complexity claim не враховує allocated data.

### Level-up follow-up

Як видавати результати потоком замість збирання output?

## Sources

<!-- generated from frontmatter -->
