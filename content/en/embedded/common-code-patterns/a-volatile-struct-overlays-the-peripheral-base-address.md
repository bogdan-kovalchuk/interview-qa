---
id: emb-patterns-0023
title: "How do you describe a peripheral register block with a struct?"
description: "A struct with volatile fields overlaid on the peripheral base address"
track: embedded
section: common-code-patterns
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

## Question code

```c
typedef struct {
  volatile uint32_t CR;  // control
  volatile uint32_t SR;  // status
  volatile uint32_t DR;  // data
} USART_t;
#define USART1 ((USART_t *)0x40011000U)
```

## Short answer

**A struct with `volatile` fields overlaid on the peripheral base address.**

Fields follow the same order and offsets as the registers in the datasheet; access looks like `USART1->DR = b;`. This is exactly how vendor HALs (hardware abstraction layer) such as STM32 HAL, NXP SDK (software development kit), and TI DriverLib define peripheral access.

Rule: lock down the layout with `offsetof` asserts so the match with the datasheet does not break.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
