---
id: py-funcs-0012
title: "Чому функція може отримати `UnboundLocalError` під час читання глобального `x`, якщо нижче в її тілі є присвоєння `x = ...`?"
description: "Python визначає ім’я як локальне, якщо будь-де в тілі функції є операція зв’язування, тому всі звертання до цього імені в тілі трактуються як до локального."
track: python
section: functions-and-scope
level: middle
type: pitfall
tags: [unboundlocalerror]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  en: 2
applies_to:
  - product: "CPython"
    version: null
anki:
  export: true
sources:
  - source_id: py314-reference-executionmodel-resolution-of-names
    title: "Python 3.14: Reference/executionmodel"
    url: https://docs.python.org/3.14/reference/executionmodel.html#resolution-of-names
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-faq-programming-why-am-i-getting-an-unboundlocalerror
    title: "Python 3.14: Faq/programming"
    url: https://docs.python.org/3.14/faq/programming.html#why-am-i-getting-an-unboundlocalerror-when-the-variable-has-a-value
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
---

## Short answer

**Python визначає ім’я в тілі функції як локальне, якщо будь-де в ньому є операція зв’язування (присвоєння, `for`, `import` тощо), і тоді всі звертання до цього імені в тілі трактуються як до локального.**[^py314-reference-executionmodel-resolution-of-names] Якщо читання відбувається до першого присвоєння, локальна змінна ще не має значення, і виникає `UnboundLocalError`.[^py314-faq-programming-why-am-i-getting-an-unboundlocalerror] Щоб у такій функції читати глобальний `x`, оголошують `global x`; тоді всі звертання до `x` у тілі стосуються модульного імені.[^py314-reference-executionmodel-resolution-of-names]

## Detailed explanation

Python визначає локальні імена за текстом блоку, а не за порядком виконання рядків: локальні змінні блоку визначаються скануванням усього тексту блоку на операції зв’язування імен.[^py314-reference-executionmodel-resolution-of-names] Якщо в блоці є операція зв’язування імені, то всі звертання до цього імені в блоці стосуються локального імені, навіть ті, що стоять раніше за присвоєння. До операцій зв’язування належать не лише присвоєння, а й `for`, `import`, `with ... as`, `except ... as` і параметри функції.

Тому читання `x` до присвоєння не переходить до глобального `x`. Локальне ім’я вже існує в тілі, але ще не прив’язане до значення, і Python піднімає `UnboundLocalError`, підклас `NameError`.[^py314-reference-executionmodel-resolution-of-names] У CPython 3.11 і новіших текст повідомлення такий: `cannot access local variable 'x' where it is not associated with a value`; FAQ наводить той самий текст.[^py314-faq-programming-why-am-i-getting-an-unboundlocalerror]

Три функції з одним модульним `x` показують межі правила:

```python
x = 10

def read_then_assign():
    print(x)   # raises UnboundLocalError: the assignment below makes x local to the whole body
    x = 20

def read_only():
    print(x)   # 10: no binding in this body, so x is looked up as a global

def with_global():
    global x
    print(x)   # 10: the global declaration applies to the whole body
    x = 20     # rebinds the module-level x
```

Щоб у функції з присвоєнням читати глобальний `x`, оголошують `global x`. Декларація має стояти раніше за всі звертання до імені в блоці. Після неї всі звертання, включно з `x = 20`, стосуються модульного `x`, а не створюють локальне ім’я.[^py314-reference-executionmodel-resolution-of-names]

**Типові помилки:**
- думати, що порядок рядків важливий: достатньо присвоєння будь-де в тілі, щоб ім’я стало локальним для всього тіла;
- вважати, що глобального `x` нібито немає: він є, але функція звертається до локального імені, якому ще не присвоєно значення;
- додавати `global x` як «виправлення» для читання: декларація змінює і присвоєння в тілі, а не лише читання.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
