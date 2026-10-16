---
id: emb-fund-0009
title: "Які алгоритми на графах знаєте?"
track: embedded
section: fundamentals
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
---

## Short answer

Граф складається з вершин і ребер; може бути орієнтованим/неорієнтованим, зваженим/незваженим. Базові обходи: **DFS** і **BFS**; BFS знаходить найкоротший шлях у незваженому графі.[^dou-embedded-interview]

Для найкоротших шляхів: `Dijkstra` для невід'ємних ваг, `Bellman-Ford` допускає від'ємні ребра, `Floyd-Warshall` рахує всі пари. Для мінімального остовного дерева: `Kruskal` і `Prim`. Також часто питають topological sort для DAG, пошук циклів і компоненти зв'язності.

## Detailed explanation

TODO
