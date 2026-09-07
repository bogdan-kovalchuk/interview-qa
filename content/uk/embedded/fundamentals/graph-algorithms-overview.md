---
id: emb-fund-0009
title: "Які алгоритми на графах знаєте?"
description: "Основні алгоритми на графах включають DFS, BFS, алгоритми найкоротших шляхів, пошук мінімального остовного дерева та topological sort."
track: embedded
section: fundamentals
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження цього питання й відповіді; текст відповіді не перевірений незалежно від оригінальної Anki-колоди спільноти."
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Авторитетне джерело рівня секції для понять розділу fundamentals; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

Граф складається з вершин і ребер; може бути орієнтованим/неорієнтованим, зваженим/незваженим. Базові обходи: **DFS** і **BFS**; BFS знаходить найкоротший шлях у незваженому графі.[^dou-embedded-interview]

Для найкоротших шляхів: `Dijkstra` для невід'ємних ваг, `Bellman-Ford` допускає від'ємні ребра, `Floyd-Warshall` рахує всі пари. Для мінімального остовного дерева: `Kruskal` і `Prim`. Також часто питають topological sort для DAG, пошук циклів і компоненти зв'язності.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
