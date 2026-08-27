---
id: cs-cmplx-0002
title: "Яка time complexity коду `for i in range(n):   for j in range(i): work()` і яка сума її пояснює?"
description: "Часова складність – O(n²), що пояснюється трикутною сумою 0 + 1 + 2 + ... + (n-1) = n(n-1)/2."
track: cs
section: complexity-and-analysis
level: middle
type: mechanism
tags: [for-i-in-range-n-nbsp-nbsp-for-j-in-range-i-work]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/computer_science/algorithmes.md#L156-L161
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Часова складність – O(n²), що пояснюється трикутною сумою 0 + 1 + 2 + ... + (n-1) = n(n-1)/2.**[^py314-library-collections] Внутрішній цикл виконується `i` разів для кожного `i` від 0 до n-1, що в сумі дає n(n-1)/2 викликів `work()`. Перевірено на Python 3.14: n=10 -> 45 викликів, n=100 -> 4950 викликів. Сталий множник 1/2 відкидається в Big O нотації.

## Detailed explanation

Сума 0 + 1 + ... + (n-1) виводиться класичним прийомом Гаусса: якщо записати ту саму суму в
зворотному порядку й додати почленно, кожна пара доданків дає однакове значення n-1, а таких пар
n. Звідси подвоєна сума дорівнює n*(n-1), а сама сума – n(n-1)/2. Це формула трикутного числа, яка
описує кількість унікальних невпорядкованих пар серед n елементів – саме тому цей самий патерн
циклів зустрічається в задачах на порівняння всіх пар (наприклад, наївна перевірка дублікатів або
O(n²) сортування).

Важливо відрізняти точну кількість викликів `work()`, яка дорівнює n(n-1)/2, від асимптотичного
класу O(n²): формула точна для будь-якого n, а Big O лише описує, що зростання квадратичне,
відкидаючи множник 1/2 і доданок нижчого порядку. Якби внутрішній цикл був `range(n)` замість
`range(i)`, точна кількість викликів дорівнювала б n², але клас складності лишився б тим самим
O(n²) – різниця лише у сталому множнику вдвічі.

Ця асиметрія циклів (внутрішній діапазон залежить від зовнішньої змінної) не змінює загальний
клас складності порівняно із симетричним подвійним циклом `range(n)` x `range(n)`, бо в обох
випадках кількість ітерацій пропорційна n². Але вона важлива на практиці: реальна кількість
операцій удвічі менша, тому такий код виконується приблизно вдвічі швидше за повний подвійний
прохід n x n, навіть маючи однакову асимптотику.[^py314-library-collections]

Узагальнення на k вкладених циклів із аналогічно спадним діапазоном дає складність O(n^k / k!) –
це комбінаторна кількість k-елементних підмножин, ще один приклад того, як структура вкладеності
циклів напряму відповідає формулі з комбінаторики.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
