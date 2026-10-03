---
id: emb-volconst-0052
title: "What does `volatile` mean for shared data in C: is it a replacement for a mutex or an atomic?"
description: "No, volatile does not replace a mutex, an atomic, or RTOS synchronization."
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

<span class="warn">No. `volatile` does not replace a mutex, an atomic, or RTOS synchronization.</span>

In C, `volatile` applies to accesses to volatile-qualified objects, but does not itself create a synchronizes-with relation between threads. C11 provides atomic operations for shared data between threads; an RTOS may also define its own synchronization mechanisms.[^iso-c-n1570]

Rule: use `volatile` when required by implementation rules for externally changed objects, and synchronization primitives for thread synchronization.[^iso-c-n1570]

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
