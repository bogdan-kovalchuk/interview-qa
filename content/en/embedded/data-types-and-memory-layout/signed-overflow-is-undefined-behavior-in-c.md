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
updated: 2026-10-04
content_revision: 3
reconciled_with:
  uk: 3
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-04; this source is not proof of the claims."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for data types and memory layout concepts; details of specific devices and toolchains can differ."
---

## Short answer

If the result of signed integer arithmetic is not representable in the result type, C defines the behavior as <span class="warn">undefined behavior</span>; two's complement does not make wraparound guaranteed. Use an unsigned type for defined modular arithmetic, and check a condition such as `x <= INT_MAX - y` before addition when `y >= 0`.[^iso-c-n1570]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
