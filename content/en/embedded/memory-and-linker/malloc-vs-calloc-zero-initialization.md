---
id: emb-memlink-0004
title: "What is the difference between malloc and calloc?"
description: "malloc allocates uninitialized bytes with one argument, while calloc allocates n times size bytes, zeros them, and checks for multiplication overflow."
track: embedded
section: memory-and-linker
level: junior
type: comparison
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

`malloc(size)` allocates `size` bytes and <span class="warn">does not initialize</span> them[^dou-embedded-interview] (one argument), whereas `calloc(n, size)` allocates `n * size` bytes and **initializes them to zero** (two arguments; a good implementation also checks for multiplication overflow).

Example: `int *a = malloc(10 * sizeof(int));` – initial values are indeterminate; `int *b = calloc(10, sizeof(int));` – all elements are 0. Both return `NULL` on failure.

## Detailed explanation

TODO

## Comparison

TODO

## When to choose which

TODO

## Sources

<!-- generated from frontmatter -->
