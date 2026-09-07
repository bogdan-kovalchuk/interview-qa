---
id: emb-dtypes-0070
title: "What does this return on 32-bit? `sizeof(struct { char a; char b; int c; })`"
description: "The compiler adds 2 bytes of padding before the int, so struct { char; char; int; } takes 8 bytes."
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

**8 bytes**.

Layout: `a`@0 (1B) + `b`@1 (1B) + <span class="warn">2B padding</span> + `c`@4 (4B). Trailing padding = 0.

If the fields were in a different order: `struct { char a; int c; char b; }` -> 12 bytes (3B padding after `a`, 3B trailing).

Rule: arrange fields from largest alignment to smallest for minimum sizeof.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
