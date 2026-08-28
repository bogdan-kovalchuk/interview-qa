---
id: py-syntax-0001
title: "Що повертають оператори `and` та `or`: обов’язково `bool` чи один зі своїх operands, і як працює short-circuit evaluation?"
description: "and і or повертають один зі своїх operands, а не обов'язково bool."
track: python
section: syntax-and-control-flow
level: middle
type: mechanism
tags: [and, or, bool]
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
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/coding.md#L3-L20
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`and` і `or` повертають один зі своїх operands, а не обов'язково `bool`.**[^py314-reference-expressions] `x and y` обчислює `x`: якщо `x` falsy – повертає його, інакше повертає `y`. `x or y` обчислює `x`: якщо `x` truthy – повертає його, інакше повертає `y`. Short-circuit означає, що другий operand не обчислюється, якщо результат уже визначений першим.

## Detailed explanation

`and` і `or` – це не булеві оператори в сенсі «повертають `True`/`False`», а оператори вибору: вони
повертають **той операнд**, який визначив результат, у його первісному
вигляді.[^py314-reference-expressions]

Правило одне на обидва. `x or y` обчислює `x`; якщо він truthy, це і є результат, і `y` не
обчислюється взагалі. `x and y` обчислює `x`; якщо він falsy, результат – це `x`, і `y` знову не
обчислюється.

```python
0 or 'default'      # 'default' - the str, not True
'a' or 'b'          # 'a'       - the first truthy operand
[] and crash()      # []        - crash() is never called
1 and 2             # 2         - the last operand, because 1 is truthy
```

Truthiness визначає сам об'єкт через `__bool__`, а за його відсутності через `__len__`; тому
результат залежить від типу операнда, а не від якогось універсального
приведення.[^py314-reference-simple-stmts]

Short-circuit – це не оптимізація, а гарантія мови, і на неї можна спиратися. Саме тому працює
ідіома `obj is not None and obj.value > 0`: якщо перша частина хибна, атрибут не читається, і
`AttributeError` не виникає.

**Практичні наслідки, які варто називати:**
- значення за замовчуванням через `or` замінює будь-яке falsy значення, не лише `None` – класична
  пастка з `0` і `''`;
- ланцюжок `a or b or c` повертає перший truthy операнд, а якщо всі falsy – **останній**, а не
  `False`;
- анотувати результат як `bool` неправильно: тип результату – об'єднання типів операндів;
- якщо потрібен саме `bool`, треба сказати це явно: `bool(x or y)`;
- побічні ефекти в другому операнді можуть не статися – це і є суть short-circuit, і на цьому
  будують охоронні перевірки.

Окремо варто відрізняти `and`/`or` від `&`/`|`: останні є бітовими операторами, вони не роблять
short-circuit і для звичайних об'єктів означають зовсім інше.[^py314-reference-expressions]

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
