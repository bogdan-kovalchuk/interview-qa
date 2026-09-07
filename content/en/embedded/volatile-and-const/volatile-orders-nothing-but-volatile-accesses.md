---
id: emb-volconst-0038
title: "Why is `volatile` not a memory barrier?"
description: "volatile constrains optimizations of accesses to volatile objects but is not a full memory barrier for all memory."
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

**`volatile` constrains optimizations of accesses to volatile objects, but it is not a full CPU/compiler memory barrier for all memory.**

The compiler must preserve the order of volatile accesses relative to other volatile accesses, but this does not imply cache synchronization, bus ordering, DMA visibility, or inter-core ordering. On Cortex-M, device memory often has stronger ordering, but DMA and peripheral scenarios may still require barriers and cache maintenance.

Rule: for hardware ordering, use architectural primitives such as `__DMB()`, `__DSB()`, `__ISB()` where the reference manual requires them.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
