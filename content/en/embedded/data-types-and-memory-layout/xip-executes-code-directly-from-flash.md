---
id: emb-dtypes-0064
title: "What is XIP (Execute in Place) in embedded systems?"
description: "XIP means the CPU executes code directly from Flash without first copying it into RAM."
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

**XIP** (Execute in Place) is a mode where the CPU executes code directly from Flash without copying into RAM.

NOR Flash supports random byte access -> the CPU can address and execute instructions directly. Most Cortex-M MCUs use XIP by default.

**Advantages**: no RAM spent on code, shorter boot time. <span class="warn">Disadvantage</span>: Flash is slower (wait states); for time-critical ISRs: `__attribute__((section(".ramcode")))`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
