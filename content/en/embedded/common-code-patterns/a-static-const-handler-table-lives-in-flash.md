---
id: emb-patterns-0038
title: "Why is an FSM function-pointer table made `static const`?"
track: embedded
section: common-code-patterns
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: gcc-gccint-sections
    title: "GCC 16.1.0 Internals: Defining the Output Assembler Language, Sections"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gccint/Sections.html
  - source_id: gcc-named-address-spaces
    title: "GCC 16.1.0: Named Address Spaces (AVR Named Address Spaces)"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/Named-Address-Spaces.html#AVR-Named-Address-Spaces
  - source_id: ld-output-section-lma
    title: "GNU ld: Output Section LMA"
    url: https://sourceware.org/binutils/docs/ld/Output-Section-LMA.html
---

## Short answer

**`static const` makes the table read-only: the compiler places it in `.rodata` and the linker script usually puts `.rodata` in Flash, so the table does not occupy RAM.**[^gcc-gccint-sections]

Assigning to an element of such a table does not compile, and changing it through a cast-away `const` is undefined behavior.[^iso-c-n1570] Placement depends on the toolchain: on AVR without `__flash` or `PROGMEM`, `const` data lives in RAM.[^gcc-named-address-spaces]

Rule: make immutable dispatch/handler tables `static const`.

## Detailed explanation

TODO
