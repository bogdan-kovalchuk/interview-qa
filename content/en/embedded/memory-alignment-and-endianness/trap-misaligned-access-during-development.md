---
id: emb-align-0037
title: "Why enable `UNALIGN_TRP` on an M3/M4 during development?"
track: embedded
section: memory-alignment-and-endianness
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: arm-cortex-m3-trm
    title: "Arm Cortex-M3 Technical Reference Manual"
    url: https://documentation-service.arm.com/static/6036810d5319e554d4ba108e
  - source_id: arm-cortex-m4-guide
    title: "Cortex-M4 Devices Generic User Guide"
    url: https://documentation-service.arm.com/static/5f2ac76d60a93e65927bbdc5
---

## Short answer

**To make some misaligned accesses raise an explicit UsageFault during debugging.**

M3/M4 support unaligned accesses only for some load/store instructions; other instructions already fault. `UNALIGN_TRP` in `SCB->CCR` makes supported unaligned accesses raise UsageFault, but it does not diagnose every alignment violation in C code.[^arm-cortex-m3-trm] [^arm-cortex-m4-guide] [^iso-c-n1570]

Use this mode as an additional check on the specific core, while keeping the language and platform alignment requirements in the code.[^arm-cortex-m4-guide] [^iso-c-n1570]

## Detailed explanation

TODO
