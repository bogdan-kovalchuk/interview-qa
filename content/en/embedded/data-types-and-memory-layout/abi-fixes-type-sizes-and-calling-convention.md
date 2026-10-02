---
id: emb-dtypes-0074
title: "What is an ABI, and how does it affect type sizes?"
description: "An ABI fixes type sizes, the calling convention, and struct alignment so compiled modules stay compatible."
track: embedded
section: data-types-and-memory-layout
level: middle
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
  - source_id: aapcs32
    title: "Procedure Call Standard for the Arm Architecture, Release 2019Q1.1"
    url: https://www.macs.hw.ac.uk/~hwloidl/Courses/F28HS/Docu/aapcs32.pdf
    accessed: 2026-10-04
    kind: spec
    version: "2019Q1.1"
    applicability: "Defines AAPCS32 rules including fundamental data types, pointer size, alignment, and procedure calls; applies only to compatible 32-bit Arm ABIs."
---

## Short answer

**ABI** (Application Binary Interface) defines binary agreements between components, including function calls, argument and result passing, type representations, and structure alignment for a particular ABI.[^aapcs32]

For 32-bit AAPCS (common in Cortex-M toolchains):
- `int` = 32 bits
- `long` = 32 bits (not 64!)
- `long long` = 64 bits
- `float` = 32 bits
- `double` = 64 bits
- `pointer` = 32 bits

In this ABI, `int` is 4 bytes, but this is not a universal rule for every ABI or Cortex-M toolchain. Modules built for incompatible ABIs may exchange data or call functions incorrectly.[^aapcs32]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
