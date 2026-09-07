---
id: emb-dtypes-0026
title: "Why can't you rely on `sizeof(int)` in network/serial protocols?"
description: "sizeof(int) is platform-dependent, so protocols must use fixed-width types like uint16t instead."
track: embedded
section: data-types-and-memory-layout
level: middle
type: pitfall
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

`sizeof(int)` depends on the platform and ABI: 2 bytes on MSP430/8051, 4 bytes on Cortex-M/x86.

If device A sends an `int` as 2 bytes and device B reads it as 4 bytes -> the packet is misinterpreted.

**Solution**: always use `uint16_t`, `int32_t`, etc. Also check endianness between devices and document byte order in the protocol.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
