---
id: emb-cemb-0014
title: "What is a pointer?"
description: "A pointer is a variable that stores the address of another object or function; it enables pass-by-reference, arrays, dynamic memory, and memory-mapped I/O."
track: embedded
section: c-in-embedded
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
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for c in embedded concepts; details of specific devices and toolchains can differ."
---

## Short answer

**A pointer** is a variable that stores the address of another object or function in memory.[^dou-embedded-interview] For example: `int x = 10; int *p = &x;`. The `&` operator takes the address, and `*p` dereferences the pointer and provides access to the value.

Pointers are needed for passing objects to functions without copying, working with arrays, dynamic memory, callbacks, data structures, and memory-mapped registers. Dangers: `NULL`, dangling pointer, out-of-bounds array access, incorrect type casting.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
