---
id: emb-volconst-0025
title: "Which section does a `const` lookup table land in?"
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
