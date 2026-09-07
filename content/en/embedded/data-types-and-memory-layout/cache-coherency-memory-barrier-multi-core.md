---
id: emb-dtypes-0106
title: "What are cache coherency and memory barrier in a multi-core MCU, MPU, or Embedded Linux system?"
description: "Cache coherency means data consistency between CPU caches, DMA, and peripheral views; a memory barrier enforces operation order, and DMA often needs cache clean/invalidate to avoid stale data."
track: embedded
section: data-types-and-memory-layout
level: senior
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

**Cache coherency** means consistency of data between CPU caches, DMA, and peripheral views of memory. A **memory barrier** enforces the order of memory operations so that the CPU/compiler does not reorder critical accesses. <span class="warn">For DMA, cache clean/invalidate and barriers are often required, otherwise the device or CPU sees stale data.</span>[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
