---
id: emb-dtypes-0097
title: "What is a memory region, and how is it defined in a linker script?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: gnu-ld-memory
    title: "GNU ld documentation: MEMORY command"
    url: https://sourceware.org/binutils/docs/ld/MEMORY.html
---

## Short answer

**Memory region** – a named span of address space. Defined in the `MEMORY` block of a linker script:

`MEMORY {
  FLASH (rx)   : ORIGIN = 0x08000000, LENGTH = 512K
  RAM   (rwx)  : ORIGIN = 0x20000000, LENGTH = 128K
  CCMRAM (rwx) : ORIGIN = 0x10000000, LENGTH = 64K
}`

Attributes: `r` – read, `w` – write, `x` – execute. Sections are bound via `> REGION` in the `SECTIONS` block.[^gnu-ld-memory]

## Detailed explanation

TODO
