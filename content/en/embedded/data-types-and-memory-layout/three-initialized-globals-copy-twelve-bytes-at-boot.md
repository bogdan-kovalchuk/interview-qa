---
id: emb-dtypes-0085
title: "How many bytes does startup code copy for these globals? `int a=1; int b=2; int c=3;`"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: gnu-ld-lma
    title: "GNU ld manual: Output Section LMA"
    url: https://sourceware.org/binutils/docs/ld/Output-Section-LMA.html
---

## Short answer

The exact count depends on the ABI and `.data` contents; with 32-bit `int` and only these three objects, their values occupy 12 bytes.[^iso-c-n1570] [^gnu-ld-lma]

In a typical bare-metal layout, values are copied from an LMA in Flash to a VMA in RAM, but startup code copies the linker-script-defined `.data` range, which need not consist of only these variables or exactly 12 bytes.[^gnu-ld-lma]

Zero-initialized objects are often placed in `.bss`, but this is a toolchain convention, not a C guarantee.[^gnu-ld-lma]

## Detailed explanation

TODO
