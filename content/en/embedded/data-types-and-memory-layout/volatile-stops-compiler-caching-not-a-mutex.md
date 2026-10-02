---
id: emb-dtypes-0082
title: "What is `volatile`, and how does it interact with compiler optimization?"
description: "volatile forbids caching or eliding accesses to a variable, but gives no atomicity or ordering across threads."
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
  - source_id: gcc-volatiles
    title: "GCC documentation: Volatiles"
    url: https://gcc.gnu.org/onlinedocs/gcc/Volatiles.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Describes GCC volatile access rules, including limits on ordering ordinary memory; it is not a substitute for thread synchronization."
---

## Short answer

`volatile` marks accesses that the implementation must treat as volatile; in embedded code this is commonly needed for memory-mapped registers or values changed outside the ordinary flow of execution.[^iso-c-n1570] [^gcc-volatiles]

Without volatile accesses, the compiler may optimize repeated reads or writes of an ordinary variable when the language rules say its value cannot observably change.[^gcc-volatiles]

<span class="warn">volatile is not synchronization</span>: it does not provide atomicity or create inter-thread happens-before. For shared C++ thread state, use `std::atomic` or a mutex suited to the required protocol.[^gcc-volatiles] [^iso-c-n1570]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
