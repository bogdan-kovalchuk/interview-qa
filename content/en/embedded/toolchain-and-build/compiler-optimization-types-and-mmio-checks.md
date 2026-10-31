---
id: emb-build-0019
title: "Which optimization types does a compiler use, and how can you check that optimization did not break MMIO or a delay loop?"
track: embedded
section: toolchain-and-build
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: gcc-overall-options
    title: "GCC manual: Options Controlling the Kind of Output"
    url: https://gcc.gnu.org/onlinedocs/gcc/Overall-Options.html
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: armv7m-arm
    title: "ARMv7-M Architecture Reference Manual"
    url: https://developer.arm.com/documentation/ddi0403/latest/
---

## Short answer

The compiler performs inlining, dead-code elimination, constant propagation, loop optimization, instruction scheduling, and LTO. Check MMIO through `volatile` register definitions, barriers where ordering matters, disassembly/map review, and target tests. <span class="warn">A busy delay loop without `volatile`, a timer, or an intrinsic barrier can be shortened or removed by the optimizer.</span>[^dou-embedded-interview]

## Detailed explanation

TODO
