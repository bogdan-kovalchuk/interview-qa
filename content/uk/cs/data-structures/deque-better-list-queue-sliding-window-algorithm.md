---
id: cs-dstruct-0002
title: "Коли `deque` кращий за `list` для queue або sliding-window algorithm?"
description: "deque дає O(1) для append і pop з обох кінців, тоді як list коштує O(n) для pop(0) або insert(0, v), бо елементи доводиться зсувати в пам'яті."
track: cs
section: data-structures
level: middle
type: comparison
tags: [deque, list]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/computer_science/data_structures.md#L367-L398
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`deque` дає O(1) для append і pop з обох кінців, тоді як `list` коштує O(n) для `pop(0)` або `insert(0, v)`, бо елементи доводиться зсувати в пам'яті.**[^py314-library-collections] Для FIFO-черги або sliding-window алгоритму, що додає/видаляє елементи на початку, `collections.deque` уникає цієї лінійної вартості. Використовуйте `list`, коли append/pop потрібні лише в кінці (стек) або потрібен O(1) доступ за індексом.

## Detailed explanation

`collections.deque` реалізований як двобічно зв'язаний список блоків фіксованого розміру (а не
окремих елементів), тому кожен блок містить кілька покажчиків підряд – це дає кращу локальність
кешу, ніж класичний однозв'язний список, і водночас O(1) амортизовану вартість для `append`,
`appendleft`, `pop`, `popleft`, бо додавання чи вилучення на краю ніколи не потребує зсуву інших
елементів.

`list`, навпаки, – це суцільний масив покажчиків. `append`/`pop` у кінці – O(1) амортизовано
(Python інколи виділяє масив із запасом), а `pop(0)`/`insert(0, v)` вимагають фізично зсунути всі
інші елементи на одну позицію, тобто O(n).

Це напряму пояснює, чому `deque` – природний вибір для sliding-window алгоритмів: класичний
приклад – пошук максимуму в кожному вікні розміру k (`monotonic deque`), де елементи одночасно
додаються з правого краю й видаляються з лівого, а deque з обох боків тримає O(1). Реалізація
того самого патерну на `list` мала б O(n) вартість на кожне вилучення зліва, тобто O(n*k)
сумарно замість O(n).

Плата за цю перевагу – втрата довільного доступу за індексом: `deque[i]` для `i` в середині –
O(n), бо потрібно пройти блоки послідовно від найближчого краю, тоді як `list[i]` – завжди O(1),
бо це прямий обчислений зсув у суцільному масиві. Так само зрізи (`deque[a:b]`) не підтримуються
нативно так ефективно, як `list[a:b]`.

Тому вибір – це компроміс: якщо алгоритм переважно працює з краями послідовності (черга, стек,
sliding window), `deque` вигідніший; якщо потрібен частий довільний доступ за індексом або
зрізи, `list` залишається кращим, навіть коли зрідка трапляється вставка на початку.
[^py314-library-collections]

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
