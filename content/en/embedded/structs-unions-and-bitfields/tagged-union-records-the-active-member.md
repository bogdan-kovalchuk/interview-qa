---
id: emb-structs-0018
title: "Why is a discriminator tag often added to a `union`?"
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

**Because the union itself does not remember which member is currently active or logically valid.**

Typical pattern: an `enum kind` alongside a `union payload`. The union itself stores no separate tag and does not tell the program which variant to handle; the active member follows from language rules and the program's operations.[^iso-c-n1570]

For variant data, store a tag alongside the union and check it before reading the corresponding member.[^iso-c-n1570]

## Detailed explanation

TODO
