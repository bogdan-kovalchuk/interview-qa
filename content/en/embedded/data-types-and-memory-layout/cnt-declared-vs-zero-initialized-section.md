---
id: emb-dtypes-0055
title: "`.bss` vs `.data` for: `uint32_t cnt;` and `uint32_t cnt = 0;` (globals)?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: gcc-zero-bss
    title: "GCC: Optimize Options – -fno-zero-initialized-in-bss"
    url: https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html
---

## Short answer

`uint32_t cnt;` is guaranteed an initial value of 0; toolchains typically place it in `.bss`, but that is not a C language rule.[^gcc-zero-bss]

`uint32_t cnt = 0;` also starts at 0, and GCC may place it in `.bss` by default; flags or another toolchain can change the section.[^iso-c-n1570] [^gcc-zero-bss]

The C standard guarantees the zero value, not a particular section name. Check the map file or ELF for your compiler/linker flags; writing `= 0` does not force the variable into `.data`.[^iso-c-n1570]

## Detailed explanation

TODO
