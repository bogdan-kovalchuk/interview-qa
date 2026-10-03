---
id: emb-structs-0024
title: "Trap: why are bit-fields dangerous for memory-mapped registers?"
description: "Bit-field layout is implementation-defined and access often generates a read-modify-write."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: pitfall
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  uk: 2
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
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
  - source_id: stm32-w1c-manual
    title: "SR5E1x 32-bit Arm Cortex-M7 architecture microcontroller reference manual"
    url: https://www.st.com/resource/en/reference_manual/rm0483-sr5e1x-32bit-arm-cortexm7-architecture-microcontroller-for-electrical-vehicle-applications-stmicroelectronics.pdf
    accessed: 2026-10-04
    kind: official
    version: "RM0483 Rev 6"
    applicability: "Example of a vendor's W1C definition; verify the actual semantics in the specific device manual."
---

## Short answer

<span class="warn">Bit-field layout is implementation-defined, and access often generates a read-modify-write.</span>

Bit ordering within a storage unit, signedness of plain `int` bit-fields, and padding between them all depend on the compiler/ABI. Moreover, writing one bit-field may read the entire register and write it back, which is dangerous for write-one-to-clear or read-to-clear bits.

Defence: for hardware registers it is often better to use masks/shifts and atomic set/clear registers. If bit-fields are allowed, pin to a specific compiler ABI and test the generated code.[^iso-c-n1570]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
