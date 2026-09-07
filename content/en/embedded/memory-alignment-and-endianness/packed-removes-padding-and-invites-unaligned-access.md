---
id: emb-align-0009
title: "What does `__attribute__((packed))` do and why is it dangerous?"
description: "The packed attribute removes padding but risks misaligned access and HardFault on some cores"
track: embedded
section: memory-alignment-and-endianness
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

**Removes padding** – fields are placed back-to-back and the size approaches the sum of the fields.

<span class="warn">Risk</span>: a multi-byte field may end up at a misaligned address. On Cortex-M0 direct access to such a field can cause a HardFault; on M3/M4 the compiler often generates <span class="warn">byte-wise load/store</span> instructions, which are slower.

Rule: `packed` is for wire formats and protocol headers. For MMIO (memory-mapped I/O) register maps a naturally aligned `volatile` struct with explicit reserved fields is usually better, to avoid incorrect access width to registers.[^embeddedinterviewlab]

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
