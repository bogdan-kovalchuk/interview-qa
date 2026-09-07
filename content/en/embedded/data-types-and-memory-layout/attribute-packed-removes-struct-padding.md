---
id: emb-dtypes-0025
title: "How does `__attribute__((packed))` affect `struct { char a; int b; char c; };`?"
description: "attribute((packed)) removes padding to shrink the struct, but can trigger misaligned access."
track: embedded
section: data-types-and-memory-layout
level: middle
type: mechanism
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

Without packed: `a`@0 + 3B padding + `b`@4 + `c`@8 + 3B trailing = **12 bytes**.

With `__attribute__((packed))`: `a`@0 + `b`@1 + `c`@5 = **6 bytes**. No padding.

<span class="warn">But!</span> On Cortex-M0/M0+ access to misaligned `int b` (offset 1) -> <span class="warn">HardFault</span>; on M3/M4 – slower; packed is useful for serial protocols, but not for direct field access on MCU.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
