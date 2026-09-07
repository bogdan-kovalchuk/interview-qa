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
union U {
    uint8_t  b;
    uint16_t h;
    uint32_t w;
};
```

## Short answer

Typically `sizeof(union U) == 4` if `uint32_t` has size 4 and the largest alignment does not increase the size beyond 4.

All fields start at offset 0. `b` uses the first byte of storage, `h` the first 2 bytes, `w` all 4 bytes. The actual interpretation of the bytes depends on endianness and access rules.

Rule: union size is determined by the largest member, not the sum of members.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
