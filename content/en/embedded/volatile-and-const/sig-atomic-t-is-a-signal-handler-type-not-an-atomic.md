---
id: emb-volconst-0044
title: "Trap: does `volatile sig_atomic_t` give the same guarantees as a hardware atomic?"
description: "volatile sig_atomic_t is a specific portable C pattern for signal handlers, not a general embedded atomic primitive."
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

<span class="warn">No. `volatile sig_atomic_t` has a narrow C guarantee for signal handling; it is not a universal atomic primitive for MCU ISRs.</span>[^iso-c-n1570]

In C, `sig_atomic_t` is intended for atomic access in the signal-handling context. This does not make an arbitrary `volatile` type on an MCU atomic, or establish memory ordering between an ISR and main code.

On an MCU, check atomic access width in the CPU and ABI documentation; protect more complex communication with supported atomic operations or critical sections.[^iso-c-n1570]

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
