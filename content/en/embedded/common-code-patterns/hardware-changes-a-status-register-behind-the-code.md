---
id: emb-patterns-0024
title: "Why must peripheral registers be `volatile`?"
track: embedded
section: common-code-patterns
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: linux-volatile-mmio
    title: "The Linux kernel documentation: Why the volatile type class should not be used"
    url: https://docs.kernel.org/next/process/volatile-considered-harmful.html
---

## Short answer

**The status register is changed by hardware asynchronously, not by code.**

`volatile` tells the compiler that accesses to the object are observable and must be preserved under the C abstract machine, but it does not guarantee physical RAM access, atomicity, or MCU transaction ordering.[^iso-c-n1570] Without it, repeated reads of an ordinary object may be optimized even when a device changes the corresponding location.

For ordinary memory-mapped registers, volatile access is a typical part of the compiler contract, but accessors and any extra barriers are platform-specific.[^linux-volatile-mmio]

## Detailed explanation

TODO
