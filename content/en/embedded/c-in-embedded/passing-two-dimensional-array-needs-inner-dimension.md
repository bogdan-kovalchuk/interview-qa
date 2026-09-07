---
id: emb-cppfound-0029
title: "How should a 2D array be passed to a function to access element `[2][3]`?"
description: "A 2D array parameter must declare the inner dimension so the compiler can compute the row stride for element access."
track: embedded
section: c-in-embedded
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-07
content_revision: 3
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
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for c in embedded concepts; details of specific devices and toolchains can differ."
---

## Short answer

For a statically sized array you must specify the **inner dimension size**: `void f(int arr[][4], int rows) { arr[2][3] = 99; }` or equivalently: `void f(int (*arr)[4], int rows) { ... }`

Without the size the compiler does not know the row stride. `arr[i][j]` -> `*(*(arr+i)+j)` -> in memory: `arr + i*4*sizeof(int) + j*sizeof(int)`.

For a dynamic one: pass as `int *` and compute the offset manually.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
