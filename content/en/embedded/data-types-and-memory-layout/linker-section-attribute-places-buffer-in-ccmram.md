---
id: emb-dtypes-0050
title: "What does this do? `__attribute__((section(\".ccmram\"))) uint32_t fast_buf[256];`"
track: embedded
section: data-types-and-memory-layout
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

GCC's `section(".ccmram")` attribute asks the compiler to put a global array in the named `.ccmram` input section; by itself it assigns no RAM address and guarantees neither speed nor DMA compatibility. The linker script must map that section to available memory, and startup code must handle its initialization correctly.[^gcc-common-attributes]

## Detailed explanation

TODO
