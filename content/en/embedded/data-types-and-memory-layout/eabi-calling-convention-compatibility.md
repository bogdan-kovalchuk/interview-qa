---
id: emb-dtypes-0101
title: "What is EABI, and why does ABI matter when mixing object files, libraries, and compiler flags?"
description: "EABI fixes calling conventions, type layout, alignment, and floating-point ABI, so firmware objects and libraries must agree."
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
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
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
  - source_id: arm-aapcs32
    title: "Arm ABI: Procedure Call Standard for the Arm Architecture"
    url: https://github.com/ARM-software/abi-aa/blob/main/aapcs32/aapcs32.rst
    accessed: 2026-10-04
    kind: spec
    version: "2025Q4"
    applicability: "Defines EABI, call contracts, types, and floating-point argument variants for AArch32; it does not specify ABI for other architectures."
---

## Short answer

**EABI** is an ABI for embedded environments; a specific ABI family defines object format, calls, and data passing. For Arm, for example, AAPCS32 specifies function arguments, register preservation, and floating-point argument variants.[^arm-aapcs32] Soft-float and hard-float can use incompatible calling conventions, so the linker or runtime may detect a mismatch when such modules are combined.[^arm-aapcs32] Modules need compatible external contracts, not necessarily identical local compiler options.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
