---
id: py-syntax-0012
title: "У якому порядку Python обчислює function expression, positional arguments і keyword arguments у виклику, якщо вони мають side effects?"
description: "Python обчислює callable-вираз першим, потім усі argument expressions до початку виклику, причому *expr обчислюється перед keyword arguments, навіть якщо стоїть після них у коді."
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

**Python обчислює callable-вираз першим, потім усі argument expressions до початку виклику, причому `*expr` обчислюється перед keyword arguments, навіть якщо стоїть після них у коді.**[^py314-reference-expressions] Загальний порядок: primary expression -> позиційні аргументи (зліва направо) -> `*unpack` -> keyword arguments -> `**unpack`. Це гарантія мови (left-to-right evaluation), а не деталь реалізації.

## Detailed explanation

Виклик у Python – це звичайний вираз, і його частини обчислюються за фіксованим порядком, який
описаний у мові, а не залишений реалізації. Спочатку обчислюється сам callable, потім аргументи, і
лише після цього відбувається виклик.[^py314-reference-expressions]

Те, що callable обчислюється **першим**, помітно, коли він сам є виразом із побічним ефектом:
`get_handler()(compute())` викличе `get_handler` до `compute`, хоча в тексті вони поруч.

Аргументи обчислюються зліва направо, і це стосується всіх форм разом – позиційних, `*`-розпакування,
іменованих і `**`-розпакування.

```python
def trace(name):
    print(name)
    return name

f(trace('a'), trace('b'), key=trace('c'))
# prints a, b, c - strictly left to right
```

Тонкість, яку легко проґавити: `*expr` обчислюється разом із позиційними аргументами, тобто **до**
іменованих – навіть якщо в тексті стоїть після них.

```python
f(key=trace('kw'), *trace_iterable('star'))
# prints star, then kw - the *unpacking goes first despite the written order
```

Саме тому такий запис збиває з пантелику, і його вважають поганим стилем: візуальний порядок не
збігається з порядком обчислення. Писати `*args` перед іменованими аргументами – простий спосіб цього
уникнути.

**Загальний порядок, який варто пам'ятати:**
- вираз, що дає callable;
- позиційні аргументи, зліва направо;
- `*expr` розпакування;
- іменовані аргументи, зліва направо;
- `**expr` розпакування;
- і лише потім – сам виклик, зі зв'язуванням параметрів.

Це гарантія мови, а не деталь CPython, тож на неї можна спиратися в переносимому коді. Але спиратися
варто рідко: код, коректність якого залежить від порядку обчислення аргументів, важко читати – краще
обчислити значення в окремих рядках і передати вже готові.[^py314-reference-simple-stmts]

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
