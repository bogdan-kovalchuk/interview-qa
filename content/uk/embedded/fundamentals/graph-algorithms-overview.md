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
updated: 2026-09-06
content_revision: 1
reconciled_with:
  en: 1
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
---

## Short answer

Граф складається з вершин і ребер; може бути орієнтованим/неорієнтованим, зваженим/незваженим. Базові обходи: <span class="key">DFS</span> і <span class="key">BFS</span>; BFS знаходить найкоротший шлях у незваженому графі.[^dou-embedded-interview]

Для найкоротших шляхів: <code>Dijkstra</code> для невід'ємних ваг, <code>Bellman-Ford</code> допускає від'ємні ребра, <code>Floyd-Warshall</code> рахує всі пари. Для мінімального остовного дерева: <code>Kruskal</code> і <code>Prim</code>. Також часто питають topological sort для DAG, пошук циклів і компоненти зв'язності.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
