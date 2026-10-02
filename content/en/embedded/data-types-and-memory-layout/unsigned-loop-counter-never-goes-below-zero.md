---
id: emb-dtypes-0011
title: "Trap: what happens? `for(uint8_t i = 10; i >= 0; i--)`"
description: "Integer promotion makes i >= 0 true for every uint8_t value, so this decrementing loop does not end."
track: embedded
section: data-types-and-memory-layout
level: middle
type: pitfall
tags: []
status: published
updated: 2026-10-04
content_revision: 4
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

<span class="warn">Infinite loop!</span> In `i >= 0`, `uint8_t` undergoes integer promotion to `int`, so the comparison is always true.

After the loop body, decrementing `i` converts the result back to `uint8_t`; decrementing zero wraps to `UINT8_MAX` (255 for an 8-bit type).

To finish the loop, check `i == 0` before decrementing or use a signed type that holds the full range.[^iso-c-n1570]

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
