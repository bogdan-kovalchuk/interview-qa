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
updated: 2026-09-07
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of this question and answer; the answer text is not independently verified against the original community Anki deck."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for data types and memory layout concepts; details of specific devices and toolchains can differ."
---

## Short answer

**EABI** – the embedded ABI, which fixes the calling convention, object format, type layout, alignment, exception/unwind rules, and floating-point ABI. If object files are built with different ABI flags, for example soft-float vs hard-float, the linker or runtime can break. For firmware, all libraries must match the target CPU, FPU, endian, ABI, and compiler runtime.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
