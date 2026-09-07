---
id: emb-cemb-0029
title: "Why is structure alignment needed in C, and how does it affect memory layout?"
description: "Alignment determines structure field addresses, and padding can change the actual memory layout and size."
track: embedded
section: c-in-embedded
level: middle
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

**Alignment** forces structure fields to start at addresses that are multiples of their type's or ABI's requirements. The compiler may insert padding between fields and at the end of the structure, so the actual layout does not always equal the sum of field sizes.[^dou-embedded-interview] For DMA, MMIO mirror structures, and binary protocols this is critical: the layout must be fixed explicitly or serialized manually.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
