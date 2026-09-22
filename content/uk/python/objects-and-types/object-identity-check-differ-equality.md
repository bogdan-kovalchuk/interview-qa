---
id: py-objtypes-0001
title: "Чим перевірка object identity через `is` відрізняється від equality через `==`?"
description: "is перевіряє ідентичність об'єктів (той самий об'єкт у пам'яті), а == перевіряє рівність значень."
track: python
section: objects-and-types
level: middle
type: comparison
tags: [is]
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
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/data_types.md#L587-L609
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`is` перевіряє ідентичність об'єктів (той самий об'єкт у пам'яті), а `==` перевіряє рівність значень.**[^py314-reference-datamodel] Оператор `is` порівнює `id()` об'єктів і не перевантажується. Оператор `==` викликає метод `__eq__()`; якщо клас не визначає власний `__eq__`, типовий `object.__eq__` повертає результат `is`.

## Detailed explanation

Оператор `is` визначає, чи посилаються дві змінні на один і той самий об'єкт у пам'яті, тоді як оператор `==` перевіряє еквівалентентність значень цих об'єктів.[^py314-reference-datamodel]

У CPython кожен об'єкт має незмінну ідентичність, тип і значення. Функція `id()` повертає ціле число, що відповідає адресі об'єкта в оперативній пам'яті. Оператор `is` безпосередньо порівнює покажчики на об'єкти на рівні C-структур. Ця операція виконується за $O(1)$, не викликає методів Python і не може бути перевантажена користувацьким кодом.

На противагу цьому, оператор `==` делегує порівняння магічному методу `__eq__()` лівого операнда. Якщо метод повертає `NotImplemented`, інтерпретатор пробує викликати `__eq__()` правого операнда. Якщо обидва операнди повертають `NotImplemented`, застосовується базове порівняння з `object.__eq__`, яке перевіряє ідентичність через `is`.[^py314-library-stdtypes] Користувацькі класи можуть вільно перевизначати `__eq__` для порівняння атрибутів або реалізації власної бізнес-логіки.

Приклад, що ілюструє різницю між ідентичністю та рівністю значень:

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)  # True: values are equal
print(a is b)  # False: distinct objects in memory with different id()
print(a is c)  # True: c references the exact same object as a

print(id(a) == id(b))  # False: id() comparison matches the result of `is`
```

**Типові помилки та практичні наслідки:**
- порівняння чисел або рядків через `is` замість `==`: через оптимізації interning у CPython таке порівняння може тимчасово давати `True`, але мова цього не гарантує;
- припущення, що `==` завжди повертає `bool`: об'єкти спеціальних бібліотек можуть повертати складні структури або викликати винятки;
- ігнорування вартості порівняння: `is` завжди виконується миттєво, тоді як `==` для глибоких вкладених колекцій рекурсивно обходить усі елементи.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
