---
id: py-syntax-0004
title: "Як extended iterable unpacking працює у присвоєнні `head, *middle, tail = items` і що станеться, якщо елементів недостатньо?"
description: "*middle збирає всі проміжні елементи у list; для успіху потрібно щонайменше 2 елементи (для head і tail)."
track: python
section: syntax-and-control-flow
level: middle
type: mechanism
tags: [head-middle-tail-items]
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-reference-expressions
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-simple-stmts
    title: "Python 3.14: Reference/simple Stmts"
    url: https://docs.python.org/3.14/reference/simple_stmts.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-compound-stmts
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/syntax.md#L252-L352
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`*middle` збирає всі проміжні елементи у `list`; для успіху потрібно щонайменше 2 елементи (для `head` і `tail`).**[^py314-reference-expressions] Наприклад, `head, *middle, tail = [1, 2, 3, 4, 5]` дає `head=1, middle=[2, 3, 4], tail=5`. Якщо елементів лише один – `head, *middle, tail = [1]` – виникає `ValueError: not enough values to unpack (expected at least 2, got 1)`.

## Detailed explanation

Extended unpacking розділяє цілі на дві категорії: звичайні імена, кожне з яких забирає рівно один
елемент, і рівно одне ім'я з зірочкою, яке забирає все, що лишилось.[^py314-reference-simple-stmts]

Алгоритм простий: Python рахує звичайні цілі зліва і справа від зірочки, віддає їм по одному
елементу з відповідних кінців, а середину складає у **список** – завжди список, навіть якщо джерелом
був кортеж чи рядок.

```python
head, *middle, tail = [1, 2, 3, 4, 5]
head      # 1
middle    # [2, 3, 4]   - always a list
tail      # 5

first, *rest = 'abc'
rest      # ['b', 'c']  - a list of characters, not a string
```

Звідси й мінімальна кількість елементів: вона дорівнює кількості звичайних цілей. Для
`head, *middle, tail` це два; якщо елементів менше, буде `ValueError`, а не мовчазне
`None`.[^py314-reference-expressions]

```python
head, *middle, tail = [1]
# ValueError: not enough values to unpack (expected at least 2, got 1)

head, *middle, tail = [1, 2]
middle    # []  - exactly two is enough; the middle is simply empty
```

Зірочка може стояти в будь-якій позиції, не лише посередині – і саме це робить конструкцію зручною
для «взяти перше і решту» або «взяти останнє і решту».

```python
*init, last = [1, 2, 3]     # init = [1, 2], last = 3
a, b, *rest = [1, 2]        # rest = []
```

**Обмеження й тонкощі:**
- зірочка може бути лише **одна** в одній цілі: `*a, *b = ...` – синтаксична помилка, бо поділ був би
  неоднозначним;
- джерелом може бути будь-який iterable, включно з генератором – але він буде вичерпаний повністю,
  бо середину треба матеріалізувати;
- це робить `head, *rest = infinite_generator()` пасткою: конструкція спробує зчитати все;
- та сама зірочка в літералах означає інше – розпакування у нову колекцію (`[*a, *b]`), і там
  кількох зірочок бути може.

Найчастіше застосування – розбір послідовності відомої форми без індексів: `name, *aliases, domain =
parts` читається краще, ніж три звернення за
номером.[^py314-reference-compound-stmts]

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
