---
id: emb-dtypes-0065
title: "What does a typical section layout look like in a Cortex-M `.elf` file?"
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
    title: "GNU ld: Output Section LMA"
    url: https://sourceware.org/binutils/docs/ld/Output-Section-LMA.html
  - source_id: gnu-ld-script
    title: "GNU ld: Linker Scripts"
    url: https://www.sourceware.org/binutils/docs/ld/Scripts.html
---

## Short answer

**Typical Flash**: `[.text][.rodata][.data LMA]`
**Typical RAM**: `[.data VMA][.bss][heap]...[stack]`

LMA (Load Memory Address) is where bytes are loaded from; VMA (Virtual Memory Address) is a section's run-time address. For `.data`, they often refer to Flash and RAM respectively, and startup code copies the data between them.

Check: `arm-none-eabi-objdump -h firmware.elf` or `arm-none-eabi-size firmware.elf`[^gnu-ld-lma]

## Detailed explanation

TODO
