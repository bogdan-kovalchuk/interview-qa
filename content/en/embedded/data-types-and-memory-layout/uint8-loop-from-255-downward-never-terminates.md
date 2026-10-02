---
id: emb-dtypes-0071
title: "Trap: infinite loop? `uint8_t i; for(i = 255; i >= 0; i--)`"
description: "A `uint8_t` counter returns to 255 after decrementing zero, so the loop does not terminate."
track: embedded
section: data-types-and-memory-layout
level: middle
type: pitfall
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

<span class="warn">The loop does not terminate.</span> After integer promotion, the comparison is performed as `int`, but after decrementing zero the value is stored back in `uint8_t` as 255.[^iso-c-n1570]

When `i == 0`, `i--` computes `-1` as an `int`; assigning it back to `uint8_t` yields 255, so the next condition is true.[^iso-c-n1570]

For an inclusive countdown from 255 to 0, use a signed type that can hold both bounds, such as `int`, or stop an unsigned counter before decrementing zero.[^iso-c-n1570]

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
