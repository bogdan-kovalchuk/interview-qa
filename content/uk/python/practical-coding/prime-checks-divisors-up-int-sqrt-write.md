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
updated: 2026-10-13
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-tutorial-controlflow-the-range-function
    title: "Python 3.14: Tutorial/control flow, The range() Function"
    url: https://docs.python.org/3.14/tutorial/controlflow.html#the-range-function
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: range(start, stop) не включає stop. Не описує тестування чи мутаційне тестування."
  - source_id: py314-library-math-math-nan
    title: "Python 3.14: Library/math, math.nan"
    url: https://docs.python.org/3.14/library/math.html#math.nan
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14, примітка CPython: неприпустимі операції, наприклад sqrt(-1.0), дають ValueError. Це деталь реалізації CPython; не описує інші функції окремо."
  - source_id: py314-library-math-math-isqrt
    title: "Python 3.14: Library/math, math.isqrt"
    url: https://docs.python.org/3.14/library/math.html#math.isqrt
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: math.isqrt(n) повертає floor точного квадратного кореня цілого невід’ємного n. Не описує math.sqrt."
---

## Short answer

**Три групи тестів: base case `n < 2`, perfect square (вбиває мутацію `<` vs `<=`) і звичайні prime/composite.** Для мутації `is_prime(4)`: `int(sqrt(4)) == 2`; якщо межа виключена, `range(2, r)` не включає `r`,[^py314-tutorial-controlflow-the-range-function] діапазон порожній і мутант повертає `True`, тоді як правильний код (`range(2, r + 1)`) знаходить `4 % 2 == 0` і повертає `False`. Для `n < 2`: `is_prime(0)`, `is_prime(1)`, `is_prime(-7)` -> `False`. Додатково: `is_prime(9)` -> `False`, `is_prime(2)` -> `True`.

## Detailed explanation

Мутант із `<` замість `<=` у межі циклу відрізняється від правильної функції лише тоді, коли найменший дільник дорівнює `int(sqrt(n))`. Це складені числа `4`, `6`, `8`, `9`, `15`, `25`, `35`, `49` і подібні; серед них квадрати `4`, `9`, `25`, `49`. Для `n = 4` правильна функція знаходить дільник `2`, а мутант його не перевіряє і повертає `True`. Прості числа мутант не ловить, бо для них обидві функції повертають `True`:

```python
from math import sqrt


def is_prime(n):
    if n < 2:
        return False
    for d in range(2, int(sqrt(n)) + 1):
        if n % d == 0:
            return False
    return True


def is_prime_mutant(n):  # mutant: the inclusive upper bound became exclusive
    if n < 2:
        return False
    for d in range(2, int(sqrt(n))):
        if n % d == 0:
            return False
    return True


print(is_prime(4), is_prime_mutant(4))  # False True: the test on 4 kills the mutant
print(is_prime(6), is_prime_mutant(6))  # False True
print(is_prime(7), is_prime_mutant(7))  # True True: a prime does not kill it
```

Причина в тому, що `range(2, r)` не включає `r`.[^py314-tutorial-controlflow-the-range-function] При `r = 2` діапазон порожній, тож тест на `4` (і на `9`, де `r = 3`) має виявити саме цю помилку.

Гілка `n < 2` потрібна окремо. Для `0` і `1` без неї діапазон порожній, і функція повертає `True`. Для `-7` без guard `math.sqrt` піднімає `ValueError`: CPython дає `ValueError` для неприпустимих операцій, наприклад `sqrt(-1.0)`.[^py314-library-math-math-nan] Тому тест на `-7` перевіряє саме guard з очікуваним `False`. Для еталона в тесті можна використати `math.isqrt(n)`, який повертає floor точного квадратного кореня цілого числа.[^py314-library-math-math-isqrt]

Набір тестів має три групи: (1) `n < 2`: `0`, `1`, `-7` дають `False`; (2) числа з найменшим дільником `int(sqrt(n))`, зокрема квадрати: `4`, `9`, `15`, `25`, `49` дають `False`, а мутант на них повертає `True`; (3) звичайні числа, на яких мутант поводиться як правильна функція: `2` і `97` дають `True`, `91` (найменший дільник `7` менший за `int(sqrt(91)) = 9`) дає `False`. Кожна група перевіряє окрему гілку: guard, межу циклу і основний шлях.

**Типові помилки:**
- тестувати лише звичайні prime і composite: мутант проходить на `7` і `91`;
- не тестувати `n < 2`: `0` і `1` дають `True`, і ніхто не помітить помилку;
- не тестувати від’ємні числа: без guard тест упаде з `ValueError`, а не з логічною помилкою.

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
