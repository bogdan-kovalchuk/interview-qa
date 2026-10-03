---
id: emb-volconst-0011
title: "Trap: why is `uint32_t * volatile reg` the wrong type for hardware register data?"
description: "volatile is applied to the pointer variable, not to the data at the address, so register reads can still be optimized away."
track: embedded
section: volatile-and-const
level: junior
type: pitfall
tags: []
status: published
updated: 2026-10-04
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
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-04; this source is not proof of the claims."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
---

## Short answer

<span class="warn">`volatile` applies to the pointer variable, not to the data at the address.</span>

`volatile` qualifies accesses to the pointer variable itself, while `*reg` still has the plain type `uint32_t`. Therefore access to the register data is not volatile-qualified and does not get volatile access semantics.[^iso-c-n1570]

Fix: use `volatile uint32_t *reg` for a pointer to volatile data, or `volatile uint32_t * const reg` if the address is fixed.[^iso-c-n1570]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
