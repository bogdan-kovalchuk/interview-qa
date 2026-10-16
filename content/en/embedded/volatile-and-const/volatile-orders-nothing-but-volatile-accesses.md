---
id: emb-volconst-0038
title: "Why is `volatile` not a memory barrier?"
track: embedded
section: volatile-and-const
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: gcc-volatile
    title: "GCC documentation: Volatiles"
    url: https://gcc.gnu.org/onlinedocs/gcc/Volatiles.html
  - source_id: arm-cortex-m7
    title: "Arm Cortex-M7 Devices Generic User Guide"
    url: https://documentation-service.arm.com/static/61efd6602dd99944d051417b?token=
---

## Short answer

**`volatile` constrains optimizations of accesses to volatile objects, but it is not a full CPU/compiler memory barrier for all memory.**

`volatile` does not establish a general order between ordinary memory accesses and volatile accesses, nor is it a complete CPU/compiler memory barrier. Exact volatile access rules depend on the language, compiler, and target. Cache synchronization, bus ordering, DMA visibility, and inter-core ordering need separate platform guarantees.

Rule: for required hardware ordering, use architectural primitives such as `__DMB()`, `__DSB()`, `__ISB()` and compiler-specific facilities as required by the platform documentation.[^gcc-volatile]

## Detailed explanation

TODO
