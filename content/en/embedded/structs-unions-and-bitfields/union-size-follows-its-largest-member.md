---
id: emb-structs-0015
title: "What is the typical size of the union?"
description: "Typically sizeof(union U) equals 4 if uint32t has size 4 and the largest alignment does not increase the size beyond 4."
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
union U {
    uint8_t  b;
    uint16_t h;
    uint32_t w;
};
```

## Short answer

Typically `sizeof(union U) == 4` if `uint32_t` has size 4 and the union's alignment does not add trailing padding beyond 4 bytes.[^iso-c-n1570]

All members start at the same address, but which bytes of a numeric value are observed depends on endianness. The implementation providing `uint32_t` determines its availability and alignment.

The union must be large enough for its largest member; its size is not the sum of member sizes.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
