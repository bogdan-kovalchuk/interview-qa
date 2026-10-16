---
id: emb-dtypes-0072
title: "What is the resource difference between `.rodata` in Flash and `.data` in RAM?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: gnu-ld
    title: "The GNU linker: Linker Scripts"
    url: https://sourceware.org/binutils/docs/ld.pdf
---

## Short answer

**`.rodata`** is often placed in Flash by the linker script; the section name alone does not guarantee it. If the CPU reads it directly, the table needs no RAM copy.[^gnu-ld]

For initialized `.data`, startup code often copies initial bytes from Flash (LMA) to RAM (VMA), using space in both memories; the linker script and startup code define this.[^gnu-ld]

`const` does not guarantee Flash placement; check the linker map and MCU capabilities.[^gnu-ld]

## Detailed explanation

TODO
