---
id: py-funcs-0011
title: "Функція отримала shallow copy списку словників і змінила значення у вкладеному словнику. Чому зміна може бути видима викликачу, хоча зовнішній список скопійовано?"
track: python
section: functions-and-scope
sources:
  - source_id: py314-library-copy
    title: "Python 3.14: Library/copy"
    url: https://docs.python.org/3.14/library/copy.html
  - source_id: py314-faq-programming-why-did-changing-list-y-also-change-li
    title: "Python 3.14: Faq/programming"
    url: https://docs.python.org/3.14/faq/programming.html#why-did-changing-list-y-also-change-list-x
---

## Short answer

**`copy.copy` (shallow copy) створює новий зовнішній список, але вставляє в нього посилання на ті самі вкладені об’єкти, що й в оригіналі.**[^py314-library-copy] Тому мутація вкладеного словника через скопійований список змінює той самий об’єкт, на який посилається і оригінал. Якщо вкладені об’єкти мають бути незалежними, використовують `copy.deepcopy`, яка рекурсивно копіює вкладені об’єкти.[^py314-library-copy]

## Detailed explanation

Shallow copy копіює контейнер, а не його вміст. `copy.copy(obj)` створює новий compound object і вставляє в нього посилання на об’єкти з оригіналу.[^py314-library-copy] Для списку словників це два рівні: зовнішній список тепер окремий, а словники всередині лишаються тими самими об’єктами, тому `shallow[0] is original[0]` дає `True`. Просте присвоєння `b = a` ще слабше: воно не створює копії, а дає друге ім’я тому самому списку.[^py314-faq-programming-why-did-changing-list-y-also-change-li]

Викликач передає функції shallow copy. Функція змінює вкладений словник, і ця зміна видна в оригіналі; додавання елемента в зовнішній список копії – ні:

```python
import copy

original = [{'name': 'sensor', 'value': 1}]

def update(config):
    config[0]['value'] = 99          # changes the nested dict shared with the caller
    config.append({'name': 'new'})   # changes only the outer list of the copy

shallow = copy.copy(original)
update(shallow)
print(original)                      # [{'name': 'sensor', 'value': 99}]
print(len(original))                 # 1

deep = copy.deepcopy(original)
deep[0]['value'] = 5
print(original[0]['value'])          # 99: the deep copy did not share the dict
```

Слід розрізняти дві операції. `config[0] = {...}` змінює лише зовнішній список копії, а `config[0]['value'] = 99` змінює словник, спільний з оригіналом. Обидві виконуються в одній функції, але діють на різних рівнях, тому видимість змін залежить від того, що саме змінено.

Глибока копія `copy.deepcopy` рекурсивно копіює вкладені об’єкти, тому зміна в ній не доходить до оригіналу.[^py314-library-copy] Ціна в тому, що вона може скопіювати й дані, які мали б лишатися спільними між копіями.[^py314-library-copy]

**Типові помилки:**
- вважати, що `copy.copy` рекурсивно копіює всі рівні вкладеності;
- вважати, що `x[:]` або `list.copy()` дають глибоку копію: вони теж створюють shallow copy;[^py314-library-copy]
- завжди використовувати `copy.deepcopy`, навіть коли спільний вкладений об’єкт є свідомим рішенням.
