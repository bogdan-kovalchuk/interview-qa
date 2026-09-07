---
id: emb-dtypes-0071
title: "Trap: infinite loop? `uint8_t i; for(i = 255; i >= 0; i--)`"
description: "uint8t can never be negative, so i = 0 is always true and the loop never terminates."
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

<span class="warn">Yes, an infinite loop!</span> Just like `i >= 0` for unsigned: `uint8_t` can never be negative.

When `i = 0` -> `i--` -> `i = 255` (wraparound) -> `255 >= 0` -> true. The loop never terminates.

Fix: `for(int i = 255; i >= 0; i--)`; GCC with `-Wtype-limits` will warn about unsigned comparison against zero.[^embeddedinterviewlab]

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
