---
id: emb-structs-0017
title: "What is the safer way to read the bits of a `float` as `uint32_t` in C?"
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

**Via `memcpy`**:

`uint32_t bits; memcpy(&bits, &f, sizeof bits);`

`memcpy` copies the object representation byte by byte without accessing the `float` through an incompatible `uint32_t` lvalue. The resulting integer value depends on both types' sizes and representations and on byte order.[^iso-c-n1570]

For representation copying, `memcpy` is portable with respect to aliasing rules; that does not make the numeric bit value portable across platforms.[^iso-c-n1570]

## Detailed explanation

TODO
