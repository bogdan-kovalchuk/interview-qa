---
id: py-syntax-0006
title: "Як evaluation order впливає на результат chained assignment або unpacking, якщо правий вираз має side effects?"
description: "Права частина обчислюється першою, потім цілі зліва присвоюються зліва направо; тому side effects у правому виразі впливають на всі target."
track: python
section: syntax-and-control-flow
level: senior
type: mechanism
tags: []
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-reference-expressions
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-simple-stmts
    title: "Python 3.14: Reference/simple Stmts"
    url: https://docs.python.org/3.14/reference/simple_stmts.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-compound-stmts
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
---

## Short answer

**Права частина обчислюється першою, потім цілі зліва присвоюються зліва направо; тому side effects у правому виразі впливають на всі target.**[^py314-reference-expressions] Наприклад, при `i, x[i] = 1, 2` (де `i=0, x=[0,1]`) спочатку обчислюється кортеж `(1, 2)`, потім `i` стає `1`, і після цього `x[1]` (вже з новим `i`) стає `2` – результат `x == [0, 2]`.

## Detailed explanation

Присвоєння в Python має два кроки в чітко визначеному порядку: спочатку повністю обчислюється права
частина, потім результат розкладається по цілях зліва **зліва
направо**.[^py314-reference-simple-stmts]

Поки цілі незалежні, цей порядок непомітний. Він стає видимим, коли одна ціль впливає на те, куди
запишеться інша – наприклад, коли ім'я в лівій частині водночас є частиною індексу іншої цілі.

```python
i = 0
x = [0, 1]

i, x[i] = 1, 2
# step 1: the right side becomes the tuple (1, 2)
# step 2: i = 1        <- the name is rebound first
# step 3: x[i] = 2     <- and `i` is already 1 here, so x[1] is written

x    # [0, 2]  - not [2, 1]
```

Якщо поміняти цілі місцями, зміниться і результат, бо запис у список станеться зі старим `i`.

```python
x[i], i = 2, 1
# step 2: x[0] = 2     <- `i` is still 0 here
# step 3: i = 1
```

Chained assignment підпорядковується тому самому правилу: `a = b = expr` обчислює `expr` один раз і
присвоює його цілям зліва направо, тобто спочатку `a`, потім `b`. Це не `a = (b = expr)` – такого
виразу в Python немає.

```python
a = b = []
a.append(1)
b            # [1] - both names refer to the SAME object, evaluated once
```

**Що з цього випливає на практиці:**
- `a, b = b, a` працює саме тому, що права частина обчислюється до першого присвоєння: кортеж уже
  містить старі значення;
- `a = b = []` створює **один** список на два імені, а не два порожні – класична причина «чому мій
  другий список теж змінився»;
- при unpacking із side effects у правій частині всі виклики відбуваються до того, як будь-яка ціль
  отримає значення;
- augmented assignment (`x[i] += 1`) – окремий випадок: він читає, змінює і записує ту саму ціль, і
  індекс обчислюється один раз.[^py314-reference-expressions]

Правило легко звести до одного речення: право обчислюється повністю й один раз, ліво присвоюється по
черзі й уже бачить попередні присвоєння.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
