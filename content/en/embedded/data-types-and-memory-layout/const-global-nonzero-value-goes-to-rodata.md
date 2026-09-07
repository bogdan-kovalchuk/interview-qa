---
id: emb-dtypes-0002
title: "Which memory section does this go into? `const uint32_t FIRMWARE_VERSION = 0x0102;`"
description: "A const global with a non-zero value lands in .rodata and costs no RAM."
track: embedded
section: data-types-and-memory-layout
level: middle
type: mechanism
tags: []
status: published
updated: 2026-09-07
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

In the **.rodata** (read-only data) section in Flash. This variable **takes no RAM** – the CPU reads the value directly from Flash.

Rule: a `const` global/static with a non-zero value goes to `.rodata`. This is critical in embedded: declare constants as `const` to avoid wasting RAM.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
