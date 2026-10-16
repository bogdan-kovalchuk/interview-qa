---
id: emb-dtypes-0025
title: "How does `__attribute__((packed))` affect `struct { char a; int b; char c; };`?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: gcc-packed
    title: "GCC: Common Type Attributes (packed)"
    url: https://gcc.gnu.org/onlinedocs/gcc/Common-Attributes.html
  - source_id: arm-cortex-m0
    title: "Arm Cortex-M0 Devices Generic User Guide"
    url: https://documentation-service.arm.com/static/5ea6ce5e9931941038def8c1%3Ftoken%3D
---

## Short answer

GCC’s `__attribute__((packed))` minimizes member alignment and can remove padding, but it is a compiler extension. Under common assumptions, this struct shrinks from 12 bytes to 6, placing `int b` at offset 1; verify layout for the target ABI. That unaligned field may require slower accesses or be unsupported: Cortex-M0 faults on unaligned accesses, while behavior on other cores depends on instruction and configuration.[^gcc-packed] [^arm-cortex-m0]

## Detailed explanation

TODO
