---
id: emb-dtypes-0031
title: "Is there a difference between `int x;` and `int x = 0;` declared globally?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: arm-aapcs32
    title: "Procedure Call Standard for the Arm Architecture (AAPCS32)"
    url: https://github.com/ARM-software/abi-aa/blob/main/aapcs32/aapcs32.rst
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

For objects with static storage duration, both declarations have a zero value before program execution. `int x;` is commonly placed in `.bss`; `int x = 0;` may be placed there too. Section placement is a toolchain choice, not a C language guarantee, so an explicit zero does not necessarily use more Flash.[^iso-c-n1570]

## Detailed explanation

TODO
