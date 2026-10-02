---
id: emb-dtypes-0028
title: "Where do these live in `.bss`, `.data`, and the stack: `int g1; int g2 = 5; void f(){int l=3;}`?"
description: "The uninitialized global goes to .bss, the initialized one to .data, and the function-local variable to the stack."
track: embedded
section: data-types-and-memory-layout
level: junior
type: mechanism
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

`int g1;` has static storage duration and is typically placed in **.bss**, with value zero before execution.

`int g2 = 5;` is typically in **.data** RAM; startup code loads its initial value, often from Flash.

`int l = 3;` has automatic storage duration; a typical implementation stores it on the **stack**, though the compiler may keep it in a register or optimize it away.

Machine code for `f()` is typically in `.text`, often mapped to Flash. C does not specify these sections or physical locations.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
