---
id: emb-dtypes-0090
title: "What does this print on little-endian? `uint32_t x = 0xDEADBEEF; uint8_t *p = (uint8_t*)&x; printf(\"%02X\", p[0]);`"
description: "On little-endian the least-significant byte sits at the lowest address, so `p[0]` gives EF."
track: embedded
section: data-types-and-memory-layout
level: middle
type: mechanism
tags: []
status: published
updated: 2026-09-06
content_revision: 1
reconciled_with:
  uk: 1
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
---

## Short answer

TODO

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
