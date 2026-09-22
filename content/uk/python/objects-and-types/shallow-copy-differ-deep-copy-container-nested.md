---
id: py-objtypes-0009
title: "Чим shallow copy відрізняється від deep copy для контейнера з вкладеними mutable objects?"
description: "Shallow copy створює новий зовнішній контейнер, але внутрішні об'єкти залишаються спільними посиланнями; deep copy рекурсивно копіює все до кінця."
track: python
section: objects-and-types
level: middle
type: comparison
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/syntax.md#L442-L558
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Shallow copy створює новий зовнішній контейнер, але внутрішні об'єкти залишаються спільними посиланнями; deep copy рекурсивно копіює все до кінця.**[^py314-reference-datamodel] Для `a = [[1, 2]]`: після `s = copy.copy(a)` вираз `s[0] is a[0]` – `True`, і mutation `s[0]` змінює `a[0]`. Після `d = copy.deepcopy(a)` вираз `d[0] is a[0]` – `False`, і mutation `d[0]` не впливає на `a[0]`.

## Detailed explanation

Головна відмінність між shallow copy та deep copy полягає в глибині дублювання графа об'єктів під час створення копії.[^py314-library-copy]

Shallow copy (поверхнева копія через `copy.copy()`, зріз `lst[:]`, фабрики `list(lst)` або метод `.copy()`) створює новий зовнішній контейнер, але копіює в нього лише покажчики на вже наявні елементи. Якщо елементами є незмінні скалярні типи (числа, рядки), мутація неможлива, і така копія поводиться незалежно. Проте якщо всередині розташовані інші mutable структури (вкладені списки, словники), новий контейнер вказує на ті самі адреси в пам'яті, що й оригінал, тому зміна стану вкладеного об'єкта через копію миттєво відбивається в оригіналі.[^py314-reference-datamodel]

Deep copy (глибока копія через `copy.deepcopy()`) рекурсивно обходить увесь граф об'єктів і створює нові екземпляри для кожного знайденого контейнера. Для незмінних базових об'єктів (чисел, рядків або кортежів, які містять лише незмінні типи) Python оптимізує процес і не виділяє зайвої пам'яті, повертаючи посилання на оригінал. Для всіх mutable контейнерів створюються повністю ізольовані копії, що унеможливлює побічні ефекти при модифікації.

Вибір між ними визначається компромісом між безпекою та продуктивністю. Shallow copy виконується за час $O(n)$ від довжини зовнішньої колекції й потребує мінімуму пам'яті, тоді як deep copy витрачає ресурси на рекурсивний обхід довільного графа, створення словника memo для відстеження відвіданих адрес та конструювання множини нових об'єктів.

Приклад поведінки shallow copy та deep copy для вкладених списків:

```python
import copy

original = [[1, 2], [3, 4]]

# Shallow copy: new outer list, shared inner lists
shallow = copy.copy(original)
print(shallow is original)        # False (new outer container)
print(shallow[0] is original[0])  # True (shared inner reference)

shallow[0].append(99)
print(original[0])                # [1, 2, 99] - mutation is visible in original!

# Deep copy: recursive duplicate of all nested mutable objects
deep = copy.deepcopy(original)
print(deep is original)           # False
print(deep[0] is original[0])     # False (new independent inner list)

deep[0].append(100)
print(original[0])                # [1, 2, 99] - untouched by mutation in deep
```

**Типові помилки та практичні правила:**
- використовувати `copy.copy()`, `lst[:]` чи `d.copy()` для структур з вкладеними даними і помилково очікувати повної ізоляції змін;
- викликати `copy.deepcopy()` на великих структурах без потреби, що призводить до помітного падіння швидкодії та надлишкового споживання оперативної пам'яті;
- намагатися глибоко копіювати об'єкти, що утримують зовнішні ресурси (файлові дескриптори, мережеві сокети, потоки thread), що викликає помилки копіювання або некоректний стан;
- для часткової ізоляції застосовувати list comprehension або dict comprehension, щоб явно контролювати, які рівні вимагають створення нових об'єктів.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
