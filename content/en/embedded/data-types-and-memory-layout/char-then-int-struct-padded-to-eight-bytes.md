---
id: emb-dtypes-0010
title: "What size does this have on a 32-bit Cortex-M? `struct { char c; int x; };`"
description: "The compiler inserts padding before the int, so struct { char; int; } takes 8 bytes, not 5."
track: embedded
section: data-types-and-memory-layout
level: middle
type: mechanism
tags: []
status: published
updated: 2026-09-07
content_revision: 3
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

**8 bytes** (not 5!).

Layout: `char c` @ offset 0 (1B) -> <span class="warn">3 bytes of padding</span> -> `int x` @ offset 4 (4B). Trailing padding = 0.

Padding is inserted so that `int` sits at an address divisible by 4 (alignment requirement). Check: `offsetof(s, x) == 4`; always use `sizeof()` and `offsetof()` to analyze layout.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
