---
id: emb-patterns-0038
title: "Why is an FSM function-pointer table made `static const`?"
description: "const makes the table read-only: it is placed in .rodata (usually Flash), using no RAM, and writes to it do not compile."
track: embedded
section: common-code-patterns
level: junior
type: concept
tags: []
status: published
updated: 2026-10-06
content_revision: 3
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-06; this source is not proof of the claims."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Supports that assigning to a const object violates a constraint (6.5.16, 6.3.2.1), that modifying an object defined as const through a non-const lvalue is undefined behavior (6.7.3, paragraph 6), and that a function address is an address constant usable in a static initializer (6.6); does not say which memory holds the data."
  - source_id: gcc-gccint-sections
    title: "GCC 16.1.0 Internals: Defining the Output Assembler Language, Sections"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gccint/Sections.html
    accessed: 2026-10-06
    kind: official
    version: "16.1.0"
    applicability: "Confirms that GCC's default section selection puts read-only variables in readonly_data_section (in practice .rodata); the linker script decides which memory that section occupies."
  - source_id: gcc-named-address-spaces
    title: "GCC 16.1.0: Named Address Spaces (AVR Named Address Spaces)"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/Named-Address-Spaces.html#AVR-Named-Address-Spaces
    accessed: 2026-10-06
    kind: official
    version: "16.1.0"
    applicability: "Shows that on AVR outside avrtiny/avrxmega3 even read-only data lives in RAM by default and Flash needs `__flash` or `progmem`; applies to AVR only."
  - source_id: ld-output-section-lma
    title: "GNU ld: Output Section LMA"
    url: https://sourceware.org/binutils/docs/ld/Output-Section-LMA.html
    accessed: 2026-10-06
    kind: official
    version: null
    applicability: "Explains that a section can have a load address (LMA, the ROM image) different from its run address (VMA) and that initialized data is copied from ROM to RAM at start-up; this is why a mutable table costs both Flash and RAM."
---

## Short answer

**`static const` makes the table read-only: the compiler places it in `.rodata` and the linker script usually puts `.rodata` in Flash, so the table does not occupy RAM.**[^gcc-gccint-sections]

Assigning to an element of such a table does not compile, and changing it through a cast-away `const` is undefined behavior.[^iso-c-n1570] Placement depends on the toolchain: on AVR without `__flash` or `PROGMEM`, `const` data lives in RAM.[^gcc-named-address-spaces]

Rule: make immutable dispatch/handler tables `static const`.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
