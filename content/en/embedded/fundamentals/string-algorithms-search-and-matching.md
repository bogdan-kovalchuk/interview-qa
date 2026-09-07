---
id: emb-fund-0005
title: "What string algorithms do you know?"
description: "Basic string operations are complemented by KMP, Rabin-Karp, and Boyer-Moore substring search algorithms."
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

Basic operations: searching for a character or substring, comparison, copying, concatenation, tokenization, reverse, palindrome check, character frequency counting.[^dou-embedded-interview] In C you need to watch `\0`, buffer size, and overflow especially carefully.

Well-known algorithms: **KMP** for substring search in O(n+m), **Rabin-Karp** with a rolling hash, **Boyer-Moore** for fast practical search, Trie for a set of strings, Levenshtein distance for string similarity. For embedded, simple algorithms without heap and with controlled execution time are often important.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
