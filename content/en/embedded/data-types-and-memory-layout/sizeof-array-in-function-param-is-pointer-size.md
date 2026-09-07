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

When passing an array to a function: `void f(int arr[]) { int n = sizeof(arr)/sizeof(arr[0]); }`

Here `arr` is not an array but a <span class="warn">pointer</span> to the first element (`int*`). `sizeof(arr) = sizeof(int*) = 4 or 8`. The result is wrong.

Correct: pass the size explicitly or use `sizeof` only for arrays in the same scope where they are declared. In C++: `std::array` or `std::span`.[^embeddedinterviewlab]

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
