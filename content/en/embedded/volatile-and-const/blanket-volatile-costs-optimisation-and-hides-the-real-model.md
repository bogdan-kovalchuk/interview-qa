---
id: emb-volconst-0060
title: "Why should `volatile` not be put on every variable just in case?"
description: "Excessive volatile degrades optimization and can mask an incorrect synchronization model."
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

<span class="warn">Excessive `volatile` degrades optimization and can mask an incorrect synchronization model.</span>

The compiler is forced to go to memory more often, not keep values in registers, and limit reordering. This increases code size, execution time, and power consumption. At the same time it does not fix race conditions, atomicity, or ordering for non-volatile data.

Rule: use `volatile` as a precise contract for hardware/ISR/DMA observable state, not as a general anti-optimization incantation.[^embeddedinterviewlab]

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
