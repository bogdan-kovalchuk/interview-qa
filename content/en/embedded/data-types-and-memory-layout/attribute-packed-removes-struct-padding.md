---
id: emb-dtypes-0025
title: "How does `__attribute__((packed))` affect `struct { char a; int b; char c; };`?"
description: "attribute((packed)) removes padding to shrink the struct, but can trigger misaligned access."
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
  - source_id: gcc-packed
    title: "GCC: Common Type Attributes (packed)"
    url: https://gcc.gnu.org/onlinedocs/gcc/Common-Attributes.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Describes GCC packed member placement; exact layout depends on target and ABI."
  - source_id: arm-cortex-m0
    title: "Arm Cortex-M0 Devices Generic User Guide"
    url: https://documentation-service.arm.com/static/5ea6ce5e9931941038def8c1%3Ftoken%3D
    accessed: 2026-10-04
    kind: official
    version: "DUI 0497A"
    applicability: "Cortex-M0 does not support unaligned accesses; this claim applies to that core specifically."
---

## Short answer

GCC’s `__attribute__((packed))` minimizes member alignment and can remove padding, but it is a compiler extension. Under common assumptions, this struct shrinks from 12 bytes to 6, placing `int b` at offset 1; verify layout for the target ABI. That unaligned field may require slower accesses or be unsupported: Cortex-M0 faults on unaligned accesses, while behavior on other cores depends on instruction and configuration.[^gcc-packed] [^arm-cortex-m0]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
