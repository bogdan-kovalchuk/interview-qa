---
id: emb-structs-0023
title: "Why can you not take the address of a bit-field?"
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

<span class="warn">In C, the address-of operator `&` cannot be applied to a bit-field.</span>

A bit-field may be part of an addressable storage unit, but the C standard explicitly prohibits applying `&` to the bit-field itself. Thus `&s.flag` violates a language constraint and requires a compiler diagnostic.[^iso-c-n1570]

Such a field cannot be passed to a function as a pointer to it. If an API needs an address, copy the value into an ordinary variable or pass the containing structure/value another way.[^iso-c-n1570]

## Detailed explanation

TODO
