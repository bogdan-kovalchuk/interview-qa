---
id: emb-structs-0046
title: "Why are `volatile` on a struct pointer and `volatile` on its fields not always the same?"
description: "The volatile qualifier must apply at the type level through which the access occurs."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: concept
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

**`volatile` must qualify the object being accessed.** If a pointer points to a volatile struct, accessing one of its members with `->` also yields a volatile-qualified member lvalue.[^iso-c-n1570]

`volatile GPIO_TypeDef *GPIOA` qualifies the pointed-to object, while `GPIO_TypeDef * volatile GPIOA` qualifies the pointer itself. A non-volatile alias does not have those access semantics, and `volatile` does not provide atomicity or thread synchronization.[^iso-c-n1570]

For memory-mapped registers, the access type must match the platform contract; check the SDK type and macro definitions in the platform documentation.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
