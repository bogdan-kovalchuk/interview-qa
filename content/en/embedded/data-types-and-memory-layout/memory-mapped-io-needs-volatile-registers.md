---
id: emb-dtypes-0032
title: "What is memory-mapped I/O, and why do such registers need `volatile`?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: gcc-volatiles
    title: "GCC: When is a Volatile Object Accessed?"
    url: https://gcc.gnu.org/onlinedocs/gcc/Volatiles.html
  - source_id: arm-dmb
    title: "Cache Coherency in ARMv7-A and ARMv7-R Systems"
    url: https://developer.arm.com/-/media/Arm%20Developer%20Community/PDF/CacheCoherencyWhitepaper_6June2011.pdf?revision=e5a82cb4-0f87-4f5c-91cf-52b33a5cd1da
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**Memory-mapped I/O** – peripheral registers are accessible at addresses in the CPU memory space, but have platform-defined hardware semantics.

`volatile` is required because:
1. Hardware may change a status register between reads.
2. `volatile` marks accesses that the compiler implementation must preserve according to its rules.

`volatile` does not make an access atomic or act as a memory barrier for ordinary writes.[^gcc-volatiles]

## Detailed explanation

TODO
