---
id: emb-volconst-0058
title: "What does `volatile uint8_t rx_buf[64]` mean for a DMA receive buffer?"
description: "Each element of the array has a volatile-qualified type, so reading rxbuf[i] must be a real memory access."
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

**Each element of the array has a volatile-qualified type**, so reading `rx_buf[i]` must be a real memory access.

This can be needed if DMA modifies bytes outside the CPU control flow. But it does not solve cache coherency, does not guarantee that DMA has already finished writing, and does not make multi-byte parsing atomic.

Rule: a volatile buffer can be part of a DMA protocol, but completion flags, barriers/cache maintenance, and ownership discipline are also needed.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
