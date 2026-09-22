---
id: py-objtypes-0005
title: "Чому `y = x` не копіює mutable object і як mutation через `y` стає видимою через `x`?"
description: "Присвоювання y = x копіює лише посилання на об'єкт, а не сам об'єкт; обидва імена вказують на той самий mutable об'єкт."
track: python
section: objects-and-types
level: middle
type: mechanism
tags: [y-x]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/data_types.md#L48-L93
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Присвоювання `y = x` копіює лише посилання на об'єкт, а не сам об'єкт; обидва імена вказують на той самий mutable об'єкт.**[^py314-reference-datamodel] Будь-яка зміна стану об'єкта через одне ім'я (наприклад, `y.append(3)` для списку) одразу відображається через інше, бо `x` і `y` посилаються на одну й ту саму ділянку пам'яті. Для незалежної копії потрібні `copy.copy()` або `copy.deepcopy()`.

## Detailed explanation

У Python змінні не є іменованими ділянками пам'яті, що зберігають значення безпосередньо, а слугують мітками або посиланнями на об'єкти, розташовані в купі (heap).[^py314-reference-datamodel]

Операція присвоювання `y = x` обчислює вираз праворуч і прив'язує ім'я `y` до того самого об'єкта, на який уже вказує `x`, збільшуючи його лічильник посилань. Сам об'єкт при цьому не дублюється і не переміщується в пам'яті. Обидві змінні мають однаковий ідентифікатор (`id(x) == id(y)`) і перевірка ідентичності повертає `x is y == True` (явище aliasing).

Якщо об'єкт належить до mutable-типів (`list`, `dict`, `set`), методи мутації (наприклад, `.append()` або заміна за індексом) змінюють його внутрішній стан на місці без створення нового об'єкта. Оскільки змінна `x` посилається на ту саму ділянку пам'яті, будь-яке звернення через `x` негайно відображає внесені зміни.[^py314-library-stdtypes]

Щоб уникнути спільної мутації, необхідно створити незалежну копію об'єкта. Поверхневе копіювання (`copy.copy()`, метод `.copy()` або зріз `[:]`) створює новий зовнішній контейнер, але копіює посилання на його вкладені елементи. Якщо структура містить вкладені mutable об'єкти, надійну ізоляцію забезпечує лише глибоке копіювання `copy.deepcopy()`, яке рекурсивно клонує всі рівні ієрархії.[^py314-library-copy]

Приклад різниці між зв'язуванням посилань, поверхневим і глибоким копіюванням:

```python
import copy

x = [1, [2, 3]]
y = x                  # Aliasing: both names reference the exact same object
shallow = copy.copy(x) # Shallow copy: new outer list, but shared inner list
deep = copy.deepcopy(x) # Deep copy: independent duplicate of all nested objects

y[0] = 99
y[1].append(4)

print(x)        # [99, [2, 3, 4]]: in-place mutations through y are seen in x
print(shallow)  # [1, [2, 3, 4]]: outer list preserved, but nested list was mutated
print(deep)     # [1, [2, 3]]: completely isolated from mutations
```

**Типові пастки та практичні рекомендації:**
- змінні аргументи за замовчуванням у функціях: конструкція `def fn(items=[]):` створює один список під час завантаження функції, через що всі наступні виклики модифікують спільний екземпляр;
- створення вкладених списків множенням: конструкція `matrix = [[0] * 3] * 3` створює список із трьох посилань на один і той самий внутрішній список;
- поверхневе копіювання замість глибокого: зріз `x[:]` копіює лише верхній рівень, залишаючи вкладені списки або словники зв'язаними;
- непередбачувані побічні ефекти: передача mutable об'єкта у функцію дозволяє їй змінювати стан об'єкта у викликаючому коді без явного повернення значення.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
