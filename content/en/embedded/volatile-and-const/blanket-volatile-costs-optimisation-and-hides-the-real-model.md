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

<span class="warn">Excessive `volatile` degrades optimization and can mask an incorrect synchronization model.</span>

For volatile-qualified objects, the compiler must account for volatile accesses under its implementation's rules, which can limit some optimizations. The cost depends on the compiler and target; volatile does not define general ordering for non-volatile data and does not fix race conditions or atomicity problems.

Rule: use `volatile` as a precise contract for hardware/ISR/DMA observable state, not as a general anti-optimization incantation.[^iso-c-n1570]

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
