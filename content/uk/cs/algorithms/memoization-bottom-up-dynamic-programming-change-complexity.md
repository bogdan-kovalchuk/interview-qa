---
id: cs-algo-0003
title: "Як мемоїзація або bottom-up dynamic programming змінює complexity recursive solution з overlapping subproblems?"
description: "Мемоїзація або bottom-up DP зводить рекурсію з експоненційним часом і overlapping subproblems до поліноміального часу, розв'язуючи кожен унікальний subproblem лише один раз."
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/computer_science/algorithmes.md#L516-L530
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Мемоїзація або bottom-up DP зводить рекурсію з експоненційним часом і overlapping subproblems до поліноміального часу, розв'язуючи кожен унікальний subproblem лише один раз.**[^py314-library-collections] Наприклад, наївний рекурсивний Fibonacci має складність O(2^n), але з таблицею memo кожен з n subproblems обчислюється один раз – це дає O(n) часу і O(n) пам'яті. Компроміс – додаткова пам'ять під кеш замість повторних обчислень.

## Detailed explanation

Наївна рекурсія над задачею з overlapping subproblems будує дерево викликів, розмір якого залежить
від кількості *шляхів* до кожного стану, а не від кількості самих станів. Для Fibonacci станів
усього n + 1, але дерево викликів має розмір O(2^n), бо кожен стан fib(k) перераховується стільки
разів, скільки існує шляхів рекурсії, що до нього ведуть.

Мемоїзація ламає це дерево назад у граф: перед обчисленням стану перевіряють таблицю, і якщо стан
уже є – повертають готове значення замість повторного спуску. Коли стан описується кількома
параметрами, його зводять до hashable ключа – кортежу або, для читабельності,
namedtuple.[^py314-library-collections] Кожен унікальний стан тоді обчислюється рівно один раз, і
сумарний час стає O(кількість станів × вартість переходу без урахування рекурсивних викликів) –
O(n) для Fibonacci замість O(2^n).

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

Отже обидва підходи прибирають експоненційне дублювання роботи, перетворюючи задачу з O(2^n) на
O(кількість унікальних станів); компроміс між ними – рекурсія з лінивим обчисленням проти ітерації
з можливістю стиснути пам'ять.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
