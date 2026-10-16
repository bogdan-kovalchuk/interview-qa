---
id: emb-structs-0032
title: "What is a flexible array member?"
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

A **flexible array member** is the last field of a struct with an incomplete size, for example `uint8_t data[];`.

It allows allocating a single memory block: header plus variable-length payload. `sizeof(struct Packet)` does not include the payload bytes, only the header and any padding before the flexible array.

Rule: a flexible array member must be the last field, and the struct must have at least one other named field.[^iso-c-n1570]

## Detailed explanation

TODO
