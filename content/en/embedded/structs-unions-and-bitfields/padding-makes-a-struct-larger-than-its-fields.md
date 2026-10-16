---
id: emb-structs-0002
title: "Why can a struct be larger than the sum of its fields?"
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

Due to padding: a C implementation may insert unused bytes between fields or after the last field, including to satisfy alignment requirements.[^iso-c-n1570]

For example, on a common ABI where `uint32_t` has size and alignment of 4 bytes and `uint8_t` has size and alignment of 1 byte, 3 padding bytes may follow an initial `uint8_t`. Tail padding may make the total size a multiple of the struct's alignment.[^iso-c-n1570]

Embedded rule: never assume a struct's wire or storage layout without checking `sizeof`, `offsetof`, and the compiler/ABI.[^iso-c-n1570]

## Detailed explanation

TODO
