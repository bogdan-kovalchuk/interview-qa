---
id: emb-volconst-0044
title: "Trap: does `volatile sig_atomic_t` give the same guarantees as a hardware atomic?"
description: "volatile sigatomict is a specific portable C pattern for signal handlers, not a general embedded atomic primitive."
track: embedded
section: volatile-and-const
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  uk: 1
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
---

## Short answer

<span class="warn">No. This is a specific portable C pattern for signal handlers, not a general embedded atomic primitive.</span>

`sig_atomic_t` guarantees safe access in the context of a C signal handler within the standard library, but this does not mean that any volatile type on an MCU is atomic or has memory ordering. For bare-metal ISRs, you need to look at bus width, CPU instructions, and the ABI.

Protection: for Cortex-M shared ISR data, use types that are atomically read and written on that architecture, or critical sections.[^embeddedinterviewlab]

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
