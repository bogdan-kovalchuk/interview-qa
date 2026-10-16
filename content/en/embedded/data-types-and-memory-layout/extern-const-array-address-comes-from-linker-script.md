---
id: emb-dtypes-0093
title: "How does a linker script assign an address to `extern const uint8_t image_data[]`?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: gnu-ld-symbols
    title: "GNU ld: Source Code Reference"
    url: https://sourceware.org/binutils/docs/ld/Source-Code-Reference.html
  - source_id: gnu-ld-sections
    title: "GNU ld: SECTIONS Command"
    url: https://sourceware.org/binutils/docs/ld/SECTIONS.html
---

## Short answer

The declaration `extern const uint8_t image_data[];` does not define the array; the linker resolves the symbol in the linked image. Its physical address and section depend on the linker script and target, so it is not necessarily Flash or `.rodata`. In GNU `ld`, a script-defined symbol is an address without a separate object, so code commonly declares it as an array and reads from that address.[^gnu-ld-symbols]

## Detailed explanation

TODO
