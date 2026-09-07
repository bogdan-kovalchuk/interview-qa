---
id: emb-dtypes-0066
title: "Trap: what is the danger of `double` on embedded without an FPU?"
description: "Without a hardware FPU, double runs in software emulation, taking tens of times more cycles."
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

MCUs without an FPU (Cortex-M0/M0+/M3) execute `double` in <span class="warn">software emulation</span>: tens to hundreds of cycles instead of 1–2 for a hardware FPU.

Problems:
1. Increased execution time -> RTOS deadline missed;
2. Increased code size (soft-float library);
3. `double` = 8B, twice as much RAM/stack.

Cortex-M4F/M7 has an FPU only for `float` (32-bit). Always: use `float` instead of `double` in embedded. Check the ABI: `-mfloat-abi=hard -mfpu=fpv4-sp-d16`.[^embeddedinterviewlab]

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
