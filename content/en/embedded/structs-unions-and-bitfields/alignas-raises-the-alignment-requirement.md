---
id: emb-structs-0042
title: "What does `alignas`/`_Alignas` or a compiler-specific alignment attribute do?"
description: "Sets or strengthens the alignment requirement of an object or type."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  uk: 1
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
---

## Short answer

**Sets or strengthens the alignment requirement of an object or type.**

In embedded, this is needed for DMA buffers, cache line alignment, vector tables, or peripheral requirements. For example, a DMA descriptor may require 16-byte alignment; cache maintenance on Cortex-M7 often operates on cache lines.

Rule: alignment is part of the hardware contract. Check the address at runtime or compile time and describe the requirement in the type/attribute/linker script.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
