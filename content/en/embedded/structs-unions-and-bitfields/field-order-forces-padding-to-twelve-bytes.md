---
id: emb-structs-0003
title: "What is the typical size of `struct S` when `uint32_t` has 4-byte alignment?"
description: "On an ABI where uint32_t has 4-byte alignment, sizeof(struct S) is typically 12 bytes."
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
struct S {
    uint8_t a;
    uint32_t b;
    uint8_t c;
};
```

## Short answer

On a common ABI where `uint8_t` has size and alignment 1 byte and `uint32_t` has size and alignment 4 bytes, `sizeof(struct S) == 12`.[^iso-c-n1570]

Under those assumptions, `a` is at offset 0, `b` at offset 4, and `c` at offset 8, with tail padding after `c`. C does not guarantee these offsets or this size for every 32-bit ABI.[^iso-c-n1570]

Field order affects the RAM/Flash footprint. For arrays of structs, padding repeats in every element.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
