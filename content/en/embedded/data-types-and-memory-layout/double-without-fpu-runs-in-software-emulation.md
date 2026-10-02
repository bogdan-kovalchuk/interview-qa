---
id: emb-dtypes-0066
title: "Trap: what is the danger of `double` on embedded without an FPU?"
description: "Without hardware support for the required precision, the compiler may emit software floating-point calls; cost depends on the MCU, compiler, and operation."
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
  - source_id: gcc-arm-options
    title: "GCC: ARM Options"
    url: https://gcc.gnu.org/onlinedocs/gcc/ARM-Options.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Explains ARM soft, softfp, and hard floating-point code generation and ABI compatibility; does not predict cycle counts for a specific MCU."
  - source_id: arm-cortex-m4
    title: "Arm Cortex-M4 Processor Technical Reference Manual"
    url: https://documentation-service.arm.com/static/5fce431be167456a35b36ade
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Documents the Cortex-M4 FPU's single-precision register and instruction capability; Cortex-M4 FPU presence is implementation-optional."
  - source_id: arm-cortex-m7
    title: "Arm Cortex-M7 Processor Technical Reference Manual"
    url: https://documentation-service.arm.com/static/5e906b038259fe2368e2a7bb
    accessed: 2026-10-04
    kind: official
    version: null
    applicability: "Documents optional double-precision operations in Cortex-M7 FPU configurations; check the specific implementation."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for data types and memory layout concepts; details of specific devices and toolchains can differ."
---

## Short answer

Without an FPU for the required precision, the compiler may use software routines for `double`; measure the target build because cost varies by operation and toolchain.[^gcc-arm-options] `double` is not always eight bytes; Cortex-M4F supports single precision, while Cortex-M7 FPU implementations may support double precision.[^arm-cortex-m4][^arm-cortex-m7]

Choose by precision and timing needs, inspect generated code, and measure the critical path. GCC `-mfloat-abi` and `-mfpu` must match the MCU and all objects; hard and soft ABIs are incompatible.[^gcc-arm-options]

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
