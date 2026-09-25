---
id: py-compfn-0004
title: "Чому groups, які повертає `itertools.groupby()`, потрібно спожити або матеріалізувати до переходу до наступної group?"
description: "Кожна group – це iterator, який shares the underlying iterable з groupby(); при переході до наступної групи попередній iterator стає порожнім."
track: python
section: comprehensions-and-functional
level: middle
type: pitfall
tags: [itertools-groupby]
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

**Кожна group – це iterator, який shares the underlying iterable з `groupby()`; при переході до наступної групи попередній iterator стає порожнім.**[^py314-howto-functional] Тому збереження об'єкта group без матеріалізації (наприклад, у `list`) призведе до порожнього результату при подальшому споживанні. <span class="warn">Типова помилка: `groups = [(k, g) for k, g in groupby(data, key)]`, після якої всі `g` вже вичерпані.</span>

## Detailed explanation

Кожна група, яку повертає `itertools.groupby()`, є окремим iterator (`_grouper`), що посилається на спільний потік даних вхідної послідовності.[^py314-library-itertools] Коли зовнішній цикл переходить до наступного елемента через виклик `next()` на об'єкті `groupby`, алгоритм змушений просунути внутрішній курсор вперед до появи нового ключа. Якщо елементи поточної групи не були вичитані раніше, `groupby` проковтує їх самостійно, щоб знайти початок наступної групи, через що попередній iterator спорожнюється безповоротно.

Така поведінка – це свідомий архітектурний компроміс на користь ефективності пам'яті (streaming processing). `groupby()` розрахований на роботу з нескінченними або гігантськими послідовностями з `O(1)` додаткової пам'яті, тому він не кешує елементи груп і не буферизує вхідні значення. Якщо потрібен одночасний доступ до кількох груп або їх багаторазове проходження, кожну групу необхідно матеріалізувати (наприклад, викликавши `list(group)`) безпосередньо в тілі циклу до початку наступної ітерації `groupby`.

Варто також пам'ятати фундаментальну вимогу `groupby`: він групує лише послідовні однакові ключі (run-length grouping). На відміну від SQL `GROUP BY`, він не збирає однакові ключі з різних частин колекції, якщо вхідний iterable попередньо не відсортовано за тим самим ключем.

Демонстрація проблеми спорожнення груп та її правильного виправлення:

```python
from itertools import groupby

data = ["ant", "ape", "bat", "bear", "cat"]

# Pitfall: storing iterators without materialization
broken = [(k, g) for k, g in groupby(data, key=lambda s: s[0])]
print([(k, list(g)) for k, g in broken])
# Output: [('a', []), ('b', []), ('c', [])]

# Correct: materialize each group immediately
correct = [(k, list(g)) for k, g in groupby(data, key=lambda s: s[0])]
print(correct)
# Output: [('a', ['ant', 'ape']), ('b', ['bat', 'bear']), ('c', ['cat'])]
```

**Типові помилки та практичні наслідки:**
- збереження пар `(key, group)` у список чи словник без виклику `list(group)` у момент ітерації;
- використання `groupby()` на невідсортованих даних з очікуванням агрегації однакових ключів по всій колекції;
- спроба повторного читання `group` після виходу з внутрішнього циклу або генераторного контексту.

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
