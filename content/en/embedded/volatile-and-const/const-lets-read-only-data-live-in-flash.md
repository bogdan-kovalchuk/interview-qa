---
id: emb-volconst-0024
title: "Why does `const` matter in embedded beyond write protection?"
track: embedded
section: volatile-and-const
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: gnu-ld-linker-scripts
    title: "GNU ld manual: Linker Scripts"
    url: https://sourceware.org/binutils/docs/ld.html
---

## Short answer

**`const` makes data unmodifiable through that lvalue; the toolchain and linker script decide whether it lives in Flash**.

In a common embedded setup, the linker script may place read-only data in Flash/ROM and copy mutable initialized data from Flash to RAM at startup. This depends on the system; C does not guarantee it.[^gnu-ld-linker-scripts]

Declaring immutable tables, strings and descriptors `const` gives read-only access and may save RAM. Check the map file: the declaration alone promises neither `.rodata` nor Flash placement.[^iso-c-n1570] [^gnu-ld-linker-scripts]

## Detailed explanation

TODO
