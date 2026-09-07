---
id: emb-dtypes-0091
title: "Trap: what happens under the C standard? `int x = INT_MAX; x++;`"
description: "Overflowing a signed int past INTMAX is undefined behavior, not a guaranteed wrap to INTMIN."
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

<span class="warn">Signed integer overflow -> undefined behavior</span> (C §6.5).

The compiler may:
1. Wrap around to `INT_MIN` (typical on x86/ARM two's complement);
2. Optimize code in unexpected ways (e.g., remove conditional guard code);
3. Produce an infinite loop in certain patterns.

For defined wraparound: `uint32_t x = UINT32_MAX; x++;` -> `0`.
Check: `if(x < INT_MAX) x++;`[^embeddedinterviewlab]

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
