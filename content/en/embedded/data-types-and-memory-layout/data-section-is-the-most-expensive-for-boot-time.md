---
id: emb-dtypes-0062
title: "Which data does startup code typically copy from Flash to RAM before `main()`?"
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
---

## Short answer

Startup code commonly copies `.data` initial bytes from Flash to RAM before `main()` when the section has distinct load and run addresses. The time depends on section size and memory behavior, so `.data` is not universally the most expensive part of startup.[^gnu-ld-lma]

`.bss` is often cleared in RAM, while placement of `.text`, `.rodata`, and other sections is defined by the linker script and platform.[^gnu-ld-lma]

## Detailed explanation

TODO
