---
id: emb-memlink-0003
title: "What is realloc used for?"
description: "realloc resizes a previously allocated heap block in place when possible or copies to a new block, leaving the old pointer valid on failure."
track: embedded
section: memory-and-linker
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 3
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
  - source_id: gnu-ld-manual
    title: "GNU linker ld manual"
    url: https://sourceware.org/binutils/docs/ld/index.html
    accessed: 2026-09-06
    kind: official
    version: "2.47"
    applicability: "Authoritative section-level reference for memory and linker concepts; details of specific devices and toolchains can differ."
---

## Short answer

`realloc(ptr, new_size)` resizes a previously allocated heap block[^dou-embedded-interview]: if space is available next to it, the block is extended in place; otherwise a new block is allocated, the old data is copied, and the old block is freed.

Typical use: dynamic arrays, input buffers, variable-length strings. Important pattern: `tmp = realloc(ptr, n); if (tmp) ptr = tmp;`, because on failure `realloc` returns `NULL` while the old `ptr` stays valid. `realloc(NULL, size)` works like `malloc`; portable code should not rely on `realloc(ptr, 0)`: on many implementations it behaves like `free(ptr)`, but the details depend on the standard and implementation.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
