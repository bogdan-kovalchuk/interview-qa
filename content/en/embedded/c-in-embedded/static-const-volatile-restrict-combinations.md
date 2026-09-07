---
id: emb-cemb-0032
title: "Why are static, const, volatile, and restrict used in C, and which combinations make sense?"
description: "These qualifiers express linkage, mutability, observable access, and aliasing contracts in embedded C."
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

`static` controls linkage or storage duration, `const` disallows modification through that lvalue, `volatile` forces actual access execution, and `restrict` promises no aliasing for optimization. For MMIO a typical pointer is: `volatile uint32_t *`; for a read-only register it can be `volatile const uint32_t *`. `static const` often places tables in flash/rodata, and `restrict` is appropriate in DSP/buffer code if the contract is actually honored.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
