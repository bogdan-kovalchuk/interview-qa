---
id: py-compfn-0007
title: "Як побудувати lazy pipeline з `itertools`, щоб не матеріалізувати intermediate collections?"
description: "Компонувати функції itertools у ланцюжок, де кожна приймає iterator і повертає iterator, пропускаючи дані element-by-element без проміжних списків."
track: python
section: comprehensions-and-functional
level: middle
type: practical
tags: [itertools]
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

**Компонувати функції `itertools` у ланцюжок, де кожна приймає iterator і повертає iterator, пропускаючи дані element-by-element без проміжних списків.**[^py314-howto-functional] Наприклад, `itertools.islice(itertools.chain(iter1, iter2), n)` або композиція `filter` -> `map` -> `itertools.takewhile`. <span class="warn">Кінцеве споживання (наприклад, `for` або `list()`) запускає обчислення; до цього моменту жоден елемент не обчислюється.</span>

## Detailed explanation

"Lazy pipeline" – це ланцюжок обчислень, де кожна ланка приймає iterator і повертає новий iterator,
а не список: жоден елемент не обчислюється, поки хтось не почне ітерувати кінцевий
результат.[^py314-howto-functional]

Будувати такий ланцюжок можна з generator expressions (`(x for x in ...)`) і функцій, які самі
повертають iterator: `map`, `filter`, `itertools.chain`, `itertools.islice`, `itertools.takewhile`,
`itertools.dropwhile`.[^py314-library-itertools] Кожна така функція лише запам'ятовує джерело і
правило перетворення, не викликаючи його одразу.

Головна пастка – list comprehension (`[x for x in ...]`) матеріалізує весь результат у пам'яті
одразу. Тому ланки lazy pipeline мають бути generator expressions або функціями, що повертають
iterator, а не comprehension у квадратних дужках.[^py314-reference-expressions-displays-for-lists-sets-and-dict]

Приклад pipeline, який читає файл, фільтрує рядки й бере перші десять, не завантажуючи файл у
пам'ять цілком:

```python
lines = (line.strip() for line in open('access.log'))
errors = (line for line in lines if 'ERROR' in line)
first_ten = itertools.islice(errors, 10)

for msg in first_ten:  # nothing is read from disk until this loop runs
    print(msg)
```

Обчислення запускається лише кінцевим споживачем – циклом `for`, викликом `list()` або `next()`. До
цього моменту `lines`, `errors` і `first_ten` – це лише об'єкти-iterator, які нічого не порахували.

**Типові будівельні блоки lazy pipeline:**
- `filter(predicate, it)` і `map(func, it)` – базові однопрохідні перетворення;
- `itertools.chain(*its)` – послідовне об'єднання кількох iterables без копіювання;
- `itertools.islice(it, n)` – обмеження кількості елементів без вичерпання всього iterator;
- `itertools.takewhile(predicate, it)` і `itertools.dropwhile(predicate, it)` – обрізання за умовою.

Перевага такого підходу – constant memory: pipeline обробляє по одному елементу за раз, тому розмір
вхідних даних не обмежений об'ємом RAM, на відміну від ланцюжка list comprehensions, де кожна ланка
створює власний повний список.[^py314-howto-functional]

## Environment

TODO

## Deliverable

TODO

## Acceptance criteria

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
