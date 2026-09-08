---
id: cs-algo-0003
title: "Як мемоїзація або bottom-up dynamic programming змінює complexity recursive solution з overlapping subproblems?"
description: "Мемоїзація або bottom-up DP усуває повторне обчислення overlapping subproblems, але не гарантує поліноміального часу, якщо простір станів експоненційний."
track: cs
section: algorithms
level: senior
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
  - source_id: clrs-4e
    title: "Introduction to Algorithms, fourth edition"
    url: https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/
    accessed: 2026-09-08
    kind: book
    version: "4th edition"
    applicability: "Розділ 14 підтверджує принципи memoization, bottom-up dynamic programming і аналіз складності за простором станів."
  - source_id: py314-library-collections
    title: "Python 3.14: Library/collections"
    url: https://docs.python.org/3.14/library/collections.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/computer_science/algorithmes.md#L516-L530
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Memoization або bottom-up DP усуває повторне обчислення overlapping subproblems, розв'язуючи
кожен досяжний стан один раз.**[^clrs-4e] Отриманий час приблизно дорівнює кількості досяжних
станів, помноженій на вартість переходу, тому він поліноміальний лише тоді, коли простір станів і
робота переходу поліноміальні. Для Fibonacci це змінює експоненційну рекурсію на O(n) часу й O(n)
пам'яті memo table.

## Detailed explanation

Наївна рекурсія над задачею з overlapping subproblems будує дерево викликів, розмір якого залежить
від кількості *шляхів* до кожного стану, а не від кількості самих станів. Для Fibonacci станів
усього n + 1, але дерево викликів має розмір O(2^n), бо кожен стан fib(k) перераховується стільки
разів, скільки існує шляхів рекурсії, що до нього ведуть.

Мемоїзація згортає це дерево назад у граф: перед обчисленням стану перевіряють таблицю, і якщо стан
уже є – повертають готове значення замість повторного спуску. Коли стан описується кількома
параметрами, його зводять до hashable ключа – кортежу або, для читабельності,
namedtuple.[^py314-library-collections] Кожен унікальний стан тоді обчислюється рівно один раз, і
сумарний час стає O(кількість досяжних станів × вартість переходу без урахування рекурсивних
викликів) – O(n) для Fibonacci замість O(2^n).[^clrs-4e]

Bottom-up DP дає той самий результат іншим шляхом: замість рекурсії "згори" будують таблицю
"знизу", у порядку, що гарантує – коли обчислюється стан k, усі стани, від яких він залежить, уже
готові. Для Fibonacci це просто зростання індексу; для складніших задач – топологічний порядок
залежностей між станами.

Різниця між двома підходами – не в асимптотиці часу, а в тому, що саме обчислюється і скільки
коштує накладна структура:

- top-down memoization обчислює лише ті стани, які реально потрібні для відповіді, але платить
  стеком викликів глибиною O(depth), який може впертися в ліміт рекурсії;
- bottom-up tabulation обчислює всі стани в діапазоні, навіть зайві для конкретного запиту, зате
  уникає рекурсії, і якщо стан залежить лише від сталої кількості попередніх (як у Fibonacci – від
  двох), таблицю можна звести до змінних сталого розміру – O(1) пам'яті замість O(n).

Обидва підходи усувають повторне обчислення того самого стану, але не гарантують поліноміального
алгоритму: задача все одно може мати експоненційно багато різних досяжних станів. Компроміс між
ними – рекурсія з demand-driven evaluation проти ітерації з можливістю стиснути пам'ять.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
