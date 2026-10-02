---
id: emb-dtypes-0021
title: "Trap: what is actually being compared? `uint8_t a = 200, b = 100; if(a + b > 250)`"
description: "Integer promotion makes a + b an int before comparison; assigning the sum to uint8_t converts 300 to 44."
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

`a + b` is promoted to `int`: the result is `300` of type `int`. Therefore `300 > 250` is true. If the sum is first assigned to `uint8_t result`, conversion yields `44`, so `result > 250` is false. Integer promotion happens before the operation; conversion to the narrower type happens at assignment.[^iso-c-n1570][^embeddedinterviewlab]

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
