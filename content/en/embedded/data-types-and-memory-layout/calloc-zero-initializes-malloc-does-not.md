---
id: emb-dtypes-0060
title: "How does `calloc` differ from `malloc` when it comes to initializing memory?"
description: "malloc allocates memory without initializing it, while calloc allocates and zero-fills it."
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

`malloc(size)` allocates `size` bytes without initializing them, while `calloc(n, size)` allocates an array of `n` elements of `size` bytes each and sets all bytes to zero; zero bytes are not necessarily the semantic zero for every type.[^iso-c-n1570]

Both functions return `NULL` if allocation fails. Check the result before using it, and explicitly initialize elements to the values the program requires.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
