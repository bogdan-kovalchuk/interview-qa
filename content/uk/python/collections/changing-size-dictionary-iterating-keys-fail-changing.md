---
id: py-coll-0010
title: "Чому зміна розміру словника під час ітерації його keys може завершитися помилкою, тоді як зміна value наявного key часто допустима?"
description: "Ітерація по словнику фіксує його розмір (кількість key-слотів); додавання або видалення ключа змінює цей розмір і викликає RuntimeError: dictionary changed size during iteration."
track: python
section: collections
level: senior
type: pitfall
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-library-stdtypes
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-collections
    title: "Python 3.14: Library/collections"
    url: https://docs.python.org/3.14/library/collections.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-howto-sorting
    title: "Python 3.14: Howto/sorting"
    url: https://docs.python.org/3.14/howto/sorting.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
---

## Short answer

**Ітерація по словнику фіксує його розмір (кількість key-слотів); додавання або видалення ключа змінює цей розмір і викликає `RuntimeError: dictionary changed size during iteration`.**[^py314-library-stdtypes] Зміна значення наявного ключа не змінює розмір таблиці, тому не порушує ітерацію. Безпечний патерн – ітерувати копію ключів: `for k in list(d):`.

## Detailed explanation

Перевірка розміру – це runtime guard у самому C-рівні реалізації `dict`: ітератор словника
запам'ятовує кількість заповнених слотів (`ma_used`) на момент створення ітератора і звіряє її з
поточним значенням при кожному виклику `__next__`. Якщо лічильники розходяться, CPython одразу
піднімає `RuntimeError`, не чекаючи, поки цикл дійде до пошкодженого стану.[^py314-library-stdtypes]
Це захисний механізм реалізації, а не гарантія мови: специфікація Python лише каже, що зміна
розміру словника під час ітерації – undefined behavior, і те, що CPython ловить це надійно, –
деталь конкретного інтерпретатора.

Зміна значення наявного ключа проходить повз цю перевірку, бо оновлення value не додає й не
видаляє слот у таблиці – кількість заповнених слотів (`ma_used`) залишається тією самою, лише сам
вміст слоту перезаписується.

Пастка в тому, що видалення ключа з подальшим додаванням іншого ключа в тому самому циклі теж
може випадково зберегти той самий `ma_used` і не викликати помилку, але при цьому таблиця може
бути перехешована (resize), і поведінка ітерації після цього офіційно не визначена – відсутність
винятку тут не означає коректність.

`dict.keys()`, `dict.values()` і `dict.items()` – це тонкі view-обгортки над тим самим табличним
станом, тому їхні ітератори підпадають під те саме правило.

Безпечні альтернативи, крім `for k in list(d):` – будувати новий словник через dict comprehension
(`{k: f(v) for k, v in d.items()}`) замість мутації під час обходу, або накопичувати зміни в
окремому списку операцій і застосувати їх після завершення циклу.

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
