---
id: emb-dtypes-0033
title: "What does a stack frame hold on a function call?"
description: "A stack frame holds saved registers, the return address, local variables, and alignment padding."
track: embedded
section: data-types-and-memory-layout
level: middle
type: mechanism
tags: []
status: published
updated: 2026-09-07
content_revision: 2
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

Stack frame contains:
1. **Saved registers** (callee-saved per ABI: r4–r11 on ARM);
2. **Return address** (LR, or pushed onto the stack);
3. **Local variables** of the function;
4. Padding for alignment (Cortex-M: 8-byte aligned).

On an exception (ISR): hardware automatically pushes xPSR, PC, LR, R12, R3–R0. Therefore deep ISR nesting -> large stack.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
