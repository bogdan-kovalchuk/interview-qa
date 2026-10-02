---
id: emb-dtypes-0017
title: "How does a `static` local variable differ from a plain local one?"
description: "A plain local lives on the stack and dies with the call; a static local lives in static memory for the program's lifetime."
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

**Plain local** has automatic storage duration: it exists during its block, has an indeterminate value without initialization, and need not be stored on a stack.[^iso-c-n1570]

**Static local** has static storage duration: it exists for the program's execution and is zero-initialized if no explicit initializer is provided. It retains its value between entries to the block; `.bss` and `.data` are typical implementation sections, not language requirements.[^iso-c-n1570]

Shared mutable `static` state can break reentrancy or cause a data race, but the keyword alone does not make a function unsafe for threads.[^iso-c-n1570]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
