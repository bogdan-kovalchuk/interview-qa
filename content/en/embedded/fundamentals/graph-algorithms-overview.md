---
id: emb-fund-0009
title: "What graph algorithms do you know?"
track: embedded
section: fundamentals
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
---

## Short answer

A graph consists of vertices and edges; it can be directed/undirected, weighted/unweighted. Basic traversals: **DFS** and **BFS**; BFS finds the shortest path in an unweighted graph.[^dou-embedded-interview]

For shortest paths: `Dijkstra` for non-negative weights, `Bellman-Ford` allows negative edges, `Floyd-Warshall` computes all pairs. For minimum spanning tree: `Kruskal` and `Prim`. Also commonly asked: topological sort for DAGs, cycle detection, and connected components.

## Detailed explanation

TODO
