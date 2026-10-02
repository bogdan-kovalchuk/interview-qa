---
id: emb-dtypes-0036
title: "Trap: where does the `sizeof(arr)/sizeof(arr[0])` trick fail?"
description: "An array passed to a function decays to a pointer, so sizeof(arr) there gives the pointer's size, not the array's."
track: embedded
section: data-types-and-memory-layout
level: middle
type: pitfall
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

In a function parameter, `int arr[]` is adjusted to `int *arr`, so `sizeof(arr)` gives the pointer size, not the array size; its exact value is implementation-dependent.[^iso-c-n1570] Dividing by `sizeof(arr[0])` does not recover the element count. Pass the length separately or use a container that retains it, such as `std::array` or `std::span` in C++.[^iso-c-n1570]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
