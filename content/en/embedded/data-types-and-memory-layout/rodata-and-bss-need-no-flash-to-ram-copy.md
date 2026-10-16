---
id: emb-dtypes-0048
title: "Which sections need a Flash-to-RAM copy at boot, and which don't?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: embedded-gnu-ld
    title: "GNU ld: Using LD"
    url: https://ftp.gnu.org/old-gnu/Manuals/ld-2.9.1/html_chapter/ld_3.html
---

## Short answer

In a typical bare-metal layout, `.data` has initial values in the Flash image and a runtime address in RAM, so startup code copies its bytes; `.bss` reserves RAM that startup code zeros. Placement of `.rodata` and `.text` depends on the linker script and MCU capabilities, so section names alone do not guarantee Flash reads or execute-in-place behavior.[^embedded-gnu-ld]

## Detailed explanation

TODO
