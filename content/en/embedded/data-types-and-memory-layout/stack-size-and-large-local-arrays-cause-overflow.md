---
id: emb-dtypes-0042
title: "What are typical Cortex-M stack sizes, and the most common cause of stack overflow?"
description: "A typical Cortex-M stack is a few KB, and the most common overflow cause is large local arrays."
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
---

## Short answer

There is no fixed Cortex-M stack size: the memory layout, linker script, and system requirements determine it.

Large automatic arrays, such as `uint8_t buf[2048]`, can substantially increase a function’s stack requirement; actual placement is implementation-dependent.

Assess stack use across the full call depth and nested ISRs, using the configuration for the specific linker script.[^iso-c-n1570]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
