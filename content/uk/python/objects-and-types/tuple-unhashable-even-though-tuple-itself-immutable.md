---
id: py-objtypes-0007
title: "Чому tuple може бути unhashable, хоча сам tuple є immutable?"
description: "Tuple є hashable лише тоді, коли всі його елементи hashable."
track: python
section: objects-and-types
level: middle
type: pitfall
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
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/set_and_dict.md#L3-L16
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Tuple є hashable лише тоді, коли всі його елементи hashable.**[^py314-reference-datamodel] Hash tuple обчислюється рекурсивно з хешів елементів. Якщо tuple містить mutable об'єкт без `__hash__` (наприклад, `list` або `dict`), спроба `hash()` підніме `TypeError`. Тому такий tuple не можна використати як key у `dict` або елемент `set`.

## Detailed explanation

Об'єкт у Python є hashable лише тоді, коли його хеш-значення залишається незмінним протягом усього життєвого циклу, а для кортежу це вимагає хешовності кожного його елемента.[^py314-reference-datamodel]

Незмінність (immutability) самого контейнера не є синонімом його хешовності (hashability). `tuple` гарантує лише незмінність своєї структури: кількість елементів та адреси об'єктів, на які посилаються його комірки, зафіксовані раз і назавжди. Проте самі ці об'єкти можуть бути mutable (наприклад, `list`, `dict` або `set`). Хеш кортежу в CPython обчислюється комбінуванням хеш-значень усіх його елементів; коли інтерпретатор доходить до елемента з `__hash__ = None`, виникає `TypeError`.[^py314-library-stdtypes]

Така поведінка захищає інваріант хеш-таблиць: якщо два об'єкти рівні (`a == b`), їхні хеші обов'язково мають збігатися (`hash(a) == hash(b)`). Якби кортеж із списком усередині мав фіксований хеш, модифікація списку порушила б рівність, а якби хеш перераховувався відповідно до поточного стану списку – кортеж опинився б у неправильному бакеті `dict` або `set` і став недосяжним для пошуку.

Виправленням у подібних ситуаціях є рекурсивне приведення всіх вкладених структур до immutable еквівалентів. Замість вкладених списків слід використовувати вкладені кортежі, замість `set` – `frozenset`, а для складної структурованої інформації застосовувати frozen dataclasses або `NamedTuple`.

Приклад, що ілюструє хешовність кортежів із різним типом елементів:

```python
# A tuple of immutable objects is hashable
t1 = (1, "hello", (2, 3))
print(hash(t1))  # integer hash value
lookup = {t1: "valid_key"}
print(lookup[t1])  # 'valid_key'

# A tuple containing a mutable object (list) is unhashable
t2 = (1, [2, 3])
try:
    hash(t2)
except TypeError as exc:
    print(exc)  # unhashable type: 'list'

# It cannot be placed into a dict or set
try:
    bad_set = {t2}
except TypeError as exc:
    print(exc)  # unhashable type: 'list'
```

**Типові помилки та рекомендації:**
- вважати будь-який кортеж придатним як ключ у `dict` або елемент `set` без перевірки типів його вмісту;
- будувати складені ключі кешу з довільних аргументів функцій `(*args)` без попередньої валідації чи конвертації mutable типів;
- конвертувати список у кортеж лише на верхньому рівні (`tuple(data)`), забуваючи, що вкладені списки все одно залишають результуючий кортеж unhashable;
- для вкладених колекцій перетворювати структури на заморожені аналоги: `tuple` для послідовностей та `frozenset` для невпорядкованих наборів.

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
