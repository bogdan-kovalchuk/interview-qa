---
id: emb-structs-0033
title: "How do you correctly allocate memory for a flexible array member?"
description: "Allocate sizeof(struct Packet) plus len bytes to cover the header and the flexible array."
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
struct Packet {
    uint16_t len;
    uint8_t data[];
};
```

## Short answer

You need to allocate `sizeof(struct Packet) + len` bytes.

For example: `struct Packet *p = malloc(sizeof *p + len);`. Then `p->len = len`, and the payload sits in `p->data[0..len-1]`; `sizeof *p` does not include the flexible array.

Check for `size_t` overflow while adding the size, and check the result of `malloc` for `NULL`. Without a heap, a static byte buffer of the required size can be reserved.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
