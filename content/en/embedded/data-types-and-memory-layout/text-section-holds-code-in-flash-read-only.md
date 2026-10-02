---
id: emb-dtypes-0001
title: "What is the `.text` section in an embedded program's memory?"
description: "In a typical embedded linker script, .text holds executable instructions; placement and protection depend on the target and link layout."
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
  - source_id: embedded-ld-layout
    title: "GNU ld documentation: linker scripts and output section LMA"
    url: https://sourceware.org/binutils/docs/ld/Output-Section-LMA.html
    accessed: 2026-10-04
    kind: official
    version: "Binutils 2.47"
    applicability: "GNU ld linker scripts describe output section layout and address mapping; exact placement and execution remain target-specific."
---

## Short answer

In a typical embedded linker script, `.text` contains executable instructions; its address and access permissions are determined by the target's link layout. Code often runs from Flash, but XIP, copying to RAM, and write protection depend on the MCU and configuration. The name `.text` alone does not guarantee a HardFault on a write attempt.[^embedded-ld-layout]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
