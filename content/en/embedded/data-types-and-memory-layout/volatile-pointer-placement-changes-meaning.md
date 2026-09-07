---
id: emb-dtypes-0046
title: "What's the difference: `volatile int *reg` vs `int * volatile reg`?"
description: "volatile int reg makes the pointed-to data volatile, while int volatile reg makes the pointer itself volatile."
track: embedded
section: data-types-and-memory-layout
level: middle
type: pitfall
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

`volatile int *reg` – a pointer to a **volatile int**: every `*reg` is a real read/write (not optimized away). The pointer `reg` itself is not volatile. The **correct** choice for memory-mapped registers.

`int * volatile reg` – a **volatile pointer** to a regular int: the address is not optimized, but `*reg` may be cached.

For registers: `volatile uint32_t * const GPIOA = (volatile uint32_t*)0x40020000U;`[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
