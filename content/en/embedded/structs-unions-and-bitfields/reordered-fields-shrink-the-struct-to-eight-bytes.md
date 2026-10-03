---
id: emb-structs-0005
title: "What is the typical size after the fields are reordered?"
description: "Typically sizeof(struct S) equals 8 on an ABI where uint32t has alignment 4."
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
    uint32_t b;
    uint8_t a;
    uint8_t c;
};
```

## Short answer

On an ABI where `uint32_t` has 4-byte alignment and `uint8_t` has 1-byte alignment, `sizeof(struct S) == 8`.

`b` has offset 0, `a` has offset 4, and `c` has offset 5, followed by 2 bytes of tail padding. Under the same assumptions, the `uint8_t, uint32_t, uint8_t` variant is 12 bytes.

In an array of 1000 elements under these assumptions, the difference is 4000 bytes (about 3.91 KiB).[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
