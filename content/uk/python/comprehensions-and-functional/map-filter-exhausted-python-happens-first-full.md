---
id: py-compfn-0006
title: "Чому `map()` і `filter()` у Python 3 можна вичерпати та що станеться після першого повного обходу?"
description: "map() і filter() у Python 3 повертають iterator, а не список, тому після першого повного обходу вони вичерпуються."
track: python
section: comprehensions-and-functional
level: middle
type: mechanism
tags: [map, filter]
status: published
updated: 2026-09-27
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-howto-functional
    title: "Python 3.14: Howto/functional"
    url: https://docs.python.org/3.14/howto/functional.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-itertools
    title: "Python 3.14: Library/itertools"
    url: https://docs.python.org/3.14/library/itertools.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-functools
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-expressions-displays-for-lists-sets-and-dict
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#displays-for-lists-sets-and-dictionaries
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
---

## Short answer

**`map()` і `filter()` у Python 3 повертають iterator, а не список, тому після першого повного обходу вони вичерпуються.**[^py314-howto-functional] Повторний виклик `list()` на тому самому об'єкті дасть порожній список. Якщо дані потрібні багаторазово, слід матеріалізувати їх у `list` або створити новий iterator.

## Detailed explanation

У Python 3 вбудовані функції `map()` та `filter()` повертають ліниві об'єкти-ітератори однойменних типів (`map` і `filter`), які обчислюють елементи на вимогу під час ітерації, а не зберігають їх у пам'яті.[^py314-howto-functional] Вони реалізують стандартний iterator protocol через методи `__iter__()` та `__next__()`. Кожен виклик `next()` забирає наступний елемент із вихідної послідовності, застосовує функцію чи предикат і повертає результат, просуваючи внутрішній курсор вперед.

Коли вихідна послідовність вичерпується або фільтрація добігає кінця, об'єкт викликає виняток `StopIteration` і переходить у термінальний стан. Оскільки ітератори в Python є односпрямованими й за дизайном не кешують раніше видані значення, повторний запит елементів (наприклад, ще один виклик `list(it)` або новий цикл `for`) негайно викликає `StopIteration` знову. У результаті будь-який наступний обхід повертає порожній результат без виникнення помилок чи попереджень.

Такий підхід забезпечує роботу з фіксованими витратами пам'яті `O(1)` навіть на нескінченних генераторах або гігантських потоках даних. Якщо результат обробки потрібен багаторазово, розробник має або явно матеріалізувати його в колекцію (`list()`, `tuple()`), або створювати новий об'єкт ітератора на кожну операцію.

Приклад вичерпання об'єкта `map` після першого обходу:

```python
numbers = [1, 2, 3, 4]
squared = map(lambda x: x**2, numbers)

# First pass consumes all elements from the iterator
first_pass = list(squared)
print(first_pass)
# Output: [1, 4, 9, 16]

# Second pass over the same iterator finds it exhausted
second_pass = list(squared)
print(second_pass)
# Output: []
```

**Типові помилки та практичні нюанси:**
- передача одного й того самого об'єкта `map` або `filter` у декілька споживачів (наприклад, перевірка `if any(it): ...` частково або повністю вичерпує iterator до передачі в основний цикл);
- очікування поведінки Python 2, де `map()` і `filter()` повертали матеріалізований `list`;
- спроба викликати `len()` або отримати доступ за індексом `it[0]`, що призводить до `TypeError`, оскільки ітератори не підтримують sequence protocol;
- передчасна матеріалізація через `list()` великих або нескінченних потоків даних, що нівелює переваги потокової обробки.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
