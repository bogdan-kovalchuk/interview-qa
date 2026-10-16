---
id: emb-align-0042
title: "How can `__attribute__((aligned))` and `packed` work together?"
track: embedded
section: memory-alignment-and-endianness
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: gcc-common-attributes
    title: "GCC: Common Attributes"
    url: https://gcc.gnu.org/onlinedocs/gcc/Common-Attributes.html
---

## Short answer

**`packed` reduces padding within a type, and `aligned(N)` sets the minimum alignment of the object or type.**

That helps for wire headers or DMA descriptors, where the layout must be compact but the start address must suit the hardware. For MMIO (memory-mapped I/O) register blocks <span class="warn">do not apply `packed` automatically</span>: registers sit at natural 32-bit offsets, and gaps are better described with reserved fields.

Rule: in GCC, `packed` reduces member padding while `aligned(N)` sets minimum alignment; for register maps check access width and `offsetof`.[^gcc-common-attributes]

## Detailed explanation

TODO
