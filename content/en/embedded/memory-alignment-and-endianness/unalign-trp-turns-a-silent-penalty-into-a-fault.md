---
id: emb-align-0008
title: "How does a misaligned access behave on Cortex-M3/M4 and what is `UNALIGN_TRP`?"
description: "Supported unaligned accesses can be trapped deliberately, while some instructions always require alignment"
track: embedded
section: memory-alignment-and-endianness
level: junior
type: concept
tags: []
status: published
updated: 2026-09-08
content_revision: 4
reconciled_with:
  uk: 4
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
  - source_id: arm-cortex-m3-unaligned
    title: "Arm Cortex-M3 Devices Generic User Guide: Configurable Fault Status Register"
    url: https://developer.arm.com/documentation/dui0552/a/cortex-m3-peripherals/system-control-block/configurable-fault-status-register
    accessed: 2026-09-08
    kind: official
    version: "1.0"
    applicability: "UNALIGN_TRP behavior and Cortex-M3 instructions that always fault when unaligned."
  - source_id: arm-cortex-m4-datasheet
    title: "Arm Cortex-M4 Processor Datasheet"
    url: https://developer.arm.com/-/media/Arm%20Developer%20Community/PDF/Processor%20Datasheets/Arm%20Cortex-M4%20Processor%20Datasheet.pdf
    accessed: 2026-09-08
    kind: official
    version: null
    applicability: "Confirms architectural support for unaligned accesses on Cortex-M4; instruction and memory-region restrictions still apply."
  - source_id: learncpp-object-sizes
    title: "LearnCpp: Object sizes and the sizeof operator"
    url: https://www.learncpp.com/cpp-tutorial/object-sizes-and-the-sizeof-operator/
    accessed: 2026-09-08
    kind: community
    version: null
    applicability: "Supplementary background on multi-byte objects and target-dependent representation."
  - source_id: acode-next-cpp
    title: "aCode: End? What next?"
    url: https://acode.com.ua/end-cpp-what-is-next/
    accessed: 2026-09-08
    kind: community
    version: null
    applicability: "Supplementary Ukrainian C++ learning roadmap; not a processor reference."
---

## Short answer

**Cortex-M3/M4 support some unaligned halfword and word accesses, but support is not universal.** Memory type and instruction still matter; `LDM`, `STM`, `LDRD`, and `STRD` require alignment.

`SCB->CCR.UNALIGN_TRP` makes otherwise-supported unaligned accesses raise UsageFault, which helps expose bugs during development.

This does not make aligned typed-pointer access optional in C; violating the type's alignment requirement remains undefined behavior.[^embeddedinterviewlab]

## Detailed explanation

Cortex-M3 and Cortex-M4 advertise support for unaligned accesses, so an ordinary load/store from Normal memory may complete instead of faulting. The core can still need extra transfers, but the exact cycle cost belongs to the concrete MCU, memory region, cache, and bus fabric rather than to a universal multiplier.[^arm-cortex-m4-datasheet]

`UNALIGN_TRP` is a diagnostic control in the System Control Block. When set, an unaligned access that would otherwise be supported raises UsageFault and sets the `UNALIGNED` status bit. If UsageFault is disabled, the exception can escalate to HardFault.

```c
SCB->CCR |= SCB_CCR_UNALIGN_TRP_Msk;
```

The switch is not absolute. Arm documents that unaligned `LDM`, `STM`, `LDRD`, and `STRD` fault regardless of `UNALIGN_TRP`.[^arm-cortex-m3-unaligned] Device or Strongly-ordered memory and device-specific buses may impose additional restrictions.

At the C level, converting an arbitrary byte address to `uint32_t *` can violate the target type's alignment and cause undefined behavior.[^iso-c-n1570] The compiler may optimize based on that promise even when the processor could execute an unaligned instruction.

Use `UNALIGN_TRP` in debug builds as an early detector, then fix the access with an aligned object, `memcpy`, or explicit byte decoding. Do not disable the trap merely to hide a faulty data-layout assumption.

## Sources

<!-- generated from frontmatter -->
