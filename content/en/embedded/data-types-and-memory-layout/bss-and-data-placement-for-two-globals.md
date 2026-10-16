---
id: emb-dtypes-0008
title: "Which memory section: `uint32_t error_count;` (global) and `uint32_t sensor_count = 5;` (global)?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: gnu-ld-data
    title: "GNU ld: Output Section LMA"
    url: https://sourceware.org/binutils/docs/ld/Output-Section-LMA.html
---

## Short answer

`error_count` has static storage duration and zero initialization, so it typically goes in `.bss`; startup code sets that region to zero. `sensor_count` has a nonzero initial value, so a common embedded linker layout places it in `.data`: its initial bytes are stored at a load address and copied to its runtime address. The toolchain and linker script define the exact sections and addresses.[^gnu-ld-data]

## Detailed explanation

TODO
