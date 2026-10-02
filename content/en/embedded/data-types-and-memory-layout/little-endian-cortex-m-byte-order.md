---
id: emb-dtypes-0019
title: "What are little-endian and big-endian? How does Cortex-M store `0x12345678`?"
description: "Little-endian stores the least-significant byte at the lowest address; Cortex-M defaults to little-endian."
track: embedded
section: data-types-and-memory-layout
level: junior
type: concept
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
  - source_id: arm-cortex-m0-datasheet
    title: "Arm Cortex-M0 Processor Datasheet"
    url: https://developer.arm.com/-/media/Arm%20Developer%20Community/PDF/Processor%20Datasheets/Arm_Cortex-M0_Processor_Datasheet.pdf?hash=4AF1DD0929A9911BDC7FFC800BC74F7D&revision=9310a7ce-480c-4491-88e7-c4392d28fb80
    accessed: 2026-10-04
    kind: official
    version: "revision  r0p0"
    applicability: "Documents that Cortex-M0 implementations can support little-endian or byte-invariant big-endian data accesses; this datasheet does not establish the setting for every Cortex-M or SoC."
---

## Short answer

**Endianness** is the byte order of a multi-byte value in memory. **Little-endian** places the least-significant byte at the lowest address, so `0x12345678` is stored as `[78][56][34][12]`; Cortex-M mode depends on the implementation and configuration.[^arm-cortex-m0-datasheet]

**Big-endian** places the most-significant byte at the lowest address; protocol byte order is a separate rule, so encode bytes explicitly or use an appropriate conversion API.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
