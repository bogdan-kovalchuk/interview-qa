---
id: emb-volconst-0055
title: "Trap: what is wrong with this register address declaration?"
description: "This creates a separate volatile variable and only initializes it with the register value."
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

## Question code

```c
volatile uint32_t GPIOA_ODR = *(volatile uint32_t *)0x40020014;
```

## Short answer

<span class="warn">This creates a separate volatile variable and only initializes it with the register's value.</span>

After initialization `GPIOA_ODR` is not an alias for address `0x40020014`; it is an object in RAM or another section. A write to `GPIOA_ODR` will not write the hardware register.

Defense: use a macro/lvalue or a pointer: `#define GPIOA_ODR (*(volatile uint32_t *)0x40020014u)` or `volatile uint32_t * const GPIOA_ODR = ...`.[^embeddedinterviewlab]

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
