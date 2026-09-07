---
id: emb-structs-0033
title: "How do you allocate memory for a flexible array member correctly?"
description: "Allocate sizeof(struct Packet) plus len bytes to cover the header and the flexible array."
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
struct Packet {
    uint16_t len;
    uint8_t data[];
};
```

## Short answer

You need to allocate `sizeof(struct Packet) + len` bytes.

For example: `struct Packet *p = malloc(sizeof *p + len);`. Then `p->len = len`, and the payload sits in `p->data[0..len-1]`. `sizeof *p` does not include the flexible array.

Embedded rule: in bare-metal without a heap, this layout is often used in a statically allocated byte buffer with placement/offset discipline.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
