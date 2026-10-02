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
  - source_id: arm-cortex-m3
    title: "Arm Cortex-M3 Technical Reference Manual"
    url: https://documentation-service.arm.com/static/6036810d5319e554d4ba108e
    accessed: 2026-10-04
    kind: official
    version: "DDI 0337E"
    applicability: "Documents Flash wait-state effects on Cortex-M3; it does not establish that every MCU supports XIP or has identical memory."
---

## Short answer

**XIP** (Execute in Place) is a mode where the processor executes code directly from the memory holding the image, without first copying that code into RAM.[^arm-cortex-m3] The memory and controller must provide an executable address space; support and placement depend on the MCU.[^arm-cortex-m3]

XIP reduces the RAM needed for code, but does not by itself guarantee faster startup or execution. Flash wait states, prefetch, and cache can affect fetch time, so critical routines are sometimes placed in RAM through the linker script and startup code.[^arm-cortex-m3]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
