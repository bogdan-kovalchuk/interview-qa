---
id: emb-fund-0007
title: "What are sorting algorithms, and which ones do you know?"
track: embedded
section: common-code-patterns
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
---

## Short answer

A sorting algorithm orders elements by key: ascending, descending, or a custom comparator[^dou-embedded-interview]; important characteristics are time complexity, extra memory, stability, and behavior on nearly sorted data.

`bubble sort` and `insertion sort` are simple but usually O(n²), with insertion sort being good for small arrays. `merge sort` is stable and O(n log n) but needs extra memory; `quick sort` is fast in practice, O(n log n) on average, but O(n²) worst case; `heap sort` is O(n log n) and works in-place.

## Detailed explanation

TODO
