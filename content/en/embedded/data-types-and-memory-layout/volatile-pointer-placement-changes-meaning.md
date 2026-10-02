---
id: emb-dtypes-0046
title: "What's the difference: `volatile int *reg` vs `int * volatile reg`?"
description: "volatile int *reg qualifies the pointed-to data, while int * volatile reg qualifies the pointer itself."
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

`volatile int *reg` points to a `volatile int`, while `int * volatile reg` makes the pointer itself volatile; registers usually need the pointed-to type qualified. `volatile` requires accesses to be handled according to the C abstract machine, but does not by itself guarantee a physical bus transaction for every expression, atomicity, or synchronization.[^iso-c-n1570]

For example, `volatile uint32_t * const GPIOA` is a fixed pointer to a volatile object; the correct type and access rules depend on the MCU's register map.[^iso-c-n1570]

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
