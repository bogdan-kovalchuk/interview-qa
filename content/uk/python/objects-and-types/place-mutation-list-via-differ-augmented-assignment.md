---
id: py-objtypes-0006
title: "Чим in-place mutation списку через `+=` відрізняється від augmented assignment для immutable tuple?"
description: "Для list оператор += викликає __iadd__ і змінює список in-place (той самий id); для tuple методу __iadd__ немає, тому спрацьовує fallback на __add__, який створює новий tuple."
track: python
section: objects-and-types
level: middle
type: comparison
tags: []
status: published
updated: 2026-09-27
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-reference-datamodel
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-stdtypes
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-copy
    title: "Python 3.14: Library/copy"
    url: https://docs.python.org/3.14/library/copy.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-typing
    title: "Python 3.14: Library/typing"
    url: https://docs.python.org/3.14/library/typing.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
---

## Short answer

**Для `list` оператор `+=` викликає `__iadd__` і змінює список in-place (той самий `id`); для `tuple` методу `__iadd__` немає, тому спрацьовує fallback на `__add__`, який створює новий tuple.**[^py314-reference-datamodel] Після `t += (3,)` для tuple ім'я `t` переприв'язується до нового об'єкта з іншим `id()`. Для списку `lst += [3]` той самий об'єкт розширюється елементами.

## Detailed explanation

Оператор augmented assignment `x += y` у Python працює через протокол спеціальних методів, де ключову роль відіграє наявність методу `__iadd__`.[^py314-reference-datamodel]

Для типів із можливістю модифікації (як-от `list`) реалізовано метод `__iadd__`, який виконує in-place мутацію внутрішнього масиву покажчиків і повертає `self`. При цьому операція `lst += iterable` еквівалентна виклику `lst.extend(iterable)` – правим операндом може бути будь-який iterable, а не лише список. Змінна зліва після цього переприв'язується до того самого об'єкта, тому його `id()` не змінюється, а всі інші змінні, що посилалися на цей список, бачать зміни.

Натомість immutable типи (як-от `tuple`) не реалізують метод `__iadd__`, щоб гарантувати незмінність об'єкта після створення.[^py314-library-stdtypes] Коли `__iadd__` відсутній, інтерпретатор переходить до звичайного додавання `x = x + y`, викликаючи `tuple.__add__`. Цей метод вимагає, щоб правий операнд був виключно іншим `tuple`, виділяє пам'ять під новий об'єкт у купі та копіює туди елементи обох кортежів. Ім'я змінної переприв'язується до нового кортежу, тоді як початковий кортеж залишається незмінним.

Окремий тонкий нюанс виникає під час спроби виконати `+=` для mutable елемента всередині кортежу, наприклад `nested[0] += [3]`. Операція `+=` виконується у два кроки: спочатку викликається `__iadd__` списку, який успішно змінює його вміст in-place, але потім виконується збереження результату назад за індексом у кортеж, що викликає `TypeError`, оскільки кортеж забороняє зміну елементів за індексом.

Приклад, що демонструє різницю поведінки та граничний випадок із вкладеним списком:

```python
# List: in-place mutation via __iadd__ (same object ID)
lst1 = [1, 2]
lst2 = lst1
lst1 += [3, 4]
print(lst1 is lst2)  # True, both references see the mutation

# Tuple: creates a new object via __add__ fallback (different ID)
tup1 = (1, 2)
tup2 = tup1
tup1 += (3, 4)
print(tup1 is tup2)  # False, tup1 rebound to a newly created tuple

# Subtle pitfall: mutating a list inside a tuple via +=
nested = ([1, 2],)
try:
    nested[0] += [3]
except TypeError:
    print(nested)  # ([1, 2, 3],) - in-place mutation succeeded before assignment failed
```

**Типові помилки та практичні наслідки:**
- очікувати, що `t += (x,)` модифікує наявний кортеж in-place, тоді як у циклах це спричиняє квадратичну складність через створення нових об'єктів;
- передавати список у функцію та використовувати `+=` замість `+`, ненавмисно модифікуючи оригінальний список зусиллями виклику;
- забувати, що правий операнд для `list += ...` може бути будь-яким iterable (наприклад, рядком, де `lst += "ab"` додасть окремі символи `['a', 'b']`, а не рядок цілком);
- потрапляти у пастку `nested_tuple[0] += [item]`, коли виникає `TypeError`, але список усередині кортежу насправді змінюється.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
