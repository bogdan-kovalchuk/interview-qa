---
id: py-compfn-0012
title: "Як initializer визначає result `functools.reduce()` для empty iterable і як left-to-right grouping змінює result неасоціативної operation?"
description: "Без initializer порожнє iterable дає TypeError; з initializer – результатом стає сам initializer, навіть якщо iterable порожній."
track: python
section: comprehensions-and-functional
level: senior
type: mechanism
tags: [functools-reduce]
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

**Без initializer порожнє iterable дає `TypeError`; з initializer – результатом стає сам initializer, навіть якщо iterable порожній.**[^py314-howto-functional] `reduce()` застосовує функцію зліва направо: `reduce(sub, [1, 2, 3])` обчислює `((1-2)-3) = -4`, а не `1-(2-3) = 2`. Для неасоціативних операцій (віднімання, ділення) порядок групування визначає результат, тому `reduce` завжди фіксує left-fold семантику. Додавання initializer зсуває стартовий акумулятор: `reduce(sub, [1, 2, 3], 0)` -> `(((0-1)-2)-3) = -6`.

## Detailed explanation

Функція `functools.reduce()` реалізує ліву згортку (left fold), у якій наявність або відсутність `initializer` фундаментально визначає базовий випадок ітерації та поведінку на порожніх послідовностях.[^py314-library-functools] Якщо `initializer` передано, він стає початковим значенням внутрішнього акумулятора, і редукція починається з першого елемента ітерованого об'єкта. Якщо ж колекція виявляється порожньою, `reduce()` негайно повертає сам `initializer` без жодного виклику функції-редуктора.[^py314-howto-functional]

Коли `initializer` не вказано, `reduce()` змушений вилучити перший елемент із переданого iterable як стартове значення акумулятора, після чого застосовує функцію до акумулятора і другого елемента. Якщо iterable при цьому порожній, отримати початкове значення неможливо, тому інтерпретатор викидає `TypeError: reduce() of empty iterable with no initial value`. Якщо ж колекція містить рівно один елемент, `reduce()` повертає його без виклику функції, що також може стати непоміченим джерелом помилок, коли очікувалося виконання перетворень або валідації.

Лівоасоціативне групування означає, що обчислення виконуються строго зліва направо: для елементів `[a, b, c]` вираз обчислюється як `f(f(a, b), c)`. Для асоціативних операцій (додавання чи множення) порядок розстановки дужок не впливає на кінцеве значення, проте для неасоціативних операцій (віднімання, ділення) цей вибір є визначальним. Додавання `initializer` `x` не просто додає додатковий крок, а стає найлівішим операндом, трансформуючи дерево викликів у `f(f(f(x, a), b), c)`.

Поведінка `reduce()` з порожніми послідовностями та зміна структури обчислень при неасоціативних операціях:

```python
from functools import reduce
from operator import sub

# Empty iterable behavior
empty_list = []
res_with_init = reduce(sub, empty_list, 100)
print(res_with_init)  # 100 (returned immediately without calling sub)

try:
    reduce(sub, empty_list)
except TypeError as err:
    print(err)  # reduce() of empty iterable with no initial value

# Left-to-right grouping (left fold) with non-associative operation
items = [1, 2, 3, 4]
# Without initializer: (((1 - 2) - 3) - 4) = -8
res_no_init = reduce(sub, items)
print(res_no_init)  # -8

# With initializer (0 becomes the leftmost operand): ((((0 - 1) - 2) - 3) - 4) = -10
res_init = reduce(sub, items, 0)
print(res_init)  # -10
```

**Практичні наслідки та типові помилки:**
- виклик `reduce()` без `initializer` над динамічними генераторами чи фільтрованими послідовностями ризикує викинути несподіваний `TypeError`, якщо колекція виявиться порожньою;
- передача мутабельного об'єкта (наприклад, списку чи словника) як `initializer` може призвести до небажаних мутацій, якщо функція модифікує акумулятор на місці замість повернення нового значення;
- спроба емулювати right fold простим переворотом списку `reduce(sub, reversed(items))` змінює не лише порядок асоціативності, а й позиції операндів, що не є еквівалентом математичного `foldr`;
- для неасоціативних операцій (віднімання, ділення, конкатенація чи вкладення) зміна наявності `initializer` зсуває всю структуру дужок і призводить до принципово інших числових результатів.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
