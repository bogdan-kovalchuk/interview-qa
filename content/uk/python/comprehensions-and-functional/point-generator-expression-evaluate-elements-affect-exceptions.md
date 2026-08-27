---
id: py-compfn-0005
title: "У який момент generator expression обчислює свої elements і як це впливає на exceptions та side effects?"
description: "Generator expression створює iterator негайно, але обчислює кожен element лише на момент виклику next() (lazy evaluation)."
track: python
section: comprehensions-and-functional
level: middle
type: mechanism
tags: []
status: published
updated: 2026-09-05
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
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/functional_programming.md#L19-L28
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Generator expression створює iterator негайно, але обчислює кожен element лише на момент виклику `next()` (lazy evaluation).**[^py314-howto-functional] Це означає, що exceptions та side effects відкладаються до моменту споживання, а не виникають при створенні виразу. Наприклад, `g = (1/x for x in data)` не підніме `ZeroDivisionError` до першого `next(g)` на елементі `x == 0`.

## Detailed explanation

Ключова асиметрія: обчислюється негайно лише ітерований вираз найпершого (найзовнішнішого) `for` –
`iter()` викликається на ньому одразу під час створення генератора, ще до першого
`next()`.[^py314-howto-functional] Усі інші елементи – ітеровані вирази наступних `for`, умови `if`
та сам вираз-результат – обчислюються лише лінійно, по одному елементу, під час ітерації. Тому
`(x for x in get_items())` викликає `get_items()` одразу в момент створення виразу, а сам вміст
`get_items()` обробляється лише поступово.

Це має практичний наслідок для side effects і exceptions: якщо генератор ніколи не проітерований
повністю (наприклад, цикл `break`-нув раніше або generator просто відкинули), елементи, до яких
виконання не дійшло, ніколи не обчислюються, і жодні side effects чи exceptions на них не
виникають. Це відрізняє generator expression від list comprehension, де весь результат
матеріалізується одразу, тож усі side effects і всі exceptions трапляються негайно, у порядку
елементів, до того як comprehension поверне список.

Ще одна відмінність – одноразовість: generator expression – це iterator, і після повного споживання
(`StopIteration`) він вичерпаний назавжди; повторний `for` по тому самому об'єкту нічого не дасть.
List comprehension, навпаки, породжує новий список, який можна ітерувати скільки завгодно разів.

Для вкладених `for` усередині generator expression лінива поведінка стосується й внутрішніх
ітерованих виразів: ітерований вираз внутрішнього `for` обчислюється заново на кожній ітерації
зовнішнього, а не один раз наперед – так само, як у звичайних вкладених циклах, лише з відкладеним
запуском.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
