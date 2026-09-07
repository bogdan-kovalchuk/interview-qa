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

**Tentative definition** – a declaration of a global variable without an initializer and without `extern`: `int x;` at file scope.

Per the C rules: if there is no other definition in the same translation unit, it automatically becomes a zero-initialized definition -> placed in **.bss** or a common section depending on the compiler/flags. If the same translation unit has `int x = 5;`, the tentative definition merges with that definition. If `int x;` is placed in a header and included in multiple `.c` files, modern GCC with `-fno-common` will give a multiple definition error; for an external variable in a header, use `extern int x;`.

<span class="warn">C++ has no tentative definitions</span> – every declaration is either `extern` or a definition (ODR).[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
