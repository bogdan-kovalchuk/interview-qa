---
id: emb-cemb-0010
title: "What is alignment in structs?"
description: "Alignment places struct fields at addresses that are multiples of their alignment requirements; the compiler adds padding for fast and correct CPU access."
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

**Alignment** means that struct fields are placed at addresses that are multiples of their alignment requirements.[^dou-embedded-interview] For example, `uint32_t` often requires an address that is a multiple of 4. The compiler inserts unused padding bytes so that access is fast and correct for the CPU.

This matters in embedded: misaligned access on some MCUs is slow or triggers a fault, and register or protocol layout may require exact offsets. Size can be reduced by reordering fields from largest to smallest, but for a binary protocol or hardware registers it is better to serialize data explicitly or verify the layout with `static_assert` and `offsetof`.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
