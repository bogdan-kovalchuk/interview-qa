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

`malloc(size)` allocates `size` bytes and <span class="warn">does NOT initialize</span> (garbage), while `calloc(n, size)` allocates `n × size` bytes and **zero-fills them**, additionally checking for product overflow.

Both return `NULL` on error. In embedded, prefer static allocation; if using the heap, `calloc` is safer for structs that need zero initialization.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
