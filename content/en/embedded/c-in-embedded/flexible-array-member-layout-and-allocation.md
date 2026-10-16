---
id: emb-cppfound-0047
title: "What is a flexible array member (FAM) in C99 and where is it stored?"
track: embedded
section: c-in-embedded
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**Flexible Array Member** (FAM) – the last field of a struct with an unspecified size: `struct Packet { uint8_t len; uint8_t data[]; };`

`sizeof(struct Packet)` does not include `data`. The FAM is allocated together with the struct: `malloc(sizeof(Packet) + n)` – then `data` occupies `n` bytes immediately after the struct fields.

It is stored in the same memory block as the struct (heap or static). It cannot be the only member of a struct and cannot be in an array.[^embeddedinterviewlab]

## Detailed explanation

TODO
