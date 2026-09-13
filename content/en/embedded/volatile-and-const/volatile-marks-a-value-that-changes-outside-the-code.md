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
updated: 2026-09-13
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

**`volatile`** means an object's value can change outside the visible flow of the program: by hardware, an ISR, DMA or another asynchronous mechanism.

The compiler must then perform a real memory access on every read and write instead of keeping the value in a CPU register. On Cortex-M that is critical for memory-mapped registers: a read can return peripheral state and a write can trigger a hardware action.

Rule: `volatile` is not applied for reliability, only where the object genuinely changes outside ordinary C code.[^embeddedinterviewlab]
## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
