---
id: py-funcs-0009
title: "Чому присвоєння `items = []` усередині функції не змінює список викликача, а `items.append(value)` може його змінити?"
description: "items = [] створює нове локальне зв’язування імені, тоді як items.append(value) змінює той самий об’єкт, на який посилаються і локальний параметр, і змінна викликача."
track: python
section: functions-and-scope
level: middle
type: comparison
tags: [items, items-append-value]
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
  - source_id: py314-faq-programming-why-did-changing-list-y-also-change-list-x
    title: "Python 3.14: Faq/programming"
    url: https://docs.python.org/3.14/faq/programming.html#why-did-changing-list-y-also-change-list-x
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: зміна змінюваного об’єкта видна через усі імена, що на нього посилаються; присвоєння імені лише переприв’язує це ім’я."
  - source_id: py314-reference-simple-stmts-augmented-assignment
    title: "Python 3.14: Reference/simple Stmts"
    url: https://docs.python.org/3.14/reference/simple_stmts.html#augmented-assignment-statements
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: розширене присвоєння (+=) виконується на місці, коли це можливо, і змінює старий об’єкт замість створення нового."
---

## Short answer

**`items = []` створює нове локальне зв’язування імені, тоді як `items.append(value)` змінює той самий об’єкт, на який посилаються і локальний параметр, і змінна викликача.**[^py314-faq-programming-how-do-i-write-a-function-with-output] Присвоєння лише переприв’язує локальне ім’я `items` до нового об’єкта і не впливає на оригінал. Метод `.append()` змінює сам об’єкт, а не ім’я; оскільки викликач і функція мають посилання на один список, зміна видима обом.

## Detailed explanation

Python передає аргументи присвоєнням: параметр зв’язується з тим самим об’єктом, який передав викликач. Ім’я параметра при цьому не є псевдонімом імені у викликача: два зв’язування незалежні, і переприв’язання одного не змінює другого. FAQ описує це як передачу аргументів присвоєнням, без call-by-reference.[^py314-faq-programming-how-do-i-write-a-function-with-output]

Наступний приклад показує обидві ситуації:

```python
def rebind(items):
    items = ['new']            # the local name now refers to another list
    return items

def mutate(items):
    items.append('new')        # changes the list that the caller also refers to

data = ['old']
rebind(data)
print(data)                    # ['old']: the caller's name still refers to the original list
mutate(data)
print(data)                    # ['old', 'new']: the same list object was changed
```

Правило таке: переприв’язання імені (`items = ...`) змінює лише локальне ім’я, а зміна самого об’єкта (`items.append(...)`, `items[0] = ...`) видна через усі імена, що посилаються на нього.[^py314-faq-programming-why-did-changing-list-y-also-change-list-x]

Обережно з `+=`. Для списку `items += [value]` виконується на місці: об’єкт змінюється, і викликач бачить зміну. `items = items + [value]` створює новий список і лишає список викликача без змін. Документація описує розширене присвоєння так: коли це можливо, операція виконується на місці, і старий об’єкт змінюється замість створення нового.[^py314-reference-simple-stmts-augmented-assignment]

**Типові помилки:**
- очікувати, що присвоєння `items = ...` усередині функції змінить список викликача;
- писати `items += [value]` і не враховувати, що для списку це зміна на місці, яку бачить викликач;
- змінювати аргумент без згадки про це в назві чи документації функції, через що викликач не очікує побічного ефекту.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
