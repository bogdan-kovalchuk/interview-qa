---
id: emb-volconst-0055
title: "Trap: what is wrong with this register address declaration?"
description: "This creates a separate object and initializes it once with the value read from the register."
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
volatile uint32_t GPIOA_ODR = *(volatile uint32_t *)0x40020014;
```

## Short answer

<span class="warn">This creates a separate object and initializes it once with the value read from the register; it is not an alias for the register address.</span>[^iso-c-n1570]

After initialization, `GPIOA_ODR` is a separate object. Writing to it will not write the hardware register.

To access the register, use an lvalue through a pointer or a macro, according to the MCU memory map and compiler rules.[^iso-c-n1570]

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
