---
id: py-stdlib-0014
title: "Коли `bisect` корисний для sorted list і чому binary search не робить insertion дешевою?"
track: python
section: standard-library
sources:
  - source_id: py314-library-bisect
    title: "Python 3.14: Library/bisect"
    url: https://docs.python.org/3.14/library/bisect.html
---

## Short answer

**`bisect` знаходить позицію вставки за логарифмічну кількість порівнянь, але `insort()` коштує O(n), бо крок `list.insert()` зсуває елементи.**[^py314-library-bisect] Модуль корисний для пошуку за діапазоном у відсортованих даних і для довгих списків з дорогим порівнянням; він викликає лише `__lt__`.[^py314-library-bisect] Для частих вставок у великий список варто розглянути іншу структуру, наприклад `SortedList` із пакета `sortedcontainers`.

## Detailed explanation

`bisect` – двійковий пошук у відсортованому списку: `bisect_left` дає позицію перед рівними елементами, `bisect_right` – після них. Функції викликають лише `__lt__`, без `__eq__`, тож рівність треба перевіряти окремо.[^py314-library-bisect]

Приклад (ілюстративний, виконано на CPython 3.13 і 3.14):

```python
import bisect

# Range lookup: bisect_right returns the index of the first breakpoint above the score.
breakpoints = [60, 70, 80, 90]
grades = ["F", "D", "C", "B", "A"]
print(grades[bisect.bisect_right(breakpoints, 85)])   # B

# insort finds the position with a binary search, then list.insert shifts the tail.
data = [10, 20, 30, 40]
bisect.insort(data, 25)
print(data)                                           # [10, 20, 25, 30, 40]

# bisect never tests equality, so a membership check compares the found element.
def contains(sorted_items, x):
    i = bisect.bisect_left(sorted_items, x)
    return i < len(sorted_items) and sorted_items[i] == x

print(contains(data, 30), contains(data, 35))         # True False
```

`bisect_right(breakpoints, 85)` дає 3, тож `grades[3]` дорівнює `'B'`. Пошук для `insort` логарифмічний, але `list.insert` зсуває хвіст списку, і на великому списку домінує саме зсув, тому `insort` має O(n).[^py314-library-bisect] Функція `contains` робить рівність явною.

Модуль корисний, коли відсортований список уже є, а запити переважно читають дані: пошук позиції, межі діапазонів або довгі списки з дорогим порівнянням. Для пошуку конкретних значень словник зазвичай швидший, і документація радить його саме для цього.[^py314-library-bisect] Параметр `key` (з Python 3.10) застосовується до елементів списку, але не до `x`, тож `x` має бути вже в тому самому ключі.[^py314-library-bisect]

Межі: `bisect` не перевіряє, що список відсортований, тож на несортованому списку він мовчки поверне позицію, яка нічого не означає. Функції модуля не потокобезпечні: паралельна вставка в один список через `insort` може залишити його несортованим.[^py314-library-bisect]

**Типові помилки:**
- вважати, що `insort` має O(log n) загалом: логарифмічний лише пошук, а вставка в список коштує O(n);
- покладатися на `bisect` у перевірці наявності без порівняння `a[i] == x`;
- шукати в списку, відсортованому іншим порядком або іншим ключем: `bisect` дасть хибну позицію без помилки.
