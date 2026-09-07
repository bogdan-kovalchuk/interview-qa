---
id: emb-dtypes-0097
title: "What is a memory region, and how is it defined in a linker script?"
description: "A memory region is a named span of address space, defined with attributes and bounds in the MEMORY block."
track: embedded
section: data-types-and-memory-layout
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
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of the question and answer; the answer is not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for data types and memory layout concepts; details of specific devices and toolchains can differ."
---

## Short answer

**Memory region** – a named span of address space. Defined in the `MEMORY` block of a linker script:

`MEMORY {
  FLASH (rx)   : ORIGIN = 0x08000000, LENGTH = 512K
  RAM   (rwx)  : ORIGIN = 0x20000000, LENGTH = 128K
  CCMRAM (rwx) : ORIGIN = 0x10000000, LENGTH = 64K
}`

Attributes: `r` – read, `w` – write, `x` – execute. Sections are bound via `> REGION` in the `SECTIONS` block.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
