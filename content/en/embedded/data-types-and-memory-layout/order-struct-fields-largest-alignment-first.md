---
id: emb-dtypes-0084
title: "Why is it recommended to order struct fields from largest to smallest?"
description: "Ordering fields from largest alignment to smallest minimizes a struct's internal padding."
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

Ordering from largest alignment to smallest **minimizes internal padding**.

Bad order: `struct { char a; int b; char c; }` -> 12B (3B + 3B padding).
Good order: `struct { int b; char a; char c; }` -> 8B (no internal padding).

Rule: first `uint64_t`/`double` (align 8), then `uint32_t`/`float` (align 4), then `uint16_t` (align 2), finally `uint8_t`/`char` (align 1). Verify with `sizeof()`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
