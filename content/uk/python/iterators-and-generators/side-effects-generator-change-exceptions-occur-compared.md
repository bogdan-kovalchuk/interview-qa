---
id: py-itergen-0008
title: "Як side effects у generator змінюють момент виникнення exceptions порівняно з eager list construction?"
description: "Тіло generator виконується під час споживання, тому помилка з’являється пізніше, а частина side effects може ніколи не відбутися."
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
  - source_id: py314-reference-expressions-generator-iterator-methods
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#generator-iterator-methods
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: методи generator-iterator (__next__, send, throw, close) і їхня поведінка після завершення."
  - source_id: py314-reference-expressions-generator-expressions
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#generator-expressions
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: вираз generator; найлівіший iterable обчислюється одразу."
---

## Short answer

**Тіло generator виконується під час `next()`, тому side effects і винятки з тіла з’являються при споживанні, а не при створенні.**[^py314-reference-expressions-yield-expressions] На відміну від list comprehension, яка будує весь список, перш ніж щось повернути, generator віддає значення по одному, тож результати до помилки вже доступні споживачу. Код після останнього спожитого `yield` не виконується, а `close()` піднімає `GeneratorExit` у точці паузи, тож `finally`-блоки спрацьовують.[^py314-reference-expressions-generator-iterator-methods]

## Detailed explanation

Тіло generator не виконується при створенні, тож його side effects і винятки відкладаються до споживання. Виконання починається з виклику одного з методів generator, а на кожному `yield` тіло призупиняється і зберігає стан.[^py314-reference-expressions-yield-expressions] Щоб побачити різницю, зіставимо eager list comprehension і generator expression з однаковою функцією, яка друкує кожен свій елемент:

```python
def divide(x):
    print("processing", x)            # side effect of each element
    return 10 // x                    # ZeroDivisionError for x == 0

items = [2, 0, 5]

# eager: the whole list is built before anything is returned
try:
    values = [divide(x) for x in items]
except ZeroDivisionError:
    print("eager: no values returned")

# lazy: values come out one by one
gen = (divide(x) for x in items)      # nothing printed yet
print(next(gen))                      # processing 2, then 5
try:
    next(gen)                         # processing 0, then the error
except ZeroDivisionError:
    print("lazy: error after 5 was already returned")
```

В eager-варіанті помилка виникає під час побудови списку. До неї side effects усіх елементів до помилки вже відбулися, але споживач не отримує жодного значення. В lazy-варіанті значення повертаються по одному: `5` уже в споживача, коли з’являється помилка на нулі. Тому помилка в generator може «прийти пізно», а частина роботи не виконується взагалі, якщо споживання зупинити раніше.

Для незавершеного generator діє кілька правил. Код після останнього спожитого `yield` не виконується, бо тіло призупинене. Коли generator знищується до завершення (через нульовий reference count або GC), Python викликає `close()`, і в точці паузи піднімається `GeneratorExit`, тож `finally` виконує cleanup.[^py314-reference-expressions-yield-expressions] Тому ресурс, який має закритися гарантовано, краще закривати явно через `close()`, а не покладатися на час збирання сміття.

Одне уточнення стосується лише генераторного виразу: найлівіший iterable обчислюється одразу. Помилка в ньому з’явиться під час створення виразу, а не при споживанні.[^py314-reference-expressions-generator-expressions]

**Типові помилки:**
- очікувати, що помилка з’явиться одразу при створенні generator, а не при першому `next()`;
- вважати, що side effects усіх елементів відбулися, хоча generator споживано лише частково;
- покладатися на GC, а не на явний `close()`, для cleanup ресурсів.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
