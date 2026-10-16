---
id: emb-dtypes-0069
title: "What is a linker script, and what role does it play in placing sections?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: gnu-ld-scripts
    title: "GNU ld: Scripts"
    url: https://sourceware.org/binutils/docs/ld/Scripts.html
  - source_id: gnu-ld-memory
    title: "GNU ld: MEMORY Command"
    url: https://sourceware.org/binutils/docs/ld/MEMORY.html
  - source_id: gnu-ld-sections
    title: "GNU ld: SECTIONS Command"
    url: https://sourceware.org/binutils/docs/ld/SECTIONS.html
  - source_id: gnu-ld-lma
    title: "GNU ld: Output Section LMA"
    url: https://sourceware.org/binutils/docs/ld/Output-Section-LMA.html
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**Linker script** (`.ld` file) describes how the linker maps input sections into output sections and controls memory layout; `MEMORY` names available regions and `SECTIONS` places output sections.[^gnu-ld-scripts]

For example, `MEMORY` can describe named memory regions:
`FLASH (rx) : ORIGIN = 0x08000000, LENGTH = 512K`
`RAM (rwx) : ORIGIN = 0x20000000, LENGTH = 128K`.

`SECTIONS` defines placement rules:
`.text : { *(.text*) } > FLASH`
`.data : { *(.data*) } > RAM AT> FLASH`

The linker does not automatically generate symbols such as `_sdata`, `_edata`, and `_sidata`; a particular script commonly defines these for startup code that copies `.data` from its load address into RAM.[^gnu-ld-lma]

## Detailed explanation

TODO
