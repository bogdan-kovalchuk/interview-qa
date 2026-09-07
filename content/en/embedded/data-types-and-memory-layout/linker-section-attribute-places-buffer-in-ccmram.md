---
id: emb-dtypes-0050
title: "What does this do? `__attribute__((section(\".ccmram\"))) uint32_t fast_buf[256];`"
description: "The section attribute places the array in .ccmram, a zero-wait-state RAM for time-critical buffers."
track: embedded
section: data-types-and-memory-layout
level: middle
type: mechanism
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

Places the array in the **.ccmram** section (Core Coupled Memory RAM) on STM32 F4/F7 – a dedicated RAM connected directly to the CPU without a bus matrix.

Provides **zero-wait-state** access: ideal for time-critical buffers, lookup tables, ISR stacks.

Required: 1. Define the section in the linker script (`MEMORY { CCMRAM ... }`); 2. Initialize in startup code; Not available to DMA on some MCUs – check the reference manual.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
