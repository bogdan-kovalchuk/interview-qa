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
struct S {
    uint32_t b;
    uint8_t a;
    uint8_t c;
};
```

## Short answer

Typically `sizeof(struct S) == 8` on an ABI where `uint32_t` has alignment 4.

`b` occupies offset 0..3, `a` at offset 4, `c` at offset 5, then 2 bytes of tail padding so that the struct size is a multiple of 4. This is less than the 12 bytes of the `uint8_t, uint32_t, uint8_t` variant.

Embedded takeaway: in an array of 1000 elements, such reordering saves approximately 4 KB.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
