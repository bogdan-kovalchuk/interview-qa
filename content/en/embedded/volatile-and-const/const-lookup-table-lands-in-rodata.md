---
id: emb-volconst-0025
title: "Which section does a `const` lookup table land in?"
description: "A const table lands in .rodata in Flash when it is file-scope or static and the linker script makes no special exceptions."
track: embedded
section: volatile-and-const
level: junior
type: mechanism
tags: []
status: published
updated: 2026-10-04
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
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-04; this source is not proof of the claims."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
  - source_id: gnu-ld-linker-scripts
    title: "GNU ld manual: Linker Scripts"
    url: https://sourceware.org/binutils/docs/ld.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Explains that linker scripts map sections to memory regions; exact placement depends on the script."
---

## Question code

```c
const uint16_t sine_lut[256] = { 0, 402, 804 };
```

## Short answer

Usually into a read-only section; the linker script may place it in Flash, but the exact section and address depend on the configuration.[^gnu-ld-linker-scripts]

The example has 256 `uint16_t` elements, which occupy `256 * 2 = 512` bytes assuming 16-bit elements. If the linker leaves the table in program memory that the MCU can read directly, those bytes are not needed in SRAM; confirm this in the map file.[^gnu-ld-linker-scripts]

`const` does not set physical placement: C defines neither `.rodata` nor `.data`, only that modification through this lvalue is prohibited.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
