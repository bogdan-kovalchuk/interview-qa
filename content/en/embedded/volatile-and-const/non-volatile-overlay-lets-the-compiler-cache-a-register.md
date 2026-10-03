---
id: emb-volconst-0046
title: "Trap: what is wrong with this struct overlay?"
description: "The register overlay fields are not volatile-qualified."
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
typedef struct {
    uint32_t MODER;
    uint32_t IDR;
} GPIO_TypeDef;

#define GPIOA ((GPIO_TypeDef *)0x40020000)
```

## Short answer

<span class="warn">The register overlay fields lack the `volatile` qualifier.</span>

`GPIOA->IDR` has the plain `uint32_t` type, so the C abstract machine does not require a separate volatile access on every read. For a register changed by hardware, this can produce a stale value.[^iso-c-n1570]

Protection: declare the fields as `volatile uint32_t MODER;`, `volatile uint32_t IDR;` or use vendor CMSIS headers where the qualifiers are already set.[^iso-c-n1570]

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
