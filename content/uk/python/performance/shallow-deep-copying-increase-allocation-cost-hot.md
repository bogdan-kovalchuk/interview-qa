---
id: py-perf-0009
title: "Як shallow та deep copying можуть збільшити allocation cost у hot path?"
track: python
section: performance
sources:
  - source_id: py314-library-copy
    title: "Python 3.14: Library/copy"
    url: https://docs.python.org/3.14/library/copy.html
  - source_id: cpython-copy-py
    title: "CPython 3.14: Lib/copy.py"
    url: https://github.com/python/cpython/blob/v3.14.6/Lib/copy.py
  - source_id: py314-library-tracemalloc
    title: "Python 3.14: Library/tracemalloc"
    url: https://docs.python.org/3.14/library/tracemalloc.html
---

## Short answer

**Shallow copy створює новий контейнер верхнього рівня, а вкладені об’єкти лишаються спільними; deep copy рекурсивно створює копії вкладених контейнерів, тож кількість виділень зростає з розміром структури.**[^py314-library-copy] `copy.copy(x)` дає один новий контейнер, а `copy.deepcopy(x)` копіює кожен вкладений контейнер і веде memo-словник уже скопійованих об’єктів, щоб коректно обробити цикли. У hot path копіювання великих або глибоко вкладених структур додає помітні виділення пам’яті й час.

## Detailed explanation

Присвоєння в Python не копіює об’єкт, а лише створює ще одне посилання. Копія потрібна, коли два контейнери мають змінюватися незалежно. Модуль `copy` розрізняє два випадки: shallow copy створює новий контейнер верхнього рівня, але вкладені об’єкти лишаються тими самими; deep copy рекурсивно створює копії вкладених контейнерів.[^py314-library-copy] Приклад:

```python
import copy

orders = [[1, 2], [3]]             # nested lists
shallow = copy.copy(orders)
shallow[0].append(99)              # the nested list is shared by both copies
print(orders)                      # [[1, 2, 99], [3]]
print(shallow[0] is orders[0])     # True

deep = copy.deepcopy(orders)
deep[1].append(7)
print(orders)                      # [[1, 2, 99], [3]]: the original is unchanged
print(deep[1] is orders[1])        # False

cyclic = []
cyclic.append(cyclic)              # a list that contains itself
copied = copy.deepcopy(cyclic)     # the memo dict stops the recursion
print(copied[0] is copied)         # True

text = 'abc'
print(copy.deepcopy(text) is text) # True: atomic values such as str are returned as is
```

`deepcopy` тримає memo-словник уже скопійованих об’єктів; без нього цикл посилань міг би призвести до нескінченної рекурсії.[^py314-library-copy] Тому копія циклічного списку коректна, і її елемент вказує на саму копію. У CPython атомарні значення на кшталт `str` і `int` `deepcopy` повертає без копії; список таких типів визначено в `copy.py`.[^cpython-copy-py] Вартість deep copy тому припадає на контейнери та їхній вміст.

Звідси ціна в hot path. Shallow copy списку з `N` елементами виділяє один новий список на `N` посилань. Deep copy створює новий об’єкт для кожного вкладеного контейнера; у CPython кожен крок іде через Python-код функції `deepcopy`.[^cpython-copy-py] Якщо таке копіювання виконується на кожному запиті або в кожній ітерації, виділення пам’яті й час зростають разом із розміром структури.

У hot path зазвичай достатньо копіювати лише змінюваний рівень: `list.copy()` або зріз `x[:]` дають shallow copy, а вкладені об’єкти лишаються спільними.[^py314-library-copy] Незмінні значення, наприклад `tuple` з незмінними елементами, можна передавати без копії. Щоб побачити обсяг виділень, порівнюють знімки `tracemalloc`.[^py314-library-tracemalloc]

Shallow copy достатньо, коли вкладені об’єкти не змінюються або їхня спільна зміна допустима. Deep copy потрібен, коли вкладений змінюваний стан має бути незалежним. При цьому deep copy може скопіювати більше, ніж треба: документація прямо попереджає, що він копіює і дані, призначені для спільного використання між копіями.[^py314-library-copy]

**Типові помилки:**
- вважати, що shallow copy ізолює вкладені списки чи словники, і змінювати їх в одній копії;
- викликати `deepcopy` на кожному запиті для великої структури замість копіювання лише змінюваного рівня;
- використовувати deep copy для даних, які мають залишатися спільними між копіями.
