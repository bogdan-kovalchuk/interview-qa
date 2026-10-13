---
id: py-funcs-0010
title: "Чому модель «Python передає аргументи за посиланням» неточна, і яка модель коректно пояснює одночасно rebinding та mutation параметра?"
description: "Коректна модель – pass by assignment: параметр отримує посилання на той самий об’єкт, але не є alias змінної викликача."
track: python
section: functions-and-scope
level: middle
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
  - source_id: py314-faq-programming-how-do-i-write-a-function-with-output
    title: "Python 3.14: Faq/programming"
    url: https://docs.python.org/3.14/faq/programming.html#how-do-i-write-a-function-with-output-parameters-call-by-reference
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-faq-programming-why-did-changing-list-y-also-change-li
    title: "Python 3.14: Faq/programming"
    url: https://docs.python.org/3.14/faq/programming.html#why-did-changing-list-y-also-change-list-x
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Розділ FAQ: `y = x` не копіює список, а дає друге ім’я тому самому об’єкту, тож mutation видна через обидва імена. Документація Python 3.14."
  - source_id: py314-reference-simple-stmts-assignment-statements
    title: "Python 3.14: Reference/simple Stmts"
    url: https://docs.python.org/3.14/reference/simple_stmts.html#assignment-statements
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Розділ про оператор присвоєння: ім’я без global або nonlocal зв’язується з об’єктом у поточному локальному namespace. Документація Python 3.14."
  - source_id: py314-reference-simple-stmts-augmented-assignment
    title: "Python 3.14: Reference/simple Stmts"
    url: https://docs.python.org/3.14/reference/simple_stmts.html#augmented-assignment-statements
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Розділ про augmented assignment: де можливо, операція виконується in-place, тобто старий об’єкт змінюється замість створення нового. Документація Python 3.14."
---

## Short answer

**Коректна модель – `pass by assignment`: параметр отримує посилання на той самий об’єкт, але не є alias змінної викликача.**[^py314-faq-programming-how-do-i-write-a-function-with-output] Rebinding параметра (`x = new_value`) лише прив’язує локальне ім’я до іншого об’єкта і не впливає на викликача.[^py314-reference-simple-stmts-assignment-statements] Mutation (`x.append(v)`) змінює спільний об’єкт, і це видно обом сторонам.[^py314-faq-programming-why-did-changing-list-y-also-change-li] Модель «pass by reference» не пояснює rebinding, а «pass by value» у сенсі копії об’єкта не пояснює mutation: pass by assignment пояснює обидва випадки.

## Detailed explanation

Pass by assignment означає, що під час виклику кожен параметр зв’язується з тим самим об’єктом, який передано як аргумент, так ніби виконано присвоєння `параметр = аргумент`. Python не копіює об’єкт і не створює alias для змінної викликача: у функції з’являється нове ім’я, яке посилається на той самий об’єкт.[^py314-faq-programming-how-do-i-write-a-function-with-output]

Rebinding – це звичайне присвоєння імені. Рядок `x = [99]` усередині функції прив’язує локальне `x` до нового списку, а ім’я викликача і далі посилається на старий. Для імені, яке не оголошене `global` або `nonlocal`, присвоєння прив’язує його до об’єкта в поточному локальному namespace.[^py314-reference-simple-stmts-assignment-statements]

Mutation – це зміна самого об’єкта, а не імені. `x.append(99)` додає елемент у список, на який посилається й викликач; оскільки обидва імена вказують на один список, зміна видна з обох боків.[^py314-faq-programming-why-did-changing-list-y-also-change-li] Тому модель «pass by reference» тут не працює: у ній параметр був би alias змінної викликача, і присвоєння параметру змінювало б саму змінну, чого в Python немає. Модель «pass by value» у сенсі копії, навпаки, не пояснює, чому викликач бачить mutation.

Приклад показує обидві поведінки на одному списку:

```python
def rebind(x):
    x = [99]          # rebinding: only the local name x changes

def mutate(x):
    x.append(99)      # mutation: the list object the caller also holds changes

a = [1]
rebind(a)
print(a)              # [1]
mutate(a)
print(a)              # [1, 99]
```

Межа моделі – у тому, що означає «той самий об’єкт». Змінювані об’єкти (`list`, `dict`) можна змінити через будь-яке ім’я, що на них посилається. Незмінювані (`int`, `str`, `tuple`) змінити не можна, тому їхнє «оновлення» завжди є rebinding. Оператор `+=` тут не виняток: де можливо, він виконується in-place, тобто для list змінює спільний список, а для int лише прив’язує локальне ім’я до нового значення.[^py314-reference-simple-stmts-augmented-assignment] Тому однаковий рядок `x += ...` у функції має різний ефект залежно від типу.

**Типові помилки:**
- вважати, що присвоєння параметру змінює список викликача: `x = []` усередині функції його не чіпає;
- вважати, що `x += ...` завжди лише rebinding;
- з того, що Python «передає за посиланням», робити висновок, що присвоєнням параметру можна замінити об’єкт викликача.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
