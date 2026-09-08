---
id: emb-align-0002
title: "Why does a CPU require aligned data at all?"
description: "The bus reads and writes memory in word-aligned chunks of fixed size"
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
    applicability: "Cortex-M3 unaligned-access trapping and instructions that always fault when unaligned."
  - source_id: learncpp-object-sizes
    title: "LearnCpp: Object sizes and the sizeof operator"
    url: https://www.learncpp.com/cpp-tutorial/object-sizes-and-the-sizeof-operator/
    accessed: 2026-09-08
    kind: community
    version: null
    applicability: "Supplementary explanation of byte-addressed objects and implementation-dependent object sizes."
  - source_id: acode-next-cpp
    title: "aCode: End? What next?"
    url: https://acode.com.ua/end-cpp-what-is-next/
    accessed: 2026-09-08
    kind: community
    version: null
    applicability: "Supplementary Ukrainian C++ learning roadmap; not a normative source for processor behavior."
---

## Short answer

**Aligned access matches the boundaries expected by the type and memory system.**

An aligned value can fit within the naturally addressed transfer unit. A misaligned value may cross a boundary, so hardware can split the operation into several aligned transfers or reject it with a fault.

Do not reduce this to a Cortex-M generation rule: the result depends on the instruction, memory attributes, and trap configuration.[^embeddedinterviewlab]

## Detailed explanation

The C rule and the processor rule are separate. C requires a typed object to be suitably aligned; violating that rule produces undefined behavior before processor-specific behavior is considered.[^iso-c-n1570]

At the processor level, an implementation can translate one unaligned instruction into several aligned bus transfers. For a representative 32-bit transfer, the boundary crossing looks like this:

**Aligned access:**

If a `uint32_t` is located at address 0x2000_0000 (divisible by 4), the CPU reads it in one transaction:
```
Address: 0x2000_0000  0x2000_0004
Data:    [4 bytes]    [4 bytes]
         ^^^^
         one transaction
```

**Misaligned access:**

If a `uint32_t` is located at address 0x2000_0001 (not divisible by 4), the value straddles a word boundary:
```
Address: 0x2000_0000  0x2000_0004  0x2000_0008
Data:    [4 bytes]    [4 bytes]    [4 bytes]
          ^^^^         ^^^^
          1 byte       3 bytes
```
The implementation may read both aligned words and combine the required bytes. This is a model, not a guarantee that every 32-bit MCU exposes a four-byte bus transaction.

**A concrete Cortex-M3 example**

The Cortex-M3 can perform some unaligned loads and stores. Software can request trapping through `UNALIGN_TRP`, while unaligned `LDM`, `STM`, `LDRD`, and `STRD` fault regardless of that setting.[^arm-cortex-m3-unaligned]

Other cores and memory regions have different rules. Device memory, exclusive or multiple-register instructions, peripheral registers, and a vendor's bus fabric can impose stricter alignment than ordinary RAM access.

**Practical consequences**

- Let the compiler lay out ordinary objects and structures according to the target ABI.
- For packet or serial bytes, use `memcpy` into an aligned integer, then decode endianness. Do not cast an arbitrary byte pointer to `uint32_t *`.
- Check the MCU reference manual for DMA buffers and memory-mapped registers; alignment can be required for correctness, atomicity, or performance.
- Measure the actual target before claiming a fixed cycle multiplier.

## Sources

<!-- generated from frontmatter -->
