---
id: emb-dtypes-0047
title: "What is signed integer overflow in C, and what does the standard say about it?"
description: "A signed int going out of range is undefined behavior under the C standard, not a guaranteed wraparound."
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

Going out of the `INT_MIN..INT_MAX` range is <span class="warn">undefined behavior</span> under the C standard (§6.5).

The compiler may:
1. Wrap around to `INT_MIN` (typical two's complement);
2. Remove conditional code as "always false";
3. Infinite loop: `for(int i=0; i < i+1; i++)` – UB, the compiler may optimize it away.

For defined wraparound: `uint32_t`. Check: `if(x <= INT_MAX - y) x += y;`[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
