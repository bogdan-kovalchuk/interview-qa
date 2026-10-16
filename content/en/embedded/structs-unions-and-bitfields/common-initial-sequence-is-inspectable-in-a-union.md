---
id: emb-structs-0048
title: "What is the common initial sequence in a union of structs?"
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

**C permits reading the common initial sequence of struct members in a `union` under the standard's conditions**, when its current member is one of those structs.[^iso-c-n1570]

This rule is specific to C; do not carry it over to C++ without checking that language's standard separately. Corresponding initial members must be compatible, and corresponding bit-fields must also have the same width.[^iso-c-n1570]

Keeping the tag outside the union is often simpler: it remains available regardless of the active variant and avoids relying on this narrow rule.[^iso-c-n1570]

## Detailed explanation

TODO
