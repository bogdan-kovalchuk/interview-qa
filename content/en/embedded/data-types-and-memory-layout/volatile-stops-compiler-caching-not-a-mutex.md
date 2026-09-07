---
id: emb-dtypes-0082
title: "What is `volatile`, and how does it interact with compiler optimization?"
description: "volatile forbids caching or eliding accesses to a variable, but gives no atomicity or ordering across threads."
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

`volatile` tells the compiler that the value can change **outside its control** (hardware, ISR, multi-threading).

Without `volatile` the compiler may:
1. Cache the value in a register (not re-read it);
2. Eliminate "unnecessary" reads/writes as dead code;
3. Reorder operations.

<span class="warn">volatile is NOT synchronization</span>: it does not guarantee atomicity or memory ordering across threads. For threads – use `std::atomic` or `mutex`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
