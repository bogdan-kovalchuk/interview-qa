---
id: py-stdlib-0003
title: "Коли factory у `defaultdict` може створити небажану mutation при простому читанні key?"
description: "Якщо default_factory задано, звернення d[key] до відсутнього ключа вставляє новий запис, навіть коли значення лише читають."
track: python
section: standard-library
level: senior
type: pitfall
tags: [defaultdict]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-library-collections
    title: "Python 3.14: Library/collections"
    url: https://docs.python.org/3.14/library/collections.html
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
  - source_id: py314-library-pathlib
    title: "Python 3.14: Library/pathlib"
    url: https://docs.python.org/3.14/library/pathlib.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-datetime
    title: "Python 3.14: Library/datetime"
    url: https://docs.python.org/3.14/library/datetime.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-re
    title: "Python 3.14: Library/re"
    url: https://docs.python.org/3.14/library/re.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-collections-defaultdict
    title: "Python 3.14: Library/collections, defaultdict.__missing__"
    url: https://docs.python.org/3.14/library/collections.html#collections.defaultdict.__missing__
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: defaultdict.__missing__ (виклик default_factory і вставка значення; KeyError, якщо factory дорівнює None; get() і in не викликають __missing__)."
---

## Short answer

**Будь-яке звернення через `d[key]` до відсутнього ключа викликає `default_factory` і вставляє новий запис у словник, якщо factory задано, навіть коли значення лише читають.**[^py314-library-collections-defaultdict] Наприклад, `if d[key]:` для ще не існуючого ключа створить запис із дефолтним значенням. Метод `get()` не викликає factory і не змінює словник, тож його варто використовувати для безпечного читання.[^py314-library-collections-defaultdict]

## Detailed explanation

`defaultdict` – це звичайний `dict` із атрибутом `default_factory`. Для відсутнього ключа `dict` піднімає `KeyError`, а `defaultdict` викликає `default_factory()` без аргументів, вставляє результат під цим ключем і повертає його.[^py314-library-collections-defaultdict] Це робить метод `__missing__`, який `__getitem__` викликає тільки тоді, коли ключа немає. Отже, якщо `default_factory` задано, кожне звернення через квадратні дужки до відсутнього ключа змінює словник, навіть якщо код хотів лише прочитати значення.

Умова тут – `default_factory` не `None`. Якщо factory немає, `__missing__` піднімає `KeyError` з ключем як аргументом і нічого не вставляє.[^py314-library-collections-defaultdict] Інші операції, як-от `get()` і перевірка `in`, метод `__missing__` не викликають.[^py314-library-collections-defaultdict]

Читання через квадратні дужки вставляє ключ, а `get()` і `in` – ні:

```python
from collections import defaultdict

groups = defaultdict(list)
if groups['admin']:            # a plain read: 'admin' is inserted with []
    print('has admins')
print('admin' in groups)      # True
print(groups.get('guest'))    # None: get() does not call default_factory
print('guest' in groups)     # False
```

Найнебезпечніша ситуація – ітерація. Якщо цикл читає відсутній ключ із того самого словника, вставка змінює його розмір, і наступний крок ітератора в CPython піднімає `RuntimeError`:

```python
from collections import defaultdict

inventory = defaultdict(int, {'apple': 3, 'pear': 0})
try:
    for item in inventory:
        if inventory['kiwi'] == 0:   # a read of a missing key adds 'kiwi'
            pass
except RuntimeError as error:
    print(error)                     # dictionary changed size during iteration
print(sorted(inventory))             # ['apple', 'kiwi', 'pear']
```

Практичне правило: `default_factory` варто використовувати там, де вставка і є наміром, наприклад `groups[key].append(item)`. Для перевірки або читання, яке не має змінювати словник, використовуйте `key in d` або `d.get(key)`.[^py314-library-collections-defaultdict]

**Типові помилки:**
- вважати, що `if d[key]:` лише перевіряє значення і нічого не змінює;
- читати `d[key]` всередині циклу по тому самому `d` і отримувати `RuntimeError` або зайві ключі в результаті;
- вважати, що `get()` створює ключ через `default_factory`: він повертає `None` (або переданий default) і не викликає factory.

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
