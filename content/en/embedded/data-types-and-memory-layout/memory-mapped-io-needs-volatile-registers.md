---
id: emb-dtypes-0032
title: "What is memory-mapped I/O, and why do such registers need `volatile`?"
description: "Peripheral registers are accessed like ordinary memory, and volatile stops the compiler from caching or eliding accesses to them."
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

**Memory-mapped I/O** – peripheral registers (GPIO, UART, ADC) are accessible at fixed addresses in the CPU address space like ordinary memory.

`volatile` is required because:
1. The value can change by hardware between reads (status register).
2. Without `volatile` the compiler may eliminate a "redundant" write (dead store) or cache the value in a register.

Correct: `volatile uint32_t * const GPIOA_ODR = (volatile uint32_t*)0x40020014U;`[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
