---
id: emb-align-0030
title: "What does `__attribute__((aligned(N)))` do for a variable?"
track: embedded
section: memory-alignment-and-endianness
sources:
  - source_id: gcc-variable-attributes
    title: "GCC 12.5: Common Variable Attributes"
    url: https://gcc.gnu.org/onlinedocs/gcc-12.5.0/gcc/Common-Variable-Attributes.html
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Question code

```c
uint8_t buf[64] __attribute__((aligned(32)));
```

## Short answer

**For a supported target, asks GCC to give the variable alignment of at least N bytes.**[^gcc-variable-attributes]

Used for DMA or cache-line buffers when an aligned address is required. This is a GNU compiler extension; standard C has `_Alignas`, but support for a particular value depends on the implementation and target.[^gcc-variable-attributes] [^iso-c-n1570]

`aligned` changes an alignment requirement, but does not select a memory region, configure DMA, or define a wire format. `packed` is a separate attribute with separate consequences.[^gcc-variable-attributes]

## Detailed explanation

TODO
