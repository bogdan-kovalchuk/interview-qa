---
id: emb-volconst-0008
title: "How do you correctly declare a memory-mapped 32-bit register at `0x40020014`?"
description: "A memory-mapped register must be cast to a pointer to volatile so every access actually reaches the hardware bus address."
track: embedded
section: volatile-and-const
level: junior
type: mechanism
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

Typical form: `#define GPIOA_ODR (*(volatile uint32_t *)0x40020014u)`.

Here `volatile uint32_t *` means pointer to volatile 32-bit data. Every read or write through the macro must actually access the bus address. This matters for GPIO, timer, UART, ADC, and other Cortex-M peripheral registers.

Rule: a peripheral register address must be explicitly cast to a pointer-to-volatile object; otherwise the optimiser does not know that hardware sits at that address.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
