---
id: emb-dtypes-0094
title: "What is a tentative definition in C, and where does it end up?"
description: "A global declared without an initializer or extern becomes a zero-initialized definition in .bss."
track: embedded
section: data-types-and-memory-layout
level: middle
type: concept
tags: []
status: published
updated: 2026-09-13
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

**Tentative definition** – a global declared without an initializer and without `extern`: `int x;` at file scope.

If no other definition exists in that translation unit it becomes a zero-initialized definition -> **.bss** or a common section, depending on compiler and flags; with `int x = 5;` present, the two merge. In a header included by several `.c` files, modern GCC with `-fno-common` reports a multiple definition error; declare external variables as `extern int x;`.

<span class="warn">C++ has no tentative definitions</span> – every declaration is either `extern` or a definition (ODR).[^embeddedinterviewlab]
## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
