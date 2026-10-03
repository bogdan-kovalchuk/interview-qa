---
id: emb-volconst-0004
title: "Trap: does `volatile` make an operation atomic?"
description: "No, volatile does not guarantee atomicity; it only forces the compiler to perform a memory access."
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
  - source_id: gcc-volatile
    title: "GCC documentation: When is a Volatile Object Accessed?"
    url: https://gcc.gnu.org/onlinedocs/gcc/Volatiles.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "GCC volatile-access behavior and the lack of a memory-barrier guarantee; other compilers can differ."
---

## Short answer

<span class="warn">No. `volatile` does not guarantee atomicity.</span> For example, a `volatile uint32_t` on an 8-bit MCU may be read in several instructions, and an ISR can fire between them; even if a single `counter` read is atomic on a particular Cortex-M, `counter++` consists of a read, computation, and write.

Mitigation: for shared state use atomic operations, a critical section, or platform primitives chosen for the required guarantee.[^iso-c-n1570]

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
