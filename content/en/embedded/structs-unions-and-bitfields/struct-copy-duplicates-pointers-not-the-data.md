---
id: emb-structs-0051
title: "Trap: why can copying a struct with pointer fields be a shallow-copy bug?"
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

<span class="warn">Structure assignment copies the pointer value, not the data it points to.</span>

After `b = a`, both structures may point to the same buffer. If one structure frees or modifies the buffer, the other sees the consequences. In embedded, this commonly occurs with DMA buffers, queues, and driver config pointers.

Mitigation: define ownership: the pointer is borrowed and documented, a deep copy is needed, or the buffer is passed separately with a lifetime contract.[^iso-c-n1570]

## Detailed explanation

TODO
