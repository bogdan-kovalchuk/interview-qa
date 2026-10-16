---
id: emb-structs-0052
title: "Why is `sizeof(struct with flexible array)` not the full packet size?"
track: embedded
section: structs-unions-and-bitfields
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**Because a flexible array member has no fixed length and contributes no elements to the structure's `sizeof`.**

`sizeof(struct Packet)` returns the structure size, including possible padding, but not any `data[]` elements. The real size is `sizeof(struct Packet) + payload_len * sizeof data[0]`.

Rule: a flexible array member describes the prefix layout, it does not own storage automatically.[^iso-c-n1570]

## Detailed explanation

TODO
