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
typedef struct {
  volatile uint32_t CR;  // control
  volatile uint32_t SR;  // status
  volatile uint32_t DR;  // data
} USART_t;
#define USART1 ((USART_t *)0x40011000U)
```

## Short answer

**A struct with `volatile` fields overlaid on the peripheral base address.**

Fields follow a register-compatible order, but their required offsets must be checked against the datasheet: C permits padding between structure members. Access looks like `USART1->DR = b;`.[^iso-c-n1570]

Rule: lock down the layout with `offsetof` asserts so the match with the datasheet does not break.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
