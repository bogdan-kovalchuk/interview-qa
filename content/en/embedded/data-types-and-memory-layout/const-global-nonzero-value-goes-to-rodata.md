---
id: emb-dtypes-0002
title: "Which memory section does this go into? `const uint32_t FIRMWARE_VERSION = 0x0102;`"
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

A typical embedded layout places `const uint32_t FIRMWARE_VERSION = 0x0102;` in read-only storage, often `.rodata` in Flash. In C, however, `const` prevents modification through that lvalue; it does not instruct the linker to choose `.rodata` or guarantee zero RAM use. Actual placement depends on the compiler, how the object is used, and the linker script.[^embedded-ld-layout]

## Detailed explanation

TODO
