---
id: py-syntax-0014
title: "Як chained comparison `a < b < c` відрізняється від `a < b and b < c` щодо кількості обчислень середнього operand?"
description: "У chained comparison a < b < c середній операнд b обчислюється лише один раз, тоді як у a < b and b < c – двічі (якщо a < b істинне)."
track: python
section: syntax-and-control-flow
level: middle
type: comparison
tags: [a-lt-b-lt-c, a-lt-b-and-b-lt-c]
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

**У chained comparison `a < b < c` середній операнд `b` обчислюється лише один раз, тоді як у `a < b and b < c` – двічі (якщо `a < b` істинне).**[^py314-reference-expressions] Обидва варіанти семантично еквівалентні за результатом і short-circuit поведінкою (якщо `a < b` хибне, `c` не обчислюється в жодному випадку), але chained comparison уникає повторного обчислення `b`, що важливо, коли `b` – вираз із side effects або дорогим обчисленням.

## Detailed explanation

Chained comparison – це не скорочення для `and`, а окреме правило граматики. Вираз `a < b < c`
розгортається в `a < b and b < c` з однією поправкою: середній операнд обчислюється **один раз**, і
його результат використовується в обох порівняннях.[^py314-reference-expressions]

Поки операнди – прості імена, різниці немає. Вона з'являється, коли середній операнд є викликом
функції: у формі з `and` виклик відбувається двічі.

```python
def value():
    print('called')
    return 5

1 < value() < 10      # prints 'called' once
1 < value() and value() < 10   # prints 'called' twice - two different calls
```

Це має значення не лише для швидкості. Якщо функція має побічний ефект або повертає щось нове при
кожному виклику – читає з ітератора, бере наступний елемент черги, звертається до мережі – форма з
`and` порівнює **різні** значення, і результат може бути логічно неправильним.

Short-circuit працює однаково в обох формах: якщо перше порівняння хибне, друге не обчислюється, і
`c` не торкається взагалі.[^py314-reference-expressions] Тобто ланцюжок нічого не втрачає порівняно з
`and`.

**Що ще варто знати про ланцюжки:**
- довжина не обмежена трьома: `0 <= i < j < len(items)` – коректний вираз;
- оператори можна змішувати, включно з `is`, `in` і `!=`: `a is not None != b` розгортається так
  само, і це часте джерело плутанини – читається не так, як здається;
- `a < b > c` синтаксично валідний, але майже завжди означає помилку в намірі;
- ланцюжок не еквівалентний порівнянню кортежів: `(a, b) < (c, d)` – це лексикографічне порівняння,
  зовсім інша операція.

Практичний висновок простий: ланцюжок читабельніший і безпечніший там, де середній операнд не є
простим іменем, і саме тому `0 <= index < len(items)` – канонічна форма перевірки меж, а не
стилістична забаганка.[^py314-reference-simple-stmts]

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
