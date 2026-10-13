---
id: py-funcs-0001
title: "Які різні обмеження на спосіб передавання аргументів задають символи `/` і `*` у сигнатурі `def f(a, /, b, *, c): ...`?"
description: "/ розділяє positional-only та решту параметрів, а * розділяє звичайні та keyword-only параметри."
track: python
section: functions-and-scope
level: middle
type: comparison
tags: [def-f-a-b-c]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-reference-compound-stmts-function-definitions
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#function-definitions
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-expressions-calls
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#calls
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-tutorial-controlflow-special-parameters
    title: "Python 3.14: Tutorial/control flow, special parameters"
    url: https://docs.python.org/3.14/tutorial/controlflow.html#special-parameters
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: розділ про positional-only (/) та keyword-only (*) параметри, з прикладами TypeError."
---

## Short answer

**`/` розділяє positional-only та решту параметрів, а `*` розділяє звичайні та keyword-only параметри.**[^py314-reference-compound-stmts-function-definitions] Параметр `a` (ліворуч від `/`) приймається лише позиційно – виклик `f(a=1)` дасть `TypeError`.[^py314-tutorial-controlflow-special-parameters] Параметр `b` (між `/` і `*`) приймається обома способами. Параметр `c` (праворуч від `*`) приймається лише як keyword – виклик `f(1, 2, 3)` дасть `TypeError`, бо третій позиційний аргумент не має слота.[^py314-reference-expressions-calls]

## Detailed explanation

Символи `/` і `*` не є параметрами. Це межі в списку параметрів, які задають, як саме можна передати кожен параметр: лише позиційно, будь-яким способом або лише за іменем. Усе, що стоїть до `/`, є positional-only. Усе, що стоїть після `*`, є keyword-only. Параметри між ними приймаються і позиційно, і за іменем. Позначка `/` з’явилася в Python 3.8.[^py314-reference-compound-stmts-function-definitions]

Для `def f(a, /, b, *, c): ...` це означає таке. Параметр `a` не можна передати ключем, тому `f(a=1, b=2, c=3)` дає `TypeError`.[^py314-tutorial-controlflow-special-parameters] Параметр `b` приймає обидва способи. Параметр `c` можна передати лише ключем, тому `f(1, 2, 3)` дає `TypeError`: після `a` і `b` немає слота для третього позиційного аргумента, а `c` позиційно не приймається.[^py314-reference-expressions-calls]

Приклад перевіряє кожне правило; коментарі показують результат:

```python
def f(a, /, b, *, c):
    return a, b, c

print(f(1, 2, c=3))      # (1, 2, 3): a and b by position, c by keyword
print(f(1, b=2, c=3))    # (1, 2, 3): b may also be passed by keyword

try:
    f(a=1, b=2, c=3)     # TypeError: a is positional-only
except TypeError:
    print('TypeError')

try:
    f(1, 2, 3)           # TypeError: c is keyword-only, the third positional argument has no slot
except TypeError:
    print('TypeError')
```

Обмеження мають практичне значення для API. Параметр, який стає keyword-only, перестає приймати позиційні аргументи, тож старі виклики можуть зламатися. Якщо функція була `def f(a, b)`, а стала `def f(a, *, b)`, виклик `f(1, 2)` починає давати `TypeError`, бо другий позиційний аргумент більше не має слота.[^py314-reference-expressions-calls]

**Типові помилки:**
- вважати, що параметр між `/` і `*` можна передати лише позиційно або лише за іменем: він приймається обома способами;
- передавати за іменем параметр ліворуч від `/` і очікувати, що Python знайде його за іменем;
- додати `*` до наявної сигнатури без перевірки старих викликів, які передавали аргументи позиційно.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
