---
id: emb-volconst-0053
title: "Why is `volatile uint32_t counter; counter++;` unsafe for an ISR-shared counter?"
description: "counter++ is a read-modify-write, not an atomic operation."
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

<span class="warn">`counter++` reads, computes, and writes; `volatile` does not make that sequence atomic.</span>[^iso-c-n1570]

The expression `counter++` must read the value, compute a new one, and write it. If an interrupt can occur between these steps and modify the same counter, an update can be lost. The exact access rules for an ISR-shared object depend on the implementation and platform.[^iso-c-n1570]

Defense: use a critical section that covers both contexts, or an atomic operation supported by the platform.[^iso-c-n1570]

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
