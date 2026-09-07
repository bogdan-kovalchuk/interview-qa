---
id: emb-volconst-0004
title: "Trap: does `volatile` make an operation atomic?"
description: "No, volatile does not guarantee atomicity; it only forces the compiler to perform a memory access."
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

<span class="warn">No. `volatile` does not guarantee atomicity.</span> It only forces the compiler to perform a memory access: for example, a `volatile uint32_t` on an 8-bit MCU may be read in several instructions, and an ISR can fire between bytes and see a partially updated value; even on Cortex-M, `counter++` is a read-modify-write, not a single indivisible operation.

Mitigation: for shared state use atomic operations, a critical section, briefly disabling interrupts, or dedicated CMSIS/RTOS primitives.[^embeddedinterviewlab]

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
