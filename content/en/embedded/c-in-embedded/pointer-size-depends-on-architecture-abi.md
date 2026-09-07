---
id: emb-cemb-0004
title: "What is the size of a pointer, and what does it depend on?"
description: "Pointer size depends on the architecture address space and ABI, not on the pointed-to type; typical values are 2, 4, or 8 bytes."
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

The size of a pointer depends on the architecture's address space and ABI, not on the type it points to.[^dou-embedded-interview] On a 32-bit system, `sizeof(void*) == 4` is typical; on 64-bit – `8`; on 16-bit – `2`.

`int *`, `char *`, and `struct Foo *` usually have the same size within one platform because they all store an address. In embedded, there may be nuances with different memory spaces or function pointers, so the correct answer is to check with `sizeof(pointer)` for the specific compiler and target.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
