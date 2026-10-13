---
id: py-funcs-0007
title: "Коли обчислюється вираз default argument і чому default на кшталт `timeout=get_timeout()` може не відображати подальші зміни конфігурації?"
description: "Default-вираз обчислюється під час виконання інструкції def, а не при кожному виклику функції."
track: python
section: functions-and-scope
level: middle
type: mechanism
tags: [timeout-get-timeout]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-reference-compound-stmts-function-definitions
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#function-definitions
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
---

## Short answer

**Default-вираз обчислюється під час виконання інструкції `def` – один раз для кожного такого виконання, а не при кожному виклику функції.**[^py314-reference-compound-stmts-function-definitions] Функція зберігає вже обчислений результат. Якщо `get_timeout()` повертає, наприклад, `30` під час імпорту модуля, то всі подальші виклики без аргументу отримуватимуть `30`, навіть якщо конфігурація змінилася. Щоб значення відповідало поточній конфігурації, його треба обчислювати в тілі функції.

## Detailed explanation

Значення за замовчуванням обчислюються зліва направо під час виконання інструкції `def`. Python зберігає результат обчислення, а не сам вираз, тому `get_timeout()` у сигнатурі викликається один раз, коли виконується `def`, а виклики `fetch(...)` без `timeout` далі використовують готове число.[^py314-reference-compound-stmts-function-definitions]

У цьому прикладі `get_timeout()` виконується під час `def`, а зміна середовища після імпорту вже нічого не змінює:

```python
import os

def get_timeout():
    print('get_timeout() called')         # runs once, while def executes
    return int(os.environ.get('TIMEOUT', '30'))

def fetch(url, timeout=get_timeout()):   # the default is computed here
    return f'{url} timeout={timeout}'

os.environ['TIMEOUT'] = '60'             # configuration changes after the import
print(fetch('a'))                        # a timeout=30 (default computed earlier)
print(fetch('b'))                        # b timeout=30
print(fetch('c', timeout=5))             # c timeout=5 (explicit argument)
```

Так поводиться будь-який вираз, що залежить від стану на момент `def`: `datetime.now()`, прочитаний файл, поточний користувач. Для модуля `def` виконується під час імпорту. Якщо `def` виконується кілька разів, наприклад у функції-фабриці, яка створює нові функції, вираз обчислюється при кожному такому виконанні.[^py314-reference-compound-stmts-function-definitions]

Щоб значення відповідало конфігурації в момент виклику, `default` роблять `None`, а значення обчислюють у тілі функції:

```python
import os

def get_timeout():
    return int(os.environ.get('TIMEOUT', '30'))

def fetch(url, timeout=None):
    if timeout is None:
        timeout = get_timeout()          # evaluated on every call
    return f'{url} timeout={timeout}'

print(fetch('a'))                        # a timeout=30
os.environ['TIMEOUT'] = '60'
print(fetch('b'))                        # b timeout=60
```

Ціна – один додатковий рядок. У сигнатурі видно `timeout=None`, а реальне значення береться під час виклику.

**Типові помилки:**
- вважати, що `timeout=get_timeout()` викликається при кожному виклику `fetch`;
- змінити конфігурацію після імпорту і очікувати, що вже визначені default-значення оновляться;
- ставити `datetime.now()` у default і очікувати актуального часу при кожному виклику.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
