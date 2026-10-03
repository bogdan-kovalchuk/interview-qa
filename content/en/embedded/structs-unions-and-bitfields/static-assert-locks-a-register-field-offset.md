---
id: emb-structs-0008
title: "What does this code check?"
description: "At compile time, it checks offset 0x14 for the ODR field in GPIO_TypeDef."
track: embedded
section: structs-unions-and-bitfields
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
_Static_assert(offsetof(GPIO_TypeDef, ODR) == 0x14,
               "bad GPIO layout");
```

## Short answer

At compile time, it checks that the `ODR` field in `GPIO_TypeDef` has offset `0x14`.

For a peripheral struct overlay this is critical: if preceding fields or reserved gaps are incorrect, `GPIOA->ODR` accesses a different address. On Cortex-M this can mean the wrong peripheral, a silent bug, or a fault.

This requires a correct type definition and `<stddef.h>` for `offsetof`; the assertion checks the compiled layout, but does not confirm the peripheral base address or the accuracy of the hardware manual.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
