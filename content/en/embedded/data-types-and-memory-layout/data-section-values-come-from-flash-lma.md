---
id: emb-dtypes-0083
title: "What does the `.data` section hold, and where do its startup values come from?"
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

In a typical bare-metal configuration, `.data` contains data that needs initial values in RAM; a linker script can give it an LMA in Flash and a VMA in RAM.[^gnu-ld-lma]

When LMA and VMA differ, startup code copies bytes from the image at the LMA into the RAM range at the VMA; the boundary symbols depend on the linker script.

Startup code commonly zeroes `.bss` afterward and then calls `main()`. The details depend on the runtime and linker script.[^gnu-ld-lma]

## Detailed explanation

TODO
