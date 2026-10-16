---
id: emb-dtypes-0038
title: "What does startup code do with the `.data` section before calling `main()`?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: gnu-ld-lma-vma
    title: "GNU ld documentation: Output Section LMA"
    url: https://sourceware.org/binutils/docs/ld/Output-Section-LMA.html
---

## Short answer

In a typical bare-metal GNU toolchain, startup code copies initial `.data` values from Flash (LMA - Load Memory Address) to RAM (VMA - Virtual Memory Address); this is a common convention, not a universal requirement.[^gnu-ld-lma-vma]

For example, initializer `uint32_t x = 42;` is stored in the program image, then its representation is copied to RAM; byte order is platform-dependent.

A GNU startup file may copy with `memcpy(&_sdata, &_sidata, &_edata - &_sdata);`, then zero `.bss` with `memset(&_sbss, 0, &_ebss - &_sbss);`.[^gnu-ld-lma-vma]

## Detailed explanation

TODO
