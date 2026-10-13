---
id: py-itergen-0017
title: "У якому scope обчислюється outermost iterable generator expression і коли обчислюються решта його clauses?"
description: "Outermost iterable обчислюється негайно в enclosing scope; усі інші вирази (output expression, наступні for/if) обчислюються ліниво в окремому implicit nested scope."
track: python
section: iterators-and-generators
level: senior
type: mechanism
tags: []
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-library-stdtypes-iterator-types
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html#iterator-types
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-expressions-yield-expressions
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#yield-expressions
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-datamodel-object-iter
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__iter__
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-expressions-generator-expressions
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#generator-expressions
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14, розділ generator expressions: найлівіший iterable обчислюється одразу, решта виразів обчислюється лениво, як у generator."
  - source_id: py314-reference-expressions-displays-for-lists-sets-and-dictionaries
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#displays-for-lists-sets-and-dictionaries
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14, розділ displays: comprehension виконується в implicitly nested scope, а змінні target list не просочуються в enclosing scope."
  - source_id: py314-reference-executionmodel-resolution-of-names
    title: "Python 3.14: Reference/executionmodel"
    url: https://docs.python.org/3.14/reference/executionmodel.html#resolution-of-names
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14, розділ resolution of names: область імен класу не поширюється на comprehensions і generator expressions."
---

## Short answer

**Outermost iterable обчислюється негайно в enclosing scope; усі інші вирази (output expression, наступні `for` і `if`) обчислюються ліниво в implicitly nested scope.**[^py314-reference-expressions-generator-expressions] Тому `NameError` або `TypeError` для outermost iterable виникає під час створення generator expression, а помилки у внутрішніх виразах – лише під час ітерації. Змінні target list не просочуються у зовнішню область.[^py314-reference-expressions-displays-for-lists-sets-and-dictionaries]

## Detailed explanation

Генераторний вираз має два моменти: створення і виконання. У момент створення Python обчислює outermost iterable в enclosing scope і передає його як аргумент у implicitly nested scope. Решта виразів, тобто output expression та наступні `for` і `if`, виконується пізніше.[^py314-reference-expressions-displays-for-lists-sets-and-dictionaries] Ці вирази обчислюються ліниво, як у звичайного generator, тобто тоді, коли iterator просять віддати значення.[^py314-reference-expressions-generator-expressions] Тому `(x for x in 5)` падає одразу з `TypeError`, а помилка в output expression з’являється лише при першому `next()`.

Найлегше побачити наслідки в class body, бо там область імен класу сама по собі обмежена. Outermost iterable бачить імена класу, а output expression – ні, бо область імен класу не поширюється на generator expressions.[^py314-reference-executionmodel-resolution-of-names] У прикладі `ok` працює, бо `names` обчислюється в class scope, а `gen` падає лише під час ітерації:

```python
class Config:
    names = ['a', 'b']
    prefix = '>'
    ok = [n for n in names]              # outermost iterable: class scope, works
    gen = (prefix + n for n in names)    # prefix is looked up in the nested scope

g = Config.gen                           # no error yet: creation succeeded
# next(g)                                # NameError: name 'prefix' is not defined
# (x for x in 5)                         # TypeError at creation: 'int' object is not iterable
```

Змінні target list не просочуються в enclosing scope: після генераторного виразу імені `x` у зовнішній області немає.[^py314-reference-expressions-displays-for-lists-sets-and-dictionaries]

**Типові помилки:**
- вважати, що помилка в output expression з’явиться одразу, під час створення generator expression;
- звертатися в class body до імені класу в output expression і очікувати, що його буде знайдено: NameError з’явиться під час ітерації;
- шукати змінну target list після генераторного виразу: вона не просочується в зовнішню область.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
