---
id: py-syntax-0013
title: "Чому вираз `-3 ** 2` дає інший результат, ніж `(-3) ** 2`?"
description: "-3"
track: python
section: syntax-and-control-flow
level: middle
type: mechanism
tags: [3-2]
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  en: 2
execution:
  language: python
  standard: null
  toolchain:
    name: cpython
    version: "3.14"
  flags: []
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

**`-3 ** 2` дає `-9`, а `(-3) ** 2` дає `9`, тому що оператор `**` має вищий пріоритет, ніж унарний мінус зліва від нього.**[^py314-reference-expressions] Тобто `-3 ** 2` інтерпретується як `-(3 ** 2)`. Дужки змінюють порядок: спочатку обчислюється `-3`, потім піднесення до степеня.

```text
>>> print(-3 ** 2)
-9
>>> print((-3) ** 2)
9
```

## Detailed explanation

`**` – єдиний оператор у Python, який має вищий пріоритет за унарний мінус **зліва** від себе, але
нижчий за унарний мінус **справа**. Це навмисне правило, а не випадковість граматики, і воно робить
вираз асиметричним.[^py314-reference-expressions]

Ліворуч мінус застосовується до вже обчисленого степеня: `-3 ** 2` розбирається як `-(3 ** 2)`,
тобто спочатку `9`, потім заперечення. Праворуч мінус належить показнику: `2 ** -1` – це `2` у
степені `-1`, і жодних дужок для цього не потрібно.

```python
-3 ** 2       # -(3 ** 2)  = -9
(-3) ** 2     # (-3) * (-3) =  9
2 ** -1       # 0.5 - the unary minus binds tighter on the RIGHT of **
```

Причина такого вибору – математична нотація. У формулі `-x²` мінус традиційно стосується всього
степеня, і мова відтворює саме цю звичку; водночас від'ємний показник треба було зробити зручним без
дужок.

Ще одна асиметрія, про яку легко забути: `**` правоасоціативний. `2 ** 3 ** 2` – це `2 ** (3 ** 2)`,
тобто `512`, а не `64`. Більшість інших бінарних операторів лівоасоціативні.

**Практичні наслідки:**
- у формулах з від'ємною основою дужки обов'язкові: `(-x) ** 2`, інакше знак «випаде» назовні;
- при перенесенні формули з іншої мови варто перевірити її правила – у деяких мовах `-3 ** 2` дає
  `9`;
- вираз із `**` і кількома рівнями краще дужкувати явно навіть там, де правила дозволяють без них:
  правоасоціативність рідко тримають у голові;
- для дробових степенів від'ємної основи результат стає complex, а не помилкою: `(-8) ** (1/3)` – не
  `-2`.

Швидка перевірка в голові: якщо мінус стоїть перед основою і не в дужках, він застосується
**останнім**.[^py314-reference-simple-stmts]

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
