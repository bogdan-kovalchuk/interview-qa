---
id: emb-volconst-0039
title: "Trap: is `volatile` enough for a DMA buffer?"
description: "volatile is not always enough for a DMA buffer."
track: embedded
section: volatile-and-const
level: junior
type: pitfall
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

<span class="warn">Not always.</span>

`volatile` can force the CPU to re-read a descriptor or flag that DMA modifies. But it does not address cache coherency, alignment, ownership, memory barriers, or race conditions. On a Cortex-M7 with D-cache, DMA can write to RAM while the CPU still reads stale cache lines.

Protection: beyond correct volatile flags and descriptors, use non-cacheable memory or cache clean/invalidate, barriers, and a clear ownership protocol between the CPU and DMA.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
