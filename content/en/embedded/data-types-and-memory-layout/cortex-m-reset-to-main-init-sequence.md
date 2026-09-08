---
id: emb-dtypes-0007
title: "What is the C runtime init sequence before `main()` on Cortex-M?"
description: "The hardware reads the vector table, copies .data, zeroes .bss, and only then calls main()."
track: embedded
section: data-types-and-memory-layout
level: middle
type: mechanism
tags: []
status: published
updated: 2026-09-08
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
    applicability: "Origin of the question and answer; the answer is not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for data types and memory layout concepts; details of specific devices and toolchains can differ."
---

## Short answer

The hardware reads the Vector Table: SP receives the value at address `0x00000000`, while PC receives the Reset Handler address from `0x00000004`. Startup code copies `.data` from Flash (LMA) to RAM (VMA), zeroes `.bss`, calls global C++ constructors (if any), and finally `main()`.

Local variables in `main()` live on the stack and are <span class="warn">not initialized</span>.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
