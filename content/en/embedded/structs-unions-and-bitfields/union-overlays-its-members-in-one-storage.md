---
id: emb-structs-0014
title: "What is a `union` in C?"
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

**A `union`** gives several members shared storage, so their values occupy the same memory area. Reading another member reinterprets the stored representation; it does not convert the value between types.[^iso-c-n1570]

Unlike a `struct`, union members overlap and share a starting address. Writing through one member changes shared bytes; reading through another type depends on the object representation and can encounter a trap representation.[^iso-c-n1570]

Embedded code uses unions for variant data and payload representations, but byte access requires care with language rules and endianness.[^iso-c-n1570]

## Detailed explanation

TODO
