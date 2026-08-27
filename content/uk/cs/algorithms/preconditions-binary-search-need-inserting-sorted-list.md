---
id: cs-algo-0001
title: "Які preconditions потрібні для binary search і чому вставка в sorted list все ще може бути O(n)?"
description: "Binary search вимагає відсортованої послідовності; bisect знаходить позицію вставки за O(log n), але list.insert() зсуває елементи за O(n)."
track: cs
section: algorithms
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
  - source_id: py314-library-collections
    title: "Python 3.14: Library/collections"
    url: https://docs.python.org/3.14/library/collections.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-heapq
    title: "Python 3.14: Library/heapq"
    url: https://docs.python.org/3.14/library/heapq.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-bisect
    title: "Python 3.14: Library/bisect"
    url: https://docs.python.org/3.14/library/bisect.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/computer_science/algorithmes.md#L168-L198
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Binary search вимагає відсортованої послідовності; `bisect` знаходить позицію вставки за O(log n), але `list.insert()` зсуває елементи за O(n).**[^py314-library-collections] Передумова – відсортований input: `bisect_left` і `bisect_right` покладаються на порядок за `__lt__`. Навіть якщо сам пошук логарифмічний, вставка в `list` усе одно потребує зсуву до n елементів, тому сумарна вартість вставки – O(n).

## Detailed explanation

`bisect` не перевіряє впорядкованість вхідної послідовності – це контракт, а не runtime-перевірка.
Якщо список не відсортований, `bisect_left`/`bisect_right` все одно повернуть якийсь індекс без
помилки, просто цей індекс не гарантує коректного порядку після вставки. Єдина вимога до
елементів – існування тотального порядку через `__lt__`; `bisect` ніколи не викликає `__eq__`
напряму, тому кастомний клас з визначеним лише `__lt__` уже придатний для пошуку.

Для дублікатів `bisect_left` повертає позицію першого входження, а `bisect_right` – позицію одразу
після останнього; це дає змогу керувати стабільністю вставки відносно рівних елементів, не
змінюючи сам алгоритм пошуку.[^py314-library-bisect]

Причина, чому `list.insert()` залишається O(n) навіть після O(log n) пошуку позиції, – у самій
структурі даних: Python `list` – це суцільний масив покажчиків, і вставка в середину вимагає
фізично зсунути всі елементи праворуч від точки вставки на одну позицію в пам'яті. Це не залежить
від того, як швидко знайдено позицію – хоч би й миттєво. Заміна на `collections.deque` тут не
рятує: `deque` дає O(1) додавання й вилучення з обох кінців, але вставка чи вилучення в довільній
середній позиції – так само O(n), бо це двобічна черга, а не структура з довільним доступом до
середини за O(log n).[^py314-library-collections]

Структура, яка дійсно дає O(log n) і для пошуку, і для вставки, – це самобалансована структура з
упорядкованим індексом (наприклад, skip list або balanced BST з підтримкою rank), а не масив і не
однозв'язний список: однозв'язний список дає O(1) вставку, коли позиція вже відома, але сам пошук
позиції в ньому лінійний, бо немає довільного доступу за індексом, потрібного для бінарного поділу
діапазону.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
