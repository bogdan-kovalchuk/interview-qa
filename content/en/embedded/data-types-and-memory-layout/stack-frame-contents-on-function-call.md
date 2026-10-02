---
id: emb-dtypes-0033
title: "What does a stack frame hold on a function call?"
description: "A stack frame holds saved registers, the return address, local variables, and alignment padding."
track: embedded
section: data-types-and-memory-layout
level: middle
type: mechanism
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  uk: 3
anki:
  export: true
sources:
  - source_id: arm-aapcs32
    title: "Procedure Call Standard for the Arm Architecture (AAPCS32)"
    url: https://github.com/ARM-software/abi-aa/blob/main/aapcs32/aapcs32.rst
    accessed: 2026-10-04
    kind: spec
    version: "AAPCS32"
    applicability: "Describes stack and alignment rules for the Arm 32-bit ABI; it does not prescribe a universal frame."
  - source_id: armv7m
    title: "Armv7-M Architecture Reference Manual"
    url: https://developer.arm.com/documentation/ddi0403/latest/
    accessed: 2026-10-04
    kind: official
    version: "Armv7-M"
    applicability: "Armv7-M exceptions; it does not cover all Cortex-M generations identically."
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
---

## Short answer

Stack frame contents depend on the ABI, compiler, and optimization: it may contain saved registers, a return address, local data, and padding, but there is no universal fixed list. On Cortex-M, exception entry automatically stacks a basic frame containing R0–R3, R12, LR, PC, and xPSR; cores with an FPU can use an extended frame and lazy stacking.[^armv7m]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
