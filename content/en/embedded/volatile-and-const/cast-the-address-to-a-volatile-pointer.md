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
updated: 2026-10-04
content_revision: 3
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
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-04; this source is not proof of the claims."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
---

## Short answer

Typical form: `#define GPIOA_ODR (*(volatile uint32_t *)0x40020014u)`.[^iso-c-n1570]

Here `volatile uint32_t *` means pointer to volatile 32-bit data. Dereferencing it produces a volatile lvalue whose access preserves implementation-defined volatile semantics; mapping that to a physical bus access depends on the MCU and compiler.[^iso-c-n1570]

This is a common form for a memory-mapped register, but check the address and permitted access width against the MCU documentation.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
