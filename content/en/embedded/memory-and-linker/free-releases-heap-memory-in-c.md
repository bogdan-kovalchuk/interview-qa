---
id: emb-memlink-0001
title: "How do you free memory in C?"
description: "Memory allocated by malloc, calloc, or realloc is released with free, and the pointer should be set to NULL to avoid a dangling pointer."
track: embedded
section: memory-and-linker
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
  - source_id: gnu-ld-manual
    title: "GNU linker ld manual"
    url: https://sourceware.org/binutils/docs/ld/index.html
    accessed: 2026-09-06
    kind: official
    version: "2.47"
    applicability: "Authoritative section-level reference for memory and linker concepts; details of specific devices and toolchains can differ."
---

## Short answer

With the `free(ptr)` function from `<stdlib.h>`.[^dou-embedded-interview] After the call, every pointer to that block becomes a <span class="warn">dangling pointer</span>. It is common practice to null out the variable right away: `free(ptr); ptr = NULL;`.

Important caveat: this only helps for that one pointer variable. Other copies of the same address are still dangling, so ownership must be tracked; rules: only free what was allocated via `malloc`/`calloc`/`realloc`; never double free; never free stack or static objects.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
