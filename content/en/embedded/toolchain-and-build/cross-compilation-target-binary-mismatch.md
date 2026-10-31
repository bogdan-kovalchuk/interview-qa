---
id: emb-build-0017
title: "What is cross-compilation, and what typical errors occur when running a binary on a different architecture?"
track: embedded
section: toolchain-and-build
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: gcc-overall-options
    title: "GCC manual: Options Controlling the Kind of Output"
    url: https://gcc.gnu.org/onlinedocs/gcc/Overall-Options.html
  - source_id: arm-aapcs32
    title: "Arm ABI: Procedure Call Standard for the Arm Architecture"
    url: https://github.com/ARM-software/abi-aa/blob/main/aapcs32/aapcs32.rst
  - source_id: gccint-configure-terms
    title: "GCC Internals: Configure Terms and History"
    url: https://gcc.gnu.org/onlinedocs/gccint/Configure-Terms.html
  - source_id: gcc-arm-options
    title: "GCC manual: ARM Options"
    url: https://gcc.gnu.org/onlinedocs/gcc/ARM-Options.html
  - source_id: cmsis-core-nvic
    title: "CMSIS-Core (Cortex-M): Interrupts and Exceptions (NVIC)"
    url: https://arm-software.github.io/CMSIS_6/latest/Core/group__NVIC__gr.html
---

## Short answer

Cross-compilation is building on a host machine for a different CPU/OS/ABI target. Typical errors: built for host, mixed the wrong sysroot, soft/hard-float ABI, endianness, or libc, resulting in `Exec format error` or runtime crashes. Check with `file`, `readelf -h`, target triplet, and toolchain flags.[^dou-embedded-interview]

## Detailed explanation

TODO
