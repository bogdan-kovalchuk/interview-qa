---
id: emb-volconst-0001
title: "What does the `volatile` qualifier mean in C?"
description: "volatile means the value of an object can change outside the visible program flow, by hardware, ISR, DMA, or another asynchronous mechanism."
track: embedded
section: volatile-and-const
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

**`volatile`** means that the value of an object can change outside the visible flow of the program: by hardware, an ISR, DMA, or another asynchronous mechanism.

The compiler must perform an actual memory access for every read or write of such an object, rather than keeping the value only in a CPU register. For Cortex-M this is critical for memory-mapped registers: reading an address can return peripheral state, and writing can trigger a hardware action.

Rule: `volatile` is not applied for reliability, only when the object can genuinely change outside the control of ordinary C code.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
