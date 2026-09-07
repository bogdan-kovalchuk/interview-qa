---
id: emb-dtypes-0024
title: "What is padding in structs, and where does it come from?"
description: "Padding is the bytes the compiler inserts between struct fields to satisfy alignment requirements."
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

**Padding** – unused bytes the compiler inserts between fields (or at the end) of a struct to satisfy alignment requirements.

Rule: a field of type T is placed at an address divisible by `alignof(T)`.

Example: `struct { char c; int x; }` – after `char` (1B) the compiler adds 3B of padding so that `int` is at offset 4.

Struct size is always a multiple of the alignment of its largest field.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
