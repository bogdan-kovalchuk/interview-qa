---
id: emb-dtypes-0011
title: "Trap: what happens? `for(uint8_t i = 10; i >= 0; i--)`"
description: "uint8t is unsigned, so i = 0 is always true and the decrementing loop never ends."
track: embedded
section: data-types-and-memory-layout
level: middle
type: pitfall
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

<span class="warn">Infinite loop!</span> `uint8_t` is an unsigned type, so `i >= 0` is always `true`.

When `i` reaches `0` and `i--` executes -> the value becomes `255` (wraparound), not `-1`.

Fix: `for(int i = 10; i >= 0; i--)` or `do { ... } while(i-- > 0);`. GCC with `-Wtype-limits` will warn about this.[^embeddedinterviewlab]

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
