---
id: emb-dtypes-0055
title: "`.bss` vs `.data` for: `uint32_t cnt;` and `uint32_t cnt = 0;` (globals)?"
description: "Both globals start with value 0; placement in .bss or .data depends on the toolchain and linker script."
track: embedded
section: data-types-and-memory-layout
level: middle
type: mechanism
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  uk: 3
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-04; this source is not proof of the claims."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for data types and memory layout concepts; details of specific devices and toolchains can differ."
  - source_id: gcc-zero-bss
    title: "GCC: Optimize Options – -fno-zero-initialized-in-bss"
    url: https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Documents GCC's default placement of zero-initialized globals in BSS and the option that changes it; does not describe every compiler or linker."
---

## Short answer

`uint32_t cnt;` is guaranteed an initial value of 0; toolchains typically place it in `.bss`, but that is not a C language rule.[^gcc-zero-bss]

`uint32_t cnt = 0;` also starts at 0, and GCC may place it in `.bss` by default; flags or another toolchain can change the section.[^iso-c-n1570] [^gcc-zero-bss]

The C standard guarantees the zero value, not a particular section name. Check the map file or ELF for your compiler/linker flags; writing `= 0` does not force the variable into `.data`.[^iso-c-n1570]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
