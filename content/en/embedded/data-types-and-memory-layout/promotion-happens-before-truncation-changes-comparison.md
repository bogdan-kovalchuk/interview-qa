---
id: emb-dtypes-0021
title: "Trap: what is actually being compared? `uint8_t a = 200, b = 100; if(a + b > 250)`"
description: "The intermediate a + b is computed as int, so comparing 300250 differs from comparing the truncated uint8t result."
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

`a + b` is promoted to `int`: the result is `300` of type `int`. Comparison `300 > 250` -> `true`.

But: `uint8_t result = a + b; if(result > 250)` -> result = 44, condition `false`!

<span class="warn">Same expression – different result</span> depending on where the intermediate value is stored. Promotion happens before the operation; assignment truncates.[^embeddedinterviewlab]

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
