---
id: emb-cppfound-0042
title: "What is the difference between an array of pointers `int *arr[8]` and a pointer to an array `int (*arr)[8]`?"
description: "How array-of-pointers and pointer-to-array declarations differ."
track: embedded
section: c-in-embedded
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 4
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
    applicability: "Origin of the question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for c in embedded concepts; details of specific devices and toolchains can differ."
---

## Short answer

`int *arr[8]` is an **array of 8 pointers** to int. Size: 8 × 4 = 32 bytes. Each element is a separate address and can point to different arrays of different sizes.

`int (*arr)[8]` is a **pointer to an array** of 8 int; the size of `arr` itself = 4 bytes (a pointer); `arr+1` -> +32 bytes (the size of an array of 8 int).

Operator precedence: `[]` binds tighter than `*`, which is why parentheses are needed.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
