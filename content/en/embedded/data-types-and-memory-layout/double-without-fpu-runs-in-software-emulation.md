---
id: emb-dtypes-0066
title: "Trap: what is the danger of `double` on embedded without an FPU?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: gcc-arm-options
    title: "GCC: ARM Options"
    url: https://gcc.gnu.org/onlinedocs/gcc/ARM-Options.html
  - source_id: arm-cortex-m4
    title: "Arm Cortex-M4 Processor Technical Reference Manual"
    url: https://documentation-service.arm.com/static/5fce431be167456a35b36ade
  - source_id: arm-cortex-m7
    title: "Arm Cortex-M7 Processor Technical Reference Manual"
    url: https://documentation-service.arm.com/static/5e906b038259fe2368e2a7bb
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

Without an FPU for the required precision, the compiler may use software routines for `double`; measure the target build because cost varies by operation and toolchain.[^gcc-arm-options] `double` is not always eight bytes; Cortex-M4F supports single precision, while Cortex-M7 FPU implementations may support double precision.[^arm-cortex-m4][^arm-cortex-m7]

Choose by precision and timing needs, inspect generated code, and measure the critical path. GCC `-mfloat-abi` and `-mfpu` must match the MCU and all objects; hard and soft ABIs are incompatible.[^gcc-arm-options]

## Detailed explanation

TODO
