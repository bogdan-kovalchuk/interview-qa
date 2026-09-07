---
id: emb-fund-0007
title: "What are sorting algorithms, and which ones do you know?"
description: "Sorting algorithms order elements by key; bubble and insertion sort are simple and O(n²), while merge, quick, and heap sort are typically O(n log n)."
track: embedded
section: fundamentals
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of this question and answer; the answer text is not independently verified against the original community Anki deck."
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Authoritative section-level reference for fundamentals concepts; details of specific devices and toolchains can differ."
---

## Short answer

A sorting algorithm orders elements by key: ascending, descending, or a custom comparator[^dou-embedded-interview]; important characteristics are time complexity, extra memory, stability, and behavior on nearly sorted data.

`bubble sort` and `insertion sort` are simple but usually O(n²), with insertion sort being good for small arrays. `merge sort` is stable and O(n log n) but needs extra memory; `quick sort` is fast in practice, O(n log n) on average, but O(n²) worst case; `heap sort` is O(n log n) and works in-place.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
