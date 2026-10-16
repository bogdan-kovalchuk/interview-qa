---
id: emb-structs-0001
title: "What is a `struct` in C and what is it for in embedded?"
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

**`struct`** groups several fields of different types into one object whose fields have a defined declaration order, while exact offsets and padding depend on the C implementation.[^iso-c-n1570]

In embedded, structs are used for peripheral register maps, protocol frames, driver state, configuration blocks, and DMA descriptors. Importantly, a struct has not only logical fields but also a physical layout in memory: offsets, padding, alignment.

Rule: when a struct crosses the boundary to hardware, a binary protocol, or a Flash layout, its size and offsets must be verified explicitly.[^iso-c-n1570]

## Detailed explanation

TODO
