---
id: emb-dtypes-0079
title: "What does the `register` storage class mean, and does it still matter today?"
description: "Modern compilers ignore register as a hint; the only remaining effect is forbidding taking that variable's address."
track: embedded
section: data-types-and-memory-layout
level: junior
type: concept
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

`register` – a hint to the compiler to store the variable in a CPU register. In modern compilers (GCC, Clang with `-O2`+) – <span class="warn">ignored</span>: the compiler allocates registers optimally on its own.

The only remaining effect: **forbids taking the address** of the variable (`&reg_var` – compilation error).

In C++17 – deprecated. In C11 retained for compatibility; do not use in new projects – trust register allocation to the compiler.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
