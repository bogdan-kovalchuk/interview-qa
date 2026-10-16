---
id: emb-dtypes-0004
title: "What is the `.bss` section and how does it differ from `.data`?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: embedded-ld-layout
    title: "GNU ld documentation: linker scripts and output section LMA"
    url: https://sourceware.org/binutils/docs/ld/Output-Section-LMA.html
---

## Short answer

In a typical embedded image, `.bss` describes global or `static` objects whose initial value is zero, while `.data` holds objects with nonzero initial values. Startup code commonly zeroes the `.bss` range in RAM and copies `.data` initial bytes from ROM/Flash into RAM; the linker script defines the exact layout.[^embedded-ld-layout]

## Detailed explanation

TODO
