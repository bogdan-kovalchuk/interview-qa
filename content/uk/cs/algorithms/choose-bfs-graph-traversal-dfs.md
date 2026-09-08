---
id: cs-algo-0002
title: "Коли для graph traversal обрати BFS, а коли DFS?"
description: "BFS обходить граф рівень за рівнем через queue і знаходить найкоротший шлях у неважених графах; DFS йде вглиб через stack і використовує менше пам'яті на широких графах."
track: cs
section: algorithms
level: middle
type: comparison
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
    applicability: "Розділи 20-22 підтверджують складність BFS/DFS, найкоротші шляхи в неважених графах і застосування DFS."
  - source_id: py314-library-collections
    title: "Python 3.14: Library/collections"
    url: https://docs.python.org/3.14/library/collections.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/computer_science/algorithmes.md#L416-L436
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**BFS обходить граф рівень за рівнем через queue і знаходить найкоротший шлях у неважених графах;
DFS йде вглиб через stack і може тримати менший фронт на широких неглибоких графах.**[^clrs-4e]
Обирайте BFS, коли потрібен найкоротший шлях або обхід за рівнями, а DFS – для topological sorting
чи дослідження вглиб. Під час обходу графа обом алгоритмам також може знадобитися visited set
розміром O(V); звичне порівняння O(width) проти O(depth) стосується queue або stack.

## Detailed explanation

З visited set обидва алгоритми обробляють кожну досяжну вершину й ребро сталу кількість разів,
тому асимптотика становить O(V + E) на adjacency list.[^clrs-4e] Різниця – в порядку
відвідування, і саме він визначає доступні властивості шляху.

BFS тримає FIFO queue: вершина виходить із черги в тому ж порядку, в якому туди зайшла, і граф
розгортається "хвилями" за відстанню від старту. Тому перший знайдений шлях до будь-якої вершини –
найкоротший за кількістю ребер, а не за вагою. У Python для такої черги типово беруть
`collections.deque`, бо `append`/`popleft` там O(1); список дав би O(n) на вилученні з
початку.[^py314-library-collections] Хвильова структура BFS також дає multi-source BFS
"безкоштовно" – можна одразу порахувати відстані від кількох стартових вершин.

DFS натомість заглиблюється в одну гілку до кінця і повертається назад лише після тупика,
використовуючи явний stack або стек викликів. Активний шлях може займати O(depth), тоді як queue
BFS може зрости до O(width). Це порівняння не враховує visited set для загального графа, який в
обох обходах може займати O(V). Ітеративний DFS також може зберігати кілька відкладених сусідів,
тому O(depth) не є універсальною межею всієї пам'яті кожної реалізації.

Порядок обходу DFS – зокрема post-order – є основою topological sorting і пошуку strongly
connected components.[^clrs-4e] У directed graph знайдене DFS зворотне ребро виявляє цикл; в
undirected graph з цієї перевірки треба виключити ребро до батьківської вершини.

Отже:

- якщо потрібна найкоротша за ребрами відстань або обхід рівнями – BFS;
- якщо потрібен топологічний порядок або дослідження вглиб – DFS; у широкому неглибокому графі
  його активний фронт може бути меншим за фронт BFS, але visited set треба рахувати окремо.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
