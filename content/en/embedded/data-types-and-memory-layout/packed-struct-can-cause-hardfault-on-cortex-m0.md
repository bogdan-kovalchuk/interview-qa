---
id: emb-dtypes-0051
title: "Trap: why can a `packed struct` cause a HardFault on Cortex-M0?"
description: "Cortex-M0 does not support misaligned access, so a packed struct without padding can trigger a HardFault."
track: embedded
section: data-types-and-memory-layout
level: middle
type: pitfall
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  uk: 3
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-04; this source is not proof of the claims."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for data types and memory layout concepts; details of specific devices and toolchains can differ."
  - source_id: armv6m-alignment
    title: "Arm: ARMv6-M vs ARMv7-M – Unpacking the microcontrollers"
    url: https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/armv6-m-vs-armv7-m---unpacking-the-microcontrollers
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Explains natural-alignment requirements for Cortex-M0/M0+/M1; the effect of an operation also depends on generated instructions and the memory system."
  - source_id: gcc-packed
    title: "GCC: Common Type Attributes – packed"
    url: https://gcc.gnu.org/onlinedocs/gcc/Common-Type-Attributes.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Documents GCC packed layout; it does not prescribe the generated code or fault behavior for every target."
---

## Short answer

Cortex-M0/M0+ requires naturally aligned memory accesses, but `packed` does not itself guarantee a HardFault: the compiler may generate safe byte accesses. The result depends on the emitted instruction and the memory address/region.[^armv6m-alignment]

`__attribute__((packed))` removes inter-member padding, so a `uint32_t` may have offset 1. Inspect the assembly and use `memcpy` into an aligned object for portable reads from a byte buffer.[^gcc-packed]

Some Cortex-M3/M4 instructions support unaligned accesses, but that is not universal for every instruction or memory region.[^armv6m-alignment]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
