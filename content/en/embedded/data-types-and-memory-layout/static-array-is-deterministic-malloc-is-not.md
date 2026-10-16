---
id: emb-dtypes-0092
title: "What is the difference between `malloc` and a static array for a buffer in embedded?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

Static arrays have a size and storage duration known in advance; placement in `.bss` or `.data` depends on initialization and the linker script. `malloc(256)` requests a block at runtime and may fail, returning a null pointer that must be checked. Allocator timing and ISR suitability depend on the implementation and timing requirements; safety projects often restrict dynamic memory, but this is not a universal MISRA or IEC 61508 requirement.[^iso-c-n1570]

## Detailed explanation

TODO
