---
id: emb-dtypes-0068
title: "Where is this stored inside a function? `static const uint16_t lookup[] = {1, 2, 3};`"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: gnu-ld-sections
    title: "GNU ld: SECTIONS Command"
    url: https://sourceware.org/binutils/docs/ld/SECTIONS.html
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

Inside a function, `static` gives the array static storage duration, while `const` prevents modification through that name; neither keyword alone guarantees `.rodata` placement or zero RAM use.[^iso-c-n1570] The compiler and linker script determine sections and addresses, so check the linker map.[^gnu-ld-sections]

On a typical embedded layout, an initialized read-only table can reside in Flash, while writable initialized data is copied from its load image into RAM at startup. The actual result depends on the compiler, linker script, and MCU memory map.[^gnu-ld-sections]

## Detailed explanation

TODO
