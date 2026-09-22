---
id: py-objtypes-0016
title: "Як numeric equality між `1`, `1.0` і `True` впливає на їх використання як keys одного словника?"
description: "1, 1.0 і True мають однаковий hash і порівнюються як рівні (1 == 1.0 == True), тому в dict вони займають одну й ту ж комірку – перемагає останнє присвоєння."
track: python
section: objects-and-types
level: senior
type: pitfall
tags: [1-0]
status: published
updated: 2026-09-27
content_revision: 2
reconciled_with:
  en: 2
execution:
  language: python
  standard: null
  toolchain:
    name: cpython
    version: "3.14.7"
  flags: []
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/set_and_dict.md#L104-L117
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`1`, `1.0` і `True` мають однаковий hash і порівнюються як рівні (`1 == 1.0 == True`), тому в dict вони займають одну й ту ж комірку – перемагає останнє присвоєння.**[^py314-reference-datamodel]

```text
d = {1: 'a', 1.0: 'b', True: 'c'}
print(d)        # {1: 'c'}
print(len(d))   # 1
```

Це наслідок числової ієрархії Python: `bool` є підтипом `int`, тому `True == 1`, а `float` і `int` порівнюються за числовим значенням. <span class="warn">Аналогічна колапсія відбувається у `set`: `{1, 1.0, True}` містить лише один елемент.</span>

## Detailed explanation

Пошук та вставка ключів у хеш-таблицях Python (`dict` та `set`) базуються на двох обов'язкових умовах: збігу хеш-значень (`hash(k1) == hash(k2)`) та еквівалентності об'єктів (`k1 is k2 or k1 == k2`).[^py314-reference-datamodel]

Оскільки `bool` є прямим підкласом `int` (`isinstance(True, int)` повертає `True`), булеве значення `True` має числове значення `1`. Фундаментальний інваріант об'єктної моделі Python вимагає: якщо два об'єкти рівні за `==`, їхні хеші зобов'язані збігатися (`a == b` тягне за собою `hash(a) == hash(b)`). Тому `hash(1) == hash(1.0) == hash(True) == 1`, і для словника всі три об'єкти вказують на одну й ту саму комірку хеш-таблиці.[^py314-library-stdtypes]

Коли `dict` отримує ключ, чий хеш та значення вже присутні в таблиці, він оновлює значення за цим слотом, але зберігає початковий об'єкт ключа (перший вставлений). Це оптимізація CPython, яка уникає зайвого декременту та інкременту лічильників посилань для незмінних ключів, проте вона створює небезпечну ілюзію: тип збереженого ключа залежить від порядку викликів, тоді як значення завжди відповідає останньому запису.

Демонстрація колізії однакових числових ключів та збереження початкового об'єкта:

```python
# Keys with equal numeric values share the same hash
print(hash(1) == hash(1.0) == hash(True))  # True
print(1 == 1.0 == True)  # True

# Dict overwrites value but preserves the FIRST inserted key object
data = {1: "integer", 1.0: "float", True: "boolean"}
print(data)  # {1: 'boolean'}
first_key = list(data.keys())[0]
print(type(first_key), first_key)  # <class 'int'> 1

# Lookup succeeds with any numerically equal key
print(data[True])  # boolean
print(data[1.0])  # boolean

# Set deduplication retains only the first inserted object
unique_items = {True, 1, 1.0}
print(unique_items)  # {True}
```

**Практичні наслідки для архітектури та коду:**
- неявна втрата ключів: збереження конфігурацій чи результатів парсингу з різними типами (наприклад, прапорець `True` та числовий ID `1`) в одному `dict` призводить до перезапису значень;
- неочевидний тип збереженого ключа: `dict` оновлює значення, але залишає перший доданий ключ, тому ітерація по `keys()` може повертати `int` замість очікуваного `bool`;
- колапс у `set`: використання `set` для дедуплікації змішаних колекцій непомітно відкидає елементи, які розробник вважав різними сутностями;
- захисний підхід: якщо тип ключа має значення, використовують складений ключ `(type(k), k)` або окремі словники для кожного типу.

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
