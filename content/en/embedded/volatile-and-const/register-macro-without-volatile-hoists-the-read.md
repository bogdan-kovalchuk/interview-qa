---
id: emb-volconst-0007
title: "Trap: what is wrong with this polling code?"
description: "The hardware register access is missing volatile, so the compiler can cache the first read and polling may hang."
track: embedded
section: volatile-and-const
level: junior
type: pitfall
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

## Question code

```c
#define UART_SR (*( uint32_t *)0x40011000)

while ((UART_SR & 0x20) == 0) { }
```

## Short answer

<span class="warn">The memory-mapped register access is not `volatile`.</span>

`UART_SR` dereferences a plain `uint32_t *`, so the C compiler is not required to treat each access as volatile; an optimisation may remove repeated reads. In a release build, polling may then miss a change to the status register.[^iso-c-n1570]

Use `#define UART_SR (*(volatile uint32_t *)0x40011000u)` and check that the address and access width match the MCU documentation. `volatile` does not prove that the address is correct or that the peripheral supports that access.[^iso-c-n1570]

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
