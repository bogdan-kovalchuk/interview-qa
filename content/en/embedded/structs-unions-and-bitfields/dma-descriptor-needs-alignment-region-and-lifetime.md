---
id: emb-structs-0043
title: "Trap: why can a DMA descriptor struct not simply sit on the stack?"
description: "DMA may require specific alignment, memory region, and a lifetime longer than the stack frame."
track: embedded
section: structs-unions-and-bitfields
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

<span class="warn">DMA may require specific alignment, memory region, and a lifetime longer than the stack frame.</span>

A stack object can disappear after the function returns, be misaligned for the DMA engine, or reside in cacheable RAM without clean/invalidate. The descriptor struct must also have a layout that exactly matches the hardware manual.

Mitigation: DMA descriptors are typically made `static`, aligned, placed in the correct linker section, with explicit barriers and cache maintenance.[^embeddedinterviewlab]

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
