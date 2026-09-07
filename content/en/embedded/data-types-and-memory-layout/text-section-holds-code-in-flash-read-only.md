---
id: emb-dtypes-0001
title: "What is the `.text` section in an embedded program's memory?"
description: "The .text section holds compiled code and sits read-only in Flash on embedded targets."
track: embedded
section: data-types-and-memory-layout
level: junior
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
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of the question and answer; the answer is not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for data types and memory layout concepts; details of specific devices and toolchains can differ."
---

## Short answer

The **.text** section contains the compiled machine code (instructions) of all program functions. In embedded, it is stored in **Flash memory** and is read-only.

The CPU executes instructions directly from Flash (XIP – Execute in Place) or after copying to RAM for speed. An attempt to write to `.text` -> HardFault (if the MPU is configured).[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
