---
id: emb-volconst-0036
title: "Trap: what is wrong with reading a register and discarding the result?"
description: "If the macro is not volatile, the compiler can remove that read."
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
  - source_id: gcc-volatile
    title: "GCC documentation: Volatiles"
    url: https://gcc.gnu.org/onlinedocs/gcc/Volatiles.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Describes volatile access behavior and discarded scalar expressions in GCC specifically; this is not a universal guarantee for every compiler."
---

## Question code

```c
#define ADC_DR (*( uint32_t *)0x4001204C)

ADC_DR;
```

## Short answer

<span class="warn">If the register lvalue is not volatile-qualified, the compiler can remove the read.</span>

A data-register read may clear a flag or remove a FIFO sample; a plain `uint32_t` expression statement has no observable effect, so the compiler can remove it. GCC treats a discarded scalar volatile expression as a read, although the definition of a volatile access is implementation-defined.

Protection: declare an MMIO register through a volatile-qualified type, such as `(*(volatile uint32_t *)address)`. A `(void)` cast documents intent but does not make an ordinary object volatile.[^gcc-volatile]

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
