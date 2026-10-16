---
id: emb-dtypes-0074
title: "What is an ABI, and how does it affect type sizes?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: aapcs32
    title: "Procedure Call Standard for the Arm Architecture, Release 2019Q1.1"
    url: https://www.macs.hw.ac.uk/~hwloidl/Courses/F28HS/Docu/aapcs32.pdf
---

## Short answer

**ABI** (Application Binary Interface) defines binary agreements between components, including function calls, argument and result passing, type representations, and structure alignment for a particular ABI.[^aapcs32]

For 32-bit AAPCS (common in Cortex-M toolchains):
- `int` = 32 bits
- `long` = 32 bits (not 64!)
- `long long` = 64 bits
- `float` = 32 bits
- `double` = 64 bits
- `pointer` = 32 bits

In this ABI, `int` is 4 bytes, but this is not a universal rule for every ABI or Cortex-M toolchain. Modules built for incompatible ABIs may exchange data or call functions incorrectly.[^aapcs32]

## Detailed explanation

TODO
